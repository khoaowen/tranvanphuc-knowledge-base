---
tracker_id: ""
key: ""
type: epic
title: "Automated video-to-knowledge pipeline"
parent: initiative-tran-van-phuc-knowledge-base
covers: [CAP-1, CAP-2, CAP-3, CAP-4, CAP-5, CAP-6]
after: []
assignee: ""
risk: medium
---

# Automated video-to-knowledge pipeline

## Description

The channel's weekly uploads become, without manual checking, a browsable public repo of transcripts and structured summaries, consolidated into a small set of files a human can paste into a ChatGPT Custom GPT's Knowledge tab. This is the whole initiative's one epic: single owner, one sequential pipeline (detect → fetch → summarize → organize/consolidate → manual GPT upload), per the spec's Option C architecture.

## Outcome

Within 24-48h of each Saturday upload, the new video is processed end to end and committed to the public repo, `knowledge-gpt/` regenerates automatically, and a brief manual re-upload in the GPT Builder is all that stands between a fresh video and a Custom GPT answer grounded in it, disclaimer shown — the spec's Success signal.

## Requirements

- CAP-1: Detect new videos on the channel since the last run, on a weekly schedule after the usual Saturday upload. (spec, Capabilities)
- CAP-2: Fetch the Vietnamese transcript and core metadata (title, publish date, video ID, URL, duration) for each queued video. (spec, Capabilities)
- CAP-3: Generate a structured summary (key points, topic tags from a controlled vocabulary, timestamps) per video via an LLM at $0 (Gemini free tier in CI for the weekly video, local `claude -p` for backlog); keep both transcript and summary. (spec, Capabilities)
- CAP-4: Organize transcripts, summaries, and metadata into the public repo per `repo-structure.md` — README index by date/topic, `videos/<slug>/`, `topics/*.md`, reachable in two clicks or fewer. (spec, Capabilities)
- CAP-5: Consolidate repo content into `knowledge-gpt/*.md`, regenerated every run, never exceeding 20 files or OpenAI's per-file Knowledge size ceiling, repacked/rebalanced as the corpus grows. (spec, Capabilities)
- CAP-6: Document the one-time-per-run manual hand-off — uploading `knowledge-gpt/*.md` into the Custom GPT Builder, with instructions/system-prompt text that always shows the disclaimer and translates on demand. (spec, Capabilities)

## Done when

1. A GitHub Actions scheduled workflow, run manually (`workflow_dispatch`) against the real channel, correctly identifies which known videos are already processed and would queue a genuinely new one.
2. For at least one real past video, `videos/<slug>/transcript.md`, `summary.md`, and `metadata.json` all exist, are correctly structured, and the summary carries topic tags and timestamps and is materially shorter than the transcript.
3. The README and `topics/` index reach that video's transcript and summary in two clicks or fewer, and every health-content file (README, each `summary.md`) carries the disclaimer per `disclaimer.md`.
4. `consolidate.py` run against the seeded videos produces `knowledge-gpt/*.md` that never exceeds 20 files and stays under OpenAI's per-file size ceiling.
5. A documented procedure exists for the manual GPT Builder upload and system-prompt text, and following it once produces a GPT that answers a question about the seeded content in a non-Vietnamese language, grounded, with the disclaimer shown.

## Boundaries

The pipeline code (`scripts/`, `.github/workflows/weekly-sync.yml`), the repo content structure it writes to, and the documentation for the one manual step. Not the GPT as a hosted service, not translation quality, not fact-checking, not video/audio hosting — see the spec's Non-goals. CAP-7 (agents reading the repo via `git clone`) needs no entry here: it falls out of the repo being plain, public markdown once CAP-4 is delivered.

## References

- parent — ../../initiative-tran-van-phuc-knowledge-base.md
- spec — ../../spec-tran-van-phuc-kb/spec-tran-van-phuc-kb.md, section Capabilities
- architecture — ../../spec-tran-van-phuc-kb/pipeline-architecture.md
- structure — ../../spec-tran-van-phuc-kb/repo-structure.md
- disclaimer — ../../spec-tran-van-phuc-kb/disclaimer.md

## Notes

- Decision: one epic for CAP-1 through CAP-6, no split by capability — single owner, one sequential lane, no boundary justifies more than one epic (user's request, this session).
- Decision: CAP-7 gets no story; it is a side effect of CAP-4's plain-markdown structure (spec's Non-goals; user's request, this session).
- Open question: YouTube transcript/metadata source for CAP-1/CAP-2 — YouTube Data API (needs an API key secret) vs. `yt-dlp`/`youtube-transcript`-style scraping (no key, more fragile). The opening story (detection) decides and records it.
- Decision (2026-10-11): CAP-3 runs at $0. CI uses Gemini free tier (secret `GEMINI_API_KEY`, confirmed free tier); local `./review-batch` uses `claude -p`. No paid API, no subscription login in CI. Free-tier limits on 3-4h transcripts are untested; chunking required.
- Unknown: the controlled topic-tag vocabulary starts empty; entry 4 seeds it from evidence in the validated summaries, with human approval.
- Dropped: entry 3 "Generate structured summary" (2026-10-11) — superseded by the $0 hybrid amendment (paid auditor, WIF, dollar caps removed). Its plan status was `superseded`, not a valid status, so it is set to `dropped`; the file is otherwise untouched and is not to be implemented from.
- Decision (2026-10-11): re-sliced after stories 1-2 (done). Ids are never reused, so the new stories take 8-11 (Gemini CI summarizer, local review-batch, validator and publish gate, weekly workflow); 4-7 keep their ids and are re-scoped. Build order at that re-slice was the table order: 1, 2, 8, 9, 10, 11, 4, 5, 6, 7.
- Decision (2026-10-11): CI Gemini summarizes only the newly detected video; backlog stays `transcribed` for local `./review-batch`. One queue, newest first, no special backlog mode.
- Assumption: local summarization needs no new CAP; CAP-3 and the spec Constraints already cover `claude -p`, resumability and the validation gate.
- Source conflict: spec CAP-3 — lists key points, topics, claims, timestamps vs. memlog 2026-10-11 decision that the summary is the GPT retrieval layer (self-contained header, ?t= links, question-shaped lines, VI/EN/FR glossary, hedges kept). The contract lives only in `.memlog.md`; offer to pass it to `bmad-spec`.
- Decision (2026-10-24): resolve the historical CAP-3 source conflict for the pipeline integration: the richer retrieval/fidelity contract is now recorded in `../../spec-tran-van-phuc-kb/summary-contract.md` and implemented by the shipped summarizer, validator, and hash-bound local review gate. Entry 11 consumes that contract unchanged; the shorter CAP-3 wording does not remove its header, deep links, question-shaped lines, glossary, or fidelity requirements. No schema redesign is part of 11.
- Decision (2026-10-11): tag check is option A. Tags are free-form until `topics/vocabulary.md` exists; 8 and 9 load it into the prompt when present; 10 takes the vocabulary path as a parameter and enforces only when the file exists; 4 seeds and gets it approved, then re-validates all summaries and re-queues failures.
- Decision (2026-10-11): entry 9 owns the queue/state helper; 10 reuses it, so 10 is after 8 and 9.
- Decision (2026-10-11): CI fetches and Gemini-summarizes only the single newest video not yet in videos/; backlog is queued as pending and fetched locally by entry 9 (no CI backlog fetch, no extra Gemini quota).
- Decision (2026-10-11): entry 4 does not wait on 9; option A seeds the vocabulary from the validated summaries available.
- Decision (2026-10-11): entry 8 does not prove the Free tier in CI; builder re-confirms in AI Studio once. CAP-3 summary contract to go through bmad-spec.
- Unknown: whether detect/fetch (stories 1-2, done) already queue the whole channel backlog; entry 11 owns any change needed and does not reopen 1 or 2.
- Decision (2026-10-11): added entry 12, a Claude fidelity review that blocks publishing. It restores the auditor from the dropped entry 3, which the $0 amendment removed with the paid parts and no ticket re-homed (user's request, this session). Build order: 1, 2, 8, 9, 12, 10, 11, 4, 5, 6, 7.
- Decision (2026-10-11): the fidelity review (entry 12) stays local, Claude-only and blocking. No Gemini second pass and no quote-per-claim check in CI (user's request, this session). Consequence accepted: the weekly CI Gemini video is committed but unpublished until ./review-summaries is run locally and review.md is pushed. Entry 11 must keep it unpublished until then.
- Decision (2026-10-11): restore four dropped entry-3 requirements. Entry 12 checks speaker attribution and requires each finding to cite a verbatim Vietnamese quote plus timestamp range. Entry 10's validation/consolidation gate is read-only for transcript.md, proves its bytes unchanged, preserves the prior summary on failed regeneration, and excludes stale summaries from publication/consolidation. User agreed after requirements audit.
- Decision (2026-10-11): Entry 12 reviews long transcripts in overlapping timestamped chunks, checks every summary claim against raw transcript evidence, and performs a full-summary coverage audit across the transcript. Pass requires all claims supported, attributed, timestamped, and qualifications preserved; flag is for localized unresolved/minor concerns; fail is for clear unsupported/materially misleading defects. Only pass publishes; both flag and fail block. The review must be bound to the exact summary reviewed; summary changes invalidate an earlier pass. Verify with clean, flag, and fail fixtures and boundary-spanning claims on both real videos.
- Decision (2026-10-11): User-facing GPT answers that use video content must include supporting source evidence and a deep link to the relevant video sequence, so users can verify the answer and explore the original discussion. This is answer-time citation behavior, distinct from Entry 12's summary-fidelity review; it is not added to Entry 12 or implemented in this ticket. Summary-contract and Custom GPT setup/ticket updates remain follow-up scope.

### Raw-caption provenance follow-up — integrated (2026-10-21)

Feature head `e5eff1d` (baseline `47c72ce`) is merged into `khoaowen/Epic2-publish-videos` at `471834d`. The [canonical plan](story-raw-caption-provenance-plan.md) records the final independent review with no findings; [human walkthrough Blocks 1–5](../../../walkthrough-e5eff1d/walkthrough-e5eff1d.md) are accepted. Fix `51443d9` removes a pre-existing filesystem-order assumption in a test and restores BMad artifact paths. A fresh isolated run of the exact integrated commit passed all 147 tests; `git diff --check` passed, and `videos/` is unchanged. The user approved this documentation checkpoint and pushing Epic 2; verify remote state to confirm completion. This supersedes the earlier `9124c18`, 137-test, outstanding-review and no-push state. Backfill, correction approvals, publication, and a merge to `main` remain outside this authorization. See the [continuation handoff](../../continuation-transcript-fidelity.md) for remaining work; the whole epic is not declared complete.
