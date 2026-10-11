# review-batch (local backlog summarizer)

`./review-batch` summarizes every video that has no `summary.md`, newest first, through
`claude -p` (your Claude subscription login). **Local only; never run in CI.**

    ./review-batch                      # all unsummarized videos, Sonnet
    ./review-batch --model haiku --limit 1
    ./review-batch --no-commit

- A video with `metadata.json` but no `transcript.md` is fetched with `fetch_transcript.py` first.
- Each finished video is committed on its own (`content: summary for <id> (review-batch)`); nothing is pushed.
- Re-running resumes: finished videos have a `summary.md` and are skipped. The backlog uses the same queue.
- State comes from `scripts/queue_state.py` (pending / transcribed / summarized), reused by entry 10.
- The prompt, schema and vocabulary loading are `summarize.py`'s (entry 8).

## Short 429 vs usage limit

`classify_failure()` in `scripts/review_batch.py` decides. It parses `claude -p --output-format json`
(`is_error`, `result`):
- text with "usage limit" / "hit your limit" / "limit reached" -> usage limit: stop, print the text
  after "resets" (verbatim), exit 0, earlier commits kept.
- text with "429" / "rate limit" / "overloaded" -> short 429: backoff and retry (max 5), then skip the video.
- anything else -> that video fails; the run continues.

**Observed so far:** only an expired login (2026-10-11): `is_error: true`,
`result: "Failed to authenticate: OAuth session expired and could not be refreshed"`, exit 1
(treated as a per-video failure; run `claude` and log in again). The real wording of a usage limit and
of a short 429 has **not** been observed yet. After the first real limit hit, record the exact text
here and adjust the patterns in `classify_failure`.

## Stubbing

`--claude-cmd <script>` or env `REVIEW_BATCH_CLAUDE` replaces `claude`. The stub reads the prompt on
stdin and prints the JSON result (`{"is_error":false,"result":"..."}`) on stdout.
