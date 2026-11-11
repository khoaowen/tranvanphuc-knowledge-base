# Decision brief, ticket 2.6: V-Qfwjo28Zg review-gate failures

Status: **decision brief only**. Nothing was applied. No summary, review, claim map, audit JSON, `videos/`, `scripts/`, `docs/` or `regenerated-2.5/` file was edited, no paid gate run was made, nothing was staged or committed. V-Qfwjo28Zg stays blocked.

## 0. Baseline and how to read this brief

- Baseline summary: `audit/V-Qfwjo28Zg/regenerated-2.5/summary.md`, SHA-256 `970a54c9e30fceb11fb27b3011a905f035b8adec38082272672a32a71c80974d`. **Hash confirmed** with `sha256sum` before any work; it equals `summary_sha256` in `gate-970a54c9/review.md`.
- Gate run 2 (`regenerated-2.5/gate-970a54c9/`): 566 claims, 524 pass, 42 fail, 21 concerns (12 material, 9 minor), 16 omissions, `coverage_complete` false. Verdict fail.
- **Claim ids.** Rows use the **run-2 id** (the id in the baseline `review.md`). The ids in the ticket carry-over list (c042, c167 … c484, c297 …) are 2.4 ids, and some collide with a different run-2 claim (run-2 c370 and c480 are other claims). Mapping used: 2.4 c042 = run-2 c047, 2.4 c297 = run-2 c238, 2.4 c301 = run-2 c242, 2.4 c167 = run-2 c263, 2.4 c209 = run-2 c302, 2.4 c360 = run-2 c359, 2.4 c367 = run-2 c384, 2.4 c370 = run-2 c387, 2.4 c464 = run-2 c461, 2.4 c465 = run-2 c462, 2.4 c480 = run-2 c474, 2.4 c483 = run-2 c477, 2.4 c484 = run-2 c478.
- The 46 undecided corrections are audit-record ids from `proposed-corrections.md`. Every one maps to exactly one run-2 claim with identical text (checked); the audit id is shown on each row. `proposed-corrections.md` is the source of truth; `proposed-corrections.json` was not used.
- "Protected" = wording fixed by an owner decision from 2.4 (`human-decisions.md`, the "Quyết định người duyệt" lines in `proposed-corrections.md`, `regenerated/owner-decision-brief.md`). Only protected rows are listed with a reason; I did not change any of them.
- Fix text marked "proposal" comes from `proposed-corrections.md` and has not been reviewed by the owner. Text marked "drafted" was written for this brief strictly from the transcript quote shown; check it before applying. Nothing medical is added in either.
- Quote check: every reviewer quote below was matched against `regenerated/transcript.md` where it is a single passage. Links are `?t=` seconds of the quote start.

### 0.1 What the merged list contains

| Source | Count | Where it lands |
|---|---|---|
| Run-2 failures | 42 | 42 rows |
| Concerns | 21 (12 material, 9 minor) on 19 claims (c159, c240 have two) | 18 of the 19 claims are already failures; the 19th, **c473**, passes and is its own row |
| Undecided corrections | 46 | 18 are also failures; **28 pass** in run 2 and are their own rows (groups G1, G2) |
| Carry-over duplicates | 4 (2.4 c297, c301, c464, c465) | 4 rows (pass in all runs), group E |
| Carry-over moved, no quote | 9 (2.4 c042, c167, c209, c360, c367, c370, c480, c483, c484) | all 9 are run-2 failures; flagged `carry-over` inside groups A, C, D, F |
| Omissions | 16 | 16 rows, section 4 |
| Header tag split | 1 | 1 row, section 5 |
| **Total rows** | **75 claim rows + 16 omissions + 1 tag = 92** | 42 + 1 (c473) + 28 + 4 = 75 claim rows |

## 1. Decide by group (summary)

| Group | What it is | Rows | Recommended default | Decision for you |
|---|---|---|---|---|
| A | Added or changed detail (the summary says more, less or something else than the transcript) | 18: c046, c047, c068, c086, c110, c123, c129, c155, c159, c199, c225, c236, c240, c263, c359, c448, c482, c507 | Fix all 18 with the wording below (strictly from the transcript). | approve / change |
| B | Attribution (who said it: doctor, host, viewer, a guess) | 4: c196, c208, c216, c450 | Fix all 4 (attribution to the right speaker). | approve / change |
| C | "Phần nhận xét" cluster (03:25–03:36, text read out; the gate cannot tell the reader is the doctor) | 6: c368, c370, c384, c387, c388, c391 | Fix all 6: "Phần nhận xét nói …" instead of "Bác sĩ nói …". Alternative needs your input (see group C). | approve / change |
| D | Owner-confirmed labels, and numbers/names the transcript only partly gives | 9: c113, c302, c318, c331, c371, c473, c474, c477, c552 | Accept the 7 protected rows with their reasons; fix the 2 unit rows (c318, c331) with the transcript unit. | approve / change |
| E | Duplicates (carry-over from 2.5) | 4: c238, c242, c461, c462 | Keep all 4. | approve / change |
| F | No transcript evidence found by the gate (bridge sentences, summaries of a sequence) | 6: c087, c154, c184, c245, c375, c478 | Fix 5 with transcript wording; drop c478. | approve / change |
| G1 | Undecided corrections that pass in run 2: fix recommended | 16: c034, c056, c066, c105, c145, c161, c186, c203, c204, c206, c262, c272, c275, c276, c294, c444 | Fix 16 (changed speaker, number, order, condition or scope). | approve / change |
| G2 | Undecided corrections that pass in run 2: keep recommended | 12: c081, c107, c149, c162, c231, c281, c282, c348, c354, c367, c540, c561 | Keep 12 (hedge or tone only; the gate passes them). | approve / change |
| H | Omissions (section 4) | 16 | Add 8 that appeared in both runs; accept 8 that appeared only in run 2 | approve / change |
| T | Header tag split (section 5) | 1 | Apply (already decided in 1.14) | confirm |

Totals of the recommendation over the 75 claim rows: **52 fix, 16 keep, 7 accept** (plus 8 omissions to add, 8 to accept, 1 tag change).

### 1.1 Two decisions that change the plan

**D0. The gate cannot reach a literal "pass" while owner-confirmed labels stay in the summary.** Need your decision before any paid run.
- `scripts/review_summaries.py::determine_verdict` returns `fail` if any claim fails or any concern is material or any omission exists, and `flag` (not pass) if any minor concern exists. It cannot see the owner decisions.
- Seven protected rows fail or raise concerns in every run for that reason: c113 (reviewer wants "xương cổ đùi"), c302, c371 (owner labels the transcript cannot confirm), c474, c477, c552 (editorial notes with no transcript quote, so "no transcript evidence found"), and c473 (minor concern, GSGS vs GSSG).
- Ticket requirement 4 ends the loop at verdict pass, and requirement 5 says an accepted claim does not make the verdict pass. Both cannot hold with these rows kept.
- Options: **(a, recommended)** keep your 2.4 decisions; the closing record lists the 7 rows as accepted with reasons and defines done as "the only failures and concerns are the accepted list, and `coverage_complete` is true"; the verdict stays literally `fail`/`flag`. **(b)** reopen the 2.4 decisions and reword or drop the five labels so the transcript can confirm them (loses your confirmations of GSSG, NADPH, Nhật Bản, 5.600, 6.000–7.000). **(c)** change the gate to read an accepted list; this is pipeline code, outside this ticket.
- Also: `coverage_complete` is true only when the omission list is empty (`parse_coverage_audit`), so every omission the auditor proposes must be added or the run cannot close either; section 4 and the budget depend on this.

**D1. Group C: who reads the 03:20–03:36 commentary?** The gate fails six claims because the passage never says the reader is the doctor (one reviewer note at 03:39:02 even calls it "bản nhận xét do bác sĩ viết"). Recommended: say "Phần nhận xét nói …", as the 2.5/2.4 summary already does for c359. If you know the doctor is the author and reader, you can confirm it, but a confirmation the transcript cannot show would fail the gate every run, like D0.

## 2. Claim rows by group

### Group A — Added or changed detail (the summary says more, less or something else than the transcript) (18 rows)

#### c046 — 00:33:42 · Hydro peroxit (H₂O₂, oxy già)
- Why it is in the list: run-2 FAIL; undecided correction (audit id c045); concern: minor
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Theo bài, H₂O₂ được cho vào vết thương để phá hủy mô hoại tử, virus và vi khuẩn, làm sạch vết thương, và sủi bọt.
- Reviewer [00:38:37-00:38:44]: Các tác dụng phá hủy mô, virus, vi khuẩn, làm sạch và sủi bọt được nêu; nguồn chỉ nói mô, không xác định đó là mô hoại tử.
- Concern (minor): c046 thêm tính chất hoại tử cho mô bị oxy già phá hủy, trong khi lời nói tại đây chỉ nêu mô nói chung.
- Transcript [00:38:37-00:38:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2317s): “nó phá hủy các cái mô, nó phá hủy virus vi khuẩn, nó làm sạch những cái vết thương và nó đùn đẩy lên >> sủi bọt >> trên sủi bọt lên.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Theo bài, H₂O₂ được cho vào vết thương; bác sĩ nói nó phá hủy các mô, phá hủy virus vi khuẩn, làm sạch vết thương và sủi bọt.

#### c047 — 00:33:42 · Hydro peroxit (H₂O₂, oxy già)
- Why it is in the list: run-2 FAIL; carry-over (2.4/ticket id c042)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Bài nêu enzyme SOD (superoxide dismutase) là thành phần giúp kiểm soát superoxit, buộc các phân tử này "thỏa thuận" để không còn gây nguy hiểm.
- Reviewer [00:35:22-00:35:45]: Có enzyme SOD và phép ví buộc hai gia đình thỏa thuận để không nguy hiểm; tên đầy đủ superoxide dismutase không được đọc trong phần này.
- Transcript [00:35:22-00:35:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2122s): “bản chất của nó là một cái enzyme ký hiệu là SOD. Ông tổ trưởng tổ dân phố SCOD này ông ấy thấy không ổn được khi để hai gia đình này cứ phá làng phá xóm. Vậy ông bắt hai gia đình này phải đến một căn phòng chung. >> Đến một căn phòng chung thì ông ấ bắt hai gia đình này phải tự thỏa thuận làm thế nào để cho không còn nguy hiểm nữa.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Delete the parenthetical "(superoxide dismutase)"; the transcript says only "enzyme ký hiệu là SOD". Rest of the sentence unchanged.

#### c068 — 00:48:55 · Gốc tự do tấn công màng tế bào: lipid và lipit peroxit
- Why it is in the list: run-2 FAIL; undecided correction (audit id c068)
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ nói hậu quả có thể là bệnh mãn tính, lão hóa và nhiều bệnh khác.
- Reviewer [00:06:52-00:07:02]: Có nói gốc tự do liên quan bệnh mãn tính và nhiều bệnh khác; chưa nói đến lão hóa hoặc hậu quả riêng của lipit peroxit.
- Reviewer [02:36:33-02:36:38]: Có phát biểu về lão hóa do gốc tự do; phần này không nhắc bệnh mãn tính và nhiều bệnh khác trong nhận định này.
- Transcript [00:06:52-00:07:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=412s): “hầu hết những các cái bệnh tật mãn tính, những bệnh tật cực kỳ nguy hiểm và đặc biệt kể cả những bệnh về ung thư đều xuất phát từ cái con đường của gốc tự do.”
- Transcript [02:36:33-02:36:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9393s): “Vì gốc tự do tạo ra nó gây ra hiện tượng lão hóa nhanh khủng khiếp.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói tế bào hoại tử, tế bào chết đi thì sẽ sinh ra bệnh mãn tính, sẽ bị lão hóa và sẽ bị đủ thứ bệnh.

#### c086 — 00:59:12 · Tóm tắt bảy gốc tự do và cách hiểu gốc tự do
- Why it is in the list: run-2 FAIL; undecided correction (audit id c084)
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ nói nếu chỉ đọc tài liệu thông thường thì khó hiểu, nhưng cách phân tích này giúp dễ nhớ hơn.
- Reviewer [01:08:34-01:08:45]: Có nhận xét tự đọc tài liệu khó hiểu và phần trình bày giúp hiểu gốc tự do; chưa nói rõ lợi ích dễ nhớ hơn.
- Reviewer [05:03:49-05:03:58]: Bác sĩ đối chiếu cách diễn giải với việc tự đọc tài liệu khó hiểu; không nói rõ lợi ích nhớ lâu hoặc dễ nhớ hơn.
- Transcript [01:08:34-01:08:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4114s): “nếu cho quý vị tự đọc sách, tự đọc tài liệu, chúng ta sẽ không hiểu gốc tự do là cái gì. Nhưng rõ ràng với những kiến thức mà tôi trình bày vừa rồi thì chúng ta sẽ thấy gốc tự do bản thân nó là à đứa con hoang”
- Transcript [05:03:49-05:03:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18229s): “sau khi nghe xong thấy bắt đầu nó sáng ra và dễ hiểu đúng không ạ? hơn rằng là chúng ta cứ mày mò để chúng ta đi đọc nó hơi khó khăn và không hiểu rằng tại sao nó lại như thế.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói nếu tự đi tìm đọc về gốc tự do thì "chắc chắn" sẽ không thể hiểu được vì nó rất rắc rối, nhưng nếu hiểu theo cách ông phân tích thì từ nay sẽ nhớ được.

#### c110 — 01:11:21 · Điều dưỡng kể về bố chồng tiểu đường dùng vi chất
- Why it is in the list: run-2 FAIL; undecided correction (audit id c108); concern: material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào cho thấy vi chất làm giảm đường huyết.
- Reviewer [01:12:01-01:12:12]: Người phủ nhận cơ chế là chủ nhiệm khoa, không phải điều dưỡng; phát biểu nói riêng về magie, không phải toàn bộ vi chất.
- Concern (material): c110 đổi người phát biểu từ chủ nhiệm khoa sang điều dưỡng và mở rộng nhận xét về magie thành nhận xét về mọi vi chất.
- Transcript [01:12:01-01:12:12](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4321s): “Em đã chia sẻ lại điều này cho chỉ huy khoa và các bác sĩ khác. Nhưng chủ nhiệm khoa em nói rằng không có cơ chế nào thể hiện ma dê giúp làm giảm đường huyết cả.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào thể hiện "ma dê" (bản ghi âm ghi như vậy) giúp làm giảm đường huyết.

#### c123 — 01:18:51 · Người 50 tuổi: đại tràng co thắt, táo bón, đầy đau đầu chu kỳ
- Why it is in the list: run-2 FAIL; undecided correction (audit id c121); concern: minor
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Họ cũng kể đau đầu và buồn nôn khi có chu kỳ đã hết sau nhiều tháng.
- Reviewer [01:20:00-01:20:32]: Người xem xác nhận hết đau đầu sau năm tháng, nhưng không xác nhận riêng rằng buồn nôn cũng đã hết.
- Concern (minor): c123 bổ sung kết quả hết buồn nôn dù lời tự kể chỉ xác nhận rõ hết đau đầu.
- Transcript [01:20:00-01:20:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4800s): “Không những thế, trước đây mỗi khi đến chu kỳ kinh nguyệt là tôi bị đau đầu khủng khiếp và buồn nôn nữa. Cứ đến ngày đó là tôi phải nghỉ làm. Nằm bẹp dí trong phòng kín, sợ ánh sáng, sợ âm thanh. Tiếng ồn kéo dài từ hai đến ba ngày. Mỗi lần đau tôi chỉ biết uống thuốc giảm đau dù biết là không tốt. Đau đến mức chỉ mong nhanh chóng đến tuổi mãn kinh cho đỡ đớn đau. Kỳ lạ thay, sau năm tháng bổ sung vi chất, giờ tôi …”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Họ cũng kể trước đây mỗi khi đến chu kỳ kinh nguyệt bị đau đầu khủng khiếp và buồn nôn; sau "năm tháng" bổ sung vi chất, họ nói đã hết đau đầu.

#### c129 — 01:24:09 · Phác đồ người xem đang dùng: sắt, vitamin B9, nhịn ăn gián đoạn 168
- Why it is in the list: run-2 FAIL; undecided correction (audit id c127); concern: material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ sắt II fumarat khô cùng 250 mcg vitamin B9, cùng bộ vi chất của bác sĩ.
- Reviewer [01:24:11-01:24:33]: Transcript ghi sắt hai sunfat khô, không phải sắt II fumarat khô; ngày bắt đầu và hàm lượng được giữ đúng.
- Concern (material): c129 ghi sai dạng hợp chất sắt: fumarat thay cho sunfat trong transcript.
- Transcript [01:24:11-01:24:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5051s): “Từ ngày 22 tháng 04 năm 2026, em đã bắt đầu dùng bộ vi chất bác sĩ phổ biến chung kết hợp xem các số phát sóng về sắt. Mỗi ngày em bổ sung một phiên sắt chứa 50 mg sắt nguyên tố từ sắt hai xun phát khô cộng với 250 micrg vitamin B9.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ "sắt hai xun phát khô" (bản ghi âm ghi như vậy) cùng 250 mcg vitamin B9, cùng bộ vi chất của bác sĩ.

#### c155 — 01:35:18 · Bác sĩ tổng kết: kết quả người xem gần như đạt "ngọn mục" sau khi bổ s
- Why it is in the list: run-2 FAIL; concern: material
- Runs: 2.4: fail · run 1: pass · run 2: fail; **⚠ status changed run 1→2 with identical text (pass→fail)**
- Protected wording: no
- Summary now: Bác sĩ nói mười bình luận đều liên quan đến glutathion.
- Reviewer [03:53:25-03:53:35]: Đoạn này nói mười bình luận liên quan tới gốc tự do, không phải glutathion.
- Concern (material): c155 đổi chủ đề mà bác sĩ nói mười bình luận liên quan tới từ gốc tự do thành glutathion.
- Transcript [03:53:25-03:53:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14005s): “trong số 10 bình luận của  khán giả chúng ta thấy tràn ngập những  các cái vấn đề kiến thức đều liên quan  tới cái chủ đề ngày hôm nay đó chính là  gốc tự do.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Bác sĩ nói trong mười bình luận của khán giả có tràn ngập những vấn đề kiến thức đều liên quan tới chủ đề hôm nay, đó chính là gốc tự do.

#### c159 — 01:36:23 · Lời khuyên cho học sinh hay quên bị mẹ mắng
- Why it is in the list: run-2 FAIL; undecided correction (audit id c208); concern: material, material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ nói trí tuệ không phải do trời cho mà đến từ sự cần cù, chịu khó và quyết tâm.
- Reviewer [01:37:20-01:37:47]: Bác sĩ nói không phải ai cũng được trời cho trí tuệ tốt, rồi kể bản thân thành công nhờ cần cù và quyết tâm; tóm tắt khái quát thành phủ nhận tuyệt đối trí tuệ bẩm sinh.
- Reviewer [01:37:20-01:37:47]: Nguồn nói không phải ai cũng được trời cho trí tuệ tốt, rồi kể bản thân thành công nhờ cần cù và quyết tâm. Nhận định biến điều đó thành kết luận chung rằng trí tuệ không do trời cho mà đến từ nỗ lực.
- Concern (material): c159 biến nhận xét có giới hạn và trải nghiệm cá nhân thành khẳng định tuyệt đối rằng trí tuệ không do trời cho.
- Concern (material): c159 khái quát quá mức: lời kể về việc không phải ai cũng có trí tuệ thiên phú và nỗ lực của bản thân bị chuyển thành kết luận chung về nguồn gốc trí tuệ.
- Transcript [01:37:20-01:37:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5840s): “con người ta sinh ra không phải ông trời cũng cho tất cả mọi người có được cái trí tuệ tốt, có được cái trí nhớ siêu phàm hay là có những cái năng lực tuyệt vời. Như tôi vẫn tâm sự trong nhiều số phát sóng trước đây, đó là bản thân tôi là người mà có trí tuệ không được tốt cho lắm. học cũng mọi cái của tôi cũng không phải là thông minh giỏi giang các thứ gì mà chỉ nhờ vào cái sự cần cù chịu khó, cái sự quyết tâm”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói con người sinh ra không phải ông trời cũng cho tất cả mọi người trí tuệ tốt, trí nhớ siêu phàm hay năng lực tuyệt vời; riêng bản thân ông nói mình có trí tuệ không được tốt lắm và chỉ nhờ sự cần cù chịu khó, sự quyết tâm trong những năm tháng tuổi ấu thơ.

#### c199 — 02:04:21 · Thầy Nguyễn Hiền: đau cột sống, uống nhiều thuốc và paracetamol
- Why it is in the list: run-2 FAIL; undecided correction (audit id c248); concern: minor
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Thầy Nguyễn Hiền, giáo viên vật lý, đau cột sống và đau xương hông, nghi có thể là ung thư xương, uống đủ loại thuốc kể cả kháng sinh nhưng không đỡ mà càng uống càng nặng.
- Reviewer [02:04:21-02:04:45]: Nguồn xác nhận nghề nghiệp, đau cột sống và xương hông, cảm tưởng ung thư xương, dùng nhiều thuốc kể cả kháng sinh không đỡ. Đoạn nói về đáp ứng điều trị không xác nhận chi tiết càng uống càng nặng.
- Concern (minor): c199 thêm mức độ bệnh càng nặng khi uống thuốc; lời nguồn ở đây chỉ xác nhận không đỡ.
- Transcript [02:04:21-02:04:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7461s): “Như là thầy Nguyễn Hiền, thầy giáo vật lý bắt đầu vào trường Đại học Sư phạm tôi nhớ là năm 1971. Sau đó thầy đi dạy thầy về quê thầy chuyển chỗ này chỗ khác và thầy bị đau cột sống đau xương hông rồi bị một loạt những các cái bệnh tật mà thầy cảm tưởng rằng thầy bị đến ung thư xương. Thế thì uống đủ các loại thuốc cả kháng sinh đủ các thứ nhưng cuối cùng không đỡ thầy càng uống vào.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Thầy Nguyễn Hiền, thầy giáo vật lý, đau cột sống, đau xương hông, cảm tưởng mình bị đến ung thư xương, uống đủ các loại thuốc cả kháng sinh nhưng cuối cùng không đỡ.

#### c225 — 02:13:40 · Vitamin C, E, glutathion và các vi chất phối hợp với nhau
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Ông cũng nhắc đến bo và silic là những thành phần quan trọng thường có trong sản phẩm bổ sung.
- Reviewer [04:12:57-04:13:05]: Có nhắc bo và silic là các thành phần bổ sung thêm; không nói chúng thường có trong sản phẩm hoặc đánh giá riêng tầm quan trọng.
- Transcript [04:12:57-04:13:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15177s): “Chưa kể những các cái sản phẩm mà chúng ta phải thêm đó là vitamin B7, nào là vitamin B8 đúng không ạ? Nào là bo, nào là silic.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Drop the sentence. It sits under 02:13:40 but its only evidence is 04:12:57, and c448 already states "vitamin B7, B8, bo, silic". (Alternative: "Ông cũng nhắc bo và silic trong số những thành phần phải thêm vào.")

#### c236 — 02:21:07 · Một số bệnh nhân đau dây thần kinh số 5 đỡ sau khi bổ sung vi chất
- Why it is in the list: run-2 FAIL; undecided correction (audit id c287); concern: material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Theo bác sĩ, một số bệnh nhân đến bổ sung vi chất đúng và đủ thì cơn đau biến mất hẳn, có người đỡ 90 đến 95%, và số còn lại chỉ còn đau nhẹ không đáng kể.
- Reviewer [02:21:18-02:21:26]: Nguồn nói có những người hết đau và có những người đỡ 90–95%, chỉ còn đau nhẹ. Không xác nhận toàn bộ số bệnh nhân còn lại đều chỉ đau nhẹ.
- Concern (material): c236 mở rộng kết quả của một số người thành kết quả của toàn bộ số còn lại.
- Transcript [02:21:18-02:21:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8478s): “Thế có những người đỡ được đến 8 90% 95%. Đỡ tới 90 95% là khỏi rồi. Còn cái gì nữa đâu ạ? người ta bảo chỉ còn hơi hơi không đáng kể nữa thôi.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Theo bác sĩ, sau khi những bệnh nhân đến bổ sung vi chất đúng và đủ thì có những người nói tự dưng hết hẳn, có những người đỡ được đến "8 90% 95%" và người ta bảo chỉ còn hơi hơi không đáng kể; có những người nói khỏi sau khi bổ sung vi chất.

#### c240 — 02:22:01 · Đau nửa đầu của chị Nhung và tim nhanh: kết quả sau khi bổ sung vi chấ
- Why it is in the list: run-2 FAIL; undecided correction (audit id c291); concern: material, material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Chị ăn nhiều đồng để quên cơn đau nên cân nặng tăng nhanh.
- Reviewer [01:29:17-01:29:40]: Người xem kể ăn hoặc uống đường mía thô để thấy dễ chịu khi mệt, không phải ăn “đồng” để quên cơn đau.
- Reviewer [02:22:47-02:22:57]: Nhận định ghi ăn nhiều 'đồng'; nguồn nói ăn đường để quên đau và tăng cân.
- Concern (material): c240 ghi “ăn nhiều đồng”, trong khi nguồn nói ăn hoặc uống đường mía thô khi mệt.
- Concern (material): c240 ghi nhầm đường thành đồng, làm sai chất được ăn để quên đau.
- Transcript [01:29:17-01:29:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5357s): “Trong lúc mệt mỏi, tôi ăn hoặc là uống đường mía thô thì thấy rằng cơ thể dễ chịu hơn. Từ đó tôi lạm dụng. Cứ mệt là tôi uống đường. Sau 3 tháng sử dụng lượng đường quá nhiều, cơ thể tôi gióng lên hồi chuông thê thảm nhất. Tôi bị khó thở, nhịp tim tăng lên 170 nhịp một phút, mệt mỏi, chân tay tê dại, tăng cân không phanh”
- Transcript [02:22:47-02:22:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8567s): “Đau đến nỗi mà bắt đầu bác ăn đường vào để cho quên hết tất cả. Lấy cái ngọt ngào để che lấp đi tất cả những cái cơn đau này dẫn tới là cân nặng tăng lên vù vù.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Chị ăn đường vào để quên cơn đau nên cân nặng tăng nhanh.

#### c263 — 02:34:11 · Bóng đè có nguy hiểm không và xử lý khi gặp
- Why it is in the list: run-2 FAIL; undecided correction (audit id c162); concern: minor; carry-over (2.4/ticket id c167)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, tác dụng chủ yếu là trấn an tâm lý, không phải hiệu quả thực sự.
- Reviewer [02:35:06-02:35:09]: Bản tóm tắt phủ định hiệu quả thực sự dứt khoát hơn nguồn. Bác sĩ nói “không hẳn”, chủ yếu trấn an tâm lý.
- Concern (minor): c263 làm mất mức dè dặt “không hẳn”, chuyển nhận xét chủ yếu trấn an tâm lý thành phủ định hiệu quả thực sự.
- Transcript [02:35:06-02:35:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9306s): “Chứ còn nó hiệu quả thực sự thì nó không hẳn chủ yếu là trấn an tâm lý.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, về mặt tinh thần để trấn an tâm lý; ông nói "chứ còn nó hiệu quả thực sự thì nó không hẳn chủ yếu là trấn an tâm lý" (bản ghi âm ghi như vậy) rồi đi sâu hơn vào nguyên nhân.

#### c359 — 03:21:06 · Chỉ số TSAT, feritin và biểu hiện thiếu sắt
- Why it is in the list: run-2 FAIL; undecided correction (audit id c352); concern: material; carry-over (2.4/ticket id c360)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Phần nhận xét nói kết hợp kho sắt đóng và lượng sắt lưu hành giảm không gây nguy hiểm đến tính mạng, nhưng làm chậm phân phối năng lượng tạo máu.
- Reviewer [03:23:25-03:23:36]: Nguồn nói số xe chở sắt giảm, tức phương tiện vận chuyển sắt, không phải lượng sắt lưu hành giảm; trước đó còn khẳng định lượng sắt lưu hành vẫn ổn định.
- Concern (material): c359 đổi sự sụt giảm phương tiện vận chuyển sắt thành sự giảm lượng sắt lưu hành, trong khi nguồn khẳng định lượng sắt lưu hành vẫn ổn định.
- Transcript [03:23:25-03:23:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12205s): “Sự kết hợp giữa một kho sắt đóng mất cửa với số lượng xe trở sắt bị sụt giảm, không gây ra nguy cấp tử sinh nhưng nó tạo nên một sự trì trệ [âm nhạc] trong việc phân phối năng lượng tạo máu.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Phần nhận xét nói sự kết hợp giữa kho sắt đóng cửa với số lượng xe chở sắt bị sụt giảm không gây nguy cấp tử sinh, nhưng tạo nên sự trì trệ trong việc phân phối năng lượng tạo máu.

#### c448 — 04:13:09 · Glutathione là chủ đề của ngày hôm nay và được truyền thông mô tả thế 
- Why it is in the list: run-2 FAIL; undecided correction (audit id c447); concern: minor
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Ông cũng nhắc rằng ngoài bảy nhóm vi chất còn có khoảng 18 sản phẩm thuộc các nhóm này, cùng các thành phần khác như vitamin B7, B8, bo, silic và glutathione.
- Reviewer [04:12:52-04:13:11]: Nguồn nói ít nhất 18 sản phẩm; bản tóm tắt đổi giới hạn tối thiểu thành khoảng 18.
- Concern (minor): c448 đổi ít nhất 18 sản phẩm thành khoảng 18, làm mất giới hạn tối thiểu được bác sĩ nhấn mạnh.
- Transcript [04:12:52-04:13:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15172s): “chúng ta phải ít nhất có 18 cái sản phẩm đúng không ạ? 18 sản phẩm nằm trong bảy nhóm này. Chưa kể những các cái sản phẩm mà chúng ta phải thêm đó là vitamin B7, nào là vitamin B8 đúng không ạ? Nào là bo, nào là silic. Hôm nay chúng ta lại đến Glutathion đúng không ạ?”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Ông cũng nhấn mạnh rằng trong bảy nhóm vi chất phải ít nhất có 18 sản phẩm, chưa kể những sản phẩm phải thêm như vitamin B7, B8, bo, silic, và hôm nay là glutathion.

#### c482 — 04:37:48 · Những nguồn nào sinh ra gốc tự do?
- Why it is in the list: run-2 FAIL; undecided correction (audit id c478)
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ nêu ba nguồn chính.
- Reviewer [04:37:48-04:38:02]: Mới có nguồn thứ nhất là tinh thần và tiếp theo là ăn uống; lát cắt kết thúc trước nguồn thứ ba, chưa xác nhận tổng số ba.
- Reviewer [04:37:48-04:37:50]: Có liệt kê các nguồn, nhưng không chốt tổng số ba nguồn chính; kim loại nặng còn được nêu riêng sau tinh thần, ăn uống và thuốc.
- Transcript [04:37:48-04:38:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16668s): “Thì đầu tiên cái thứ nhất là liên quan tới yếu tố tinh thần mà lúc nãy chúng ta phân tích suốt rồi đúng không ạ? >> Yếu tố tinh thần rất quan trọng. Tiếp theo đó là do cái gì? Những các cái gì nó gây ra? Ta nhắc lại cái là do đồ ăn thức uống của chúng ta đúng không ạ?”
- Transcript [04:37:48-04:37:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16668s): “Thì đầu tiên cái thứ nhất là liên quan tới yếu tố tinh thần”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Đầu tiên bác sĩ nói cái thứ nhất là yếu tố tinh thần; tiếp theo ông đánh số: thứ nhất là ăn uống, thứ hai là thuốc, thứ ba là kim loại nặng.

#### c507 — 04:50:35 · Glutathion bảo vệ ti thể và năng lượng tế bào
- Why it is in the list: run-2 FAIL; undecided correction (audit id c500); concern: minor
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Ti thể có ADN riêng nằm sát màng trong, nên gốc tự do thấm qua có thể phá hủy ADN này và gây đột biến.
- Reviewer [04:51:57-04:52:04]: Nguồn xác nhận ADN riêng nằm sát màng ti thể và có thể bị phá hủy, đột biến; không xác định đó là màng trong. Nhận định thêm độ chính xác về vị trí mà nguồn không cung cấp.
- Concern (minor): c507 thêm vị trí màng trong, trong khi nguồn chỉ nói ADN nằm sát màng ti thể.
- Transcript [04:51:57-04:52:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17517s): “ADN là vật chất di truyền rất quan trọng. Thế mà nằm ở sát màng ti thể này dẫn tới là các gốc tự do nó thấm qua đây thì phá hủy gì ạ? ADN”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Ti thể có ADN riêng nằm sát màng ti thể, nên các gốc tự do thấm qua thì phá hủy ADN riêng này, tạo thành gốc tự do và bị đột biến.

### Group B — Attribution (who said it: doctor, host, viewer, a guess) (4 rows)

#### c196 — 02:03:37 · Chia sẻ của khán giả ở Đức và Tokyo sau khi bổ sung vi chất
- Why it is in the list: run-2 FAIL; undecided correction (audit id c245); concern: minor
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác Thủy ở Đức kể sau khi bổ sung vi chất, mọi người xung quanh ốm nhưng bác không sao.
- Reviewer [02:03:42-02:03:50]: Kết quả được thuật lại đúng, nhưng tên Thủy chỉ là phỏng đoán của bác sĩ; nhận định bỏ mất giới hạn này.
- Concern (minor): c196 xác định tên người xem là Thủy trong khi bác sĩ chỉ đoán tên.
- Transcript [02:03:42-02:03:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7422s): “Thì bác ở bên Đức tôi đoán bác tên là Thủy. Thì bác thấy rằng sau khi bác bổ sung vi chất tất cả mọi người xung quanh đều quay ra ốm nhưng bác chẳng làm sao hết cả.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Một bác ở Đức (bác sĩ nói "tôi đoán bác tên là Thủy") kể sau khi bổ sung vi chất, mọi người xung quanh đều quay ra ốm nhưng bác không sao.

#### c208 — 02:06:24 · Trường hợp chị Ngọc Thơ: vàng da, vàng củng mạc mắt và hemoglobin thấp
- Why it is in the list: run-2 FAIL; undecided correction (audit id c256); concern: material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Người dẫn chương trình đặt nghi vấn chị đang bị thiếu máu nhược sắc do thiếu sắt, gây tan hồng cầu và vàng da.
- Reviewer [02:07:41-02:08:02]: Bác sĩ quy giả thuyết thiếu máu thiếu sắt cho chính người bình luận. Người dẫn tiếp lời về thiếu máu nhược sắc và tan hồng cầu, không được chứng minh là người đặt nghi vấn ban đầu.
- Concern (material): c208 quy việc đặt giả thuyết thiếu máu thiếu sắt cho người dẫn, trong khi bác sĩ đang thuật giả thuyết của người bình luận.
- Transcript [02:07:41-02:08:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7661s): “Cuối cùng là cái vàng đó chị đặt ra một cái điều rất hay đó là có phải sau khi tìm hiểu cũng như nghe trên kênh tìm hiểu các tài liệu thì chị thấy rằng đây chị đang rơi vào trường hợp là thiếu máu thiếu sắt, >> thiếu máu nhược sắc do thiếu sắt và nó gây ra một cái hiện tượng là tan hồng cầu.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Chị, người viết bình luận, tự cho rằng có lẽ mình thiếu sắt nhược sắc; bác sĩ thuật lại câu hỏi chị đặt ra là có phải thiếu máu nhược sắc do thiếu sắt gây tan hồng cầu và vàng da hay không.

#### c216 — 02:10:50 · Rối loạn tụy, tiểu đường và cân nặng sau khi bổ sung vi chất
- Why it is in the list: run-2 FAIL; concern: minor
- Runs: 2.4: pass · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Chị Ngân đã đề nghị trưởng khoa xem xét nhưng trưởng khoa không đồng ý, vì nghiên cứu dinh dưỡng để có bằng chứng thực chứng rất khó khi không thể dừng mọi thứ khác của bệnh nhân để chỉ bổ sung một thứ.
- Reviewer [02:11:09-02:11:13]: Lý giải về khó khăn thực chứng là lời bác sĩ. Đoạn nói trưởng khoa 'sẽ không đồng ý' bị chuyển thành một sự từ chối đã được xác nhận.
- Concern (minor): c216 chuyển dự đoán trưởng khoa sẽ không đồng ý thành sự từ chối đã xảy ra.
- Transcript [02:11:09-02:11:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7869s): “Chị mang cái điều đó đến trưởng khoa để thuyết phục thì trưởng khoa sẽ không đồng ý.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Bác sĩ nói nếu chị Ngân mang điều đó đến trưởng khoa để thuyết phục thì trưởng khoa sẽ không đồng ý; ông giải thích rằng nghiên cứu dinh dưỡng để có bằng chứng thực chứng rất khó khi không thể dừng mọi thứ khác của bệnh nhân để chỉ bổ sung một thứ. (Check the explanation clause against the transcript right after 02:11:13 before applying.)

#### c450 — 04:13:09 · Glutathione là chủ đề của ngày hôm nay và được truyền thông mô tả thế 
- Why it is in the list: run-2 FAIL; undecided correction (audit id c449); concern: material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ nói những lời truyền miệng này "hào nhoáng" và cần nhìn lại dưới góc nhìn y khoa.
- Reviewer [04:17:42-04:17:49]: Nhận xét hào nhoáng và lời dẫn sang góc nhìn y khoa do Khánh Lành nói trước khi mời bác sĩ, không phải lời bác sĩ.
- Concern (material): c450 gán lời người dẫn Khánh Lành cho bác sĩ: nhận xét lời truyền miệng hào nhoáng xuất hiện trong phần dẫn trước khi mời bác sĩ.
- Transcript [04:17:42-04:17:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15462s): “Vâng. Thế nhưng đằng sau những lời chuyển miệng hào nhoáng ấy, báo chí và truyền thông cũng ghi nhận không ít những khoảng tối hoang mang.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Khánh Lành, trong phần giới thiệu, nói đằng sau những lời truyền miệng hào nhoáng ấy, báo chí và truyền thông cũng ghi nhận không ít những khoảng tối, và đặt câu hỏi glutathion thực sự là gì dưới góc nhìn y khoa.

### Group C — "Phần nhận xét" cluster (03:25–03:36, text read out; the gate cannot tell the reader is the doctor) (6 rows)

Run-2 ids c368, c370, c384, c387, c388, c391. Carry-over: c384 = 2.4 c367, c387 = 2.4 c370 (both moved with no quote in 2.5). None of this wording is protected. Recommended fix is the same for all six: attribute to the commentary, keep what the quote says.

#### c368 — 03:25:00 · Điều đáng bận tâm hơn feritin và TSAT: viêm mạn tính
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Theo bác sĩ, điều đáng bận tâm hơn nằm ở ngọn lửa viêm mạn tính.
- Reviewer [03:25:00-03:25:10]: Nội dung có trong phần nhận xét; đoạn này không xác định người đọc là bác sĩ.
- Reviewer [03:39:02-03:39:11]: Bản nhận xét do bác sĩ viết có yêu cầu dập tắt viêm mạn tính; không so sánh mức đáng lo với feritin hay TSAT.
- Transcript [03:25:00-03:25:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12300s): “Như vậy, điều đáng bận tâm của bác không nằm ở con số feritin hay là TSAT mà nằm ở chỗ làm sao để vỗ về ngọn lửa viêm mạn tính.”
- Transcript [03:39:02-03:39:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13142s): “Tế bào của bác cần được nuôi dưỡng, tái  tạo và dập tắt ngọn lửa viêm mạn tính  bằng cách cung cấp đầy đủ, kiên trì và  chuẩn xác nguồn nguyên liệu đầu vào.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Replace "Theo bác sĩ" with "Phần nhận xét nói" and follow the source: "điều đáng bận tâm của bác không nằm ở con số feritin hay TSAT mà nằm ở chỗ làm sao để vỗ về ngọn lửa viêm mạn tính".

#### c370 — 03:25:17 · Vitamin B12 838,9: có đáng lo không và các nguyên nhân tăng giả
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ nói rằng nhiều người có thể hoảng khi thấy chỉ số này cao, nhưng theo góc nhìn y khoa hiện đại thì đây là chỉ số cần được hiểu một cách điềm tĩnh.
- Reviewer [03:25:26-03:25:39]: Có lời giải thích về thái độ điềm tĩnh trước B12 tăng; đoạn này không xác định người đọc là bác sĩ.
- Transcript [03:25:26-03:25:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12326s): “nhiều người có thể giật mình cho rằng chỉ số này đang tăng cao nguy hiểm. Nhưng đứng dưới góc nhìn y khoa hiện đại [âm nhạc] và chăm sóc sức khỏe toàn diện, đây lại là một chỉ số cần được thấu hiểu bằng sự điềm tĩnh và thấu đáo.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Replace "Bác sĩ nói rằng" with "Phần nhận xét nói"; the rest follows the quoted lines ("giật mình … nhưng đứng dưới góc nhìn y khoa hiện đại …").

#### c384 — 03:28:54 · Chụp CT lồng ngực của bác Lương Trắc Nghiên: xẹp thùy phổi và đường dẫ
- Why it is in the list: run-2 FAIL; carry-over (2.4/ticket id c367)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Bác sĩ liên hệ với việc bác hút thuốc để quên nỗi buồn sau khi vợ mất và làm nghề thợ mộc hàng chục năm.
- Reviewer [02:54:20-02:54:36]: Hồ sơ kể nghề mộc và hút thuốc giải tỏa sau khi vợ mất. Chưa có liên hệ chuyên môn của bác sĩ với tổn thương phổi hoặc thời gian làm mộc hàng chục năm.
- Reviewer [03:28:54-03:29:14]: Có liên hệ giữa mất vợ, hút thuốc và nghề mộc lâu năm; đoạn này không xác định người đọc là bác sĩ.
- Reviewer [03:58:41-03:58:59]: Bác sĩ liên hệ mất vợ, hút thuốc và nghề mộc; không xác định thời gian làm nghề là hàng chục năm.
- Transcript [02:54:20-02:54:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10460s): “từng làm nghề mộc và hiện đang sinh sống tại Hưng Yên. Bi kịch xảy đến với tôi khi mới 37 tuổi. Người vợ thân yêu đột ngột qua đời vì bệnh tim, để lại một mình tôi gà trống nuôi con. Trong những năm tháng cô đơn và đầy biến cố ấy, tôi từng tìm đến thuốc lá như một cách giải tỏa rồi bị nghiện nhiều năm.”
- Transcript [03:28:54-03:29:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12534s): “Sự cô đơn quánh đặc sau cái chết của người bạn đời cộng hưởng với hàng vạn bao thuốc lá rút ra trong những đêm đông cô quạnh để sởi ấm tâm hồn. Cùng hàng chục năm lăn lộn với nghề thợ mộc, hít chọn từng hạt bụi gỗ ly ti bay lơ lửng trong không khí đã tạo nên cái nhân nghiệt ngã tàn phá lồng ngực của bác.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Phần nhận xét liên hệ việc bác hút thuốc lá để quên nỗi buồn sau khi vợ mất với nghề thợ mộc lâu năm. (Drops "hàng chục năm": no duration is stated at 03:28:54.)

#### c387 — 03:31:26 · Đợt suy hô hấp cấp và động mạch chủ: vì sao canxi bám thành mạch
- Why it is in the list: run-2 FAIL; carry-over (2.4/ticket id c370)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Theo bác sĩ, canxi bị rút khỏi xương do suy dinh dưỡng, thiếu vitamin D và magie kéo dài, rồi bám vào thành mạch máu, khiến động mạch trở nên xơ cứng.
- Reviewer [03:32:04-03:32:23]: Có đầy đủ cơ chế được mô tả; đoạn này không xác định người đọc là bác sĩ.
- Reviewer [04:02:41-04:02:58]: Có thiếu vi chất, rút canxi từ xương và lắng đọng gây vôi hóa mạch; không nêu riêng thiếu vitamin D và magie kéo dài.
- Transcript [03:32:04-03:32:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12724s): “Đây là cái quả đắng ngắt của hiện tượng canxi bị rút khỏi hệ thống xương do tình trạng suy dinh dưỡng, thiếu hụt vitamin D và mag kéo dài để rồi dòng canxi đi lang thang ấy lại bám chặt vào thành mạch máu, biến con sông từng dẻo dai thời trai trẻ thành một đường ống sơ cứng.”
- Transcript [04:02:41-04:02:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14561s): “Bác lại sống cuộc  sống là thiếu vi chất nó hút từ xương  da, canxi ra hút quá đà nó lắng đọng ở  trên thành mạch nó làm loét tổn thương  mạch máu. Các cái gốc tự do này nó gây  ra loét mạch máu nhưng lại không có tiểu  cầu vá thì sẽ dẫn tới bác sẽ bị gì ạ? Sẽ  bị vôi hóa các cái thành mạch.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Replace "Theo bác sĩ" with "Phần nhận xét nói"; the rest follows the 03:32:04 quote ("suy dinh dưỡng, thiếu hụt vitamin D và magie …").

#### c388 — 03:34:58 · Uống đủ nước và uống nước ấm
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ nói bác Nghiên đã nhiều năm quên cách uống nước, chỉ uống khi cổ họng khô khốc.
- Reviewer [03:34:58-03:35:05]: Có mô tả thói quen uống nước; đoạn này không xác định người đọc là bác sĩ.
- Transcript [03:34:58-03:35:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12898s): “Đã bao năm rồi bác quên mất cách uống nước, chỉ đợi khi cổ họng khô khốc mới nhấp một cụm nhỏ”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Replace "Bác sĩ nói" with "Phần nhận xét nói"; rest unchanged.

#### c391 — 03:35:43 · Hướng xử lý ban đầu cho viêm phổi tắc nghẽn mạn tính: giải thoát tâm t
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Theo bác sĩ, việc đầu tiên là giải thoát tâm thức và xoa dịu lồng ngực đang ngột ngạt vì viêm phổi tắc nghẽn mạn tính.
- Reviewer [03:35:35-03:35:43]: Có hướng xử lý đầu tiên như claim; đoạn này không xác định người đọc là bác sĩ.
- Reviewer [04:09:17-04:09:21]: Có khuyên giải quyết tinh thần, buông bỏ nỗi buồn; không có nguyên văn chỉ dẫn đầu tiên xoa dịu lồng ngực ngột ngạt.
- Transcript [03:35:35-03:35:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12935s): “Việc đầu tiên là phải giải thoát cho tâm thức và xoa dịu lồng ngực đang ngột ngạt vì căn bệnh viêm phổi tắc nghẽn mạn tính.”
- Transcript [04:09:17-04:09:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14957s): “bác giải quyết cái vấn đề tinh thần. Tức là cuộc sống chúng ta phải buông bỏ.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Replace "Theo bác sĩ" with "Phần nhận xét nói"; rest unchanged (supported at 03:35:35).

### Group D — Owner-confirmed labels, and numbers/names the transcript only partly gives (9 rows)

Protected rows come with the owner decision that protects them. They are expected to stay failing (see D0). c318 and c331 are not protected: the transcript gives the unit only as "m/l" and "n/ml".

#### c113 — 01:12:21 · Người xem bị đau lưng, thoái hóa, theo dõi kênh từ năm 2024
- Why it is in the list: run-2 FAIL; concern: material
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: YES: owner decision 2.4 (human-decisions.md, c111): "xương cổ, xương đùi" is correct; original sentence stays
- Summary now: Họ nói đã hết đau cột sống, xương cổ, xương đùi và xương quai xanh, và không còn tê nửa người bên trái.
- Reviewer [01:13:48-01:14:01]: Transcript nói “xương cổ đùi”, không phải hai vị trí “xương cổ, xương đùi”.
- Concern (material): c113 tách sai thuật ngữ giải phẫu “xương cổ đùi” thành xương cổ và xương đùi.
- Transcript [01:13:48-01:14:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4428s): “Tôi nhận thấy mình không còn bị đau cột sống, xương cổ đùi và xương quai xanh nữa. Những nơi mà trước đây đau đến mức tôi từng tưởng như là mình bị ung thư xương. Tôi cũng không còn bị tê dọc nửa người bên trái.”
- **Recommend: ACCEPT** — Protected by the owner decision on c111. The reviewer wants the verbatim "xương cổ đùi"; the owner ruled "xương cổ, xương đùi" is right. Keep; list as accepted.

#### c302 — 02:44:45 · Vitamin D 50.000 IU: nồng độ mục tiêu và cách duy trì
- Why it is in the list: run-2 FAIL; carry-over (2.4/ticket id c209)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: YES: owner decision 2.4 (human-decisions.md, c201): "trên dưới 2.000 UI"; 5.600 and 6.000–7.000 confirmed by owner; wording and label applied in 2.4
- Summary now: Có người chỉ cần khoảng 5.600 UI, có người lên tới 6.000 đến 7.000 UI (hai con số này là xác nhận của người duyệt; phiên âm chỉ ghi "5 600" và "6 7000"), nhưng đại đa số mọi người là con số trên dưới 2.000 UI.
- Reviewer [02:49:13-02:49:20]: Nguồn có các chuỗi “5 600”, “6 7000” và mức đại đa số trên dưới 2.000 UI. Phần này không xác minh lời xác nhận của người duyệt hay cách diễn giải chính xác hai chuỗi số.
- Transcript [02:49:13-02:49:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10153s): “Có người chỉ có 5 600 UI đã đủ rồi nhưng có người lên tới 6 7000 UI cơ. >> Vâng. >> Nhưng đại đa số mọi người là con số trên dưới 2000 UI.”
- **Recommend: ACCEPT** — Protected (owner decision on c201). The reviewer cannot verify the owner label; the transcript does contain the strings "5 600", "6 7000" and "trên dưới 2.000 UI" (02:49:13). Keep; list as accepted.

#### c318 — 02:56:30 · Chức năng gan, thận và mỡ máu của bác Lương Trắc Nghiên
- Why it is in the list: run-2 FAIL
- Runs: 2.4: pass · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Ure máu là 7,4 mmol/L, sát ngưỡng trên của khoảng 2,5 đến 7,5.
- Reviewer [02:56:43-02:56:50]: Giá trị, khoảng tham chiếu và nhận xét sát ngưỡng trên đều có. Đơn vị chỉ được phiên âm là “m/l”, chưa xác nhận đầy đủ mmol/L.
- Transcript [02:56:43-02:56:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10603s): “về chức năng thận ure máu là 7,4 m/l bình thường sát ngưỡng trên khoảng tham chiếu từ 2,5 đến 7,5.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Ure máu là 7,4 (đơn vị phiên âm ghi là "m/l"), sát ngưỡng trên của khoảng tham chiếu từ 2,5 đến 7,5. (Writing "mmol/L" is an unit the transcript does not give. If the owner would rather confirm the unit, use the owner-label form; the gate will then keep failing it, like c371.)

#### c331 — 02:57:43 · Sắt, vitamin và khoáng chất: feritin, TSAT và biểu hiện thiếu sắt
- Why it is in the list: run-2 FAIL
- Runs: 2.4: pass · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Vitamin D là 31,76 ng/ml.
- Reviewer [02:58:24]: Giá trị 31,76 được nêu; đơn vị phiên âm là “n/ml”, chưa xác nhận đầy đủ ng/ml.
- Transcript [02:58:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10704s): “Vitamin D là 31,76 n/ml.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Vitamin D là 31,76 (đơn vị phiên âm ghi là "n/ml"). Same unit remark as c318.

#### c371 — 03:25:17 · Vitamin B12 838,9: có đáng lo không và các nguyên nhân tăng giả
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: YES: owner decision 2.4 (human-decisions.md, c377): the country is Nhật Bản; kept with the label "xác nhận của người duyệt"
- Summary now: Ông so sánh với quy chuẩn tham chiếu của nhiều quốc gia phát triển như Nhật Bản (xác nhận của người duyệt; phiên âm không chứa), nơi giới hạn trên thường được mở rộng lên tới 1000 hoặc thậm chí 1500 pg/ml, và cho rằng con số của bác vẫn hoàn toàn nằm trong ngưỡng an toàn.
- Reviewer [03:25:43-03:25:59]: Có các mức 1000, 1500 và nhận định an toàn. Phiên âm không ghi rõ Nhật Bản, không có xác nhận của người duyệt và không xác định người đọc là bác sĩ.
- Transcript [03:25:43-03:25:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12343s): “Nếu so sánh với quy chuẩn tham chiếu của nhiều quốc gia phát triển như bản, nơi giới hạn trên của vitamin P12 thường được mở rộng lên tới 1000 picog [âm nhạc] ml hoặc thậm chí là 1500 thì con số của bác vẫn hoàn toàn nằm trong ngưỡng an toàn của cơ thể.”
- **Recommend: ACCEPT** — Protected (owner decision on c377, Nhật Bản). "bản" is in the transcript, "Nhật Bản" is not; the label says so. Keep; list as accepted.

#### c473 — 04:29:03 · Cấu tạo, hoạt động và tái tạo của glutathion (tiếp)
- Why it is in the list: concern: minor
- Runs: 2.4: fail · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: YES: owner decision 2.4 (human-decisions.md, c471): GSSG accepted; the note is the owner-confirmation label
- Summary now: Hai glutathion hỏng sẽ khóa vào nhau tạo thành GSSG.
- Concern (minor): Bản ghi có bất nhất về ký hiệu phức hợp glutathion: đoạn này ghi GSGS, trong khi đoạn tái tạo sau đó đọc tách GS và SG. Cần giữ lưu ý phiên âm khi xác minh ký hiệu GSSG ở c473.
- Transcript [04:31:49-04:31:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16309s): “để tạo nên một cái phức hợp gọi là GSGS.”
- **Recommend: ACCEPT** — Protected (owner decision on c471, GSSG). Run 2 passes it; only a minor concern about the "GSGS" transcription remains, which is what the label already says.

#### c474 — 04:29:03 · Cấu tạo, hoạt động và tái tạo của glutathion (tiếp)
- Why it is in the list: run-2 FAIL; carry-over (2.4/ticket id c480)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: YES: owner decision 2.4 (human-decisions.md, c471): GSSG accepted; the note is the owner-confirmation label
- Summary now: Ghi chú: GSSG là xác nhận của người duyệt; phiên âm không chứa (phiên âm ghi "GSGS").
- Reviewer: no transcript evidence found in any chunk
- Transcript [04:31:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16312s): “phức hợp gọi là GSGS.”
- **Recommend: ACCEPT** — Protected: it is the owner-confirmation note for c471 (GSSG). It is an editorial note, so the gate can never find a transcript quote for it. Keep; list as accepted.

#### c477 — 04:29:03 · Cấu tạo, hoạt động và tái tạo của glutathion (tiếp)
- Why it is in the list: run-2 FAIL; carry-over (2.4/ticket id c483)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: YES: owner decision 2.4 (human-decisions.md, c473): NADPH accepted; the note is the owner-confirmation label
- Summary now: Ghi chú: NADPH là xác nhận của người duyệt; phiên âm không ghi đúng "NADPH"; có "NA"/"DPH" ngắt dòng và "NADH".
- Reviewer [04:32:24-04:32:39]: Bản ghi xác nhận các dạng NA/DPH và NADH; việc người duyệt xác nhận NADPH là thông tin biên tập không nằm trong lời thoại.
- Transcript [04:32:24-04:32:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16344s): “nó cần phải cung cấp năng lượng là NA DPH. Đây là cái năng lượng mà nó sinh ra ở trong quá trình hô hớp tế bào, tức là quá trình chu trình CRP để nó tạo ra năng lượng để sửa cái kìm kia. >> Vâng. >> Thế thì NADH này sẽ cho gì ạ?”
- **Recommend: ACCEPT** — Protected: it is the owner-confirmation note for c473 (NADPH). Its transcript half ("NA DPH", "NADH") is confirmed by the reviewer; the owner half cannot be. Keep; list as accepted.

#### c552 — 05:15:59 · Thực phẩm chứa cơ chất tổng hợp glutathione và số loại thực phẩm mỗi n
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: YES: owner decision 2.4 (human-decisions.md, c541): keep, labelled as the summarizer's note
- Summary now: Ghi chú của người tóm tắt (không phải nội dung chương trình): đây là cách nói trong bản phiên âm, nên người xem nên đối chiếu lại nếu cần.
- Reviewer: no transcript evidence found in any chunk
- Transcript [05:15:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18952s): “Đặc biệt là cái anh Fittain này này là”
- **Recommend: ACCEPT** — Protected (owner decision on c541): the summarizer's note. A note has no transcript quote by design ("Fittain" is at 05:15:52). Keep; list as accepted.

### Group E — Duplicates (carry-over from 2.5) (4 rows)

The 2.5 build left these under a heading far from where they are said (c238 and c242 under 02:22:01, said at 01:27–01:29; c461 and c462 under 04:19:29, said at 02:41). The 2.5 plan records that no move, drop or keep was ever decided and that run 2 passes all four. My check of the baseline: c238 repeats the story already under 01:26:58 (c138, c140); c242 repeats c145 (01:29:22, "nhịp tim tăng 170"); c461 and c462 repeat the passage 02:41:03–02:41:29 already covered by c275 (02:35:19), which group G1 proposes to rewrite to name vitamin C, vitamin E, zinc and selenium, so after that fix c462 adds nothing. All four pass in 2.4, run 1 and run 2 and no reviewer finding names them. Options: **keep** (recommended), **drop** (removes a repeat; the only fact lost is "sinh ba con" in c238), **move** (changes the heading, new hash). The gate accepts verbatim evidence outside the heading window since commit 8975775, so keeping them does not fail it.

#### c238 — 02:22:01 · Đau nửa đầu của chị Nhung và tim nhanh: kết quả sau khi bổ sung vi chấ
- Why it is in the list: carry-over (2.4/ticket id c297)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Chị Nhung 41 tuổi bị đau nửa đầu từ năm 15 tuổi, sinh ba con và bị gắn nhãn trầm cảm.
- Transcript [01:27:03-01:28:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5223s): “Tôi năm nay 41 tuổi, là người con Đông Anh, Hà Nội, rất gần với quê hương của bác sĩ. Tôi mới biết đến kênh được 10 tháng. Trước đó là chuỗi ngày tăm tối nhất khi sức khỏe của tôi suy sụp hoàn toàn. Tôi mắc trứng đau nửa đầu từ năm 15 tuổi, đã chữa trị ở nhiều bệnh viện lớn tại Hà Nội. Bác sĩ chẩn đoán tôi bị nang dưới nhện góc tiểu cầu não trái. Dây thần kinh số năm bị chèn ép dẫn đến đau nửa đầu. Bình quân mỗi …”
- **Recommend: KEEP** — passes in 2.4, run 1 and run 2; the text is true and under its own heading it is a repeat of text that already exists elsewhere (see group note). Moving or dropping changes the hash and adds gate exposure for no accuracy gain.

#### c242 — 02:22:01 · Đau nửa đầu của chị Nhung và tim nhanh: kết quả sau khi bổ sung vi chấ
- Why it is in the list: carry-over (2.4/ticket id c301)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Trước đây nhịp tim của chị lên tới 170.
- Transcript [01:29:34-01:29:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5374s): “Tôi bị khó thở, nhịp tim tăng lên 170 nhịp một phút”
- **Recommend: KEEP** — passes in 2.4, run 1 and run 2; the text is true and under its own heading it is a repeat of text that already exists elsewhere (see group note). Moving or dropping changes the hash and adds gate exposure for no accuracy gain.

#### c461 — 04:19:29 · Đường, gốc tự do và trường hợp chị Hằng: vòng xoắn bệnh lý và sau khi 
- Why it is in the list: carry-over (2.4/ticket id c464)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ nói glutathion không hoạt động được nếu thiếu các yếu tố hiệp đồng.
- Transcript [02:41:18-02:41:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9678s): “Nếu bây giờ các bạn thiếu kẽm thì glutathion chẳng có giá trị. Cen quá quan trọng trong cái chuyện là enzyme để mà chuyển hóa gốc tự do. Nếu không có cen thì glutat vất đi.”
- **Recommend: KEEP** — passes in 2.4, run 1 and run 2; the text is true and under its own heading it is a repeat of text that already exists elsewhere (see group note). Moving or dropping changes the hash and adds gate exposure for no accuracy gain.

#### c462 — 04:19:29 · Đường, gốc tự do và trường hợp chị Hằng: vòng xoắn bệnh lý và sau khi 
- Why it is in the list: carry-over (2.4/ticket id c465)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ nêu kẽm, vitamin C và vitamin E cùng nhiều vi chất khác, và nói có đủ glutathion mà thiếu các chất này thì cũng không tác dụng.
- Transcript [02:41:03-02:41:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9663s): “Tôi nhắc lại là vitamin C là một này, E là hai này, kẽm là ba này, cen là 4 này. Tất cả bốn cái này là giải quyết những cái gốc tự do vô cùng quan trọng. Và đây là những cái yếu tố hợp đồng với lại glutathion. >> Vâng. >> Nếu bây giờ các bạn thiếu kẽm thì glutathion chẳng có giá trị.”
- **Recommend: KEEP** — passes in 2.4, run 1 and run 2; the text is true and under its own heading it is a repeat of text that already exists elsewhere (see group note). Moving or dropping changes the hash and adds gate exposure for no accuracy gain.

### Group F — No transcript evidence found by the gate (bridge sentences, summaries of a sequence) (6 rows)

The gate saw one chunk and found no evidence. For c087, c154, c184, c245, c375 I found the passage in the transcript myself (quotes below); c478 I could not find. The reviewer's own finding is only "no transcript evidence found in any chunk", so the gate gives no reason for these rows other than missing support.

#### c087 — 01:00:47 · Cơ thể phản ứng với gốc tự do qua ba bước
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Bác sĩ mô tả ba bước.
- Reviewer: no transcript evidence found in any chunk
- Transcript [01:02:08-01:03:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3728s): “bước số một là cảm tử ra để cánh đỡ. Sau khi cảm tử ra cánh đỡ rồi thì bước thứ hai … đến bước thứ hai là các cái chất, các cái gọi là đội đặc nhiệm … Bước thứ ba … nó phát đi các cái tín hiệu … ký hiệu là Rn F2 … đưa về ADN”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Bác sĩ mô tả ba bước khi gốc tự do tấn công cơ thể: bước một là đội "cảm tử", bước hai là đội "đặc nhiệm", bước ba là phát tín hiệu "Rn F2" về ADN để sản xuất thêm đội đặc nhiệm. (The transcript has all three steps at 01:01:05–01:03:20; the gate saw only one chunk.)

#### c154 — 01:33:05 · Vitamin D 50.000 IU: liều, nồng độ mục tiêu và cách duy trì
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Đoạn đầu này bác sĩ chưa trả lời trực tiếp, nhưng phần bàn về vitamin D sau đó được tóm tắt dưới đây.
- Reviewer [01:34:05-01:34:27]: Phần này có câu hỏi và chuyển sang lời tổng kết, chưa có trả lời trực tiếp về vitamin D; phần bàn sau không nằm trong slice.
- Transcript [01:34:05-01:34:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5645s): “Em muốn nhờ bác sĩ phân tích giúp em rằng việc bổ sung duy trì vitamin D liều 50.000 đơn vị với tần suất một tháng một viên như vậy có an toàn và hợp lý về mặt y khoa hay không ạ? Em xin chân thành cảm ơn bác sĩ và toàn thể ekip chương trình. Vâng thưa quý vị lắng nghe từng ý kiến của quý vị gửi về cho chương trình.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Replace the bridge sentence with what is said at 01:34:05: Người xem hỏi bác sĩ phân tích việc bổ sung duy trì vitamin D liều 50.000 đơn vị, tần suất một tháng một viên, có an toàn và hợp lý về mặt y khoa hay không.

#### c184 — 01:47:01 · Glutathion và gốc tự do, nhìn qua thơ văn và hội họa
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Đây là phần ví von để minh họa cho việc nhìn kiến thức đa chiều.
- Reviewer: no transcript evidence found in any chunk
- Transcript [01:48:35-01:48:51](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6515s): “phân tích được dưới góc độ y khoa. Các bạn phải phân tích được dưới góc độ toán học. Các bạn phải phân tích được dưới góc độ vật lý học … Các bạn phải nhìn dưới góc độ y học, dưới góc độ sức khỏe”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Bác sĩ nói phải phân tích kiến thức dưới nhiều góc độ, như y khoa, toán học, vật lý học (ví dụ với một bài thơ).

#### c245 — 02:23:53 · Thoát vị đĩa đệm và thiếu vi chất
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Ông khuyên nên phòng ngừa từ sớm bằng cách bổ sung vi chất đầy đủ, để tránh tình trạng này xảy ra.
- Reviewer: no transcript evidence found in any chunk
- Transcript [02:24:18-02:24:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8658s): “Chúng ta phải phòng ngay từ khi đừng để cho nó xảy ra cái tình trạng ấy nữa. Mà muốn như vậy chúng ta phải bổ sung vi chất các thứ cho nó đầy đủ vào.”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Ông nói phải phòng ngay từ khi đừng để tình trạng ấy xảy ra, và muốn vậy thì phải bổ sung vi chất cho đầy đủ.

#### c375 — 03:25:17 · Vitamin B12 838,9: có đáng lo không và các nguyên nhân tăng giả
- Why it is in the list: run-2 FAIL
- Runs: 2.4: fail · run 1: fail · run 2: fail
- Protected wording: no
- Summary now: Transcript nêu hai nhóm nguyên nhân.
- Reviewer: no transcript evidence found in any chunk
- Transcript [03:26:00-03:26:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12360s): “Lý do là bởi vitamin B12 thuộc nhóm vitamin tan trong nước. Nếu cơ thể không dùng hết thì lượng dư thừa sẽ được thận nhẹ nhàng đảo thải qua nước tiểu … chỉ số B12 tăng trong xét nghiệm thường đến từ hiện tượng dương tính giả hoặc nhiễu kỹ thuật … tế bào gan bị tổn thương mạn tính cũng làm giải phóng một lượng B12 dự trữ”
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Phần nhận xét nêu các lý do khiến chỉ số B12 tăng không đáng lo: B12 tan trong nước và phần dư được thận đào thải; chỉ số tăng trong xét nghiệm thường do dương tính giả hoặc nhiễu kỹ thuật; tổn thương gan mạn tính làm giải phóng B12 dự trữ vào máu. (Replaces the unsupported "hai nhóm nguyên nhân".)

#### c478 — 04:29:03 · Cấu tạo, hoạt động và tái tạo của glutathion (tiếp)
- Why it is in the list: run-2 FAIL; carry-over (2.4/ticket id c484)
- Runs: 2.4: fail · run 1: fail · run 2: fail; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Bác sĩ dùng cách này để giải thích vì sao cơ thể không vứt bỏ glutathion sau khi dùng.
- Reviewer: no transcript evidence found in any chunk
- **Recommend: FIX** (drafted for this brief from the transcript; check before applying): Drop the sentence. No transcript support was found by the gate in three runs, and a keyword search of 04:29–04:36 finds nothing about discarding glutathione.

### Group G1 — Undecided corrections that pass in run 2: fix recommended (16 rows)

These 28 rows are in the 46 undecided corrections but pass in run 2 (each pair marked 2.4/run 1/run 2 below). Fix recommended because the proposal corrects who said it, a number, an order, a condition or a scope; or because the claim failed in an earlier run (c034, c056, c272, c203, c204, c206, c294, c444), so passing is not stable.

#### c034 — 00:15:44 · Gốc tự do ngoại nhập từ chế độ ăn uống
- Why it is in the list: undecided correction (audit id c034)
- Runs: 2.4: fail · run 1: fail · run 2: pass; **⚠ status changed run 1→2 with identical text (fail→pass)**
- Protected wording: no
- Summary now: Chất béo chuyển hóa được mô tả là chất béo bị đốt cháy quá mức, ví dụ đồ chiên rán, hoặc dầu thực vật bị dùng sai khi rán, dẫn đến chuyển hóa thành chất béo trung gian.
- Transcript [00:16:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=989s): “những chất béo mà khi chúng ta bị đốt cháy là dở dở đi ấy. Ví dụ như là đồ chiên dàn chẳng hạn.”
- Transcript [00:16:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=998s): “là dầu thực vật mà chúng ta thực hiện trên dán thì nó sẽ chuyển hóa thành cái chất béo trung gian.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Chất béo chuyển hóa được bác sĩ mô tả là những chất béo "bị đốt cháy là dở dở đi" (bản ghi âm ghi như vậy, nghĩa chưa rõ), ví dụ đồ chiên rán; còn dầu thực vật dùng sai khi rán thì chuyển hóa thành chất béo trung gian.

#### c056 — 00:45:22 · Ozon: gốc tự do thứ tư
- Why it is in the list: undecided correction (audit id c054)
- Runs: 2.4: fail · run 1: fail · run 2: pass; **⚠ status changed run 1→2 with identical text (fail→pass)**
- Protected wording: no
- Summary now: Ozon không cướp trực tiếp như các gốc khác, mà xen vào các phân tử oxy khác, tạo thành cuộc "tình tay ba", và từ đó sinh ra gốc tự do.
- Transcript [00:45:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2759s): “Thế bây giờ có thêm một cái oxy nữa nó xen vào đây trở thành cuộc tình tay ba.”
- Transcript [00:47:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2828s): “không đi ăn cướp nhưng cái này nó đi nó xen vào câu chuyện của các gia đình khác”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Ozon được mô tả là có thêm một oxy nữa xen vào oxy hai nguyên tử, thành cuộc "tình tay ba"; ozon không đi ăn cướp, nhưng gặp chỗ nào xen được thì xen vào câu chuyện của các gia đình khác, và từ đó cũng tạo ra một gốc tự do.

#### c066 — 00:48:55 · Gốc tự do tấn công màng tế bào: lipid và lipit peroxit
- Why it is in the list: undecided correction (audit id c066)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ ví màng tế bào như một bãi xăng, nên một gốc tự do cũng đủ làm sụp đổ hệ thống.
- Transcript [00:53:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3229s): “người ta ví rằng màng tế bào nó giống như là một bãi”
- Transcript [00:53:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3233s): “Vậy chỉ cần một gốc tự do tấn công màn tế bào ngay lập tức nó sụp đổ hệ”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ thuật lại rằng người ta ví màng tế bào như một bãi xăng, nên chỉ cần một gốc tự do tấn công màng tế bào là ngay lập tức sụp đổ hệ thống.

#### c105 — 01:06:19 · Glutathion được quảng cáo để làm trắng da: nội dung số phát sóng
- Why it is in the list: undecided correction (audit id c103)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ nói glutathion đang được quảng cáo là chất chống oxy hóa giúp trắng da và nhiều người mua về bổ sung.
- Transcript [01:06:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3983s): “ta quảng cáo rất nhiều về glutathion để”
- Transcript [01:06:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3988s): “Chủ yếu là với tác dụng là chất chống”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói người ta quảng cáo rất nhiều về glutathion; người đáp là Khánh Lành nêu chủ yếu với tác dụng là chất chống oxy hóa giúp trắng da, bác sĩ xác nhận "giúp trắng da" và nói rất nhiều người mua về, nhất là chị em phụ nữ.

#### c145 — 01:29:22 · Lạm dụng đường mía thô: nhịp tim 170 lần/phút và các triệu chứng
- Why it is in the list: undecided correction (audit id c140)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Người xem kể sau khi mệt là uống đường mía thô, và dùng lâu dài thì có khó thở, nhịp tim tăng 170 nhịp mỗi phút, tăng cân, bụng to và gan bắt đầu nhiễm mỡ.
- Transcript [01:29:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5357s): “Trong lúc mệt mỏi, tôi ăn hoặc là uống đường mía thô”
- Transcript [01:29:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5369s): “Sau 3 tháng sử dụng lượng đường quá nhiều”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Người xem kể lúc mệt mỏi đã ăn hoặc uống đường mía thô, rồi lạm dụng; sau 3 tháng dùng lượng đường quá nhiều thì bị khó thở, nhịp tim tăng lên 170 nhịp một phút, tăng cân, bụng to và gan bắt đầu nhiễm mỡ.

#### c161 — 01:39:48 · Thói quen ăn uống của học sinh: thức ăn nhanh, đường và nước ga
- Why it is in the list: undecided correction (audit id c210)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Học sinh cũng lười nhai và thường chỉ muốn ăn nhanh, hấp thu năng lượng nhanh, dẫn đến calo rỗng.
- Transcript [01:40:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6014s): “cái calor rỗng các bạn đang rơi vào cái tình trạng đấy rất nhiều. Thế và các bạn ăn những các cái đồ ăn của thức ăn nhanh. Đến nỗi mà tôi có chị bạn có hai”
- Transcript [01:40:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6034s): “thịt cũng thế phải say nó ra để đỡ khỏi nhai. Các bạn ấy lười nhai, các bạn ấy lười tất cả mọi thứ và chỉ muốn rằng ăn sẵn ăn nhanh.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói các bạn ăn thức ăn nhanh, uống nhiều đồ uống có đường và rơi vào tình trạng calo rỗng rất nhiều. Ông kể hai đứa con của một chị bạn lười nhai, lười mọi thứ và chỉ muốn ăn sẵn, ăn nhanh.

#### c186 — 01:52:19 · Lối sống lành mạnh là con đường thay cho lối tắt
- Why it is in the list: undecided correction (audit id c235)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Ông nói từng bước đan xen kiến thức, và tin rằng người làm như vậy sẽ thành công, không phải người gặp khó khăn khi bước vào đời.
- Transcript [01:52:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6760s): “cái kỹ năng đó khi bạn chuẩn bị cho mình thì tôi tin rằng đến một ngày không xa bạn sẽ thành công. Và ngày hôm nay bạn xem kênh của chúng tôi biết đặt ra câu hỏi như thế này, biết quan tâm trăn trở như thế này, tôi tin rằng bạn sẽ là cái người thành công chứ không phải là cái người mà sau này bạn bước vào đời gặp phải những cái khó khăn. Tôi tin rằng”
- Transcript [01:52:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6755s): “đan xen các cái kiến thức với nhau.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Ông nói từng bước đan xen kiến thức, tin rằng khi chuẩn bị những kỹ năng đó thì đến một ngày không xa bạn sẽ thành công; và ông nói riêng với bạn Anh Anh, người xem kênh, biết đặt câu hỏi, biết quan tâm trăn trở, rằng ông tin bạn sẽ là người thành công chứ không phải người sau này bước vào đời gặp phải khó khăn.

#### c203 — 02:05:39 · Hoại tử chỏm xương đùi, bỏ thuốc lá và tuổi thọ
- Why it is in the list: undecided correction (audit id c251)
- Runs: 2.4: pass · run 1: fail · run 2: pass; **⚠ status changed run 1→2 with identical text (fail→pass)**
- Protected wording: no
- Summary now: Ông kể một bệnh nhân đau vùng háng, chụp thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải khoan giảm áp và thay khớp háng.
- Transcript [02:05:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7518s): “này, có những người đau ở bên phần háng ấy. Thế đến khi dần dần đi chụp ích quang một ngày bắt đầu thấy hoại tử vô khuẩn trỏm xương đùi, cuối cùng là phải”
- Transcript [02:05:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7527s): “xuyên giảm áp, cuối cùng là phải thay cả khớp háng. Thế nhưng mà những bệnh nhân ấy chỉ cần yêu cầu gì thôi là đang hút”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nêu ví dụ có những người đau bên phần háng, dần dần đi chụp thì thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải "xuyên giảm áp" (bản ghi âm ghi như vậy) rồi thay cả khớp háng.

#### c204 — 02:05:39 · Hoại tử chỏm xương đùi, bỏ thuốc lá và tuổi thọ
- Why it is in the list: undecided correction (audit id c252)
- Runs: 2.4: pass · run 1: fail · run 2: pass; **⚠ status changed run 1→2 with identical text (fail→pass)**
- Protected wording: no
- Summary now: Bệnh nhân này đang hút thuốc, khi chỉ dừng hút thuốc lá thì cơn đau đã giảm đi nhiều.
- Transcript [02:05:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7529s): “khớp háng. Thế nhưng mà những bệnh nhân ấy chỉ cần yêu cầu gì thôi là đang hút thuốc lá chỉ cần có một động tác đó là”
- Transcript [02:05:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7536s): “dừng hút thuốc lá lại nó đã giảm đau đi rất nhiều.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói những bệnh nhân ấy, nếu đang hút thuốc lá, chỉ cần một động tác là dừng hút thuốc lá lại thì đã giảm đau đi rất nhiều.

#### c206 — 02:06:24 · Trường hợp chị Ngọc Thơ: vàng da, vàng củng mạc mắt và hemoglobin thấp
- Why it is in the list: undecided correction (audit id c254)
- Runs: 2.4: pass · run 1: fail · run 2: pass; **⚠ status changed run 1→2 with identical text (fail→pass)**
- Protected wording: no
- Summary now: Chị Ngọc Thơ, theo bình luận được đọc trên chương trình, từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt, khiến chị xấu hổ và không dám chụp ảnh với ai.
- Transcript [01:21:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4902s): “Tình trạng của em trước đây. Từ năm 2017 đến nay, da của em đặc biệt là lòng bàn tay, lòng bàn chân và da mặt, luôn bị vàng bợt, thiếu sức sống. Niêm mạc mắt”
- Transcript [02:06:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7593s): “Ngọc hay là Ngọc Thơ? Tôi đoán là chị Ngọc Thơ không có dấu không có dấu cho nên tôi đoán là chị Ngọc Thơ. Thế thì chị Ngọc Thơ có bình”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Một người xem, theo bình luận được đọc trên chương trình (bác sĩ nói "tôi đoán là chị Ngọc Thơ" vì tài khoản không dấu), từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt; bác sĩ kể lại chị xấu hổ, ngại ngùng, không dám chụp ảnh với ai.

#### c262 — 02:34:11 · Bóng đè có nguy hiểm không và xử lý khi gặp
- Why it is in the list: undecided correction (audit id c161)
- Runs: 2.4: pass · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Khi xảy ra, hít một hơi thật sâu rồi thở ra từ khoảng 15 đến 30 giây, sau đó lấy lại bình tĩnh thì sẽ thoát khỏi tình trạng này.
- Transcript [02:34:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9269s): “bóng đè này hít một hơi thật sâu quãng”
- Transcript [02:34:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9272s): “sau đó thì bắt đầu thở ra từ 15 đến 30”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói hầu hết tài liệu khoa học khuyên khi xảy ra thì hít một hơi thật sâu, rồi thở ra từ 15 đến 30 giây ("đại ý"), sau đó lấy lại bình tĩnh thì thoát; nhưng ông nói "cứ khuyên nhau thế thôi nhưng mà ai cũng sợ", và sau đó nhận xét nói thế thì rất đơn giản.

#### c272 — 02:35:19 · Căng thẳng kéo dài, gốc tự do và bóng đè
- Why it is in the list: undecided correction (audit id c172)
- Runs: 2.4: fail · run 1: fail · run 2: pass; **⚠ status changed run 1→2 with identical text (fail→pass)**; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Bác sĩ nói những người bị táo bón, hội chứng ruột kích thích, viêm dạ dày ruột không tiết được serotonin, nên dễ bị bóng đè khi mơ màng lúc ngủ, thức.
- Transcript [02:40:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9603s): “thấy rằng một số những người mà bị táo”
- Transcript [02:40:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9609s): “dày ruột thì nó không thể tiết được”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói một số những người bị táo bón, bị hội chứng ruột kích thích, bị dạ dày ruột thì không thể tiết được serotonin, nên cứ mơ màng, thức ngủ thì rất dễ bị bóng đè.

#### c275 — 02:35:19 · Căng thẳng kéo dài, gốc tự do và bóng đè
- Why it is in the list: undecided correction (audit id c176)
- Runs: 2.4: pass · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Kẽm là yếu tố hợp đồng với glutathione: nếu thiếu kẽm thì glutathione không có giá trị, vì selen là enzyme chuyển hóa gốc tự do.
- Transcript [02:41:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9674s): “là những cái yếu tố hợp đồng với lại glutathion.”
- Transcript [02:41:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9678s): “Nếu bây giờ các bạn thiếu kẽm thì glutathion chẳng có giá trị. Cen quá quan trọng trong cái chuyện là enzyme để mà chuyển hóa gốc tự do. Nếu không có cen thì glutat vất đi.”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Vitamin C, vitamin E, kẽm và selen (bản ghi âm ghi là "cen") là những yếu tố hợp đồng với glutathione. Nếu thiếu kẽm thì glutathione chẳng có giá trị. Selen quá quan trọng trong chuyện là enzyme để chuyển hóa gốc tự do; nếu không có selen thì glutathione vất đi.

#### c276 — 02:35:19 · Căng thẳng kéo dài, gốc tự do và bóng đè
- Why it is in the list: undecided correction (audit id c177)
- Runs: 2.4: pass · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Theo bác sĩ, bổ sung đủ các chất này giúp ngủ ngon và tế bào não hoạt động bình thường.
- Transcript [02:41:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9693s): “Vitamin C, vitamin E vô cùng quan trọng. Vậy khi bổ sung nó thì chúng ta sẽ ngủ ngon, chúng ta ngủ tốt, thực hành lối sống tốt, ngủ ngon, ngủ tốt thì chúng ta các tế bào não hoạt động bình thường,”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Theo bác sĩ, khi bổ sung các chất này thì sẽ ngủ ngon, ngủ tốt; cùng với thực hành lối sống tốt, ngủ ngon, ngủ tốt thì các tế bào não hoạt động bình thường.

#### c294 — 02:44:45 · Vitamin D 50.000 IU: nồng độ mục tiêu và cách duy trì
- Why it is in the list: undecided correction (audit id c193)
- Runs: 2.4: fail · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Người khỏe mạnh, không có bệnh nền, không có mỡ máu, tiểu đường hay huyết áp cao thì bổ sung liều cao lên nồng độ dễ và hiệu quả.
- Transcript [02:46:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10004s): “tật gì khác, rất khỏe rồi, không bị nhiều mỡ, mỡ dưới da ít, mỡ nội tạng không có, không bị mỡ máu, không bị tiểu đường, không bị huyết áp thì khánh lành bổ sung liều cao thì nó sẽ lên được dễ và nó hiệu quả. Nhưng nếu chúng ta có”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Người khỏe mạnh, không còn bệnh tật gì khác, không bị nhiều mỡ, mỡ dưới da ít, không có mỡ nội tạng, không bị mỡ máu, tiểu đường hay huyết áp thì bổ sung liều cao sẽ lên được dễ và hiệu quả.

#### c444 — 04:11:00 · Danh sách vi chất theo bác sĩ: magie, kẽm, canxi, vitamin D3
- Why it is in the list: undecided correction (audit id c407)
- Runs: 2.4: fail · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Bác sĩ nói đầu tiên là magie, rồi kẽm, canxi, vitamin D3, vitamin tổng hợp (đặc biệt nhóm B), vitamin C và cuối cùng là omega 3.
- Transcript [04:10:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15056s): “sung thì những cái gì. Đó là đầu tiên là cái mag rất quan trọng mà lúc nãy tôi vừa mới nói đó là chúng ta ma kẽm cen vân vân các thứ nếu chúng ta không có đủ”
- Transcript [04:11:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15074s): “gì hết cả. Chân ma là rất quan trọng. Sau đó đến gì ạ? Đến canxi. Xong đến vitamin D3 đúng không ạ? Thì đây chính là bộ ba tam giác vàng. Tiếp theo nữa là”
- **Recommend: FIX** (proposal from proposed-corrections.md (not yet owner-reviewed)): Bác sĩ nói đầu tiên là magie, rồi canxi, vitamin D3, vitamin tổng hợp (đặc biệt nhóm B), vitamin C, kẽm và cuối cùng là omega 3.

### Group G2 — Undecided corrections that pass in run 2: keep recommended (12 rows)

These 28 rows are in the 46 undecided corrections but pass in run 2 (each pair marked 2.4/run 1/run 2 below). Keep recommended: the proposal restores a hedge or tone (for example "sẽ" for "có thể"), or the claim is stable. Exact wording is shown if you prefer it.

#### c081 — 00:56:11 · Gốc tự do tấn công ADN và mã di truyền G (gốc tự do thứ bảy)
- Why it is in the list: undecided correction (audit id c079)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Đột biến gen có thể gây bệnh hiếm và ung thư.
- Transcript [00:58:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3509s): “mà đột biến gen này thì sẽ gây ra một là”
- Transcript [00:58:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3512s): “bệnh nguy hiểm, bệnh hiếm đúng không ạ?”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Đột biến gen sẽ gây ra bệnh nguy hiểm, bệnh hiếm và ung thư.

#### c107 — 01:06:19 · Glutathion được quảng cáo để làm trắng da: nội dung số phát sóng
- Why it is in the list: undecided correction (audit id c105)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ cũng nói nếu cơ thể cạn kiệt glutathion thì có thể sinh ra nhiều bệnh mãn tính, một số bệnh ung thư và lão hóa nhanh.
- Transcript [01:07:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4035s): “cạn kiệt glutathon thì chúng ta sẽ sinh”
- Transcript [01:07:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4039s): “nhiều các bệnh mãn tính, có những bệnh”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Bác sĩ cũng nói một khi đã cạn kiệt glutathion thì sẽ sinh ra một loạt bệnh, trong đó có vô cùng nhiều các bệnh mãn tính, có những bệnh ung thư, có những bệnh nguy hiểm, và đặc biệt lão hóa rất nhanh.

#### c149 — 01:31:32 · Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý
- Why it is in the list: undecided correction (audit id c144)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Họ kể vẫn còn nhịp tim nhanh và thỉnh thoảng bị bóng đè khi ngủ.
- Transcript [01:31:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5484s): “Nhịp tim đôi lúc bị nhanh và khi ngủ thỉnh thoảng vẫn bị hiện tượng bóng đè.”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Họ kể nhịp tim đôi lúc bị nhanh và khi ngủ thỉnh thoảng vẫn bị bóng đè.

#### c162 — 01:39:48 · Thói quen ăn uống của học sinh: thức ăn nhanh, đường và nước ga
- Why it is in the list: undecided correction (audit id c211)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ nói việc này có thể khiến các em thất bại, nên phải thay đổi thói quen ăn uống từ hàng ngày.
- Transcript [01:40:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6042s): “Vậy khi chúng ta duy trì một cái lối sống mà nhanh gấp gáp, chỉ muốn rằng là tiếp thu những cái gì mà nó nhanh chóng tạo ra năng lượng thì chúng ta sẽ thất bại. Vậy đầu tiên là ta phải thay đổi ngay từ cái thói quen ăn uống hàng ngày.”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Bác sĩ nói khi duy trì lối sống nhanh, gấp gáp, chỉ muốn những gì nhanh chóng tạo ra năng lượng thì "chúng ta sẽ thất bại", nên đầu tiên phải thay đổi ngay từ thói quen ăn uống hàng ngày.

#### c231 — 02:16:47 · Đau dây thần kinh số 5 và nang dưới nhện: quan điểm không mổ
- Why it is in the list: undecided correction (audit id c282)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Ông cho rằng đau có thể do gốc tự do tấn công thần kinh và cần tìm hướng khác.
- Transcript [02:18:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8302s): “Và tôi cho rằng cái này nó do những cái đau đầu hay là những cái triệu chứng gì đó chúng ta hãy đi tìm theo cái hướng khác và dường như có những cái ẩn chứa phía sau. Thì đến bây giờ tôi thấy rằng”
- Transcript [02:21:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8498s): “sao nó lại như thế? Đau dây thần kinh số 5 đến giờ phút này tôi cho rằng vẫn là nguyên nhân gốc tự do nó tấn công vào đây này. Gốc tự do nó tấn công vào đây và gây tổn thương dây thần kinh số năm.”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Ông cho rằng với những đau đầu hay triệu chứng đó thì hãy đi tìm theo hướng khác; còn đau dây thần kinh số 5, đến giờ phút này ông cho rằng vẫn là nguyên nhân gốc tự do tấn công vào đây và gây tổn thương dây thần kinh số năm.

#### c281 — 02:42:02 · Bóng đè do thiếu oxy hay do tư thế nằm, và cách giảm bóng đè
- Why it is in the list: undecided correction (audit id c182)
- Runs: 2.4: pass · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Bác sĩ nói bóng đè là biểu hiện tổn thương ở mức tế bào, phân tử do lối sống, tâm sinh lý, ăn uống và môi trường sai, làm gốc tự do gây mất nhịp giữa "người lái" và "bánh xe".
- Transcript [02:42:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9770s): “cuộc sống. Tôi cho rằng là bóng đè là một cái nó thể hiện cơ thể chúng ta đang thể hiện rằng đang tổn thương ở mức độ tế bào,”
- Transcript [02:42:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9779s): “tổn thương ở mức độ phân tử. Do chúng ta thực hành lối sống sai, do tâm sinh lý chúng ta sai, do ăn uống, do tiếp xúc với lại các cái yếu tố tác nhân môi trường sai để xuất hiện những cái chất”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Bác sĩ nói "tôi cho rằng" bóng đè thể hiện cơ thể đang tổn thương ở mức độ tế bào, phân tử, do lối sống, tâm sinh lý, ăn uống và tiếp xúc tác nhân môi trường sai, làm xuất hiện gốc tự do, và gốc tự do làm cho cái phanh không nhịp nhàng giữa người lái xe và bánh xe.

#### c282 — 02:43:43 · Chị Nhung và nhịp tim
- Why it is in the list: undecided correction (audit id c294)
- Runs: 2.4: pass · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Bác sĩ hướng dẫn trong vài tiếng đồng hồ, và sau đó chị bổ sung vi chất theo từng bước, nâng dần liều.
- Transcript [02:44:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9840s): “nhưng mà sau đó ba mẹ con đến khám thì tôi đã hướng dẫn cho ngày đấy hướng dẫn mấy tiếng đồng hồ cơ 4 năm tiếng đồng hồ cơ. Vâng.”
- Transcript [02:44:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9847s): “Để mà bổ sung vi chất thì sau khi hướng dẫn tôi trải qua từng bước một cứ nâng cao nâng cao dần thì đã thấy rằng cái hiệu quả đã thay đổi ngoạn mục trông thấy. Và nếu chị mua được các cái vi”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Bác sĩ hướng dẫn trong mấy tiếng đồng hồ ("4 năm tiếng đồng hồ" theo bản ghi âm) để bổ sung vi chất, và sau đó chị trải qua từng bước một, "cứ nâng cao nâng cao dần".

#### c348 — 03:13:53 · Ý nghĩa MPV giảm, MCV và MCH tăng nhẹ ở bác Lương Trắc Nghiên
- Why it is in the list: undecided correction (audit id c319)
- Runs: 2.4: pass · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Số lượng hồng cầu có thể chưa thấp đến mức thiếu máu cấp, nhưng cơ thể có thể đang thiếu máu chức năng và đói oxy.
- Transcript [03:15:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11711s): “Mặc dù số lượng hồng cầu trên giấy tờ có thể chưa tụt xuống đến mức báo động của thiếu máu cấp tính, nhưng cơ thể bác lại giơ vào tình trạng thiếu máu chức năng và đói oxy vô cùng trầm trọng.”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Số lượng hồng cầu trên giấy tờ có thể chưa tụt xuống mức báo động của thiếu máu cấp tính, nhưng cơ thể bác đang ở tình trạng thiếu máu chức năng và đói oxy vô cùng trầm trọng.

#### c354 — 03:18:45 · Axit uric và cholesterol tăng ở người gầy, ăn đạm bạc
- Why it is in the list: undecided correction (audit id c333)
- Runs: 2.4: pass · run 1: pass · run 2: pass; moved to this heading in 2.5 (text unchanged)
- Protected wording: no
- Summary now: Gan và thận thiếu vi chất nên giảm khả năng đào thải, và tinh thể urat có thể lắng đọng ở khớp và thành mạch, gây đau gút.
- Transcript [03:19:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11970s): “tăng vọt. Trong khi đó, lá gan và quả thận đã kiệt sức vì thiếu vi chất nên mất đi khả năng đảo thải.”
- Transcript [03:19:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11979s): “Những tinh thể uras sắc nhọn như vô số mũi kim nhỏ âm thầm đọng lại nơi khấp xương và thành mạch. Đe dọa mang đến”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Gan và thận kiệt sức vì thiếu vi chất nên mất đi khả năng đào thải, và những tinh thể urat âm thầm đọng lại nơi khớp xương và thành mạch, đe dọa mang đến những cơn đau gút.

#### c367 — 03:24:03 · Kẽm, đồng và canxi ion hóa: đọc kết quả và triệu chứng thiếu kẽm
- Why it is in the list: undecided correction (audit id c373)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Transcript cho rằng những thiếu hụt này xuất hiện sau nhiều thập kỷ hút thuốc lá và thiếu vi chất.
- Transcript [03:24:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12275s): “xương lành dường như đã cạn kiệt sau hàng thập kỷ bác sống trong khói thuốc lá và thiếu hụt vi chất.”
- Transcript [03:24:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12269s): “Kẽm và đồng chính là những người thợ sửa [âm nhạc] chữa tí hon.”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Transcript nói kẽm và đồng dường như đã cạn kiệt sau hàng thập kỷ bác sống trong khói thuốc lá và thiếu hụt vi chất.

#### c540 — 05:06:37 · Các đường đưa glutathione vào cơ thể: uống, ngậm dưới lưỡi, tiêm, lipo
- Why it is in the list: undecided correction (audit id c529)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ cho rằng đường tiêm "quá nguy hiểm", có thể gây sốc và ngộ độc.
- Transcript [05:12:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18755s): “Thì con đường này quá nguy hiểm.”
- Transcript [05:12:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18759s): “Con đường tiêm này thì sẽ một là sốc và hai là ngộ độc.”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Bác sĩ nói đường tiêm "quá nguy hiểm", và đường tiêm này thì "sẽ một là sốc và hai là ngộ độc".

#### c561 — 05:19:25 · Quan điểm của bác sĩ về sản phẩm glutathione đắt tiền
- Why it is in the list: undecided correction (audit id c549)
- Runs: 2.4: pass · run 1: pass · run 2: pass
- Protected wording: no
- Summary now: Bác sĩ nói glutathione đang bán rất đắt và là sản phẩm "hot" trên thị trường.
- Transcript [05:19:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19165s): “sản phẩm Glutathion trên thế giới có những sản phẩm bán rất đắt và nó đã trở thành một cái sản phẩm khá hot trên thị trường”
- **Recommend: KEEP** — run-2 pass; the difference is hedge or tone, not a changed fact. Optional exact wording (proposed-corrections.md): Bác sĩ nói trên thế giới có những sản phẩm glutathion bán rất đắt, và nó đã trở thành một sản phẩm khá hot trên thị trường.

## 3. Run-1 vs run-2: the 15 claims whose status changed with no text change

Only c277 moved between the runs, so these 15 differences (14 fail→pass, 1 pass→fail) are reviewer variance. **7 are rows above; 8 are outside the merged list** because they pass in run 2 and are in no other list. They may flip back.

| Claim | Run 1→run 2 | In the merged list? | Text (start) |
|---|---|---|---|
| c034 | fail→pass | yes, group G1 | Chất béo chuyển hóa được mô tả là chất béo bị đốt cháy quá mức, ví dụ đồ chiên rán, hoặc dầu thực vật bị dùng sai khi rá |
| c056 | fail→pass | yes, group G1 | Ozon không cướp trực tiếp như các gốc khác, mà xen vào các phân tử oxy khác, tạo thành cuộc "tình tay ba", và từ đó sinh |
| c155 | pass→fail | yes, group A | Bác sĩ nói mười bình luận đều liên quan đến glutathion. |
| c203 | fail→pass | yes, group G1 | Ông kể một bệnh nhân đau vùng háng, chụp thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải khoan giảm áp và thay khớp |
| c204 | fail→pass | yes, group G1 | Bệnh nhân này đang hút thuốc, khi chỉ dừng hút thuốc lá thì cơn đau đã giảm đi nhiều. |
| c206 | fail→pass | yes, group G1 | Chị Ngọc Thơ, theo bình luận được đọc trên chương trình, từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt, khiến chị  |
| c215 | fail→pass | no (pass; not in any list) | Bố chồng chị Ngân bổ sung vi chất và đường huyết giảm xuống (bác sĩ nói “chồng chị Ngân”; theo chủ sở hữu, ý là bố chồng |
| c227 | fail→pass | no (pass; not in any list) | Bác sĩ nói “chồng chị Ngân” sau khi uống thì đường huyết giảm trở lại bình thường (theo chủ sở hữu, bác sĩ nói lỡ, ý là  |
| c241 | fail→pass | no (pass; not in any list) | Uống đủ thuốc không đỡ, nhưng sau khi bổ sung vi chất, theo bác sĩ, chị thay đổi hoàn toàn, không còn đau nửa đầu và đau |
| c272 | fail→pass | yes, group G1 | Bác sĩ nói những người bị táo bón, hội chứng ruột kích thích, viêm dạ dày ruột không tiết được serotonin, nên dễ bị bóng |
| c288 | fail→pass | no (pass; not in any list) | Dược sĩ nước ngoài hướng dẫn bổ sung 50.000 UI mỗi tuần, liên tục 8 tuần thì nồng độ lên tới mức lý tưởng. |
| c373 | fail→pass | no (pass; not in any list) | Bác sĩ hiếm khi bận tâm khi chỉ số này tăng nhẹ, thậm chí tăng gấp rưỡi hoặc gấp đôi. |
| c406 | fail→pass | no (pass; not in any list) | Bác sĩ nói một thân thể đã chịu 73 năm bão táp cần ít nhất nửa năm đến một năm được chăm sóc đúng cách. |
| c441 | fail→pass | no (pass; not in any list) | Bác có thể tập thở đơn giản theo "1 1,5", tức là cố gắng kéo dài thì thở ra một chút (bản ghi âm ghi "thì sau ra"; người |
| c512 | fail→pass | no (pass; not in any list) | Bác sĩ cũng kể trường hợp chị Ngân, điều dưỡng ở một bệnh viện lớn tại Hà Nội, có chồng bị tiểu đường: sau khi bổ sung v |

## 4. Omissions (16)

Run 1 reported 15 omissions; 8 of the 16 below were also in run 1 (by timestamp), 8 are new. "add" means: one sentence in the heading that covers the timestamp, wording taken from the quote, labelled "khán giả tự kể" for viewer items. Importance (H/M/L) is the auditor's from `omissions.md`.

| # | Timestamp (link) | Topic the reviewer says is missing | Transcript quote | In run 1? | omissions.md id | Recommend |
|---|---|---|---|---|---|---|
| O1 | [01:04:05-01:04:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3845s) | Catalaz được mô tả dùng sắt hai cộng để phá hủy gốc tự do. | “Và Catala nó có một cái nó sử dụng thanh kiếm đó chính là thanh kiếm sắt hai cộng. thanh kiếm sắt 2+ để nó phá hủy nó nó làm nổ tung những các quả bom gốc tự do ra.” | no | o17 [M] | **ACCEPT** — Not in run 1; mechanism detail (o17 [M]). Re-check if it reappears. |
| O2 | [01:22:12-01:22:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4932s) | Người xem bị vàng da tự kể cơ hàm khó điều khiển, đơ cứng và nói không rõ từ năm 2012. | “Đặc biệt là từ năm 2012, khu vực cơ hàm của em luôn bị khó điều khiển hay đơ cứng khiến em nói không tròn vành rõ chữ. có lúc mất điều khiển phần hàm.” | no | not in omissions.md | **ACCEPT** — Not in run 1; a viewer self-report that is not a safety item (omissions.md method excludes these). |
| O3 | [01:20:27-01:20:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4827s) | Người xem 50 tuổi tự kể hết viêm da dị ứng và ghèn mắt, nhưng còn viêm xoang và hen phế quản. | “giờ tôi đã hết đau đầu, hết viêm da dị ứng và hết cả ghen mắt lèm nghèm mỗi sáng. Giờ tôi chỉ mong khỏi nốt bệnh viêm xoang và hen phế quản nữa” | no | not in omissions.md | **ACCEPT** — Not in run 1; viewer self-report. Note c123 is being fixed to say only "hết đau đầu". |
| O4 | [01:30:22-01:30:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5422s) | Trước khi bổ sung vi chất, chị Nhung tự kể cai đường, bấm huyệt và uống thuốc nam giúp cải thiện khoảng 30%. | “Sau đó, tôi bắt đầu cai đường. Tôi đi bấm huyệt và uống thuốc nam thì cơ thể đã được 30%.” | no | not in omissions.md | **ACCEPT** — Not in run 1; viewer self-report, not a safety item. |
| O5 | [01:32:05-01:32:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5525s) | Nguyễn Điểm tự kể cải thiện đau đầu, cổ vai gáy, triệu chứng dạ dày, tê chân tay và đầy hơi sau dùng vi chất; gia đình cũng báo cáo cải thiện. | “Từ đó, bệnh đau đầu và đau cổ vai gái của em gần như khỏi hẳn. Trước đây em từng đi khám ở hai bệnh viện tuyến cuối mà vẫn không chữa được. Ngày đó em cứ nghĩ chắc mình có khối u ở trong não. Ngoài ra” | yes | not in omissions.md | **ADD** — In both runs. Viewer self-report; add one sentence under the label "khán giả tự kể" as the owner did for o19–o22 (not as diagnosis, cause or advice). |
| O6 | [01:41:46-01:42:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6106s) | Khuyến nghị lan tỏa kiến thức và hành vi dinh dưỡng trong trường học, xã hội, tổ chức seminar về ăn uống. | “sau đó lan tỏa những cái kiến thức tốt đó những cái hành vi đó cho các bạn xung quanh thế rồi tiến tới là trong cả lớp xong sau đó đến cả trường đến tất cả các cái hệ thống giáo dục xong lan ra toàn x” | no | o23 [M], o24 [L] | **ACCEPT** — Not in run 1; o23/o24 [M/L] school-nutrition advice. |
| O7 | [02:19:52-02:20:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8392s) | Gió nhẹ, đánh răng và cười được mô tả có thể khởi phát cơn đau dây thần kinh số 5. | “chỉ cần một cơn gió thổi nho nhẹ qua cái thôi là cái cơn giật mặt nó [tiếng cười] khủng khiếp. Đánh răng cái thôi là bắt đầu giật mạch khủng khiếp. Thế rồi có khi một nụ cười cái thôi là đã bắt đầu ph” | yes | o31 [M] | **ADD** — In both runs (run 1 flagged "đánh răng hoặc cười"); o31 [M] triggers of trigeminal pain. |
| O8 | [02:17:39-02:17:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8259s) | Bác sĩ mô tả nang dưới nhện là hiện tượng tăng tích dịch tại khe rãnh cuộn não. | “ở đây là cái khe rãnh cuộn não này thì nó sẽ có tích dịch ở đây nó tăng tích dịch thì người ta nói rằng đó chính là một cái khoang cái nang ở dưới nhện.” | yes | not in omissions.md | **ADD** — In both runs; explanation of the cyst already in the summary (c228). |
| O9 | [03:15:55-03:16:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11755s) | Phần nhận xét gắn rối loạn tế bào máu với chóng mặt khi đứng dậy, tay chân lạnh và da nhợt. | “Những cơn hoa mắt chóng mặt trao đảo mỗi khi đứng dậy. Đôi bàn tay bàn chân lúc nào cũng lạnh ngắt như ngâm trong nước đá. Làn da khô nhợt nhạt, thiếu vắng hồng cầu khỏe mạnh” | no | o32 [M] | **ACCEPT** — Not in run 1; o32 [M] symptom list inside the commentary. |
| O10 | [03:30:12-03:30:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12612s) | Phần nhận xét khẳng định vùng phổi xẹp đã vĩnh viễn ngừng trao đổi khí. | “Điều đó có nghĩa là một phần lá phổi của người thợ mộc già đã vĩnh viễn ngừng trao đổi khí” | yes | not in omissions.md | **ADD** — In both runs; commentary statement about the collapsed lung area. |
| O11 | [03:31:07-03:31:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12667s) | Gió mùa và vi khuẩn được mô tả gây co thắt phế quản và khởi phát đợt cấp COPD. | “Chỉ cần một trận gió mùa đông bắc tràn về qua khe cửa hay một chút vi khuẩn thừa cơ xâm nhập, lòng phế quản sẽ lập tức co thắt dữ dội, bịt kín [âm nhạc] nguồn sống ít ỏi còn lại, đầy bác vào những đợt” | yes | o33 [H] | **ADD** — In both runs; o33 [H]: triggers of a COPD flare. Safety relevance, so add. |
| O12 | [03:54:08-03:54:16](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14048s) | Bác sĩ liên hệ cơ thể suy yếu với giảm tập trung, vấp ngã, va chạm và tai nạn. | “Khi  cơ thể chúng ta suy yếu thì chúng ta mới  không tập trung được, chúng ta đi mới  hay bị vấp ngã, mới hay bị va chạm, mới  hay bị tai nạn.” | no | o36 [M] | **ACCEPT** — Not in run 1; o36 [M]. |
| O13 | [04:26:01-04:26:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15961s) | Bác sĩ giải thích cacbon alpha kém bền do chuyển dịch electron từ nitơ và oxy. | “Thế còn thì cái cacbon alpha này là cacbon mà do có chuyển dịch electron của nitơ này và của oxy của cái nhóm cacbonin cbosin này dẫn tới là cái cacbon này nó không bền, >> nó rất dễ bị phá vỡ.” | no | not in omissions.md | **ACCEPT** — Not in run 1; chemistry detail inside the glutathione mechanism. |
| O14 | [04:35:48-04:35:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16548s) | Bác sĩ mô tả mục đích cướp electron và H+ của gốc tự do là tạo thành nước H2O. | “Cướp E và lấy H+ để nhằm mục đích gì đấy ạ? để mục đích tạo thành H2O là cái này hiền hòa.” | yes | not in omissions.md | **ADD** — In both runs (run 1 wording at 04:35:51); purpose of taking e⁻ and H⁺ is to make water. |
| O15 | [04:45:33-04:45:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17133s) | Bác sĩ kể người được gắn nhãn tăng động giảm chú ý, tự kỷ hoặc học dốt cải thiện sau bổ sung vi chất. | “được dán nhãn là trầm cảm, được dán nhãn tăng động giảm chú ý, được gián nhãn tự kỷ. Nhưng sau khi bổ sung vi chất, tất cả mọi cái nó tốt lên, được dán nhãn học dốt tự dưng nó tốt lên.” | yes | o39 [H], o50 [H] | **ADD** — In both runs; o39 [H]: people labelled ADHD, autism or "học dốt" improving. The owner already added the o50 letter sentence nearby. |
| O16 | [05:18:17-05:18:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19097s) | Bác sĩ khuyên không tránh beta-caroten theo các bình luận được nhắc tới. | “Đừng có tránh betacaroten như là các chị đang bình luận” | yes | o46 [H] | **ADD** — In both runs; o46 [H]: do not avoid beta-carotene. Safety relevance, so add. |

Because `coverage_complete` needs an empty list and the auditor finds about half a new set each run, adding every omission cannot be guaranteed to end the loop. Recommended: add the 8 that persisted, accept the other 8 for now, and add any of them that reappear.

## 5. Header tag

- Current header: `- **Topics:** gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu thiếu sắt, lối sống lành mạnh`.
- Decided in ticket 1.14: `thiếu máu thiếu sắt` → `thiếu máu, thiếu sắt`. Both tags are in `topics/vocabulary.md` (lines 19–20), and the other seven tags are too. `verify-output.txt` and the validator fail only on the unsplit tag.
- Recommend: **apply**. Free check after the edit: the validator and a header diff; no gate run needed for the tag alone (the header is not a claim).

## 6. Proposed budget for paid reruns

**Ask: three paid gate runs at most (runs 3, 4 and 5), each with your explicit permission, all on the one fixed summary lineage. Stop rule below.**

Why more than one run, from what the two runs of the same text showed:
- Of the 55 claims that failed in run 1, **14 passed in run 2** with identical text: about 1 in 4 failures on unchanged text is noise. Of the 511 that passed, **1 failed** in run 2 (c155): about 1 in 500.
- With roughly 525 passing claims, that is about one spontaneous new failure per run (expected count ≈ 1.0), so the chance that a run shows none is only about one in three even if every real problem is fixed. This rests on a single observation and is rough.
- Concerns went 25→21 and omissions 15→16, but only 8 of the 16 omissions repeat. The 42 failures are not a fixed set: 41 are stable, 1 is new, and 14 earlier ones disappeared.
- A literal pass needs zero failures, zero concerns (minor concerns give `flag`) and zero omissions in one run. That is a high bar for a noisy reviewer, and D0 shows it may be unreachable.
- Any edit changes the summary hash, and the progress cache is bound to the hash (`review_summaries.py` resets it), so **every run reviews all 11 chunks again**. Run 2 hit the usage limit after chunk 10 and needed a resume after the quota reset; plan one run per quota window.

Plan:
1. **Before any paid run (free):** you decide the groups; I apply all decided fixes in **one** batch, rebuild once, then run the free checks: header identical apart from the tag split, headings strictly increasing, `?t=` links, verbatim quote check of every new sentence, validator. Fixes are batched so that each paid run tests the whole set, not one group.
2. **Run 3 (first paid run).** Goal: see which real failures remain. Expect the 7 protected rows to fail or flag (D0) and a few new or noise failures. You then decide each residual row again.
3. **Run 4 (only if run 3 leaves rows you want fixed).** Apply only the new decisions; rerun. A claim that fails in one of two runs and passes in the other is treated as noise and gets "accept with reason", not another edit.
4. **Run 5 (final, tie-break).** Only if run 4 leaves no more than a handful of unprotected failures or omissions. The second reader re-reads every "accept" row against the transcript before this run (ticket note).
5. **Stop rule.** Stop when a run has no failure, concern or omission outside the accepted list and `coverage_complete` is true (the record then names the SHA-256 and lists accepted rows with reasons; see D0 on the literal verdict). Stop and ask you after run 5 if that is not reached; the ticket then stays open. Stop early and ask if a run makes things worse (more unprotected failures than the run before). No fourth fix-and-rerun loop without a new budget decision.
6. **Not budgeted:** a run for the tag split alone, and any run on a summary where you have not decided a changed row.

Expected cost: 3 full runs of 11 chunks plus one coverage audit each, i.e. about 3× the cost of the run-2 attempt (which also included a resume). If you want a cheaper plan, cap at two runs and accept more residual rows; the trade-off is more "accept with reason" rows in the final record, and a second-reader pass over each.

## 7. What I need from you

1. D0: option a, b or c.
2. D1: "Phần nhận xét" (recommended) or another attribution for group C.
3. For each group A–G2: approve the recommended default, or name the rows to open.
4. Omissions: approve add 8 / accept 8, or change.
5. Tag split: confirm.
6. Budget: three paid runs, or another cap.
