# GPT rerun (c) triage: proposed corrections, q7uDJG8YQ5c (draft, NOT applied)

Source: `review.md` from the 2026-10-22 `gpt-6.1-sol` rerun after the c024 trim and the six approved next-pass edits. Result: **fail**; 188 pass, 18 flag, 4 fail (210 claims); omissions 0; coverage complete; 3 concerns. Previous review preserved as `review-before-fidelity-rerun-2026-10-22c.json`.

Preconditions verified:
- `summary.md` SHA-256 `d6e464b8116388cc1f4dd23455fc667636076343d3a31fda4f5061614e5304f8` (equals `review.md.summary_sha256`).
- `transcript.md` SHA-256 `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`.
- `review.md` SHA-256 `f5b3a5c4752a825274e54bc0f86523432db7018569dff0443711550c5de0f22d`.
- Every fail/flag claim text matches `summary.md` exactly. Every `old text` below matches exactly once.

Nothing applied. Every item is **pending-human-approval**. Quote ranges come from `scripts/fidelity.resolve_quote`; at least 60 s of context on each side was read.

## Summary

| id | status | class | proposal |
|---|---|---|---|
| **c118** | fail | **partly supported** | **g1 rewrite** |
| c149 | fail | reviewer error | none |
| c076 | fail | reviewer error (repeat of old c073) | none |
| c186 | fail | reviewer error (repeat of old c181) | none; optional g4 to stop the repeat |
| c174 | flag | supported at a different timestamp | none |
| c003, c146, c147, c150, c171, c180 | flag | reviewer error | none |
| c010, c033, c070, c071, c073, c075, c101, c123, c172, c175 | flag | repeats of earlier flags, already triaged as supported | none |
| c148 | flag | repeat of c144 (f1, skipped by you) | none |
| (no id) | n/a | process wording left in summary | **g2, g3 remove "caption ghi"** |

## g1 (c118): fix the 20:1 denominator

- **status:** pending-human-approval
- **section:** `[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách`
- **watch:** [02:28:58](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=8938s) to 02:29:33
- **review finding:** Trong câu nêu 20:1, mẫu số được nói là DHA hoặc EPA, không phải tổng Omega-3 như cách diễn đạt của nhận định.
- **class:** partly supported. The 20:1, US/Europe, research framing and "hòa loãng" are all in the source. But the preceding sentence of the summary sets up "tỷ lệ Omega-6/Omega-3", so a reader takes 20:1 as omega-6:omega-3. The doctor actually says the components eaten are divided by **DHA or EPA**. The claim also drops that this is what studies found.
- **old text:** `Tuy nhiên, tại Mỹ và Châu Âu, người dân đang ăn theo tỷ lệ mất cân bằng lên tới 20:1, khiến các dưỡng chất quý như EPA và DHA bị hòa loãng.`
- **new text:** `Tuy nhiên, bác sĩ Phúc nói các nghiên cứu ở Mỹ và châu Âu thấy các thành phần này trong khẩu phần, đem chia cho DHA hoặc EPA, có tỷ lệ tới 20:1, khiến các dưỡng chất quý như EPA và DHA bị hòa loãng, không còn ý nghĩa.`
  - quote (computed `fidelity.resolve_quote` range `02:29:01-02:29:13`): "những nghiên cứu đến bây giờ phút này, đặc biệt là ở Mỹ hay là quốc các quốc gia Châu Âu người ta thấy rằng chúng ta đang ăn những thành phần này đem chia cho DHA hoặc epa là tỉ lệ 20 chia 1."
  - quote (computed `fidelity.resolve_quote` range `02:29:20-02:29:23`): "toàn bộ những vàng này nó sẽ bị hòa loãng ra vô nghĩa rồi."

## g2: remove "caption ghi 'dầu ôu'" (line 112)

- **status:** pending-human-approval
- **watch:** [01:57:03](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=7023s)
- **why:** audit/process wording in reader text, same rule you set for o3/o5. Transcript `01:57:09` reads "ôu"; "dầu ô liu" is the normalisation.
- **old text:** `còn dầu ô liu (caption ghi 'dầu ôu'), dầu cọ`
- **new text:** `còn dầu ô liu, dầu cọ`

## g3: remove "caption ghi 'phải mua APA cao hơn DHA'" (line 214)

- **status:** pending-human-approval
- **watch:** [03:14:04](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=11644s)
- **why:** same rule. The transcript `03:14:05` says "APA", which the summary already normalises to EPA in the same sentence.
- **old text:** `để quét mỡ máu và quét gan nhiễm mỡ đi (caption ghi 'phải mua APA cao hơn DHA').`
- **new text:** `để quét mỡ máu và quét gan nhiễm mỡ đi.`
  - quote (computed `fidelity.resolve_quote` range `03:14:05`): "thì chúng ta phải mua APA cao hơn DHA."

## g4 (c186, optional): add the 02:25 nuance so the reviewer stops failing it

- **status:** pending-human-approval (optional; the current claim is accurate)
- **watch:** [03:14:32](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=11672s) and [02:25:27](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=8727s)
- **why:** the claim matches its own quote at 03:14:44 to 03:14:56; the reviewer has failed it twice by comparing it to 02:25:27. Adding the second statement records both and should end the repeat.
- **old text:** `theo bác sĩ Phúc, phần EPA còn thừa cũng có thể bổ sung cho não.`
- **new text:** `theo bác sĩ Phúc, phần EPA còn thừa cũng có thể bổ sung cho não (ở đoạn trước ông nói EPA có dành một phần rất nhiều cho não, nhưng ưu thế vẫn dành cho tim).`
  - quote (computed `fidelity.resolve_quote` range `03:14:54-03:14:56`): "Và EPA nó xu hướng ở ngoài còn thừa nó sẽ bổ sung cho não."
  - quote (computed `fidelity.resolve_quote` range `02:25:27-02:25:29`): "Tất nhiên EPA dành có dành một phần rất nhiều cho não nữa."
  - quote (computed `fidelity.resolve_quote` range `02:25:30`): "Nhưng mà ưu thế thì nó vẫn dành cho tim."

## No change: new items checked

- **c149** (reviewer error). Watch [02:41:56](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=9716s). Own evidence says Omega-3 is the most valuable, and within it EPA and DHA. The reviewer judged a different slice (02:34:19).
  - quote (computed `fidelity.resolve_quote` range `02:41:59-02:42:05`): "quý nhất thì vẫn chỉ là omega 3 và trong omega 3 quý nhất là cái gì?"
  - quote (computed `fidelity.resolve_quote` range `02:42:10-02:42:13`): "Hai cái này là cái quý nhất."
- **c174** (supported at a different timestamp). Watch [03:02:08](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=10928s). The review cited 03:02:58, which lacks the price; "khá đắt rồi" is verbatim at 03:02:16 to 03:02:18, tied to 0,5.
  - quote (computed `fidelity.resolve_quote` range `03:02:16-03:02:18`): "Nó khá đắt rồi. Từ 0 phẩ chia được con số được 0,5 là khá đắt rồi."
  - quote (computed `fidelity.resolve_quote` range `03:02:58-03:03:00`): "Đại đa số thì mọi người chấp nhận được con số 0,5 đến con số 0,6."
- **c003** (reviewer error). Watch [00:02:14](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=134s). Paraphrase of own evidence; "y khoa" follows from the section topic.
  - quote (computed `fidelity.resolve_quote` range `00:02:14-00:02:18`): "Tuy nhiên thì để có kiến thức rộng và sâu thì video ngắn hoàn toàn không thể đáp ứng được."
- **c146** (reviewer error). Watch [02:40:31](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=9631s). Own evidence 02:40:31 to 02:40:47 includes "người trưởng thành cần chăm sóc sức khỏe não, mắt và tim mạch".
  - quote (computed `fidelity.resolve_quote` range `02:40:31-02:40:38`): "Với trẻ em, phụ nữ có thai và người trưởng thành cần chăm sóc sức khỏe não, mắt và tim mạch thì chọn loại omega 3 giàu DHA hơn."
- **c147** (reviewer error). Watch [03:13:30](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=11610s). Own evidence 03:14:24 plus the disease-based choice at 03:13:30 to 03:14:05 and 03:14:59 to 03:15:16.
  - quote (computed `fidelity.resolve_quote` range `03:14:24-03:14:31`): "Quý vị đừng nhớ là trẻ em với phụ nữ có thai hay là người trung niên hay là cái gì nó hơi khó."
  - quote (computed `fidelity.resolve_quote` range `03:14:59-03:15:07`): "những ai đang bị gan nhiễm mỡ, bị mỡ máu, bị tiểu đường, bị đau khớp, bị tăng huyết áp"
- **c150** (reviewer error). Watch [02:42:27](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=9747s). Own evidence has both.
  - quote (computed `fidelity.resolve_quote` range `02:42:27-02:42:32`): "Vì cái DPA thì nó cũng không phải là cái sản phẩm chỉ là sản phẩm trung gian thôi."
  - quote (computed `fidelity.resolve_quote` range `02:42:34-02:42:39`): "Thế còn ALA thì có một đặc điểm là trong dầu thực vật có rất nhiều."
- **c171** (reviewer error). Watch [03:01:21](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=10881s). Own evidence 03:01:21 to 03:01:41 has impurities, unnecessary fats, closer to natural, easier to absorb.
  - quote (computed `fidelity.resolve_quote` range `03:01:25-03:01:28`): "Đang có xu hướng nhiều tạp chất."
  - quote (computed `fidelity.resolve_quote` range `03:01:38-03:01:40`): "Nhưng mà có cái ưu điểm là gần với tự nhiên hơn,"
- **c180** (reviewer error). Watch [03:04:40](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=11080s). Own evidence has prescription and very high price.
  - quote (computed `fidelity.resolve_quote` range `03:04:40-03:04:46`): "Còn từ 0,9 trở lên thì bác sĩ kê đơn để điều trị một số những các cái căn bệnh này khác"
  - quote (computed `fidelity.resolve_quote` range `03:04:59`): "và giá thành của nó thì rất đắt."

## Concerns

- **material, c118:** addressed by g1.
- **minor, c186:** addressed by optional g4.
- **minor, c112 (ALA inconsistency):** the transcript later says "Alla gây viêm" (02:10:53). You confirmed by ear that he says LA is inflammatory and ALA anti-inflammatory, and you chose to remove the 'Alla' sentence. No change proposed; it may keep appearing as a minor concern.

## Approval

Waiting for approval of g1, g2, g3 and optional g4. Nothing applied.

