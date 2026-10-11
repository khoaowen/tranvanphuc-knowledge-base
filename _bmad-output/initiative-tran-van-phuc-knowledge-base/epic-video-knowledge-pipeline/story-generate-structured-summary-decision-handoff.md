# Handoff (condensed 2026-10-11): Generate structured summary (CAP-3)

Status: the earlier decision-session handoff is SUPERSEDED. It assumed a paid Anthropic API auditor
(`claude-sonnet-5-5`), Workload Identity Federation, dollar caps and paid Gemini. The new constraint is
$0 beyond the Claude Pro subscription: no API credits, no paid Gemini, no subscription login in CI.
`story-generate-structured-summary-plan.md` (status: draft) still carries those superseded decisions
and must be reworked with the spec amendment. Do not implement from it as written.

## Still-valid facts
- Seed video `q7uDJG8YQ5c`: 12765 s (~3.5 h), transcript 305,272 bytes, 5,330 lines, ~51k words.
  Real Vietnamese token ratio is unmeasured. Chunking/map-reduce is needed for Pro-limit runs.
- Gemini free tier: Google may use submitted content to improve products. The repo content is public,
  so this is acceptable only for public transcripts. Paid tier does not use content. Tier of our key
  is UNVERIFIED (check AI Studio and Cloud billing). A smoke test on 2026-10-11 returned HTTP 200 from
  `gemini-3.6-flash` using GitHub secret `GEMINI_API_KEY` (vars: `GEMINI_MODEL`, `LLM_PROVIDER=gemini`).
- Gemini 3.6 flash paid pricing doubles on 2027-01-01. Irrelevant on the free tier. Free-tier rate and
  daily limits against 3.5 h transcripts are untested.
- Anthropic: Pro includes no API credits. Usage is shared across claude.ai and Claude Code with a
  5-hour and a weekly limit.
- Model IDs: dateless IDs are pinned snapshots (4.6 generation and later).
- Vocabulary: `topics/vocabulary.md` does not exist. Topic names in `repo-structure.md` are candidates only.
  Initial entries need evidence and timestamps, and human approval.
- Fidelity standard (keep): summary reflects only the Vietnamese transcript. No external fact-checking,
  no medical validation, no automatic medical repair. Model agreement is not medical correctness.

## Dropped (superseded)
Anthropic auditor, WIF/OIDC rule, `TVP_AUDITOR_ANTHROPIC_API_KEY`, dollar ceilings, Batch/caching
pricing, qualification check against a paid API.
