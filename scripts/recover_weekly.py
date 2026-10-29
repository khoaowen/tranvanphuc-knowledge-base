#!/usr/bin/env python3
"""Recover locally prepared weekly-sync artifacts whose report.json was lost.

Used only by `./weekly-sync --recover`. `inspect_inventory` is read-only: it
lists Git state with NUL-delimited paths and verifies the untracked prepared
inventory on disk (exactly one fully fetched new video, every other new folder
metadata.json only) with the existing fetch_transcript read-only helpers. It
never fetches, never calls Gemini and never writes videos/ or Git.
`save_recovered_evidence` runs only after the owner confirms: it re-inspects,
then writes a new evidence directory outside the repository holding a clearly
labelled recovered report.json and a replacement before.sha.
"""

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import detect_new_videos  # noqa: E402
import fetch_transcript  # noqa: E402
import weekly_sync  # noqa: E402

VIDEOS_DIR = "videos"
METADATA = "metadata.json"
TRANSCRIPT = "transcript.md"
PROVENANCE = f"{fetch_transcript.RAW_DIRNAME}/{fetch_transcript.PROVENANCE_FILENAME}"
CAPTION_TRACKS = ("vi-orig", "vi")
VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RECOVERY_KIND = "local-artifact-recovery"
CAVEATS = [
    "The original prepare report.json, before.sha and phase logs were lost; they were not recovered.",
    "before.sha holds the HEAD at recovery time: a labelled replacement baseline, "
    "not the original pre-prepare HEAD.",
    "The original channel listing order and detection output are unavailable; pending order "
    "here is by directory name (published date), newest first.",
    "Artifacts were verified from files on disk only; this is not evidence of the original "
    "run's log output or status.",
]


class RecoveryError(RuntimeError):
    """The inventory cannot be adopted; nothing was written."""


def git_paths(repo, *args):
    """Run a read-only `git ... -z` listing and return its NUL-delimited paths."""
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if result.returncode:
        raise RecoveryError(f"git {' '.join(args)} failed: "
                            f"{result.stderr.decode('utf-8', 'replace').strip()}")
    return [p for p in result.stdout.decode("utf-8").split("\0") if p]


def git_text(repo, *args):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if result.returncode:
        raise RecoveryError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def walk_files(video_dir, rel_dir):
    """Return the folder's files (relative names); refuse symlinks, special files, nested dirs."""
    files = set()
    pending = [(video_dir, "")]
    while pending:
        directory, prefix = pending.pop()
        for entry in directory.iterdir():
            name = prefix + entry.name
            if entry.is_symlink():
                raise RecoveryError(f"symlink in prepared folder: {rel_dir}/{name}")
            if entry.is_dir() and not prefix and entry.name == fetch_transcript.RAW_DIRNAME:
                pending.append((entry, name + "/"))
            elif entry.is_file():
                files.add(name)
            else:
                raise RecoveryError(f"unexpected entry in prepared folder: {rel_dir}/{name}")
    return files


def read_metadata(video_dir, rel_dir):
    """Validate metadata.json content, canonical bytes and canonical folder name; return it."""
    path = video_dir / METADATA
    try:
        raw = path.read_bytes()
        metadata = json.loads(raw.decode("utf-8"))
    except (OSError, ValueError) as exc:
        raise RecoveryError(f"malformed {rel_dir}/{METADATA}: {exc}") from exc
    if not isinstance(metadata, dict) or set(metadata) != {
            "video_id", "title", "url", "published_at", "duration", "topics"}:
        raise RecoveryError(f"malformed {rel_dir}/{METADATA}: unexpected fields")
    video_id, title, published_at = metadata["video_id"], metadata["title"], metadata["published_at"]
    duration = metadata["duration"]
    if not isinstance(video_id, str) or not VIDEO_ID_PATTERN.match(video_id):
        raise RecoveryError(f"invalid video_id in {rel_dir}/{METADATA}: {video_id!r}")
    if not isinstance(title, str) or not title or not fetch_transcript.slugify(title):
        raise RecoveryError(f"invalid title in {rel_dir}/{METADATA}")
    try:
        if not isinstance(published_at, str) or not DATE_PATTERN.match(published_at):
            raise ValueError(published_at)
        date.fromisoformat(published_at)
    except ValueError as exc:
        raise RecoveryError(f"invalid published_at in {rel_dir}/{METADATA}: {published_at!r}") from exc
    if (isinstance(duration, bool) or not isinstance(duration, (int, float))
            or not math.isfinite(duration) or duration <= 0):
        raise RecoveryError(f"invalid duration in {rel_dir}/{METADATA}: {duration!r}")
    if metadata["url"] != f"https://www.youtube.com/watch?v={video_id}":
        raise RecoveryError(f"{rel_dir}/{METADATA} url is not the YouTube URL of {video_id}")
    source = {"id": video_id, "title": title, "webpage_url": metadata["url"],
              "upload_date": published_at.replace("-", ""), "duration": duration}
    if fetch_transcript.video_dir_for(VIDEOS_DIR, source).name != video_dir.name:
        raise RecoveryError(f"{rel_dir} is not the canonical folder for its metadata")
    canonical = json.dumps(fetch_transcript.metadata_json_for(source), ensure_ascii=False, indent=2) + "\n"
    if raw != canonical.encode("utf-8"):
        raise RecoveryError(f"{rel_dir}/{METADATA} is not in the canonical written form")
    return metadata


def verify_fetched(video_dir, rel_dir, files, video_id):
    """Verify a complete fetch result bound to its metadata; raise on any problem."""
    if PROVENANCE not in files or TRANSCRIPT not in files:
        raise RecoveryError(f"partial fetch in {rel_dir}: {sorted(files)}")
    try:
        provenance, raw_path = fetch_transcript.load_raw_captions(video_dir)
    except Exception as exc:
        raise RecoveryError(f"raw captions of {rel_dir} fail verification: {exc}") from exc
    if not isinstance(provenance, dict):
        raise RecoveryError(f"malformed provenance in {rel_dir}")
    track = provenance.get("track")
    if (provenance.get("video_id") != video_id
            or provenance.get("source_url") != f"https://www.youtube.com/watch?v={video_id}"
            or track not in CAPTION_TRACKS
            or provenance.get("raw_file") != f"captions.{track}.json3.gz"
            or provenance.get("caption_kind") != fetch_transcript.CAPTION_KIND):
        raise RecoveryError(f"provenance of {rel_dir} does not identify video {video_id}")
    expected = {METADATA, TRANSCRIPT, PROVENANCE,
                f"{fetch_transcript.RAW_DIRNAME}/{provenance['raw_file']}"}
    if files != expected:
        raise RecoveryError(f"{rel_dir} is not exactly one complete fetch result "
                            f"(found {sorted(files)})")
    try:
        lines = fetch_transcript.build_transcript_lines(raw_path)
    except Exception as exc:
        raise RecoveryError(f"captions of {rel_dir} cannot be parsed: {exc}") from exc
    if not lines:
        raise RecoveryError(f"captions of {rel_dir} contain no transcript lines")
    problems = fetch_transcript.check_transcript(video_dir)
    if problems:
        raise RecoveryError(f"transcript of {rel_dir} fails verification: {'; '.join(problems)}")


def tracked_video_ids(repo, tracked):
    """{video_id: dir} for every tracked videos/*/metadata.json."""
    ids = {}
    for path in tracked:
        parts = path.split("/")
        if len(parts) != 3 or parts[2] != METADATA:
            continue
        try:
            video_id = json.loads((repo / path).read_text(encoding="utf-8"))["video_id"]
        except (OSError, ValueError, KeyError, TypeError) as exc:
            raise RecoveryError(f"cannot read tracked {path} for duplicate checks: {exc}") from exc
        ids.setdefault(video_id, "/".join(parts[:2]))
    return ids


def inspect_inventory(repo):
    """Read-only: validate the untracked prepared inventory; return it or raise RecoveryError."""
    repo = Path(repo).resolve()
    branch = git_text(repo, "branch", "--show-current")
    if not branch or branch in ("main", "master"):
        raise RecoveryError("Use the feature branch, not main/master or detached HEAD.")
    head = git_text(repo, "rev-parse", "--verify", "HEAD")
    if git_paths(repo, "diff", "--cached", "--name-only", "-z"):
        raise RecoveryError("Staged work exists; refusing to adopt it.")
    if git_paths(repo, "diff", "--name-only", "-z", "HEAD", "--"):
        raise RecoveryError("Tracked files are modified; refusing to adopt them.")
    videos = repo / VIDEOS_DIR
    if videos.is_symlink() or not videos.is_dir() or videos.resolve() != videos:
        raise RecoveryError(f"{VIDEOS_DIR}/ is not a real directory inside the repository")

    folders = {}
    for path in git_paths(repo, "ls-files", "--others", "--exclude-standard", "-z"):
        parts = path.split("/")
        nested_ok = len(parts) == 3 or (len(parts) == 4 and parts[2] == fetch_transcript.RAW_DIRNAME)
        if parts[0] != VIDEOS_DIR or not nested_ok or parts[1].startswith("."):
            raise RecoveryError(f"Unrelated untracked file: {path}")
        folders.setdefault(parts[1], set()).add("/".join(parts[2:]))
    if not folders:
        raise RecoveryError("No untracked prepared artifacts found under videos/.")

    tracked = git_paths(repo, "ls-files", "-z", "--", VIDEOS_DIR)
    tracked_dirs = {p.split("/")[1] for p in tracked if p.count("/") >= 2}
    known = tracked_video_ids(repo, tracked)
    fetched, pending, seen, digests = [], [], {}, {}
    for name in sorted(folders):
        rel_dir = f"{VIDEOS_DIR}/{name}"
        video_dir = videos / name
        if name in tracked_dirs:
            raise RecoveryError(f"Untracked files inside tracked folder {rel_dir}: {sorted(folders[name])}")
        if video_dir.is_symlink() or not video_dir.is_dir() or video_dir.resolve() != video_dir:
            raise RecoveryError(f"{rel_dir} is not a real directory inside videos/")
        files = walk_files(video_dir, rel_dir)
        if files != folders[name]:
            raise RecoveryError(f"{rel_dir} holds files Git does not list as untracked: "
                                f"{sorted(files - folders[name])}")
        video_id = read_metadata(video_dir, rel_dir)["video_id"]
        if video_id in known:
            raise RecoveryError(f"{video_id} in {rel_dir} duplicates tracked {known[video_id]}")
        if video_id in seen:
            raise RecoveryError(f"{video_id} appears in both {seen[video_id]} and {rel_dir}")
        seen[video_id] = rel_dir
        if files == {METADATA}:
            if {p.name for p in video_dir.iterdir()} != {METADATA}:
                raise RecoveryError(f"partial fetch in {rel_dir}: leftover empty directory")
            pending.append({"video_id": video_id, "dir": rel_dir})
        else:
            verify_fetched(video_dir, rel_dir, files, video_id)
            fetched.append({"video_id": video_id, "dir": rel_dir})
        for file in sorted(files):
            digests[f"{rel_dir}/{file}"] = hashlib.sha256((video_dir / file).read_bytes()).hexdigest()
    if len(fetched) != 1:
        raise RecoveryError(f"Expected exactly one fully fetched new video, found {len(fetched)}: "
                            f"{[item['dir'] for item in fetched]}")
    pending.sort(key=lambda item: item["dir"], reverse=True)
    listing = json.dumps(digests, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "head": head,
        "branch": branch,
        "selected": fetched[0],
        "pending": pending,
        "files": digests,
        "inventory_sha256": hashlib.sha256(listing).hexdigest(),
    }


def build_recovered_state(inventory, recovered_at):
    """A weekly_sync state (prepare already done) labelled as a recovery, not the original run."""
    state = weekly_sync.new_state(argparse.Namespace(
        channel_id=detect_new_videos.DEFAULT_CHANNEL_ID, videos_dir=VIDEOS_DIR))
    selected = inventory["selected"]
    pending_ids = [item["video_id"] for item in inventory["pending"]]
    state["selected"] = selected["video_id"]
    state["unseen"] = []  # Channel detection output was lost; never reconstructed.
    state["pending"] = pending_ids
    state["items"] = [
        {"dir": selected["dir"], "video_id": selected["video_id"], "kind": "fetched",
         "summary_candidate": False, "stale_marker": False},
        *({"dir": item["dir"], "video_id": item["video_id"], "kind": "pending",
           "summary_candidate": False, "stale_marker": False} for item in inventory["pending"]),
    ]
    state["notices"] = [
        f"recovered at {recovered_at} from verified untracked prepared artifacts; the original "
        "prepare report, logs and before.sha were lost (see the report's recovery section)"
    ]
    state["recovery"] = {
        "kind": RECOVERY_KIND,
        "recovered_at": recovered_at,
        "head": inventory["head"],
        "branch": inventory["branch"],
        "baseline": "replacement: HEAD at recovery time, not the original before.sha",
        "selected": selected,
        "pending": inventory["pending"],
        "inventory_sha256": inventory["inventory_sha256"],
        "files": inventory["files"],
        "caveats": CAVEATS,
    }
    return state


def save_recovered_evidence(repo, runs_dir, inventory):
    """After owner approval: re-inspect, then write a new durable evidence directory."""
    repo = Path(repo).resolve()
    if inspect_inventory(repo) != inventory:
        raise RecoveryError("The inventory or HEAD changed after inspection; nothing was adopted.")
    runs_dir = Path(runs_dir).resolve()
    if runs_dir == repo or repo in runs_dir.parents:
        raise RecoveryError(f"Evidence directory {runs_dir} must be outside the repository.")
    runs_dir.mkdir(parents=True, exist_ok=True)
    recovered_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state = build_recovered_state(inventory, recovered_at)
    evidence = Path(tempfile.mkdtemp(prefix="recover-", dir=runs_dir))
    with (evidence / "before.sha").open("x", encoding="utf-8") as handle:
        handle.write(inventory["head"] + "\n")
    weekly_sync.save_state(evidence / "report.json", state)
    return evidence
