---
id: 4
type: story
title: "A current V-Qfwjo28Zg summary is built from the historical text and the 15 approved replacements, validated in a temporary folder, and nothing applied"
parent: epic-summary-source-audit
covers: [E2-R3, E2-R4]
after: [2]
refined: true
hitl: true
risk: high
---

# A current V-Qfwjo28Zg summary is built from the historical text and the 15 approved replacements, validated in a temporary folder, and nothing applied

## Description

`videos/` has no `summary.md` for V-Qfwjo28Zg: the old one was removed in `4e31e57` to re-queue the video. This story builds one current summary by applying the 15 replacements the owner approved to the historical summary text, in a temporary folder outside `videos/`, then validates it and leaves a report. The owner steps are deciding the open items below and reading the report. Applying the result to `videos/` is a separate ticket with its own approval and start.

## Requirements

Verify: the new summary passes the summary contract and validators, binds to its own SHA-256, accounts for all 15 replacements, and every audit artifact, `videos/` and pipeline code are byte-identical to before.

1. **Inputs are fixed and hashed before generation**
   **Given** the inputs below
   **When** the run starts
   **Then** a provenance file in the temporary folder lists each input with its SHA-256 and the run stops if any hash differs from this ticket:
   - Historical summary: `git show 4e31e57^:videos/2026-10-10-so-135-glutathione-can-bang-oxy-hoa-khu-phuc-hoi-ty-the-va-bao-ve-te-bao-tu-cap-do-phan-tu/summary.md`, `fbae11bf16fa47c8055fe7b309f45dfeb696db23a0009c593504c1351a98203c` (reference only, never restored)
   - `videos/<that folder>/transcript.md`: `dedb6e4d414945da6e0c7895fbcdf5344d5c366305b1bcc7a034eb6cc59776e4`
   - `final_records.json`: `af300706e3d70433442cdbdac2ee3ee4ec9b408b2f32e5b1e653fc55a2061d60`
   - `proposed-corrections.json`: `9ebdd751599622d6d36b5f60704731a377e6ae280434b93a5ab3ba9cff5d750e`
   - `additional-corrections.json`: `4d6eb5611e2a3223a5f064ca01ebb45096bc1f9110a9996856f1f77ed79065c4`
   - `revised-summary-draft.md`: `6c80e4354d7e80c9588f9010c537b74fe977243bb6b8b74e0b4a017735f5b64f`
2. **The new summary is built only in the temporary folder**
   **Given** the historical summary text and the 15 replacements
   **When** the summary is built
   **Then** it is written to `audit/V-Qfwjo28Zg/regenerated/summary.md` only, with copies of `transcript.md` and `metadata.json` beside it so the validators can run; no file under `videos/` is created or changed, no generator is run, and pipeline code is not edited
   **And** the result differs from the historical text only at the 15 replacements and the items the owner has already decided (c456 removed, c509 changed, c541 labelled as the summariser's note, o19–o22 kept under "khán giả tự kể"), and nothing else
3. **The new summary meets the contract and the validators**
   **Given** the new `summary.md`
   **When** `validate_summaries.py` and the review gate run on it
   **Then** the header, banner, timestamped `?t=` sections, question lines, VI/EN/FR glossary and vocabulary tags all pass, and the review result names the summary's own SHA-256; any failure is reported, not patched around
4. **Added wording is quote-checked**
   **Given** the new summary and the audit records
   **When** the quote check runs on the supporting quotes of the replacements
   **Then** every quote is a verbatim substring of `transcript.md` at its cited timestamp, and any failure is reported and the item flagged
5. **All 15 replacements are accounted for once**
   **Given** c318, c156, c275, c544, c552, c286, c158, c242, c260, c402, c213, c538, c278, c279, c013
   **When** the report is read
   **Then** a table lists each as applied or not applied, with its location in the new summary and the reason, the applied plus not-applied count is 15, and c013, c156 and c275 are not counted a second time from `proposed-corrections.json`
6. **Fixed wording holds**
   **Given** the new summary
   **When** its text is checked
   **Then** c156 carries the thức → ngủ addition in one item, c278 keeps both "bố chồng" (reading the comment) and "chồng chị Ngân" (the doctor speaking), and c279 does not say chị Nhung was suspected of a brain tumour
7. **No other approved change is lost or invented**
   **Given** the 63 non-supported items and the owner's decisions in `human-decisions.md`
   **When** the new summary is compared with them
   **Then** each item is reported as followed, not followed or undecided; nothing undecided is silently applied, and no medical content absent from the transcript is added
8. **Claims map one-to-one onto the audit**
   **Given** the new summary
   **When** its claims are extracted with the audit's method
   **Then** each maps to at most one audit record, and every claim split, merged, added or removed is listed for the owner; a difference stops the run rather than rewriting audit records
9. **Nothing historical changes and the video stays blocked**
   **Given** the files before and after the run
   **When** they are compared
   **Then** `final_records.json`, `claims.json`, `raw/`, the JSON files above and `proposed-corrections.json` (still 63 non-supported items) are byte-identical, their status stays `pending-human-approval`, `videos/` and pipeline code are unchanged, nothing is committed, pushed, staged or published, and the audit status stays `blocked`

## Boundaries

- Must not change: `videos/`, pipeline code and tests, the historical audit, `final_records.json`, the pending-human-approval status of any JSON.
- Must not: restore the historical summary into `videos/`, publish, unblock, commit, push, stash or revert the existing uncommitted audit artifacts.
- Touch point: validators and review gate — used as-is, run on the temporary folder; owner: epic-video-knowledge-pipeline

## References

- parent — `_bmad-output/initiative-tran-van-phuc-knowledge-base/tickets/epic-summary-source-audit/epic-summary-source-audit.md`
- contract — `_bmad-output/initiative-tran-van-phuc-knowledge-base/summary-contract.md`
- audit — `_bmad-output/initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/`, `additional-corrections.md`, `revised-summary-draft.md`
- decisions — `_bmad-output/initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/human-decisions.md`
- sibling — `_bmad-output/initiative-tran-van-phuc-knowledge-base/tickets/epic-summary-source-audit/tickets/story-apply-approved-corrections-q7uDJG8YQ5c.md`, the pattern for applying approved corrections

## Notes

- Decision: 2026-10-31, owner chose a separate story 2.4 in epic 2, `after: [2]`, planning only (user).
- Decision: 2026-10-31, the owner first chose regeneration with the pipeline; an Opus review found criteria 5–8 cannot hold for a regenerated text (claim ids and the 15 replacements belong to the historical text). The owner then chose to build from the historical text plus the 15 replacements (user, 2026-10-31). `revised-summary-draft.md` is the reference to compare against, not the output.
- Decision: the 15 replacements are approved for the draft only; the JSON files keep `pending-human-approval` and their schema (user, prior round).
- Open question: do the other 48 items of the 63, and c456, c509, c541 and o19–o22, enter the new summary? The owner decides before generation; unanswered items are reported as undecided.
- Open question: how is owner-confirmed evidence (GSSG, NADPH, Nhật Bản, "trên dưới 2.000 UI") treated, given it is not in the transcript and audio is not checkable? Default: follow the decision and label it as the owner's confirmation.
- Open question: is ticket 2.2 (state review) accepted done now, or held until 2.4 ends? Default: held.
- Open question: before anything reaches `videos/`, who changes the JSON status, where the new summary is stored, whether `review.md` is refreshed, and whether the epic and spec "pending-human-approval" notes are amended? A later ticket decides; none of it happens here.
- Check beyond the criteria (risk high): the owner reads the new summary against `revised-summary-draft.md` for the 15 replacements before accepting the report.
