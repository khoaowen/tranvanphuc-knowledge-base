# PR #9 — human review checklist

**Purpose:** decide whether to accept this audit record and whether to approve any proposed correction. This is the short review file. The previous exhaustive pack is retained as [`PR9-full-decision-pack.md`](PR9-full-decision-pack.md).

**Video:** [open on YouTube](https://www.youtube.com/watch?v=V-Qfwjo28Zg). Every ▶ link starts five seconds before the cited caption.

**Important:** the “before” text is from the historical summary SHA `fbae11bf…a98203c`, deleted from `videos/` by `4e31e57`. The “after” text is only a proposal; all 63 remain `pending-human-approval`.

## First: audit-record decisions

### 1. What should these corrections apply to?
- **Current state:** the historical summary they correct is deleted; a regenerated summary gets different claim IDs.
- **Choose one:** (a) restore and correct that historical summary, (b) regenerate and use these only as an audit checklist, or (c) regenerate and reuse individual corrections only where the same claim reappears.

### 2. Is one-pass coverage acceptable?
- **Current state:** pass 1 checked all 554 claims. A blind second pass checked all 63 non-supported claims plus only 30 of 491 supported claims. **461 supported claims have only pass-1 review.**
- **Evidence:** 24 pass-1/pass-2 disagreements are listed below. A separate 25-claim spot check found no additional error.
- **Choose one:** accept this as a mergeable audit record; require a larger supported-claim sample; or require a full second pass.

### 3. Is the omissions result adequate?
- **Current state:** 47 omissions were consolidated from 23 range-restricted pass-1 reads, not from one dedicated sequential full-transcript omissions pass.
- **Choose one:** accept it; or require the dedicated full omission pass before calling ticket 2.2 complete.

### 4. Confirm the 24 adjudicated pass disagreements
The final class below is what the audit will record. Use the video link and full-context link to accept or change it.

| Claim | Pass 1 | Blind pass 2 | Recorded final | Review |
|---|---|---|---|---|
| c003 | `attribution_qualification` | `supported` | **`supported`** | [▶ 00:07:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=429s) · [full transcript context](PR9-full-decision-pack.md#c003) |
| c013 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 00:06:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=398s) · [full transcript context](PR9-full-decision-pack.md#c013) |
| c034 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 00:16:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=984s) · [full transcript context](PR9-full-decision-pack.md#c034) |
| c054 | `mismatch` | `supported` | **`mismatch`** | [▶ 00:45:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2754s) · [full transcript context](PR9-full-decision-pack.md#c054) |
| c103 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 01:06:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3978s) · [full transcript context](PR9-full-decision-pack.md#c103) |
| c111 | `mismatch` | `unresolved` | **`unresolved`** | [▶ 01:13:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4423s) · [full transcript context](PR9-full-decision-pack.md#c111) |
| c121 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 01:20:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4797s) · [full transcript context](PR9-full-decision-pack.md#c121) |
| c125 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s) · [full transcript context](PR9-full-decision-pack.md#c125) |
| c135 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 01:27:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5239s) · [full transcript context](PR9-full-decision-pack.md#c135) |
| c166 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 02:37:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9417s) · [full transcript context](PR9-full-decision-pack.md#c166) |
| c177 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 02:41:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9688s) · [full transcript context](PR9-full-decision-pack.md#c177) |
| c182 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 02:42:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9765s) · [full transcript context](PR9-full-decision-pack.md#c182) |
| c193 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 02:46:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9999s) · [full transcript context](PR9-full-decision-pack.md#c193) |
| c235 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 01:52:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6755s) · [full transcript context](PR9-full-decision-pack.md#c235) |
| c254 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 01:21:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4897s) · [full transcript context](PR9-full-decision-pack.md#c254) |
| c282 | `supported` | `attribution_qualification` | **`attribution_qualification`** | [▶ 02:18:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8297s) · [full transcript context](PR9-full-decision-pack.md#c282) |
| c294 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 02:44:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9835s) · [full transcript context](PR9-full-decision-pack.md#c294) |
| c352 | `mismatch` | `supported` | **`mismatch`** | [▶ 03:23:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12200s) · [full transcript context](PR9-full-decision-pack.md#c352) |
| c377 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 03:25:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12338s) · [full transcript context](PR9-full-decision-pack.md#c377) |
| c456 | `attribution_qualification` | `unresolved` | **`unresolved`** | [▶ 05:22:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19340s) · [full transcript context](PR9-full-decision-pack.md#c456) |
| c471 | `mismatch` | `supported` | **`mismatch`** | [▶ 04:31:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16299s) · [full transcript context](PR9-full-decision-pack.md#c471) |
| c478 | `mismatch` | `supported` | **`mismatch`** | [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s) · [full transcript context](PR9-full-decision-pack.md#c478) |
| c500 | `attribution_qualification` | `supported` | **`attribution_qualification`** | [▶ 04:51:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17512s) · [full transcript context](PR9-full-decision-pack.md#c500) |
| c509 | `attribution_qualification` | `unresolved` | **`attribution_qualification`** | [▶ 05:01:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18077s) · [full transcript context](PR9-full-decision-pack.md#c509) |

### 5. Confirm these special cases

| Decision | What you need to decide | Review items |
|---|---|---|
| Removal proposals | Whether to remove/relabel a summary sentence rather than merely reword it. | c456, c541, c172, c373 (cards below) |
| `unresolved` vs `mismatch` | c456 and c541 are absent/editorial rather than supported by speech. Keep the cautious `unresolved` class, or call them `mismatch`? | c456, c541 |
| Caption/audio ambiguity | Whether to preserve the caption literally or write what is audible. | c471 (`GSGS`), c127 (iron salt), c201 (UI numbers), c377 (country), c070/c488 (speaker), c111 (body site) |
| Safety | Approve only after listening; c401 changes breathing guidance. | c401; also review omissions o19–o22 in the full pack |
| Numbering consistency | If c478 is accepted, decide whether c479–c482 must change too. | c478–c482 in full pack |

### 6. Decide status
- Keep ticket 2.2 **in review** until items 1–3 are accepted, or accept it as a merged audit record with the above caveats.
- Separately resolve the plan conflict: the initiative says “no git commit”; ticket 2.2 says to commit logical batches.

## Correction decisions (63)
For each: **Accept / edit / reject.** “Before” is the historical summary; “after” is the audit proposal. The short quote is verbatim from the transcript. Use the full-context link when the short quote does not settle it.


### c013 — `attribution_qualification`
**Review:** [▶ 00:06:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=398s) · [full transcript context](PR9-full-decision-pack.md#c013)  
**Before:** Hình thành gốc tự do bắt đầu từ việc các chất xâm nhập vào cơ thể.  
**After:** Bác sĩ nói "có thể nói rằng" hầu hết các loại bệnh tật có con đường đi từ quá trình các chất xâm nhập vào cơ thể, hình thành gốc tự do, rồi cuối cùng phát sinh bệnh tật; còn gốc tự do thì ông nói có hai nguồn, trong đó có con đường nội sinh.  
**Why:** The sentence describes the path of disease, not free-radical formation in general. The doctor separately names an endogenous source, so the summary's general statement is too broad.
**Transcript evidence:** [▶ 00:06:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=398s) “từ quá trình khi mà các cái chất nó xâm nhập vào cơ thể chúng ta, hình thành ra gốc tự do và đi trên cái con đường của gốc tự do” · [▶ 00:09:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=540s) “gốc tự do này nó được phát sinh từ đâu? Nó có hai nguồn.” · [▶ 00:06:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=389s) “Có thể nói rằng hầu hết tất cả các cái loại bệnh tật”

### c034 — `attribution_qualification`
**Review:** [▶ 00:16:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=984s) · [full transcript context](PR9-full-decision-pack.md#c034)  
**Before:** Chất béo chuyển hóa được mô tả là chất béo bị đốt cháy quá mức, ví dụ đồ chiên rán, hoặc dầu thực vật bị dùng sai khi rán, dẫn đến chuyển hóa thành chất béo trung gian.  
**After:** Chất béo chuyển hóa được bác sĩ mô tả là những chất béo "bị đốt cháy là dở dở đi" (bản ghi âm ghi như vậy, nghĩa chưa rõ), ví dụ đồ chiên rán; còn dầu thực vật dùng sai khi rán thì chuyển hóa thành chất béo trung gian.  
**Why:** 'Quá mức' (excessive) is not what the caption says. The caption is garbled, so the proposal keeps it as spoken and marks it unclear instead of interpreting it.
**Transcript evidence:** [▶ 00:16:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=984s) “những chất béo mà khi chúng ta bị đốt cháy là dở dở đi ấy. Ví dụ như là đồ chiên dàn chẳng hạn.” · [▶ 00:16:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=993s) “là dầu thực vật mà chúng ta thực hiện trên dán thì nó sẽ chuyển hóa thành cái chất béo trung gian.”

### c045 — `attribution_qualification`
**Review:** [▶ 00:38:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2305s) · [full transcript context](PR9-full-decision-pack.md#c045)  
**Before:** Theo bài, H₂O₂ được cho vào vết thương để phá hủy mô hoại tử, virus và vi khuẩn, làm sạch vết thương, và sủi bọt.  
**After:** Theo bài, H₂O₂ được cho vào vết thương; bác sĩ nói nó phá hủy các mô, phá hủy virus vi khuẩn, làm sạch vết thương và sủi bọt.  
**Why:** The transcript says 'các cái mô' (tissues). 'Hoại tử' (necrotic) is a qualifier the summary added.
**Transcript evidence:** [▶ 00:38:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2305s) “thành phần mà tại sao oxy già chúng ta sẽ cho vào những vết thương.” · [▶ 00:38:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2312s) “nó phá hủy các cái mô, nó phá hủy virus vi khuẩn, nó làm sạch những cái vết thương” · [▶ 00:38:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2319s) “trên sủi bọt lên.”

### c054 — `mismatch`
**Review:** [▶ 00:45:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2754s) · [full transcript context](PR9-full-decision-pack.md#c054)  
**Before:** Ozon không cướp trực tiếp như các gốc khác, mà xen vào các phân tử oxy khác, tạo thành cuộc "tình tay ba", và từ đó sinh ra gốc tự do.  
**After:** Ozon được mô tả là có thêm một oxy nữa xen vào oxy hai nguyên tử, thành cuộc "tình tay ba"; ozon không đi ăn cướp, nhưng gặp chỗ nào xen được thì xen vào câu chuyện của các gia đình khác, và từ đó cũng tạo ra một gốc tự do.  
**Why:** In the transcript the love triangle is ozone itself (a third oxygen joining O2). Ozone interjects into other 'families' only afterward; the summary moves the metaphor to that later step.
**Transcript evidence:** [▶ 00:45:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2754s) “Thế bây giờ có thêm một cái oxy nữa nó xen vào đây trở thành cuộc tình tay ba.” · [▶ 00:47:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2823s) “không đi ăn cướp nhưng cái này nó đi nó xen vào câu chuyện của các gia đình khác” · [▶ 00:46:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2804s) “Từ đây nó sẽ dẫn tới là ozon này cứ đi gặp bất cứ chỗ nào mà có thể xen được vào là nó xen.” · [▶ 00:47:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2819s) “Đây là cái lý do mà cũng lại tạo ra một cái gốc tự do.”

### c066 — `attribution_qualification`
**Review:** [▶ 00:53:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3224s) · [full transcript context](PR9-full-decision-pack.md#c066)  
**Before:** Bác sĩ ví màng tế bào như một bãi xăng, nên một gốc tự do cũng đủ làm sụp đổ hệ thống.  
**After:** Bác sĩ thuật lại rằng người ta ví màng tế bào như một bãi xăng, nên chỉ cần một gốc tự do tấn công màng tế bào là ngay lập tức sụp đổ hệ thống.  
**Why:** The doctor reports the comparison as 'người ta ví rằng' (others compare it); the summary credits it to him.
**Transcript evidence:** [▶ 00:53:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3224s) “người ta ví rằng màng tế bào nó giống như là một bãi” · [▶ 00:53:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3228s) “Vậy chỉ cần một gốc tự do tấn công màn tế bào ngay lập tức nó sụp đổ hệ”

### c068 — `attribution_qualification`
**Review:** [▶ 00:53:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3198s) · [full transcript context](PR9-full-decision-pack.md#c068)  
**Before:** Bác sĩ nói hậu quả có thể là bệnh mãn tính, lão hóa và nhiều bệnh khác.  
**After:** Bác sĩ nói tế bào hoại tử, tế bào chết đi thì sẽ sinh ra bệnh mãn tính, sẽ bị lão hóa và sẽ bị đủ thứ bệnh.  
**Why:** Softened hedge only: the doctor says 'sẽ' (will), the summary says 'có thể'. The proposal restores his wording.
**Transcript evidence:** [▶ 00:53:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3198s) “sinh ra bệnh mãn tính, chúng ta sẽ bị lão hóa” · [▶ 00:53:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3202s) “chúng ta sẽ bị đủ thứ bệnh trên” · [▶ 00:53:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3196s) “tế bào chết đi tức là chúng ta sẽ sinh ra bệnh mãn tính”

### c070 — `mismatch`
**Review:** [▶ 00:55:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3310s) · [full transcript context](PR9-full-decision-pack.md#c070)  
**Before:** Oxy hoặc ozon sau đó xâm nhập vào để tạo thành POOH, và protein này giống hệt protein bị hỏng.  
**After:** Protein có dấu chấm bị oxy lợi dụng xâm nhập, hoặc ozon nhường oxy vào, để thành PO trừ; PO trừ lại cướp H+ để tạo thành POOH. Protein đi theo con đường giống hệt lipit (câu này đứng sau dấu đổi người nói trong bản ghi âm).  
**Why:** 'Giống hệt protein bị hỏng' is not in the transcript: the comparison is to the lipid pathway. The summary also skips the PO- step before POOH. The 'y xì như lipit' line follows a speaker-change mark, so the proposal names no speaker for it. Human to confirm the speaker.
**Transcript evidence:** [▶ 00:55:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3310s) “hoặc là ozon nó nhường oxy vào đây để trở thành gì ạ? PO tr-” · [▶ 00:55:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3324s) “Để tạo thành là POOH giống hệt protein” · [▶ 00:55:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3331s) “y xì như lipit và protein cũng lại giống” · [▶ 00:55:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3317s) “Sau đó PO trừ lại không đang thiếu vật liệu để xây phòng lại cướp gì ạ? Cướp H+ đúng không ạ?”

### c079 — `attribution_qualification`
**Review:** [▶ 00:58:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3504s) · [full transcript context](PR9-full-decision-pack.md#c079)  
**Before:** Đột biến gen có thể gây bệnh hiếm và ung thư.  
**After:** Đột biến gen sẽ gây ra bệnh nguy hiểm, bệnh hiếm và ung thư.  
**Why:** Softened hedge: the doctor says 'sẽ gây ra', the summary says 'có thể gây'. 'Bệnh nguy hiểm' was also dropped. The proposal restores his wording.
**Transcript evidence:** [▶ 00:58:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3504s) “mà đột biến gen này thì sẽ gây ra một là” · [▶ 00:58:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3507s) “bệnh nguy hiểm, bệnh hiếm đúng không ạ?” · [▶ 00:58:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3509s) “Hai là gây ra gì ạ? Ung thư.”

### c084 — `attribution_qualification`
**Review:** [▶ 00:59:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3569s) · [full transcript context](PR9-full-decision-pack.md#c084)  
**Before:** Bác sĩ nói nếu chỉ đọc tài liệu thông thường thì khó hiểu, nhưng cách phân tích này giúp dễ nhớ hơn.  
**After:** Bác sĩ nói nếu tự đi tìm đọc về gốc tự do thì "chắc chắn" sẽ không thể hiểu được vì nó rất rắc rối, nhưng nếu hiểu theo cách ông phân tích thì từ nay sẽ nhớ được.  
**Why:** Softened hedge: 'chắc chắn ... sẽ không thể hiểu được' became 'khó hiểu'. 'Tài liệu thông thường' is the summary's own wording.
**Transcript evidence:** [▶ 00:59:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3569s) “gốc tự do là gì thì chắc chắn quý vị sẽ” · [▶ 00:59:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3572s) “không thể hiểu được và Khánh lành cũng” · [▶ 00:59:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3582s) “nay trở đi chúng ta sẽ nhớ được gốc tự” · [▶ 00:59:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3575s) “bởi vì nó sẽ rất rắc rối”

### c103 — `attribution_qualification`
**Review:** [▶ 01:06:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3978s) · [full transcript context](PR9-full-decision-pack.md#c103)  
**Before:** Bác sĩ nói glutathion đang được quảng cáo là chất chống oxy hóa giúp trắng da và nhiều người mua về bổ sung.  
**After:** Bác sĩ nói người ta quảng cáo rất nhiều về glutathion; người đáp là Khánh Lành nêu chủ yếu với tác dụng là chất chống oxy hóa giúp trắng da, bác sĩ xác nhận "giúp trắng da" và nói rất nhiều người mua về, nhất là chị em phụ nữ.  
**Why:** Speaker split: the antioxidant wording is the host's answer after a speaker change. The doctor confirms only whitening and that many people buy it.
**Transcript evidence:** [▶ 01:06:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3978s) “ta quảng cáo rất nhiều về glutathion để” · [▶ 01:06:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3983s) “Chủ yếu là với tác dụng là chất chống” · [▶ 01:06:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3989s) “nhiều mu người mua cái sản phẩm này về” · [▶ 01:06:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3987s) “Giúp trắng da đúng không ạ?”

### c105 — `attribution_qualification`
**Review:** [▶ 01:07:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4030s) · [full transcript context](PR9-full-decision-pack.md#c105)  
**Before:** Bác sĩ cũng nói nếu cơ thể cạn kiệt glutathion thì có thể sinh ra nhiều bệnh mãn tính, một số bệnh ung thư và lão hóa nhanh.  
**After:** Bác sĩ cũng nói một khi đã cạn kiệt glutathion thì sẽ sinh ra một loạt bệnh, trong đó có vô cùng nhiều các bệnh mãn tính, có những bệnh ung thư, có những bệnh nguy hiểm, và đặc biệt lão hóa rất nhanh.  
**Why:** Softened hedge: 'sẽ sinh ra' became 'có thể sinh ra', and 'bệnh nguy hiểm' was dropped. The proposal restores his wording.
**Transcript evidence:** [▶ 01:07:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4030s) “cạn kiệt glutathon thì chúng ta sẽ sinh” · [▶ 01:07:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4034s) “nhiều các bệnh mãn tính, có những bệnh” · [▶ 01:07:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4040s) “biệt chúng ta lão hóa rất nhanh.”

### c108 — `mismatch`
**Review:** [▶ 01:12:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4322s) · [full transcript context](PR9-full-decision-pack.md#c108)  
**Before:** Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào cho thấy vi chất làm giảm đường huyết.  
**After:** Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào thể hiện "ma dê" (bản ghi âm ghi như vậy) giúp làm giảm đường huyết.  
**Why:** Entity changed: the comment read out names 'ma dê', not micronutrients in general. The doctor later says the case was not only about ma dê, but that is his reply, not the head of department's statement.
**Transcript evidence:** [▶ 01:12:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4322s) “chủ nhiệm khoa em nói rằng không có cơ” · [▶ 01:12:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4324s) “chế nào thể hiện ma dê giúp làm giảm” · [▶ 02:11:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7855s) “ma dê nó không hẳn chỉ ma dê.”

### c111 — `unresolved`
**Review:** [▶ 01:13:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4423s) · [full transcript context](PR9-full-decision-pack.md#c111)  
**Before:** Họ nói đã hết đau cột sống, xương cổ, xương đùi và xương quai xanh, và không còn tê nửa người bên trái.  
**After:** Họ nói không còn đau cột sống, "xương cổ đùi" (bản ghi âm ghi như vậy, không rõ là một vị trí hay hai vị trí) và xương quai xanh, và không còn tê dọc nửa người bên trái.  
**Why:** Stays unresolved. The unpunctuated 'xương cổ đùi' could be one site or two, and the transcript does not settle it. The proposal keeps the spoken words and states the doubt.
**Transcript evidence:** [▶ 01:13:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4423s) “Tôi nhận thấy mình không còn bị đau cột” · [▶ 01:13:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4425s) “sống, xương cổ đùi và xương quai xanh” · [▶ 01:13:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4433s) “xương. Tôi cũng không còn bị tê dọc nửa”

### c121 — `attribution_qualification`
**Review:** [▶ 01:20:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4797s) · [full transcript context](PR9-full-decision-pack.md#c121)  
**Before:** Họ cũng kể đau đầu và buồn nôn khi có chu kỳ đã hết sau nhiều tháng.  
**After:** Họ cũng kể trước đây mỗi khi đến chu kỳ kinh nguyệt bị đau đầu khủng khiếp và buồn nôn; sau "năm tháng" bổ sung vi chất, họ nói đã hết đau đầu.  
**Why:** The viewer says only the headache ended, not the nausea. 'Năm tháng' became 'nhiều tháng', which changes the stated duration.
**Transcript evidence:** [▶ 01:20:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4797s) “chu kỳ kinh nguyệt là tôi bị đau đầu” · [▶ 01:20:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4822s) “năm tháng bổ sung vi chất, giờ tôi đã” · [▶ 01:20:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4824s) “hết đau đầu, hết viêm da dị ứng và hết” · [▶ 01:20:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4799s) “khủng khiếp và buồn nôn nữa”

### c125 — `attribution_qualification`
**Review:** [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s) · [full transcript context](PR9-full-decision-pack.md#c125)  
**Before:** Họ nghi ngờ thiếu sắt nhược sắc, nhưng chưa rõ chính xác.  
**After:** Họ cho rằng có lẽ vấn đề nằm ở việc thiếu sắt nhược sắc; riêng thông tin đọc được về xác hồng cầu bị phá hủy làm da có ánh vàng thì họ nói không rõ độ chính xác.  
**Why:** The doubt is misplaced: 'không rõ độ chính xác' refers to the hemolysis information the viewer read, not to the iron-deficiency suspicion, whose hedge is 'có lẽ'.
**Transcript evidence:** [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s) “nhận ra có lẽ vấn đề nằm ở việc bị thiếu” · [▶ 01:23:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4999s) “vàng. Nhưng em không rõ độ chính xác của” · [▶ 01:23:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4989s) “Em có xem một số tài liệu nói rằng khi thiếu sắt hồng cầu mỏng manh dễ bị phá hủy hàng loạt”

### c127 — `mismatch`
**Review:** [▶ 01:24:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5046s) · [full transcript context](PR9-full-decision-pack.md#c127)  
**Before:** Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ sắt II fumarat khô cùng 250 mcg vitamin B9, cùng bộ vi chất của bác sĩ.  
**After:** Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ "sắt hai xun phát khô" (bản ghi âm ghi như vậy) cùng 250 mcg vitamin B9, cùng bộ vi chất của bác sĩ.  
**Why:** Iron salt changed: the transcript says 'xun phát', the summary says 'fumarat'. Date and both amounts match.
**Transcript evidence:** [▶ 01:24:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5046s) “2026. Từ ngày 22 tháng 04 năm 2026, em” · [▶ 01:24:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5059s) “sắt chứa 50 mg sắt nguyên tố từ sắt hai xun phát khô cộng với 250 micrg vitamin”

### c135 — `attribution_qualification`
**Review:** [▶ 01:27:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5239s) · [full transcript context](PR9-full-decision-pack.md#c135)  
**Before:** Bác sĩ chẩn đoán nang dưới nhện góc tiểu cầu não trái làm dây thần kinh số năm bị chèn ép.  
**After:** Người xem kể đã chữa trị ở nhiều bệnh viện lớn tại Hà Nội, và bác sĩ ở đó (không phải bác sĩ Phúc) chẩn đoán họ bị nang dưới nhện góc tiểu cầu não trái, dây thần kinh số năm bị chèn ép dẫn đến đau nửa đầu.  
**Why:** As written, 'Bác sĩ chẩn đoán' reads as Dr. Phúc. The viewer is reporting a diagnosis from Hanoi hospitals, and Dr. Phúc later plays down the cyst.
**Transcript evidence:** [▶ 01:27:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5239s) “chữa trị ở nhiều bệnh viện lớn tại Hà Nội.” · [▶ 01:27:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5241s) “Bác sĩ chẩn đoán tôi bị nang dưới nhện góc tiểu cầu não trái. Dây thần kinh số năm bị chèn ép dẫn đến đau nửa đầu.” · [▶ 02:18:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8286s) “con nang dưới nhện và người ta đang chung sống hòa bình. Nếu chúng ta mà mổ dẫn lưu như vậy thì vô tình bệnh nhân lại thêm một cái vết mổ chứ không cần thiết.”

### c140 — `attribution_qualification`
**Review:** [▶ 01:29:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5352s) · [full transcript context](PR9-full-decision-pack.md#c140)  
**Before:** Người xem kể sau khi mệt là uống đường mía thô, và dùng lâu dài thì có khó thở, nhịp tim tăng 170 nhịp mỗi phút, tăng cân, bụng to và gan bắt đầu nhiễm mỡ.  
**After:** Người xem kể lúc mệt mỏi đã ăn hoặc uống đường mía thô, rồi lạm dụng; sau 3 tháng dùng lượng đường quá nhiều thì bị khó thở, nhịp tim tăng lên 170 nhịp một phút, tăng cân, bụng to và gan bắt đầu nhiễm mỡ.  
**Why:** 'Sau 3 tháng' and the excess amount became 'dùng lâu dài', and 'ăn hoặc uống' was narrowed to 'uống'.
**Transcript evidence:** [▶ 01:29:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5352s) “Trong lúc mệt mỏi, tôi ăn hoặc là uống đường mía thô” · [▶ 01:29:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5364s) “Sau 3 tháng sử dụng lượng đường quá nhiều” · [▶ 01:29:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5369s) “Tôi bị khó thở, nhịp tim tăng lên 170 nhịp một phút” · [▶ 01:29:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5357s) “Từ đó tôi lạm dụng.”

### c144 — `attribution_qualification`
**Review:** [▶ 01:31:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5479s) · [full transcript context](PR9-full-decision-pack.md#c144)  
**Before:** Họ kể vẫn còn nhịp tim nhanh và thỉnh thoảng bị bóng đè khi ngủ.  
**After:** Họ kể nhịp tim đôi lúc bị nhanh và khi ngủ thỉnh thoảng vẫn bị bóng đè.  
**Why:** Hedge dropped: heart rate is fast 'đôi lúc' (at times), while 'vẫn còn nhịp tim nhanh' reads as constant.
**Transcript evidence:** [▶ 01:31:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5479s) “Nhịp tim đôi lúc bị nhanh và khi ngủ thỉnh thoảng vẫn bị hiện tượng bóng đè.”

### c156 — `mismatch`
**Review:** [▶ 02:31:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9066s) · [full transcript context](PR9-full-decision-pack.md#c156)  
**Before:** Bản ghi âm ghi là "K G3" và "glycerin" cho cùng cơ chế này; cơ chế liệt vận động không được kịp nhả.  
**After:** Bản ghi âm ghi là "K G3" và "glycerin" cho cơ chế này; khi chuyển vào giấc ngủ mà việc làm liệt vận động không làm được kịp thời ("cái phanh này không được kịp thời"), người ngủ sẽ nói và vận động trong mơ.  
**Why:** Wrong scenario: going into sleep, the brake is not applied in time. 'Không kịp nhả' (not released) belongs to the separate sleep-to-wake case, which c157 already covers.
**Transcript evidence:** [▶ 02:31:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9066s) “G3 và tiết ra glycerin này nó lại không” · [▶ 02:31:16](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9071s) “Tức là cái phanh này không được kịp” · [▶ 02:32:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9138s) “lại không có phanh.” · [▶ 02:31:31](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9086s) “Nói trong mơ và vận động trong mơ.”

### c161 — `attribution_qualification`
**Review:** [▶ 02:34:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9264s) · [full transcript context](PR9-full-decision-pack.md#c161)  
**Before:** Khi xảy ra, hít một hơi thật sâu rồi thở ra từ khoảng 15 đến 30 giây, sau đó lấy lại bình tĩnh thì sẽ thoát khỏi tình trạng này.  
**After:** Bác sĩ nói hầu hết tài liệu khoa học khuyên khi xảy ra thì hít một hơi thật sâu, rồi thở ra từ 15 đến 30 giây ("đại ý"), sau đó lấy lại bình tĩnh thì thoát; nhưng ông nói "cứ khuyên nhau thế thôi nhưng mà ai cũng sợ", và sau đó nhận xét nói thế thì rất đơn giản.  
**Why:** The summary states this as plain advice. The doctor reports it as what the literature says, doubts it, and later calls it too simple.
**Transcript evidence:** [▶ 02:34:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9264s) “bóng đè này hít một hơi thật sâu quãng” · [▶ 02:34:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9267s) “sau đó thì bắt đầu thở ra từ 15 đến 30” · [▶ 02:34:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9277s) “khuyên nhau thế thôi nhưng mà ai cũng sợ” · [▶ 02:34:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9253s) “hầu hết tất cả các tài liệu khoa học đều nói rằng đây là hiện tượng không có gì đáng ngại cả.” · [▶ 02:43:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9803s) “hướng dẫn nhau hít một hơi thở thật sâu rồi chúng ta bình tĩnh lại. Nói thế thì nó rất là đơn giản”

### c162 — `attribution_qualification`
**Review:** [▶ 02:34:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9284s) · [full transcript context](PR9-full-decision-pack.md#c162)  
**Before:** Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, tác dụng chủ yếu là trấn an tâm lý, không phải hiệu quả thực sự.  
**After:** Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, về mặt tinh thần để trấn an tâm lý; ông nói "chứ còn nó hiệu quả thực sự thì nó không hẳn chủ yếu là trấn an tâm lý" (bản ghi âm ghi như vậy) rồi đi sâu hơn vào nguyên nhân.  
**Why:** Hedge hardened: 'không hẳn' became a flat 'không phải hiệu quả thực sự'. The spoken sentence is itself unclear, so the proposal quotes it instead of interpreting it.
**Transcript evidence:** [▶ 02:34:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9284s) “số người đi ngủ sẽ đặt con dao ở dưới” · [▶ 02:35:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9296s) “là liệu pháp giả dược.” · [▶ 02:35:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9304s) “hẳn chủ yếu là trấn an tâm lý.” · [▶ 02:35:06](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9301s) “Chứ còn nó hiệu quả thực sự thì nó không hẳn chủ yếu là trấn an tâm lý.”

### c166 — `attribution_qualification`
**Review:** [▶ 02:37:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9417s) · [full transcript context](PR9-full-decision-pack.md#c166)  
**Before:** Lời khuyên là sống bình thường, làm được gì thì làm, không làm được thì thôi, và không tiếp nhận năng lượng xấu như đọc tin tiêu cực quá nhiều.  
**After:** Bác sĩ khuyên "aq quy một chút": cuộc sống diễn ra bình thường, cái gì làm được thì làm, không làm được thì thôi. Ông kể bản thân không tiếp cận năng lượng xấu vào cơ thể, còn thông tin xấu trên mạng xã hội thì ông chỉ đọc lướt qua để xem hôm nay xảy ra chuyện gì.  
**Why:** The news part is the doctor's own habit, and the summary turns it into general advice. 'Quá nhiều' (too much) is not said.
**Transcript evidence:** [▶ 02:37:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9417s) “ta làm được thì làm, còn không làm được” · [▶ 02:37:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9447s) “tiếp cận những cái năng lượng xấu vào cơ” · [▶ 02:37:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9451s) “đọc những cái thông tin xấu. Tôi đọc chỉ” · [▶ 02:37:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9451s) “Tôi đọc chỉ là để tôi lướt qua tôi xem ngày hôm nay đang xảy ra chuyện gì.”

### c172 — `attribution_qualification`
**Review:** [▶ 02:40:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9598s) · [full transcript context](PR9-full-decision-pack.md#c172)  
**Before:** Bác sĩ nói những người bị táo bón, hội chứng ruột kích thích, viêm dạ dày ruột không tiết được serotonin, nên dễ bị bóng đè khi mơ màng lúc ngủ, thức.  
**After:** Bác sĩ nói một số những người bị táo bón, bị hội chứng ruột kích thích, bị dạ dày ruột thì không thể tiết được serotonin, nên cứ mơ màng, thức ngủ thì rất dễ bị bóng đè.  
**Why:** Qualifier dropped: 'một số' (some) was removed, so the claim covers everyone with these conditions.
**Transcript evidence:** [▶ 02:40:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9598s) “thấy rằng một số những người mà bị táo” · [▶ 02:40:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9604s) “dày ruột thì nó không thể tiết được” · [▶ 02:40:16](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9611s) “dễ bị bóng đè.”

### c176 — `mismatch`
**Review:** [▶ 02:41:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9669s) · [full transcript context](PR9-full-decision-pack.md#c176)  
**Before:** Kẽm là yếu tố hợp đồng với glutathione: nếu thiếu kẽm thì glutathione không có giá trị, vì selen là enzyme chuyển hóa gốc tự do.  
**After:** Vitamin C, vitamin E, kẽm và selen (bản ghi âm ghi là "cen") là những yếu tố hợp đồng với glutathione. Nếu thiếu kẽm thì glutathione chẳng có giá trị. Selen quá quan trọng trong chuyện là enzyme để chuyển hóa gốc tự do; nếu không có selen thì glutathione vất đi.  
**Why:** The transcript makes two separate statements. The summary invents a causal link (zinc matters 'vì selen...') and says selenium 'is' the enzyme.
**Transcript evidence:** [▶ 02:41:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9669s) “là những cái yếu tố hợp đồng với lại glutathion.” · [▶ 02:41:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9673s) “Nếu bây giờ các bạn thiếu kẽm thì glutathion chẳng có giá trị. Cen quá quan trọng trong cái chuyện là enzyme để mà chuyển hóa gốc tự do. Nếu không có cen thì glutat vất đi.” · [▶ 02:41:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9658s) “Tôi nhắc lại là vitamin C là một này, E là hai này, kẽm là ba này, cen là 4 này.”

### c177 — `attribution_qualification`
**Review:** [▶ 02:41:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9688s) · [full transcript context](PR9-full-decision-pack.md#c177)  
**Before:** Theo bác sĩ, bổ sung đủ các chất này giúp ngủ ngon và tế bào não hoạt động bình thường.  
**After:** Theo bác sĩ, khi bổ sung các chất này thì sẽ ngủ ngon, ngủ tốt; cùng với thực hành lối sống tốt, ngủ ngon, ngủ tốt thì các tế bào não hoạt động bình thường.  
**Why:** The transcript pairs supplementation with 'thực hành lối sống tốt'. The summary credits supplementation alone.
**Transcript evidence:** [▶ 02:41:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9688s) “Vitamin C, vitamin E vô cùng quan trọng. Vậy khi bổ sung nó thì chúng ta sẽ ngủ ngon, chúng ta ngủ tốt, thực hành lối sống tốt, ngủ ngon, ngủ tốt thì chúng ta các tế bào não hoạt động bình thường,”

### c182 — `attribution_qualification`
**Review:** [▶ 02:42:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9765s) · [full transcript context](PR9-full-decision-pack.md#c182)  
**Before:** Bác sĩ nói bóng đè là biểu hiện tổn thương ở mức tế bào, phân tử do lối sống, tâm sinh lý, ăn uống và môi trường sai, làm gốc tự do gây mất nhịp giữa "người lái" và "bánh xe".  
**After:** Bác sĩ nói "tôi cho rằng" bóng đè thể hiện cơ thể đang tổn thương ở mức độ tế bào, phân tử, do lối sống, tâm sinh lý, ăn uống và tiếp xúc tác nhân môi trường sai, làm xuất hiện gốc tự do, và gốc tự do làm cho cái phanh không nhịp nhàng giữa người lái xe và bánh xe.  
**Why:** Hedge dropped: the doctor marks this as his view with 'Tôi cho rằng', and the summary drops it. The proposal restores his wording.
**Transcript evidence:** [▶ 02:42:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9765s) “cuộc sống. Tôi cho rằng là bóng đè là một cái nó thể hiện cơ thể chúng ta đang thể hiện rằng đang tổn thương ở mức độ tế bào,” · [▶ 02:42:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9774s) “tổn thương ở mức độ phân tử. Do chúng ta thực hành lối sống sai, do tâm sinh lý chúng ta sai, do ăn uống, do tiếp xúc với lại các cái yếu tố tác nhân môi trường sai để xuất hiện những cái chất” · [▶ 02:43:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9784s) “gốc tự do. Gốc tự do và chính gốc tự do này nó là cái nguyên nhân để làm cho cái phanh này nó không nhịp nhàng giữa người lái xe và bánh xe. Từ đấy chúng ta sẽ rơi vào cái trạng thái bóng đè. Tôi cho”

### c193 — `attribution_qualification`
**Review:** [▶ 02:46:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9999s) · [full transcript context](PR9-full-decision-pack.md#c193)  
**Before:** Người khỏe mạnh, không có bệnh nền, không có mỡ máu, tiểu đường hay huyết áp cao thì bổ sung liều cao lên nồng độ dễ và hiệu quả.  
**After:** Người khỏe mạnh, không còn bệnh tật gì khác, không bị nhiều mỡ, mỡ dưới da ít, không có mỡ nội tạng, không bị mỡ máu, tiểu đường hay huyết áp thì bổ sung liều cao sẽ lên được dễ và hiệu quả.  
**Why:** Conditions dropped: the doctor also limits this to people with little body, subcutaneous and visceral fat.
**Transcript evidence:** [▶ 02:46:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9999s) “tật gì khác, rất khỏe rồi, không bị nhiều mỡ, mỡ dưới da ít, mỡ nội tạng không có, không bị mỡ máu, không bị tiểu đường, không bị huyết áp thì khánh lành bổ sung liều cao thì nó sẽ lên được dễ và nó hiệu quả. Nhưng nếu chúng ta có”

### c201 — `mismatch`
**Review:** [▶ 02:49:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10148s) · [full transcript context](PR9-full-decision-pack.md#c201)  
**Before:** Có người chỉ cần khoảng 5.600 UI (bản ghi âm ghi như vậy), có người lên tới 6.000 đến 7.000 UI, nhưng đa số dưới 2.000 UI.  
**After:** Có người chỉ có "5 600 UI" (bản ghi âm ghi như vậy, con số không rõ) đã đủ, có người lên tới "6 7000 UI", nhưng đại đa số mọi người là con số trên dưới 2.000 UI.  
**Why:** 'Trên dưới 2000' (around 2000) became 'dưới 2.000' (under 2000). '5 600' is also ambiguous, so the summary's 5.600 is not confirmed.
**Transcript evidence:** [▶ 02:49:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10148s) “Có người chỉ có 5 600 UI đã đủ rồi nhưng có người lên tới 6 7000 UI cơ.” · [▶ 02:49:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10152s) “Vâng. Nhưng đại đa số mọi người là con số trên dưới 2000 UI. Cho nên khi dò liều tôi”

### c208 — `attribution_qualification`
**Review:** [▶ 01:37:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5835s) · [full transcript context](PR9-full-decision-pack.md#c208)  
**Before:** Bác sĩ nói trí tuệ không phải do trời cho mà đến từ sự cần cù, chịu khó và quyết tâm.  
**After:** Bác sĩ nói con người sinh ra không phải ông trời cũng cho tất cả mọi người trí tuệ tốt, trí nhớ siêu phàm hay năng lực tuyệt vời; riêng bản thân ông nói mình có trí tuệ không được tốt lắm và chỉ nhờ sự cần cù chịu khó, sự quyết tâm trong những năm tháng tuổi ấu thơ.  
**Why:** Overgeneralized: he says heaven does not give everyone good intellect and describes his own diligence. He does not say intellect in general comes from diligence.
**Transcript evidence:** [▶ 01:37:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5835s) “Anh, con người ta sinh ra không phải ông trời cũng cho tất cả mọi người có được cái trí tuệ tốt, có được cái trí nhớ siêu phàm hay là có những cái năng lực tuyệt vời. Như tôi vẫn tâm sự trong” · [▶ 01:37:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5850s) “thân tôi là người mà có trí tuệ không được tốt cho lắm.” · [▶ 01:37:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5854s) “học cũng mọi cái của tôi cũng không phải là thông minh giỏi giang các thứ gì mà chỉ nhờ vào cái sự cần cù chịu khó, cái sự quyết tâm trong những năm tháng của tuổi ấu thơ với cái điều kiện thiếu ăn”

### c210 — `attribution_qualification`
**Review:** [▶ 01:40:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6009s) · [full transcript context](PR9-full-decision-pack.md#c210)  
**Before:** Học sinh cũng lười nhai và thường chỉ muốn ăn nhanh, hấp thu năng lượng nhanh, dẫn đến calo rỗng.  
**After:** Bác sĩ nói các bạn ăn thức ăn nhanh, uống nhiều đồ uống có đường và rơi vào tình trạng calo rỗng rất nhiều. Ông kể hai đứa con của một chị bạn lười nhai, lười mọi thứ và chỉ muốn ăn sẵn, ăn nhanh.  
**Why:** Causal link added: empty calories are tied to sugary drinks and fast food, not to lazy chewing. The chewing story is about a friend's two children, not students in general.
**Transcript evidence:** [▶ 01:40:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6009s) “cái calor rỗng các bạn đang rơi vào cái tình trạng đấy rất nhiều. Thế và các bạn ăn những các cái đồ ăn của thức ăn nhanh. Đến nỗi mà tôi có chị bạn có hai” · [▶ 01:40:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6029s) “thịt cũng thế phải say nó ra để đỡ khỏi nhai. Các bạn ấy lười nhai, các bạn ấy lười tất cả mọi thứ và chỉ muốn rằng ăn sẵn ăn nhanh.” · [▶ 01:40:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6037s) “Vậy khi chúng ta duy trì một cái lối sống mà nhanh gấp gáp, chỉ muốn rằng là tiếp thu những cái gì mà nó nhanh chóng tạo ra năng lượng thì chúng ta sẽ thất” · [▶ 01:40:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6000s) “các bạn uống rất nhiều đường”

### c211 — `attribution_qualification`
**Review:** [▶ 01:40:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6037s) · [full transcript context](PR9-full-decision-pack.md#c211)  
**Before:** Bác sĩ nói việc này có thể khiến các em thất bại, nên phải thay đổi thói quen ăn uống từ hàng ngày.  
**After:** Bác sĩ nói khi duy trì lối sống nhanh, gấp gáp, chỉ muốn những gì nhanh chóng tạo ra năng lượng thì "chúng ta sẽ thất bại", nên đầu tiên phải thay đổi ngay từ thói quen ăn uống hàng ngày.  
**Why:** Softened hedge: 'chúng ta sẽ thất bại' became 'có thể khiến các em thất bại'. The proposal restores his wording and his 'chúng ta'.
**Transcript evidence:** [▶ 01:40:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6037s) “Vậy khi chúng ta duy trì một cái lối sống mà nhanh gấp gáp, chỉ muốn rằng là tiếp thu những cái gì mà nó nhanh chóng tạo ra năng lượng thì chúng ta sẽ thất bại. Vậy đầu tiên là ta phải thay đổi ngay từ cái thói quen ăn uống hàng ngày.”

### c235 — `attribution_qualification`
**Review:** [▶ 01:52:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6755s) · [full transcript context](PR9-full-decision-pack.md#c235)  
**Before:** Ông nói từng bước đan xen kiến thức, và tin rằng người làm như vậy sẽ thành công, không phải người gặp khó khăn khi bước vào đời.  
**After:** Ông nói từng bước đan xen kiến thức, tin rằng khi chuẩn bị những kỹ năng đó thì đến một ngày không xa bạn sẽ thành công; và ông nói riêng với bạn Anh Anh, người xem kênh, biết đặt câu hỏi, biết quan tâm trăn trở, rằng ông tin bạn sẽ là người thành công chứ không phải người sau này bước vào đời gặp phải khó khăn.  
**Why:** Scope lost: the last prediction is addressed to Anh Anh and rests on asking questions and showing concern. The summary generalizes it to anyone who follows the steps.
**Transcript evidence:** [▶ 01:52:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6755s) “cái kỹ năng đó khi bạn chuẩn bị cho mình thì tôi tin rằng đến một ngày không xa bạn sẽ thành công. Và ngày hôm nay bạn xem kênh của chúng tôi biết đặt ra câu hỏi như thế này, biết quan tâm trăn trở như thế này, tôi tin rằng bạn sẽ là cái người thành công chứ không phải là cái người mà sau này bạn bước vào đời gặp phải những cái khó khăn. Tôi tin rằng” · [▶ 01:52:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6750s) “đan xen các cái kiến thức với nhau.” · [▶ 01:52:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6773s) “Thì đấy là bạn Anh Anh sau khi”

### c245 — `attribution_qualification`
**Review:** [▶ 02:03:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7417s) · [full transcript context](PR9-full-decision-pack.md#c245)  
**Before:** Bác Thủy ở Đức kể sau khi bổ sung vi chất, mọi người xung quanh ốm nhưng bác không sao.  
**After:** Một bác ở Đức (bác sĩ nói "tôi đoán bác tên là Thủy") kể sau khi bổ sung vi chất, mọi người xung quanh đều quay ra ốm nhưng bác không sao.  
**Why:** Hedge dropped: the name is the doctor's guess, and the summary states it as fact.
**Transcript evidence:** [▶ 02:03:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7417s) “Thì bác ở bên Đức tôi đoán bác tên là Thủy. Thì bác thấy rằng sau khi bác bổ sung vi chất tất cả mọi người xung quanh đều quay ra ốm nhưng bác chẳng làm sao hết cả. Thế hoặc là cô giáo thu trang ở”

### c248 — `attribution_qualification`
**Review:** [▶ 02:04:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7459s) · [full transcript context](PR9-full-decision-pack.md#c248)  
**Before:** Thầy Nguyễn Hiền, giáo viên vật lý, đau cột sống và đau xương hông, nghi có thể là ung thư xương, uống đủ loại thuốc kể cả kháng sinh nhưng không đỡ mà càng uống càng nặng.  
**After:** Thầy Nguyễn Hiền, thầy giáo vật lý, đau cột sống, đau xương hông, cảm tưởng mình bị đến ung thư xương, uống đủ các loại thuốc cả kháng sinh nhưng cuối cùng không đỡ.  
**Why:** 'Càng uống càng nặng' is not stated: the doctor's sentence breaks off at 'thầy càng uống vào'. 'Cảm tưởng' is also closer to the transcript than 'nghi có thể'.
**Transcript evidence:** [▶ 02:04:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7459s) “Nguyễn Hiền, thầy giáo vật lý bắt đầu vào trường Đại học Sư phạm tôi nhớ là năm 1971. Sau đó thầy đi dạy thầy về quê thầy chuyển chỗ này chỗ khác và thầy bị đau cột sống đau xương hông rồi bị một loạt những các cái bệnh tật mà thầy cảm tưởng rằng thầy bị đến ung thư xương.” · [▶ 02:04:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7475s) “Thế thì uống đủ các loại thuốc cả kháng sinh đủ các thứ nhưng cuối cùng không đỡ thầy càng uống vào. Mà lúc nãy tôi có”

### c250 — `attribution_qualification`
**Review:** [▶ 02:04:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7490s) · [full transcript context](PR9-full-decision-pack.md#c250)  
**Before:** Khi được hỏi về paracetamol, bác sĩ cho rằng thuốc này có thể hại gan, và cũng hại thận và nhiều cơ quan khác, vì sinh ra một hóa chất gây gốc tự do rất lớn.  
**After:** Trong đoạn nói về thuốc giảm đau, bản ghi âm nêu paracetamol "hại tới gan", rồi "hại tới thận, hại tới tất cả các nơi"; thuốc này là một hóa chất vào trong cơ thể và gây ra gốc tự do rất lớn.  
**Why:** No one asks about paracetamol, and 'có thể' softens a definite statement. Pass 1 and pass 2 read the liver line's speaker differently, so the proposal does not name a speaker for it. Human to confirm the speaker.
**Transcript evidence:** [▶ 02:04:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7490s) “Vâng. Đặc biệt là những cái thuốc giảm đau. Thuốc giảm đau như paracetamol nó hại tới gan đúng không ạ?” · [▶ 02:05:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7496s) “Thế rồi thì nó hại tới thận, hại tới tất cả các nơi thì thuốc này nó sinh ra đây là một cái hóa chất vào trong cơ thể chúng ta. Nó gây ra gốc tự do rất là lớn. Thế thì những cái gốc tự do đấy”

### c251 — `attribution_qualification`
**Review:** [▶ 02:05:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7513s) · [full transcript context](PR9-full-decision-pack.md#c251)  
**Before:** Ông kể một bệnh nhân đau vùng háng, chụp thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải khoan giảm áp và thay khớp háng.  
**After:** Bác sĩ nêu ví dụ có những người đau bên phần háng, dần dần đi chụp thì thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải "xuyên giảm áp" (bản ghi âm ghi như vậy) rồi thay cả khớp háng.  
**Why:** Population changed: he gives a general example ('có những người'), not one specific patient. The caption says 'xuyên giảm áp'; 'khoan' is the summary's word.
**Transcript evidence:** [▶ 02:05:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7513s) “này, có những người đau ở bên phần háng ấy. Thế đến khi dần dần đi chụp ích quang một ngày bắt đầu thấy hoại tử vô khuẩn trỏm xương đùi, cuối cùng là phải” · [▶ 02:05:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7522s) “xuyên giảm áp, cuối cùng là phải thay cả khớp háng. Thế nhưng mà những bệnh nhân ấy chỉ cần yêu cầu gì thôi là đang hút”

### c252 — `attribution_qualification`
**Review:** [▶ 02:05:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7524s) · [full transcript context](PR9-full-decision-pack.md#c252)  
**Before:** Bệnh nhân này đang hút thuốc, khi chỉ dừng hút thuốc lá thì cơn đau đã giảm đi nhiều.  
**After:** Bác sĩ nói những bệnh nhân ấy, nếu đang hút thuốc lá, chỉ cần một động tác là dừng hút thuốc lá lại thì đã giảm đau đi rất nhiều.  
**Why:** Population changed: 'những bệnh nhân ấy ... chỉ cần' is a general statement, which the summary turns into an outcome for one patient.
**Transcript evidence:** [▶ 02:05:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7524s) “khớp háng. Thế nhưng mà những bệnh nhân ấy chỉ cần yêu cầu gì thôi là đang hút thuốc lá chỉ cần có một động tác đó là” · [▶ 02:05:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7531s) “dừng hút thuốc lá lại nó đã giảm đau đi rất nhiều.”

### c254 — `attribution_qualification`
**Review:** [▶ 01:21:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4897s) · [full transcript context](PR9-full-decision-pack.md#c254)  
**Before:** Chị Ngọc Thơ, theo bình luận được đọc trên chương trình, từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt, khiến chị xấu hổ và không dám chụp ảnh với ai.  
**After:** Một người xem, theo bình luận được đọc trên chương trình (bác sĩ nói "tôi đoán là chị Ngọc Thơ" vì tài khoản không dấu), từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt; bác sĩ kể lại chị xấu hổ, ngại ngùng, không dám chụp ảnh với ai.  
**Why:** Hedge dropped: the doctor guesses the name because the account has no diacritics. The summary states the name as fact.
**Transcript evidence:** [▶ 01:21:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4897s) “Tình trạng của em trước đây. Từ năm 2017 đến nay, da của em đặc biệt là lòng bàn tay, lòng bàn chân và da mặt, luôn bị vàng bợt, thiếu sức sống. Niêm mạc mắt” · [▶ 02:06:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7588s) “Ngọc hay là Ngọc Thơ? Tôi đoán là chị Ngọc Thơ không có dấu không có dấu cho nên tôi đoán là chị Ngọc Thơ. Thế thì chị Ngọc Thơ có bình” · [▶ 02:06:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7600s) “xấu hổ, chị ngại ngùng, không dám đi đâu, không dám chụp ảnh với ai vì rằng là cơ thể mình ốm yếu đã đành, mệt mỏi”

### c256 — `attribution_qualification`
**Review:** [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s) · [full transcript context](PR9-full-decision-pack.md#c256)  
**Before:** Người dẫn chương trình đặt nghi vấn chị đang bị thiếu máu nhược sắc do thiếu sắt, gây tan hồng cầu và vàng da.  
**After:** Chị, người viết bình luận, tự cho rằng có lẽ mình thiếu sắt nhược sắc; bác sĩ thuật lại câu hỏi chị đặt ra là có phải thiếu máu nhược sắc do thiếu sắt gây tan hồng cầu và vàng da hay không.  
**Why:** Speaker misattributed: the viewer raises this question ('chị đặt ra'), not the host.
**Transcript evidence:** [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s) “nhận ra có lẽ vấn đề nằm ở việc bị thiếu sắt nhược sắc.” · [▶ 01:23:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4999s) “vàng. Nhưng em không rõ độ chính xác của thông tin này như thế nào. Em đã đi khám” · [▶ 02:07:41](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7656s) “này. Cuối cùng là cái vàng đó chị đặt ra một cái điều rất hay đó là có phải sau” · [▶ 02:07:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7671s) “thiếu máu nhược sắc do thiếu sắt và nó gây ra một cái hiện tượng là tan hồng cầu.”

### c275 — `attribution_qualification`
**Review:** [▶ 02:13:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8014s) · [full transcript context](PR9-full-decision-pack.md#c275)  
**Before:** Người dẫn nói vitamin C và vitamin E cũng là các chất liên quan đến gốc tự do, và glutathion cũng vậy.  
**After:** Trong đoạn bác sĩ nhắc lại ("lúc ấy tôi nói là gì ạ?"), bản ghi âm ghi "Vitamin C cũng là gốc tự do, vitamin E cũng là gốc tự do" (có dấu đổi người nói giữa câu), rồi nhắc đến glutathion đang nói hôm nay.  
**Why:** The doctor leads this recall, not the host. The caption says 'cũng là gốc tự do', which the summary softens to 'liên quan'. A speaker-change mark sits mid-sentence, so the speaker of that half needs a human check. The wording is kept as spoken with no correction.
**Transcript evidence:** [▶ 02:13:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8014s) “quyết cái vấn đề gốc tự do. Lúc ấy tôi nói là gì ạ? Vitamin C cũng là gốc tự do, vitamin E cũng là gốc tự do đúng không ạ?” · [▶ 02:13:46](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8021s) “Gluten cái gì đấy? Glutat. Glutat mà chúng ta đang nói hôm nay”

### c282 — `attribution_qualification`
**Review:** [▶ 02:18:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8297s) · [full transcript context](PR9-full-decision-pack.md#c282)  
**Before:** Ông cho rằng đau có thể do gốc tự do tấn công thần kinh và cần tìm hướng khác.  
**After:** Ông cho rằng với những đau đầu hay triệu chứng đó thì hãy đi tìm theo hướng khác; còn đau dây thần kinh số 5, đến giờ phút này ông cho rằng vẫn là nguyên nhân gốc tự do tấn công vào đây và gây tổn thương dây thần kinh số năm.  
**Why:** Added hedge: 'tôi cho rằng vẫn là nguyên nhân' has no 'có thể'. This follows the reconciliation rationale; the record's note is stale pass-1 text.
**Transcript evidence:** [▶ 02:18:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8297s) “Và tôi cho rằng cái này nó do những cái đau đầu hay là những cái triệu chứng gì đó chúng ta hãy đi tìm theo cái hướng khác và dường như có những cái ẩn chứa phía sau. Thì đến bây giờ tôi thấy rằng” · [▶ 02:21:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8493s) “sao nó lại như thế? Đau dây thần kinh số 5 đến giờ phút này tôi cho rằng vẫn là nguyên nhân gốc tự do nó tấn công vào đây này. Gốc tự do nó tấn công vào đây và gây tổn thương dây thần kinh số năm.”

### c287 — `attribution_qualification`
**Review:** [▶ 02:21:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8466s) · [full transcript context](PR9-full-decision-pack.md#c287)  
**Before:** Theo bác sĩ, một số bệnh nhân đến bổ sung vi chất đúng và đủ thì cơn đau biến mất hẳn, có người đỡ 90 đến 95%, và số còn lại chỉ còn đau nhẹ không đáng kể.  
**After:** Theo bác sĩ, sau khi những bệnh nhân đến bổ sung vi chất đúng và đủ thì có những người nói tự dưng hết hẳn, có những người đỡ được đến "8 90% 95%" và người ta bảo chỉ còn hơi hơi không đáng kể; có những người nói khỏi sau khi bổ sung vi chất.  
**Why:** Residual slight pain describes the same 90-95% group, not a separate 'số còn lại'. The patient-reported framing ('có những người nói') was dropped.
**Transcript evidence:** [▶ 02:21:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8466s) “những bệnh nhân đến bổ sung vi chất đúng và đủ thì có những người nói tự dưng hết hẳn không còn đau dây thần kinh số năm nữa. Thế có những người đỡ được đến 8 90% 95%. Đỡ tới 90 95% là khỏi rồi. Còn” · [▶ 02:21:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8476s) “90% 95%. Đỡ tới 90 95% là khỏi rồi. Còn cái gì nữa đâu ạ? người ta bảo chỉ còn hơi hơi không đáng kể nữa thôi. Thế còn” · [▶ 02:21:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8484s) “có những người nói rằng khỏi sau khi bổ sung vi chất xong chẳng còn thấy đau dây thần kinh số năm đâu nữa và cuộc sống trở nên vui vẻ thoải mái. Thế thì tại”

### c291 — `mismatch`
**Review:** [▶ 02:22:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8564s) · [full transcript context](PR9-full-decision-pack.md#c291)  
**Before:** Chị ăn nhiều đồng để quên cơn đau nên cân nặng tăng nhanh.  
**After:** Chị ăn đường vào để quên cơn đau nên cân nặng tăng nhanh.  
**Why:** Wrong substance: the transcript says 'đường' (sugar), the summary says 'đồng' (copper). 'Nhiều' is also not stated.
**Transcript evidence:** [▶ 02:22:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8564s) “nỗi mà bắt đầu bác ăn đường vào để cho quên hết tất cả. Lấy cái ngọt ngào để che lấp đi tất cả những cái cơn đau này dẫn tới là cân nặng tăng lên vù vù. Thế”

### c294 — `attribution_qualification`
**Review:** [▶ 02:44:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9835s) · [full transcript context](PR9-full-decision-pack.md#c294)  
**Before:** Bác sĩ hướng dẫn trong vài tiếng đồng hồ, và sau đó chị bổ sung vi chất theo từng bước, nâng dần liều.  
**After:** Bác sĩ hướng dẫn trong mấy tiếng đồng hồ ("4 năm tiếng đồng hồ" theo bản ghi âm) để bổ sung vi chất, và sau đó chị trải qua từng bước một, "cứ nâng cao nâng cao dần".  
**Why:** 'Liều' (dose) is added: 'nâng cao dần' is in a micronutrient context, but dose is not named.
**Transcript evidence:** [▶ 02:44:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9835s) “nhưng mà sau đó ba mẹ con đến khám thì tôi đã hướng dẫn cho ngày đấy hướng dẫn mấy tiếng đồng hồ cơ 4 năm tiếng đồng hồ cơ. Vâng.” · [▶ 02:44:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9842s) “Để mà bổ sung vi chất thì sau khi hướng dẫn tôi trải qua từng bước một cứ nâng cao nâng cao dần thì đã thấy rằng cái hiệu quả đã thay đổi ngoạn mục trông thấy. Và nếu chị mua được các cái vi”

### c319 — `attribution_qualification`
**Review:** [▶ 03:15:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11706s) · [full transcript context](PR9-full-decision-pack.md#c319)  
**Before:** Số lượng hồng cầu có thể chưa thấp đến mức thiếu máu cấp, nhưng cơ thể có thể đang thiếu máu chức năng và đói oxy.  
**After:** Số lượng hồng cầu trên giấy tờ có thể chưa tụt xuống mức báo động của thiếu máu cấp tính, nhưng cơ thể bác đang ở tình trạng thiếu máu chức năng và đói oxy vô cùng trầm trọng.  
**Why:** Softened hedge: only the first half has 'có thể'. The review asserts functional anemia and oxygen hunger 'vô cùng trầm trọng'. The proposal restores that wording.
**Transcript evidence:** [▶ 03:15:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11706s) “Mặc dù số lượng hồng cầu trên giấy tờ có thể chưa tụt xuống đến mức báo động của thiếu máu cấp tính, nhưng cơ thể bác lại giơ vào tình trạng thiếu máu chức năng và đói oxy vô cùng trầm trọng.”

### c333 — `attribution_qualification`
**Review:** [▶ 03:19:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11965s) · [full transcript context](PR9-full-decision-pack.md#c333)  
**Before:** Gan và thận thiếu vi chất nên giảm khả năng đào thải, và tinh thể urat có thể lắng đọng ở khớp và thành mạch, gây đau gút.  
**After:** Gan và thận kiệt sức vì thiếu vi chất nên mất đi khả năng đào thải, và những tinh thể urat âm thầm đọng lại nơi khớp xương và thành mạch, đe dọa mang đến những cơn đau gút.  
**Why:** Hedges moved in both directions: 'mất đi' became 'giảm', 'đọng lại' became 'có thể lắng đọng', and 'đe dọa mang đến' hardened to 'gây'.
**Transcript evidence:** [▶ 03:19:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11965s) “tăng vọt. Trong khi đó, lá gan và quả thận đã kiệt sức vì thiếu vi chất nên mất đi khả năng đảo thải.” · [▶ 03:19:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11974s) “Những tinh thể uras sắc nhọn như vô số mũi kim nhỏ âm thầm đọng lại nơi khấp xương và thành mạch. Đe dọa mang đến” · [▶ 03:19:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11982s) “những cơn đau gút, xé thịt, xé da như muốn bóc nghẹt thân thể vốn đã gầy gộc.”

### c352 — `mismatch`
**Review:** [▶ 03:23:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12200s) · [full transcript context](PR9-full-decision-pack.md#c352)  
**Before:** Phần nhận xét nói kết hợp kho sắt đóng và lượng sắt lưu hành giảm không gây nguy hiểm đến tính mạng, nhưng làm chậm phân phối năng lượng tạo máu.  
**After:** Phần nhận xét nói sự kết hợp giữa kho sắt đóng cửa với số lượng xe chở sắt bị sụt giảm không gây nguy cấp tử sinh, nhưng tạo nên sự trì trệ trong việc phân phối năng lượng tạo máu.  
**Why:** Entity changed: the number of iron-transport vehicles fell, not circulating iron, which the review says earlier has not run down.
**Transcript evidence:** [▶ 03:23:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12200s) “Sự kết hợp giữa một kho sắt đóng mất cửa với số lượng xe trở sắt bị sụt giảm, không gây ra nguy cấp tử sinh nhưng nó” · [▶ 03:23:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12209s) “tạo nên một sự trì trệ [âm nhạc] trong việc phân phối năng lượng tạo máu.” · [▶ 03:21:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12104s) “chứng minh rằng dẫu số lượng xe vận tải bị thu hệp, lượng sắt thực sự lưu hành trong dòng máu của bác vẫn đang giữ được sự nhịp nhàng, chưa hề bị rơi vào cảnh suy kiệt cạn kiệt.”

### c373 — `attribution_qualification`
**Review:** [▶ 03:24:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12270s) · [full transcript context](PR9-full-decision-pack.md#c373)  
**Before:** Transcript cho rằng những thiếu hụt này xuất hiện sau nhiều thập kỷ hút thuốc lá và thiếu vi chất.  
**After:** Transcript nói kẽm và đồng dường như đã cạn kiệt sau hàng thập kỷ bác sống trong khói thuốc lá và thiếu hụt vi chất.  
**Why:** Hedge dropped: 'dường như' was removed, and the statement covers zinc and copper only, while 'những thiếu hụt này' also takes in ionized calcium.
**Transcript evidence:** [▶ 03:24:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12270s) “xương lành dường như đã cạn kiệt sau hàng thập kỷ bác sống trong khói thuốc lá và thiếu hụt vi chất.” · [▶ 03:24:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12264s) “Kẽm và đồng chính là những người thợ sửa [âm nhạc] chữa tí hon.”

### c377 — `attribution_qualification`
**Review:** [▶ 03:25:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12338s) · [full transcript context](PR9-full-decision-pack.md#c377)  
**Before:** Ông so sánh với quy chuẩn của một số nước phát triển như Nhật Bản, nơi giới hạn trên có thể được mở rộng lên 1000 hoặc thậm chí 1500 pg/ml, và cho rằng con số của bác vẫn nằm trong ngưỡng an toàn.  
**After:** Ông so sánh với quy chuẩn tham chiếu của nhiều quốc gia phát triển như "bản" (bản ghi âm ghi như vậy), nơi giới hạn trên thường được mở rộng lên tới 1000 hoặc thậm chí 1500 pg/ml, và cho rằng con số của bác vẫn hoàn toàn nằm trong ngưỡng an toàn.  
**Why:** The caption says 'như bản'; naming Japan is not safely grounded in it. 'Nhiều' and 'thường' were also softened to 'một số' and 'có thể'. Human to confirm the country from the audio.
**Transcript evidence:** [▶ 03:25:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12338s) “Nếu so sánh với quy chuẩn tham chiếu của nhiều quốc gia phát triển như bản, nơi giới hạn trên của vitamin P12 thường được mở rộng lên tới 1000 picog” · [▶ 03:25:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12348s) “[âm nhạc] ml hoặc thậm chí là 1500 thì con số của bác vẫn hoàn toàn nằm trong ngưỡng an toàn của cơ thể.”

### c401 — `mismatch`
**Review:** [▶ 04:09:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14987s) · [full transcript context](PR9-full-decision-pack.md#c401)  
**Before:** Bác có thể bắt đầu với việc nín thở khoảng 1 đến 1,5 giây, và nếu nhịn được 10 hoặc 15 giây thì chỉ giảm xuống khoảng 8 đến 9 giây để giữ an toàn.  
**After:** Bác có thể tập thở đơn giản theo "1 1,5", tức là cố gắng kéo dài thì sau ra một chút để đẩy khí cạn ra, tuyệt đối không cố gắng; và nếu nhịn được 15 giây, 10 giây thì chỉ giảm xuống độ 8, 9 giây để giữ an toàn.  
**Why:** Safety-relevant: '1 1,5' is about lengthening the later phase of the breath, not holding the breath for 1 to 1.5 seconds. A reader could follow the current text wrongly. The 8-9 second part matches.
**Transcript evidence:** [▶ 04:09:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14987s) “thế này thôi. Chỉ là 1 1,5 thôi đã đã là quý rồi. 1 1,5 tức là ta cố gắng là kéo dài cái thì sau ra một chút để ta đẩy” · [▶ 04:09:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14994s) “dài cái thì sau ra một chút để ta đẩy được các cái khí cạn ra. Nhưng bác tuyệt đối không cố gắng bởi vì nếu cố quá nó sẽ thành ra là nguy hiểm. Vì sao? Vì sức” · [▶ 04:10:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15006s) “lẽ ra nếu bác thở bác nhịn được chẳng hạn như là 15 giây, 10 giây chẳng hạn thì bác chỉ giảm xuống độ 8 9 giây thôi để giữ cái an toàn như mình đã. Thế thì” · [▶ 04:10:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15013s) “Thế thì có thể không cần thiết là bác phải thở 1 luôn mà bác có thể chở thở 1 1,5 thôi đã.”

### c407 — `mismatch`
**Review:** [▶ 04:10:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15051s) · [full transcript context](PR9-full-decision-pack.md#c407)  
**Before:** Bác sĩ nói đầu tiên là magie, rồi kẽm, canxi, vitamin D3, vitamin tổng hợp (đặc biệt nhóm B), vitamin C và cuối cùng là omega 3.  
**After:** Bác sĩ nói đầu tiên là magie, rồi canxi, vitamin D3, vitamin tổng hợp (đặc biệt nhóm B), vitamin C, kẽm và cuối cùng là omega 3.  
**Why:** Order wrong: zinc comes after vitamin C. The early mention of zinc is an aside about cofactors, not a list position.
**Transcript evidence:** [▶ 04:10:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15051s) “sung thì những cái gì. Đó là đầu tiên là cái mag rất quan trọng mà lúc nãy tôi vừa mới nói đó là chúng ta ma kẽm cen vân vân các thứ nếu chúng ta không có đủ” · [▶ 04:11:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15069s) “gì hết cả. Chân ma là rất quan trọng. Sau đó đến gì ạ? Đến canxi. Xong đến vitamin D3 đúng không ạ? Thì đây chính là bộ ba tam giác vàng. Tiếp theo nữa là” · [▶ 04:11:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15104s) “vitamin C xong tiếp nữa là đến gì ạ? Đến kẽm mà lúc đấy tôi vừa nói xong cuối cùng là gì ạ? Omega 3 thì chúng ta phải” · [▶ 04:11:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15076s) “Tiếp theo nữa là vitamin gì ạ? Vitamin tổng hợp.”

### c447 — `attribution_qualification`
**Review:** [▶ 04:12:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15163s) · [full transcript context](PR9-full-decision-pack.md#c447)  
**Before:** Ông cũng nhắc rằng ngoài bảy nhóm vi chất còn có khoảng 18 sản phẩm thuộc các nhóm này, cùng các thành phần khác như vitamin B7, B8, bo, silic và glutathione.  
**After:** Ông cũng nhấn mạnh rằng trong bảy nhóm vi chất phải ít nhất có 18 sản phẩm, chưa kể những sản phẩm phải thêm như vitamin B7, B8, bo, silic, và hôm nay là glutathion.  
**Why:** Threshold changed: 'phải ít nhất có 18' (at least) became 'khoảng 18' (about).
**Transcript evidence:** [▶ 04:12:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15163s) “cái vi chất này là bảy cái nhóm cơ bản nhưng mà đến giờ Giờ phút này thì tôi vẫn nhấn mạnh là chúng ta phải ít nhất có 18 cái sản phẩm đúng không ạ? 18 sản phẩm nằm trong bảy nhóm này. Chưa kể” · [▶ 04:12:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15174s) “những các cái sản phẩm mà chúng ta phải thêm đó là vitamin B7, nào là vitamin B8 đúng không ạ? Nào là bo, nào là silic. Hôm nay chúng ta lại đến Glutathion đúng”

### c449 — `attribution_qualification`
**Review:** [▶ 04:17:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15457s) · [full transcript context](PR9-full-decision-pack.md#c449)  
**Before:** Bác sĩ nói những lời truyền miệng này "hào nhoáng" và cần nhìn lại dưới góc nhìn y khoa.  
**After:** Khánh Lành, trong phần giới thiệu, nói đằng sau những lời truyền miệng hào nhoáng ấy, báo chí và truyền thông cũng ghi nhận không ít những khoảng tối, và đặt câu hỏi glutathion thực sự là gì dưới góc nhìn y khoa.  
**Why:** Speaker misattributed: both lines are Khánh Lành's segment intro, before the host invites the doctor to speak.
**Transcript evidence:** [▶ 04:17:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15457s) “Vâng. Thế nhưng đằng sau những lời chuyển miệng hào nhoáng ấy, báo chí và truyền thông cũng ghi nhận không ít những khoảng tối hoang mang. Đó là gì ạ?” · [▶ 04:18:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15510s) “Vậy glutathe thực sự là gì dưới góc nhìn y khoa chân chính? Và tại sao sự thiếu” · [▶ 04:18:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15528s) “Khánh Lành xin kính mời bác sĩ Phúc”

### c456 — `unresolved`
**Review:** [▶ 05:22:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19340s) · [full transcript context](PR9-full-decision-pack.md#c456)  
**Before:** Bác sĩ dùng lập luận này để giải thích cơ chế, không phải để khẳng định chẩn đoán cho bất kỳ ai.  
**After:** Đề xuất bỏ câu này vì transcript không có lời nào như vậy của bác sĩ. Nếu muốn giữ một lời nhắc, ghi rõ đây là lời chung của Khánh Lành cuối chương trình (đã có ở c553), không quy cho bác sĩ.  
**Why:** Stays unresolved. The only related text is the host's general closing disclaimer, which does not say that this explanation is not a diagnosis. The quote shows that closing text only and does not support the claim.
**Transcript evidence:** [▶ 05:22:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19340s) “video trên kênh đều trị mang tính chất tham khảo và với mục đích là nâng cao nhận thức kiến thức chăm sóc sức khỏe cho cộng đồng và hoàn toàn không thay thế cho việc chẩn đoán và yểu điều trị y khoa trực tiếp và mỗi cơ thể là một”

### c471 — `mismatch`
**Review:** [▶ 04:31:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16299s) · [full transcript context](PR9-full-decision-pack.md#c471)  
**Before:** Hai glutathion hỏng sẽ khóa vào nhau tạo thành GSSG.  
**After:** Hai glutathion hỏng tạm thời đám vào nhau tạo nên một phức hợp gọi là "GSGS" (bản ghi âm ghi như vậy).  
**Why:** The doctor says 'GSGS', the summary says 'GSSG'. Changing it to either form as a chemistry correction is out of scope, so the proposal keeps the spoken form. 'Tạm thời' is restored.
**Transcript evidence:** [▶ 04:31:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16299s) “vào trạng thái là chúng ta thấy gì? Cả hai kìm này đều hỏng thì các mũi kìm nó đám vào nhau tạm thời để tạo nên một cái phức hợp gọi là GSGS. Thế phức hợp GSGS này thì không hoạt” · [▶ 04:32:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16362s) “electron và 2H+ của cái gì? cho vào cái GS đúng không ạ? SG SìG để từ đây lại tạo ra hai cái kìm hoàn chỉnh. Vâng.”

### c478 — `mismatch`
**Review:** [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s) · [full transcript context](PR9-full-decision-pack.md#c478)  
**Before:** Bác sĩ nêu ba nguồn chính.  
**After:** Đầu tiên bác sĩ nói cái thứ nhất là yếu tố tinh thần; tiếp theo ông đánh số: thứ nhất là ăn uống, thứ hai là thuốc, thứ ba là kim loại nặng.  
**Why:** 'Three sources' loses the source's numbering: mental factors come first, then diet, medicine and heavy metals are numbered 1 to 3. Note for the human: c479 to c482 number these differently and were classed supported, so they may need the same wording if this item is accepted.
**Transcript evidence:** [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s) “Thì đầu tiên cái thứ nhất là liên quan tới yếu tố tinh thần mà lúc nãy chúng ta phân tích suốt rồi đúng không ạ?” · [▶ 04:38:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16709s) “Nó gắn tất cả những cái này gắn vào nó sẽ thành chất nguy hiểm. Thứ hai nữa là chúng ta ngoài cái ăn uống ra thì chúng ta có gì ạ? Có thuốc. các sản phẩm thuốc” · [▶ 04:39:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16739s) “bắt đầu nó nguy hiểm. Cái thứ ba đó là chúng ta rất chú ý là những cái kim loại nặng.” · [▶ 04:38:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16679s) “Do đồ ăn thức uống thứ nhất là do ăn uống.”

### c488 — `mismatch`
**Review:** [▶ 04:41:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16909s) · [full transcript context](PR9-full-decision-pack.md#c488)  
**Before:** Các cơ quan này đều thực hiện nhiều chức năng thải độc.  
**After:** Đây là những cơ quan thực hiện rất nhiều chức năng; về thải độc, bản ghi âm ghi "thận cũng thải độc rất nhiều. Gan, não, thận trong ruột của chúng ta rất nhiều" và "thận là cái nơi thải độc" (chưa rõ những cơ quan nào được nói là thải độc).  
**Why:** The transcript says these organs have many functions, and the summary turns this into all of them performing many detox functions. The captions clearly call the kidney a detox site, but the unpunctuated 'Gan, não, thận trong ruột ... rất nhiều' follows a speaker change and is affirmed at the next turn, so it is unclear which organs it covers. The proposal keeps the caption's wording. Human to check which organs detox and who says it.
**Transcript evidence:** [▶ 04:41:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16909s) “và thận cũng thải độc rất nhiều. Gan, não, thận trong ruột của chúng ta rất nhiều. Vâng. Đúng rồi. Đấy là những cơ quan mà” · [▶ 04:42:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16934s) “đang lục phủ ngũ tạng của chúng ta đang thực hiện những chức năng rất nhiều tim rồi đến phổi vân vân. Tất cả như thế này” · [▶ 04:41:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16914s) “Đấy là những cơ quan mà chúng ta thực hiện rất nhiều chức năng” · [▶ 04:42:06](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16921s) “Thứ hai là là gì ạ? Là thận là cái nơi thải độc đúng không ạ?”

### c500 — `attribution_qualification`
**Review:** [▶ 04:51:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17512s) · [full transcript context](PR9-full-decision-pack.md#c500)  
**Before:** Ti thể có ADN riêng nằm sát màng trong, nên gốc tự do thấm qua có thể phá hủy ADN này và gây đột biến.  
**After:** Ti thể có ADN riêng nằm sát màng ti thể, nên các gốc tự do thấm qua thì phá hủy ADN riêng này, tạo thành gốc tự do và bị đột biến.  
**Why:** 'Màng trong' (inner membrane) is added: the doctor says only 'sát màng ti thể'. 'Có thể' also softens his direct statement.
**Transcript evidence:** [▶ 04:51:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17512s) “ADN là vật chất di truyền rất quan trọng. Thế mà nằm ở sát màng ti thể này dẫn tới là các gốc tự do nó thấm qua đây thì phá hủy gì ạ? ADN” · [▶ 04:52:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17522s) “Đúng rồi. Phá hủy ADN nó có hai cái. Một là chính ADN này tạo thành gốc tự do. Hai là gì ạ? Là bị đột biến. Vâng.”

### c509 — `attribution_qualification`
**Review:** [▶ 05:01:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18077s) · [full transcript context](PR9-full-decision-pack.md#c509)  
**Before:** Bác sĩ nói đây là cơ chế, không phải lời khuyên.  
**After:** Bác sĩ nói "đấy là cái cơ chế làm trắng da là như vậy".  
**Why:** 'Không phải lời khuyên' is not said. The host's closing disclaimer is general and not tied to this mechanism.
**Transcript evidence:** [▶ 05:01:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18077s) “đấy là cái cơ chế làm trắng da là như vậy.”

### c529 — `attribution_qualification`
**Review:** [▶ 05:12:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18750s) · [full transcript context](PR9-full-decision-pack.md#c529)  
**Before:** Bác sĩ cho rằng đường tiêm "quá nguy hiểm", có thể gây sốc và ngộ độc.  
**After:** Bác sĩ nói đường tiêm "quá nguy hiểm", và đường tiêm này thì "sẽ một là sốc và hai là ngộ độc".  
**Why:** Softened hedge: 'sẽ một là sốc và hai là ngộ độc' became 'có thể gây'. The proposal restores his wording.
**Transcript evidence:** [▶ 05:12:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18750s) “Thì con đường này quá nguy hiểm.” · [▶ 05:12:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18754s) “Con đường tiêm này thì sẽ một là sốc và hai là ngộ độc.”

### c541 — `unresolved`
**Review:** [▶ 05:15:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18954s) · [full transcript context](PR9-full-decision-pack.md#c541)  
**Before:** Lưu ý: đây là cách nói trong bản phiên âm, nên người xem nên đối chiếu lại nếu cần.  
**After:** Đề xuất bỏ ghi chú này, hoặc đánh dấu rõ đây là ghi chú của người tóm tắt, không phải nội dung chương trình.  
**Why:** Stays unresolved. This is an editorial note about transcript reliability, not something said in the video, so no supporting quote exists. The figures it refers to were checked at c540.
**Transcript evidence:** none; this is an editorial note, not video speech.

### c549 — `attribution_qualification`
**Review:** [▶ 05:19:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19160s) · [full transcript context](PR9-full-decision-pack.md#c549)  
**Before:** Bác sĩ nói glutathione đang bán rất đắt và là sản phẩm "hot" trên thị trường.  
**After:** Bác sĩ nói trên thế giới có những sản phẩm glutathion bán rất đắt, và nó đã trở thành một sản phẩm khá hot trên thị trường.  
**Why:** Qualifier dropped: 'có những sản phẩm' (some products) and 'khá hot' became glutathione in general being 'rất đắt' and 'hot'.
**Transcript evidence:** [▶ 05:19:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19160s) “sản phẩm Glutathion trên thế giới có những sản phẩm bán rất đắt và nó đã trở thành một cái sản phẩm khá hot trên thị trường”

## Safety omissions requiring a human call
These are viewer self-reports that the audit kept as omissions under a safety exception to its viewer-comment rule. Decide whether to retain them as omissions.

| Item | Topic | Watch / full context |
|---|---|---|
| o19 | Parent gives supplements to teenage children | [▶ 01:26:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5163s) · [full context](PR9-full-decision-pack.md#o19) |
| o20 | Reported side effects of neurological / anti-epileptic drugs | [▶ 01:27:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5274s) · [full context](PR9-full-decision-pack.md#o20) |
| o21 | Online “natural healing” groups and fear of Western medicine | [▶ 01:28:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5309s) · [full context](PR9-full-decision-pack.md#o21) |
| o22 | Whole-body rigidity, emergency care, IV calcium | [▶ 01:28:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5320s) · [full context](PR9-full-decision-pack.md#o22) |

## Record your decisions
Use a comment, a PR review, or a separate approval record. For each correction, state: `cNNN: accept`, `cNNN: edit — <replacement>`, or `cNNN: reject — <reason>`. Do not apply changes until the target-summary decision above is settled.

