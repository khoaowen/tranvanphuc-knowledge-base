#!/usr/bin/env python3
"""Review summary fidelity locally with a configured model; never modify summary.md."""

import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import queue_state  # noqa: E402
import review_batch  # noqa: E402
import summarize  # noqa: E402
from fidelity import (candidate_chunks, evidence_timestamp_matches, extract_claims,  # noqa: E402,F401
                      resolve_quote)

DEFAULT_CHUNK_CHARS = 40000
OVERLAP_CHARS = 4000
INVALID_RESPONSE_ATTEMPTS = 5
PROGRESS_NAME = ".review-progress.json"
PROGRESS_VERSION = 3

class ReviewError(Exception):
    """Review inputs or model response cannot safely produce a review."""


def summary_hash(content):
    return hashlib.sha256(content).hexdigest()


def chunk_overlapping(entries, max_chars=DEFAULT_CHUNK_CHARS, overlap_chars=OVERLAP_CHARS):
    """Split timestamped entries with a bounded, timestamp-aligned overlap."""
    if max_chars < 1 or overlap_chars < 0 or overlap_chars >= max_chars:
        raise ValueError("chunk sizes must satisfy 0 <= overlap < max_chars")
    chunks, current, size = [], [], 0
    for entry in entries:
        n = len(entry[1]) + 1
        if current and size + n > max_chars:
            chunks.append(current)
            overlap, overlap_size = [], 0
            for prior in reversed(current):
                if overlap_size + len(prior[1]) + 1 > overlap_chars:
                    break
                overlap.insert(0, prior)
                overlap_size += len(prior[1]) + 1
            current, size = overlap, overlap_size
        current.append(entry)
        size += n
    if current:
        chunks.append(current)
    return chunks


def _claims_block(claims):
    out, last = [], None
    for c in claims:
        head = (c["section"], c["question"])
        if head != last:
            out.append(f"\n## {c['section']}" + (f"\n{c['question']}" if c["question"] else ""))
            last = head
        out.append(f"[{c['id']}] {c['claim']}")
    return "\n".join(out)


def prompt_for_review(claims, transcript_chunk, mode, index, total):
    return f'''You are an independent fidelity auditor for a Vietnamese medical-video summary.
The numbered summary claims below were pre-selected as likely to be discussed in PART {index}/{total}
of the transcript. You see only this part, so many claims may not be covered by it. You MUST answer
EVERY listed claim exactly once. If this part does not contain the material for a claim, answer
{{"id": "cNNN", "status": "not_in_slice"}}: that is never a defect, other parts are checked separately.
Use in_slice only when you can point to the transcript text that discusses the claim.
Return exactly one JSON object with keys: claims, concerns, omitted_topics. No prose outside JSON.
claims: array with one object per listed claim: {{"id": "cNNN", "status": "not_in_slice"}} or
{{"id": "cNNN", "status": "in_slice", "supported": bool, "attributed": bool,
"qualifications_preserved": bool, "contradicts": bool, "finding": string, "quote": string}}.
in_slice means this part contains the evidence. quote is ONE exact Vietnamese
fragment copied from the transcript (it may span consecutive lines; omit [HH:MM:SS] prefixes).
supported: the claim is backed by the quote. attributed: statements are attributed to the doctor only
if the transcript proves the doctor said them (not a guest, quoted study or other speaker).
qualifications_preserved: hedges/ranges/conditions (may, about, 4:1-5:1, only in some cases) are not
hardened or dropped. contradicts: the quote says something opposite or materially different (wrong numbers,
years, units). finding: empty string when everything is true, otherwise a short explanation (required
whenever any boolean is unfavourable). Timestamps are computed by the tool; do not provide them.
concerns: array of {{"severity": "minor"|"material", "finding": string, "quote": string}} for localized
problems you find in this part (exact quote required). Do not invent concerns.
omitted_topics: array of {{"topic": string, "quote": string}} for substantive source topics in THIS part
that the summary (claims below) does not cover at all; quote is exact transcript text. Ignore small talk,
ads, greetings and repetition.
This is {mode} {index}/{total}.
<summary_claims>{_claims_block(claims)}
</summary_claims>
<timestamped_transcript>\n{transcript_chunk}\n</timestamped_transcript>'''


def prompt_for_coverage_audit(claims, candidates):
    listing = "\n".join(f"{i}. [{c['timestamp']}] {c['topic']} — \"{c['quote']}\"" for i, c in enumerate(candidates, 1))
    return f'''You are the final whole-summary coverage auditor of a Vietnamese medical-video summary.
Reviewers of each transcript part proposed candidate source topics that they believe the summary omits.
Check each against the complete summary claims below. Keep only topics that are substantive (medical
advice, facts, numbers, warnings, recommendations) and genuinely absent from the whole summary; drop
topics the summary covers elsewhere, and small talk/ads/repetition.
Return exactly one JSON object: {{"coverage_complete": bool, "omissions": [{{"topic": string, "quote": string}}]}}.
coverage_complete is true only if omissions is empty. quote must be copied exactly from a candidate.
No prose outside JSON.
<candidates>\n{listing}\n</candidates>
<summary_claims>{_claims_block(claims)}
</summary_claims>'''


def _loads_object(text, what):
    try:
        data = json.loads(text)
    except (ValueError, TypeError) as exc:
        raise ReviewError(f"malformed {what} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ReviewError(f"{what} must be a JSON object")
    return data


def _nonempty(obj, key, what):
    if not isinstance(obj.get(key), str) or not obj[key].strip():
        raise ReviewError(f"{what} missing {key}")


def parse_model_review(text, transcript, valid_ids, salvage=False):
    """Validate one chunk response. Returns {"claims": [in_slice entries], "concerns", "omitted_topics"}.
    not_in_slice entries (and claims left out) carry no evidence and are dropped.

    All problems are collected and reported together (so the retry feedback is complete). With
    salvage=True (the last attempt) bad entries are handled in the conservative direction only:
    a positive report whose quote is not verbatim is dropped (no evidence is never a pass); a
    negative report (failed check / contradiction) is kept with `unverified_quote` so a defect is
    never silently discarded.
    """
    data = _loads_object(text, "review")
    for key in ("claims", "concerns", "omitted_topics"):
        if not isinstance(data.get(key), list):
            raise ReviewError(f"review {key} must be an array")
    errors, seen, in_slice = [], set(), []
    valid_ids = set(valid_ids)
    for entry in data["claims"]:
        if not isinstance(entry, dict) or entry.get("id") not in valid_ids:
            errors.append(f"claim entry has unknown id: {entry.get('id') if isinstance(entry, dict) else entry!r}")
            continue
        cid = entry["id"]
        if cid in seen:
            errors.append(f"duplicate claim id {cid}")
            continue
        seen.add(cid)
        if entry.get("status") == "not_in_slice":
            continue
        if entry.get("status") != "in_slice":
            errors.append(f"{cid}: status must be in_slice or not_in_slice")
            continue
        flags = ("supported", "attributed", "qualifications_preserved", "contradicts")
        if any(not isinstance(entry.get(key), bool) for key in flags):
            errors.append(f"{cid}: {', '.join(flags)} must all be boolean")
            continue
        defective = (not entry["supported"] or not entry["attributed"] or not entry["qualifications_preserved"]
                     or entry["contradicts"])
        finding = entry.get("finding") if isinstance(entry.get("finding"), str) else ""
        if defective and not finding.strip():
            errors.append(f"{cid}: finding is required when any check fails")
            if not salvage:
                continue
            finding = "(model gave no explanation for the failed check)"
        quote = entry.get("quote") if isinstance(entry.get("quote"), str) else ""
        resolved = resolve_quote(quote, transcript) if quote.strip() else None
        item = {"id": cid, **{k: entry[k] for k in flags}, "finding": finding.strip(), "quote": quote,
                "timestamp": resolved}  # computed from the transcript, never trusted from the model
        if not resolved:
            errors.append(f"{cid}: quote is not verbatim transcript text: {quote[:80]!r}")
            if not (salvage and defective):
                continue
            item["unverified_quote"] = True
        in_slice.append(item)
    concerns = []
    for concern in data["concerns"]:
        if (not isinstance(concern, dict) or concern.get("severity") not in {"minor", "material"}
                or not isinstance(concern.get("finding"), str) or not concern["finding"].strip()):
            errors.append("malformed concern (needs severity minor|material and finding)")
            continue
        quote = concern.get("quote") if isinstance(concern.get("quote"), str) else ""
        resolved = resolve_quote(quote, transcript) if quote.strip() else None
        item = {"severity": concern["severity"], "finding": concern["finding"], "quote": quote, "timestamp": resolved}
        if not resolved:
            errors.append(f"concern quote is not verbatim transcript text: {quote[:80]!r}")
            if not salvage:
                continue
            item["unverified_quote"] = True
        concerns.append(item)
    omitted = []
    for topic in data["omitted_topics"]:
        quote = topic.get("quote") if isinstance(topic, dict) and isinstance(topic.get("quote"), str) else ""
        resolved = resolve_quote(quote, transcript) if quote.strip() else None
        if (not isinstance(topic, dict) or not isinstance(topic.get("topic"), str) or not topic["topic"].strip()
                or not resolved):
            errors.append(f"omitted topic is malformed or its quote is not verbatim: {quote[:80]!r}")
            continue
        omitted.append({"topic": topic["topic"], "quote": quote, "timestamp": resolved})
    missing = sorted(valid_ids - seen)
    if missing:  # at salvage time an unanswered claim is simply not_in_slice (no evidence, never a pass)
        errors.append(f"{len(missing)} listed claims were not answered, e.g. {', '.join(missing[:8])}")
    if errors and not salvage:
        raise ReviewError("; ".join(errors[:12]) + (f" (+{len(errors) - 12} more)" if len(errors) > 12 else ""))
    return {"claims": in_slice, "concerns": concerns, "omitted_topics": omitted}


def parse_coverage_audit(text, transcript):
    data = _loads_object(text, "coverage audit")
    if not isinstance(data.get("coverage_complete"), bool) or not isinstance(data.get("omissions"), list):
        raise ReviewError("coverage audit needs boolean coverage_complete and omissions array")
    omissions = []
    for item in data["omissions"]:
        if not isinstance(item, dict):
            raise ReviewError("malformed omission")
        for key in ("topic", "quote"):
            _nonempty(item, key, "omission")
        resolved = resolve_quote(item["quote"], transcript)
        if not resolved:
            raise ReviewError(f"omission quote is not verbatim transcript text: {item['quote'][:80]!r}")
        omissions.append({"topic": item["topic"], "quote": item["quote"], "timestamp": resolved})
    if data["coverage_complete"] == bool(omissions):
        raise ReviewError("coverage_complete must be true exactly when omissions is empty")
    return {"coverage_complete": data["coverage_complete"], "omissions": omissions}


def aggregate_claim(claim, evidences):
    """Combine every chunk's in-slice report of one claim into a single result.

    pass: >=1 clean verbatim evidence anywhere in the transcript, nothing contradicting or defective.
    fail: contradicted, wrong attribution/qualification, evidence that never supports the claim,
          or no evidence at all.
    flag: one slice calls the claim merely unsupported while another gives clean support.
    """
    clean = [e for e in evidences if e["supported"] and e["attributed"] and e["qualifications_preserved"]
             and not e["contradicts"]]
    hard = [e for e in evidences if e["contradicts"] or not e["attributed"] or not e["qualifications_preserved"]]
    soft = [e for e in evidences if e not in clean and e not in hard]  # merely supported == False
    if hard:
        status, issues = "fail", hard
    elif not clean:
        status, issues = "fail", soft
    elif soft:
        status, issues = "flag", soft
    else:
        status, issues = "pass", []
    best = (clean or evidences or [None])[0]
    result = {"id": claim["id"], "claim": claim["claim"], "section": claim["section"], "status": status,
              "supported": bool(clean) and not hard,
              "attributed": bool(evidences) and all(e["attributed"] for e in evidences),
              "qualifications_preserved": bool(evidences) and all(e["qualifications_preserved"] for e in evidences),
              "timestamp": best["timestamp"] if best else None, "quote": best["quote"] if best else None,
              "evidence": [{k: e[k] for k in ("chunk", "timestamp", "quote")} for e in clean],
              "issues": [{k: e.get(k) for k in ("chunk", "timestamp", "quote", "finding")} for e in issues]}
    for issue, e in zip(result["issues"], issues):
        if e.get("unverified_quote"):
            issue["unverified_quote"] = True
    if not evidences:
        result["issues"] = [{"finding": "no transcript evidence found in any chunk"}]
    return result


def determine_verdict(claims, concerns, coverage_complete):
    if (not claims or not coverage_complete or any(c["status"] == "fail" for c in claims)
            or any(c["severity"] == "material" for c in concerns)):
        return "fail"
    if any(c["status"] == "flag" for c in claims) or concerns:
        return "flag"
    return "pass"


def _ask(client, prompt, parse, label, log, max_retries, sleep):
    """parse(raw, salvage) must raise ReviewError on invalid output; the final attempt is parsed
    with salvage=True (conservative handling of bad entries) before giving up."""
    feedback = ""
    for attempt in range(1, INVALID_RESPONSE_ATTEMPTS + 1):
        raw, _ = summarize.call_with_retry(client, prompt + feedback, max_retries=max_retries, sleep=sleep, log=log)
        last = attempt == INVALID_RESPONSE_ATTEMPTS
        try:
            return parse(raw, last)
        except ReviewError as exc:
            if last:
                raise
            log(f"{label} invalid response ({exc}); retrying")
            feedback = f"\n\nYour previous answer was rejected: {exc}. Re-do it; every quote must be copied exactly from the transcript above."


def review_video(video_dir, client, chunk_chars=DEFAULT_CHUNK_CHARS, overlap_chars=OVERLAP_CHARS, sleep=None, log=lambda m: None, max_retries=5):
    video_dir = Path(video_dir)
    try:
        summary_bytes = (video_dir / "summary.md").read_bytes()
        transcript = (video_dir / "transcript.md").read_text(encoding="utf-8")
    except OSError as exc:
        raise ReviewError(f"cannot read summary/transcript: {exc}") from exc
    digest = summary_hash(summary_bytes)
    existing = queue_state.completed_review(video_dir)
    if existing and existing.get("summary_sha256") == digest:
        log(f"{video_dir.name}: current hash-bound review; skipping")
        return existing
    entries = summarize.parse_transcript(transcript)
    if not entries:
        raise ReviewError("transcript has no timestamped lines")
    summary = summary_bytes.decode("utf-8")
    claims = extract_claims(summary)
    if not claims:
        raise ReviewError("summary has no reviewable claims")
    chunks = chunk_overlapping(entries, chunk_chars, overlap_chars)
    rendered_chunks = [summarize.render_chunk(chunk) for chunk in chunks]
    chosen = candidate_chunks(claims, rendered_chunks)
    reviews = []
    # Validated chunk results are cached (keyed by summary + chunk content) so a rerun after a
    # failure only redoes the failed chunks. Deleted once the review is written.
    progress_path = video_dir / PROGRESS_NAME
    try:
        progress = json.loads(progress_path.read_text(encoding="utf-8"))
        if progress.get("summary_sha256") != digest or progress.get("version") != PROGRESS_VERSION:
            progress = {}
    except (OSError, ValueError, AttributeError):
        progress = {}
    cached = progress.get("chunks", {}) if isinstance(progress, dict) else {}
    def save():
        summarize.write_atomic(progress_path, json.dumps(
            {"summary_sha256": digest, "version": PROGRESS_VERSION, "chunks": cached}, ensure_ascii=False))
    for i, chunk in enumerate(chunks, 1):
        rendered = rendered_chunks[i - 1]
        chunk_claims = [c for c in claims if (i - 1) in chosen[c["id"]]]
        valid_ids = {c["id"] for c in chunk_claims}
        listed = ",".join(sorted(valid_ids))
        key = hashlib.sha256(f"{i}/{len(chunks)}\n{listed}\n{rendered}".encode("utf-8")).hexdigest()
        if key in cached:
            reviews.append(cached[key])
            log(f"{video_dir.name}: chunk {i}/{len(chunks)} restored from progress cache")
            continue
        prompt = prompt_for_review(chunk_claims, rendered, "claim review", i, len(chunks))
        data = _ask(client, prompt, lambda raw, salvage: parse_model_review(raw, rendered, valid_ids, salvage),
                    f"{video_dir.name}: chunk {i}/{len(chunks)}", log, max_retries, sleep)
        for item in data["claims"]:
            item["chunk"] = i
        for item in data["concerns"] + data["omitted_topics"]:
            item["chunk"] = i
        reviews.append(data)
        cached[key] = data
        save()
        log(f"{video_dir.name}: reviewed chunk {i}/{len(chunks)}")
    # Final whole-summary coverage audit over the omissions the chunk reviewers proposed.
    candidates = [t for r in reviews for t in r["omitted_topics"]]
    if candidates:
        key = "coverage:" + hashlib.sha256(json.dumps(candidates, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        if key in cached:
            audit = cached[key]
        else:
            audit = _ask(client, prompt_for_coverage_audit(claims, candidates),
                         lambda raw, salvage: parse_coverage_audit(raw, transcript),
                         f"{video_dir.name}: coverage audit", log, max_retries, sleep)
            cached[key] = audit
            save()
        log(f"{video_dir.name}: coverage audit done")
    else:
        audit = {"coverage_complete": True, "omissions": []}
    by_claim = {}
    for r in reviews:
        for item in r["claims"]:
            by_claim.setdefault(item["id"], []).append(item)
    aggregated = [aggregate_claim(c, by_claim.get(c["id"], [])) for c in claims]
    concerns = [c for r in reviews for c in r["concerns"]]
    result = {
        "video_id": json.loads((video_dir / "metadata.json").read_text(encoding="utf-8"))["video_id"],
        "summary_sha256": digest,
        "verdict": determine_verdict(aggregated, concerns, audit["coverage_complete"]),
        "chunks": len(chunks),
        "claims": aggregated,
        "concerns": concerns,
        "coverage_complete": audit["coverage_complete"],
        "omissions": audit["omissions"],
    }
    # Re-check before writing to avoid binding a review to a concurrent summary edit.
    if summary_hash((video_dir / "summary.md").read_bytes()) != digest:
        raise ReviewError("summary changed during review; result not recorded")
    summarize.write_atomic(video_dir / "review.md", json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    progress_path.unlink(missing_ok=True)
    return result


def commit_review(video_dir, video_id, repo_root):
    rel = os.path.relpath(video_dir, repo_root)
    added = subprocess.run(["git", "add", "--", f"{rel}/review.md"], cwd=repo_root, capture_output=True, text=True)
    if added.returncode:
        raise ReviewError(f"git add failed: {added.stderr.strip()}")
    done = subprocess.run(["git", "commit", "-m", f"content: fidelity review for {video_id} (review-summaries)", "--", f"{rel}/review.md"], cwd=repo_root, capture_output=True, text=True)
    if done.returncode:
        raise ReviewError(f"git commit failed: {(done.stderr or done.stdout).strip()}")


def run_batch(videos_dir, client, repo_root, limit=None, max_retries=5, commit=True, log=summarize.log_stderr):
    result = {"done": [], "skipped": [], "failed": [], "stopped_reset": None}
    newly_completed = 0
    entries = [e for e in queue_state.list_videos(videos_dir) if e["state"] == queue_state.SUMMARIZED]
    for entry in entries:
        if limit is not None and newly_completed >= limit:
            break
        try:
            existing = queue_state.completed_review(entry["dir"])
            current_digest = summary_hash((entry["dir"] / "summary.md").read_bytes())
            if existing and existing.get("summary_sha256") == current_digest:
                log(f"{entry['dir'].name}: current hash-bound review; skipping")
                result["skipped"].append(entry["video_id"])
                continue
            review_video(entry["dir"], client, log=log, max_retries=max_retries)
            if commit:
                commit_review(entry["dir"], entry["video_id"], repo_root)
            result["done"].append(entry["video_id"])
            newly_completed += 1
        except review_batch.UsageLimitReached as exc:
            result["stopped_reset"] = exc.reset_text
            log(f"usage limit reached; stopping. Reset: {exc.reset_text}")
            break
        except (ReviewError, summarize.SummarizeError) as exc:
            log(f"warning: skipping {entry['video_id']}: {exc}")
            result["failed"].append(entry["video_id"])
    return result


def main(argv=None, client=None):
    parser = argparse.ArgumentParser(description="Review video summaries with a local model client.")
    parser.add_argument("--videos-dir", default="videos")
    parser.add_argument("--provider", choices=["codex", "claude"], default="codex")
    parser.add_argument("--model", default="gpt-6.1-sol")
    parser.add_argument("--command", help="provider command; defaults to codex or claude")
    parser.add_argument("--claude-cmd", help=argparse.SUPPRESS)  # backward-compatible alias
    parser.add_argument("--limit", type=int)
    parser.add_argument("--max-retries", type=int, default=5)
    parser.add_argument("--no-commit", action="store_true")
    args = parser.parse_args(argv)
    if client is None:
        command = args.command or args.claude_cmd
        if args.provider == "codex":
            client = review_batch.CodexClient(command or os.environ.get("REVIEW_SUMMARIES_CODEX", "codex"),
                                              args.model)
        else:
            client = review_batch.ClaudeClient(command or os.environ.get("REVIEW_SUMMARIES_CLAUDE", "claude"),
                                               args.model)
    result = run_batch(args.videos_dir, client, Path(__file__).resolve().parent.parent,
                       args.limit, args.max_retries, not args.no_commit)
    print(f"reviewed {len(result['done'])}, failed {len(result['failed'])}")
    if result["stopped_reset"]:
        print(f"stopped at usage limit; resets: {result['stopped_reset']}")
        return 0
    return 1 if result["failed"] and not result["done"] else 0

if __name__ == "__main__":
    sys.exit(main())
