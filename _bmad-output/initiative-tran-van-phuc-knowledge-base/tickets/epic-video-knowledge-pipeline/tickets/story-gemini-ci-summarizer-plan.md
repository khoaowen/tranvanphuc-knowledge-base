---
title: 'Gemini CI summarizer (summarize.py)'
type: 'feature'
ticket: '8'
created: '2026-10-11'
status: 'done'
baseline_revision: '36d00d88fdeaae115cd588cf76f442fadf29579a'
route: 'full'
route_source: 'auto'
risk: 'high'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/summary-contract.md'
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/disclaimer.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Transcripts (seed `q7uDJG8YQ5c`, ~51k Vietnamese words) have no retrieval-layer `summary.md`; CI needs a $0 Gemini free-tier summarizer whose schema and prompt entries 9 and 10 reuse.

**Approach:** `scripts/summarize.py` chunks the transcript by timestamp, map-reduces through an injectable Gemini client, and atomically writes `summary.md` per `summary-contract.md`. Free-tier limits are measured on the seed; chunk size and pacing come from that result.

## Boundaries & Constraints

**Always:** Key only from env `GEMINI_API_KEY`, model from `GEMINI_MODEL`; never print, log or write either value or request headers. Free tier is confirmed by the user (AI Studio, this session). Write temp file then `os.replace`. Disclaimer text copied verbatim from `disclaimer.md`. Hedges kept; no medical content absent from the transcript. Back off with jitter on 429, honoring `Retry-After`. Load `topics/vocabulary.md` into the prompt only if it exists. Stdlib only (no new dependency).

**Decisions:** Live seed run happens in CI via a manual-only `workflow_dispatch` workflow `.github/workflows/summarize-seed.yml` (uses `secrets.GEMINI_API_KEY`, `vars.GEMINI_MODEL`; uploads summary.md and the measurement log as an artifact; entry 11 later absorbs it). Measured limits are recorded in `docs/summarizer-limits.md`.

**Never:** Implement from the dropped `story-generate-structured-summary-plan.md`. No paid API, no Anthropic/`claude -p` path (entry 9), no validator (entry 10), no weekly-workflow wiring (entry 11), no `topics/vocabulary.md` creation (entry 4).

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Happy | video dir with transcript.md + metadata.json, stub client | summary.md with header, banner, timestamped `?t=` sections, questions, glossary | none |
| 429 | client raises rate-limit | retry with backoff, then succeed | after max retries exit non-zero, no summary.md written |
| Daily quota | client signals exhausted | stop, print reset hint, no partial file | exit non-zero |
| Crash mid-write | failure after temp write | existing summary.md untouched | temp file removed |
| No vocabulary | topics/vocabulary.md absent | free-form tags | none |
| Vocabulary present | file exists | its terms in prompt | none |

</frozen-after-approval>

## Code Map

- `scripts/fetch_transcript.py` -- writes `videos/<date>-<slug>/{transcript.md,metadata.json}`; mirror its argparse/Path style and `[HH:MM:SS] text` line format. Do not modify.
- `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/` -- seed input (metadata keys: video_id, title, url, published_at, duration).
- `_bmad-output/.../summary-contract.md` -- required structure; `disclaimer.md` -- banner text.
- `requirements.txt`, `.github/workflows/weekly-sync.yml` -- unchanged (stdlib; weekly wiring is entry 11).

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/summarize.py` -- chunking, map/reduce, schema+prompt constants, urllib Gemini client (injectable `client(prompt)->text`), 429 backoff, atomic write, CLI `summarize.py <video-dir>` -- core deliverable
- [ ] `.github/workflows/summarize-seed.yml` -- workflow_dispatch only; runs summarize.py on the seed with secret/var env; uploads artifact -- live measurement without exposing the key
- [ ] `tests/test_summarize.py` -- stub-client tests for the matrix (chunking, atomic write, 429, vocabulary, secret never in output)
- [ ] `docs/summarizer-limits.md` -- measured free-tier RPM/TPM/RPD, chunk size, pacing, observed 429 behavior from the seed run

**Acceptance Criteria:**
- Given the seed and the live client, when run, then summary.md exists, is far shorter than the transcript and has every contract element.
- Given any run, when output and logs are inspected, then no key value appears.
- Given the user reviews the seed summary, then they approve it.

## Verification

**Commands:**
- `python -m unittest discover tests` -- expected: all pass
- `python scripts/summarize.py videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua` -- expected: stub run writes summary.md; the live run is the `summarize-seed.yml` dispatch
