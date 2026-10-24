---
title: 'Local review-batch via claude -p'
type: 'feature'
ticket: '9'
created: '2026-10-11'
status: done
baseline_revision: '65a05c88d9d7d812dab4a98ee1cb7894388e5605'
route: 'full'
route_source: 'auto'
risk: 'medium'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['self-review']
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/summary-contract.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Backlog transcripts (all but the newest video) can only be summarized locally on the Claude subscription; there is no resumable runner, and no shared helper that tells which videos still need work (entry 10 needs it too).

**Approach:** Add `scripts/queue_state.py` (derives pending/transcribed/summarized from files) and `scripts/review_batch.py` with a `./review-batch` wrapper. It loops over videos with no summary, newest first, fetches a missing transcript, summarizes each through `claude -p` by reusing entry 8's `summarize.py` pipeline with a `claude` client, and commits per video.

## Boundaries & Constraints

**Always:** Reuse `summarize.py` (`summarize_video`, schema/prompt, atomic write, `call_with_retry`); the claude client is `client(prompt)->text`, injectable (`--claude-cmd` / env `REVIEW_BATCH_CLAUDE`, default `claude`), prompt on stdin, model via `--model` (default `sonnet`, `haiku` allowed). Short 429 → `RateLimitError` (existing backoff). Real usage limit → stop cleanly, print reset time, exit 0 with a summary of what was done, leave no partial file. One `git add <video dir>` + commit per finished video, no push. Skip when `summary.md` exists, so re-running resumes. Load `topics/vocabulary.md` when present (already done by `summarize_video`). Stdlib only.

**Never:** No CI use, no workflow edits, no API key path, no validator (entry 10), no changes to `summarize.py` or `fetch_transcript.py` behavior, no push, no special backlog mode. Do not name the module `queue.py` (shadows stdlib).

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Happy | 2 transcribed videos, stub claude | newest summarized first, 2 summaries, 2 commits | none |
| Resume | 1 of 2 already has summary.md | only the other is processed | none |
| Pending | dir with metadata.json, no transcript.md | fetch_transcript.py called for its id, then summarized | fetch failure: warn, skip, continue, exit non-zero if all failed |
| Short 429 | stub says rate limit once | backoff, retry, success | after max retries: video skipped, no file, continue |
| Usage limit | stub says limit reached, reset time | stop, print reset time, no partial file, earlier commits kept | exit 0 |
| Bad output | stub returns malformed text | no summary.md written, warn, next video | per-video failure |
| Nothing to do | all summarized | prints nothing-pending | exit 0 |

</frozen-after-approval>

## Code Map

- `scripts/summarize.py` -- reuse `summarize_video(video_dir, client, vocabulary_path, chunk_chars, pace_seconds, max_retries, sleep, jitter, log)`, `RateLimitError`, `DailyQuotaExhausted`, `TransientError`, `SummarizeError`, `default_vocabulary_path`, `log_stderr`. Do not modify.
- `scripts/fetch_transcript.py` -- CLI `fetch_transcript.py <id>` writes `videos/<date>-<slug>/{metadata.json,transcript.md}`; call via subprocess.
- `scripts/detect_new_videos.py` -- how known ids are read from `videos/*/metadata.json`; mirror style.
- `tests/test_summarize.py` -- unittest style with stub clients and tmp dirs; mirror. Run `python -m unittest discover tests`.
- `videos/2025-12-06-…/` -- only video on disk; its summary.md exists (approved), so it is `summarized`.
- Directory dates `YYYY-MM-DD-` prefix give newest-first order.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/queue_state.py` -- `list_videos(videos_dir)` -> entries `{dir, video_id, state}` with state `pending` (metadata, no transcript), `transcribed`, `summarized`; `todo(videos_dir)` newest first -- shared with entry 10
- [ ] `scripts/review_batch.py` -- `ClaudeClient` (subprocess, stdin prompt, `--model`, classify output into `RateLimitError` / `UsageLimitReached(reset)` / `SummarizeError`), loop with git commit per video, CLI `--videos-dir --model --claude-cmd --limit --max-retries`
- [ ] `review-batch` -- executable wrapper `exec python3 scripts/review_batch.py "$@"` from repo root
- [ ] `tests/test_review_batch.py` -- stub claude and temp git repo covering every matrix row, plus queue_state states and ordering
- [ ] `docs/review-batch.md` -- usage, observed `claude -p` limit/429 output, how to stub

**Acceptance Criteria:**
- Given two transcribed videos, when `./review-batch` runs, then both get summary.md and one commit each.
- Given a run interrupted after the first, when re-run, then only unfinished videos are processed.
- Given a stubbed short 429 then success, then it retries and finishes; given a stubbed usage limit, then it stops cleanly and prints the reset time.

## Implementation Notes

Implemented directly (no subagent enabled). `claude -p` could not be exercised live: the local OAuth session is expired (`Failed to authenticate`), so the real usage-limit and short-429 wording is unobserved; classifier patterns are best guesses and documented as such in `docs/review-batch.md`. Verified with 42 unit tests and an end-to-end stub run on a temp repo (summary written, one commit, re-run reports nothing pending). The live `--limit 1 --model haiku` check and a second fetched video remain for the human after `claude` login.

## Plan Change Log

## Review Triage Log

Self-review of the diff (no independent lens available). Counts: high 0, medium 1, low 0.
- medium, defer-in-doc: unverified usage-limit / 429 text patterns in `classify_failure` -- settled only by observing a real limit; recorded in docs.
- false: git commit failure leaves summary.md uncommitted and counted as failed -- run still resumes (summary exists), harm negligible.

## Design Notes

Short 429 vs usage limit is unsettled; keep the classifier in one function `classify_failure(returncode, stdout, stderr)` so patterns are adjusted in one place. Start from observed real output of `claude -p --output-format json` (is_error, result text): text containing "usage limit"/"hit your limit"/"resets" (plus an epoch or clock time) → usage limit, and print the reset text verbatim if it cannot be parsed; text containing "429"/"rate limit"/"overloaded" without a reset → short 429. Record what was observed in `docs/review-batch.md`. Unknown output is a per-video failure, never a silent success.

## Verification

**Commands:**
- `python -m unittest discover tests` -- expected: all pass
- `./review-batch --claude-cmd <stub> ` on a temp copy with two transcribed videos -- expected: two summaries, two commits, re-run does nothing
- `claude -p "reply ok"` once -- expected: output format observed and noted in the doc

**Manual checks:**
- The builder fetches a second id with `fetch_transcript.py`, then a real `./review-batch --limit 1 --model haiku` produces a summary and a commit.
