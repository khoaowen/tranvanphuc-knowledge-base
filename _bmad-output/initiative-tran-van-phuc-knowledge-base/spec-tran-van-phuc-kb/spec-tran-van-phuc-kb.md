---
id: SPEC-tran-van-phuc-kb
companions: [repo-structure.md, pipeline-architecture.md, disclaimer.md]
sources: []
---

> **Canonical contract.** This SPEC and the files in `companions:` are the complete, preservation-validated contract for what to build, test, and validate. Source documents listed in frontmatter are for traceability — consult them only if you need narrative rationale or prose color this contract intentionally omits.

# Tran Van Phuc Knowledge Base

## Why

Dr. Tran Van Phuc (channel "Bác sĩ Trần Văn Phúc Official", 431K subscribers) publishes long-form health livestreams nearly every Saturday. His audience cannot search, re-watch, or quiz this material. The user wants a durable, growing, public knowledge base distilled from these videos, modeled on `mlabonne/llm-course`: a versioned GitHub repo as the source of truth, feeding a ChatGPT Custom GPT people can chat with to learn about health topics the doctor has covered — kept current automatically as new videos appear, with a one-click (manual) bridge into the GPT's knowledge.

## Capabilities

- **CAP-1**
  - **intent:** The system detects new videos published on the channel without manual checking.
  - **success:** A scheduled run finds any video published since the last run and queues it for processing, verified weekly after the doctor's usual Saturday upload.
- **CAP-2**
  - **intent:** For each queued video, the system fetches the Vietnamese transcript and core metadata (title, publish date, video ID, URL, duration).
  - **success:** A transcript file and a metadata record exist in the repo for every processed video, sourced directly from YouTube captions.
- **CAP-3**
  - **intent:** For each video, the system generates a structured summary (key points, medical topics covered, notable claims, timestamps) from the raw transcript via an LLM at no cost: Gemini free tier in CI for the weekly video, local `claude -p` (Pro subscription) for backlog and re-summaries.
  - **success:** A summary file with topic tags exists alongside every transcript; given 3-4h source videos, the summary is materially shorter and topic-navigable compared to the raw transcript. Both the raw transcript and the structured summary are kept per video — confirmed by the user.
- **CAP-4**
  - **intent:** Transcripts, summaries, and metadata are organized into a public, versioned GitHub repository structured and browsable like `mlabonne/llm-course` (indexed README, per-video entries, topic index).
  - **success:** A visitor can browse by topic or by date from the README and reach any video's transcript and summary in two clicks or fewer.
- **CAP-5**
  - **intent:** The repo content is automatically consolidated into a small set of markdown files sized and counted to fit a ChatGPT Custom GPT's Knowledge upload limits.
  - **success:** The consolidation step regenerates on every pipeline run and never exceeds 20 output files or OpenAI's per-file knowledge size ceiling.
- **CAP-6**
  - **intent:** A ChatGPT Custom GPT, configured once with these consolidated files as Knowledge, answers health questions grounded in Dr. Phuc's content, in whatever language the user asks, and always shows a medical disclaimer.
  - **success:** Asked a question in French about a topic the doctor has covered, the GPT answers from his content (translating from the Vietnamese source as needed) and includes the disclaimer; updating to a newer set of consolidated files requires only re-uploading them in the GPT Builder.
- **CAP-7**
  - **intent:** Coding agents (e.g. Claude Code, Codex) can use the same GitHub repo as a local knowledge base by cloning or reading it directly.
  - **success:** The repo requires no extra tooling beyond a normal git clone and plain-markdown reading for an agent to retrieve and cite its content.

## Constraints

- The Custom GPT Knowledge tab accepts at most 20 files: the consolidation step (CAP-5) must always fit within this ceiling regardless of how many videos accumulate.
- OpenAI provides no API to push files into a Custom GPT's Knowledge tab: the final hand-off from consolidated files to the live GPT is necessarily a manual upload; the pipeline automates everything up to that point (detection, transcript, summary, repo commit, consolidation).
- No raw video or audio is stored in the repo — text only (transcripts, summaries, metadata), to control repo size and respect YouTube's terms of service.
- Source transcripts stay in Vietnamese; no dedicated translation step is built — the GPT translates on demand at query time. Repo documentation (README, code, commit messages, this spec's own companions) is in English; the disclaimer's canonical text is English, localized at the GPT-response level only.
- The repo is public and must be named/branded to disambiguate from other people named Tran Van Phuc, referencing the channel "Bác sĩ Trần Văn Phúc Official" (channel ID `UC79E6KatRfXbmdWVWGncsew`, handle `@BacsiTranVanPhucOfficial`).
- Every health-content surface (repo README, per-video files, GPT instructions) must carry a disclaimer stating the content does not replace a medical consultation (see `disclaimer.md`).
- Total cost is $0 beyond the existing Claude Pro subscription: no paid LLM API, no API credits, no paid Gemini tier. The Gemini key must stay on the Free tier (project has no billing). Subscription login is local-only, never in CI; secrets are never printed or pasted.
- A video's state is derived from files on disk (pending → transcribed → summarized → published); no separate state store.
- Local summarization is resumable and safe to interrupt: atomic writes, skip finished videos, stop cleanly on a real usage limit.
- A summary is published only after CI validation (schema, disclaimer, timestamps, length); unsummarized videos stay queued.
- Automation must run on free infrastructure (GitHub Actions scheduled workflow), timed around the doctor's weekly Saturday upload.

## Non-goals

- No GPT Action or hosted search API for live, upload-free synchronization (Option B rejected) — a short manual upload step after each pipeline run is accepted.
- No paid LLM services, no hosted worker, and no digest/email channel beyond the repo itself.
- No fact-checking, correction, or medical validation of the doctor's claims — the repo mirrors his stated content as-is, clearly attributed.
- No professional or certified translation of the Vietnamese content — reliance on the GPT's native translation at answer time.
- No video or audio hosting/redistribution in the repo.
- Claude Code / Codex integration (CAP-7) ships as a side effect of the repo's structure, not as a dedicated feature with its own tooling, UI, or support surface.

## Success signal

Within 24-48h of each Saturday upload, the new video's transcript and structured summary land in the public GitHub repo and the consolidated knowledge files regenerate automatically. After a brief manual re-upload in the GPT Builder, a user chatting with the Custom GPT in French can ask about that week's video and get an answer grounded in Dr. Phuc's own words, with the medical disclaimer shown.

## Assumptions

- GitHub Actions' free scheduled-workflow tier is acceptable and sufficient hosting for the weekly automation (CAP-1, CAP-2, CAP-3, CAP-5).
- "LLM can translate easily" is read as: no dedicated translation pipeline is needed: Vietnamese stays the canonical source language and the GPT translates at query time (applies to CAP-6 and the Constraints).
- Free-tier Gemini limits (rate, daily tokens) may not fit a 3-4h transcript in one request; the story must chunk and measure. Unverified.
- Free-tier Gemini may use content to improve Google products; acceptable because the repo content is public.
- After the backlog is caught up, volume is one video per week, so the CI Gemini path is expected to need no manual step beyond the GPT upload.
- GitHub account `khoaowen` (gh CLI authenticated) owns the public repo `tranvanphuc-knowledge-base`.
