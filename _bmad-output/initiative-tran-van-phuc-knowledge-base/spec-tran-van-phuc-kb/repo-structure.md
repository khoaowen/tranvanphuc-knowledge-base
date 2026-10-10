# Repo structure

Mirrors `mlabonne/llm-course`'s navigability: one README index, content grouped for browsing, plus a consolidated layer the GPT pipeline regenerates.

```
tranvanphuc-knowledge-base/
  README.md                        # index: by date, by topic, links to every video entry; disclaimer banner
  DISCLAIMER.md                    # full medical disclaimer text (see disclaimer.md companion)
  videos/
    2026-01-10-so-132-vac-xin-ung-thu/
      metadata.json                # {video_id, title, url, published_at, duration, topics[]}
      transcript.md                # raw Vietnamese transcript, timestamped
      summary.md                   # structured summary: key points, topic tags, timestamps
    2026-01-03-so-131-.../
      ...
  topics/
    ung-thu.md                     # per-topic index: links into videos/ entries tagged with this topic
    vitamin.md
    dinh-duong.md
    ...
  knowledge-gpt/                   # CAP-5 output — regenerated every pipeline run, never hand-edited
    01-overview.md
    02-videos-2026-q1.md
    03-topics-ung-thu-vitamin.md
    ...                            # <=20 files total, each under OpenAI's per-file size ceiling
  scripts/
    detect_new_videos.py           # CAP-1
    fetch_transcript.py            # CAP-2 (wraps the youtube-transcript skill or yt-dlp)
    summarize.py                   # CAP-3
    consolidate.py                 # CAP-5
  .github/workflows/
    weekly-sync.yml                # CAP-1-5 scheduled run (cron, Saturday+buffer)
```

## Naming convention

- Video folder: `<published-date>-<video-number-from-title>-<slugified-title>/`. The doctor's own titles are numbered ("Số 132: ..."), so the number is preserved for continuity with his own indexing.
- Topic files are hand-curated tag targets; `summarize.py` assigns tags from a controlled topic vocabulary grown incrementally (avoid unbounded tag sprawl).

## `knowledge-gpt/` consolidation rule

- Never exceeds 20 files (CAP-5 constraint).
- Each file batches several videos/topics, not one video per file, to stay within OpenAI's 20-file ceiling as the corpus grows; `consolidate.py` repacks and rebalances files as the corpus grows rather than appending indefinitely to one file.
- Files are the only ones a human uploads by hand into the Custom GPT's Knowledge tab after each pipeline run.
