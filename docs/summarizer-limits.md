# Gemini free-tier summarizer limits

Status: **measured on the seed run** (workflow run 38167907304, model
`gemini-3.6-flash`, free tier confirmed by the user in AI Studio). RPM, TPM and
RPD **ceilings were not reached and not read from AI Studio**; the table says
what was observed versus what is unknown.

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

| Item | Setting | Measured / observed |
|------|---------|---------------------|
| Model | `vars.GEMINI_MODEL` | `gemini-3.6-flash` |
| RPM | — | Not hit: 0 HTTP 429 in 6 calls (about 1 call per 1-2 min incl. retries). Ceiling unknown. |
| TPM | — | Not hit. Largest call: 27,735 prompt + 2,088 output + 3,790 thinking tokens. Whole run: ~118k prompt, ~15.5k output tokens. Ceiling unknown. |
| RPD | — | Not hit. The run used 6 successful calls plus 6 retried 5xx attempts (12 requests); the daily ceiling is unknown. |
| Chunk size | 60,000 chars (5 chunks + 1 reduce = 6 calls for the seed) | Works: ~26-28k prompt tokens per map call, 8-34 s per call without retries. Keep 60,000. |
| Pacing between calls | 6 s | No 429 at 6 s. Keep 6 s. |
| 429 behavior | backoff 10 s x 2^n + 0-5 s jitter, max 5 retries; `Retry-After` honored | Not observed (0 hits), so the 429 path is stub-tested only. |
| 503 "high demand" (UNAVAILABLE) | same backoff, separate retry budget | Frequent: 1st run died on it; 2nd run hit it 6 times (3 on call 1, 2 on call 4, 1 on reduce). All recovered within 3 retries. |
| Run time / output | — | About 12 min total. summary.md body is 27,496 chars = 11.2% of the transcript. |

## Behavior notes

- A per-day quota (`quotaId` containing `PerDay`) stops the run with a reset
  hint (daily quotas reset at midnight Pacific time); nothing is written.
- The reduce call receives all map outputs in one prompt; very long videos
  could exceed the model's input limit (not handled).
