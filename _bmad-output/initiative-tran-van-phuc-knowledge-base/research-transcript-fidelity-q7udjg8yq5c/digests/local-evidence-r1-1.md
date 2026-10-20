# Digest: local evidence, round 1 (inline, no subagents)

accessed: 2026-10-19 (UTC 20:32 onward). All evidence was gathered in this run from local files and yt-dlp caption retrieval. No web search was used.

| # | claim | source | confidence |
|---|---|---|---|
| 1 | fetch_transcript.py requests `--write-auto-sub` vi-orig,vi json3 into a TemporaryDirectory. It keeps only "[hh:mm:ss] text" from events that have dDurationMs, dropping per-word `acAsrConf`, `isSpeakerChange` and `tOffsetMs`. metadata.json has no caption provenance. | scripts/fetch_transcript.py L80-160; videos/…/metadata.json | high |
| 2 | Only automatic captions exist (vi-orig and vi, plus about 150 auto-translations). "Available subtitles" lists only `live_chat`, so there is no creator track. | evidence/raw-captions/list-subs.txt L4, L153-154, L163-165 | high |
| 3 | The vi-orig and vi json3 files are byte-identical (sha256 64d93b68…), so vi is not a separate translation. | evidence/raw-captions/PROVENANCE.txt | high |
| 4 | Re-parsing the 2026-10-19 json3 with the repo's own `build_transcript_lines` reproduces the saved transcript.md exactly: 5330/5330 lines, diff 0. There is no extraction loss and no caption-version drift between the 2026-10-10 fetch (commit b8a1ce4) and today. | this run, ctx_execute; transcript.md git log | high |
| 5 | `acAsrConf` = 0 on all 43,103 word segments, so it carries no confidence signal. `isSpeakerChange=1` occurs 814 times and maps 1:1 to the 814 `>>` markers. | evidence/raw-captions/word-level-c068-c163.tsv; this run | high |
| 6 | c068 raw words: " dán"@01:45:31.000, " phân"@01:45:31.239, "giảm phân", "bốn bào tử". "nguyên phân" appears 0 times in the whole caption file. "dán phân" appears twice (01:33:57 and 01:45:30). | word-level tsv; transcript.md L2295, L2564 | high (what the caption says), not about speech |
| 7 | c163 caption turns: `>>` at 03:02:16 ("Nó khá đắt rồi…Tôi thấy rất nhiều người bỏ được…trí nhớ bắt đầu cải thiện"). Next `>>` at 03:02:47 ("Alzimer run rẩy tay chân Parkison. Alzimer…cải thiện được rất nhiều…từ 0,6 trở lên nhưng mà giá thành đắt rồi…người tôi hướng dẫn…kinh tế"). Next `>>` at 03:03:12 ("Vâng."). No marker separates the improvement or price statements from the Alzheimer/Parkinson mention. | transcript.md 03:01:58-03:03:43; word-level tsv | high (caption structure) |
| 8 | Regression sample captions contain visible errors: ratio colons are lost ("11 đến 51", "41", "21 hay là 31"); "omega6/ên omega3"; "hen suuyễn"; "Khách lành" for the host name "Khánh lành"; "kỷ lực"; "hôm nấy"; "Từ 0 phẩ chia được con số"; split-word turns ">> D", ">> DA". | evidence/raw-captions/regression-sample-raw.txt | high (that the caption text has these strings) |
| 9 | The audio could not be obtained. The ranged ffmpeg fetch returned 403. Full-stream downloads returned 403 or "only images" across the default, web_safari, tv, ios and mweb clients. yt-dlp warns that a GVS PO Token is required and that the 2026.03.17 build is more than 90 days old. | evidence/audio/dl*.log | high |
| 10 | whisper.cpp large-v3-turbo is present locally, but the host is an Intel i9 (x86_64) with no Apple-Silicon Metal path. whisper-cli diarization is stereo-only (`-di`) or needs a tdrz model (`-tdrz`), so it does not identify speakers in mono audio. | evidence/asr/asr-tooling.txt, whisper-cli-help.txt | high |
| 11 | The spec CAP-2 requires transcripts "sourced directly from YouTube captions", and CAP-3 keeps both the raw transcript and the summary. | spec-tran-van-phuc-kb.md L20-26 | high |
| 12 | Claim ID `c068` names two different claims: one in final_records.json (the 4:1 ratio claim) and one in supplement-records.json (the Lipton/division claim). | audit/q7uDJG8YQ5c/*.json | high |

Leads not chased: the YouTube web UI transcript panel. It was not opened because there is no interactive browser session in this run. Track equality (finding 3) and the zero diff (finding 4) make a different UI track unlikely, but this is not verified.
Searched for and not found: any local copy of the audio for q7uDJG8YQ5c; a creator-provided caption track.
