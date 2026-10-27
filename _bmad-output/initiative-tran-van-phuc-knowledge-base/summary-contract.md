# Summary contract (R3 retrieval layer)

`videos/*/summary.md` is what the Custom GPT retrieves from. Each chunk must answer a query on its own. Written by `summarize.py` (CI, Gemini) or `./review-batch` (local, `claude -p`); gated by `scripts/validate_summaries.py`.

## Required structure

1. **Self-contained header**: title, video ID, publish date, URL, topic tags (from `topics/vocabulary.md`). Retrieval may surface any section alone, so the header must identify the video.
2. **Disclaimer banner** directly under the header (text in `disclaimer.md`).
3. **Topic sections**: one per topic discussed. Heading carries a start timestamp (`[HH:MM:SS]`) and a link `https://www.youtube.com/watch?v=<id>&t=<seconds>s` (the `?t=` deep link).
4. **Question-shaped lines** in each section: the questions a viewer would ask, each answered beneath, phrased as users would query.
5. **Specific claims**: named conditions, substances, doses, numbers and durations exactly as stated; no generic gloss ("discusses nutrition").
6. **VI/EN/FR glossary** at the end: key terms in Vietnamese, English, French, so queries in any language match.

## Fidelity rules

- Every claim traces to the transcript at the cited timestamp.
- Keep the doctor's hedges (may, in some cases, depends); do not harden them into absolutes.
- Add no medical content, correction, or advice absent from the transcript.

## CI validation (`validate_summaries.py`)

Fails a summary that lacks: header fields, disclaimer banner, at least one timestamped topic section with a valid `?t=` link, question-shaped lines, glossary with all three languages, or tags outside `topics/vocabulary.md`. Invalid summaries are dropped from consolidation and the video stays queued.
