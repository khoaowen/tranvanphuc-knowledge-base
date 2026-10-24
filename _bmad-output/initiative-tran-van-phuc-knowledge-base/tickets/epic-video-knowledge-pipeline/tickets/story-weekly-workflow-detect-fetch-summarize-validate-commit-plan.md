---
title: 'Weekly workflow: detect, fetch, summarize, validate, commit'
type: 'feature'
ticket: '11'
created: '2026-10-24'
status: 'built'
baseline_revision: '415a9fc18b0af1fad65cf6261f07d96c2daf6464'
route: 'full'
route_source: 'auto'
risk: 'medium'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick-inline']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** `weekly-sync.yml` only detects and echoes new IDs. Nothing fetches, queues, summarizes, validates, gates by tests, or commits, and the Reduce prompt has no size guard.

**Approach:** Add a testable Python orchestrator (`scripts/weekly_sync.py`) that the existing workflow calls: select the newest unseen ID, queue the rest metadata-only, fetch and Gemini-summarize the selected one, validate every summary via the per-video API, then allowlist-stage, rebase, re-gate and push. Ticket 1.11's thirteen refined criteria are the acceptance contract; the ticket file is authoritative on every detail below.

## Boundaries & Constraints

**Always:** Consume the shipped summary contract, queue states, hash-bound review gate, and `validate_video` results unchanged. Existing transcript/raw/provenance bytes stay identical. Exit 0 permits staging, exit 1 permits safe progress but ends red, exit 2/unexpected fails closed with no commit or push. `python -m unittest discover -s tests -v` must pass before any commit. Stage an explicit allowlist only; rebase onto the remote head, never force push, then rerun tests and validation on the combined tree. `GEMINI_API_KEY` reaches only the summarize step; redact it everywhere.

**Never:** No second production workflow; do not edit `summarize-seed.yml`. No `claude -p`, no local fidelity review, no all-video `fetch_transcript.py --check`, no legacy backfill. No backlog fetching, no persisted publication flag, no Reduce truncation or hierarchical Reduce, no automatic conflict resolution, no writes to the real remote from tests.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| New videos | newest-first IDs, some unseen | first distinct unseen selected before any dir is created; others metadata-only pending; selected fetched and summarized | per-item diagnostic, no guessed destination |
| No new video | all IDs known | no fetch/Gemini; tests and validation run; empty diff means no commit | detection error is a failure, never an empty success |
| Captions not ready | selected ID lacks vi captions | selected stays metadata-only pending, notice, no fallback to older ID | other fetch errors fail the job |
| Generation fails | prior summary exists | prior bytes restored, `--mark-stale <id>` on them, marker committed if gates allow | restore or mark failure blocks commit/push |
| Generation fails | no prior summary | fetch result only (`transcribed`); no marker | red status |
| Reduce over ceiling | prompt length above 60,000 (configurable, positive) | no Reduce call, counts diagnostic, safe failure path | nonpositive config fails before model calls |
| Push race | remote head moved | non-conflicting: rebase, rerun gates, push | conflict: abort rebase, name branch and paths, fail; rejected push fails, no force |

</frozen-after-approval>

## Code Map

- `.github/workflows/weekly-sync.yml` -- extend: `permissions: contents: write`, `concurrency` (group per ref, `cancel-in-progress: false`), full checkout, step-scoped Gemini env, final-status propagation. Keep cron and dispatch.
- `scripts/weekly_sync.py` -- new orchestrator: select, queue pending, fetch, summarize, validate, regenerate-failure handling, allowlist staging, rebase, push, report.
- `scripts/detect_new_videos.py` -- `get_channel_video_ids` (newest first) and `get_known_video_ids` (by metadata ID). Reuse; it exits on error, so keep detection failures red.
- `scripts/fetch_transcript.py` -- `fetch_metadata`, `fetch_one_video` (complete fetch result, staged and atomic), `video_dir_for`, `write_video_files`. Reuse; add a metadata-only pending writer that never overwrites. Do not change fetch or raw bytes behavior.
- `scripts/summarize.py` -- `summarize_video`, `build_reduce_prompt`, `call_with_retry` (TransientError and 429 budgets exist), `GeminiClient`, `scrub`. Add the Reduce ceiling check before the Reduce call; summary written only after all calls succeed.
- `scripts/validate_summaries.py` -- `validate_video` (invalid, review_missing, published, state, reasons), `--mark-stale`, exit codes 0/1/2, `TranscriptChanged`. Consume by import.
- `scripts/queue_state.py` -- `list_videos`, `video_state`, `publishable`. Reuse.
- `tests/` -- add `test_weekly_sync.py` plus Reduce-bound, retry and redaction cases in `test_summarize.py`; temp Git repos with a local bare remote.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/summarize.py` -- add configurable positive Reduce prompt ceiling (default 60,000), checked on the complete prompt before the call; validate config before any model call; tests for boundary, +1, overhead, and retry recovery/exhaustion for map and Reduce without sleeping; sentinel-key redaction -- criteria 9, 10, 12
- [ ] `scripts/fetch_transcript.py` -- metadata-only pending writer (no overwrite, ID/destination ambiguity stops that item) -- criterion 2
- [ ] `scripts/weekly_sync.py` -- orchestrator with injectable detect/fetch/summarize/git seams -- criteria 1-8, 11
- [ ] `tests/test_weekly_sync.py` -- offline fixtures for every I/O row plus all validator exits, valid-unreviewed versus published, invalid candidate isolation, unittest failure, push race (conflict and rejected), backlog exclusion -- criterion 13
- [ ] `.github/workflows/weekly-sync.yml` -- wire the orchestrator, permissions, concurrency, secrets scoping, red status after safe push -- criteria 1, 6, 12
- [ ] `docs/` -- short note on the weekly workflow and owner's live-run inspection checklist

**Acceptance Criteria:**
- Given the refined ticket, when its Given/When/Then criteria 1-13 are exercised by offline tests, then all pass with no live network, Gemini or remote writes.
- Given the owner dispatches the workflow on the real channel, when they inspect run URL, selected ID, pending list, report and committed files, then no leak or unintended change exists and acceptance is recorded (criterion 13, hitl).

## Implementation Notes

## Plan Change Log

## Review Triage Log

Inline quick self-review (no subagent authorized): no high/medium findings. One real defect fixed during build: the Gemini error body was truncated before key redaction, which could leak a key straddling the cut; now scrubbed first. Manual criterion 13 (owner live run of the real channel) remains open.

## Design Notes

Keep the orchestrator a thin sequence over existing helpers; put git and subprocess behind small functions so temp-repo tests drive them. Candidate summaries are generated in a temp location or backed up so a failed or invalid replacement can be restored byte-for-byte. The report is a JSON file passed between workflow steps, never parsed from human text.

## Verification

**Commands:**
- `python -m unittest discover -s tests -v` -- expected: all pass, no credentials
- `git diff --check` -- expected: clean
- `git diff --stat 415a9fc -- videos/` -- expected: empty

**Manual checks (if no CLI):**
- Owner dispatches Weekly sync on the real channel and inspects selected ID, pending backlog, validation report, final status, commit list and logs.
