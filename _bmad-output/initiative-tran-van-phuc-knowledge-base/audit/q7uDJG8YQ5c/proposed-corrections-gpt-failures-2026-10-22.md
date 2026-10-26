# GPT fidelity failures: proposed corrections, q7uDJG8YQ5c (draft, not applied)

Source: `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/review.md` (GPT rerun, `fidelity-rerun-gpt-2026-10-22.md`). Result: fail; 185 pass, 15 flag, 4 fail (204 claims); 7 omissions; 1 concern. Claim ids are current-summary ids; match by exact old text.

Preconditions verified before analysis:

- `summary.md` SHA-256: `a7fa809724e4988c07bf89ff5723dff58cef2650b78b1405eacada5384437d8d` (matched; also equals `review.md.summary_sha256`).
- `transcript.md` SHA-256: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b` (matched).

Analysis only. No summary, transcript, review, queue_state, publishable, or existing audit file was edited. Nothing was committed, pushed, published, or sent to a paid service. Every proposal is **pending-human-approval**; none is applied. Note on `review.md`: it is a JSON document; fields below come from it directly.

## Triage result

| claim | review status | class | proposed fix |
|---|---|---|---|
| c024 | fail | partly supported | trim (rewrite last clause) |
| c068 | fail | reviewer error | none |
| c073 | fail | reviewer error | none |
| c181 | fail | reviewer error | none (see optional note) |

Pattern for c068, c073, c181: the reviewer's own cited `quote` (and its `evidence` entry) verbatim supports the claim. The recorded `issue` points at a different slice (`01:33:55`, `03:16:08`, `02:25:27`), which is a different statement. The fail comes from that mismatched slice, not from the claim text. `resolve_quote` confirms each primary quote lies exactly at the range the review cites.

## p1 (c024): trim the unsupported "vô cùng dài" ending

- **status:** pending-human-approval
- **section:** `[00:34:05] Mô hình toán học về giá trị cuộc sống (Hàm V)`
- **review status:** fail (supported=false, attributed=true, qualifications_preserved=false)
- **current claim:** (Ví dụ bác sĩ Phúc kể để cho thấy chiều rộng cuộc sống (W) quan trọng hơn chiều dài: một người anh họ bác sĩ bị ung thư dạ dày giai đoạn cuối chỉ sống thêm hơn 1 năm sau phẫu thuật, nhưng nhờ tập trung lo liệu chu toàn cho gia đình nên khoảng thời gian ngắn đó đã trở nên vô cùng dài và có ý nghĩa).
- **cited timestamp:** `00:38:43-00:39:01`
- **review finding:** Câu chuyện và ý nghĩa của hơn một năm được kể rõ, nhưng nguồn nêu tiên lượng sống sau phẫu thuật; cách viết 'chỉ sống thêm' biến tiên lượng thành kết cục đã được xác nhận.
- **cited quote:** "nhưng mà anh ấy lại bị ung thư vào cái giai đoạn cuối. Thế thành ra là xác định cái thời gian sống của anh ấy chỉ hữu hạn thôi. Tức là ngắn trong vòng cơ độ hơn năm trời, năm rưỡi là cùng. >> Vâng. >> Nếu không phẫu thuật thì anh ấy chỉ 1 hai tháng không thể vượt qua được. Thế nhưng nếu phẫu thuật thì sẽ kéo dài ra được năm hơn năm."
- **class:** partly supported
- **60-second context read:** `00:37:40–00:41:05` (candidate passage `00:38:11–00:40:59`; 60+ seconds before and after were read). Searched the whole transcript for `ung thư dạ dày` (only `00:10:03`, an unrelated mention, and `00:38:28`), `anh họ`, `người anh trong họ`, `vô cùng dài`, `rất dài`.
- **what is supported:** the relative is a man over 70 with stomach cancer (`00:38:17-00:38:28`); surgery removed the tumour but it was already late-stage (`00:38:41-00:38:45`); prognosis "hơn năm trời, năm rưỡi là cùng" and 1–2 months without surgery (`00:38:48-00:39:01`); the doctor tells him life width matters more than length (`00:39:09-00:39:12`); he focused on arranging things for his family (`00:40:29-00:40:43`); and the doctor reports that over the "hơn năm trời" he did the most in his life and his life continues in his child and grandchild (`00:40:49-00:40:59`). That last line also covers "chỉ sống thêm hơn 1 năm", so the reviewer's prognosis-vs-outcome point is largely answered, though the doctor never states the exact date of death.
- **what is not supported:** "khoảng thời gian ngắn đó đã trở nên vô cùng dài". The source never calls the period long; the nearest statements are "làm được nhiều việc nhất trong cuộc đời" and that he can leave "thanh thản". "Vô cùng dài" is a figurative gloss added by the summary.
- **minimal fix:** trim: replace only the ending clause with the source's own claim. The section heading citation is unchanged (the passage falls inside `00:34:05`–next section).
- **old text:** `nhưng nhờ tập trung lo liệu chu toàn cho gia đình nên khoảng thời gian ngắn đó đã trở nên vô cùng dài và có ý nghĩa)`
- **new text:** `nhưng nhờ tập trung lo liệu chu toàn cho gia đình nên theo lời bác sĩ, ông anh thấy trong hơn một năm đó mình làm được nhiều việc nhất trong cuộc đời và ra đi thanh thản)`
- **why:** Removes the invented "vô cùng dài" while keeping the point (width over length). "Ra đi thanh thản" is the relative's reported statement at `00:40:45-00:40:49`; drop that tail if a shorter edit is preferred. The uncertainty about the exact lifespan is left as is.
- **quote** (computed `fidelity.resolve_quote` range: `00:40:43-00:40:49`): "Anh đã chuẩn bị tất cả mọi thứ và đến bây giờ anh ra đi anh thanh thản, anh không phải suy nghĩ gì."
- **quote** (computed `fidelity.resolve_quote` range: `00:40:49-00:40:59`): "Và đây là cái thời gian mặc dù có hơn năm trời thôi nhưng mà anh thấy anh làm được nhiều việc nhất trong cuộc đời và cuộc đời của anh vẫn còn tiếp nối đối với con anh và đối cháu anh."
- **quote** (computed `fidelity.resolve_quote` range: `00:38:51-00:38:53`): "Tức là ngắn trong vòng cơ độ hơn năm trời, năm rưỡi là cùng."
- **quote** (computed `fidelity.resolve_quote` range: `00:40:29-00:40:31`): "anh ấy tập trung làm các cái công việc xong xuôi"
- **review quote check:** the review's cited quote resolves to `00:38:43-00:39:01`; it supports the prognosis only, so it does not cover the outcome sentences above.

## p2 (c068): reviewer error, no change proposed

- **status:** pending-human-approval (decision: no change)
- **section:** `[01:42:36] Khái niệm màng tế bào là bộ não của tế bào`
- **review status:** fail (supported=false, attributed=false, qualifications_preserved=true)
- **current claim:** Ông cũng thuật lại phép ví của Lipton coi nhân như cơ quan sinh sản của tế bào; trong phần giải thích, bác sĩ nói qua quá trình gián phân thì một tế bào tạo nên hai tế bào bằng cách phân chia nhân, còn qua quá trình giảm phân thì một tế bào tạo thành 'bốn bào tử'.
- **cited timestamp:** `01:45:19-01:45:41`
- **cited quote:** "nhân nó chỉ là bộ phận sinh dục của tế bào. Nhân chính là bộ phận sinh dục của tế bào bởi vì nhân nó chỉ là nhân tế bào nó chỉ có nhân lên thôi. Nếu qua quá trình dán phân thì một tế bào sẽ tạo nên hai tế bào bằng cách là phân chia nhân. Thế còn qua quá trình giảm phân thì một tế bào sẽ tạo thành bốn bào tử, tức là nó sẽ phân chia ra làm bốn."
- **review finding:** Có phần bác sĩ giải thích một tế bào phân chia thành hai; chưa có phép ví của Lipton về cơ quan sinh sản hoặc nội dung giảm phân thành bốn bào tử. (slice `01:33:55-01:34:04`, which is Dr. Phúc explaining cell division in the DNA section, not the passage this claim cites)
- **class:** reviewer error
- **60-second context read:** `01:44:16–01:46:50`. Lipton is the subject throughout (`01:44:53`: "nhà khoa học Lip tông ... màng tế bào mới là bộ não của tế bào"; `01:45:13-01:45:17`: "Từ đấy ông đưa ra thế này, ông đưa ra cái là nhân nó chỉ là bộ phận sinh dục của tế bào"). The cited text then gives the mitosis and meiosis explanation and concludes "nhân tế bào ở đây phải là cơ quan sinh sản của tế bào" (`01:45:45-01:45:47`).
- **why it holds:** attribution to Lipton is explicit ("ông đưa ra"); the doctor does explain cell division as the nucleus's role; "bốn bào tử" is verbatim at `01:45:37`. The transcript says "dán phân" (ASR), and the summary's "gián phân" is a reasonable normalisation. A residual nit: "phép ví" is slightly stronger than the source (it is stated as a claim, not an analogy) and "cơ quan sinh sản" comes at `01:45:45`, just after the cited `01:45:19-01:45:41`. Neither changes the meaning.
- **quote** (computed `fidelity.resolve_quote` range: `01:45:19-01:45:28`): "nhân nó chỉ là bộ phận sinh dục của tế bào. Nhân chính là bộ phận sinh dục của tế bào bởi vì nhân nó chỉ là nhân tế bào nó chỉ có nhân lên thôi."
- **quote** (computed `fidelity.resolve_quote` range: `01:45:28-01:45:41`): "Nếu qua quá trình dán phân thì một tế bào sẽ tạo nên hai tế bào bằng cách là phân chia nhân. Thế còn qua quá trình giảm phân thì một tế bào sẽ tạo thành bốn bào tử, tức là nó sẽ phân chia ra làm bốn."
- **quote** (computed `fidelity.resolve_quote` range: `01:45:41-01:45:47`): "Thế vậy thì nhân tế bào ở đây phải là cơ quan sinh sản của tế bào"
- **old text:** n/a
- **new text:** n/a. Optional, only if wanted: widen the cited range to `01:45:19-01:45:47`; the review does not require it.

## p3 (c073): reviewer error, no change proposed

- **status:** pending-human-approval (decision: no change)
- **section:** `[01:47:01] Vai trò của Omega-3, DHA và EPA trong cấu trúc màng tế bào`
- **review status:** fail (supported=false, attributed=true, qualifications_preserved=false)
- **current claim:** Ông cũng cho rằng ăn cá giàu DHA có thể giúp thông minh hơn và mắt sáng hơn; nếu DHA ít thì khó đạt được điều đó.
- **cited timestamp:** `01:49:16-01:49:32`
- **cited quote:** "nếu cá đó có nhiều DHA thì chúng ta ăn sẽ thông minh và chúng ta ăn sẽ có ngoài cái thông minh lên thì mắt chúng ta nhìn cũng sẽ sáng lên nhưng với điều kiện là DHA nó phải nhiều. Thế còn nếu DHA ít thì chúng ta cũng khó để mà có cái điều đấy được."
- **review finding:** Đoạn này nói về bổ sung DHA, không nói ăn cá; lời khuyên tăng DHA đi kèm điều kiện khỏe mạnh, xét nghiệm tốt và không có bệnh. (slice `03:16:08-03:16:22`, a different passage about taking supplements)
- **class:** reviewer error
- **60-second context read:** `01:48:20–01:50:35`, plus the neighbouring `01:47:01–01:48:20`. The doctor answers the audience question "chúng ta ăn cá nó có giúp thông minh hay không?" (`01:48:40-01:48:45`) and then gives the answer at `01:49:16-01:49:32`. The conditional "nếu DHA ít thì khó" is preserved in the claim, and "giàu DHA" matches "nhiều DHA". The `03:16` passage is a separate statement on supplementing DHA, which is used for another claim.
- **why it holds:** the claim restates the cited quote closely, with the condition and negative case kept. The summary's "có thể giúp" is a mild hedge relative to "sẽ thông minh", which is safe.
- **quote** (computed `fidelity.resolve_quote` range: `01:49:16-01:49:32`): "nếu cá đó có nhiều DHA thì chúng ta ăn sẽ thông minh và chúng ta ăn sẽ có ngoài cái thông minh lên thì mắt chúng ta nhìn cũng sẽ sáng lên nhưng với điều kiện là DHA nó phải nhiều. Thế còn nếu DHA ít thì chúng ta cũng khó để mà có cái điều đấy được."
- **quote** (computed `fidelity.resolve_quote` range: `01:48:48-01:48:56`): "nếu cá mà có nhiều loại nào mà có nhiều DHA thì thứ nhất là nó sẽ giúp cho có nhiều DHA để nuôi tế bào não và tế bào mắt."
- **old text:** n/a
- **new text:** n/a

## p4 (c181): reviewer error, no change proposed

- **status:** pending-human-approval (decision: no change)
- **section:** `[03:13:11] Lựa chọn tỷ lệ EPA và DHA theo tình trạng bệnh lý`
- **review status:** fail (supported=false, attributed=true, qualifications_preserved=false); the review's `concerns` also repeats this as a minor concern (`02:25:27-02:25:29`)
- **current claim:** Bác sĩ Phúc đưa ra nguyên tắc lựa chọn dựa trên nơi các chất ưu tiên đi tới: DHA ưu tiên đi vào não và mắt, còn EPA ưu tiên đi vào tim; theo bác sĩ Phúc, phần EPA còn thừa cũng có thể bổ sung cho não.
- **cited timestamp:** `03:14:44-03:14:56`
- **cited quote:** "DHA thì ưu tiên đi vào não và >> mắt. >> Còn DPA à EPA thì đi vào đâu ạ? >> Đi vào tim. Chúng ta nhớ nguyên tắc đó. Và EPA nó xu hướng ở ngoài còn thừa nó sẽ bổ sung cho não."
- **review finding:** Ưu tiên não/mắt và tim được xác nhận, nhưng lát này nói EPA cũng dành một phần cho não, không giới hạn phần đó là EPA còn thừa. (slice `02:25:27-02:25:30`)
- **class:** reviewer error
- **60-second context read:** `03:13:11–03:16:00` and `02:24:00–02:26:35`. At `03:14:32-03:14:56` the doctor gives the rule: DHA goes to brain and eyes, EPA goes to the heart, "EPA nó xu hướng ở ngoài còn thừa nó sẽ bổ sung cho não". The summary's "phần EPA còn thừa cũng có thể bổ sung cho não" follows that sentence, and "có thể" is a hedge.
- **why it holds:** the claim matches the passage it cites. The `02:25` slice is a different, earlier statement ("EPA có dành một phần rất nhiều cho não nữa ... ưu thế vẫn dành cho tim"). The two statements differ in degree but do not contradict, and the claim faithfully reports the one it cites. One weakness: the ASR phrase "xu hướng ở ngoài" is garbled, so the claim only rests on "còn thừa nó sẽ bổ sung cho não".
- **optional note (not a fix):** if the human wants the nuance, add it as a new omission-style claim from `02:25:27-02:25:33`; do not alter c181.
- **quote** (computed `fidelity.resolve_quote` range: `03:14:44-03:14:47`): "DHA thì ưu tiên đi vào não và mắt."
- **quote** (computed `fidelity.resolve_quote` range: `03:14:52-03:14:56`): "Đi vào tim. Chúng ta nhớ nguyên tắc đó. Và EPA nó xu hướng ở ngoài còn thừa nó sẽ bổ sung cho não."
- **quote** (computed `fidelity.resolve_quote` range: `02:25:27-02:25:29`): "Tất nhiên EPA dành có dành một phần rất nhiều cho não nữa."
- **old text:** n/a
- **new text:** n/a

## Next-pass queue (no changes drafted)

Severity here is my provisional triage, not reviewer-assigned (the review gives claim status only, except the one concern marked `minor`). Fix-type labels are hypotheses to test in the next pass. A recurring pattern in the flags: the review's `issues` slice differs from the cited `evidence` slice, so many flags may be reviewer slice artefacts like c068/c073/c181, so check evidence first before editing.

### Flags (15)

**Higher (health advice, dosage, medication or numeric statements; wrong wording could mislead readers)**

| id | topic | review finding (short) | likely fix |
|---|---|---|---|
| c170 | Từ 0,6 trở lên bỏ được thuốc | slice at `03:08:42` mentions only improvement at 0.6, not stopping medication | search for the medication claim; likely re-cite or trim |
| c130 | Kết hợp dưỡng chất, bỏ thuốc | slice lacks oil control and stopping heart/BP/diabetes/lipid/thyroid medication | check full range; likely re-cite or trim |
| c122 | 3 nắp chai bia dầu ăn, mỡ lợn bù | `03:04` slice has the limit but not lard | likely re-cite; trim lard if absent |
| c167 | Theo dõi, nguy cơ tăng mỡ máu/gan nhiễm mỡ | slice has monitoring, not the warning | check; likely re-cite or trim |
| c114 | Tỷ lệ 4:1 chấp nhận, cùng lắm 5:1 | slice has only the "không để lên 4–5:1" advice | likely trim attribution/"dẫn tài liệu" part |
| c178 | Mua ở nhà thuốc, không tích trữ | slice lacks the stockpiling advice | likely re-cite |
| c144 | Tiêu chí cấp phép, công ty dược | `03:10:30` slice shows no read-aloud criteria | likely re-cite (an `02:39:11`-area passage) |

**Medium (attribution or completeness of factual content)**

| id | topic | review finding (short) | likely fix |
|---|---|---|---|
| c010 | Gödel, Định lý bất toàn 1931 | slice has no Gödel, nationality or year | likely re-cite; trim details only if absent |
| c072 | DHA "vàng của não và mắt", EPA "vàng của tim" | slice lacks EPA gold | likely re-cite (second evidence at `02:24:45`) |
| c119 | EPA và DHA trong cá biển sâu / gan cá | slice lacks EPA and liver | likely re-cite or trim "gan cá biển sâu" |
| c098 | acetyl-CoA hai cacbon | slice lacks "hai cacbon" | likely trim or re-cite |
| c136 | Bài báo: DHA cho trẻ/thai phụ, EPA cho nhóm khác | slice cut before the EPA group | likely re-cite to a longer range |

**Lower (illustrative detail; low risk if slightly mis-cited)**

| id | topic | review finding (short) | likely fix |
|---|---|---|---|
| c033 | Ví dụ đường thẳng, nhà đến cơ quan | issue slice `01:00:18` has no commute example; this claim was already re-cited in `proposed-corrections-fidelity-2026-10-22b.md` r1 | probably reviewer slice artefact; confirm r1 status first |
| c067 | Lipton: màng tế bào là bộ não | slice at `03:26:34` is not the Lipton retelling; evidence at `01:44:38` fits | probably reviewer error |
| c070 | Màng tế bào có protein và chất béo | slice `02:08:34` lacks protein; cited `01:47:06` says protein and fat | probably reviewer error |

### Omissions (7), all from `coverage_complete: false`

Nothing was verified beyond the review's own quote and timestamp. Fix type for all: add (insert a new claim or fold into an existing section) after a quote and context check; skipping is also possible.

**Higher (substantive scientific or health content; verify whether it conflicts with existing text)**

1. `01:32:46-01:33:09`: DNA structure (two nucleotide strands, A–T, G–X, hydrogen versus covalent bonds). Add. Possibly lower priority if the summary leaves out the DNA section.
2. `01:33:35-01:33:52`: DNA replication by strand separation, then cell division. Add.
3. `02:10:31`: ALA is anti-inflammatory, opposite to LA. Add; short quote, so check context.
4. `02:19:06-02:19:10`: vascular inflammation and ulceration as the mechanism being described. Add; needs context for the mechanism.

**Lower (supporting detail)**

5. `02:25:04-02:25:06`: LA goes mainly to local organs. Add or merge with c181's section.
6. `02:47:03-02:47:20`: free fatty acids in fish oil are very low, negligible. Add.
7. `03:21:34-03:21:49`: mathematician plus clinical epidemiologist building epidemic models with 20–30 variables. Add; peripheral to the Omega-3 topic.

### Concern (1)

- c181, minor: the nuance that EPA gives "một phần rất nhiều" to the brain at `02:25:27-02:25:33`. Possibly handled as an add-on claim; see p4.

## Approval

Waiting for human approval. Nothing above has been applied. Only p1 proposes a text change; p2–p4 propose no change.
