---
id: 6
type: story
title: "The V-Qfwjo28Zg review-gate failures are each decided and fixed or accepted until the review gate passes on the temporary summary"
parent: epic-summary-source-audit
covers: [E2-R3, E2-R4]
after: [5]
refined: true
hitl: true
risk: high
---

# The V-Qfwjo28Zg review-gate failures are each decided and fixed or accepted until the review gate passes on the temporary summary

## Description

Walk the owner through the claims the review gate fails (48 on the 2.4 summary) and the 46 undecided corrections, decide each as fix, keep or accept with a reason, apply only decided fixes to the temporary summary, and rerun the gate until its verdict is pass. Nothing medical is added beyond the transcript.

## Requirements

1. **Every failing claim has a decision** (E2-R3)
   **Given** the claims the review gate fails on the summary rebuilt by 2.5 (48 on the 2.4 summary; the number may change)
   **When** the owner walks through them
   **Then** each has one recorded decision: fix, keep or accept, with a reason
   **And** a claim the owner cannot decide stays open and the ticket is not done.

2. **Every undecided correction has a decision** (E2-R3)
   **Given** the 46 undecided corrections (63 proposed minus 17 already decided; report section 4 of `regenerated/`)
   **When** the owner walks through them
   **Then** each has one recorded decision: fix, keep or accept, with a reason
   **And** a claim that is both a failing claim and an undecided correction gets one decision, not two.

3. **Only decided fixes are applied** (E2-R3)
   **Given** the recorded decisions
   **When** the temporary summary is edited
   **Then** only claims decided "fix" change, each with the owner's text or a verbatim quote at its timestamp
   **And** nothing medical is added beyond the transcript, and the tags from ticket 1.14 are used in the header.

4. **The gate is rerun until it passes** (E2-R4)
   **Given** the edited temporary summary
   **When** the review gate is run, each run with the owner's permission
   **Then** the loop ends when the verdict is pass with `coverage_complete` true, naming the summary's SHA-256
   **And** after each failed run the owner decides again, or stops and ticket 2.6 stays open.

5. **Accepted claims are not hidden** (E2-R3)
   **Given** a claim the owner accepts although the gate fails it
   **When** the final record is written
   **Then** it lists that claim with its reason, and the verdict is not called pass on the strength of acceptance alone.

## Constraints

- Every gate run uses codex quota; the owner permits each run. Set a stop rule with the owner at the start (for example three runs).
- Walk-through in batches the owner can read (about 10 claims), with the transcript quote beside each.

## Boundaries

- Must not change: `videos/`, pipeline code, the audit JSON files and 2.4's files. V-Qfwjo28Zg stays blocked; applying to `videos/` needs its own approval.
- Must not change: the 15 approved replacements and the tag decisions of 1.14.
- Depends on: 2.5 for the rebuilt summary, and 1.14 for the tags.

## References

- parent — _bmad-output/initiative-tran-van-phuc-knowledge-base/tickets/epic-summary-source-audit/epic-summary-source-audit.md
- ../../../audit/V-Qfwjo28Zg/regenerated/owner-decision-brief.md
- ../../../audit/V-Qfwjo28Zg/proposed-corrections.md
- ../../../audit/V-Qfwjo28Zg/human-decisions.md

## Notes

- The 46 undecided corrections and the failing claims overlap; the first step is a merged list with one row per claim.
- Source conflict: the 2.4 brief reports 47 or 48 fails and an earlier owner note said 48 undecided; the count of undecided is 46 (brief, appendix). Recount on the rebuilt summary.
- Risk high: medical content for the public; an accepted wrong claim publishes. Check beyond the criteria: a second reader re-reads every claim decided "accept" against the transcript before the final run.
- hitl: the owner decides each claim.
- Source of truth (owner, 2026-11-06): `audit/V-Qfwjo28Zg/proposed-corrections.md` carries the owner's decisions on c070, c111, c201, c377 and others ("Quyết định người duyệt" in each `why`). `proposed-corrections.json` is frozen at hash `9ebdd751…` with `pending-human-approval` and is stale for those items. Do not edit the JSON here; whoever applies corrections later reconciles from the `.md` and `human-decisions.md`.
- Claim-to-record map for the 2.4 summary: `audit/V-Qfwjo28Zg/regenerated/claim-map.md` (530 unchanged, 26 rewritten or split, 9 new without a record, 1 removed). Use it for the merged claim list; new claims have no audit verdict until a new audit.
