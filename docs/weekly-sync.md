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

## Generated index and GPT files

After validation passes (validator exit 0) and the unit tests pass, finalize runs `scripts/generate_index.py` (the README block between `<!-- index:start -->` and `<!-- index:end -->`, and `topics/<tag>.md`) and `scripts/consolidate.py` (`knowledge-gpt/*.md`, at most 20 files of at most 2,000,000 bytes each, whole summaries packed oldest first). Both read only videos the validator reports `published`, so unvalidated, stale or unreviewed summaries never appear. Changed generated files join the same allowlist-gated commit; `topics/vocabulary.md` is human-owned and never staged. A validator failure (exit 1) commits no generated files. A generator failure (including cap overflow, which writes nothing) makes the run red but does not block the video commit. Run both by hand with `python3 scripts/generate_index.py && python3 scripts/consolidate.py`; reruns on unchanged inputs change nothing. Only files carrying a "generated, do not edit" marker are ever removed.

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

### Recovering prepared artifacts after the report was lost

If prepare succeeded but its evidence directory (with `report.json` and `before.sha`)
was lost, the launcher refuses to start fresh against the untracked prepared files.
Run **`./weekly-sync --recover`** (cannot be combined with `--resume`; an exported
`WEEKLY_RUN` pointing at the lost report is ignored). Recovery is read-only until you
confirm: it never fetches, re-detects the channel, calls Gemini, writes `videos/`, or
stages/commits. `scripts/recover_weekly.py` refuses staged or modified tracked work,
unrelated or ignored extra files (including macOS `.DS_Store`; delete those first),
symlinks, malformed or non-canonical metadata, duplicate IDs (also against the tracked corpus), partial
fetches, more or fewer than one fetched video, and any existing
`summary.md`/`review.md`/`summary.stale`. It requires exactly one complete new fetch
result (raw caption checksum, nonempty parsed captions, exact transcript re-render and
transcript checksum, provenance bound to the metadata ID/URL/track) and every other
new folder holding `metadata.json` only.

It then shows the selected ID, the derived pending count and the replacement
baseline, and asks before adopting. On approval it writes a new
`~/.local/state/tranvanphuc-weekly/recover-*` directory: `report.json` with a
`recovery` section (timestamp, current full HEAD and branch, per-file digests and
inventory digest, selected/pending IDs, caveats) and `before.sha` holding the HEAD at
recovery time. The launcher then continues with summarize (selected video only) and
still asks before finalize commits and pushes; after an interruption use
`./weekly-sync --resume <that directory>`.

Recovery verifies the artifacts on disk; it does not recover the original run. The
original logs, report, `before.sha` and channel listing order remain unavailable;
`before.sha` is a labelled replacement baseline, the report's `unseen` list is left
empty, and pending order is by directory name (published date, then slug), newest
first. Record that distinction during owner acceptance.

This is an interactive, manually started local run, not an unattended weekly
schedule or evidence of GitHub Actions execution. Inspect the local evidence and
record that distinction explicitly during owner acceptance.

## Secret-leak gate

`./weekly-sync` first verifies the pinned scanner and scans the repository (history +
tracked snapshot); `finalize` scans the exact staged index before committing and the exact
commit's history and tree before every push. Any finding or inability to scan stops with
exit 2 and nothing is committed, pushed or uploaded; reports hold only sanitized outcomes.
Supported platforms, recovery and incident steps: [docs/security.md](security.md).

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
