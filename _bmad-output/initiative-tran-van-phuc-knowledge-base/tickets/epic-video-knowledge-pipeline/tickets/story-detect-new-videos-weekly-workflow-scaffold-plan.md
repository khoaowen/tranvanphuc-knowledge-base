---
title: 'Detect new videos + weekly workflow scaffold'
type: 'feature'
ticket: '1'
created: '2026-03-21'
status: done
baseline_revision: '14d7b38fda284f4b770461c33e46aa31e5f384a2'
route: 'full'
route_source: 'auto'
risk: 'medium'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** The repo has no way to tell which of Dr. Trần Văn Phúc's channel videos are already processed versus genuinely new, and no scheduled trigger exists to run that check weekly.

**Approach:** Add `scripts/detect_new_videos.py`, which lists the channel's uploaded video IDs via `yt-dlp` (no API key needed — verified locally against the real channel), diffs against video IDs already recorded in `videos/*/metadata.json`, and emits the new-video-id list. Add `.github/workflows/weekly-sync.yml` scaffolding a cron (Sunday, after the doctor's usual Saturday upload) plus `workflow_dispatch`, with Python setup and a step invoking the script.

## Boundaries & Constraints

**Always:** Use `yt-dlp` (already installed, confirmed working against channel `UC79E6KatRfXbmdWVWGncsew` and listing seed video `q7uDJG8YQ5c` among 140 uploads) — no YouTube Data API key/secret. Treat a missing or empty `videos/` directory as zero known videos (everything channel-side counts as new) rather than erroring. Read known video IDs only from `metadata.json`'s `video_id` field, never from folder names (folder slugs are human-oriented, not IDs, per `repo-structure.md`). Script must be runnable standalone (`python scripts/detect_new_videos.py`) and print the new-video-id list in a form later stories can consume (one ID per line to stdout, plus a GITHUB_OUTPUT-compatible `new_videos` list when `GITHUB_OUTPUT` env var is set, for the workflow step). Workflow only wires up this detection step for now — later stories append fetch/summarize/commit steps; do not stub those.

**Never:** Do not fetch transcripts or metadata beyond the ID list (that is story 2). Do not create a `videos/` directory or any seed content. Do not introduce a YouTube Data API key/secret. Do not hardcode `q7uDJG8YQ5c` as a special case in the script — it's only a verification fixture.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| No `videos/` dir yet | Repo has no `videos/` directory | All channel video IDs reported as new | No error; treat as empty known-set |
| Known video present | A `videos/<slug>/metadata.json` exists with `video_id` matching a channel upload | That ID excluded from the new-video list | No error |
| Seed video absent | `q7uDJG8YQ5c` has no `videos/` folder | `q7uDJG8YQ5c` appears in the new-video list | No error |
| yt-dlp failure (network/rate-limit) | `yt-dlp` subprocess exits non-zero or returns empty | Script exits non-zero with a clear stderr message | Non-zero exit code; workflow step fails visibly |
| Malformed `metadata.json` | A videos/ subfolder's `metadata.json` is missing or has no `video_id` key | That folder is skipped (logged), does not crash the run | Warning to stderr, continue |

</frozen-after-approval>

## Code Map

- `scripts/detect_new_videos.py` -- new file; no prior code to reuse. Must not depend on packages beyond `yt-dlp` (already present as a system binary, invoked via `subprocess`) and the Python stdlib (`json`, `pathlib`, `os`, `sys`, `argparse`).
- `.github/workflows/weekly-sync.yml` -- new file; scaffold only (detect step), later stories append jobs/steps for fetch/summarize/commit/consolidate.
- `requirements.txt` -- new file at repo root; pins `yt-dlp` for the workflow's `pip install -r requirements.txt` step (local yt-dlp is a standalone binary install, not pip-tracked, so CI needs its own pinned install).
- `videos/` -- does not exist yet; script must tolerate its absence (see Edge-Case Matrix).
- `_bmad-output/.../repo-structure.md` -- defines `metadata.json`'s `video_id` field and the `videos/<slug>/` layout this script reads against.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/detect_new_videos.py` -- implement `get_channel_video_ids(channel_id)` (runs `yt-dlp --flat-playlist --print "%(id)s" <channel-uploads-url>`, returns ordered list, raises/exits non-zero with stderr message on failure or empty result), `get_known_video_ids(videos_dir)` (globs `videos/*/metadata.json`, reads `video_id`, skips+warns on missing/malformed), and a `main()` that diffs the two, prints new IDs one per line to stdout, and — when `GITHUB_OUTPUT` env var is set — appends a `new_videos` output (newline-joined or JSON list, workflow consumes either) -- this is R1's detection logic and the sole input later stories (fetch/summarize) consume.
- [ ] `.github/workflows/weekly-sync.yml` -- add `on: schedule` (cron for Sunday, e.g. `0 3 * * 0`, after Saturday's usual upload) and `on: workflow_dispatch`; one job `detect` that checks out the repo, sets up Python 3.12, `pip install -r requirements.txt`, runs `python scripts/detect_new_videos.py`, and surfaces its output -- the only automation entry point for the whole pipeline; later stories append steps/jobs to this same workflow rather than creating new ones.
- [ ] `requirements.txt` -- add a pinned `yt-dlp` version -- keeps CI's install reproducible independent of the local system binary.

**Acceptance Criteria:**
- Given no `videos/` directory exists, when `detect_new_videos.py` runs against channel `UC79E6KatRfXbmdWVWGncsew`, then `q7uDJG8YQ5c` appears in the printed new-video-id list.
- Given a temporary `videos/<slug>/metadata.json` is created with `video_id` set to some other real channel upload ID, when the script runs, then that ID is excluded from the new-video list while other channel uploads (including `q7uDJG8YQ5c`) still appear.
- Given the workflow file, when triggered via `workflow_dispatch` against the real channel, then the run succeeds and its logs show the detect step's new-video-id output.
- Given a `videos/<slug>/metadata.json` that is malformed or missing `video_id`, when the script runs, then it logs a warning to stderr and completes without crashing.

## Implementation Notes

## Plan Change Log

## Review Triage Log

- Finding: `requirements.txt:1` pins `yt-dlp==2026.3.17`, claimed to not match a real published release (padding mismatch vs. `yt-dlp --version` output `2026.03.17`).
  Verdict: **false**. Verified directly against PyPI (`pip index versions yt-dlp` and `pip download yt-dlp==2026.3.17 --no-deps`): `2026.3.17` is a real, unpadded-in-metadata PyPI release (confirmed in the version list and successfully downloaded as `yt_dlp-2026.3.17-py3-none-any.whl`). The locally installed binary's `--version` output is zero-padded for display only; the PyPI version string itself is unpadded. The pin resolves fine.
- Finding: `scripts/detect_new_videos.py:16-24` (`get_channel_video_ids`) calls `subprocess.run(...)` with no `timeout`, so a network stall/rate-limit hang (vs. a clean non-zero exit) hangs the detect step indefinitely instead of failing visibly.
  Verdict: **medium**. Confirmed by reading the code: no `timeout=` kwarg is passed, so a hung `yt-dlp` process blocks the subprocess call forever; the workflow step would only end via GitHub Actions' own long default job timeout, wasting CI minutes and delaying failure visibility for the weekly sync. Routed to `patch`: smallest fix is adding a `timeout=` kwarg and catching `subprocess.TimeoutExpired` to exit non-zero with a clear stderr message, consistent with the matrix's existing non-zero/empty-result handling. Trivial, no new public surface, no new guarded state.

## Design Notes

yt-dlp was chosen over the YouTube Data API for R1's channel-listing need: it's already installed locally, requires no API key/secret to provision or rotate in GitHub Actions, and was verified against the real channel (140 uploads listed, seed video `q7uDJG8YQ5c` present). This is a narrower, lower-risk choice than committing to yt-dlp for transcript fetching too — story 2 (R2) re-evaluates the source for transcripts specifically and may choose differently (e.g. a transcript-specific library) since scraping fragility risk is higher for transcript text than for a simple ID listing.

Known-video detection deliberately reads `metadata.json`'s `video_id` field rather than parsing folder names, because the naming convention (`<date>-<number>-<slug>`) is lossy with respect to the actual YouTube ID and is meant for human browsing, not machine lookup.

## Verification

**Commands:**
- `python scripts/detect_new_videos.py` -- expected: exits 0, prints video IDs (one per line) to stdout; with no `videos/` dir, includes `q7uDJG8YQ5c`.
- `mkdir -p videos/tmp-test/ && echo '{"video_id": "<some-other-real-id>"}' > videos/tmp-test/metadata.json && python scripts/detect_new_videos.py; rm -rf videos/tmp-test` -- expected: that ID is absent from output, `q7uDJG8YQ5c` still present.
- `act workflow_dispatch -W .github/workflows/weekly-sync.yml` (if `act` available) or a real `gh workflow run weekly-sync.yml` + `gh run watch` -- expected: run succeeds, detect step's log shows the new-video-id output.

**Manual checks (if no CLI):**
- Open the Actions tab on `github.com/khoaowen/tranvanphuc-knowledge-base` after a `workflow_dispatch` run and confirm the detect step's output log lists `q7uDJG8YQ5c`.
