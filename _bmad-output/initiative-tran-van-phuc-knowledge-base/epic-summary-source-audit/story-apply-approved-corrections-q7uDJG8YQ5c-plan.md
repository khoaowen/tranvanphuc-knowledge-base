---
title: '2.3 follow-up: accept verified cross-section evidence'
type: 'bugfix'
ticket: '3'
created: '2026-10-18'
status: 'built'
baseline_revision: '5f4536d58c06c2d8204bb92176ad75c82c52af80'
route: 'oneshot'
route_source: 'auto'
risk: 'high'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

The human authorized step 1 of the 2026-10-18 follow-up: let a claim use a verbatim transcript quote outside its summary section. First assess all existing stored reviews without calling a model or writing video files. Correct review aggregation and the publication gate consistently, add regression tests, run the full suite, present the diff, and stop for human review.

Keep quote authenticity, evidence timestamp validation, semantic review checks, exact-summary binding and coverage requirements. Existing review verdicts are not rewritten automatically. The human explicitly authorizes continuation on the dirty working tree described in the prompt and forbids staging, committing, pushing or publishing. No summary additions, review runs or unblocking decisions belong to this step. Preserve all video content, V-Qfwjo28Zg's files/audit, ticket 1.12, transcripts, proposed-corrections.r1.md and the approved correction text. Hash-check the Omega-3 transcript before and after.

</frozen-after-approval>

## Implementation Notes

- Oneshot scope: remove one obsolete predicate from aggregation and one from the gate; adapt and extend the existing fidelity tests. Production change is under 30 lines. Risk stays high because this changes publication eligibility for medical summaries.
- `scripts/review_summaries.py`: `parse_model_review` verifies quotes against the supplied transcript chunk and computes timestamps. `aggregate_claim` currently discards otherwise clean evidence solely on section location.
- `scripts/queue_state.py`: `completed_review` checks all stored evidence against transcript timestamps and binds the claim inventory and summary hash. `current_review` redundantly imposes the section location rule; retain every other requirement.
- `scripts/fidelity.py`: existing `resolve_quote` and `evidence_timestamp_matches` already establish normalized verbatim matching across consecutive captions. Reuse unchanged; no new matching rules.
- Pre-change read-only simulation checked all two stored reviews. Neither overall verdict changes. Omega-3's seven window-only claims would pass; its 17 omissions keep coverage false. V-Qfwjo28Zg is the glutathione video; 106 stored window-only claims would pass, but content failures, concerns and omissions keep fail. Its stored inventory is already invalid under the current extractor (561 stored versus 554 derived claims); leave it untouched.
- Preserve existing unrelated working-tree edits; review only this step's production/test patch and new workflow artifacts.
- Implemented in review aggregation and gate; fidelity matching helpers stay unchanged. Two changed acceptance expectations failed before the production fix. All 86 tests pass after it, and diff whitespace checks pass.
- All 94 protected video/audit files retain the baseline manifest digest, including the full transcript hash. Both actual stored verdicts and publication results remain fail/false. No model reviews were rerun.
- Step-1 report includes the full code/test diff at `../spec-summary-source-audit/audit/q7uDJG8YQ5c/tool-fix-report.md`. Stopped before omission drafting, as requested. No staging, commit or publication.

## Verification

- Given a clean supported claim whose authentic quote appears before or after its section, when reviewed, then the claim and an otherwise complete review pass and the gate accepts the result.
- Given cross-section evidence with failed semantic checks, a fabricated quote or a false evidence timestamp, when reviewed or validated, then publication remains blocked.
- Given coverage omissions, stale summary binding or malformed claim inventory, when validated, then publication remains blocked.
- `python3 -m unittest discover -s tests -v` must pass in full.
- Before changes transcript SHA-256: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`.
- Before changes protected content manifest: 94 video/protected-audit files, SHA-256 `61e215231ac543a6560a63d8ed8bcbecf32a1efcaa0aebcb334706d3d0285384` (sorted relative path, NUL, SHA-256 bytes per file).

## Plan Change Log

## Review Triage Log

- Quick reviewer: no findings. No patches or deferred findings. Thorough lenses skipped on the oneshot route.
