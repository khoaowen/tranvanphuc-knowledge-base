
- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-gemini-ci-summarizer-plan.md`
  summary: summarize.py does not retry transient 5xx/timeout errors; only 429 is backed off.
  evidence: plan specifies backoff for 429 only; a late 503 discards earlier map calls and wastes free-tier RPD.
- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-gemini-ci-summarizer-plan.md`
  summary: Reduce prompt has no size guard and no maxOutputTokens; long videos could exceed limits (unverified until live run).
  evidence: docs/summarizer-limits.md notes it; settle with the live seed measurement.

- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-ci-validator-and-publish-gate-plan.md`
  summary: Disclaimer banner is accepted anywhere in summary.md and compared to the summarize.py constant, not disclaimer.md.
  evidence: validate_summaries.py check is `DISCLAIMER_BANNER not in summary`; contract says directly under the header.
- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-ci-validator-and-publish-gate-plan.md`
  summary: A summary made only of "Đã gộp vào mục" stub sections passes the **Q: rule; sections after ## Glossary break section-body slicing.
  evidence: merged exemption is per section; bounds assume Glossary is last.
- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-ci-validator-and-publish-gate-plan.md`
  summary: --mark-stale marks only the first directory when two share a video_id.
  evidence: main() uses match[0].
- source_plan: `_bmad-output/initiative-tran-van-phuc-knowledge-base/epic-video-knowledge-pipeline/story-ci-validator-and-publish-gate-plan.md`
  summary: CI workflows do not run python unittest, so tests/ are not gated (wire in entry 11).
  evidence: grep for unittest/pytest in .github finds nothing.
