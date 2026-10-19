#!/usr/bin/env python3
"""CI validator and publish gate for videos/*/summary.md (read-only, stdlib only).

Checks each summary against summary-contract.md, rejects stale ones, and derives
`published` from files: valid + not stale + a hash-bound passing review
(queue_state.publishable). Never writes transcript.md or summary.md.

Exit codes: 0 all summarized videos valid; 1 some summarized video failed a check;
2 transcript.md changed while validating (hard failure).
"""

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fidelity  # noqa: E402
import queue_state  # noqa: E402
from summarize import DISCLAIMER_BANNER  # noqa: E402

PUBLISHED = "published"
MIN_RATIO = 0.02  # summary chars / transcript chars
MAX_RATIO = 0.50
STALE_FILE = "summary.stale"
DEFAULT_VOCABULARY = Path("topics/vocabulary.md")

LINK = re.compile(r"https?://www\.youtube\.com/watch\?v=([\w-]+)&t=(\d+)s")
HEADER_FIELDS = ("Video ID", "Published", "URL", "Topics")


class TranscriptChanged(Exception):
    pass


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe_sha256(path):
    """SHA-256 of a file, None when it is missing or unreadable."""
    try:
        return sha256(path)
    except OSError:
        return None


def norm(tag):
    """Tag comparison key: NFC-normalized and casefolded (Vietnamese has composed/decomposed forms)."""
    return unicodedata.normalize("NFC", tag).strip().casefold()


def valid_duration(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def load_vocabulary(path):
    """Return the lowercase tag set, or None when the vocabulary file does not exist.

    Format (entry 4 seeds it): one tag per line, bullets optional, or comma separated; '#' lines ignored.
    """
    path = Path(path) if path else None
    if not path or not path.is_file():
        return None
    tags = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for part in re.sub(r"^[-*+]\s+", "", line).split(","):
            if part.strip():
                tags.add(norm(part))
    return tags


def is_stale(video_dir):
    marker = Path(video_dir) / STALE_FILE
    try:
        return marker.read_text(encoding="utf-8").strip() == sha256(Path(video_dir) / "summary.md")
    except OSError:
        return False


def mark_stale(video_dir):
    """Record the current summary's SHA-256 so it is ineligible until it changes."""
    video_dir = Path(video_dir)
    (video_dir / STALE_FILE).write_text(sha256(video_dir / "summary.md") + "\n", encoding="utf-8")


def check_summary(video_dir, vocabulary):
    """Return a list of human-readable reasons the summary violates the contract."""
    video_dir = Path(video_dir)
    reasons = []
    try:
        summary = (video_dir / "summary.md").read_text(encoding="utf-8")
        transcript = (video_dir / "transcript.md").read_text(encoding="utf-8")
        meta = json.loads((video_dir / "metadata.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"unreadable input: {exc}"]
    video_id = meta.get("video_id") if isinstance(meta, dict) else None
    duration = meta.get("duration") if isinstance(meta, dict) else None
    lines = summary.splitlines()
    if not valid_duration(duration):
        reasons.append("metadata: duration missing or invalid")
        duration = None

    # header
    if not (lines and lines[0].startswith("# ") and lines[0][2:].strip()):
        reasons.append("header: missing title")
    fields = {}
    for line in lines:
        m = re.match(r"^- \*\*([^:*]+):\*\*\s*(.*)$", line)
        if m:
            fields.setdefault(m.group(1).strip(), m.group(2).strip())
        if line.startswith("## "):
            break
    for name in HEADER_FIELDS:
        if not fields.get(name):
            reasons.append(f"header: missing {name}")
    if video_id and fields.get("Video ID") and fields["Video ID"] != video_id:
        reasons.append("header: Video ID differs from metadata.json")

    # disclaimer
    if DISCLAIMER_BANNER not in summary:
        reasons.append("missing disclaimer banner")

    # topic sections
    sections = [(i, fidelity.SECTION_HEADING.match(l)) for i, l in enumerate(lines) if l.startswith("## ") and l.strip() != "## Glossary"]
    sections = [(i, m) for i, m in sections if m]
    if not sections:
        reasons.append("no timestamped topic section")
    bounds = [i for i, _ in sections] + [next((n for n, l in enumerate(lines) if l.strip() == "## Glossary"), len(lines))]
    for k, (i, m) in enumerate(sections):
        seconds = fidelity.to_seconds(":".join(m.groups()[:3]))
        label = f"section [{m.group(1)}:{m.group(2)}:{m.group(3)}]"
        if duration is not None and seconds > duration:
            reasons.append(f"{label}: time beyond video duration")
        link = LINK.search(lines[i])
        if not link:
            reasons.append(f"{label}: missing ?t= link")
        else:
            if video_id and link.group(1) != video_id:
                reasons.append(f"{label}: link points at another video")
            if int(link.group(2)) != seconds:
                reasons.append(f"{label}: ?t= differs from heading time")
            if duration is not None and int(link.group(2)) > duration:
                reasons.append(f"{label}: ?t= beyond video duration")
        body = [l.strip() for l in lines[i + 1:max(bounds[k + 1], i + 1)] if l.strip()]
        merged = len(body) == 1 and re.fullmatch(r"Đã gộp vào mục\s+[^.!?]{1,100}[.!]?", body[0], re.I)
        if not merged and not any(l.startswith("**Q:") for l in body):
            reasons.append(f"{label}: no **Q: line")

    # glossary
    gloss = re.search(r"^## Glossary\s*$(.*)", summary, re.M | re.S)
    if not gloss:
        reasons.append("missing Glossary")
    else:
        head = next((l for l in gloss.group(1).splitlines() if l.strip().startswith("|")), "")
        cells = [c.strip().casefold() for c in head.strip().strip("|").split("|")]
        if cells[:3] != ["vietnamese", "english", "french"]:
            reasons.append("Glossary lacks Vietnamese | English | French columns")

    # length
    if transcript:
        ratio = len(summary) / len(transcript)
        if ratio < MIN_RATIO:
            reasons.append(f"summary too short ({ratio:.1%} of transcript)")
        elif ratio > MAX_RATIO:
            reasons.append(f"summary too long ({ratio:.1%} of transcript)")
    else:
        reasons.append("empty transcript")

    # tags
    if vocabulary is not None and fields.get("Topics"):
        unknown = [t.strip() for t in fields["Topics"].split(",") if t.strip() and norm(t) not in vocabulary]
        if unknown:
            reasons.append("tags outside vocabulary: " + ", ".join(unknown))

    if is_stale(video_dir):
        reasons.append("stale: regeneration failed, summary unchanged")
    return reasons


def validate_video(video_dir, vocabulary_path=DEFAULT_VOCABULARY):
    """Return {state, reasons, published}; raises TranscriptChanged if transcript.md was altered."""
    video_dir = Path(video_dir)
    transcript = video_dir / "transcript.md"
    before = safe_sha256(transcript)
    state = queue_state.video_state(video_dir)
    reasons, published, review_missing = [], False, False
    if state == queue_state.SUMMARIZED:
        try:
            vocabulary = load_vocabulary(vocabulary_path)
        except (OSError, ValueError) as exc:
            vocabulary, reasons = None, [f"vocabulary unreadable: {exc}"]
        reasons = reasons + check_summary(video_dir, vocabulary)
        if not reasons:
            published = queue_state.publishable(video_dir)
            if not published:
                review_missing = True
                reasons = ["no passing review bound to this summary"]
    after = safe_sha256(transcript)
    if before != after:
        raise TranscriptChanged(video_dir.name)
    return {"state": PUBLISHED if published else state, "reasons": reasons, "published": published,
            "review_missing": review_missing,
            "invalid": state == queue_state.SUMMARIZED and bool(reasons) and not review_missing}


def video_publish_state(video_dir, vocabulary_path=DEFAULT_VOCABULARY):
    return validate_video(video_dir, vocabulary_path)["state"]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--videos-dir", default="videos")
    ap.add_argument("--vocabulary", default=str(DEFAULT_VOCABULARY))
    ap.add_argument("--mark-stale", metavar="VIDEO_ID")
    args = ap.parse_args(argv)

    if args.mark_stale:
        match = [e for e in queue_state.list_videos(args.videos_dir) if e["video_id"] == args.mark_stale]
        if not match or not (match[0]["dir"] / "summary.md").is_file():
            print(f"{args.mark_stale}: no summary to mark stale", file=sys.stderr)
            return 1
        mark_stale(match[0]["dir"])
        print(f"{args.mark_stale}: marked stale")
        return 0

    failed = False
    for entry in queue_state.list_videos(args.videos_dir):
        try:
            result = validate_video(entry["dir"], args.vocabulary)
        except TranscriptChanged as exc:
            print(f"{entry['dir'].name}: transcript changed during validation ({exc})", file=sys.stderr)
            return 2
        failed = failed or result["invalid"]
        print(f"{entry['dir'].name}: {result['state']}" + (f" ({'; '.join(result['reasons'])})" if result["reasons"] else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
