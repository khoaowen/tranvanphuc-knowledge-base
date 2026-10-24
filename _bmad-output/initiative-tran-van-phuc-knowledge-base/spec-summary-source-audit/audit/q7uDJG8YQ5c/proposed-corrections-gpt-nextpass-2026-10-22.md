# GPT fidelity next-pass: proposed corrections for 15 flags and 7 omissions, q7uDJG8YQ5c (draft, not applied)

Follows `proposed-corrections-gpt-failures-2026-10-22.md` (its p1 for c024 was applied). Review: `review.md` (GPT rerun, `fidelity-rerun-gpt-2026-10-22.md`).

Preconditions verified before analysis:

- `transcript.md` SHA-256 `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b` (matched).
- `summary.md` SHA-256 now `5565a00256b6869c74d9864d190806813ae110525a0d8414cd1b248d406bdf95`. This differs from the `a7fa8097…` hash the review is bound to, because c024 was edited after the review. Every one of the 15 flagged claim texts was re-checked and still matches `summary.md` exactly. The `review.md` result is stale and a fresh fidelity rerun is needed after any approved edits.

Nothing here is applied. Every proposal is **pending-human-approval**. No summary, transcript, review, queue_state, publishable or existing audit file was edited; nothing was committed, pushed, published, or sent to a paid service. Quote ranges below are computed with `scripts/fidelity.resolve_quote`; at least 60 seconds of transcript on each side of each passage was read.

## Key finding

Of the 15 flags, only **c144** needs a text change. The other 14 are supported in the transcript: the reviewer's own cited `evidence` contains the claimed detail, but its `issues` slice pointed at another passage that lacks it (the same pattern as c068/c073/c181). The 7 omissions are real gaps in the summary; 5 are small insertions and 2 are peripheral (candidates to skip).

## Part A: flags

| id | class | proposal |
|---|---|---|
| c010 | supported at a different timestamp | none |
| c033 | reviewer error (re-cite already applied) | none |
| c067 | reviewer error | none |
| c070 | supported at a different timestamp | none |
| c072 | reviewer error | none |
| c098 | reviewer error | none |
| c114 | reviewer error | none |
| c119 | reviewer error | none |
| c122 | supported at a different timestamp | none |
| c130 | reviewer error | none |
| c136 | reviewer error | none |
| **c144** | **partly supported** | **rewrite (add cross-reference)** |
| c167 | reviewer error | none |
| c170 | reviewer error | none |
| c178 | reviewer error | none |

### f1 (c144): add the "ở phần sau" cross-reference

- **status:** pending-human-approval
- **section:** `[02:39:11] Các tiêu chí lựa chọn sản phẩm Omega-3 chất lượng` (range `02:39:11` to `02:41:46`)
- **review status:** flag; finding: "Phần này xác nhận lời bác sĩ về hàng xách tay và bảo quản, nhưng không chứa đoạn bài đọc về cấp phép, công ty dược và tránh hàng trôi nổi."
- **current claim:** Theo bài được đọc: được cơ quan có thẩm quyền cấp phép và phân phối bởi công ty dược uy tín, không nên mua hàng xách tay hoặc hàng trôi nổi trên thị trường; riêng hàng xách tay, bác sĩ Phúc nói vẫn có thể là sản phẩm tốt, vấn đề là vận chuyển và bảo quản có đúng cách hay không.
- **class:** partly supported. Both halves exist, but in different places: the article text (cấp phép, công ty dược, không mua hàng xách tay/trôi nổi) is at `02:40:51-02:41:03`, inside this section; the doctor's remark that hand-carried goods can still be good is at `03:10:27-03:10:49`, in the later section `03:09:08`. The reviewer cited the second and flagged the first as absent, so the claim is accurate but silent about the jump. Item 4 in the same list already uses the same convention ("ở phần sau").
- **context read:** `02:39:50–02:41:20` and `03:09:30–03:11:00`.
- **minimal fix:** rewrite, inserting two words. Claim facts unchanged.
- **old text:** `riêng hàng xách tay, bác sĩ Phúc nói vẫn có thể là sản phẩm tốt`
- **new text:** `riêng hàng xách tay, ở phần sau bác sĩ Phúc nói vẫn có thể là sản phẩm tốt`
  - quote (computed `fidelity.resolve_quote` range `02:40:51-02:40:59`): "Thứ năm là chọn sản phẩm Omega 3 được các cơ quan có thẩm quyền cấp phép và được phân phối bởi Công ty dược phẩm uy tín."
  - quote (computed `fidelity.resolve_quote` range `02:41:00-02:41:03`): "Không nên mua loại Omega 3 hàng xách tay hoặc hàng trôi nổi trên thị trường."
  - quote (computed `fidelity.resolve_quote` range `03:10:30-03:10:37`): "xách tay từ nước ngoài về vẫn mua được đấy là sản phẩm tốt. Nhưng cái quá trình vận chuyển cá quá trình đem về nhà quý vị có biết bảo quản hay không?"

### Flags with no change proposed (14)

Each entry: the detail the review said was missing, where it actually is, and the evidence check. All proposals below are **pending-human-approval** (decision: no change).


- **c010** (Gödel, định lý bất toàn 1931): review said the slice `00:30:53` has no Gödel, nationality or year. Found at `00:28:36-00:28:44` (name, "nhà toán học người Đức", "Phát biểu năm 1931") and the meaning at `00:31:23-00:31:33` (the review's own evidence). Both lie in section `00:23:00`. Minor: the caption renders the name as "Golden", and "Kurt" never appears in the transcript; "Kurt Gödel" is the summary's normalisation. Optional only: drop "Kurt" if strict source-only names are wanted (old `Nhà toán học Đức Kurt Gödel`, new `Nhà toán học Đức Gödel`). Not recommended..
  - quote (computed `fidelity.resolve_quote` range `00:28:36-00:28:42`): "Định lý bất toàn là của nhà toán học người Đức Golden."
  - quote (computed `fidelity.resolve_quote` range `00:28:44`): "Phát biểu năm 1931."
  - quote (computed `fidelity.resolve_quote` range `00:31:23-00:31:29`): "Thế thì cái định lý bất toàn đó nó thể hiện rằng thế giới tự nhiên của chúng ta có rất nhiều cái vô hạn."
- **c033** (đường thẳng): the review's issue slice `01:00:18` has no commute example; the example is in its own evidence `00:58:38-00:59:04`. The re-cite of the section heading to `00:58:42` (r1 of `proposed-corrections-fidelity-2026-10-22b.md`) is already in `summary.md`. No further change.
  - quote (computed `fidelity.resolve_quote` range `00:58:38-00:58:46`): "Nếu như quý vị muốn đi từ nhà đến cơ quan mà quý vị đi bằng đường thẳng thì quý vị thất bại không bao giờ đi được."
- **c067** (Lipton: màng tế bào là bộ não): review said the `03:26:34` slice is only a restatement. Found at the review's own evidence `01:44:38-01:44:43` and `02:08:20-02:08:28`; Lipton is named at `01:44:53` and `02:08:23`..
  - quote (computed `fidelity.resolve_quote` range `01:44:38-01:44:43`): "bắt đầu ông nói rằng là dường như bộ não tế bào không phải là nhân mà bộ não tế bào là màng của tế bào."
  - quote (computed `fidelity.resolve_quote` range `02:08:20-02:08:26`): "Lúc nãy tôi có nói rằng nhà khoa học, nhà sinh học Liptông có đưa ra màng tế bào là gì?"
- **c070** (màng tế bào có protein và chất béo): review said the `02:08:34` slice lacks protein. Found at `01:47:06-01:47:13` ("Nó được cấu tạo bởi protein, được cấu tạo bởi các chất béo"), just before the cited `01:47:16-01:47:54`. Optional: widen the cited range to start at `01:47:06`..
  - quote (computed `fidelity.resolve_quote` range `01:47:06-01:47:09`): "Nó được cấu tạo bởi protein, được cấu tạo bởi các chất béo."
  - quote (computed `fidelity.resolve_quote` range `01:47:42-01:47:52`): "Ví dụ như là Omega 3. Omega 3 thì chiếm một cái thành phần rất nhiều. Omega 6 cũng là thành phần rất nhiều. Thậm chí là Omega9"
- **c072** (EPA là vàng của tim): review said the `01:31:02` slice has only DHA. Found at the review's own evidence `01:52:08-01:52:14` and `02:24:45-02:25:03`..
  - quote (computed `fidelity.resolve_quote` range `01:52:11-01:52:14`): "Vàng của tim đó chính là gì ạ? Chính là EPA."
  - quote (computed `fidelity.resolve_quote` range `02:25:01-02:25:03`): "Epa thì là của gì ạ? Của tim."
- **c098** (acetyl-CoA hai cacbon, liên kết pi dễ phá vỡ): review said the `01:29:14` slice lacks "hai cacbon". Found at `02:06:31-02:06:53` (pi bonds are unstable, broken to give acetyl-CoA burned in mitochondria) and `02:07:15-02:07:27` ("hai nguyên tử cacbon"). Wording "acetyl-CoA" is the summary's normalisation of "axetin coenzyma" (ASR)..
  - quote (computed `fidelity.resolve_quote` range `02:06:35`): "Liên kết pi là liên kết không bền vững"
  - quote (computed `fidelity.resolve_quote` range `02:07:23-02:07:27`): "có hai nguyên tử cacbon để chúng ta thực hiện cái quá trình đốt cháy cho nó dễ dàng ở trong ti thể."
- **c114** (4:1 chấp nhận, cùng lắm 5:1): review said the `02:35:45` slice has only the advice. Found at the review's own evidence `02:28:43-02:28:56` (studies/documents, 4:1 acceptable, at most 5:1, "5 chia 1 thì đã là quá nhiều rồi")..
  - quote (computed `fidelity.resolve_quote` range `02:28:43-02:28:56`): "Có những nghiên cứu và những tài liệu nói rằng chấp nhận được tỉ lệ những cái này đem chia ra thì là 4 chia 1 thì được. Cùng lắm là đến 5 chia 1. 5 chia 1 thì đã là quá nhiều rồi."
- **c119** (EPA và DHA trong cá biển sâu, gan cá): review said the `01:31:21` slice lacks EPA and liver. Found at `02:26:51-02:27:06`: question is EPA and DHA ("Thế còn EPA và DHA thì có từ gì ạ?"), answer "gan cá biển sâu hoặc là cá biển sâu ... mới tập trung nhiều"..
  - quote (computed `fidelity.resolve_quote` range `02:26:51`): "Thế còn EPA và DHA thì có từ gì ạ?"
  - quote (computed `fidelity.resolve_quote` range `02:26:59-02:27:06`): "Gan cá biển sâu hoặc là cá biển sâu đúng không ạ? thì nó mới tập trung nhiều chứ còn không thì khá là ít những cái thành phần này."
- **c122** (3 nắp chai bia, mỡ lợn bù): review said the `03:04:05` slice lacks the lard advice. Found at `02:31:09-02:31:31`, in the same passage as the 3-cap limit: "chúng ta lấy mỡ lợn chúng ta bù vào"..
  - quote (computed `fidelity.resolve_quote` range `02:30:59-02:31:05`): "mỗi một ngày chúng ta không nên ăn quá ba cái nắp chai bia về dầu ăn."
  - quote (computed `fidelity.resolve_quote` range `02:31:26-02:31:31`): "sẽ sử dụng cái ăn vượt quá thì chúng ta sẽ dừng ở con số đó và chúng ta lấy mỡ lợn chúng ta bù vào."
- **c130** (kết hợp dưỡng chất, bỏ thuốc): review said the `01:24:40` slice lacks oil control and stopping medicines. Found at the review's own evidence `02:34:44-02:35:12` (oil diet, omega 3, vitamin D, calcium, magnesium, "bỏ được thuốc tim mạch ... huyết áp ... tiểu đường ... mỡ máu ... tiến giáp")..
  - quote (computed `fidelity.resolve_quote` range `02:34:51-02:34:58`): "điều chỉnh lại chế độ ăn dầu ăn và bổ sung omega 3 thì quý vị gần như thay đổi rất ngoạn mục."
  - quote (computed `fidelity.resolve_quote` range `02:35:03-02:35:07`): "bỏ được thuốc tim mạch, bỏ được thuốc huyết áp, bỏ được thuốc tiểu đường, bỏ được thuốc mỡ máu"
- **c136** (bài báo: DHA cho trẻ/thai phụ, EPA cho nhóm khác): review said the slice was cut before the EPA group. Found at the review's own evidence `02:38:57-02:39:07` contains the full EPA sentence, and the article repeats it at `02:40:31-02:40:47`..
  - quote (computed `fidelity.resolve_quote` range `02:38:57-02:39:07`): "Với trẻ em và phụ nữ có thai thì cần ưu tiên chọn loại giàu DHA hơn. Còn với người trung niên, người cao tuổi, người mắc các bệnh lý tim mạch, huyết áp, mỡ máu thì nên chọn loại giàu EPA hơn."
- **c167** (theo dõi, nguy cơ tăng mỡ máu/gan nhiễm mỡ): review said the `03:08:37` slice lacks the warning. Found at the review's own evidence `03:01:46-03:01:57`..
  - quote (computed `fidelity.resolve_quote` range `03:01:50-03:01:57`): "có những người uống xong một thời gian chúng ta có thể bị tăng cái mỡ máu hay gan nh mỡ hay gì gì đấy lên thì chúng ta phải kiểm tra theo dõi."
- **c170** (từ 0,6 bỏ được thuốc): review said the `03:08:42` slice lacks the specific claims. Found at the review's own evidence `03:02:22-03:02:46`, which lists the medicines and symptoms verbatim..
  - quote (computed `fidelity.resolve_quote` range `03:02:22-03:02:28`): "Lên tới 0,6 nếu quý vị nào mà uống từ 0,6 trở lên thì chúng ta sẽ bỏ được nhiều những các cái sản phẩm thuốc."
  - quote (computed `fidelity.resolve_quote` range `03:02:32-03:02:34`): "Tôi thấy rất nhiều người bỏ được."
- **c178** (mua ở nhà thuốc uy tín, không tích trữ): review said the `03:10:17` slice lacks the stockpiling advice. Found at the review's own evidence `03:11:51-03:12:02`; the licence advice is at `03:10:17-03:10:24`..
  - quote (computed `fidelity.resolve_quote` range `03:11:51-03:11:54`): "Và tốt nữa cái là chúng ta đừng mua quá nhiều."
  - quote (computed `fidelity.resolve_quote` range `03:11:56-03:12:00`): "Có người mua đến hàng chục hộp về để sẵn đấy xong uống dần chúng ta không bảo quản được."

For c067 and c033 the review's own evidence is enough. For the rest, the old/new text is `n/a`.

## Part B: omissions

For each, the passage was checked against `summary.md` (keyword search for the topic found no existing coverage except where noted). Every insertion is a pure addition: the old text is an exact anchor already in `summary.md` and the new text repeats it unchanged with the addition. All quotes below resolve in the transcript. Omissions 1–2 and 7 are off the Omega-3 thread; skipping them is a legitimate choice and is marked so.


### o1: ADN structure (skip candidate)

- **status:** pending-human-approval
- **section:** `[01:25:23] Vai trò của DHA trong cá biển đối với tế bào não`
- **source range:** `01:32:46-01:33:09 and 01:33:35-01:33:52 (omissions 1 and 2 are one recap, combined)`
- **class:** real omission; fix type add
- **why:** Combines the two DNA omissions into one paragraph so the recap reads as one idea. Setup for the later nucleus-versus-membrane argument, but not about Omega-3. The caption 'duy truyền' is ASR for 'di truyền'. Approve, or skip both.
- **old text (anchor):** `albumin là chất rất quan trọng nhưng vì thực hiện quá nhiều chức năng nên rất ít được dành cho não.`
- **new text:** `albumin là chất rất quan trọng nhưng vì thực hiện quá nhiều chức năng nên rất ít được dành cho não.\nKhi ôn lại cấu trúc tế bào, bác sĩ Phúc nhắc rằng ADN nằm trong nhân tế bào và là vật chất di truyền; ADN gồm hai chuỗi nucleotit, A bắt cặp với T và G với X, A liên kết với T bằng liên kết hydro, còn các liên kết trên mỗi mạch đơn là liên kết cộng hóa trị. Khi tế bào phát triển, các mạch tách ra thành mạch đơn rồi lấy nucleotit ở môi trường để tổng hợp phân tử ADN khác; một phân tử ADN tạo ra hai phân tử ADN, rồi tế bào phân chia.`
  - quote (computed `fidelity.resolve_quote` range `01:32:32-01:32:36`): "ADN ở bên trong nhân tế bào chứa ADN. ADN là vật chất duy truyền."
  - quote (computed `fidelity.resolve_quote` range `01:32:48-01:32:50`): "Có các nucleotit là A >> đi với T"
  - quote (computed `fidelity.resolve_quote` range `01:32:56`): "G đi với X."
  - quote (computed `fidelity.resolve_quote` range `01:33:08-01:33:09`): "Liên kết cộng hóa trị."
  - quote (computed `fidelity.resolve_quote` range `01:33:35-01:33:40`): "Tách ra thành mạch đơn sau đó nó lại lấy nucleotit ở môi trường để nó tổng hợp phân tử ADN khác."

### o3: ALA chống viêm, đối lập LA

- **status:** pending-human-approval
- **section:** `[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm`
- **source range:** `02:10:17-02:10:31`
- **class:** real omission; fix type add
- **why:** The captions give 'Alla' both as anti-inflammatory (`02:10:31`) and as inflammatory (`02:10:53`), so the first most likely means ALA and the second AA. Both labels are quoted as captioned, with the uncertainty kept. Needs a human audio check before approval; if audio disagrees, reword or skip.
- **old text (anchor):** `chất mà caption ghi là 'Alla' thì gây viêm (có thể là AA, phiên âm không rõ);`
- **new text:** `bác sĩ Phúc nói LA gây viêm còn ALA chống viêm (caption ghi 'la viêm còn Alla là chống viêm'); chất mà caption ghi là 'Alla' ở câu sau thì gây viêm (có thể là AA, phiên âm không rõ);`
  - quote (computed `fidelity.resolve_quote` range `02:10:31`): "la viêm còn Alla là chống viêm."
  - quote (computed `fidelity.resolve_quote` range `02:10:50-02:10:53`): "Còn cái Alla này thì nó lại gây viêm."

### o4: Viêm loét mạch máu

- **status:** pending-human-approval
- **section:** `[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm`
- **source range:** `02:19:06-02:19:10`
- **class:** real omission; fix type add
- **why:** The doctor lists blood-vessel inflammation and ulceration among the effects of excess omega-6, before muscle, nerve, brain and eye effects. The bullet already lists the later ones in that order. 'nó' refers to the excess just discussed at `02:19:00-02:19:06`.
- **old text (anchor):** `- Các cơ quan khác: thoái hóa chất trắng ở não,`
- **new text:** `- Các cơ quan khác: viêm loét mạch máu, thoái hóa chất trắng ở não,`
  - quote (computed `fidelity.resolve_quote` range `02:19:06-02:19:10`): "Tiếp theo là nó đi các cái nơi ví dụ nó vào trong mạch máu của chúng ta nó gây viêm loét của mạch máu ra."

### o5: LA dành cho các tạng địa phương

- **status:** pending-human-approval
- **section:** `[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn`
- **source range:** `02:25:04-02:25:06`
- **class:** real omission; fix type add
- **why:** Sits directly before the sentence already summarised (`02:25:15`). The caption spells it 'La' after `02:24:21`'s 'La'/'GLA' pairing, so LA is likely but the hedge is kept.
- **old text (anchor):** `Bác sĩ Phúc còn nói nếu DHA và EPA thừa thì có thể dành cho gan, mật, tụy, lách và thận ([02:25:15](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=8715s)).`
- **new text:** `Bác sĩ Phúc nói caption ghi 'La' (có thể là LA, Omega-6) chủ yếu dành cho các tạng địa phương ([02:25:04](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=8704s)). Bác sĩ Phúc còn nói nếu DHA và EPA thừa thì có thể dành cho gan, mật, tụy, lách và thận ([02:25:15](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=8715s)).`
  - quote (computed `fidelity.resolve_quote` range `02:25:04-02:25:06`): "La thì dành cho các cái tạng địa phương là chính."

### o6: Axit béo tự do trong dầu cá

- **status:** pending-human-approval
- **section:** `[02:46:03] Phân biệt các loại dầu cá Omega-3: TG, EE và rTG`
- **source range:** `02:47:03-02:47:20`
- **class:** real omission; fix type add
- **why:** Fits the section's TG topic. 'Chủ yếu là triglycerit' is `02:47:24-02:47:30`.
- **old text (anchor):** `Bác sĩ Phúc phân loại 3 dạng dầu cá:`
- **new text:** `Bác sĩ Phúc nói trong dầu cá, omega 3 tồn tại chủ yếu ở dạng triglycerit (TG); ngoài ra còn có axit béo tự do nhưng hàm lượng vô cùng thấp, không đáng kể. Bác sĩ Phúc phân loại 3 dạng dầu cá:`
  - quote (computed `fidelity.resolve_quote` range `02:47:00-02:47:06`): "Một là tồn tại ở dạng TG là triggerlycerit này là chính. Hai là tồn tại ở axit béo tự do."
  - quote (computed `fidelity.resolve_quote` range `02:47:16-02:47:20`): "Thì cái hàm lượng axit béo tự do này vô cùng thấp, không đáng kể."

### o7: Mô hình toán học chống dịch (skip candidate)

- **status:** pending-human-approval
- **section:** `[03:19:08] Bộ 7 vi chất dinh dưỡng và xét nghiệm Omega-3 trong tế bào hồng cầu`
- **source range:** `03:20:35-03:21:49`
- **class:** real omission; fix type add
- **why:** Peripheral to Omega-3 but a source-stated example, and the summary has no Covid mention (keyword search). It starts the passage that leads into the red-cell test, and sits before the `03:26` red-cell content the anchor line summarises. 'Nhà lãnh đạo' paraphrases 'nguyên thủ quốc gia'; use the original wording if preferred. Approve or skip.
- **old text (anchor):** `Bác sĩ Phúc nói ở một số nước phát triển có xét nghiệm EPA và DHA trong tế bào hồng cầu`
- **new text:** `Bác sĩ Phúc nói trong đại dịch Covid, ở các nước phát triển, nhà lãnh đạo luôn có một nhà toán học và một nhà dịch tễ học lâm sàng đi cùng; hai người cùng lập mô hình toán học phòng chống dịch với hàm nhiều biến, có khi tới 20 hoặc 30 biến, để can thiệp vào từng biến một cách hiệu quả và khoa học, và ông dùng đó làm ví dụ về ứng dụng kiến thức toán vào cuộc sống.\nBác sĩ Phúc nói ở một số nước phát triển có xét nghiệm EPA và DHA trong tế bào hồng cầu`
  - quote (computed `fidelity.resolve_quote` range `03:21:34-03:21:39`): "Hai người đấy sẽ cùng nhau để lập lên những mô hình chống dịch bằng toán học."
  - quote (computed `fidelity.resolve_quote` range `03:21:39-03:21:49`): "những các cái hàm số đá biến mà những hàm lên tới 20 biến, 30 biến để người ta can thiệp vào từng biến một nó mang tính hiệu quả và khoa học."

## Notes

- Omissions 1 and 2 are combined into one proposal (o1), so the 7 review omissions map to o1 (items 1+2), o3, o4, o5, o6, o7; there is no o2 by design.
- Every "new text" above that contains `\n` means a line break at that point.
- After any approved edits, `summary.md` needs a fresh fidelity rerun and a source-audit coverage check; the current `review.md` is stale (bound to `a7fa8097…`).

## Approval

Waiting for human approval. Nothing above has been applied. Only f1 (c144) plus o1, o3, o4, o5, o6 and o7 propose text changes; o1 and o7 are skip candidates.

