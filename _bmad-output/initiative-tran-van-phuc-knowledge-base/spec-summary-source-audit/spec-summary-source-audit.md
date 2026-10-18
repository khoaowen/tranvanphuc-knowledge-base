---
id: SPEC-summary-source-audit
companions: [audit-record-format.md]
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the complete, preservation-validated contract for what to build, test, and validate. Source documents listed in frontmatter are for traceability — consult them only if you need narrative rationale or prose color this contract intentionally omits.

# Summary Source-Grounded Audit (q7uDJG8YQ5c, V-Qfwjo28Zg)

## Why

Two summaries, the seed `q7uDJG8YQ5c` (`videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/`, 149 claims) and `V-Qfwjo28Zg` (`videos/2026-10-10-so-135-glutathione-…/`, 554 claims), cannot be trusted for publication: their `review.md` files predate the current claim extraction, so verdicts and claim IDs are stale. The operator needs an independent, human-checkable record of what the summaries actually say versus the transcripts before approving any correction. Medical content makes silent errors, misattributed speakers and hardened hedges costly.

## Capabilities

- **CAP-1**
  - **intent:** For every claim in each video's current `summary.md`, the auditor records exact claim text, section, verbatim transcript evidence with timestamp, and a classification (supported, mismatch, attribution/qualification issue, unresolved).
  - **success:** Claim records exist for 149 + 554 claims (the current `fidelity.extract_claims` output); every record has a class; every non-unresolved record has a quote that is a verbatim substring of `transcript.md` at the cited timestamp (checkable by script); no claim ID is copied from `review.md`.
- **CAP-2**
  - **intent:** The auditor identifies important transcript topics the summary omits.
  - **success:** Each video has an omission list with timestamp range and verbatim anchor quote per topic, or an explicit "none found" after a full-transcript pass.
- **CAP-3**
  - **intent:** Proposed corrections are recorded apart from the audit findings for later human approval.
  - **success:** `proposed-corrections.md` exists per video, every item `pending-human-approval`, and the diff of `videos/` against HEAD is empty for these two videos after the run.
- **CAP-4**
  - **intent:** Both videos remain blocked from publication throughout.
  - **success:** `queue_state.publishable(video_dir)` is false for both before and after; per-video summary states `blocked`.

## Constraints

- Evidence is only current `summary.md`, `transcript.md`, and existing `review.md`; old review verdicts and claim IDs are never treated as current (review.md may be read only as a lead to locate candidate evidence).
- Every claim is checked against the full `transcript.md`, not a section window. A claim with no evidence found is `unresolved`; absence is never assumed from a failed search.
- Speaker identity and qualifications are preserved as spoken; the auditor does not medically correct, and does not infer facts beyond the transcript.
- Audit only: no edits to `summary.md` or `transcript.md`, no changes to `review.md`/`.review-progress.json`, no model calls except read-only subagents on `claude-opus-5-5` (reading, re-check, advisory correction review) which never write outside `audit/`, no publishing, no git commit.
- Outputs are written outside `videos/` (see `audit-record-format.md`).

## Non-goals

- Applying any correction or regenerating summaries.
- Producing a new pass/flag/fail verdict or refreshing `review.md`.
- Medical validation of the doctor's statements.
- Auditing other videos or changing the review tool (`scripts/review_summaries.py`, `fidelity.py`).
- Unblocking or publishing either video.

## Success signal

A human reviewer can open one record per claim, see the summary sentence beside the verbatim transcript quote and timestamp, and decide approve/reject on each proposed correction, while `git status` shows no change to either video's files and both stay unpublishable.

## Assumptions

- Output location `_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-summary-source-audit/audit/<video_id>/` since no location was given.
- Claim ids `c001…` regenerate from current `fidelity.extract_claims`; counts may change if the summary or extractor changes, in which case the audit restarts.

## Assumptions (approval)

- Superseding the earlier model-free stance: user approved subagents on `anthropic/claude-opus-5-5` (availability unverified) for claim-by-claim reading, each given the full transcript. A second independent pass re-checks every non-supported claim; a script verifies each quote is verbatim in `transcript.md`. Approval of proposed corrections is a later, separate phase. The same model may review each correction and record approve/reject plus rationale; its verdict is binding (user-accepted); applying corrections is outside this audit phase.

- Amendment (2026-10-18): corrections for q7uDJG8YQ5c only were approved and applied by the human; "pending-human-approval" and "no applying" still hold for V-Qfwjo28Zg. Requirement text unchanged.

## Open Questions

- Confirm `claude-opus-5-5` is accepted by the subagent runtime before launch.
