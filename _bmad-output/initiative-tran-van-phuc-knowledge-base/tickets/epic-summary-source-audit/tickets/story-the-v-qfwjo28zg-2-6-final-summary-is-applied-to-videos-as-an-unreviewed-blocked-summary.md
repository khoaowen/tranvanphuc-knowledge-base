---
id: 7
type: story
title: "The V-Qfwjo28Zg 2.6 final summary is applied to videos/ as an unreviewed, blocked summary"
parent: epic-summary-source-audit
covers: [E2-R3, E2-R4]
after: [6]
assignee: ""
refined: true
hitl: true
risk: high
---

# The V-Qfwjo28Zg 2.6 final summary is applied to videos/ as an unreviewed, blocked summary

## Description

This story copies the 2.6 final summary into `videos/` as a new file. It is drafted only; applying it needs a separate start plus the owner's approval of the exact diff. The ticket 2.6 gate verdict is FAIL, accepted on record. This is not a pass. The q7uDJG8YQ5c override (story 3 Notes) does not reach V-Qfwjo28Zg.

## Acceptance Criteria

1. **SHA binding**
   **Given** `regenerated-2.6/summary.md` and the SHA in `final-record.md`
   **When** it is copied
   **Then** `videos/…/summary.md` has SHA-256 `8c910a25a0edc763e885db855c5d930fe4955ed061129dffcd46112366660979`, is byte-identical to the source, and the source is unchanged.
2. **Summary contract**
   **Given** the applied file
   **When** the contract is checked
   **Then** header (title, ID, date, URL, tags), disclaimer banner, timestamped sections with valid `?t=` links, question-shaped lines and the VI/EN/FR glossary are present, and every tag is in `topics/vocabulary.md`.
3. **Validators**
   **Given** the applied folder
   **When** `validate_summaries.validate_video` runs
   **Then** the only reason is "no passing review bound to this summary", `invalid` is false, and `transcript.md` SHA is still `dedb6e4d414945da6e0c7895fbcdf5344d5c366305b1bcc7a034eb6cc59776e4`. The check runs on a temp copy first and again after the apply.
4. **One-to-one claim map**
   **Given** the applied summary
   **When** `fidelity.extract_claims` runs
   **Then** it yields 583 claims, mapped to the 582 run-6 claims plus the 01:50:49 sentence; c312 and that sentence are listed as not gate-verified; any split, merge or drop is listed for the owner and an unexplained one stops the run.
5. **Nothing new is claimed**
   **Given** `videos/` after the apply
   **When** it is compared with HEAD
   **Then** the only added file is `summary.md`; no `review.md` or `.review-progress.json` exists, and `metadata.json` and `transcript.md` are unchanged.
6. **Stays blocked**
   **Given** the folder after the apply
   **When** `queue_state.publishable` runs
   **Then** it returns false, and the audit still says `blocked` and `publishable: false`.
7. **Diff approved before write**
   **Given** the apply plan
   **When** the exact diff is previewed
   **Then** nothing is written to `videos/` until the owner approves that diff, and nothing is committed or staged.

## Boundaries

- Must not change: `scripts/`, the audit JSON files (frozen, stale), `regenerated-2.5/`, `regenerated-2.6/`, `transcript.md`, `metadata.json`, tickets 1.12 and 1.14.
- Must not: run a paid gate, publish or unblock, commit or push, or edit the epic or spec text. A dated "applied, still blocked" note is a separate small edit after the owner accepts.

## References

- final record — `../../../audit/V-Qfwjo28Zg/regenerated-2.6/final-record.md`
- summary — `../../../audit/V-Qfwjo28Zg/regenerated-2.6/summary.md`
- corrections source of truth — `../../../audit/V-Qfwjo28Zg/proposed-corrections.md`, `human-decisions.md`
- contract — `../../../summary-contract.md`

## Notes

- Decision: applying to `videos/` was parked in the epic Notes (2026-11-05) and needs its own approval. This ticket is that request.
- Stays blocked: no passing review and no gate has run on this file; ticket 2.6 verdict stays FAIL; c312 and the 01:50:49 sentence are not gate-verified.
- The 46 undecided corrections were decided in 2.6 and are inside `summary.md`.
- Open 1: once `summary.md` exists the weekly queue stops re-summarising this video; alternative is a `.stale` marker. Default: no marker.
- Open 2: `metadata.json` `topics: []` stays unchanged. Default: unchanged.
- Check outside the criteria (risk high): the owner reads the diff of the new `summary.md`.
