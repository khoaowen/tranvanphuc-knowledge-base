---
title: '2.5 V-Qfwjo28Zg temporary summary: c286 split, 16 mis-timed headings rebuilt, review gate rerun once'
type: 'chore'
ticket: '5'
created: '2026-11-08'
status: 'done'
baseline_revision: '25f0926df70016f0e225345e41115eb816c71372'
risk: 'high'
---

# Ticket 2.5 plan and implementation record

The ticket is `story-the-v-qfwjo28zg-temporary-summary-has-claim-c286-split-by-sp.md`. All paths below are relative to `audit/V-Qfwjo28Zg/`.

## Result

- Summary: `regenerated-2.5/summary.md`, SHA-256 `970a54c9e30fceb11fb27b3011a905f035b8adec38082272672a32a71c80974d`.
  - Built by `regenerated-2.5/build.py` (`eb438148…`) from `regenerated/summary.md` (`90c7e4aa…`) and `regenerated/review.md`.
  - An isolated rebuild (2026-11-08) reproduced it byte for byte, with 118 moves.
- Review gate run 2 (the current result): `regenerated-2.5/gate-970a54c9/` (`review.md`, `claim-map.md`, `gate-report.md`, `provenance.json`, `verify-output.txt`, `run-logs/`).
  - `review.md` (`d514978c…`) binds summary `970a54c9…`.
  - Verdict **fail**: 566 claims, 524 pass, 42 fail, 21 concerns (12 material), 16 omissions, coverage_complete false.
  - Compared with run 1: 41 claims still fail, 14 went from fail to pass, and 1 (c155) went from pass to fail. Only c277 moved between the runs, so these differences are model variance, not fixes.
- Review gate run 1 (historical, bound to summary `606f8441…`): `regenerated-2.5/{review.md,claim-map.md,gate-report.md,provenance.json,moves.json}`. 55 fail. These files are unchanged.
  - That `gate-report.md` says the current summary "has not been gate-reviewed". This was true when it was written and has been superseded by `gate-970a54c9/`.
- V-Qfwjo28Zg stays blocked. `videos/` is untouched, nothing is published, and the failures are not fixed (ticket 2.6).

## The paid run

- One owner-authorized run: `./review-summaries --provider codex --model gpt-6.1-sol --limit 1 --no-commit` on an isolated copy. It started at 2026-11-08T08:35Z.
- It hit the usage limit after chunks 1–10 of 11. The owner chose to resume the same run.
- Resume attempts reused the hash-bound progress cache and retried every 30 minutes until the quota reset. The run finished chunk 11 and the coverage audit at 12:55Z.
- No second gate run was made.

## Owner decisions (2026-11-08)

- **c277 contextual placement.** The caveat "Bác sĩ không nêu rõ liều hay điều kiện cụ thể." sits beside the case at 04:53:37, while its evidence stays at 02:11:08–02:11:09.
  - This is an explicit exception. The general timestamp checks are not relaxed, and `verify.py` still reports it as outside its window.
- **Unrelated working-tree changes.** Their history and byte-for-byte preservation are unknown. They are preserved as-is and are not part of this ticket's commit.
- **A1, requirement 2 is not met for 4 claims; this is accepted for 2.5 and deferred to 2.6.**
  - The claims are c297 and c301 (under 02:22:01, said at 01:28 and 01:29) and c464 and c465 (under 04:19:29, said at 02:41).
  - All four repeat text that already exists elsewhere (01:26:58, 01:29:22, c181). No decision to move, drop or keep them was ever made, and run 2 passes all four.
  - 2.6 decides move, drop or keep.
- **B1, requirement 3: 14 moved claims had no quote to check; this is accepted and routed to 2.6.**
  - 5 now have gate-verified quotes inside their new heading window: c177, c415, c201, c409, c479.
  - 9 are among the 42 run-2 failures: c042, c167, c209, c360, c367, c370, c480, c483, c484.
  - Before 2.6 changes any of these, it checks whether the wording is protected (from the 2.4 owner decisions).
- **D.** The owner declared the walkthrough done and approved committing the 2.5 files only.
- **F, deferred and not blocking.** `docs/review-summaries.md` still says publication requires evidence inside each claim's section window.
  - Commit `8975775` (2026-10-18) deliberately removed that rule from `scripts/review_summaries.py` and `scripts/queue_state.py`. Only the documentation is stale.
  - Fixing it is a docs-only follow-up, outside this ticket. Pipeline code is not touched.
  - Consequence to know: if the window rule were ever restored, c277 at 04:53:37 would block publication.

## Free verification (2026-11-08)

`gate-970a54c9/verify-output.txt` was produced from the isolated rebuild. The workspace's `moves.json` is the historical 117-move file and lacks c277.

- Passed:
  - the header is identical;
  - headings run in strictly increasing time;
  - every `?t=` link matches its heading time;
  - no claim text changed apart from c271 and c286.
- 103 of 104 locatable moved claims are inside their window. The exception is c277, as recorded above.
- `verify.py` reports c402, c404 and c406 as "absent". They were already absent from the 2.4 summary, so this ticket did not cause it.
- The validator exits 1 on the tag `thiếu máu thiếu sắt`.
  - Ticket 1.14 already decided to split it into `thiếu máu` and `thiếu sắt`, and both are in `topics/vocabulary.md`.
  - Applying the split to the header is 2.6's job.
