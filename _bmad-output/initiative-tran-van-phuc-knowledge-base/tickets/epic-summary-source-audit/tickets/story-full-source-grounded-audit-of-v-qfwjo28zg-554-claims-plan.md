---
title: "Full source-grounded audit of V-Qfwjo28Zg (554 claims)"
type: chore
ticket: 2
status: 'done'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
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

## Review Triage Log

Quick lens, 2026-10-31. Seven findings verified real and patched in `4e177a4`: c070 speaker (medium), c488 settled wording (medium), c377 dropped unit (medium), c135 quote (low), o05 coverage (low), o22 safety reason (low), checker drift coverage (low).

## Code Review

### 2026-11-06
Chunk 1 of N (audit/V-Qfwjo28Zg core files; regenerated/, regenerated-timefix/, revised-summary-draft.md and the other tickets' files not yet reviewed). 3 `decision-needed`, 2 `patch`, 1 `defer`, 3 rejected.

- [x] [Review][Patch] (decided 1a) Overlapping correction ids c013, c156, c275 — They exist in both proposed-corrections.* and additional-corrections.* with different text, and c156 has opposite rationales. check_audit never checks precedence. Options: (a) mark them `supersedes` in additional-corrections and add a checker assertion; (b) drop them from proposed-corrections (changes the 63 count); (c) merge into one file. Recommended: (a) — keeps the 63 invariant and the history.
- [x] [Review][Patch] (decided 2a) Reviewer decisions not reflected in pending state — human-decisions.md keeps original for c471/c473/c111/c125/c135/c166/c456, but all items are still pending-human-approval and audit-summary counts are unchanged. Commit f7980cf says "15 approved replacements"; the data says none is approved. The 28 new findings are not reconciled to the 15 recorded. Options: (a) add a per-item `decision` field and have the checker verify it against human-decisions.md; (b) only note in audit-summary that counts predate the decisions. Recommended: (a) — otherwise rejected items can be re-applied.
- [x] [Review][Patch] (decided 3a) Pending correction text defects — c544 `why` says tobacco is dropped but the current text keeps "thuốc lá"; c013 adds "con đường nội sinh" that the cited 00:09:05 quote does not support; proposals embed ASR noise (c318 "tăng nghệ", c402, c538 "da cầm", c275 "Glutat…"). Options: (a) drop the "nội sinh" clause, fix c544 `why`, and clean the ASR noise with owner-approved wording; (b) add a quote naming the endogenous route. Recommended: (a) for c013 — no new evidence is needed.
- [x] [Review][Patch] check_audit.py is non-hermetic and has vacuous checks — depends on `4e31e57^` and `origin/main`; hard-codes 63/554/["c541"]; the videos diff ignores untracked files; `publishable()` is trivially False because summary.md is absent; git errors and `by_id[...]` KeyError give tracebacks; `additional_matches` lacks the trailing-newline anchor [audit/V-Qfwjo28Zg/check_audit.py:24,108-113,189-190]
- [x] [Review][Patch] Documentation precision — o45 "not stated anywhere" contradicts its anchor [omissions.md:313]; o48 "tim nhanh" blurs the c158 scene; c201 keeps a parenthetical human-decisions says may be dropped; c158 has no effective_class note in additional-corrections.json; omissions bookkeeping (66 / 49+20 / 46+19, o29 gap) needs a reconciliation table
- [x] [Review][Defer] c275/c279 speaker attribution (doctor vs host/Nhung) [additional-corrections.json] — deferred: needs an audio check; human-decisions.md records it as reviewer-confirmed

**Rejected**
- "11 supported-class entries carry pending rewrites, only c158 overridden" — low: by design in additional-corrections.md; a fix is a classification redesign.
- No flag for source-side medical errors (ozone = H2O2, c260) — low: outside the epic's fidelity-only scope.
- No safety handling for self-harm content (o50, c286) — low: outside the audit scope; belongs in the publishing step.
Patches applied (2026-11-06): see audit/V-Qfwjo28Zg: `supersedes` for c013/c156/c275, `decisions.json` (recorded, nothing applied), c013/c275/c544 text fixes, checker hardening, o45/o48/c201 wording, summary reconciliation. Not done: ASR-noise cleanup for c318/c402/c538 and c544 "thuốc lá bỏ đi" need owner-approved wording. `check_audit.py` passes.
