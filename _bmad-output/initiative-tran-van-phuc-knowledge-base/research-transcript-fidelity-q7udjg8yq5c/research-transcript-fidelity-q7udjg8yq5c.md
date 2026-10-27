---
title: 'technical research: transcript fidelity for q7uDJG8YQ5c'
type: 'technical'
topic: 'Transcript fidelity: YouTube auto-captions vs independent ASR vs targeted human verification'
decision: 'Retain YouTube auto-captions, introduce independent audio transcription, or use targeted human verification'
source: 'native run, local evidence, yt-dlp, browser player capture, local whisper.cpp ASR'
status: complete for machine evidence; human listening still pending
preset: 'quick (inline)'
validation: 'normal'
created: '2026-10-19'
updated: '2026-10-20'
---

# Transcript fidelity for q7uDJG8YQ5c

**Decision this research serves:** whether to keep YouTube automatic captions, add independent audio transcription, or add targeted human verification.

## Executive summary

- **The browser player and our transcript use the same captions.** In a real Chrome session with the user's profile, the player loaded one track, `vi` / `kind=asr` (auto-generated) [13]. Re-rendered with the repo parser, that response equals the saved `transcript.md` line for line (5330/5330). The rendered on-screen captions show the same strings: "trình dán phân" and "Alzimer nhớ nhớ quên quên" [14]. Upgrading yt-dlp (2026.08.19) also returned byte-identical captions [15].
- **Why the captions look correct while watching:** they are mostly **phonetically** right. In northern Vietnamese, *dán* and *gián* sound the same, so "dán phân" is heard as *gián phân*. "Alzimer" and "Parkison" read as the disease names. A viewer who sees the speaker on screen supplies the speaker identity that the caption text lacks.
- **c068:** the blind ASR hears **"gián phân"**, both here and in the 01:33:57 cross-reference, plus **"bốn bào tử"** [16]. The captions misspell the first word. The summary's "nguyên phân" is a **substitution** (a synonym that was not spoken), and "four" without "bào tử" drops the spoken noun.
- **c163:** pitch analysis shows one continuous male-range voice from 03:02:44 to 03:02:58, with no female-range segment. The host's female-range "Vâng" is visible at 03:02:16 [17]. The blind ASR merges the passage into one turn [16]. A video frame at 03:02:51 shows the doctor gesturing while the host listens [14]. The caption's `>>` at 03:02:47 is most likely a **false speaker change**. Identity remains a human call.
- **The independent ASR is useful but unsafe alone.** It fixed spellings and ratio formatting. But it hallucinated an entire 25 s regression clip ("Hãy subscribe cho kênh Ghiền Mì Gõ…"), dropped short interjections, and cannot label speakers [10][16].
- **Recommendation: hybrid.** Keep the captions as the immutable raw layer. Use ASR as a triage diff on flagged windows. Use a human listener only where the two sources disagree on a critical word, number or speaker.

## 1. Provenance and root cause

| Question | Finding | Evidence |
|---|---|---|
| Tracks available | Automatic only. No creator track exists; the manual list holds only `live_chat`. | [2] |
| Track downloaded | `vi-orig`, byte-identical to `vi` | [3] |
| Interface-selected track | `vi`, `kind=asr`, vss_id `a.vi`, labelled "Vietnamien (générés automatiquement)". It is the only track the player offers. | [13] |
| Player text vs saved transcript | Identical: 5330/5330 lines. The screenshots show the same strings. | [13][14] |
| Extraction loss | None | [4] |
| Caption-version drift | None: 2026-10-10 fetch = 2026-10-19 fetch = 2026-10-20 fetch (yt-dlp 2026.08.19) = player response | [4][15] |
| Fields discarded by the pipeline | The raw file; `isSpeakerChange`, reduced to a `>>` prefix; word offsets; provenance. `acAsrConf` is dropped but is 0 for every word. | [1][5] |

**Root cause:** the transcript is a lossless copy of YouTube's ASR. Some caption errors are spelling-level (homophones, loanwords, ratio formatting). Others are structural (spurious `>>` speaker changes). The summary-level errors in c068 came from the summarizer **normalizing** caption text into terminology that was not spoken.

## 2. Comparison table

"Direct listening" means a human ear. No human listening was done. ASR and pitch are machine evidence.

| Item | YouTube caption = saved transcript = player | Blind ASR (whisper large-v3-turbo) | Acoustic / visual | Current summary.md | Verdicts |
|---|---|---|---|---|---|
| c068, process 1 (01:45:30) | "dán phân" | "**gián phân**"; the 01:33:57 cross-reference also gives "gián phân" | — | "nguyên phân" | **Transcript vs recording:** the caption is phonetically consistent but misspelled; *gián phân* is likely (machine evidence only, 2 independent hearings). **Summary vs transcript:** mismatch; "nguyên phân" is unsupported normalization [6]. |
| c068, product 1 | "tạo nên hai tế bào" | "tạo lên hai tế bào" | — | "tạo ra hai tế bào" | Consistent (two cells). |
| c068, process 2 | "giảm phân" | "giảm phân" | — | "giảm phân" | Consistent. |
| c068, product 2 | "bốn bào tử … phân chia ra làm bốn" | "**bốn bào tử** … phân chia ra làm bốn" | — | "tạo ra bốn" | Transcript vs recording: two machine sources agree on **"bốn bào tử"**. Summary: **qualification lost** (the noun is dropped). |
| c163, Alzheimer/Parkinson mention (03:02:47) | `>>` + "Alzimer run rẩy tay chân Parkison." | "Alzheimer, zoom dẩy tay chân, Parkinson, Alzheimer nhớ nhớ quên quên…" as one segment | F0 139–147 Hz continuous from 03:02:44; voiced=5 at 03:02:47 (a pause) | "Parkinson … người nói không rõ" | **Voice separation:** no voice change detected; same male-range voice as before. **Identity:** pending human. |
| c163, improvement statement | Same turn | Same segment | F0 143–147 Hz | inside "bác sĩ Phúc nói" [7] | Same voice as the preceding "Tôi thấy rất nhiều người bỏ được" (03:02:32). Identity pending human. |
| c163, price statement | Same turn | "thì đấy là từ 0,6 trở lên nhưng mà giá thành đắt rồi" | F0 107–146 Hz; no female-range pitch until 03:03:12 | "ông nói … giá thành đắt" | Same continuous voice. Summary vs transcript: the hedge "người nói không rõ" now looks over-cautious, but the identity "ông" is still unconfirmed. |

Speaker attribution is kept separate from content. Pitch separates **voices**, not **identities**: a second male speaker cannot be excluded by pitch, so naming the voice "bác sĩ Phúc" remains a human confirmation. Nothing was inferred from medical content.

**Scientific truth** is out of scope.

## 3. Pilot results (regression sample)

| Clip | YouTube caption | Blind ASR | Note |
|---|---|---|---|
| R1 ratios (01:55:58) | "11 đến 51", "41", "21 hay là 31", "hen suuyễn", "omega6/ên" [8] | "1-1 đến 5-1", "4-1", "2-1 hay là 3-1", "hen xuyển" | ASR is better on ratios. **Both misspell** *suyễn*. Negation "lại không có tác dụng" and the hedge "có thể" are preserved in both. |
| R2 DHA (01:28:50) | 7 `>>` turns incl. ">> D", ">> DA", ">> Liên kết.", ">> Liên kết đôi."; "Khách lành" | No turn markers; "Khánh là"; drops ">> Liên kết." and "DA" | Captions keep the turn structure. ASR loses the backchannel answers and the turn changes. |
| R3 intro (00:02:30) | Plausible dialogue ("4 tiếng hơn 30 phút", "kỷ lực") | **Hallucination:** "Hãy subscribe cho kênh Ghiền Mì Gõ…" for all 25 s | Critical ASR failure mode. Without a VAD and comparison step, ASR output is unsafe. |

**Operational cost:** on this Intel i9-9880H CPU, whisper takes about 0.6× realtime (≈ 2 h for this 3.5 h video). The Metal/AMD backend produces garbage, so `-ng` (CPU only) is required [18]. Full-video ASR is feasible overnight. Running ASR only on flagged windows takes seconds per claim. Human listening takes about 1–2 min per clip.

**Limits:** one video, two primary clips and four regression clips. These are not error rates. ASR accuracy on R2 and R3 shows the model's failure modes; it does not measure them.

## 3a. c163 correction: the `>>` is not a real turn

YouTube's "Show transcript" panel contains **no `>>` markers** (0 of 1999 segments). It groups "Alzimer run rẩy tay chân Parkison." with the 3:02:44 sentence "…trí nhớ bắt đầu cải thiện.", not as a new line at 03:02:47 [20]. The `>>` in our `transcript.md` (814 occurrences) is the ASR speaker-change flag, written into the caption text. The player overlay shows it; the panel strips it.

Evidence that the speaker is continuous from 03:02:44 to 03:02:58:

- **Video frames:** at 03:02:49 and 03:02:59 the man on the left is speaking and gesturing, and the host is listening.
- **Pitch:** one continuous male-range voice.
- **Blind ASR:** one unbroken segment.

Therefore the c163 question "who says Alzheimer improves and who comments on price" rests on a false premise. On machine and visual evidence, the same on-screen speaker says the memory, Alzheimer/Parkinson, improvement and price sentences. The summary's "người nói không rõ" hedge is unnecessary. A human listen is still the final confirmation.

## 3b. Timestamp alignment

Measured by aligning caption word times with blind-ASR word times on the same audio [19]:

- **Raw caption word times are in sync with the audio:** median +0.1 to +0.4 s.
- **`transcript.md` line labels run early:** they are the line start, truncated to the second. A word is spoken a median 1.2–1.4 s after its line label, at most about 4 s. Examples: "tử" is labelled [01:45:37] but spoken at about 01:45:39.9; "đắt" is labelled [03:02:55] but spoken at about 03:02:58.0.
- **Summary links point to the section start:** c068 links to 01:42:36, about 3 min early; c163 links to 03:01:21, about 1.5 min early. Audit quotes carry the first line's time; c068's evidence is labelled 01:45:17.

The pipeline already holds the fix data: per-word `tOffsetMs` exists in the raw json3 but is discarded [5].

## 4. Recommendation: hybrid

1. **Retain** the YouTube captions as the immutable raw layer. They are the source the player shows, are lossless in our pipeline, keep the turn structure (R2), and are required by spec R2 [11].
2. **Add ASR as a triage diff, not a replacement.** For each summary claim's evidence window (±15 s), run blind whisper and diff the critical tokens (terms, numbers, negations) against the captions. Agreement means the caption text is accepted, reported as "two machine sources agree", not as "verified". Disagreement, or an ASR segment with no lexical overlap with the captions (the hallucination signature), goes to a human.
3. **Use targeted human verification** for: speaker attribution near `>>` markers on attributed claims; caption/ASR disagreements on critical words; summary terms that appear in neither source. The packet `human-verification-packet.md` already covers c068, c163 and R1–R3.
4. **Fix the summarizer side:** c068 shows the larger risk is summary normalization ("nguyên phân", dropping "bào tử"), not the transcript. The summary contract should require spoken terms to be kept, or explicitly marked as glosses.

## 5. Proposed separation of artifacts

| Layer | Path (proposed) | Mutability | Content |
|---|---|---|---|
| Raw captions | `videos/<dir>/raw/captions.vi-orig.json3` + `raw/provenance.json` | immutable; a new dated file per retrieval | track id/kind, retrieved_at, sha256, yt-dlp version |
| Rendered transcript | `videos/<dir>/transcript.md` (unchanged) | regenerated from raw with a diff-0 check | today's format |
| ASR triage | `videos/<dir>/asr/<window>.json` | regenerable, never authoritative | model, sha, command, no prompt |
| Verified corrections | `videos/<dir>/transcript-corrections.jsonl` | append-only | `{window, caption_text, asr_text, heard_text, voices:[{start, label}], identity?, identity_confidence, method: human-listen, verifier, date}` |
| Derived summary | `summary.md` | regenerated or edited | claims cite timestamp and layer |
| Audit records | `audit/<id>/…` | append-only | revision-scoped claim IDs: `c068` currently names two different claims [12] |

## 6. Smallest next implementation step

Persist the raw json3 and `provenance.json` in `fetch_transcript.py`, plus a test that re-rendering gives zero diff. This is additive. Next would be a script that takes a claim's window and writes the ASR triage diff; it reuses the commands in `evidence/asr/asr-tooling.txt`. Neither step touches existing transcripts, summaries or review decisions.

## Open items

- A human listener confirms: c068 "gián phân" and "bốn bào tử"; c163 that the voice from 03:02:32 to 03:03:11 is one person and who it is; the R3 dialogue.
- yt-dlp [9]: brew is still on 2026.03.17 (the brew upgrade was interrupted; the original link was restored). This run used 2026.08.19 via `uvx`. Cookies were **not** needed for audio; the `web` client still withholds `vi-orig` without a PO token, which the browser capture covers.

## Sources (local, accessed 2026-10-19/20)

| # | Source |
|---|---|
| [1] | `scripts/fetch_transcript.py`; `videos/2025-12-06-…/metadata.json` |
| [2] | `evidence/raw-captions/list-subs.txt` |
| [3] | `evidence/raw-captions/PROVENANCE.txt` |
| [4] | Re-render of `evidence/raw-captions/q7uDJG8YQ5c.vi-orig.json3` vs `transcript.md` (5330/5330); commit `b8a1ce4` |
| [5] | `evidence/raw-captions/word-level-c068-c163.tsv`; json3 field census |
| [6] | `transcript.md` L2295, L2564; caption counts ("nguyên phân" 0) |
| [7] | `transcript.md` 03:01:58–03:03:43; `audit/q7uDJG8YQ5c/supplement-records.json`, `supplement-pass2.json` |
| [8] | `evidence/raw-captions/regression-sample-raw.txt` |
| [9] | `evidence/audio/dl*.log` (2026-10-19 failures with yt-dlp 2026.03.17) |
| [10] | `evidence/asr/whisper-cli-help.txt` (no mono diarization) |
| [11] | `initiative-tran-van-phuc-knowledge-base.md` R2, R3 |
| [12] | `audit/q7uDJG8YQ5c/final_records.json` vs `supplement-records.json` (id c068) |
| [13] | `evidence/player-captions/player-state.json`, `player-timedtext-1.json3`, `player-timedtext-urls.txt` (Chrome 155, user profile, 2026-10-20) |
| [14] | `evidence/player-captions/screen-{6328,6334,10966,10970,10973}.png`, `screens.json` |
| [15] | `evidence/raw-captions-latest/` (yt-dlp 2026.08.19; sha256 `64d93b68…`, identical) |
| [16] | `evidence/asr/{c068,c068-xref,c163,r1,r2,r3}.whisper-large-v3-turbo.{txt,json}` |
| [17] | `evidence/asr/c163-pitch-track.tsv`, `pitch_track.py` |
| [18] | `evidence/asr/asr-tooling.txt`; `evidence/asr/failed-metal/` |
| [19] | `evidence/timing-alignment.md` |
| [20] | `evidence/player-playback-c163/` (`transcript-panel.json`, `playback-samples.json`, `play-*.png`, `c163-display-comparison.md`) |

## Staleness map

- Caption inventory and yt-dlp access: re-check within 1 month.
- c068/c163 rows: final once the human packet is answered.
