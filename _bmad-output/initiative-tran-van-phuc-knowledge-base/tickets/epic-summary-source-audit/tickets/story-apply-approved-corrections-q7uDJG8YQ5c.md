---
id: 3
type: story
title: "The 24 human-approved corrections are applied to the q7uDJG8YQ5c summary, which stays blocked"
parent: epic-summary-source-audit
covers: [E2-R4]
after: [1]
assignee: ""
refined: true
hitl: true
risk: high
---

# The 24 human-approved corrections are applied to the q7uDJG8YQ5c summary, which stays blocked

## Description

The q7uDJG8YQ5c summary gets the proposed text of all 24 corrections the human approved on 2026-10-15, each matched by its current text, and the result is left as an uncommitted diff for the human to review. The human steps are the review of that diff and the answers to the open questions below. This story is drafted only; applying it needs a separate start.

The audit spec and epic exclude applying corrections and require every correction to be `pending-human-approval`. For this video only, the human overrode both (see Notes). The override does not reach V-Qfwjo28Zg.

## Acceptance Criteria

1. **Each correction is matched by text, with its id verified first**
   **Given** `proposed-corrections.md` (revision 2) with 24 items marked `approved`, and the current `summary.md`
   **When** an item is applied
   **Then** the claim is located by its `current` text, its audit-time id is checked to point at that same text, and any item whose text is missing, appears more than once, or does not match its id is not applied and is reported to the human
2. **Only the approved text is written**
   **Given** an item whose text matched
   **When** it is applied
   **Then** the matched claim is replaced with the item's `proposed` text exactly, and no other line of `summary.md` changes
3. **All 24 are accounted for**
   **Given** the run is finished
   **When** the human reads the apply report
   **Then** it lists each of the 24 items as applied or not applied with the reason, and the applied count plus the not-applied count equals 24
4. **The edited summary still maps one-to-one onto the audit**
   **Given** the edited `summary.md`
   **When** its claims are extracted with the same method the audit used
   **Then** each extracted claim maps to exactly one audit record and each audit record to exactly one claim, or every difference (claim split, merged, added, or removed) is listed for the human, and no claim is silently dropped
5. **Added wording is quote-checked**
   **Given** wording the corrections added to the summary
   **When** the quote check from the audit runs on the supporting quotes of the applied items
   **Then** every quote is a verbatim substring of `transcript.md` at its cited timestamp, and any failure is reported and the item flagged
6. **Refreshing review artifacts is decided by the human**
   **Given** `review.md` and `.review-progress.json` for the video
   **When** the edit is done
   **Then** both files are byte-identical to before, and the human has been asked whether to refresh them
7. **The video stays blocked**
   **Given** the video after the edit
   **When** `queue_state.publishable` runs on its folder
   **Then** it returns false, and the audit summary still says `blocked` and `publishable: false`
8. **The human reviews a diff before anything is recorded**
   **Given** the edit is done
   **When** the run ends
   **Then** the human has a diff of `summary.md` against HEAD, nothing is committed or staged, and the audit files are recorded as applied only after the human accepts the diff

## Boundaries

- Must not change: V-Qfwjo28Zg, its audit and its files.
- Must not change: ticket 1.12, the review tool, `transcript.md`, and the proposed corrections' approved text and `proposed-corrections.r1.md`.
- Must not change: `review.md` and `.review-progress.json`, unless the human answers open question 3 with a refresh and says so.
- Must not publish, unblock, or commit; no medical correction or inference beyond the approved text.

## References

- parent — `epic-summary-source-audit.md`
- corrections — `../spec-summary-source-audit/audit/q7uDJG8YQ5c/proposed-corrections.md`, revision 2, 24 items
- approval — `../spec-summary-source-audit/audit/q7uDJG8YQ5c/approval-record.md`
- audit contract — `../spec-summary-source-audit/spec-summary-source-audit.md` and `../spec-summary-source-audit/audit-record-format.md`
- audit record — `../spec-summary-source-audit/audit/q7uDJG8YQ5c/`, `claims.json` and `replacement-check.md`
- target — `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/summary.md`

## Notes

- Decision: the human approved all 24 items of revision 2 on 2026-10-15, for later application in a separate story.
- Decision: for q7uDJG8YQ5c only, the human overrides the audit spec's non-goal "applying any correction" and the epic's boundary and E2-R3 requirement that corrections stay `pending-human-approval` (user, 2026-10-15). Those documents are not edited by this draft.
- Decision: no commit unless the human asks; the human reviews the diff first.
- Decision: V-Qfwjo28Zg, ticket 1.12, and the review tool are out of scope.
- Check outside the criteria (risk high): the human reads the diff of `summary.md` against the approved `proposed` texts before accepting it.
- Decision: `after: [1]` confirmed (user, 2026-10-15).
- Decision: the 13 reviewer-approved items and the 11 revised (r2) items are applied together in one run and one diff; the apply report tags each item as reviewer-approved or revised (user, 2026-10-15).
- Decision: after the human accepts the diff, a short dated amendment note is added in both the epic Notes and the spec Assumptions: corrections for q7uDJG8YQ5c only were approved and applied by the human, and "pending-human-approval" and "no applying" still hold for V-Qfwjo28Zg. The requirement text is not changed. This is a separate small edit, not part of this story's apply step (user, 2026-10-15).
- Decision: `review.md` and `.review-progress.json` are not refreshed and stay byte-identical; a refresh may be its own later ticket (user, 2026-10-15).
- Decision: if the edited summary no longer maps one-to-one onto the audit, the run stops and lists the differences; the human chooses a new audit revision or a changed edit. Existing audit records are not overwritten; any new mapping goes in a supplementary file (user, 2026-10-15).
- Decision: the apply report is a new file, `audit/q7uDJG8YQ5c/apply-report.md` (user, 2026-10-15).
- Decision: `apply-report.md` and `approval-record.md` carry a one-line note "corrections applied, uncommitted, video still blocked"; `audit-summary.md` is unchanged until the human accepts the diff (user, 2026-10-15).
- Decision: audit artifacts reconciled (user, 2026-10-15). `proposed-corrections.md` now holds all 24 items, each `approved`: c065 and c108 were restored from r1 (c065 takes the reviewer's suggested text because the reviewer rejected the r1 text), and `report.md` and `audit-summary.md` now say 24. `final_records.json` was right all along. The c065 text was not in the file the human approved.
- Decision: the human reviewed c065 and keeps the reviewer's text, which is two sentences (user, 2026-10-15). If it splits the claim, the one-to-one mapping check reports the split and the run stops, as already decided.
