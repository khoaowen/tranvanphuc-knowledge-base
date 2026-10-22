# Fidelity proposed corrections: q7uDJG8YQ5c (draft, not applied)

Source: transcript-fidelity research, `research-transcript-fidelity-q7udjg8yq5c/` (2026-10-20). Ids are the supplement-audit ids (`supplement-records.json`). Match by `current` text in `videos/2025-12-06-…/summary.md`. Nothing here has been applied. Both items were **gated on the human listen** (`human-verification-packet.md`, Clips A and B). Answers were recorded 2026-10-22 in `research-transcript-fidelity-q7udjg8yq5c/evidence/human-listening-ab-2026-10-22.md`. On 2026-10-22 the owner (BDK) approved the exact proposed text of both items. Both were applied to `summary.md` on 2026-10-22 (`fidelity-apply-2026-10-22.md`). Quotes are checked as substrings of `transcript.md`, with line breaks joined.

Evidence grades used below:
- **caption**: YouTube automatic caption, identical to transcript.md and to the player
- **asr**: blind whisper large-v3-turbo
- **acoustic/visual**: pitch track and video frames
- **human**: one listener, the project owner (BDK), answers recorded 2026-10-22. No headphones. Not blind: the listener had seen the captions before listening. Speaker identity for c163 was given with 100% confidence.

## p1 (c068): keep the spoken division terms
- **status:** applied (approved by BDK and applied to summary.md on 2026-10-22; see `fidelity-apply-2026-10-22.md`)
- **class:** mismatch (unsupported normalization plus a dropped noun)
- **current:** Ông cũng thuật lại phép ví của Lipton coi nhân như cơ quan sinh sản của tế bào; trong phần giải thích, bác sĩ nói nguyên phân tạo ra hai tế bào, còn giảm phân tạo ra bốn.
- **proposed (the listener heard "gián phân"):** Ông cũng thuật lại phép ví của Lipton coi nhân như cơ quan sinh sản của tế bào; trong phần giải thích, bác sĩ nói qua quá trình gián phân thì một tế bào tạo nên hai tế bào bằng cách phân chia nhân, còn qua quá trình giảm phân thì một tế bào tạo thành 'bốn bào tử'.
- **fallback:** superseded by the human listen. The earlier 'dán phân' (caption) wording is no longer proposed.
- **why:**
  - "nguyên phân" occurs 0 times in the captions. The caption says "dán phân", here and at 01:33:57. Blind ASR hears "gián phân" at both places. *dán* and *gián* are homophones in northern speech.
  - The summary drops "bốn bào tử" and reads as "four cells". Caption and ASR agree on "bốn bào tử".
  - Human listen (2026-10-22):
    - A1 "Gián phân"; A-xref: the same term at 01:33:55.
    - A2 "một tế bào sẽ tạo nên hai tế bào".
    - A3 "giảm phân".
    - A4 "một tế bào sẽ tạo thành 4 bào tử".
    - A5: the same speaker throughout.
  - "bằng cách phân chia nhân" rests on caption and ASR. The listener was not asked to confirm it.
  - Biological correctness is out of scope; the summary should report what was said.
- **quote** [01:45:28]: "Nếu qua quá trình dán phân thì một tế bào sẽ tạo nên hai tế bào bằng cách là phân chia nhân."
- **quote** [01:45:35]: "Thế còn qua quá trình giảm phân thì một tế bào sẽ tạo thành bốn bào tử, tức là nó sẽ phân chia ra làm bốn."
- **evidence grade:** caption, asr and human (one listener). Human and ASR agree on "gián phân". The caption's "dán" is treated as a homophone transcription. The listener had seen the captions beforehand, so the listen was not blind.

## p2 (c163): one continuous speaker, remove the unclear-speaker hedge
- **status:** applied (approved by BDK and applied to summary.md on 2026-10-22; see `fidelity-apply-2026-10-22.md`)
- **class:** attribution_qualification (the human listener heard no voice change at the caption's `>>` turn marker)
- **current:** Alzheimer 'cải thiện được rất nhiều' (Parkinson được nhắc trong cùng đoạn, người nói không rõ); ông nói từ 0,6 trở lên thì giá thành đắt.
- **proposed (the listener heard one voice, the doctor, from 03:02:08 to 03:03:15):** Ông nhắc đến Alzheimer ('nhớ nhớ quên quên') và Parkinson ('run rẩy tay chân'), nói là 'cải thiện được rất nhiều, học hành nó tốt'; ông nói từ 0,6 trở lên thì giá thành đắt.
- **fallback:** superseded by the human listen, which heard no second voice.
- **why:** The `>>` at 03:02:47 is YouTube's ASR speaker-change flag. YouTube's own "Show transcript" panel has no `>>` (0 of 1999 segments) and groups this line with the preceding 3:02:44 sentence. Machine and visual checks are compatible with one continuous speaker, but they cannot prove identity on their own:
  - Video frames at 03:02:49 and 03:02:59: the man on the left appears to be speaking and the host listening. These are visual context only.
  - Pitch track: one male-range voice. This cannot rule out a second, similar voice.
  - Blind ASR: one unbroken segment.

  Human listen (2026-10-22):
  - B1: no voice change.
  - B2: "Alzimer nhớ nhớ quên quên, Parkison run rẩy tay chân", spoken by the doctor.
  - B3: same voice.
  - B4: still the doctor.
  - B5: "0.6".

  The surrounding bullet already attributes the passage to bác sĩ Phúc.

  Wording change from the earlier draft: B2's word order differs from the caption ("Alzimer run rẩy tay chân Parkison. Alzimer nhớ nhớ quên quên…"). The proposal therefore pairs each condition with the phrase the listener heard. It no longer quotes "nhớ nhớ quên quên là cải thiện…" as one caption string. B3 confirms the voice but gives no verbatim text, so 'cải thiện được rất nhiều, học hành nó tốt' rests on the caption only.

  B6 ("từ 0.5 là khá đắt rồi" at 03:02:16) is outside the claim text and does not change it. 0,6 is the (EPA+DHA)/total-fat concentration ratio, not a dose; the wording is unchanged.
- **quote** [03:02:44]: "Thế rồi trí nhớ bắt đầu cải thiện."
- **quote** [03:02:47]: "Alzimer run rẩy tay chân Parkison. Alzimer nhớ nhớ quên quên là cải thiện được rất nhiều, học hành nó tốt. Thì đấy là từ 0,6 trở lên nhưng mà giá thành đắt rồi."
- **evidence grade:** caption structure, YouTube panel, acoustic/visual, asr and human (one non-blind listener, BDK, who identified the speaker as the doctor with 100% confidence).

## Note on ids

`c068` also names a different claim, the 4:1 ratio claim, in `final_records.json`. These proposals use the supplement-audit id and match by `current` text only.
