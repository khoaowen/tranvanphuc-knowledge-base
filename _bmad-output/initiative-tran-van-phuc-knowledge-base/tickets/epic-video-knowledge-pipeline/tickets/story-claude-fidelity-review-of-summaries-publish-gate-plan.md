---
title: 'Claude fidelity review of summaries (publish gate)'
type: 'feature'
ticket: '12'
created: '2026-10-11'
status: done
baseline_revision: 'e3f269c704190d2de769040a5bebd438addca676'
route: 'full'
route_source: 'auto'
risk: 'high'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/summary-contract.md'
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/epic-video-knowledge-pipeline.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Summaries can be published without an independent check that their claims match the Vietnamese transcript, preserve qualification, attribution and timing, or cover the source faithfully.

**Approach:** Add a local Claude fidelity review command that examines timestamped overlapping transcript chunks, checks every summary claim against transcript evidence, then audits full-summary coverage. It writes a review bound to the exact summary bytes; only a passing, current review permits publication.

## Boundaries & Constraints

**Always:** Check all claims; cite verbatim Vietnamese evidence with timestamp ranges; attribute words to the doctor only when transcript speaker identity supports it. Pass only if every claim is supported, attributed, timestamped and qualifications preserved. Flag localized unresolved/minor concerns; fail clear unsupported or materially misleading defects. Pass alone permits publication; flag, fail, missing, and stale reviews block. Never modify summary.md. Reuse entry 9 queue/state, resume, commit-as-it-goes, backoff, usage-limit behavior and injectable Claude command. Keep operation local; no subscription login in CI.

**Never:** Do not edit summaries during review. Do not implement answer-time GPT citations/deep links; that is a separate follow-up. Do not modify unrelated files or start other tickets.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Supported | Accurate summary and transcript | Pass review bound to summary hash; video publishable | None |
| Localized concern | Minor/unresolved claim | Flag with quote/timestamp; publication blocked | Review remains recorded |
| Material defect | Invented/hardened/wrong attribution or timestamp | Fail with evidence; publication blocked | No summary mutation |
| Long transcript | Claims early, middle, late and across chunk boundaries | Overlapping timestamped chunks checked and whole-summary coverage audited | Missing evidence cannot pass |
| Summary changed | Existing pass then changed summary bytes | Old review becomes stale; video unpublished until re-review | Re-run only skips current hash-bound reviews |
| Usage limit | Claude reports limit/reset | Stop cleanly and report reset time | Preserve completed work |

</frozen-after-approval>

## Code Map

- `scripts/queue_state.py` -- shared `list_videos`, `video_state`, and `todo`; reuse and extend state derivation only as needed for review/publish gating.
- `scripts/review_batch.py`, `review-batch` -- local runner, injectable Claude subprocess, resumability, backoff, usage-limit handling, and per-video commits; follow these conventions.
- `scripts/summarize.py` -- transcript timestamp format and parsing/chunk conventions; do not change summary generation.
- `tests/test_review_batch.py`, `tests/test_summarize.py` -- unittest style and stub/temporary-repository patterns.
- `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/` and `videos/2026-10-10-so-135-glutathione-can-bang-oxy-hoa-khu-phuc-hoi-ty-the-va-bao-ve-te-bao-tu-cap-do-phan-tu/` -- seed and second specified real video.
- `summary-contract.md` -- structural and fidelity requirements; epic decision dated 2026-10-11 defines overlapping chunks, coverage audit, verdict thresholds, publish block, and scope boundary.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/review_summaries.py` and `review-summaries` -- chunked Claude review, evidence/verdict validation, exact-summary binding, resume and local CLI; reuse existing queue patterns.
- [ ] `scripts/queue_state.py` and publishing integration -- represent review freshness and allow publication only with current pass; preserve existing queue helper behavior.
- [ ] `tests/test_review_summaries.py`, related publish tests -- fixtures for pass/flag/fail, attribution/qualification/timestamp defects, coverage, overlap boundaries, stale hashes and usage limit.
- [ ] `docs/review-summaries.md` -- local operation, verdict meanings, evidence format and limitations.

**Acceptance Criteria:**
- Given both specified real videos, when run, then each receives a committed review bound to its current summary.
- Given clean, minor-concern, and material-defect fixtures, when reviewed, then verdicts are pass, flag, and fail respectively, with flag/fail unpublished.
- Given long transcripts and claims at early/middle/late/boundary positions, when reviewed, then every claim is evidenced and full-summary coverage is audited.
- Given a passed review and a subsequent summary edit, when publication is evaluated, then the video is unpublished until a current re-review passes.
- Given existing review state, when rerun, then only hash-current reviews are skipped; usage limit stops cleanly and reports reset time.

## Implementation Notes

Original implementation checks passed; both specified real-video review artifacts were subsequently created and have fail verdicts (seed: 131 pass, 17 fail, 1 flag; second: 403 pass, 155 fail, 3 flag). These summaries and review artifacts are preserved untouched. Following independent review, six code defects were fixed in `scripts/fidelity.py`, `scripts/queue_state.py`, and `scripts/review_summaries.py`, with regression coverage in `tests/test_review_summaries.py`; docs updated. Focused suite: `python -m unittest discover -s tests -p 'test_review_summaries.py'` — 43 passed. Broader suite: `python -m unittest discover -s tests` — 85 passed. No model calls, summary edits, commits, or publication performed. Ticket is not marked complete; the genuine c160 wrong-section timestamp and real-review fail findings remain.

**Update — temporary reviewer substitution and per-claim aggregation.** The user approved temporarily using OpenAI GPT-6 Luna (`pi --provider openai-codex --model gpt-6-luna -p --mode text`, wrapped by a local script passed via `--claude-cmd`) in place of Claude, with the same evidence, verdict, attribution, timestamp, qualification and coverage requirements. The first design (whole summary + one transcript slice per chunk, per-chunk `coverage_complete`) produced mostly artifacts: claims about out-of-slice material were marked unsupported and coverage was declared incomplete. It was replaced by per-claim aggregation: the summary is deterministically split into stable-ID claims (`scripts/fidelity.py`), each chunk reports only claims it can see (`in_slice`/`not_in_slice`), claims are aggregated across chunks (pass needs one clean verbatim quote and no contradiction; no evidence anywhere fails), and a single final whole-summary coverage audit replaces per-chunk coverage flags. Quote timestamps are tool-computed, invalid model responses are retried, and chunk results are cached in a gitignored progress file. `queue_state.current_review()` now requires one-to-one claim match with the current summary and re-verifies every evidence quote. See `docs/review-summaries.md`.

## Plan Change Log

- 2026-10-14 — Approved code-only remediation of six independently verified issues; separated completed-review resumption from strict publication eligibility, corrected limit accounting, chronological section windows, strict evidence-window validation, repeated-quote resolution, and narrow editorial-note exclusion. Preserved all real summaries and review artifacts; added focused regression tests. Verification: 43 focused and 85 total tests pass; no model calls or commits. Remaining real-review defects are unresolved and no completion/publication claim is made.


## Review Triage Log

- high — `scripts/queue_state.py`: malformed current-hash pass records could omit claim text and still pass the publication gate. Verified persisted reviews now require a non-empty claim string.
- medium — `scripts/review_summaries.py`: an empty claims array in one covered transcript chunk incorrectly failed the overall review. Verdict now fails only when no reviewed chunk contains any claims; complete coverage remains required.
- false — `scripts/queue_state.py`: no current publishing/consolidation path exists to bypass this gate; repository search found only the upcoming entry 1.10 validator contract. `publishable()` checks current hash and pass, and docs state downstream validator/consolidation must call it.
- low — `scripts/review_batch.py`: a session-limit response without reset wording reported the full error blob as reset text. It now reports `not provided by Claude`.

## Design Notes

Review identity must be computed from exact summary content (SHA-256 is suitable), and freshness compared at every publish eligibility check, not merely at review-run time. Overlapping timestamp-aligned chunks reduce boundary misses, while a final full-summary audit prevents the chunking strategy from treating unseen source coverage as proof. Evidence must quote source text, not model paraphrases. A malformed or inconclusive review must never yield pass.

## Verification

**Commands:**
- `python -m unittest discover tests` -- expected: all relevant unit and integration tests pass.
- `uv run _bmad/method/scripts/tickets.py --project-root . validate` -- expected: ticket tree validates without unrelated changes.
- Run `./review-summaries` against both specified real videos with locally authenticated Claude -- expected: committed hash-bound review for each; no summary edits.
- Exercise fixture tests for usage-limit stop/reset handling and stale review invalidation.
