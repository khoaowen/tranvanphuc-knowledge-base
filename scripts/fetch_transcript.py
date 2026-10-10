#!/usr/bin/env python3
"""Fetch transcript and metadata for YouTube videos into videos/<slug>/.

For each video ID (given as command-line args, or piped on stdin one per
line), uses yt-dlp (no API key) to fetch video metadata and the Vietnamese
auto-caption track (preferring vi-orig, falling back to vi), then writes
videos/<published_at>-<slug>/metadata.json and transcript.md.

A per-video failure (no Vietnamese captions, yt-dlp error) does not abort
the run -- it is warned to stderr and skipped. The run exits non-zero only
if every requested video failed.
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

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


def build_transcript_lines(json3_path):
    """Parse a json3 caption file into timestamped transcript lines.

    Skips bare-newline-only events (segs == [{"utf8": "\\n"}], no
    dDurationMs). Returns a list of "[hh:mm:ss] text" strings.
    """
    with open(json3_path, encoding="utf-8") as f:
        data = json.load(f)

    lines = []
    for event in data.get("events", []):
        segs = event.get("segs")
        if not segs:
            continue
        if "dDurationMs" not in event:
            continue

        text = "".join(seg.get("utf8", "") for seg in segs).strip()
        if not text:
            continue

        start_ms = event.get("tStartMs", 0)
        total_seconds = start_ms // 1000
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        lines.append(f"[{timestamp}] {text}")

    return lines


def write_video_files(videos_dir, metadata, lines):
    """Write metadata.json and transcript.md under videos/<published_at>-<slug>/."""
    upload_date = metadata["upload_date"]
    published_at = f"{upload_date[0:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
    slug = slugify(metadata["title"])
    video_dir = Path(videos_dir) / f"{published_at}-{slug}"
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
    (video_dir / "transcript.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    return video_dir


def fetch_one_video(video_id, videos_dir):
    """Fetch metadata and transcript for a single video, write its files.

    Raises RuntimeError (or propagates one) on any failure; callers should
    treat this as a per-video skip, not a fatal error.
    """
    metadata = fetch_metadata(video_id)
    with tempfile.TemporaryDirectory() as tmp_dir:
        json3_path = fetch_caption_json3(video_id, tmp_dir)
        lines = build_transcript_lines(json3_path)
    return write_video_files(videos_dir, metadata, lines)


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
    args = parser.parse_args()

    video_ids = read_video_ids(args.video_ids)

    if not video_ids:
        return 0

    failures = []
    for video_id in video_ids:
        try:
            video_dir = fetch_one_video(video_id, args.videos_dir)
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
