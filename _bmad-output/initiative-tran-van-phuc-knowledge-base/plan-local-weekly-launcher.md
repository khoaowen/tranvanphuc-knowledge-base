---
title: One-command local weekly sync
created: '2026-10-28'
type: chore
ticket: ''
status: built
baseline_revision: '48337a15d2a5b0985ed4d8e3ce97c84442660584'
route: oneshot
route_source: auto
risk: low
review: quick
review_source: pinned
lenses_ran: [quick]
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

Provide one local executable command, ./weekly-sync, for the owner's Mac each week. Use the existing Python phase CLI rather than duplicate pipeline behavior. Bootstrap a private virtual environment outside the checkout from requirements.txt and run preflight automatically. Prompt securely for the Gemini key only when needed; never store it or pass it to setup, tests, git or finalize. Resolve the Gemini model from the repository's gh variable, with a clear failure if unavailable. Show the target branch, selected video and pending count and request confirmation before new fetch work, and again before finalize commits/pushes. Save phase logs/report and baseline SHA outside the repository. Stop on process errors OR failures/fatal entries in the report. Never force-push or re-fetch known videos.

Resume the owner's existing prepared report via WEEKLY_RUN (already exported in their terminal) or an explicit --resume directory; do not re-run prepare or repeat an already successful summarize. Refuse unrelated dirty/staged work and refuse detached HEAD/main/master for this acceptance run. Do not modify weekly-sync.yml or add an Actions runner. Leave pre-existing kanban.html untouched. This launcher improves the local route only; it cannot itself establish GitHub Actions live-run acceptance or mark story 1.11 done.

</frozen-after-approval>

## Implementation Notes

Implemented executable weekly-sync with stdlib bootstrap, private cached venv, per-attempt preflight logs, persistent evidence directory, report resume through WEEKLY_RUN/--resume, hidden key prompt and explicit finalize confirmation. Existing prepared Mac report is accepted without repeat prepare. Added local-use docs and ten hermetic launcher tests covering fresh/resume/cancel/failure/secret scoping. The wrapper grew beyond the initial line estimate to make failure handling and evidence preservation explicit; no additional user-facing goal was introduced. No live pipeline phases run on this server.

## Plan Change Log

## Review Triage Log

- Medium / patch: WEEKLY_RUN with a missing report could start fresh; now both explicit and environment resume fail closed. Regression tests cover missing and valid environment reports.
- Medium / patch: recorded summary_candidate could skip generation after summary deletion; now stop without regenerating. Regression test added, and mock summarization now creates its output file as production does.
- Medium / patch: empty/null or wrong-version resume JSON could fall through to a fresh run. Resume presence now selects the path explicitly, and invalid type/version is rejected before work. Regression covers both --resume and WEEKLY_RUN with {}, null, arrays and wrong versions.
- Final independent re-review: no findings. Final verification: 224 tests pass, validator exit 0, executable --help exits 0. Fourteen hermetic launcher cases cover resume, failures, cancellation, branches, staged/dirty work, invalid state and secret scoping. No live fetch, Gemini call or data push was performed by these tests.

## Verification

Compile launcher; run hermetic simulated fresh, resume, failure and cancellation paths including explicit assertions no prepare on resume, no finalize on recorded failures, no secret outside summarize, and no repeated summarize after successful resume. Run complete unittest suite and summary validator. Independent quick review before commit. No local live fetching from this server.
