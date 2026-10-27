# Pipeline architecture (Option C)

```mermaid
flowchart TD
    A[GitHub Actions cron<br/>weekly, after Saturday upload] --> B[detect_new_videos.py<br/>R1: list channel videos,<br/>diff against videos/ already in repo]
    B -->|new video IDs| C[fetch_transcript.py<br/>R2: pull YouTube transcript + metadata]
    C --> D[summarize.py<br/>R3: LLM structured summary,<br/>topic tags, timestamps]
    D --> E[Commit to repo:<br/>videos/&lt;slug&gt;/transcript.md, summary.md, metadata.json]
    E --> F[consolidate.py<br/>R5: rebuild knowledge-gpt/*.md,<br/>&lt;=20 files, size-capped]
    F --> G[Commit consolidated files]
    G --> H((Manual step))
    H --> I[Human re-uploads changed<br/>knowledge-gpt/*.md files<br/>into Custom GPT Builder]
    I --> J[ChatGPT Custom GPT<br/>R6: answers grounded<br/>in latest content]

    E -.-> K[Repo is a normal git repo:<br/>R7, Claude Code / Codex<br/>clone and read directly]
```

- Steps A-G run unattended on GitHub Actions; a failed step surfaces as a failed workflow run (notification via GitHub's default email/Actions UI — no extra tooling built for this).
- Step H-I is the only manual action in the whole loop, forced by the Constraints (no Knowledge-upload API).
- R7 (agent access) needs no separate pipeline step: it is satisfied by the repo's existence and structure alone.

## Amendment 2026-10-11: $0 hybrid (supersedes step D as CI-only)

- Step D (`summarize`) has two runners writing the same `summary.md`: CI with Gemini free tier for the weekly video; local `./review-batch` with `claude -p` for backlog and re-summaries.
- CI never uses the subscription login. Local runs commit and push; CI validates (step E gate) before consolidation (F).
- Queue order is newest first. Re-running either runner skips videos that already have a valid summary.
