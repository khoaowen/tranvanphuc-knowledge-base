# Fidelity proposed corrections: q7uDJG8YQ5c (draft, not applied)

Source: transcript-fidelity research, `research-transcript-fidelity-q7udjg8yq5c/` (2026-10-20). Ids are the supplement-audit ids (`supplement-records.json`). Match by `current` text in `videos/2025-12-06-…/summary.md`. Nothing here has been applied. Both items are **gated on the human listen** (`human-verification-packet.md`, Clips A and B). Quotes are checked as substrings of `transcript.md`.

Evidence grades used below:
- **caption**: YouTube automatic caption, identical to transcript.md and to the player
- **asr**: blind whisper large-v3-turbo
- **acoustic/visual**: pitch track and video frames
- **human**: a human listener (none yet)

## p1 (c068): keep the spoken division terms
- **status:** pending-human-listen
- **class:** mismatch (unsupported normalization plus a dropped noun)
- **current:** Ông cũng thuật lại phép ví của Lipton coi nhân như cơ quan sinh sản của tế bào; trong phần giải thích, bác sĩ nói nguyên phân tạo ra hai tế bào, còn giảm phân tạo ra bốn.
- **proposed (if the listener confirms "gián phân"):** Ông cũng thuật lại phép ví của Lipton coi nhân như cơ quan sinh sản của tế bào; trong phần giải thích, bác sĩ nói qua quá trình gián phân thì một tế bào tạo nên hai tế bào bằng cách phân chia nhân, còn qua quá trình giảm phân thì một tế bào tạo thành 'bốn bào tử'.
- **fallback (if there is no listen, or the result is unclear):** … bác sĩ nói qua quá trình 'dán phân' (theo phụ đề tự động) thì một tế bào tạo nên hai tế bào, còn qua quá trình giảm phân thì một tế bào tạo thành 'bốn bào tử'.
- **why:**
  - "nguyên phân" occurs 0 times in the captions. The caption says "dán phân", here and at 01:33:57. Blind ASR hears "gián phân" at both places. *dán* and *gián* are homophones in northern speech.
  - The summary drops "bốn bào tử" and reads as "four cells". Caption and ASR agree on "bốn bào tử".
  - Biological correctness is out of scope; the summary should report what was said.
- **quote** [01:45:28]: "Nếu qua quá trình dán phân thì một tế bào sẽ tạo nên hai tế bào bằng cách là phân chia nhân."
- **quote** [01:45:35]: "Thế còn qua quá trình giảm phân thì một tế bào sẽ tạo thành bốn bào tử, tức là nó sẽ phân chia ra làm bốn."
- **evidence grade:** caption plus asr; human pending.

## p2 (c163): one continuous speaker, remove the unclear-speaker hedge
- **status:** pending-human-listen
- **class:** attribution_qualification (the hedge rests on a false turn boundary)
- **current:** Alzheimer 'cải thiện được rất nhiều' (Parkinson được nhắc trong cùng đoạn, người nói không rõ); ông nói từ 0,6 trở lên thì giá thành đắt.
- **proposed (if the listener confirms one voice from 03:02:44 to 03:02:58):** Ông nhắc đến Alzheimer, run rẩy tay chân, Parkinson và nói người 'nhớ nhớ quên quên là cải thiện được rất nhiều, học hành nó tốt'; ông nói từ 0,6 trở lên thì giá thành đắt.
- **fallback (if the listener hears a second voice):** keep the current hedge, and name only the voice the listener identifies.
- **why:** The `>>` at 03:02:47 is YouTube's ASR speaker-change flag. YouTube's own "Show transcript" panel has no `>>` (0 of 1999 segments) and groups this line with the preceding 3:02:44 sentence. All three machine and visual checks show one continuous speaker:
  - Video frames at 03:02:49 and 03:02:59: the man on the left is speaking and the host is listening.
  - Pitch track: one male-range voice.
  - Blind ASR: one unbroken segment.

  The surrounding bullet already attributes the passage to bác sĩ Phúc. 0,6 is the (EPA+DHA)/total-fat concentration ratio, not a dose; the wording is unchanged.
- **quote** [03:02:44]: "Thế rồi trí nhớ bắt đầu cải thiện."
- **quote** [03:02:47]: "Alzimer run rẩy tay chân Parkison. Alzimer nhớ nhớ quên quên là cải thiện được rất nhiều, học hành nó tốt. Thì đấy là từ 0,6 trở lên nhưng mà giá thành đắt rồi."
- **evidence grade:** caption structure, YouTube panel, acoustic/visual and asr; human pending.

## Note on ids

`c068` also names a different claim, the 4:1 ratio claim, in `final_records.json`. These proposals use the supplement-audit id and match by `current` text only.
