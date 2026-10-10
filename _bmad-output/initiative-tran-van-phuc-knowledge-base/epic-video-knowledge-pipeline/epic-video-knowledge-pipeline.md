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
- CAP-3: Generate a structured summary (key points, topic tags from a controlled vocabulary, timestamps) per video via an LLM; keep both transcript and summary. (spec, Capabilities)
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

- parent — ../initiative-tran-van-phuc-knowledge-base.md
- spec — ../spec-tran-van-phuc-kb/spec-tran-van-phuc-kb.md, section Capabilities
- architecture — ../spec-tran-van-phuc-kb/pipeline-architecture.md
- structure — ../spec-tran-van-phuc-kb/repo-structure.md
- disclaimer — ../spec-tran-van-phuc-kb/disclaimer.md

## Notes

- Decision: one epic for CAP-1 through CAP-6, no split by capability — single owner, one sequential lane, no boundary justifies more than one epic (user's request, this session).
- Decision: CAP-7 gets no story; it is a side effect of CAP-4's plain-markdown structure (spec's Non-goals; user's request, this session).
- Open question: YouTube transcript/metadata source for CAP-1/CAP-2 — YouTube Data API (needs an API key secret) vs. `yt-dlp`/`youtube-transcript`-style scraping (no key, more fragile). The opening story (detection) decides and records it.
- Unknown: the LLM provider/credentials for CAP-3 summarization (which model, which API key secret) — the summarize.py story decides and records it.
- Unknown: the controlled topic-tag vocabulary starts empty; the summarize.py story seeds an initial list from the first processed videos rather than inventing one upfront.
