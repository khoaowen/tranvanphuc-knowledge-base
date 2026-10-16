"""Shared queue/state helper: derive each video's state from files.

States (derived, never stored):
  pending      metadata.json exists, transcript.md does not
  transcribed  transcript.md exists, summary.md does not
  summarized   summary.md exists

Used by review_batch.py (entry 9) and the validator (entry 10).
Stdlib only.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fidelity  # noqa: E402

PENDING = "pending"
TRANSCRIBED = "transcribed"
SUMMARIZED = "summarized"
REVIEW_PASS = "pass"


def completed_review(video_dir):
    """Return a structurally valid review bound to the current summary, whatever its verdict."""
    video_dir = Path(video_dir)
    try:
        data = json.loads((video_dir / "review.md").read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("verdict") not in {"pass", "flag", "fail"}:
            return None
        digest = __import__("hashlib").sha256((video_dir / "summary.md").read_bytes()).hexdigest()
        if data.get("summary_sha256") != digest:
            return None
        claims, concerns = data.get("claims"), data.get("concerns")
        if not isinstance(claims, list) or not claims or not isinstance(concerns, list):
            return None
        if not isinstance(data.get("coverage_complete"), bool) or not isinstance(data.get("omissions"), list):
            return None
        transcript = (video_dir / "transcript.md").read_text(encoding="utf-8")
        expected = fidelity.extract_claims((video_dir / "summary.md").read_text(encoding="utf-8"))
        if [(c.get("id"), c.get("claim")) for c in claims if isinstance(c, dict)] != \
                [(c["id"], c["claim"]) for c in expected] or len(claims) != len(expected):
            return None  # every summary claim must be reviewed, no more and no fewer
        for claim in claims:
            if (claim.get("status") not in {"pass", "flag", "fail"}
                    or not isinstance(claim.get("supported"), bool)
                    or not isinstance(claim.get("attributed"), bool)
                    or not isinstance(claim.get("qualifications_preserved"), bool)
                    or not isinstance(claim.get("evidence"), list)
                    or not isinstance(claim.get("issues"), list)):
                return None
            for ev in claim["evidence"]:
                if (not isinstance(ev, dict)
                        or not fidelity.evidence_timestamp_matches(ev.get("quote"), ev.get("timestamp"), transcript)):
                    return None
        if any(not isinstance(c, dict) for c in concerns):
            return None
        return data
    except (OSError, ValueError, TypeError, AttributeError, KeyError):
        return None


def current_review(video_dir):
    """Return a strictly publication-eligible pass, or None."""
    video_dir = Path(video_dir)
    data = completed_review(video_dir)
    if not data or data.get("verdict") != REVIEW_PASS or data.get("coverage_complete") is not True or data.get("omissions") != []:
        return None
    try:
        transcript = (video_dir / "transcript.md").read_text(encoding="utf-8")
        expected = fidelity.extract_claims((video_dir / "summary.md").read_text(encoding="utf-8"))
        claims = data["claims"]
        if [(c.get("id"), c.get("claim")) for c in claims] != [(c["id"], c["claim"]) for c in expected]:
            return None
        if data.get("concerns") or any(c["status"] != "pass" or c.get("issues") for c in claims):
            return None
        for claim, derived in zip(claims, expected):
            if (any(claim.get(k) is not True for k in ("supported", "attributed", "qualifications_preserved"))
                    or not claim["evidence"]):
                return None
            for ev in claim["evidence"]:
                if (not fidelity.evidence_timestamp_matches(ev.get("quote"), ev.get("timestamp"), transcript)
                        or not fidelity.in_section_window(derived, ev.get("timestamp"))):
                    return None
        return data
    except (OSError, ValueError, TypeError, AttributeError, KeyError):
        return None


def publishable(video_dir):
    """Publication requires a passing review of the exact current summary bytes."""
    video_dir = Path(video_dir)
    try:
        summary_hash = __import__("hashlib").sha256((video_dir / "summary.md").read_bytes()).hexdigest()
    except OSError:
        return False
    review = current_review(video_dir)
    return bool(review and review.get("summary_sha256") == summary_hash
                and review.get("verdict") == REVIEW_PASS)


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
