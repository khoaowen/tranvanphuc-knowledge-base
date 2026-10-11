# Gemini free-tier summarizer limits

Status: **not yet measured.** The live seed run (`summarize-seed.yml`,
manual `workflow_dispatch`) has not been executed. The values below marked
"default" are the starting settings in `scripts/summarize.py`, not
measurements. Fill the "Measured" column from the run's `measurement.log`
artifact, then adjust `DEFAULT_CHUNK_CHARS` / `DEFAULT_PACE_SECONDS` to match.

Seed: `q7uDJG8YQ5c`, 5330 transcript lines, 245,832 characters (~51k words).

## How to measure

1. Set repo secret `GEMINI_API_KEY` and repo variable `GEMINI_MODEL` (free-tier
   AI Studio key).
2. Run the "Summarize seed video" workflow. The `measurement.log` artifact has
   one line per call (prompt chars, response chars, 429 count, elapsed, token
   usage as reported by Gemini) plus every 429 with its `Retry-After`/
   `retryDelay` and the wait applied.
3. Read the limits for the model from AI Studio (Rate limits) and compare with
   what the log shows.

## Limits

| Item | Default | Measured |
|------|---------|----------|
| Model | `vars.GEMINI_MODEL` | _pending_ |
| RPM | — | _pending_ |
| TPM | — | _pending_ |
| RPD | — | _pending_ |
| Chunk size | 60,000 chars (5 chunks + 1 reduce = 6 calls for the seed) | _pending_ |
| Pacing between calls | 6 s | _pending_ |
| Observed 429 behavior (`Retry-After`, per-minute vs per-day) | backoff 10 s × 2^n + 0–5 s jitter, max 5 retries; `Retry-After` honored if longer; a per-day quota violation stops the run | _pending_ |

## Behavior notes

- A per-day quota (`quotaId` containing `PerDay`) stops the run with a reset
  hint (daily quotas reset at midnight Pacific time); nothing is written.
- The reduce call receives all map outputs in one prompt; very long videos
  could exceed the model's input limit (not handled).
