---
title: 'CI validator and publish gate'
type: 'feature'
ticket: '10'
created: '2026-10-19'
status: 'built'
baseline_revision: '8325a516d9447f654f9cf7c0ea17cc2a864de3f2'
route: 'full'
route_source: 'auto'
risk: 'medium'
review: 'quick'
review_source: 'pinned'
lenses_ran: []
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/summary-contract.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Nothing yet decides whether a `summary.md` may be published or consolidated. `summary-contract.md` names `scripts/validate_summaries.py` as the gate, but it does not exist, and `queue_state` only knows pending/transcribed/summarized.

**Approach:** Add a stdlib, read-only `scripts/validate_summaries.py` that checks each summary against the contract, rejects stale ones, and derives `published` from files: valid + current + not stale + a hash-bound `pass` review (via `queue_state.publishable`). Exit non-zero on any invalid video so CI can gate the commit.

## Boundaries & Constraints

**Always:** Never write `transcript.md` or `summary.md`; hash `transcript.md` before and after and fail loudly if it changed. Reuse `queue_state` (`list_videos`, `publishable`) and `fidelity`; the schema is the one `summarize.py` emits. The vocabulary path is a parameter (default `topics/vocabulary.md`); tags are enforced only when that file exists. A video is `published` only if every check passes AND `queue_state.publishable` is true. Output one line per video (`slug: state` plus reasons) and exit 1 if any summarized video fails a check.

**Never:** Edit `summarize.py`, `review_batch.py`, `review_summaries.py` or the workflow (entry 11 wires the gate in). No network, no Claude/Gemini calls. No fixing or rewriting summaries. No new third-party dependency.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Published | Valid summary + passing review bound to its hash | state `published`, exit 0 | — |
| Structure | Missing header field, disclaimer, `## [..]` section with valid `?t=` link, `**Q:` line, or Vietnamese/English/French glossary | `summarized`, reason named, exit 1 | Rejected, unpublished |
| Timestamp | Section time or `?t=` beyond `metadata.json` `duration` | rejected | Rejected |
| Length | Summary under 2% or over 50% of transcript characters | rejected | Rejected |
| Tags | Tag not in vocabulary (file exists) | rejected; no vocab file → not checked | Rejected |
| Stale | `summary.stale` holds the current summary's SHA-256 (regeneration failed) | ineligible, even with a matching `pass` review | Rejected; prior summary untouched |
| Review | `review.md` missing, `flag`, `fail`, or bound to different bytes | `summarized`, not published | Not an error for CI exit code |
| Transcript changed | Transcript bytes differ after validation | abort, exit 2 | Hard failure |

</frozen-after-approval>

## Code Map

- `scripts/queue_state.py` -- `list_videos`, `video_state`, `publishable`, `current_review`; reuse; do not change its three states.
- `scripts/fidelity.py` -- `SECTION_HEADING`, `to_seconds`; reuse for timestamps.
- `scripts/summarize.py` -- `DISCLAIMER_BANNER` constant (verbatim), `SECTION_SCHEMA`, header shape (`- **Video ID:**`, `Published`, `URL`, `Topics`), `## Glossary` table `Vietnamese | English | French`, links `…&t=<s>s`. Import `DISCLAIMER_BANNER`.
- `videos/*/metadata.json` -- `duration` (seconds), `video_id`; `summary.md`/`transcript.md` neighbours.
- `tests/test_review_batch.py` -- unittest + tempdir fixture pattern to copy.
- `_bmad-output/.../spec-tran-van-phuc-kb/summary-contract.md` -- CI validation rules; real ratios: summary/transcript is 0.15 and 0.22.
- Do not touch `videos/`, `topics/` (absent), `.github/workflows/`.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/validate_summaries.py` -- `validate_video(dir, vocabulary_path)`, `video_publish_state`, `mark_stale(dir)` (writes `summary.stale` with the summary SHA-256), CLI `--videos-dir`, `--vocabulary`, `--mark-stale <video_id>` -- the gate
- [ ] `tests/test_validate_summaries.py` -- fixture per I/O row (valid, bad schema, no disclaimer, timestamp past duration, too short, too long, unknown tag, no vocab file, stale marker, no/pending/flag/fail/hash-mismatched review); transcript and prior-summary bytes unchanged; stale marker cleared by a changed summary

**Acceptance Criteria:**
- Given a valid summary with a passing hash-bound review, when validated, then it reads `published` and exit is 0.
- Given each failure fixture, when validated, then it is not published and the reason is printed.
- Given `--mark-stale`, when run on a video, then `summary.md` is byte-identical, the video is ineligible, and a later regenerated summary (different hash) is judged on validation and review again.
- Given the two real videos, when run, then nothing crashes, and `published` appears only if their review is a strict pass.

## Implementation Notes

Implemented directly (no subagents authorized). Quick review lens not run via subagent; self-reviewed against the matrix. Cross-reference sections (`Đã gộp vào mục …`) are exempt from the `**Q:` rule, matching `fidelity.extract_claims`; needed for the real V-Qfwjo28Zg summary.

## Plan Change Log

## Review Triage Log

## Design Notes

- Stale marker holds a SHA-256 so it expires on regeneration without any cleanup step; entry 11 calls `--mark-stale` when Gemini regeneration fails.
- Vocabulary format is not yet defined (entry 4 seeds it): accept one tag per line, bullets optional, or comma-separated; `#` lines ignored; case-insensitive match.
- Length bounds are module constants (2% to 50%) so they are easy to tune.

## Verification

**Commands:**
- `python3 -m unittest tests.test_validate_summaries -v` -- expected: all pass
- `python3 -m unittest discover -s tests` -- expected: existing suites still pass
- `python3 scripts/validate_summaries.py --videos-dir videos` -- expected: one line per video, no traceback
