---
type: initiative
title: Tran Van Phuc Knowledge Base
parent: none
covers: [CAP-1, CAP-2, CAP-3, CAP-4, CAP-5, CAP-6, CAP-7]
after: []
assignee: ""
risk: medium
---

# Tran Van Phuc Knowledge Base

## Description

A durable, growing, public knowledge base distilled from Dr. Tran Van Phuc's weekly health livestreams, modeled on `mlabonne/llm-course`: a versioned GitHub repo as the source of truth, feeding a ChatGPT Custom GPT people can chat with about the topics he has covered. See the spec for the full contract.

## Outcome

Within 24-48h of each Saturday upload, the new video's transcript and structured summary land in the public repo, the consolidated `knowledge-gpt/` files regenerate automatically, and — after a brief manual re-upload in the GPT Builder — a user chatting with the Custom GPT in any language gets an answer grounded in Dr. Phuc's own words, with the medical disclaimer shown (spec's Success signal).

## Requirements

See `spec-tran-van-phuc-kb/spec-tran-van-phuc-kb.md`, section Capabilities (CAP-1 through CAP-7).

## Done when

1. A scheduled GitHub Actions run detects and processes any video published since the last run, verified weekly after the doctor's usual Saturday upload (CAP-1).
2. Every processed video has a transcript, a structured summary, and metadata committed under `videos/<slug>/` (CAP-2, CAP-3).
3. A visitor can browse by topic or by date from the README and reach any video's transcript and summary in two clicks or fewer (CAP-4).
4. `knowledge-gpt/` regenerates on every pipeline run and never exceeds 20 files or OpenAI's per-file Knowledge size ceiling (CAP-5).
5. Documented, repeatable steps exist for re-uploading `knowledge-gpt/` into the Custom GPT Builder, and the GPT answers a question in a non-Vietnamese language grounded in the doctor's content with the disclaimer shown (CAP-6).

## Boundaries

The automated pipeline (detection, transcript fetch, summarization, repo organization, consolidation) and the one-time, documented manual hand-off into the Custom GPT. Not the GPT itself as a hosted service (OpenAI's, operated manually by the user outside this repo), not fact-checking or translation quality (spec's Non-goals), not raw video/audio hosting. Tracer path: one real past video detected, fetched, summarized, committed, and consolidated end to end.

- Touch point: coding agents (Claude Code, Codex) reading the repo via plain `git clone` — CAP-7, satisfied automatically by the repo structure the epic delivers; no dedicated story or tooling.

## References

- spec — _bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/spec-tran-van-phuc-kb.md, section Capabilities
- constraint — same spec, section Constraints (20-file GPT cap, no Knowledge-upload API, text-only, free CI, public repo naming, disclaimer everywhere)
- architecture — same spec folder, pipeline-architecture.md (Option C flow)
- structure — same spec folder, repo-structure.md (target repo layout, naming convention, consolidation rule)
- disclaimer — same spec folder, disclaimer.md (canonical text)

## Notes

- Decision: one epic covers CAP-1 through CAP-6 — single owner, single pipeline, no boundary justifies a split (user's request, this session).

## Transcript fidelity continuation — 2026-10-20

[Fresh-context handoff](continuation-transcript-fidelity.md) tracks the caption-fidelity research, pending human listening bundle, c068/c163 correction proposals, and the raw-caption implementation branch (in-review, not merged). It also records which earlier five-disagreement / eleven-omission findings remain applicable. Publication remains blocked; no new fidelity decisions or content corrections are approved by this handoff.
