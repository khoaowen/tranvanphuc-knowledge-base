"""Shared evidence helpers for the fidelity review (stdlib only).

Used by review_summaries.py (runs the review) and queue_state.py (validates a stored review),
so both agree on what counts as verbatim transcript evidence and on which claims a summary has.
"""

import re

TIMESTAMP_LINE = re.compile(r"^\[(\d+):(\d{2}):(\d{2})\]\s?(.*)$")
SECTION_HEADING = re.compile(r"^## \[(\d+):(\d{2}):(\d{2})\]\s*(.*?)\s*(?:—\s*https?://\S+)?\s*$")
TOLERANCE = 120  # seconds of slack around a section window (chapters are only roughly aligned)
RANGE = re.compile(r"(\d{2}:\d{2}:\d{2})(?:\s*[-–]\s*(\d{2}:\d{2}:\d{2}))?")


def squash(text):
    """Compare words only: ignore case, punctuation, whitespace and '>>' turn markers."""
    text = re.sub(r"[^\w\s]|_", " ", text.replace(">>", " ")).casefold()
    return " ".join(text.split())


def stamp(seconds):
    return f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"


def to_seconds(value):
    h, m, s = (int(part) for part in value.split(":"))
    return h * 3600 + m * 60 + s


def resolve_quote(quote, transcript, timestamp=None):
    """Find a verbatim quote (it may span consecutive captions) and return its timestamp
    range "HH:MM:SS" / "HH:MM:SS-HH:MM:SS" computed from the transcript, or None."""
    lines = []
    for line in transcript.splitlines():
        parsed = TIMESTAMP_LINE.match(line.strip())
        if parsed:
            at = int(parsed.group(1)) * 3600 + int(parsed.group(2)) * 60 + int(parsed.group(3))
            lines.append((at, squash(parsed.group(4))))
    needle = squash(quote) if isinstance(quote, str) else ""
    if not needle:
        return None
    joined, spans = "", []
    for at, text in lines:
        if joined:
            joined += " "
        spans.append((len(joined), len(joined) + len(text), at))
        joined += text
    positions, offset = [], 0
    while True:
        pos = joined.find(needle, offset)
        if pos == -1:
            break
        times = [at for lo, hi, at in spans if lo < pos + len(needle) and hi > pos]
        if times:
            positions.append((pos, min(times), max(times)))
        offset = pos + 1
    if not positions:
        return None
    selected = positions[0]
    match = RANGE.fullmatch(timestamp or "")
    if match:
        lo, hi = to_seconds(match.group(1)), to_seconds(match.group(2) or match.group(1))
        selected = next((p for p in positions if p[1] <= hi and lo <= p[2]), selected)
    _, first, last = selected
    return stamp(first) if first == last else f"{stamp(first)}-{stamp(last)}"


def evidence_timestamp_matches(quote, timestamp, transcript):
    """True if the quote is verbatim transcript text and the cited range overlaps its captions."""
    resolved = resolve_quote(quote, transcript, timestamp)
    match = RANGE.fullmatch(timestamp or "")
    if not resolved or not match:
        return False
    r = resolved.split("-")
    lo, hi = to_seconds(r[0]), to_seconds(r[-1])
    start, end = to_seconds(match.group(1)), to_seconds(match.group(2) or match.group(1))
    return start <= hi and lo <= end


def _sentences(text):
    parts, start = [], 0
    for m in re.finditer(r"[.!?;]\s+", text):
        rest = text[m.end():m.end() + 1]
        if rest and (rest.isupper() or rest.isdigit() or rest in "\"“(["):
            parts.append(text[start:m.end()].strip())
            start = m.end()
    parts.append(text[start:].strip())
    return [p for p in parts if len(p) > 1]


def extract_claims(summary):
    """Deterministically split a summary into sentence-level claims with stable IDs.

    Skips the metadata header, the health disclaimer, headings and the Q: lines (kept as
    context). Returns [{"id": "c001", "section": ..., "question": ..., "claim": ...}].
    Because the split depends only on the summary bytes, the review tool and the publish
    gate derive identical claims.
    """
    claims, section, question, in_body = [], "", "", False
    start, starts = None, []
    for raw in summary.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            in_body, question = True, ""
            heading = SECTION_HEADING.match(line)
            section = (f"[{heading.group(1).zfill(2)}:{heading.group(2)}:{heading.group(3)}] {heading.group(4)}"
                       if heading else line[3:])
            start = (int(heading.group(1)) * 3600 + int(heading.group(2)) * 60 + int(heading.group(3))) if heading else None
            starts.append(start)
            continue
        if not in_body or line.startswith((">", "#", "|")):
            continue  # tables (e.g. the translation glossary) are reference data, not source claims
        if re.fullmatch(r"\*\*Q:.*\*\*", line):
            question = line[2:-2]
            continue
        body = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", line)
        body = body.replace("**", "").strip()
        # Internal editorial navigation is not a source claim. Restrict exclusion to a
        # standalone, short cross-reference note; assertions remain ordinary claims.
        if re.fullmatch(r"Đã gộp vào mục\s+[^.!?]{1,100}[.!]?", body, re.IGNORECASE):
            continue
        for sentence in _sentences(body):
            claims.append({"id": f"c{len(claims) + 1:03d}", "section": section,
                           "question": question, "claim": sentence,
                           "section_index": len(starts) - 1})
    # Section window: from its own timestamp to the next timestamped section (open-ended for the last).
    for c in claims:
        i = c.pop("section_index")
        c["section_start"] = starts[i] if i >= 0 else None
        later = [t for t in starts if t is not None and c["section_start"] is not None
                 and t > c["section_start"]]
        c["section_end"] = min(later) if later else None
    return claims


def in_section_window(claim, timestamp):
    """True if the evidence range lies (within TOLERANCE) inside the claim's section window."""
    match = RANGE.fullmatch(timestamp or "")
    if not match:
        return False
    lo, hi = to_seconds(match.group(1)), to_seconds(match.group(2) or match.group(1))
    start, end = claim.get("section_start"), claim.get("section_end")
    if start is not None and hi < start - TOLERANCE:
        return False
    if end is not None and lo > end + TOLERANCE:
        return False
    return True


def candidate_chunks(claims, chunk_texts, top=4, threshold=0.5):
    """For each claim id, pick which chunks could hold its evidence by word-bigram overlap:
    the `top` best chunks plus every chunk whose overlap fraction >= threshold. Only a retrieval
    aid: a claim whose evidence sits in an unselected chunk simply fails (never passes)."""
    def grams(text):
        words = squash(text).split()
        return {" ".join(words[i:i + 2]) for i in range(len(words) - 1)} or set(words)
    chunk_grams = [grams(re.sub(r"\[\d+:\d{2}:\d{2}\]", " ", t)) for t in chunk_texts]
    chosen = {}
    for c in claims:
        g = grams(c["claim"])
        scores = sorted(((len(g & cg) / len(g) if g else 0.0, i) for i, cg in enumerate(chunk_grams)), reverse=True)
        pick = {i for _, i in scores[:top]} | {i for sc, i in scores if sc >= threshold}
        chosen[c["id"]] = pick
    return chosen
