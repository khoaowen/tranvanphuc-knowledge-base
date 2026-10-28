# Weekly sync

`.github/workflows/weekly-sync.yml` (Sundays 03:00 UTC, or manual dispatch) is the
only production workflow. It calls `scripts/weekly_sync.py` in three steps that share
a JSON report in `$RUNNER_TEMP` (state is read from the report, never from log text):

1. **prepare** – lists the channel newest-first, selects the first distinct unseen ID
   (before any directory exists), queues every other unseen ID as metadata-only
   `pending`, and fetches the selected video's captions (complete result or nothing).
   Captions not ready: the selected ID stays `pending` with a notice; no fallback.
2. **summarize** – the only step that receives `GEMINI_API_KEY` / `GEMINI_MODEL`.
   The complete Reduce prompt must be at most 60,000 characters
   (`--reduce-max-chars`, positive); above it no Reduce request is made. A failed or
   invalid generation restores the prior summary byte-for-byte and runs
   `validate_summaries.py --mark-stale`; with no prior summary only the fetch result remains.
3. **finalize** (`if: !cancelled()`; a cancelled run never commits or pushes) – validates every summary via `validate_video`, runs
   `python -m unittest discover -s tests -v`, stages an explicit allowlist, commits,
   fetches and rebases onto the branch head, re-runs validation and tests on the
   combined tree, then pushes without force.

Exit status of finalize: `0` clean; `1` red but safe progress may be pushed (invalid
summary elsewhere, fetch/generation failure, rebase conflict or other rebase failure,
duplicate video ID after rebase, rejected push); `2` write path blocked, nothing
pushed (transcript changed, unexpected validator result or finalize error, failing
tests, restore/mark failure, missing state). If the block happens after the local
commit (for example tests failing on the rebased tree), that commit stays unpushed
in the runner checkout only.

A committed summary is not a published one: publication stays file-derived (valid,
not stale, hash-bound passing review). Backlog fetching and fidelity review stay
local (`review_batch.py`); the corpus-wide `fetch_transcript.py --check` is not wired
until legacy raw captions are backfilled.

## One-command local Mac run

From a feature-branch checkout, run **`./weekly-sync`**. Requires Python 3.12+
with venv support, Git, and authenticated `gh`; no Actions runner is registered.
The launcher manages a cached virtual environment outside the checkout, installs
the pinned requirements, runs preflight, previews detection, and asks before
fetching. It prompts for the Gemini key with hidden input (never saved), obtains
`GEMINI_MODEL` through `gh`, and asks again before finalize commits and pushes to
the displayed branch. It refuses main/master and unrelated dirty/staged work.

Logs, `before.sha`, and `report.json` are saved in the displayed evidence directory.
To resume prepared work without fetching again, use `./weekly-sync --resume DIR`.
An exported `WEEKLY_RUN` pointing to an existing report also resumes it automatically
(for the owner's in-progress live run). Successful summary generation is not repeated.
After any recorded failure or finalized report, stop and inspect; do not delete the
report or retry a known video to manufacture success. For a later independent week,
use a new terminal without that old `WEEKLY_RUN` variable.

This is an interactive, manually started local run, not an unattended weekly
schedule or evidence of GitHub Actions execution. Inspect the local evidence and
record that distinction explicitly during owner acceptance.

## Owner live-run inspection checklist

Dispatch **Weekly sync** on the real channel, then check:

- [ ] Run URL recorded; job status matches the report (red only for real failures).
- [ ] Selected ID is the newest unseen upload; the pending list is the other unseen IDs.
- [ ] Pending directories hold `metadata.json` only; only the selected video has
      transcript, `raw/` and provenance.
- [ ] Step summary / logs show the validation report and published set; no `GEMINI_API_KEY`
      value, `claude`, or `--check` anywhere in the logs.
- [ ] Commit list: only `metadata.json`, `transcript.md`, `raw/*`, `summary.md`,
      `summary.stale` under `videos/`; `git diff --stat <before> -- videos/` shows no
      change to existing transcripts/raw files.
- [ ] No unseen video: the run is a no-op (tests and validation ran, no commit).
- [ ] Record the run URL, commit SHA (or no-diff) and acceptance in the build evidence.
