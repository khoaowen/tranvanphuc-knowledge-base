---
title: 'Full source-grounded audit of q7uDJG8YQ5c (149 claims)'
type: 'chore'
ticket: '1'
created: '2026-10-19'
status: 'built'
baseline_revision: '47c72cecc30ff5e836e868b690352ec17cd613c6'
route: 'full'
route_source: 'auto'
risk: 'high'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Audit artifacts for q7uDJG8YQ5c exist (149 records in `final_records.json`, 22 omissions, 24 corrections, pass 2 by claude-opus-5-5), but they match the pre-correction summary. Ticket 3 changed it (6f6f3e3, b26a10b): it was then 160 claims; b26a10b rewrote it again, so HEAD has 194 claims (sha e8cef3b0e5), 89 unchanged vs the 149 old records and 105 changed/new. The 160-claim records (49) only have review-tool records (`final-claims-audit.json`) lacking section/speaker/class and an independent second pass. `audit-summary.md` says 47 omissions; `omissions.md`, `omissions_full_pass.md` and `report.md` say 22.

**Approach:** Verify the existing audit (option A), then append a supplement: format-compliant records for the 105 changed/new claims, an id remap for the 89 unchanged, a second pass on any non-supported new claim using gpt-6.1-sol, and a re-check of the 22 omissions against the current summary. Nothing existing is overwritten.

## Boundaries & Constraints

**Always:** Audit dir = `../../../spec-summary-source-audit/audit/q7uDJG8YQ5c/`; every output is a new file or a dated append. Verify quotes with `../../../spec-summary-source-audit/audit/verify_quotes.py`. Keep `queue_state.publishable=false` (`scripts/queue_state.py`) and report `blocked`. "Unchanged video/review files" means unchanged by this build versus baseline `47c72ce` (`git diff --stat 47c72ce -- videos/` before and after). Authoritative omissions count: 22. Any new second-pass uses `gpt-6.1-sol` via `codex exec` (human-approved replacement for opus).

**Never:** Edit `videos/`, summary/transcript/review files, `final_records.json`, `pass1.json`, `raw/`, or ticket 1.12; touch the 17 `pending-human-approval` items in `proposed-omissions.md`; apply corrections; commit or publish; reword the 7 claims failing only the timestamp-window rule (c002, c014–c017, c116, c121); infer medical corrections; treat stale `claims-after-apply.md` / `split-claims-audit.*` as current.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Unchanged claim | 89 current claims matching old text | Remapped old id -> current id, old record kept | Unmapped id: report, do not guess |
| Changed/new claim | 105 claims | Full record (section, quote+timestamp, speaker, class, note) | Quote not verbatim: class unresolved |
| Non-supported new claim | class != supported | Blind gpt-6.1-sol second pass | Disagreement: keep non-supported, flag for human |
| Omission now covered | 1 of 22 omissions | Marked "now covered" with current-summary cite | Unclear: stay "still omitted" |

</frozen-after-approval>

## Code Map

- `../../../spec-summary-source-audit/audit/q7uDJG8YQ5c/final_records.json` -- 149 pre-correction records c001–c149; read-only
- `.../final-claims-mapping.md`, `final-claims-audit.json` -- current 160-claim mapping and 49 review-tool records (current sources)
- `.../omissions.md` (22 entries), `audit-summary.md`, `report.md` -- reports; `audit-summary.md` gets an append-only correction note
- `../../../spec-summary-source-audit/audit/verify_quotes.py` -- `verify_quotes.py <video_id> <transcript.md> <records.json> [tol]`
- `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/` -- summary.md, transcript.md (read-only)
- `scripts/fidelity.py` (`extract_claims`), `scripts/queue_state.py` -- claim ids, publishable gate

## Tasks & Acceptance

**Execution:**
- [x] `audit/q7uDJG8YQ5c/verification-report.md` -- verify 149 records/fields, run verify_quotes.py, confirm all 24 non-supported have pass 2, record `git diff 47c72ce` baseline and blocked state
- [x] `audit/q7uDJG8YQ5c/supplement-records.json` -- full-format records for 105 changed/new claims (current 194-claim summary) from the full transcript, plus id remap of the 89; reuse final-claims-audit.json records only where claim text and quote match exactly
- [x] `audit/q7uDJG8YQ5c/supplement-pass2.json` -- blind gpt-6.1-sol re-check of non-supported supplement claims
- [x] `audit/q7uDJG8YQ5c/omissions-recheck.md` -- each of 22 omissions marked still-omitted or now-covered
- [x] `audit/q7uDJG8YQ5c/audit-summary.md` -- append dated note: omissions are 22 (47 was erroneous), supplement and 194-claim state

**Acceptance Criteria:**
- Given supplement and original records, when quotes are verified, then 0 failures and every current claim (194) maps to a record.
- Given all new non-supported claims, when pass 2 completes, then each has an independent result.
- Given the finished build, when diffing `videos/` against 47c72ce, then the diff equals the pre-build diff and `publishable` is false.

## Implementation Notes

## Plan Change Log

- 2026-10-20 (human-directed model replacement): use gpt-6.1-sol via codex exec instead of anthropic/claude-opus-5-5 for the supplement second pass.

- 2026-10-19 (human chose option A): scope is the current HEAD summary, 194 claims (89 unchanged, 105 changed/new), not 160 (111/49). review.md is stale (189 claims, sha f4fd69e4a8); not used.

## Review Triage Log

## Design Notes

Opus review (2026-10-19) found the 149 vs 160 scope gap; the supplement approach avoids a full re-audit while meeting the current-summary requirement.

## Verification

**Commands:**
- `python3 ../../../spec-summary-source-audit/audit/verify_quotes.py q7uDJG8YQ5c <transcript.md> <records.json>` -- expected: 0 failures, for each records file
- `git diff --stat 47c72ce -- videos/` -- expected: identical before and after the build
