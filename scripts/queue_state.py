"""Shared queue/state helper: derive each video's state from files.

States (derived, never stored):
  pending      metadata.json exists, transcript.md does not
  transcribed  transcript.md exists, summary.md does not
  summarized   summary.md exists

Used by review_batch.py (entry 9) and the validator (entry 10).
Stdlib only.
"""

import json
from pathlib import Path

PENDING = "pending"
TRANSCRIBED = "transcribed"
SUMMARIZED = "summarized"


def video_state(video_dir):
    video_dir = Path(video_dir)
    if (video_dir / "summary.md").is_file():
        return SUMMARIZED
    if (video_dir / "transcript.md").is_file():
        return TRANSCRIBED
    return PENDING


def list_videos(videos_dir):
    """Return [{dir, video_id, state}] for every videos/*/metadata.json, newest first.

    Directory names start with YYYY-MM-DD, so a reverse name sort is newest first.
    Unreadable metadata is skipped.
    """
    videos_dir = Path(videos_dir)
    if not videos_dir.is_dir():
        return []
    entries = []
    for metadata_path in videos_dir.glob("*/metadata.json"):
        try:
            video_id = json.loads(metadata_path.read_text(encoding="utf-8"))["video_id"]
        except (OSError, ValueError, KeyError, TypeError):
            continue
        video_dir = metadata_path.parent
        entries.append({"dir": video_dir, "video_id": video_id, "state": video_state(video_dir)})
    entries.sort(key=lambda e: e["dir"].name, reverse=True)
    return entries


def todo(videos_dir):
    """Videos without a summary (pending or transcribed), newest first."""
    return [e for e in list_videos(videos_dir) if e["state"] != SUMMARIZED]
