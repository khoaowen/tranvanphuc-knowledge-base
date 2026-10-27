# Timing alignment, c068 and c163 (2026-10-20)

Method: word-sequence alignment between the raw caption json3 word times (tStartMs+tOffsetMs) and the blind whisper large-v3-turbo token times for the same audio clip. Whisper times are machine estimates, typically within ±0.3 s.

| Layer | c068 | c163 | Regression clips R1/R2 |
|---|---|---|---|
| Raw caption word time minus audio (median; p10..p90) | +0.13 s (0.0..+0.6) | +0.20 s (-0.1..+0.6) | +0.44 / +0.18 s |
| transcript.md line label vs when a word is actually spoken (median; max) | +1.4 s (max 3.9) | +1.2 s (max 4.2) | — |
| Example | "[01:45:37] … bốn bào tử": "tử" is spoken at ≈01:45:39.9 (+2.9 s) | "[03:02:55] … giá thành đắt": "đắt" is spoken at ≈03:02:58.0 (+3.0 s) | |
| Summary link for the claim | section "[01:42:36]" (&t=6156s): about 2 min 54 s before the spoken passage at 01:45:30 | section "[03:01:21]" (&t=10881s): about 1 min 30 s before 03:02:51 | |
| Audit evidence timestamp | 01:45:17 (the first line of a multi-line quote): 13 s before "gián phân" | 03:02:47 | |

Causes:
1. `fetch_transcript.py` labels each line with its event start, truncated to the whole second. A caption line holds about 6–9 words spoken over 2–4 s, so later words in the line are spoken after the label.
2. The summary links to the start of the topic section, not to the claim.
3. Audit quotes that span several lines carry the first line's timestamp.

Player check: screenshots at 6331.4 s and 10973.4 s show the caption text that matches the audio at those moments (see player-captions/screens.json).
