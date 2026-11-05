---
id: 5
type: story
title: "The V-Qfwjo28Zg temporary summary has claim c286 split by speaker and its 16 mis-timed headings rebuilt, and the review gate is rerun once"
parent: epic-summary-source-audit
covers: [E2-R3, E2-R4]
after: [4]
refined: true
hitl: true
risk: high
---

# The V-Qfwjo28Zg temporary summary has claim c286 split by speaker and its 16 mis-timed headings rebuilt, and the review gate is rerun once

## Description

In a temporary folder outside videos/, split the c286 sentence so each part carries one speaker and one timestamp, rebuild the 16 section headings whose content sits far from their time and ?t= link (reported in regenerated-timefix/report.md), then rerun the review gate once. The owner decides how content is split under each heading. Applying to videos/ is not part of this ticket.

## Requirements

1. **c286 carries one speaker and one timestamp per part** (E2-R3)
   **Given** claim c286, which joins the host reading the father-in-law comment with the doctor's reply
   **When** the temporary summary is rebuilt
   **Then** it is two sentences: the host reading (glucose 5.5–6.8) cited at 01:11:52, and the doctor on chồng chị Ngân and chị Ngọc Thơ cited at 02:14:12
   **And** each sentence is a verbatim-checked quote at its own timestamp.

2. **Each of the 16 headings matches its content** (E2-R3)
   **Given** the 16 headings in the table of `regenerated-timefix/report.md` section 4
   **When** the owner has decided how the content under each is split
   **Then** every heading's `[HH:MM:SS]` and `?t=` link point to the transcript time of the content under it
   **And** no heading in that table keeps a claim that sits far from its time.

3. **Moved text is verified** (E2-R3)
   **Given** any sentence added or moved by this ticket
   **When** it is compared with the transcript
   **Then** it is a verbatim-checked quote at its cited timestamp, with no medical statement beyond the transcript.

4. **Heading order is chronological** (E2-R3)
   **Given** the two reversed pairs (04:04:39 before 04:03:09, 04:14:18 before 04:13:09)
   **When** the headings are rebuilt
   **Then** headings in the temporary summary run in increasing time.

5. **The review gate is rerun once and bound to the new summary** (E2-R4)
   **Given** the rebuilt temporary summary
   **When** the review gate is run once, with the owner's permission for that paid run
   **Then** the review result names the new summary's SHA-256
   **And** failures remain reported, not hidden; fixing them is ticket 2.6.

## Constraints

- The temporary folder is outside `videos/`. Claim ids and `section` no longer match the 2.4 `review.md` one to one, so the rerun is a new audit of the new SHA, with a mapping file by claim content.
- Only a rerun the owner permits: it uses codex quota.

## Boundaries

- Must not change: `videos/`, pipeline code, every audit JSON, 2.4's files and the 2.4 summary. V-Qfwjo28Zg stays blocked.
- Must not change: the 15 approved replacements and the tag decisions of ticket 1.14; applying tags to the header belongs to 2.6.
- Touch point: stubs that already exist at 02:26:23, 02:34:11, 02:35:19, 02:43:43, 03:31:26, 04:03:09 and 04:53:37 may receive moved blocks (report section 6, narrow option B).

## References

- parent — _bmad-output/initiative-tran-van-phuc-knowledge-base/tickets/epic-summary-source-audit/epic-summary-source-audit.md
- ../../../audit/V-Qfwjo28Zg/regenerated/owner-decision-brief.md
- ../../../audit/V-Qfwjo28Zg/regenerated-timefix/report.md
- ../../../audit/V-Qfwjo28Zg/human-decisions.md

## Notes

- Source conflict resolved: the 2.4 brief said 13 headings; report section 4 lists 16. The owner chose all 16 (2026-11-05).
- Risk high: wrong times send viewers to the wrong place in a medical video, and the rebuild moves text. Check beyond the criteria: a second reader compares a sample of five moved sentences with the transcript before the rerun.
- hitl: the owner decides, per heading, how content is split.
- Depends on 2.4 leaving review; do not start before then.
