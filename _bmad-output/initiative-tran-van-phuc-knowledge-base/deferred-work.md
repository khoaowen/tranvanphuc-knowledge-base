
- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-gemini-ci-summarizer-plan.md`
  summary: summarize.py does not retry transient 5xx/timeout errors; only 429 is backed off.
  evidence: plan specifies backoff for 429 only; a late 503 discards earlier map calls and wastes free-tier RPD.
- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-gemini-ci-summarizer-plan.md`
  summary: Reduce prompt has no size guard and no maxOutputTokens; long videos could exceed limits (unverified until live run).
  evidence: docs/summarizer-limits.md notes it; settle with the live seed measurement.
