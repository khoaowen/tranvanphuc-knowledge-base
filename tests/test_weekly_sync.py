"""Offline tests for scripts/weekly_sync.py: temp Git repos with a local bare remote."""

import contextlib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "tests"))

import fetch_transcript  # noqa: E402
import summarize  # noqa: E402
import validate_summaries  # noqa: E402
import weekly_sync  # noqa: E402
from test_validate_summaries import (  # noqa: E402
    DURATION, TRANSCRIPT, VID, summary_text, write_review,
)

SECRET = "AIzaSy-weekly-sentinel-key-987"
KNOWN = VID  # the fixture's already-committed video
TITLES = {"N1": "Video mới nhất", "N2": "Video cũ hơn", "N3": "Video cũ nhất", "N4": "Video thứ tư"}
DATES = {"N1": "20260105", "N2": "20251201", "N3": "20251101", "N4": "20251001"}


def meta(video_id):
    return {
        "id": video_id, "title": TITLES[video_id], "upload_date": DATES[video_id],
        "duration": DURATION, "webpage_url": f"https://www.youtube.com/watch?v={video_id}",
    }


def sh(cwd, *args):
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, check=True).stdout


def valid_summary_for(video_id):
    return summary_text().replace(VID, video_id)


class Harness(unittest.TestCase):
    """A work clone of a bare remote plus a Deps whose network seams are fakes."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)
        self.remote = self.tmp / "remote.git"
        sh(self.tmp, "init", "--bare", "-b", "main", str(self.remote))
        self.repo = self.tmp / "work"
        self.other = self.tmp / "other"
        for clone in (self.repo, self.other):
            sh(self.tmp, "clone", "-q", str(self.remote), str(clone))
            sh(clone, "config", "user.name", "Fixture")
            sh(clone, "config", "user.email", "fixture@example.invalid")
        known = self.repo / "videos" / "2025-01-01-known"
        known.mkdir(parents=True)
        (known / "metadata.json").write_text(
            json.dumps({"video_id": KNOWN, "duration": DURATION}), encoding="utf-8")
        (known / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
        (known / "summary.md").write_text(summary_text(), encoding="utf-8")
        write_review(known)
        (self.repo / "README.md").write_text("fixture\n", encoding="utf-8")
        sh(self.repo, "add", "-A")
        sh(self.repo, "commit", "-q", "-m", "initial")
        sh(self.repo, "push", "-q", "-u", "origin", "HEAD:main")
        sh(self.other, "pull", "-q", "origin", "main")
        sh(self.repo, "branch", "-M", "main")

        self.known_dir = known
        self.report = self.tmp / "report.json"
        self.calls = {"fetch": [], "metadata": [], "summarize": [], "tests": 0}
        self.channel = ["N1", "N2", "N3"]
        self.no_captions = set()
        self.fetch_errors = set()
        self.summarize_mode = "valid"  # valid | reviewed | invalid | raise
        self.tests_pass = True
        self.test_results = None  # optional list of results per call
        self.env = {"GEMINI_API_KEY": SECRET, "GEMINI_MODEL": "model-x"}
        self.logs = []

        deps = weekly_sync.Deps(repo=self.repo)
        deps.channel_ids = lambda channel_id: self._channel()
        deps.fetch_metadata = self._fetch_metadata
        deps.fetch_one = self._fetch_one
        deps.summarize = self._summarize
        deps.make_client = lambda key, model: object()
        deps.run_tests = self._run_tests
        deps.log = self.logs.append
        self.deps = deps

    # --- fakes ---
    def _channel(self):
        if isinstance(self.channel, BaseException):
            raise self.channel
        return list(self.channel)

    def _fetch_metadata(self, video_id):
        self.calls["metadata"].append(video_id)
        return meta(video_id)

    def _fetch_one(self, video_id, videos_dir):
        self.calls["fetch"].append(video_id)
        if video_id in self.no_captions:
            raise fetch_transcript.NoCaptionsError(f"no Vietnamese captions for {video_id}")
        if video_id in self.fetch_errors:
            raise RuntimeError(f"yt-dlp exploded for {video_id}")
        video_dir = fetch_transcript.write_video_files(
            videos_dir, meta(video_id), TRANSCRIPT.strip().splitlines())
        fetch_transcript.write_raw_captions(
            video_dir, video_id, "vi", b'{"events": []}', "2026-01-01T00:00:00Z", "test")
        return video_dir

    def _summarize(self, video_dir, client, **kwargs):
        video_dir = Path(video_dir)
        video_id = json.loads((video_dir / "metadata.json").read_text(encoding="utf-8"))["video_id"]
        self.calls["summarize"].append(video_id)
        mode = self.summarize_mode
        if mode == "raise":
            raise summarize.SummarizeError(f"generation failed with key {SECRET}")
        text = valid_summary_for(video_id)
        if mode == "changed":
            text = summary_text(extra="Ghi chú bổ sung.").replace(VID, video_id)
        if mode == "invalid":
            text = text.replace("## Glossary", "## Notes")
        (video_dir / "summary.md").write_text(text, encoding="utf-8")
        if mode == "reviewed":
            write_review(video_dir)
        return video_dir / "summary.md"

    def _run_tests(self):
        self.calls["tests"] += 1
        if self.test_results is not None:
            return self.test_results.pop(0) if self.test_results else True
        return self.tests_pass

    # --- helpers ---
    def run_sync(self, phase="all", env=None, extra=()):
        argv = [phase, "--report", str(self.report), *extra]
        stdout = io.StringIO()
        with mock.patch.dict(os.environ, env if env is not None else self.env):
            os.environ.pop("GITHUB_STEP_SUMMARY", None)
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
                rc = weekly_sync.main(argv, deps=self.deps)
        self.stdout = stdout.getvalue()
        return rc

    def state(self):
        return json.loads(self.report.read_text(encoding="utf-8"))

    def remote_head(self):
        return sh(self.remote, "rev-parse", "main").strip()

    def local_head(self):
        return sh(self.repo, "rev-parse", "HEAD").strip()

    def remote_files(self, rev="main"):
        return sorted(sh(self.remote, "ls-tree", "-r", "--name-only", rev).splitlines())

    def committed_files(self, rev="HEAD"):
        out = sh(self.repo, "show", "--name-only", "--format=", rev)
        return sorted(out.splitlines())

    def vdir(self, video_id):
        title = TITLES[video_id]
        slug = fetch_transcript.slugify(title)
        date = DATES[video_id]
        return self.repo / "videos" / f"{date[:4]}-{date[4:6]}-{date[6:]}-{slug}"

    def other_push(self, files, message="local push"):
        sh(self.other, "pull", "-q", "--rebase", "origin", "main")
        for name, content in files.items():
            path = self.other / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        sh(self.other, "add", "-A")
        sh(self.other, "commit", "-q", "-m", message)
        sh(self.other, "push", "-q", "origin", "HEAD:main")


class SelectionTest(Harness):
    def test_selects_first_distinct_unseen_and_queues_the_rest_metadata_only(self):
        self.channel = ["N1", "N1", KNOWN, "N2", "N3", "N2"]
        rc = self.run_sync()
        self.assertEqual(rc, 0)
        state = self.state()
        self.assertEqual(state["selected"], "N1")
        self.assertEqual(state["unseen"], ["N1", "N2", "N3"])
        self.assertEqual(state["pending"], ["N2", "N3"])
        self.assertEqual(self.calls["fetch"], ["N1"])  # backlog is never fetched
        self.assertEqual(self.calls["summarize"], ["N1"])  # nor summarized
        self.assertEqual(self.calls["metadata"], ["N2", "N3"])
        for backlog in ("N2", "N3"):
            self.assertEqual([p.name for p in self.vdir(backlog).iterdir()], ["metadata.json"])
            self.assertEqual(queue_state_state(self.vdir(backlog)), "pending")
        n1 = self.vdir("N1")
        self.assertTrue((n1 / "transcript.md").is_file() and (n1 / "summary.md").is_file())
        self.assertEqual(self.remote_head(), self.local_head())

    def test_selection_happens_before_any_directory_is_created(self):
        seen = {}
        original = self.deps.fetch_one

        def spy(video_id, videos_dir):
            seen["dirs"] = sorted(p.name for p in Path(videos_dir).iterdir())
            return original(video_id, videos_dir)

        self.deps.fetch_one = spy
        self.run_sync()
        self.assertEqual(seen["dirs"], ["2025-01-01-known"])

    def test_known_ids_are_compared_by_metadata_id_not_slug(self):
        self.channel = [KNOWN]
        self.assertEqual(self.run_sync(), 0)
        self.assertEqual(self.state()["unseen"], [])

    def test_no_new_video_skips_fetch_and_model_but_runs_gates_without_commit(self):
        self.channel = [KNOWN, KNOWN]
        head = self.local_head()
        rc = self.run_sync()
        self.assertEqual(rc, 0)
        self.assertEqual(self.calls["fetch"] + self.calls["summarize"] + self.calls["metadata"], [])
        self.assertEqual(self.calls["tests"], 1)
        self.assertEqual(self.state()["report"]["validator_exit"], 0)
        self.assertEqual(self.local_head(), head)
        self.assertEqual(self.remote_head(), head)

    def test_detection_error_is_a_failure_never_an_empty_success(self):
        self.channel = SystemExit(1)
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        self.assertTrue(any("detection failed" in f for f in self.state()["failures"]))
        self.assertEqual(self.calls["tests"], 1)  # gates still run
        self.assertEqual(self.remote_head(), self.local_head())

    def test_captions_not_ready_leaves_selected_pending_without_fallback(self):
        self.no_captions = {"N1"}
        rc = self.run_sync()
        self.assertEqual(rc, 0)  # a notice, not a failure
        self.assertEqual(self.calls["fetch"], ["N1"])  # no fallback to an older ID
        self.assertEqual(self.calls["summarize"], [])
        for video_id in ("N1", "N2", "N3"):
            self.assertEqual([p.name for p in self.vdir(video_id).iterdir()], ["metadata.json"])
        self.assertTrue(any("captions not ready for N1" in n for n in self.state()["notices"]))
        self.assertEqual(self.state()["pending"], ["N1", "N2", "N3"])
        files = self.committed_files()
        self.assertTrue(all(f.endswith("metadata.json") for f in files), files)

    def test_other_fetch_errors_fail_but_safe_queue_artifacts_survive(self):
        self.fetch_errors = {"N1"}
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        self.assertFalse(self.vdir("N1").exists())
        self.assertEqual(self.state()["pending"], ["N2", "N3"])
        self.assertEqual(self.remote_head(), self.local_head())  # pushed, but job is red
        self.assertEqual(len(self.committed_files()), 2)


def queue_state_state(video_dir):
    import queue_state
    return queue_state.video_state(video_dir)


class PendingWriterTest(Harness):
    def test_never_overwrites_and_refuses_ambiguous_destination(self):
        videos = self.repo / "videos"
        first = fetch_transcript.write_pending_metadata(videos, meta("N2"), expected_id="N2")
        before = (first / "metadata.json").read_bytes()
        with self.assertRaises(RuntimeError):
            fetch_transcript.write_pending_metadata(videos, meta("N2"))
        self.assertEqual((first / "metadata.json").read_bytes(), before)
        other = dict(meta("N3"), title=TITLES["N2"], upload_date=DATES["N2"])
        with self.assertRaises(RuntimeError):  # different ID, same destination
            fetch_transcript.write_pending_metadata(videos, other)
        self.assertEqual(json.loads((first / "metadata.json").read_text())["video_id"], "N2")

    def test_unusable_or_mismatched_metadata_writes_nothing(self):
        videos = self.repo / "videos"
        before = sorted(p.name for p in videos.iterdir())
        for bad in ({"id": "N2"}, dict(meta("N2"), title="!!!"), dict(meta("N2"), duration=None)):
            with self.assertRaises(RuntimeError):
                fetch_transcript.write_pending_metadata(videos, bad, expected_id="N2")
        with self.assertRaises(RuntimeError):
            fetch_transcript.write_pending_metadata(videos, meta("N3"), expected_id="N2")
        self.assertEqual(sorted(p.name for p in videos.iterdir()), before)

    def test_queue_failure_for_one_id_does_not_stop_the_others(self):
        # N3 collides with an existing directory of another video.
        clash = self.vdir("N3")
        clash.mkdir(parents=True)
        (clash / "metadata.json").write_text(json.dumps({"video_id": "other"}), encoding="utf-8")
        sh(self.repo, "add", "-A")
        sh(self.repo, "commit", "-q", "-m", "clash")
        sh(self.repo, "push", "-q", "origin", "HEAD:main")
        self.channel = ["N1", "N3", "N2"]
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        self.assertEqual(self.state()["pending"], ["N2"])
        self.assertTrue(any("cannot queue N3" in f for f in self.state()["failures"]))
        self.assertEqual(json.loads((clash / "metadata.json").read_text())["video_id"], "other")


class ValidationAndStagingTest(Harness):
    def test_valid_unreviewed_summary_is_committed_but_not_published(self):
        rc = self.run_sync()
        self.assertEqual(rc, 0)
        report = self.state()["report"]
        self.assertEqual(report["published"], ["videos/2025-01-01-known"])
        row = report["videos"][str(self.vdir("N1").relative_to(self.repo))]
        self.assertEqual((row["published"], row["review_missing"], row["invalid"]), (False, True, False))
        self.assertIn(f"{self.vdir('N1').relative_to(self.repo)}/summary.md", self.remote_files())
        # no persisted publication flag
        self.assertFalse(any("publish" in f.lower() for f in self.remote_files()))

    def test_valid_summary_with_current_passing_review_is_published(self):
        self.summarize_mode = "reviewed"
        # the review file is local-reviewer output, not allowlisted: it stays out of the commit
        rc = self.run_sync()
        self.assertEqual(rc, 0)
        n1 = str(self.vdir("N1").relative_to(self.repo))
        self.assertIn(n1, self.state()["report"]["published"])
        self.assertNotIn(f"{n1}/review.md", self.remote_files())

    def test_exact_allowlist_excludes_junk_and_unrelated_files(self):
        n1 = self.vdir("N1")
        self.deps_junk = []
        original = self.deps.fetch_one

        def fetch_then_litter(video_id, videos_dir):
            result = original(video_id, videos_dir)
            (result / "draft.tmp").write_text("x", encoding="utf-8")
            (result / "run.log").write_text("x", encoding="utf-8")
            return result

        self.deps.fetch_one = fetch_then_litter
        (self.repo / "notes.txt").write_text("unrelated", encoding="utf-8")
        (self.repo / ".env").write_text("TOKEN=1", encoding="utf-8")
        rc = self.run_sync()
        self.assertEqual(rc, 0)
        rel = n1.relative_to(self.repo).as_posix()
        committed = self.committed_files()
        self.assertIn(f"{rel}/transcript.md", committed)
        self.assertIn(f"{rel}/raw/provenance.json", committed)
        for junk in ("notes.txt", ".env", f"{rel}/draft.tmp", f"{rel}/run.log"):
            self.assertNotIn(junk, committed)
        self.assertTrue((self.repo / "notes.txt").is_file())

    def test_validator_exit_1_commits_safe_progress_but_ends_red(self):
        broken = self.repo / "videos" / "2024-01-01-broken"
        broken.mkdir()
        (broken / "metadata.json").write_text(
            json.dumps({"video_id": "broken1", "duration": DURATION}), encoding="utf-8")
        (broken / "transcript.md").write_text(TRANSCRIPT, encoding="utf-8")
        (broken / "summary.md").write_text("not a valid summary\n", encoding="utf-8")
        sh(self.repo, "add", "-A")
        sh(self.repo, "commit", "-q", "-m", "legacy invalid summary")
        sh(self.repo, "push", "-q", "origin", "HEAD:main")
        before = (broken / "summary.md").read_bytes()
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        self.assertEqual(self.state()["report"]["validator_exit"], 1)
        self.assertEqual(self.remote_head(), self.local_head())
        self.assertTrue(any("videos/2026" in f or "N1" in f or "video-moi" in f
                            for f in self.committed_files()))
        self.assertEqual((broken / "summary.md").read_bytes(), before)  # untouched
        self.assertFalse(any("broken" in f for f in self.committed_files()))

    def test_transcript_change_during_validation_aborts_the_write_path(self):
        head = self.remote_head()
        real = validate_summaries.validate_video

        def validator(video_dir, vocabulary):
            if "known" in str(video_dir):
                raise validate_summaries.TranscriptChanged("known")
            return real(video_dir, vocabulary)

        self.deps.validate = validator
        rc = self.run_sync()
        self.assertEqual(rc, 2)
        self.assertEqual(self.remote_head(), head)
        self.assertEqual(self.local_head(), head)

    def test_unexpected_or_undecodable_validator_results_fail_closed(self):
        head = self.remote_head()
        for bad in (RuntimeError("boom"), None, {"state": "pending"}):
            self.setUp()  # fresh repos each round
            head = self.remote_head()

            def validator(video_dir, vocabulary, bad=bad):
                if isinstance(bad, BaseException):
                    raise bad
                return bad

            self.deps.validate = validator
            self.assertEqual(self.run_sync(), 2, bad)
            self.assertEqual(self.remote_head(), head)
            self.assertEqual(self.local_head(), head)

    def test_missing_state_fails_closed(self):
        self.assertEqual(self.run_sync("finalize"), 2)
        self.report.write_text("{not json", encoding="utf-8")
        self.assertEqual(self.run_sync("finalize"), 2)
        self.assertEqual(self.remote_head(), self.local_head())

    def test_changed_existing_transcript_blocks_commit(self):
        (self.known_dir / "transcript.md").write_text(TRANSCRIPT + "[00:30:00] sửa\n", encoding="utf-8")
        head = self.remote_head()
        rc = self.run_sync()
        self.assertEqual(rc, 2)
        self.assertEqual(self.remote_head(), head)
        self.assertEqual(self.local_head(), head)

    def test_failing_unittest_blocks_every_commit_including_metadata(self):
        self.tests_pass = False
        head = self.local_head()
        rc = self.run_sync()
        self.assertEqual(rc, 2)
        self.assertEqual(self.local_head(), head)
        self.assertEqual(self.remote_head(), head)
        self.assertTrue(self.vdir("N2").exists())  # produced, but not committed

    def test_failing_unittest_also_blocks_stale_marker_only_runs(self):
        self.channel = [KNOWN]
        self.tests_pass = False
        self.assertEqual(self.run_sync(), 2)
        self.assertEqual(self.remote_head(), self.local_head())


class GenerationFailureTest(Harness):
    def fetched_state(self):
        """Run prepare only, so a fetched video is on disk awaiting summarization."""
        self.assertEqual(self.run_sync("prepare"), 0)

    def test_failure_without_prior_summary_leaves_only_the_fetch_result(self):
        self.summarize_mode = "raise"
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        n1 = self.vdir("N1")
        self.assertFalse((n1 / "summary.md").exists())
        self.assertFalse((n1 / "summary.stale").exists())
        files = self.committed_files()
        rel = n1.relative_to(self.repo).as_posix()
        self.assertIn(f"{rel}/transcript.md", files)
        self.assertFalse(any(f.endswith(("summary.md", "summary.stale")) for f in files))
        self.assertEqual(queue_state_state(n1), "transcribed")

    def test_invalid_candidate_is_never_committed(self):
        self.summarize_mode = "invalid"
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        self.assertFalse((self.vdir("N1") / "summary.md").exists())
        self.assertFalse(any(f.endswith("summary.md") for f in self.committed_files()))
        self.assertTrue(any("failed validation" in f for f in self.state()["failures"]))

    def regenerate(self, mode, **extra):
        """Drive generation against the committed known video (failed-regeneration path)."""
        self.summarize_mode = mode
        args = weekly_sync.build_parser().parse_args(["all", "--report", str(self.report)])
        for key, value in extra.items():
            setattr(args, key, value)
        state = weekly_sync.new_state(args)
        item = {"dir": "videos/2025-01-01-known", "video_id": KNOWN, "kind": "regen",
                "summary_candidate": False, "stale_marker": False}
        state["items"].append(item)
        state["selected"] = None
        weekly_sync.save_state(self.report, state)
        weekly_sync.generate_summary(self.deps, args, state, item, object(), lambda t: t)
        weekly_sync.save_state(self.report, state)
        return state, item

    def assert_prior_kept_and_stale(self, prior, item):
        summary = self.known_dir / "summary.md"
        self.assertEqual(summary.read_bytes(), prior)
        marker = (self.known_dir / "summary.stale").read_text(encoding="utf-8").strip()
        self.assertEqual(marker, hashlib.sha256(prior).hexdigest())  # bound to retained bytes
        self.assertTrue(item["stale_marker"])
        self.assertTrue((self.known_dir / "review.md").is_file())  # old review untouched

    def test_generation_failure_restores_prior_bytes_marks_stale_and_commits_marker(self):
        prior = (self.known_dir / "summary.md").read_bytes()
        state, item = self.regenerate("raise")
        self.assert_prior_kept_and_stale(prior, item)
        self.assertEqual(self.run_sync("finalize"), 1)
        self.assertIn("videos/2025-01-01-known/summary.stale", self.committed_files())
        self.assertNotIn("videos/2025-01-01-known/summary.md", self.committed_files())
        self.assertEqual(self.remote_head(), self.local_head())
        result = validate_summaries.validate_video(self.known_dir)
        self.assertFalse(result["published"])  # old pass can no longer publish it
        self.assertTrue(any("stale" in r for r in result["reasons"]))

    def test_replacement_failing_validation_restores_prior_and_marks_prior_hash(self):
        prior = (self.known_dir / "summary.md").read_bytes()
        state, item = self.regenerate("invalid")
        self.assert_prior_kept_and_stale(prior, item)

    def test_reduce_guard_rejection_takes_the_same_safe_path(self):
        prior = (self.known_dir / "summary.md").read_bytes()
        self.deps.summarize = summarize.summarize_video

        def client(prompt):
            return "## [00:10:00] X\n**Q: q?**\na"

        self.summarize_mode = "n/a"
        args = weekly_sync.build_parser().parse_args(
            ["all", "--report", str(self.report), "--reduce-max-chars", "50"])
        state = weekly_sync.new_state(args)
        item = {"dir": "videos/2025-01-01-known", "video_id": KNOWN, "kind": "regen",
                "summary_candidate": False, "stale_marker": False}
        weekly_sync.generate_summary(self.deps, args, state, item, client, lambda t: t)
        self.assertTrue(any("ceiling" in f for f in state["failures"]))
        self.assert_prior_kept_and_stale(prior, item)

    def test_unchanged_bytes_stay_ineligible_after_repeated_attempts(self):
        prior = (self.known_dir / "summary.md").read_bytes()
        self.regenerate("raise")
        _, item = self.regenerate("raise")
        self.assert_prior_kept_and_stale(prior, item)
        write_review(self.known_dir)  # re-running review cannot clear staleness
        self.assertFalse(validate_summaries.validate_video(self.known_dir)["published"])

    def test_changed_valid_replacement_escapes_the_marker_and_is_staged(self):
        prior = (self.known_dir / "summary.md").read_bytes()
        self.regenerate("raise")
        # rewriting identical bytes cannot clear the marker
        _, same = self.regenerate("valid")
        self.assertFalse(same["summary_candidate"])
        self.assert_prior_kept_and_stale(prior, same)
        # only changed bytes escape it (and still need a current review to publish)
        _, item = self.regenerate("changed")
        self.assertTrue(item["summary_candidate"])
        new = (self.known_dir / "summary.md").read_bytes()
        self.assertNotEqual(new, prior)
        result = validate_summaries.validate_video(self.known_dir)
        self.assertEqual((result["invalid"], result["published"]), (False, False))

    def test_failure_to_mark_or_restore_blocks_commit_and_push(self):
        head = self.remote_head()
        self.deps.mark_stale = lambda videos_dir, video_id: False
        state, item = self.regenerate("raise")
        self.assertTrue(any("cannot mark" in f for f in state["fatal"]))
        self.assertEqual(self.run_sync("finalize"), 2)
        self.assertEqual(self.remote_head(), head)
        self.assertEqual(self.local_head(), head)

    def test_restore_failure_is_fatal(self):
        self.deps.mark_stale = lambda videos_dir, video_id: True
        with mock.patch.object(weekly_sync, "restore_prior", side_effect=OSError("disk")):
            state, _ = self.regenerate("raise")
        self.assertTrue(any("cannot restore" in f for f in state["fatal"]))

    def test_missing_gemini_configuration_fails_generation_but_not_the_gates(self):
        def forbidden(key, model):
            raise AssertionError("no client may be built")

        self.deps.make_client = forbidden
        rc = self.run_sync(env={})
        self.assertEqual(rc, 1)
        self.assertEqual(self.calls["summarize"], [])
        self.assertTrue(any("GEMINI_API_KEY" in f for f in self.state()["failures"]))
        self.assertIn("transcript.md", " ".join(self.committed_files()))  # fetch result kept
        self.assertEqual(self.calls["tests"], 1)


class SecretsTest(Harness):
    def test_key_is_removed_from_the_environment_and_never_reported(self):
        self.summarize_mode = "raise"
        seen_env = {}
        original = self.deps.run_tests

        def tests():
            seen_env["key"] = os.environ.get("GEMINI_API_KEY")
            return original()

        self.deps.run_tests = tests
        self.run_sync()
        self.assertIsNone(seen_env["key"])
        blob = self.report.read_text(encoding="utf-8") + self.stdout + "\n".join(self.logs)
        self.assertNotIn(SECRET, blob)
        self.assertNotIn(SECRET[:12], blob)
        self.assertIn("[redacted]", self.report.read_text(encoding="utf-8"))

    def test_git_and_test_subprocesses_never_receive_the_key(self):
        with mock.patch.dict(os.environ, {"GEMINI_API_KEY": SECRET, "OTHER": "1"}):
            env = weekly_sync.clean_env()
        self.assertNotIn("GEMINI_API_KEY", env)
        self.assertEqual(env["OTHER"], "1")

    def test_workflow_scopes_key_and_forbids_claude_and_raw_check(self):
        text = (REPO_ROOT / ".github/workflows/weekly-sync.yml").read_text(encoding="utf-8")
        self.assertEqual(text.count("secrets.GEMINI_API_KEY"), 1)
        before_key = text.split("secrets.GEMINI_API_KEY")[0]
        self.assertIn("Summarize selected video", before_key.rsplit("- name:", 1)[1])
        self.assertNotRegex(text, r"claude\s+-p")
        self.assertNotIn("fetch_transcript.py --check", text)
        self.assertNotIn("set -x", text)
        self.assertIn("cron: '0 3 * * 0'", text)
        self.assertIn("workflow_dispatch", text)
        self.assertRegex(text, r"cancel-in-progress:\s*false")
        self.assertRegex(text, r"contents:\s*write")
        self.assertIn("fetch-depth: 0", text)
        self.assertEqual(len(list((REPO_ROOT / ".github/workflows").glob("*.yml"))), 2)


class PushRaceTest(Harness):
    def test_non_conflicting_local_push_is_retained_and_gates_rerun(self):
        self.deps.hook = lambda stage: (
            self.other_push({"notes/local.md": "entry 9 push\n"}) if stage == "before_sync" else None)
        rc = self.run_sync()
        self.assertEqual(rc, 0)
        self.assertEqual(self.calls["tests"], 2)  # before and after the rebase
        files = self.remote_files()
        self.assertIn("notes/local.md", files)
        self.assertTrue(any(f.endswith("N1") or "video-moi-nhat" in f for f in files))
        self.assertEqual(self.remote_head(), self.local_head())
        self.assertEqual(sh(self.repo, "log", "--format=%s", "-3").count("local push"), 1)

    def test_gate_failure_after_rebase_blocks_the_push(self):
        self.test_results = [True, False]
        self.deps.hook = lambda stage: (
            self.other_push({"notes/local.md": "x\n"}) if stage == "before_sync" else None)
        rc = self.run_sync()
        self.assertEqual(rc, 2)
        self.assertEqual(sh(self.remote, "rev-list", "--count", "main").strip(), "2")
        self.assertFalse(any("video-moi-nhat" in f for f in self.remote_files()))
        self.assertIn("notes/local.md", self.remote_files())

    def test_merged_change_invalidating_the_candidate_blocks_the_push(self):
        # The other clone's push adds a stale marker for the exact bytes this run generates.
        n1 = self.vdir("N1").relative_to(self.repo).as_posix()
        digest = hashlib.sha256(valid_summary_for("N1").encode()).hexdigest()
        self.deps.hook = lambda stage: (
            self.other_push({f"{n1}/summary.stale": digest + "\n"}) if stage == "before_sync" else None)
        before = self.remote_head()
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        self.assertTrue(any("no longer valid" in f for f in self.state()["failures"]))
        self.assertNotIn(f"{n1}/summary.md", self.remote_files())
        self.assertNotEqual(before, "")

    def test_rebase_conflict_is_aborted_named_and_never_forced(self):
        n1 = self.vdir("N1").relative_to(self.repo).as_posix()
        self.deps.hook = lambda stage: (
            self.other_push({f"{n1}/metadata.json": '{"video_id": "other"}\n'})
            if stage == "before_sync" else None)
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        message = " ".join(self.state()["failures"])
        self.assertIn("main", message)
        self.assertIn(f"{n1}/metadata.json", message)
        self.assertFalse((self.repo / ".git" / "rebase-merge").exists())
        self.assertFalse((self.repo / ".git" / "rebase-apply").exists())
        remote_meta = sh(self.remote, "show", f"main:{n1}/metadata.json")
        self.assertIn('"other"', remote_meta)  # remote content survived

    def test_rejected_push_fails_visibly_without_force_or_retry(self):
        pushes = []
        original = self.deps.git

        def spying_git(*args):
            if args and args[0] == "push":
                pushes.append(args)
            return original(*args)

        self.deps.git = spying_git
        self.deps.hook = lambda stage: (
            self.other_push({"notes/late.md": "late\n"}) if stage == "before_push" else None)
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        self.assertEqual(len(pushes), 1)
        self.assertNotIn("--force", " ".join(pushes[0]))
        self.assertNotIn("-f", pushes[0])
        self.assertTrue(any("rejected" in f for f in self.state()["failures"]))
        self.assertIn("notes/late.md", self.remote_files())
        self.assertFalse(any(f.endswith("transcript.md") and "video-moi" in f
                             for f in self.remote_files()))


class ReviewPatchTest(Harness):
    """Regressions for the 1.11 review patches (cancel, finalize errors, partial fetch, races)."""

    def test_cancelled_runs_never_reach_summarize_or_finalize(self):
        text = (REPO_ROOT / ".github/workflows/weekly-sync.yml").read_text(encoding="utf-8")
        self.assertNotIn("always()", text)
        for step in ("Summarize selected video", "Validate, test, commit and push"):
            block = text.split(f"- name: {step}", 1)[1].split("- name:", 1)[0]
            self.assertRegex(block, r"if:\s*\$\{\{\s*!cancelled\(\)", step)

    def test_unexpected_finalize_error_fails_closed_with_a_saved_report(self):
        head = self.remote_head()
        with mock.patch.object(weekly_sync, "build_allowlist", side_effect=ValueError("boom")):
            rc = self.run_sync()
        self.assertEqual(rc, 2)
        state = self.state()
        self.assertTrue(any("ValueError in finalize" in f for f in state["fatal"]))
        self.assertFalse(state["report"]["pushed"])
        self.assertEqual(self.remote_head(), head)
        self.assertEqual(self.local_head(), head)

    def test_summary_is_not_staged_when_its_fetch_result_is_incomplete(self):
        original = self.deps.fetch_one

        def fetch_then_lose_provenance(video_id, videos_dir):
            video_dir = original(video_id, videos_dir)
            (video_dir / "raw" / "provenance.json").unlink()
            return video_dir

        self.deps.fetch_one = fetch_then_lose_provenance
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        n1 = self.vdir("N1").relative_to(self.repo).as_posix()
        self.assertTrue((self.vdir("N1") / "summary.md").is_file())  # generated locally
        self.assertFalse(any(f.startswith(n1 + "/") for f in self.remote_files()))
        self.assertTrue(any("incomplete fetch result" in f for f in self.state()["failures"]))

    def test_duplicate_video_id_after_rebase_blocks_the_push(self):
        dup = {"video_id": "N1", "title": "renamed", "duration": DURATION}
        self.deps.hook = lambda stage: (
            self.other_push({"videos/2026-01-05-renamed/metadata.json": json.dumps(dup)})
            if stage == "before_sync" else None)
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        message = " ".join(self.state()["failures"])
        self.assertIn("more than one directory", message)
        self.assertIn("N1", message)
        n1 = self.vdir("N1").relative_to(self.repo).as_posix()
        self.assertNotIn(f"{n1}/transcript.md", self.remote_files())

    def test_non_conflict_rebase_failure_names_its_cause(self):
        def hook(stage):
            if stage == "before_sync":
                self.other_push({"notes/clash.md": "remote\n"})
                (self.repo / "notes").mkdir(exist_ok=True)
                (self.repo / "notes" / "clash.md").write_text("untracked\n", encoding="utf-8")

        self.deps.hook = hook
        rc = self.run_sync()
        self.assertEqual(rc, 1)
        message = " ".join(self.state()["failures"])
        self.assertIn("not a merge conflict", message)
        self.assertNotIn("rebase conflict", message)
        self.assertIn("notes/clash.md", self.remote_files())  # the other push survived
        n1 = self.vdir("N1").relative_to(self.repo).as_posix()
        self.assertFalse(any(f.startswith(n1 + "/") for f in self.remote_files()))
        self.assertFalse((self.repo / ".git" / "rebase-merge").exists())


if __name__ == "__main__":
    unittest.main()
