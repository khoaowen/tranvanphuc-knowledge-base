---
type: initiative
title: Tran Van Phuc Knowledge Base
parent: none
after: []
assignee: ""
risk: medium
companions: [_bmad-output/initiative-tran-van-phuc-knowledge-base/audit-record-format.md, _bmad-output/initiative-tran-van-phuc-knowledge-base/repo-structure.md, _bmad-output/initiative-tran-van-phuc-knowledge-base/pipeline-architecture.md, _bmad-output/initiative-tran-van-phuc-knowledge-base/disclaimer.md, _bmad-output/initiative-tran-van-phuc-knowledge-base/summary-contract.md]
---

# Tran Van Phuc Knowledge Base

## Description

A durable, growing, public knowledge base distilled from Dr. Tran Van Phuc's weekly health livestreams, modeled on `mlabonne/llm-course`: a versioned GitHub repo as the source of truth, feeding a ChatGPT Custom GPT people can chat with about the topics he has covered. See the spec for the full contract.

## Outcome

Within 24-48h of each Saturday upload, the new video's transcript and structured summary land in the public repo, the consolidated `knowledge-gpt/` files regenerate automatically, and — after a brief manual re-upload in the GPT Builder — a user chatting with the Custom GPT in any language gets an answer grounded in Dr. Phuc's own words, with the medical disclaimer shown (spec's Success signal).

## Requirements

- R1 (CAP-1): For every claim in each video's current `summary.md`, the auditor records exact claim text, section, verbatim transcript evidence with timestamp, and a classification (supported, mismatch, attribution/qualification issue, unresolved). Success: Claim records exist for 149 + 554 claims (the current `fidelity.extract_claims` output); every record has a class; every non-unresolved record has a quote that is a verbatim substring of `transcript.md` at the cited timestamp (checkable by script); no claim ID is copied from `review.md`.
- R2 (CAP-2): The auditor identifies important transcript topics the summary omits. Success: Each video has an omission list with timestamp range and verbatim anchor quote per topic, or an explicit "none found" after a full-transcript pass.
- R3 (CAP-3): Proposed corrections are recorded apart from the audit findings for later human approval. Success: `proposed-corrections.md` exists per video, every item `pending-human-approval`, and the diff of `videos/` against HEAD is empty for these two videos after the run.
- R4 (CAP-4): Both videos remain blocked from publication throughout. Success: `queue_state.publishable(video_dir)` is false for both before and after; per-video summary states `blocked`.

## Constraints

- Evidence is only current `summary.md`, `transcript.md`, and existing `review.md`; old review verdicts and claim IDs are never treated as current (review.md may be read only as a lead to locate candidate evidence).
- Every claim is checked against the full `transcript.md`, not a section window. A claim with no evidence found is `unresolved`; absence is never assumed from a failed search.
- Speaker identity and qualifications are preserved as spoken; the auditor does not medically correct, and does not infer facts beyond the transcript.
- Audit only: no edits to `summary.md` or `transcript.md`, no changes to `review.md`/`.review-progress.json`, no model calls except read-only subagents on `claude-opus-5-5` (reading, re-check, advisory correction review) which never write outside `audit/`, no publishing, no git commit.
- Outputs are written outside `videos/` (see `audit-record-format.md`).
- The Custom GPT Knowledge tab accepts at most 20 files: the consolidation step (R5) must always fit within this ceiling regardless of how many videos accumulate.
- OpenAI provides no API to push files into a Custom GPT's Knowledge tab: the final hand-off from consolidated files to the live GPT is necessarily a manual upload; the pipeline automates everything up to that point (detection, transcript, summary, repo commit, consolidation).
- No raw video or audio is stored in the repo — text only (transcripts, summaries, metadata), to control repo size and respect YouTube's terms of service.
- Source transcripts stay in Vietnamese; no dedicated translation step is built — the GPT translates on demand at query time. Repo documentation (README, code, commit messages, this spec's own companions) is in English; the disclaimer's canonical text is English, localized at the GPT-response level only.
- The repo is public and must be named/branded to disambiguate from other people named Tran Van Phuc, referencing the channel "Bác sĩ Trần Văn Phúc Official" (channel ID `UC79E6KatRfXbmdWVWGncsew`, handle `@BacsiTranVanPhucOfficial`).
- Every health-content surface (repo README, per-video files, GPT instructions) must carry a disclaimer stating the content does not replace a medical consultation (see `disclaimer.md`).
- Total cost is $0 beyond the existing Claude Pro subscription: no paid LLM API, no API credits, no paid Gemini tier. The Gemini key must stay on the Free tier (project has no billing). Subscription login is local-only, never in CI; secrets are never printed or pasted.
- A video's state is derived from files on disk (pending → transcribed → summarized → published); no separate state store.
- Local summarization is resumable and safe to interrupt: atomic writes, skip finished videos, stop cleanly on a real usage limit.
- A summary is published only after CI validation by `validate_summaries.py` against `summary-contract.md` (header, disclaimer, timestamps and `?t=` links, question lines, glossary, vocabulary tags); unsummarized videos stay queued.
- Automation must run on free infrastructure (GitHub Actions scheduled workflow), timed around the doctor's weekly Saturday upload.

## Done when

1. A scheduled GitHub Actions run detects and processes any video published since the last run, verified weekly after the doctor's usual Saturday upload (R1).
2. Every processed video has a transcript, a structured summary, and metadata committed under `videos/<slug>/` (R2, R3).
3. A visitor can browse by topic or by date from the README and reach any video's transcript and summary in two clicks or fewer (R4).
4. `knowledge-gpt/` regenerates on every pipeline run and never exceeds 20 files or OpenAI's per-file Knowledge size ceiling (R5).
5. Documented, repeatable steps exist for re-uploading `knowledge-gpt/` into the Custom GPT Builder, and the GPT answers a question in a non-Vietnamese language grounded in the doctor's content with the disclaimer shown (R6).

## Boundaries

The automated pipeline (detection, transcript fetch, summarization, repo organization, consolidation) and the one-time, documented manual hand-off into the Custom GPT. Not the GPT itself as a hosted service (OpenAI's, operated manually by the user outside this repo), not fact-checking or translation quality (spec's Non-goals), not raw video/audio hosting. Tracer path: one real past video detected, fetched, summarized, committed, and consolidated end to end.

- Touch point: coding agents (Claude Code, Codex) reading the repo via plain `git clone` — R7, satisfied automatically by the repo structure the epic delivers; no dedicated story or tooling.
- Non-goal: Applying any correction or regenerating summaries.
- Non-goal: Producing a new pass/flag/fail verdict or refreshing `review.md`.
- Non-goal: Medical validation of the doctor's statements.
- Non-goal: Auditing other videos or changing the review tool (`scripts/review_summaries.py`, `fidelity.py`).
- Non-goal: Unblocking or publishing either video.
- Non-goal: No GPT Action or hosted search API for live, upload-free synchronization (Option B rejected) — a short manual upload step after each pipeline run is accepted.
- Non-goal: No paid LLM services, no hosted worker, and no digest/email channel beyond the repo itself.
- Non-goal: No fact-checking, correction, or medical validation of the doctor's claims — the repo mirrors his stated content as-is, clearly attributed.
- Non-goal: No professional or certified translation of the Vietnamese content — reliance on the GPT's native translation at answer time.
- Non-goal: No video or audio hosting/redistribution in the repo.
- Non-goal: Claude Code / Codex integration (R7) ships as a side effect of the repo's structure, not as a dedicated feature with its own tooling, UI, or support surface.

## References

- constraint — same spec, section Constraints (20-file GPT cap, no Knowledge-upload API, text-only, free CI, public repo naming, disclaimer everywhere)
- architecture — same spec folder, pipeline-architecture.md (Option C flow)
- structure — same spec folder, repo-structure.md (target repo layout, naming convention, consolidation rule)
- disclaimer — same spec folder, disclaimer.md (canonical text)
- companion — audit-record-format.md
- companion — repo-structure.md
- companion — pipeline-architecture.md
- companion — disclaimer.md
- companion — summary-contract.md

## Notes

- Decision: one epic covers R1 through R6 — single owner, single pipeline, no boundary justifies a split (user's request, this session).
- Assumption: Output location `_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-summary-source-audit/audit/<video_id>/` since no location was given.
- Assumption: Claim ids `c001…` regenerate from current `fidelity.extract_claims`; counts may change if the summary or extractor changes, in which case the audit restarts.
- Open question: Confirm `claude-opus-5-5` is accepted by the subagent runtime before launch.
- Assumption: GitHub Actions' free scheduled-workflow tier is acceptable and sufficient hosting for the weekly automation (R1, R2, R3, R5).
- Assumption: "LLM can translate easily" is read as: no dedicated translation pipeline is needed: Vietnamese stays the canonical source language and the GPT translates at query time (applies to R6 and the Constraints).
- Assumption: Free-tier Gemini limits (rate, daily tokens) may not fit a 3-4h transcript in one request; the story must chunk and measure. Unverified.
- Assumption: Free-tier Gemini may use content to improve Google products; acceptable because the repo content is public.
- Assumption: After the backlog is caught up, volume is one video per week, so the CI Gemini path is expected to need no manual step beyond the GPT upload.
- Assumption: GitHub account `khoaowen` (gh CLI authenticated) owns the public repo `tranvanphuc-knowledge-base`.

## Transcript fidelity continuation — 2026-10-20

[Fresh-context handoff](continuation-transcript-fidelity.md) tracks the caption-fidelity research, pending human listening bundle, c068/c163 correction proposals, and the raw-caption implementation branch (in-review, not merged). It also records which earlier five-disagreement / eleven-omission findings remain applicable. Publication remains blocked; no new fidelity decisions or content corrections are approved by this handoff.

## Tracking reconciliation — 2026-10-26

- Decision: The explicitly authorized q7uDJG8YQ5c correction (commit `cce328c0e75693fae8c82fd6fca5112594477929`, local only) is recorded; see the epic-summary-source-audit Notes. Fresh review 222/222 pass with complete coverage, validator exit 0, `publishable` true, 205 tests pass. Nothing pushed, merged or published. The R1–R6 text, the audit spec and all audit evidence are unchanged; earlier "blocked" statements are historical. V-Qfwjo28Zg stays blocked and unapproved.
- Open: human acceptance is still needed for ticket 2.1 (audit of q7uDJG8YQ5c) and ticket 1.11 (criterion 13: the owner's live `workflow_dispatch` run on the real channel and committed file list). Both stay in review.
- Decision: The next implementation ticket is 2.2 (audit of V-Qfwjo28Zg, read-only, ready-for-dev). Ticket 1.4 is ready per `tickets.py next` but is gated in substance on 1.11's acceptance.
- Decision: 2026-10-26, owner accepted ticket 2.1 as done. Ticket 1.11 acceptance remains open.
