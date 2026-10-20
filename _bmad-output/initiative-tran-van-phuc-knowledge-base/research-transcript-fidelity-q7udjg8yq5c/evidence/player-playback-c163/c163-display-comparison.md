# c163: what YouTube displays vs our transcript.md (2026-10-20, Chrome 155, user profile)

| Source | 03:02:44–03:02:58 as displayed |
|---|---|
| transcript.md | `[03:02:44] thứ nọ kia hết. Thế rồi trí nhớ bắt đầu` / `[03:02:46] cải thiện.` / `[03:02:47] >> Alzimer run rẩy tay chân Parkison.` / `[03:02:51] Alzimer nhớ nhớ quên quên là cải thiện` … `[03:02:55] là từ 0,6 trở lên nhưng mà giá thành đắt` |
| YouTube "Show transcript" panel | `3:02:44 thứ nọ kia hết. Thế rồi trí nhớ bắt đầu cải thiện. Alzimer run rẩy tay chân Parkison.` / `3:02:51 Alzimer nhớ nhớ quên quên là cải thiện được rất nhiều, học hành nó tốt. Thì đấy là từ 0,6 trở lên nhưng mà giá thành đắt` / `3:02:58 rồi. …` (no `>>` anywhere: 0 of 1999 segments) |
| Player overlay during normal playback | `>> Alzimer` appears at player time 10968.2 s (03:02:48.2); the price line is shown at 10978.2 s (03:02:58.2) (playback-samples.json) |
| Video frames | 03:02:49 and 03:02:59: the man on the left is speaking and gesturing; the woman (host) is listening, holding a phone (play-10969.0.png, play-10979.0.png) |
| Pitch | one continuous male-range voice, 03:02:44–03:02:58 (../asr/c163-pitch-track.tsv) |
| Blind ASR | one continuous segment, no break (../asr/c163.whisper-large-v3-turbo.txt) |

Conclusion: the 03:02:47 "turn boundary" is an artifact of the ASR speaker-change flag in the caption data. YouTube's transcript panel drops it and groups "Alzimer run rẩy tay chân Parkison." with the preceding 3:02:44 sentence. All machine and visual evidence shows one continuous speaker, the man on screen, from "trí nhớ bắt đầu cải thiện" through "giá thành đắt rồi". Human listening has not been done.
