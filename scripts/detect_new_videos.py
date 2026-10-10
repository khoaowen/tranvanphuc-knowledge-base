#!/usr/bin/env python3
"""Detect new videos on Dr. Tran Van Phuc's YouTube channel.

Lists the channel's uploaded video IDs via yt-dlp (no API key needed),
diffs against video IDs already recorded in videos/*/metadata.json, and
prints the new-video-id list, one per line, to stdout.

Known video IDs are read only from metadata.json's `video_id` field, never
from folder names (folder slugs are human-oriented, not machine IDs).
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_CHANNEL_ID = "UC79E6KatRfXbmdWVWGncsew"


def get_channel_video_ids(channel_id):
    """Return an ordered list of video IDs uploaded by the given channel.

    Exits non-zero with a stderr message if yt-dlp fails or returns no IDs.
    """
    url = f"https://www.youtube.com/channel/{channel_id}/videos"
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--print", "%(id)s", url],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        print("error: yt-dlp is not installed or not on PATH", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print(
            f"error: yt-dlp timed out listing channel {channel_id}",
            file=sys.stderr,
        )
        sys.exit(1)

    if result.returncode != 0:
        print(
            f"error: yt-dlp failed (exit {result.returncode}) listing channel "
            f"{channel_id}: {result.stderr.strip()}",
            file=sys.stderr,
        )
        sys.exit(1)

    video_ids = [line.strip() for line in result.stdout.splitlines() if line.strip()]

    if not video_ids:
        print(
            f"error: yt-dlp returned no video IDs for channel {channel_id}",
            file=sys.stderr,
        )
        sys.exit(1)

    return video_ids


def get_known_video_ids(videos_dir):
    """Return the set of video IDs already recorded under videos_dir.

    Treats a missing or empty videos/ directory as zero known videos.
    Skips (with a stderr warning) any metadata.json that is missing,
    malformed, or lacks a video_id field.
    """
    known_ids = set()
    videos_path = Path(videos_dir)

    if not videos_path.is_dir():
        return known_ids

    for metadata_path in sorted(videos_path.glob("*/metadata.json")):
        try:
            with open(metadata_path, encoding="utf-8") as f:
                metadata = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            print(
                f"warning: skipping unreadable metadata file {metadata_path}: {exc}",
                file=sys.stderr,
            )
            continue

        video_id = metadata.get("video_id")
        if not video_id:
            print(
                f"warning: skipping {metadata_path}: missing 'video_id' field",
                file=sys.stderr,
            )
            continue

        known_ids.add(video_id)

    return known_ids


def main():
    parser = argparse.ArgumentParser(
        description="Detect new videos on the channel not yet recorded in videos/."
    )
    parser.add_argument(
        "--channel-id",
        default=DEFAULT_CHANNEL_ID,
        help=f"YouTube channel ID (default: {DEFAULT_CHANNEL_ID})",
    )
    parser.add_argument(
        "--videos-dir",
        default="videos",
        help="Path to the videos/ directory (default: videos)",
    )
    args = parser.parse_args()

    channel_video_ids = get_channel_video_ids(args.channel_id)
    known_video_ids = get_known_video_ids(args.videos_dir)

    new_video_ids = [vid for vid in channel_video_ids if vid not in known_video_ids]

    for video_id in new_video_ids:
        print(video_id)

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write("new_videos<<EOF\n")
            f.write("\n".join(new_video_ids))
            f.write("\nEOF\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
