#!/usr/bin/env python3
"""Fetch transcript and metadata for YouTube videos into videos/<slug>/.

For each video ID (given as command-line args, or piped on stdin one per
line), uses yt-dlp (no API key) to fetch video metadata and the Vietnamese
auto-caption track (preferring vi-orig, falling back to vi), then writes
videos/<published_at>-<slug>/metadata.json and transcript.md.

The downloaded json3 is kept, unedited, as the source of truth:
raw/captions.<track>.json3.gz (deterministic gzip of the exact bytes yt-dlp
wrote) plus raw/provenance.json (track, retrieval time, yt-dlp version,
sha256 of the stored raw file and of the rendered transcript.md). An existing
video directory is never re-fetched over; use --rerender for a raw-backed dir.

  --rerender DIR...  rewrite DIR/transcript.md from DIR/raw/
  --check DIR...     exit non-zero if DIR/transcript.md differs from a
                     re-render of DIR/raw/ (or the raw file's sha256 no
                     longer matches provenance.json)

A per-video failure (no Vietnamese captions, yt-dlp error) does not abort
the run -- it is warned to stderr and skipped. The run exits non-zero only
if every requested video failed.
"""

import argparse
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
import zlib
from datetime import datetime, timezone
from pathlib import Path

TOOL = "scripts/fetch_transcript.py"
RAW_DIRNAME = "raw"
PROVENANCE_FILENAME = "provenance.json"
# --write-auto-sub only ever yields YouTube's automatic speech recognition track.
CAPTION_KIND = "asr"

DIACRITIC_MAP = {
    "đ": "d",
    "Đ": "D",
}


def slugify(title):
    """Slugify a (possibly Vietnamese) title into a lowercase ascii slug.

    NFD-normalizes to split base letters from combining marks, maps đ/Đ
    explicitly (not decomposable via NFD), strips remaining combining
    marks, lowercases, collapses runs of non-alphanumeric characters to a
    single hyphen, and trims leading/trailing hyphens.
    """
    mapped = "".join(DIACRITIC_MAP.get(ch, ch) for ch in title)
    normalized = unicodedata.normalize("NFD", mapped)
    stripped = "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")
    lowered = stripped.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    return slug.strip("-")


def fetch_metadata(video_id):
    """Fetch and parse video metadata via yt-dlp.

    Returns a dict with at least title, upload_date, duration,
    webpage_url, id. Raises RuntimeError on yt-dlp failure or bad JSON.
    """
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        result = subprocess.run(
            ["yt-dlp", "--skip-download", "-j", url],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("yt-dlp is not installed or not on PATH") from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"yt-dlp timed out fetching metadata for {video_id}") from exc

    if result.returncode != 0:
        raise RuntimeError(
            f"yt-dlp failed (exit {result.returncode}) fetching metadata for "
            f"{video_id}: {result.stderr.strip()}"
        )

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"yt-dlp returned invalid JSON for {video_id}: {exc}") from exc


def yt_dlp_version():
    """Return `yt-dlp --version` output. Raises RuntimeError on failure."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("yt-dlp is not installed or not on PATH") from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("yt-dlp timed out reporting its version") from exc

    version = result.stdout.strip()
    if result.returncode != 0 or not version:
        raise RuntimeError(
            f"yt-dlp --version failed (exit {result.returncode}): {result.stderr.strip()}"
        )
    return version


def fetch_caption_json3(video_id, tmp_dir):
    """Download the Vietnamese auto-caption track in json3 format.

    Prefers vi-orig, falls back to vi. Returns the Path to the downloaded
    json3 file. Raises RuntimeError if yt-dlp fails or neither track was
    produced.
    """
    url = f"https://www.youtube.com/watch?v={video_id}"
    output_template = str(Path(tmp_dir) / "%(id)s")
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "--skip-download",
                "--write-auto-sub",
                "--sub-langs",
                "vi-orig,vi",
                "--sub-format",
                "json3",
                "-o",
                output_template,
                url,
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("yt-dlp is not installed or not on PATH") from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"yt-dlp timed out fetching captions for {video_id}") from exc

    if result.returncode != 0:
        raise RuntimeError(
            f"yt-dlp failed (exit {result.returncode}) fetching captions for "
            f"{video_id}: {result.stderr.strip()}"
        )

    vi_orig_path = Path(tmp_dir) / f"{video_id}.vi-orig.json3"
    vi_path = Path(tmp_dir) / f"{video_id}.vi.json3"

    if vi_orig_path.is_file():
        return vi_orig_path
    if vi_path.is_file():
        return vi_path

    raise RuntimeError(f"no Vietnamese captions (vi-orig/vi) found for {video_id}")


def caption_track(video_id, json3_path):
    """Return the track ("vi-orig" or "vi") of a <video_id>.<track>.json3 file."""
    return Path(json3_path).name.removeprefix(f"{video_id}.").removesuffix(".json3")


def build_transcript_lines(json3_path):
    """Parse a json3 caption file (plain or .gz) into timestamped transcript lines.

    Skips bare-newline-only events (segs == [{"utf8": "\\n"}], no
    dDurationMs). Returns a list of "[hh:mm:ss] text" strings.
    """
    opener = gzip.open if str(json3_path).endswith(".gz") else open
    with opener(json3_path, "rt", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict) or not isinstance(data.get("events"), list):
        raise ValueError("json3 must contain an events list")

    lines = []
    for event in data["events"]:
        if not isinstance(event, dict):
            raise ValueError("json3 events must be objects")
        segs = event.get("segs")
        if not segs:
            continue
        if "dDurationMs" not in event:
            continue

        text = "".join(seg.get("utf8", "") for seg in segs).strip()
        if not text:
            continue

        start_ms = event.get("tStartMs", 0)
        if isinstance(start_ms, bool) or not isinstance(start_ms, int) or start_ms < 0:
            raise ValueError(f"invalid tStartMs: {start_ms!r}")
        total_seconds = start_ms // 1000
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        lines.append(f"[{timestamp}] {text}")

    return lines


def render_transcript(lines):
    """Return transcript.md's exact text for the given transcript lines."""
    return "\n".join(lines) + "\n"


def published_at_for(metadata):
    upload_date = metadata["upload_date"]
    return f"{upload_date[0:4]}-{upload_date[4:6]}-{upload_date[6:8]}"


def video_dir_for(videos_dir, metadata):
    """Return videos/<published_at>-<slug>/ for the given yt-dlp metadata."""
    return Path(videos_dir) / f"{published_at_for(metadata)}-{slugify(metadata['title'])}"


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def write_video_files(videos_dir, metadata, lines):
    """Write metadata.json and transcript.md under videos/<published_at>-<slug>/."""
    published_at = published_at_for(metadata)
    video_dir = video_dir_for(videos_dir, metadata)
    video_dir.mkdir(parents=True, exist_ok=True)

    metadata_json = {
        "video_id": metadata["id"],
        "title": metadata["title"],
        "url": metadata["webpage_url"],
        "published_at": published_at,
        "duration": metadata["duration"],
        "topics": [],
    }

    (video_dir / "metadata.json").write_text(
        json.dumps(metadata_json, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (video_dir / "transcript.md").write_bytes(render_transcript(lines).encode("utf-8"))

    return video_dir


def write_raw_captions(video_dir, video_id, track, raw_bytes, retrieved_at, yt_dlp_ver):
    """Store the downloaded json3 under raw/ (gzip, deterministic) plus provenance.json.

    Must run after transcript.md is written: provenance records its sha256.
    """
    raw_dir = Path(video_dir) / RAW_DIRNAME
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_file = f"captions.{track}.json3.gz"
    # mtime=0 and no embedded filename, so re-storing the same download gives the same bytes.
    stored = gzip.compress(raw_bytes, compresslevel=9, mtime=0)
    (raw_dir / raw_file).write_bytes(stored)

    provenance = {
        "video_id": video_id,
        "source_url": f"https://www.youtube.com/watch?v={video_id}",
        "track": track,
        "caption_kind": CAPTION_KIND,
        "retrieved_at": retrieved_at,
        "raw_file": raw_file,
        "sha256": sha256_hex(stored),
        "yt_dlp_version": yt_dlp_ver,
        "tool": TOOL,
        "transcript_sha256": sha256_hex((Path(video_dir) / "transcript.md").read_bytes()),
    }
    (raw_dir / PROVENANCE_FILENAME).write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def fetch_one_video(video_id, videos_dir, pending_dir=None):
    """Fetch one video, refusing existing targets except a validated pending dir.

    The pending mode is reserved for review_batch: it may add transcript/raw
    files to a metadata-only directory whose metadata identifies this video.
    Metadata and any pre-existing artifact are never overwritten.
    """
    metadata = fetch_metadata(video_id)
    video_dir = video_dir_for(videos_dir, metadata)
    if pending_dir is None:
        if video_dir.exists():
            raise RuntimeError(
                f"{video_dir} already exists; existing videos are never overwritten "
                "(use --rerender when raw captions are already present)"
            )
    else:
        video_dir = Path(pending_dir)
        if metadata.get("id") != video_id:
            raise RuntimeError(f"yt-dlp metadata ID does not match requested video {video_id}")
        metadata_path = video_dir / "metadata.json"
        try:
            existing = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"invalid pending metadata {metadata_path}: {exc}") from exc
        if not isinstance(existing, dict) or existing.get("video_id") != video_id:
            raise RuntimeError(f"pending metadata does not identify video {video_id}: {metadata_path}")
        if not video_dir.is_dir() or set(p.name for p in video_dir.iterdir()) != {"metadata.json"}:
            raise RuntimeError(f"pending directory must contain metadata.json only: {video_dir}")
    yt_dlp_ver = yt_dlp_version()
    with tempfile.TemporaryDirectory() as tmp_dir:
        json3_path = fetch_caption_json3(video_id, tmp_dir)
        retrieved_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        track = caption_track(video_id, json3_path)
        raw_bytes = json3_path.read_bytes()
        lines = build_transcript_lines(json3_path)

    videos_dir = Path(videos_dir)
    videos_dir.mkdir(parents=True, exist_ok=True)
    # Build all additions off-destination before installing anything.
    with tempfile.TemporaryDirectory(dir=videos_dir, prefix=".fetch-") as staging_dir:
        staged_video_dir = write_video_files(staging_dir, metadata, lines)
        write_raw_captions(
            staged_video_dir, video_id, track, raw_bytes, retrieved_at, yt_dlp_ver
        )
        if pending_dir is None:
            staged_video_dir.rename(video_dir)
        else:
            # Revalidate immediately before installation. Hard links and mkdir
            # provide atomic no-replace creation; interruption leaves a partial
            # state that fails closed on retry rather than overwriting anything.
            if set(p.name for p in video_dir.iterdir()) != {"metadata.json"}:
                raise RuntimeError(f"pending directory changed during fetch: {video_dir}")
            os.link(staged_video_dir / "transcript.md", video_dir / "transcript.md")
            staged_raw = staged_video_dir / RAW_DIRNAME
            raw_dir = video_dir / RAW_DIRNAME
            raw_dir.mkdir()
            for staged_file in staged_raw.iterdir():
                os.link(staged_file, raw_dir / staged_file.name)
    return video_dir


def load_raw_captions(video_dir):
    """Return (provenance, raw_path) for video_dir, verifying the raw file's sha256.

    Raises RuntimeError if provenance or the raw file is missing, or the raw
    file no longer matches the sha256 recorded at fetch time.
    """
    raw_dir = Path(video_dir) / RAW_DIRNAME
    provenance_path = raw_dir / PROVENANCE_FILENAME
    if not provenance_path.is_file():
        raise RuntimeError(f"no raw captions: {provenance_path} is missing")
    try:
        provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
        raw_file = provenance["raw_file"]
        expected_sha256 = provenance["sha256"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise RuntimeError(f"invalid {provenance_path}: {exc!r}") from exc
    if not isinstance(raw_file, str) or Path(raw_file).name != raw_file:
        raise RuntimeError(f"invalid raw_file in {provenance_path}: {raw_file!r}")
    raw_path = raw_dir / raw_file
    if not raw_path.is_file():
        raise RuntimeError(f"raw captions file {raw_path} is missing")
    if sha256_hex(raw_path.read_bytes()) != expected_sha256:
        raise RuntimeError(f"{raw_path} sha256 does not match {provenance_path}")
    return provenance, raw_path


def rerender_transcript(video_dir):
    """Rewrite video_dir/transcript.md from its raw captions. Provenance is unchanged."""
    _, raw_path = load_raw_captions(video_dir)
    text = render_transcript(build_transcript_lines(raw_path))
    (Path(video_dir) / "transcript.md").write_bytes(text.encode("utf-8"))


def check_transcript(video_dir):
    """Return a list of problems; empty when transcript.md equals a re-render of raw/."""
    try:
        provenance, raw_path = load_raw_captions(video_dir)
    except (RuntimeError, OSError, EOFError, UnicodeDecodeError, json.JSONDecodeError,
            AttributeError, TypeError, ValueError, RecursionError, zlib.error) as exc:
        return [f"cannot read raw captions for {video_dir}: {exc}"]

    transcript_path = Path(video_dir) / "transcript.md"
    if not transcript_path.is_file():
        return [f"{transcript_path} is missing"]
    try:
        committed = transcript_path.read_bytes()
    except OSError as exc:
        return [f"cannot read transcript {transcript_path}: {exc}"]
    try:
        rendered = render_transcript(build_transcript_lines(raw_path)).encode("utf-8")
    except (OSError, EOFError, UnicodeDecodeError, json.JSONDecodeError,
            AttributeError, TypeError, ValueError, RecursionError, zlib.error) as exc:
        return [f"cannot read raw captions for {video_dir}: {exc}"]

    problems = []
    if committed != rendered:
        problems.append(f"{transcript_path} differs from a re-render of {raw_path}")
    if provenance.get("transcript_sha256") != sha256_hex(committed):
        problems.append(f"{transcript_path} sha256 does not match transcript_sha256 in provenance")
    return problems


def run_rerender(video_dirs):
    failed = 0
    for video_dir in video_dirs:
        try:
            rerender_transcript(video_dir)
        except Exception as exc:
            print(f"error: cannot re-render {video_dir}: {exc}", file=sys.stderr)
            failed += 1
            continue
        print(f"rerendered {Path(video_dir) / 'transcript.md'}")
    return 1 if failed else 0


def run_check(video_dirs):
    failed = 0
    for video_dir in video_dirs:
        problems = check_transcript(video_dir)
        for problem in problems:
            print(f"check failed: {video_dir}: {problem}", file=sys.stderr)
        if problems:
            failed += 1
        else:
            print(f"ok {video_dir}")
    return 1 if failed else 0


def read_video_ids(args_ids):
    """Return video IDs from command-line args, or from stdin if none given."""
    if args_ids:
        return args_ids
    if sys.stdin.isatty():
        return []
    return [line.strip() for line in sys.stdin if line.strip()]


def main():
    parser = argparse.ArgumentParser(
        description="Fetch transcript and metadata for YouTube videos."
    )
    parser.add_argument(
        "video_ids",
        nargs="*",
        help="YouTube video IDs (or pipe them on stdin, one per line)",
    )
    parser.add_argument(
        "--videos-dir",
        default="videos",
        help="Path to the videos/ directory (default: videos)",
    )
    parser.add_argument(
        "--complete-pending",
        metavar="VIDEO_DIR",
        help="review_batch-only: add transcript/raw files to a validated metadata-only pending dir",
    )
    raw_mode = parser.add_mutually_exclusive_group()
    raw_mode.add_argument(
        "--rerender",
        nargs="+",
        metavar="VIDEO_DIR",
        help="rewrite VIDEO_DIR/transcript.md from VIDEO_DIR/raw/ (no network)",
    )
    raw_mode.add_argument(
        "--check",
        nargs="+",
        metavar="VIDEO_DIR",
        help="exit 1 if VIDEO_DIR/transcript.md differs from a re-render of VIDEO_DIR/raw/",
    )
    args = parser.parse_args()

    if (args.rerender or args.check) and (args.video_ids or args.complete_pending):
        parser.error("--rerender/--check cannot be combined with fetch modes")
    if args.complete_pending and len(args.video_ids) != 1:
        parser.error("--complete-pending requires exactly one video ID")
    if args.rerender:
        return run_rerender(args.rerender)
    if args.check:
        return run_check(args.check)

    video_ids = read_video_ids(args.video_ids)

    if not video_ids:
        return 0

    failures = []
    for video_id in video_ids:
        try:
            video_dir = fetch_one_video(
                video_id, args.videos_dir, pending_dir=args.complete_pending
            )
        except Exception as exc:
            print(f"warning: skipping {video_id}: {exc}", file=sys.stderr)
            failures.append(video_id)
            continue
        print(f"wrote {video_dir}")

    if len(failures) == len(video_ids):
        print(
            f"error: all {len(video_ids)} requested video(s) failed: "
            f"{', '.join(failures)}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
