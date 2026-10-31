---
title: "Full source-grounded audit of V-Qfwjo28Zg (554 claims)"
type: chore
ticket: 2
status: in-progress
baseline_revision: be95ebdfbbf215147ac404bc5c912cea7dada725
route: full
risk: high
context:
  - ../../../audit-record-format.md
---

<frozen-after-approval reason="coordinator brief, task_85f25bc9311c">

## Intent

**Problem:** Existing artifacts in `../../../audit/V-Qfwjo28Zg/` hold 554 records and a blind second pass, but there is no omission list, no `proposed-corrections.md`, no per-video summary or verification record. `summary.md` and `review.md` were deleted from `videos/` in `4e31e57` (re-queue), so no "current" summary exists at HEAD.

**Approach:** Continue the artifacts (do not restart). Bind the audit to the last committed summary (`git show 4e31e57^:<video dir>/summary.md`, SHA-256 `fbae11bf16fa47c8055fe7b309f45dfeb696db23a0009c593504c1351a98203c`), whose extraction yields exactly the 554 claims. Add the missing deliverables as new files.

## Boundaries & Constraints

**Always:** Write only under `../../../audit/V-Qfwjo28Zg/` and this plan. Every item in `proposed-corrections.md` has status `pending-human-approval`. Preserve speakers and hedges as spoken; no medical correction or outside facts. Report status `blocked`. Commit in logical batches on the current branch.

**Never:** Edit or restore anything in `videos/`; edit `final_records.json`, `claims.json`, or `raw/`; use review.md verdicts or ids as findings; push, open a PR, run a GitHub workflow, or publish; touch pipeline code, tests, or epic-video-knowledge-pipeline tickets; `git stash`.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Non-supported claim | 63 records with class != supported | One correction item per claim | Quote fails verifier: fix the quote from the transcript, never fabricate |
| Unresolved claim (c111, c456, c541) | Ambiguous or absent in the transcript | Item proposes clarifying/removing; c541 has no quote and says so | Stays `unresolved` |
| Omission candidate already covered | Candidate matches a claim in the 554 | Excluded, listed with the covering claim id | Partial or unclear: stays omitted |
| Viewer-comment candidate | Batch 06 items | Excluded per the pass-1 rule unless a safety item | Listed as excluded with the reason |

</frozen-after-approval>

## Code Map

Paths below are relative to the repo root; `A` = `_bmad-output/initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg`, `T` = `videos/2026-10-10-so-135-glutathione-can-bang-oxy-hoa-khu-phuc-hoi-ty-the-va-bao-ve-te-bao-tu-cap-do-phan-tu/transcript.md`.

- `A/final_records.json` -- 554 records: supported 491, attribution_qualification 46, mismatch 14, unresolved 3. Fields include `evidence`, `note`, `pass1_*`, `pass2_*`, optional `reconciliation.rationale`. Read-only.
- `A/raw/batch_*_om.txt` -- pass-1 omission candidates by timestamp range. Use `batch_04_fullread_om.txt`; ignore `batch_04_om.txt`. Batches 07, 08, 13, 14, 23 say `none found`. Readers judged against their batch only, so every candidate must be rechecked against all 554 claims.
- `A/raw/p2_*_notes.txt` -- pass-2 notes.
- `_bmad-output/initiative-tran-van-phuc-knowledge-base/audit/verify_quotes.py` -- `python3 verify_quotes.py <video_id> <transcript.md> <records.json>`; reads each record's `evidence` list of `{quote,timestamp}`.
- `_bmad-output/initiative-tran-van-phuc-knowledge-base/audit/q7uDJG8YQ5c/report.md`, `omissions.md`, `proposed-corrections.md` -- format precedent.
- `scripts/fidelity.py` (`extract_claims(text)`), `scripts/queue_state.py` (`publishable(dir)`). Read-only.

## Tasks & Acceptance

**Execution:**
- [x] `A/check_audit.py` -- read-only checker, stdlib plus `scripts/` imports, run from repo root, exits non-zero on any failure. Checks: extraction of the bound summary via `git show` equals `final_records.json` on id, section, and claim text (554); every record has a class in the four allowed values; every non-unresolved record has evidence; pass 2 covers every non-supported id; `verify_quotes.py` passes on `final_records.json`, on `omission-anchors.json`, and on `proposed-corrections.json`; every correction item is `pending-human-approval` and the items are exactly the 63 non-supported ids; `git diff origin/main -- videos/` is empty; `publishable(video_dir)` is False. Prints counts.
- [x] `A/proposed-corrections.json` -- source data: `[{id, class, current, proposed, why, status, evidence:[{quote,timestamp}]}]`. `current` is the exact claim. `evidence` is copied from the record (c541 empty) or a verifiable quote from `T`. Read the record's note, pass-2 note, reconciliation and the transcript around each quote before writing `proposed`. Write proposals in Vietnamese, keeping speaker and hedge as spoken. Where the only defect is a softened hedge, propose restoring the speaker's own wording. Do not "correct" GSGS to GSSG (c471).
- [x] `A/proposed-corrections.md` -- generated from that JSON, one section per claim with the fields above, status line on each, and a header naming the bound summary SHA.
- [x] `A/omission-anchors.json` and `A/omissions.md` -- consolidate the candidates. Search `final_records.json` claim text for each, exclude those covered (cite the claim id) and those excluded by the viewer-comment/small-talk rule, de-duplicate (for example, Fe2+/catalase appears in batches 04 and 05). Each kept item: topic, timestamp range, verbatim anchor quote, one-line reason it matters. `omission-anchors.json` holds `[{id:"o01", evidence:[{quote,timestamp}]}]` for the verifier. State the method: 23 range-restricted pass-1 reads were consolidated, not a new sequential read.
- [x] `A/audit-summary.md` -- counts per class, omission count, correction count, pass-2 coverage (93: 63 non-supported + 30 sampled supported), the 24 reconciled disagreements listed as human-to-confirm, the bound SHA and the fact that `summary.md` is absent at HEAD, any regenerated summary invalidating these ids, publication status `blocked`.

**Acceptance Criteria:**
- Given the bound summary, when `check_audit.py` runs, then it exits 0 and reports 554 records, 0 quote failures, 63 corrections all pending.
- Given a human reading `proposed-corrections.md`, when they open any item, then the current text, proposed text, why, and supporting quote with timestamp are present, or an explicit statement that no quote exists.
- Given `omissions.md`, when each anchor is searched in the transcript, then it matches at the cited timestamp and no kept item is already stated by a claim.
- Given the finished work, when diffing `videos/` against origin/main, then the diff is empty and `publishable` is False.

## Implementation Notes

Pre-checks done before this plan: extraction matched all 554 records with 0 differences; `verify_quotes.py` passed with 1016 quotes and 0 failures; the transcript is unchanged since `dcbe460`. A numeric heuristic flagged 17 supported records; those checked in the transcript were confirmed, the flags being quote truncation only. Note: c282's `note` is stale pass-1 text; use its reconciliation rationale.

## Plan Change Log

- 2026-10-31: replaced the stale Auto Run stub with this plan.

## Verification

**Commands:**
- `uv run python _bmad-output/initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/check_audit.py` -- expected: exit 0
- `git diff --stat origin/main -- videos/` -- expected: empty
