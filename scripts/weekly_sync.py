#!/usr/bin/env python3
"""Weekly sync orchestrator: detect, fetch, summarize, validate, commit.

Three phases share one JSON report/state file (never parsed from human text):

  prepare    detect unseen videos (newest first), select the first distinct
             unseen ID, queue the rest as metadata-only `pending`, fetch the
             selected video's captions (complete fetch result or nothing).
  summarize  Gemini-summarize the selected video. The only phase that reads
             GEMINI_API_KEY; it is removed from the environment immediately.
             A failed or invalid generation restores the prior summary
             byte-for-byte and marks it stale (validate_summaries --mark-stale).
  finalize   validate every summary through the per-video API, run the unit
             tests, stage an explicit allowlist, commit, fetch+rebase onto the
             remote head, re-gate the combined tree, and push (never forced).

`all` runs the three phases in order. Exit codes of finalize: 0 clean; 1 safe
progress may exist but the run is red (validator exit 1, generation/fetch
failure, push rejected, rebase failure, duplicate video ID after rebase); 2 write
path blocked, nothing was pushed (transcript changed, unexpected validator or
finalize error, unit tests failing, restore/mark failure, missing state). A
blocked run that already committed locally (post-rebase gate failure) leaves
that commit unpushed in the runner's checkout only.

Stdlib only apart from the helpers it imports. Every collaborator is reachable
through the injectable `Deps` object so tests run offline.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import consolidate  # noqa: E402
import detect_new_videos  # noqa: E402
import fetch_transcript  # noqa: E402
import generate_index  # noqa: E402
import queue_state  # noqa: E402
import summarize  # noqa: E402
import validate_summaries  # noqa: E402

STATE_VERSION = 1
SECRET_ENV = "GEMINI_API_KEY"
TEST_COMMAND = [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
COMMIT_NAME = "github-actions[bot]"
COMMIT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"


class GenerationRejected(Exception):
    """A freshly generated summary failed validation and is not kept."""


def clean_env():
    """Environment for subprocesses: never carries the Gemini key."""
    return {k: v for k, v in os.environ.items() if k != SECRET_ENV}


def default_run_tests(repo):
    result = subprocess.run(
        TEST_COMMAND, cwd=str(repo), capture_output=True, text=True, env=clean_env()
    )
    if result.returncode != 0:
        tail = "\n".join((result.stdout + result.stderr).splitlines()[-60:])
        print(f"unit tests failed (exit {result.returncode}):\n{tail}", file=sys.stderr)
    return result.returncode == 0


class Deps:
    """Injectable seams; tests overwrite attributes."""

    def __init__(self, repo=None):
        self.repo = Path(repo or os.getcwd()).resolve()
        self.channel_ids = detect_new_videos.get_channel_video_ids
        self.known_ids = detect_new_videos.get_known_video_ids
        self.fetch_metadata = fetch_transcript.fetch_metadata
        self.fetch_one = fetch_transcript.fetch_one_video
        self.summarize = summarize.summarize_video
        self.make_client = summarize.GeminiClient
        self.validate = validate_summaries.validate_video
        self.mark_stale = self._mark_stale
        self.run_tests = lambda: default_run_tests(self.repo)
        self.generate = self._generate
        self.hook = lambda stage: None  # "before_sync" / "before_push"
        self.log = lambda message: print(message, file=sys.stderr, flush=True)

    def _mark_stale(self, videos_dir, video_id):
        return validate_summaries.main(
            ["--videos-dir", str(videos_dir), "--mark-stale", video_id]
        ) == 0

    def _generate(self, videos_dir):
        """Run both generators over published videos; True only when both succeed."""
        argv = ["--root", str(self.repo), "--videos-dir", str(videos_dir),
                "--vocabulary", str(vocabulary_path(self))]
        return generate_index.main(argv) == 0 and consolidate.main(argv) == 0

    def git(self, *args):
        return subprocess.run(
            ["git", "-c", "core.quotepath=off", "-C", str(self.repo), *args],
            capture_output=True, text=True, env=clean_env(),
        )


# --- state -----------------------------------------------------------------


def new_state(args):
    return {
        "version": STATE_VERSION,
        "channel_id": args.channel_id,
        "videos_dir": args.videos_dir,
        "selected": None,
        "unseen": [],
        "pending": [],
        "items": [],
        "notices": [],
        "failures": [],
        "fatal": [],
    }


def load_state(path):
    try:
        state = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(state, dict) or state.get("version") != STATE_VERSION:
            return None
        return state
    except (OSError, ValueError):
        return None


def save_state(path, state):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".report.", suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        json.dump(state, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(tmp, path)


def add(state, kind, message):
    state[kind].append(message)


def rel(deps, path):
    return Path(path).resolve().relative_to(deps.repo).as_posix()


def videos_path(deps, args):
    return (deps.repo / args.videos_dir).resolve()


def vocabulary_path(deps):
    return deps.repo / "topics" / "vocabulary.md"


def item_for(state, video_dir_rel):
    return next((i for i in state["items"] if i["dir"] == video_dir_rel), None)


# --- prepare ---------------------------------------------------------------


def select_unseen(channel_ids, known):
    """Distinct unseen IDs in the channel's newest-first order."""
    seen, unseen = set(), []
    for video_id in channel_ids:
        if video_id in known or video_id in seen:
            continue
        seen.add(video_id)
        unseen.append(video_id)
    return unseen


def queue_pending(deps, state, videos_dir, video_id):
    try:
        metadata = deps.fetch_metadata(video_id)
        video_dir = fetch_transcript.write_pending_metadata(
            videos_dir, metadata, expected_id=video_id
        )
    except Exception as exc:
        add(state, "failures", f"cannot queue {video_id} as pending: {exc}")
        return None
    state["items"].append({"dir": rel(deps, video_dir), "video_id": video_id, "kind": "pending",
                           "summary_candidate": False, "stale_marker": False})
    state["pending"].append(video_id)
    return video_dir


def phase_prepare(args, deps, state):
    videos_dir = videos_path(deps, args)
    try:
        channel_ids = deps.channel_ids(args.channel_id)
        known = deps.known_ids(videos_dir)
    except (Exception, SystemExit) as exc:
        add(state, "failures", f"detection failed (not an empty success): {exc}")
        return
    unseen = select_unseen(channel_ids, known)
    state["unseen"] = unseen
    if not unseen:
        add(state, "notices", "no new video: skipping fetch and Gemini; gates still run")
        return
    selected, backlog = unseen[0], unseen[1:]
    state["selected"] = selected  # chosen before any directory is created

    try:
        video_dir = deps.fetch_one(selected, videos_dir)
        video_dir = Path(video_dir)
        state["items"].append({"dir": rel(deps, video_dir), "video_id": selected, "kind": "fetched",
                               "summary_candidate": False, "stale_marker": False})
    except fetch_transcript.NoCaptionsError as exc:
        add(state, "notices",
            f"captions not ready for {selected}: left metadata-only pending; retry next run or "
            f"process locally with review_batch ({exc})")
        queue_pending(deps, state, videos_dir, selected)
    except Exception as exc:
        add(state, "failures", f"fetch failed for {selected}: {exc}")

    for video_id in backlog:
        queue_pending(deps, state, videos_dir, video_id)


# --- summarize -------------------------------------------------------------


def restore_prior(summary_path, prior):
    """Put the pre-attempt state back: prior bytes, or no summary at all."""
    if prior is None:
        summary_path.unlink(missing_ok=True)
        return
    if not summary_path.is_file() or summary_path.read_bytes() != prior:
        summary_path.write_bytes(prior)
    if summary_path.read_bytes() != prior:
        raise OSError(f"could not restore {summary_path}")


def generate_summary(deps, args, state, item, client, redact):
    """Generate one summary; on any failure restore + mark stale. Updates item/state."""
    videos_dir = videos_path(deps, args)
    video_dir = deps.repo / item["dir"]
    summary_path = video_dir / "summary.md"
    try:
        prior = summary_path.read_bytes() if summary_path.is_file() else None
    except OSError as exc:
        add(state, "fatal", f"cannot read prior summary for {item['video_id']}: {redact(str(exc))}")
        return
    vocab = vocabulary_path(deps)
    try:
        deps.summarize(video_dir, client, vocabulary_path=vocab,
                       reduce_max_chars=args.reduce_max_chars, log=deps.log)
        result = deps.validate(video_dir, vocab)
        if result["invalid"]:
            raise GenerationRejected("generated summary failed validation: "
                                     + "; ".join(result["reasons"]))
        item["summary_candidate"] = True
        return
    except validate_summaries.TranscriptChanged as exc:
        add(state, "fatal", f"transcript changed while validating {item['video_id']} ({exc})")
        return
    except summarize.DailyQuotaExhausted:
        reason = "Gemini free-tier daily quota exhausted (resets midnight Pacific)"
    except (summarize.SummarizeError, GenerationRejected) as exc:
        reason = redact(str(exc))
    except Exception as exc:  # unexpected generation error is still a safe failure path
        reason = redact(f"unexpected {type(exc).__name__}: {exc}")

    add(state, "failures", f"summary generation failed for {item['video_id']}: {reason}")
    try:
        restore_prior(summary_path, prior)
    except OSError as exc:
        add(state, "fatal", f"cannot restore prior summary for {item['video_id']}: {redact(str(exc))}")
        return
    item["summary_candidate"] = False
    if prior is None:
        return  # fetch result only (transcribed); no marker
    if not deps.mark_stale(videos_dir, item["video_id"]) or not validate_summaries.is_stale(video_dir):
        add(state, "fatal", f"cannot mark prior summary stale for {item['video_id']}")
        return
    item["stale_marker"] = True


def phase_summarize(args, deps, state):
    key = os.environ.pop(SECRET_ENV, "")
    model = os.environ.get("GEMINI_MODEL", "")

    def redact(text):
        return summarize.scrub(text, key)

    deps.log = (lambda log: lambda message: log(redact(message)))(deps.log)
    targets = [i for i in state["items"] if i["kind"] == "fetched"
               and not (deps.repo / i["dir"] / "summary.md").exists()]
    if not targets:
        return
    if not key or not model:
        add(state, "failures",
            "GEMINI_API_KEY/GEMINI_MODEL not configured: selected video stays transcribed")
        return
    client = deps.make_client(key, model)
    for item in targets:
        generate_summary(deps, args, state, item, client, redact)


# --- finalize --------------------------------------------------------------


def validate_all(deps, videos_dir):
    """Return (rc, {dir: result}, error). rc 0 ok, 1 some invalid, 2 hard failure."""
    results, rc = {}, 0
    for entry in queue_state.list_videos(videos_dir):
        name = rel(deps, entry["dir"])
        try:
            result = deps.validate(entry["dir"], vocabulary_path(deps))
        except validate_summaries.TranscriptChanged:
            return 2, results, f"transcript changed during validation of {name}"
        except Exception as exc:
            return 2, results, f"unexpected validator error for {name}: {type(exc).__name__}: {exc}"
        if not isinstance(result, dict) or "invalid" not in result:
            return 2, results, f"missing/undecodable validator result for {name}"
        results[name] = result
        if result["invalid"]:
            rc = 1
    return rc, results, None


def fetch_complete(video_dir):
    try:
        provenance = json.loads((video_dir / "raw" / "provenance.json").read_text(encoding="utf-8"))
        raw_file = provenance["raw_file"]
    except (OSError, ValueError, KeyError, TypeError):
        return None
    if not isinstance(raw_file, str) or not (video_dir / "raw" / raw_file).is_file():
        return None
    if not (video_dir / "transcript.md").is_file() or not (video_dir / "metadata.json").is_file():
        return None
    return ["metadata.json", "transcript.md", f"raw/{raw_file}", "raw/provenance.json"]


def build_allowlist(deps, state, results, failures):
    """Explicit list of repo-relative paths this run may stage."""
    paths = []
    for item in state["items"]:
        video_dir = deps.repo / item["dir"]
        names = []
        complete = True
        if item["kind"] == "pending":
            names = ["metadata.json"] if (video_dir / "metadata.json").is_file() else []
        elif item["kind"] == "fetched":
            names = fetch_complete(video_dir)
            if names is None:
                # Neither the fetch result nor a summary built on it may be staged.
                failures.append(f"incomplete fetch result for {item['video_id']} not staged "
                                "(its summary is not staged either)")
                names, complete = [], False
            names = list(names)
        result = results.get(item["dir"], {})
        if complete and item.get("summary_candidate") and (video_dir / "summary.md").is_file() \
                and not result.get("invalid", True):
            names.append("summary.md")
        if item.get("stale_marker") and (video_dir / validate_summaries.STALE_FILE).is_file():
            names.append(validate_summaries.STALE_FILE)
        paths.extend(f"{item['dir']}/{n}" for n in names)
    return sorted(set(paths))


GENERATED_ROOTS = ["README.md", "topics", "knowledge-gpt"]
HUMAN_OWNED = {"topics/vocabulary.md"}


def generated_paths(deps):
    """Changed (incl. new/deleted) files under the generator outputs, minus human-owned ones."""
    out = deps.git("status", "--porcelain", "-z", "--untracked-files=all", "--", *GENERATED_ROOTS)
    if out.returncode != 0:
        return None
    parts, paths, i = out.stdout.split("\0"), [], 0
    while i < len(parts) and parts[i]:
        status, path = parts[i][:2], parts[i][3:]
        i += 2 if "R" in status or "C" in status else 1
        if path not in HUMAN_OWNED:
            paths.append(path)
    return sorted(paths)


def protected_changes(deps, videos_rel):
    """Tracked transcript/raw files that differ from HEAD (must never change)."""
    out = deps.git("diff", "--name-status", "-z", "--no-renames", "HEAD", "--")
    if out.returncode != 0:
        return [f"git diff failed: {out.stderr.strip()}"]
    parts = out.stdout.split("\0")
    bad = []
    for status, path in zip(parts[0::2], parts[1::2]):
        p = Path(path)
        in_videos = path.startswith(videos_rel + "/")
        if in_videos and (p.name == "transcript.md" or "raw" in p.parts) and status != "A":
            bad.append(path)
    return bad


def commit_allowlist(deps, paths, selected):
    """Stage exactly `paths`; return (committed, error)."""
    if deps.git("add", "--", *paths).returncode != 0:
        return False, "git add failed"
    staged = deps.git("diff", "--cached", "--name-only", "-z")
    names = {n for n in staged.stdout.split("\0") if n}
    extra = names - set(paths)
    if extra:
        return False, f"unexpected staged paths outside the allowlist: {sorted(extra)}"
    if not names:
        return False, None
    result = deps.git("-c", f"user.name={COMMIT_NAME}", "-c", f"user.email={COMMIT_EMAIL}",
                      "commit", "-m", "Weekly sync: update video knowledge base",
                      "-m", "Automated by scripts/weekly_sync.py: " + ", ".join(sorted(names)))
    if result.returncode != 0:
        return False, f"git commit failed: {result.stderr.strip()}"
    return True, None


def duplicate_ids(deps, videos_dir, video_ids):
    """{video_id: [dirs]} for this run's IDs that now appear in more than one directory."""
    dirs = {}
    for entry in queue_state.list_videos(videos_dir):
        if entry["video_id"] in video_ids:
            dirs.setdefault(entry["video_id"], []).append(rel(deps, entry["dir"]))
    return {vid: sorted(d) for vid, d in dirs.items() if len(d) > 1}


def gates(deps, videos_dir):
    """Validation then tests. Returns (validator_rc, results, blocked_reason|None)."""
    rc, results, error = validate_all(deps, videos_dir)
    if error:
        return rc, results, error
    if not deps.run_tests():
        return rc, results, "unit tests failed"
    return rc, results, None


def sync_and_push(args, deps, state, staged_dirs, videos_dir):
    """Rebase onto the remote head, re-gate, push. Returns (pushed, red, blocked)."""
    branch = args.branch or deps.git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if not branch or branch == "HEAD":
        return False, False, "detached HEAD: no target branch to push"
    remote = args.remote
    deps.hook("before_sync")
    ref = f"refs/remotes/{remote}/{branch}"
    fetched = deps.git("fetch", remote, f"+refs/heads/{branch}:{ref}")
    if fetched.returncode != 0:
        listing = deps.git("ls-remote", "--heads", remote, branch)
        if listing.returncode != 0 or listing.stdout.strip():
            add(state, "failures", f"fetch of {remote}/{branch} failed: {fetched.stderr.strip()}")
            return False, True, None
        ref = None  # remote branch does not exist yet
    if ref and deps.git("merge-base", "--is-ancestor", ref, "HEAD").returncode != 0:
        rebased = deps.git("-c", f"user.name={COMMIT_NAME}", "-c", f"user.email={COMMIT_EMAIL}",
                           "rebase", ref)
        if rebased.returncode != 0:
            conflicts = [p for p in deps.git(
                "diff", "--name-only", "--diff-filter=U", "-z").stdout.split("\0") if p]
            deps.git("rebase", "--abort")
            if conflicts:
                add(state, "failures",
                    f"rebase conflict on branch {branch} in {conflicts}; aborted, nothing pushed. "
                    "A human must reconcile the local push and rerun.")
            else:
                add(state, "failures",
                    f"rebase onto {remote}/{branch} failed (not a merge conflict): "
                    f"{rebased.stderr.strip()[-300:]}; aborted, nothing pushed. Fix the runner "
                    "checkout and rerun.")
            return False, True, None
        rc, results, blocked = gates(deps, videos_dir)
        if blocked:
            return False, True, f"{blocked} after rebase; not pushing"
        dupes = duplicate_ids(deps, videos_dir, {i["video_id"] for i in state["items"]})
        if dupes:
            add(state, "failures",
                f"after rebase these video IDs exist in more than one directory, not pushing: "
                f"{dupes}. A human must reconcile and rerun.")
            return False, True, None
        bad = [d for d in staged_dirs if results.get(d, {}).get("invalid", True)]
        if bad:
            add(state, "failures",
                f"after rebase these candidates are no longer valid, not pushing: {bad}")
            return False, True, None
        if rc == 1:
            add(state, "failures", "validation exit 1 on the rebased tree (pre-existing invalid summary)")
    deps.hook("before_push")
    pushed = deps.git("push", remote, f"HEAD:refs/heads/{branch}")
    if pushed.returncode != 0:
        add(state, "failures",
            f"push to {remote}/{branch} rejected (no force, no retry); rerun from the latest "
            f"branch: {pushed.stderr.strip()[-300:]}")
        return False, True, None
    return True, False, None


def phase_finalize(args, deps, state):
    """Return the exit code and fill state['report']."""
    videos_dir = videos_path(deps, args)
    videos_rel = rel(deps, videos_dir)
    report = state.setdefault("report", {})
    if state["fatal"]:
        report["status"] = "blocked: " + "; ".join(state["fatal"])
        return 2
    rc, results, error = validate_all(deps, videos_dir)
    report["validator_exit"] = rc if not error else 2
    report["videos"] = {k: {f: v.get(f) for f in ("state", "published", "invalid", "review_missing", "reasons")}
                        for k, v in results.items()}
    report["published"] = sorted(k for k, v in results.items() if v.get("published"))
    if error:
        report["status"] = f"blocked: {error}"
        return 2
    if not deps.run_tests():
        report["status"] = "blocked: unit tests failed; nothing committed or pushed"
        return 2

    failures = state["failures"]
    paths = build_allowlist(deps, state, results, failures)
    generated = []
    if rc == 0:  # generated files are published only after a clean validation gate
        found = generated_paths(deps) if deps.generate(videos_dir) else None
        if found is None:
            add(state, "failures", "index/consolidation generation failed; generated files not committed")
        else:
            generated = found
    report["generated"] = generated
    paths = sorted(set(paths) | set(generated))
    report["allowlist"] = paths
    bad = protected_changes(deps, videos_rel)
    if bad:
        report["status"] = f"blocked: existing transcript/raw artifacts changed: {bad}"
        return 2

    committed, error = commit_allowlist(deps, paths, state.get("selected")) if paths else (False, None)
    if error:
        report["status"] = f"blocked: {error}"
        deps.git("reset", "-q")
        return 2
    red = bool(failures) or rc == 1
    if committed:
        staged_dirs = sorted({str(Path(p).parent.as_posix()) for p in paths if p.endswith("summary.md")})
        pushed, push_red, blocked = sync_and_push(args, deps, state, staged_dirs, videos_dir)
        if blocked:
            add(state, "failures", blocked)
            report["status"] = f"blocked: {blocked}"
            report["pushed"] = False
            return 2
        report["pushed"] = pushed
        red = red or push_red or bool(state["failures"])
        report["commit"] = deps.git("rev-parse", "HEAD").stdout.strip()
    else:
        report["commit"] = None
        report["pushed"] = False
    report["status"] = "red" if red else "ok"
    return 1 if red else 0


# --- CLI -------------------------------------------------------------------


def print_report(state, rc):
    report = state.get("report", {})
    lines = [
        f"selected: {state.get('selected')}",
        f"unseen: {len(state.get('unseen', []))}; pending queued: {state.get('pending')}",
        f"status: {report.get('status')} (exit {rc})",
        f"commit: {report.get('commit')} pushed: {report.get('pushed')}",
        f"published: {report.get('published')}",
    ]
    lines += [f"notice: {n}" for n in state.get("notices", [])]
    lines += [f"failure: {f}" for f in state.get("failures", [])]
    lines += [f"fatal: {f}" for f in state.get("fatal", [])]
    text = "\n".join(lines)
    print(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write("### Weekly sync\n```\n" + text + "\n```\n")


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("phase", choices=["prepare", "summarize", "finalize", "all"])
    parser.add_argument("--report", required=True, help="JSON state/report file (outside the repo)")
    parser.add_argument("--videos-dir", default="videos", help="relative to the repo root")
    parser.add_argument("--channel-id", default=detect_new_videos.DEFAULT_CHANNEL_ID)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default=None, help="target branch (default: checked-out branch)")
    parser.add_argument("--reduce-max-chars", type=int, default=summarize.DEFAULT_REDUCE_MAX_CHARS)
    return parser


def main(argv=None, deps=None):
    args = build_parser().parse_args(argv)
    deps = deps or Deps()
    phases = ["prepare", "summarize", "finalize"] if args.phase == "all" else [args.phase]
    state = new_state(args) if phases[0] == "prepare" else load_state(args.report)
    if state is None:
        print("error: missing or undecodable state file; failing closed, no commit or push",
              file=sys.stderr)
        return 2
    rc = 0
    if "prepare" in phases:
        phase_prepare(args, deps, state)
        save_state(args.report, state)
    if "summarize" in phases:
        try:
            phase_summarize(args, deps, state)
        except Exception as exc:
            add(state, "fatal", f"unexpected {type(exc).__name__} in summarize phase")
            rc = 1
        save_state(args.report, state)
    if "finalize" in phases:
        try:
            rc = phase_finalize(args, deps, state)
        except Exception as exc:  # fail closed with a saved report, never a bare traceback
            add(state, "fatal", f"unexpected {type(exc).__name__} in finalize phase: {exc}")
            state.setdefault("report", {})["status"] = \
                "blocked: unexpected finalize error; nothing pushed"
            state["report"]["pushed"] = False
            rc = 2
        save_state(args.report, state)
        print_report(state, rc)
    return rc


if __name__ == "__main__":
    sys.exit(main())
