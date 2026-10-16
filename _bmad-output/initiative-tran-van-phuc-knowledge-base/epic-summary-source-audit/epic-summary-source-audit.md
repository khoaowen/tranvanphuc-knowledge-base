---
tracker_id: ""
key: ""
type: epic
title: "Summary source-grounded audit"
parent: initiative-tran-van-phuc-knowledge-base
covers: [CAP-3]
after: []
assignee: ""
risk: high
---

# Summary source-grounded audit

## Description

Complete an independent, human-checkable source-grounded audit of the current summaries for q7uDJG8YQ5c and V-Qfwjo28Zg. The canonical requirements and evidence contract are in `../spec-summary-source-audit/spec-summary-source-audit.md` and its companion `audit-record-format.md`; this audit is separate from the automated video knowledge pipeline and its ticket 1.12.

## Outcome

A human can inspect every current claim against its transcript, review important omissions and separately proposed corrections, while both videos remain blocked from publication.

## Requirements

- E2-R1 (audit spec CAP-1): Every current summary claim in both videos has an exact-text claim record with section, verbatim timestamped transcript evidence where available, speaker/attribution, class, and note; unresolved claims remain unresolved until checked against the full transcript. No claim IDs are copied from stale reviews.
- E2-R2 (audit spec CAP-2): Each video has an important-omissions list with timestamp range and verbatim anchor quote, or an explicit “none found” after a full-transcript pass.
- E2-R3 (audit spec CAP-3): Proposed corrections are separate from findings, each marked `pending-human-approval`; source video files and review artifacts remain unchanged.
- E2-R4 (audit spec CAP-4): Both videos remain blocked from publication throughout and are reported as `blocked`.

## Done when

1. All 149 current claims for q7uDJG8YQ5c and all 554 current claims for V-Qfwjo28Zg have records in the companion’s format, and every non-unresolved quote is script-checkable as a verbatim transcript substring at its cited timestamp.
2. Each video has a full-transcript omissions result and a separate proposed-corrections file whose items are pending human approval.
3. An independent second pass has re-checked every non-supported claim; no old review verdicts or IDs are treated as current, and no medical correction or inference is introduced.
4. Both videos are still unpublishable and reported blocked; no summary, transcript, review, or review-progress artifact was edited, and no content was published or committed.

## Boundaries

This epic owns only the read-only audit and its outputs under `../spec-summary-source-audit/audit/<video_id>/`. It does not own changes to `videos/`, review refreshes, medical validation, applying corrections, auditing other videos, changing review tooling, unblocking or publishing, or committing. Preserve all existing audit artifacts; continue or supplement them without restarting, overwriting, or deleting prior work.

## References

- parent — `../initiative-tran-van-phuc-knowledge-base.md`, CAP-3
- spec — `../spec-summary-source-audit/spec-summary-source-audit.md`, CAP-1–CAP-4, Constraints, Non-goals, Assumptions (approval)
- companion — `../spec-summary-source-audit/audit-record-format.md`
- existing work — `../spec-summary-source-audit/.memlog.md` and `../spec-summary-source-audit/audit/`

## Notes

- Decision: The work is a separate audit epic with exactly two independently verifiable stories, one for each confirmed video (user approval, 2026-10-15).
- Decision: Preserve and continue all existing audit artifacts; do not restart, overwrite, or delete them (user approval, 2026-10-15).
- Decision: Do not change ticket 1.12; do not perform the audits, edit summaries/transcripts/reviews, publish, or commit as part of inception (user direction, 2026-10-15).
- Open question: Before any audit subagent is launched, confirm that `claude-opus-5-5` is accepted by the subagent runtime, as required by the spec.
