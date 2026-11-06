# Hồ sơ quyết định ticket 2.4: V-Qfwjo28Zg

**Đã chốt:** chủ sở hữu chấp thuận khuyến nghị 1A, 2A, 3A, 4A, 5A, 6A, 7A, 8A. Không cần sửa thêm file nào trong 2.4. 1B, 1D và 5A (dựng lại 13 heading) chuyển sang ticket riêng. Ticket giữ `in-review`.

Tài liệu này để anh/chị đọc và quyết. Nó chỉ tổng hợp, không sửa `summary.md`, `report.md` hay `topics/vocabulary.md`. Ticket vẫn `in-review`.

Mọi dẫn chiếu "dòng" là dòng trong `regenerated/transcript.md` hoặc `regenerated/summary.md`. Mọi số liệu lấy từ `review.md` mới (SHA `90c7e4aa6f160052663fe934b1c8c3867c79a05267580650be4f4d1a72cb1fec`).

## Phần 1. Tóm tắt báo cáo

**Ticket 2.4 làm gì.** Video V-Qfwjo28Zg (số 135, glutathione) hiện chưa có `summary.md` trong `videos/`. Bản cũ đã bị gỡ ở commit `4e31e57` để xếp lại hàng. Ticket dựng một bản tóm tắt hiện hành từ bản lịch sử, áp dụng 15 thay thế anh/chị đã duyệt cùng các quyết định trong `human-decisions.md`. Kết quả chỉ nằm trong `audit/V-Qfwjo28Zg/regenerated/`. Không chạm `videos/`, không commit, video vẫn `blocked`.

**Điều cần biết về nguồn.** Video là buổi hỏi–đáp: bác sĩ Trần Văn Phúc trả lời, người dẫn chương trình (Khánh Lành) đọc bình luận khán giả. Phiên âm tự động có nhiều lỗi (ví dụ "GSGS", "NA DPH", "thì sau ra"). Một số xác nhận của anh/chị (GSSG, NADPH, Nhật Bản, "trên dưới 2.000 UI") không có trong phiên âm và chưa kiểm được bằng âm thanh, nên bản tóm tắt gắn nhãn "xác nhận của người duyệt".

| # | Tiêu chí | Kết quả |
|---|---|---|
| 1 | Đầu vào cố định, hash trước khi sinh | Đạt (6/6 hash khớp) |
| 2 | Chỉ dựng trong regenerated/ | Đạt theo intent đã đóng băng |
| 3 | Hợp đồng + validator + review gate | **Không đạt** |
| 4 | Trích dẫn thêm vào kiểm nguyên văn | Đạt (74 trích dẫn, 0 lỗi) |
| 5 | 15 thay thế, đếm một lần | Đạt (15 applied, 0 not applied) |
| 6 | Từ ngữ cố định (c156, c278, c279) | Đạt |
| 7 | 63 mục non-supported | Đạt (17 đã theo quyết định, 46 chưa quyết, giữ câu cũ) |
| 8 | Claim ánh xạ 1-1 vào audit | Đạt một phần (chưa có bảng claim→record) |
| 9 | Không đổi lịch sử, video vẫn blocked | Đạt |

**Review gate (codex gpt-6.1-sol).** 565 claim: 517 pass, 48 fail. 26 concern (14 material, 12 minor), 14 omission, `coverage_complete=False`. Verdict: **fail**. Lần chạy trước có 47 fail. Hai lần chênh nhau vì reviewer không cho kết quả giống hệt nhau.

**Sau triage, đã sửa trong `summary.md`:** ghi chú nín thở ở [03:36:48], ghi chú NADPH, bỏ chữ "nồng độ" ở vitamin D. **Đã sửa trong `report.md`:** nhãn tiêu chí 2 và 8, "bốn nhóm cuối", §7 và §9. **Chưa sửa (chờ anh/chị):** các finding 1, 5, 6 và c013 ở phần 2.

**Lưu ý khi đọc review.** 48 fail chủ yếu là claim kế thừa từ bản lịch sử, chưa sửa vì chưa thuộc quyết định nào. 6 fail nằm ở phần đổi lần này (xem finding 1). Tôi chưa đối chiếu từng claim kế thừa với bản lịch sử, nên nhãn "kế thừa" là suy đoán. Danh sách đủ ở Phụ lục.

---
## Phần 2. Từng finding: bối cảnh, tác động, phương án

Mỗi finding có: **khái niệm nền**, **dữ kiện**, **tác động**, **phương án** và **khuyến nghị**. Ô quyết định ở cuối mục.

### Finding 1 (HIGH). Validator fail 8 tag và review gate fail 48/565

**Khái niệm nền.** Repo dùng "từ vựng tag có kiểm soát" (`topics/vocabulary.md`). Header của mỗi `summary.md` chỉ được dùng tag trong file này, và file ghi rõ "chỉ thêm khi con người duyệt". Hiện file chỉ có 8 tag (y học, dinh dưỡng, omega-3, dha, epa, vitamin d3, màng tế bào, sức khỏe), tạo ra từ một video khác. `validate_summaries.py` loại mọi summary dùng tag ngoài danh sách. Đây chính là lý do `4e31e57` gỡ bản cũ của video này.

**Dữ kiện.**
- 8 tag của video này đều ngoài từ vựng: gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu thiếu sắt, lối sống lành mạnh.
- Review gate là bước riêng: nó chia bản tóm tắt thành 11 chunk, hỏi mô hình từng claim có đúng phiên âm không. Fail không nói bản tóm tắt sai, chỉ nói reviewer không tìm đủ bằng chứng hoặc thấy lệch nguồn.
- Phân loại 48 fail ở Phụ lục. 6 fail thuộc phần đổi/thêm lần này: c209, c385, c480, c483, c551 (đều là nhãn/ghi chú của người duyệt hoặc người tóm tắt, không có trong phiên âm nên reviewer không thể xác minh, đây là hạn chế của cách kiểm chứ không phải lỗi nội dung) và c286 (xem ở dưới). 42 fail còn lại: chủ yếu kế thừa từ bản lịch sử, trong đó c086, c177, c409, c479, c537 mới xuất hiện ở lần chạy lại.

**c286 (cần đọc riêng).** Claim nói: người dẫn đọc bình luận về bố chồng bị tiểu đường (đường huyết 5.5–6.8), sau đó bác sĩ nói "chồng chị Ngân" giảm đường huyết, còn chị Ngọc Thơ hết vàng da. Reviewer thấy: Có phần MC đọc lời điều dưỡng về bố chồng và đường huyết 5.5–6.8. Chưa có phần bác sĩ nói về chồng chị Ngân hoặc kết quả vàng da, vàng mắt của chị Ngọc Thơ. | Có lời bác sĩ về chồng chị Ngân và chị Ngọc Thơ; không có đoạn người dẫn đọc bình luận bố chồng với mức đường huyết 5.5–6.8. | Có bác sĩ kể chồng chị Ngân giảm đường huyết; không có phần người dẫn đọc bố chồng, mức 5.5–6.8, trở về bình thường hoặc vàng da vàng mắt của chị Ngọc Thơ.

**Tác động.** Ticket 2.4 không thể `done` và 2.3 (đưa vào `videos/`) bị chặn. Video không xuất bản được, và summary tiếp tục bị loại khỏi tổng hợp nếu đưa vào `videos/` với tag hiện tại.

**Phương án.**
- **1A.** Chấp nhận tiêu chí 3 "không đạt, đã báo cáo". Giữ 2.4 `in-review`. Chuyển việc tag và các claim fail sang ticket riêng. Không sửa file nào.
- **1B.** Thêm 8 tag vào `topics/vocabulary.md` (cần anh/chị duyệt, vì file nói rõ chỉ thêm khi con người duyệt). Sau đó validator chạy lại. Review gate vẫn fail 48. Tag mới sẽ áp dụng cho mọi video về sau, nên nên quyết có chủ đích.
- **1C.** Đổi tag trong header sang tag đã có (y học, dinh dưỡng, sức khỏe, vitamin d3). Rủi ro: mất độ chính xác khi truy hồi ("bóng đè", "glutathion" không còn trong tag).
- **1D.** Sửa c286 bằng cách tách thành hai câu, mỗi câu gắn một thời điểm (01:11:52 và 02:14:12). Phải chạy lại review gate (tốn quota codex).

**Khuyến nghị.** 1A cho ticket này. Ticket riêng cho 1B (cần anh/chị duyệt từng tag) và 1D. Không chọn 1C.

**Quyết định của anh/chị:** [x] 1A  [ ] 1B  [ ] 1C  [ ] 1D (không trong 2.4; ticket riêng)

### Finding 2 (MEDIUM). Đoạn thở [03:36:48] có thể gây hiểu nhầm an toàn

**Khái niệm nền.** Bác sĩ đang hướng dẫn một bệnh nhân lớn tuổi, yếu (bác Nghiên) tập thở. Phiên âm dòng 6215–6227 ghi "1 1,5 tức là ta cố gắng kéo dài cái thì sau ra một chút…", sau đó "nếu bác thở bác nhịn được chẳng hạn 15 giây, 10 giây… thì chỉ giảm xuống độ 8 9 giây". Anh/chị đã xác nhận "thì sau ra" là "thì thở ra", tức kéo dài thì thở ra, không phải nín thở.

**Dữ kiện.** `human-decisions.md` (c401, c402): sửa theo hướng nhịp thở "1 1,5", kéo dài thì thở ra, **số trung gian giữ theo nguồn, không tự bổ sung**. Vì vậy câu "nhịn được 15 giây, 10 giây" ở lại, và chữ "nhịn" nghe giống nín thở. Tôi đã thêm ghi chú làm rõ ngay sau câu (dòng 523 của `summary.md`). Reviewer vẫn đánh c409 là fail vì không xác minh được xác nhận của anh/chị từ phiên âm, không phải vì ghi chú sai.

**Tác động.** Nội dung y tế về hô hấp cho người yếu: người đọc có thể hiểu nhầm là nên nín thở 8–15 giây. Đây là finding duy nhất có rủi ro an toàn.

**Phương án.**
- **2A.** Giữ ghi chú hiện tại (đã áp dụng).
- **2B.** Giữ và thêm một câu rõ hơn: "không nên nín thở; đây là số giây thở ra theo lời bác sĩ, chưa rõ nghĩa". Thêm câu mới là thêm nội dung ngoài phiên âm, nên cần anh/chị duyệt.
- **2C.** Bỏ cụm số giây khỏi `summary.md`. Vượt quyết định "giữ số theo nguồn".

**Khuyến nghị.** 2A (đã làm). Nếu anh/chị thấy ghi chú chưa đủ an toàn thì chọn 2B. Cần chạy lại review gate sau bất kỳ thay đổi nào.

**Quyết định của anh/chị:** [x] 2A  [ ] 2B  [ ] 2C

### Finding 3 (LOW). Ghi chú NADPH

**Khái niệm nền.** NADPH là phân tử cung cấp năng lượng để "sửa" glutathion bị hỏng trong video (bác sĩ ví glutathion như cái kìm). Phiên âm ghi chữ này thành "NA" và "DPH" ở hai dòng liền nhau (6789–6790), và sau đó là "NADH" (6796). Anh/chị đã xác nhận NADPH là đúng.

**Dữ kiện.** Plan đóng băng yêu cầu nhãn "phiên âm không chứa". Ghi chú cũ tự mâu thuẫn ("không chứa" nhưng dẫn "NA DPH"). Tôi đã sửa còn: *phiên âm không ghi đúng "NADPH"; có "NA"/"DPH" ngắt dòng và "NADH"* (dòng 626). Reviewer vẫn fail c483, vì xác nhận của anh/chị không có trong phiên âm.

**Tác động.** Chỉ là độ chính xác của lời ghi chú. Không đổi ý nghĩa y khoa.

**Phương án.** 3A giữ bản đã sửa (đang áp dụng). 3B quay về nhãn "phiên âm không chứa" nguyên văn plan.

**Khuyến nghị.** 3A.

**Quyết định của anh/chị:** [x] 3A  [ ] 3B

### Finding 4 (LOW). Vitamin D: "khoảng nồng độ"

**Khái niệm nền.** Dược sĩ nước ngoài hướng dẫn bổ sung 50.000 UI/tuần trong 8 tuần để đạt "nồng độ lý tưởng", sau đó chuyển sang một ống theo chu kỳ. Bác sĩ nói thêm lý do giai đoạn đầu.

**Dữ kiện.** Phiên âm dòng 4229–4232 chỉ có "nếu như ở trong khoảng này uống…". Bản tóm tắt cũ thêm "nồng độ". Tôi đã bỏ chữ này (dòng 242), còn "trong một khoảng thì…".

**Tác động.** Nhỏ. Chữ "nồng độ" hợp ngữ cảnh nhưng là diễn giải của người tóm tắt, trái quy tắc "không thêm nội dung ngoài phiên âm".

**Phương án.** 4A giữ bản đã sửa (đang áp dụng). 4B trả lại "khoảng nồng độ".

**Khuyến nghị.** 4A.

**Quyết định của anh/chị:** [x] 4A  [ ] 4B

### Finding 5 (LOW). Heading thời gian lệch (lỗi kế thừa)

**Khái niệm nền.** Mỗi mục trong `summary.md` có heading `[HH:MM:SS]` kèm link `?t=<giây>s`. Người xem bấm link sẽ nhảy tới đúng giây đó. Nếu heading lệch so với nội dung thật, link dẫn sai chỗ.

**Dữ kiện. Phạm vi lớn hơn tôi báo lần trước.** Tôi đã nêu hai chỗ (vitamin D, thư khủng hoảng). Report `regenerated-timefix/report.md` liệt kê **13 heading** có claim lệch xa, ví dụ:
- [01:31:32] Bóng đè: 38 claim nằm xa heading (thực tế từ 02:25 đến 04:11).
- [01:33:05] Vitamin D: 19 claim xa (thực tế 02:44–02:50).
- [02:59:04] Chụp CT lồng ngực: 8 claim xa (thực tế 03:28–03:32).
- [03:36:48] Hướng dẫn thở: 3 claim xa (thực tế 04:09–04:10).
Hai heading còn bị đảo thứ tự (04:04:39 trước 04:03:09; 04:14:18 trước 04:13:09). Phân tích đó dùng quote trong `review.md` để định vị. Anh/chị đã chọn phương án A cho `regenerated-timefix/`: **giữ nguyên summary, chỉ báo cáo**, vì phần lệch thuộc nhóm "bản lịch sử dồn nhiều nội dung dưới một heading", không sửa được chỉ bằng đổi giờ.

**Tác động.** Link `?t=` ở các mục lệch đưa người xem tới sai chỗ trong video. Không ảnh hưởng chuẩn validator.

**Phương án.**
- **5A.** Không sửa trong 2.4. Mở ticket riêng để dựng lại heading (cần tách nội dung, không chỉ đổi số).
- **5B.** Sửa ngay các heading trong 2.4. Vượt phạm vi đóng băng của ticket.

**Khuyến nghị.** 5A, và nêu rõ trong ticket mới rằng phạm vi là 13 heading, không phải 2.

**Quyết định của anh/chị:** [x] 5A  [ ] 5B

### Finding 6 (LOW). c156 không còn gắn "tim đập nhanh" vào chiều thức→ngủ

**Khái niệm nền.** "Bóng đè" theo bác sĩ: não phát lệnh liệt cơ khi ngủ (như cái phanh), nhưng phanh vào hoặc nhả sai thời điểm. Có hai chiều: thức→ngủ (phanh chưa kịp làm, nên người nói và vận động trong mơ) và ngủ→thức (phanh chưa nhả, nên não tỉnh mà tay chân không cử động).

**Dữ kiện.** Phiên âm dòng 3846–3848 (02:32:16–02:32:23): "Và tim đập nhanh. Đó là gì? Đó là chúng ta đang từ thức chuyển sang ngủ nhưng lại không có phanh." Bản hiện tại (dòng 210) nói thức→ngủ "không làm được kịp thời" nhưng không nhắc tim đập nhanh. c158 bỏ cụm này đúng theo bản anh/chị đã duyệt. `human-decisions.md` chỉ yêu cầu gộp chiều thức→ngủ theo đề xuất, không nhắc "tim đập nhanh".

**Tác động.** Mất một sắc thái (triệu chứng đi kèm), không sai nghĩa.

**Phương án.** 6A giữ nguyên. 6B thêm cụm "bản ghi cũng nhắc tim đập nhanh khi tỉnh đột ngột". Vì 15 câu thay thế đã duyệt từng chữ, thêm cụm này làm lệch khỏi bản duyệt.

**Khuyến nghị.** 6A.

**Quyết định của anh/chị:** [x] 6A  [ ] 6B

### Finding 7 (LOW). Report chấm tiêu chí 8 và tiêu chí 2

**Khái niệm nền.** Tiêu chí 8 đòi mỗi claim ánh xạ 1-1 vào record audit và mọi claim tách/gộp/thêm/xóa được liệt kê. Report có số liệu (554→565, 26 thay/sửa, 9 thêm, 1 xóa) và danh sách claim thêm, nhưng không có bảng ánh xạ đầy đủ. Tiêu chí 2 chỉ cho phép khác biệt ở 15 thay thế và vài mục đã chốt, trong khi intent đóng băng cho phép áp dụng mọi quyết định đã ghi.

**Dữ kiện.** Tôi đã đổi nhãn tiêu chí 8 thành "Đạt một phần" và tiêu chí 2 thành "Đạt theo intent đã đóng băng".

**Phương án.** 7A giữ nhãn đã sửa (đang áp dụng). 7B thêm bảng ánh xạ đầy đủ 565 dòng (script ngoài repo). 7C quay về nhãn "Đạt".

**Khuyến nghị.** 7A. Chọn 7B nếu anh/chị cần bằng chứng đầy đủ cho ticket 2.3.

**Quyết định của anh/chị:** [x] 7A  [ ] 7B  [ ] 7C

### Finding 8 (LOW). "Ba mục cuối" và c013 lặp câu mở

**Dữ kiện.** Report §3 viết "ba mục cuối" nhưng liệt kê bốn nhóm: tôi đã sửa thành "bốn nhóm cuối". Còn c013 (dòng 33 `summary.md`): câu thay thế đã duyệt mở bằng "có thể nói rằng", ngay sau câu mở đầu cũng có cụm này, nên đọc hơi lặp. Câu c013 khớp từng chữ với `revised-summary-draft.md` anh/chị đã duyệt.

**Phương án.** 8A giữ c013 nguyên văn (đang áp dụng, report đã ghi là có chủ đích). 8B bỏ chỗ lặp, nhưng lệch khỏi bản duyệt. 8C quay về "ba mục cuối".

**Khuyến nghị.** 8A.

**Quyết định của anh/chị:** [x] 8A  [ ] 8B  [ ] 8C

---
## Phần 3. Đã bác bỏ, không sửa

- **c401** có căn cứ từ `human-decisions.md`.
- **Ba file audit tracked** (`omission-anchors.json`, `omissions.md`, `proposed-corrections.md`) đã dirty trước run; report §6 xác nhận không đổi.
- **`regenerated-timefix/`** tạo sau report 2.4, không thuộc change này (xem finding 5).

---
## Phần 4. Điểm cần chú ý ngoài danh sách

1. **Việc anh/chị cần làm cho ticket.** Ticket yêu cầu chủ sở hữu đọc bản mới đối chiếu 15 thay thế với `revised-summary-draft.md` trước khi chấp nhận report (risk high, nội dung y tế). Report §2 có bảng 15 thay thế kèm dòng trong `summary.md`.
2. **`review.md` mới chỉ đúng cho SHA `90c7e4aa…`.** Mọi sửa `summary.md` thêm sẽ làm nó cũ và cần chạy lại.
3. **46 mục "chưa quyết".** Giữ câu cũ, được báo là "chưa quyết". Chúng không nằm trong finding nào. Một số có vẻ trùng với fail của reviewer (ví dụ c034, c045, c054 xuất hiện ở cả hai danh sách), nhưng id claim đã dịch chuyển giữa bản lịch sử và bản mới nên tôi chưa đối chiếu hết. Anh/chị cần quyết riêng nếu muốn xử lý (ticket khác).
4. **Số 48 ≠ 46.** Lần trước anh/chị nêu 48 mục chưa quyết; tôi đếm 46 (xem report §4). Còn 48 ở đây là số claim fail của reviewer, hai số khác nhau.

---
## Phụ lục. 48 claim fail của review gate


### Không có bằng chứng trong phiên âm (5)

- **c087** (không có mốc): no transcript evidence found in any chunk
- **c241** (không có mốc): no transcript evidence found in any chunk
- **c308** (không có mốc): no transcript evidence found in any chunk
- **c389** (không có mốc): no transcript evidence found in any chunk
- **c484** (không có mốc): no transcript evidence found in any chunk

### Người nói chưa xác định là bác sĩ (bản tóm tắt gán cho bác sĩ) (7)

- **c367** (03:28:54-03:29:14): Nội dung liên hệ có trong phần phân tích; riêng đoạn này không xác định người đang trình bày là bác sĩ. | Có bác sĩ liên hệ mất vợ, hút thuốc giải buồn và nghề thợ mộc; không định lượng thời gian làm mộc hàng c
- **c370** (03:32:04-03:32:23): Cơ chế được nêu trong phần phân tích; đoạn này chưa xác định người trình bày là bác sĩ. | Có thiếu vi chất, rút canxi từ xương và lắng đọng thành mạch; không chỉ rõ vitamin D, magie kéo dài hay riêng động mạch 
- **c382** (03:25:00-03:25:10): Có nội dung ưu tiên viêm mạn tính; đoạn này chưa xác định người trình bày là bác sĩ.
- **c384** (03:25:26-03:25:39): Nội dung được nêu trong phần phân tích, nhưng đoạn này không xác định người nói là bác sĩ.
- **c394** (03:34:58-03:35:05): Có nội dung uống nước trong phần phân tích; đoạn này chưa xác định người nói là bác sĩ.
- **c397** (03:35:35-03:35:43): Có lời hướng dẫn này trong phần phân tích; đoạn này chưa xác định người nói là bác sĩ. | Có hướng dẫn giải quyết tinh thần cho bác Nghiên; không lặp lại cách gọi việc đầu tiên hay xoa dịu lồng ngực.
- **c457** (04:17:42-04:17:49): Lời gọi truyền miệng là 'hào nhoáng' và lời dẫn sang góc nhìn y khoa thuộc người dẫn Khánh Lành, không phải bác sĩ.

### Bản tóm tắt bỏ/đổi hạn định (một số, ít nhất, điều kiện…) (7)

- **c045** (00:38:32-00:38:44): Transcript nói phá hủy các mô, không giới hạn ở mô hoại tử như bản tóm tắt.
- **c167** (02:35:06-02:35:09): Đúng về giả dược và trấn an tâm lý, nhưng 'không phải hiệu quả thực sự' tuyệt đối hơn lời nói dè dặt 'không hẳn chủ yếu là trấn an tâm lý'.
- **c177** (02:40:03-02:40:16): Bản tóm tắt bỏ giới hạn 'một số', khiến phát biểu về người có bệnh đường ruột trở thành khái quát rộng hơn nguồn.
- **c201** (02:46:44-02:46:56): Bỏ điều kiện không nhiều mỡ, ít mỡ dưới da và không có mỡ nội tạng trong mô tả người dùng liều cao dễ, hiệu quả.
- **c216** (01:37:20-01:37:47): Bác sĩ nói không phải ai cũng được trời cho trí tuệ tốt, rồi kể thành công của bản thân nhờ cần cù và quyết tâm. Tóm tắt biến lời tự sự có giới hạn thành khẳng định chung về nguồn gốc trí tuệ. | Bác sĩ nói khôn
- **c455** (04:12:52-04:13:11): Nguồn nói 'ít nhất' 18 sản phẩm, không phải 'khoảng' 18; các thành phần bổ sung thêm được nêu đúng.
- **c537** (05:12:05-05:12:15): Phần ngấm không nhiều được hỗ trợ. Tuy nhiên, bản ghi chỉ nhắc trẻ bị sốt và một số thuốc ngậm dưới lưỡi, không xác định rõ đó là thuốc hạ sốt cho trẻ em.

### Nhãn/xác nhận của người duyệt, không có trong phiên âm (7)

- **c209** (02:49:13-02:49:20): Có các chuỗi số phiên âm và nhận định đa số trên dưới 2.000 UI. Xác nhận của người duyệt về cách đọc 5.600 và 6.000–7.000 không nằm trong lát cắt.
- **c385** (03:25:43-03:25:59): Có các mức 1000–1500 và kết luận an toàn trong phần phân tích. Phiên âm không ghi rõ Nhật Bản, không chứng minh xác nhận của người duyệt và không xác định người nói là bác sĩ.
- **c409** (04:09:52-04:10:18): Hỗ trợ lời hướng dẫn và các con số; không thể xác minh xác nhận kỹ thuật của người duyệt từ transcript này.
- **c479** (04:31:42-04:31:52): Có hai glutathion hỏng khóa vào nhau; ký hiệu phiên âm không nhất quán, lúc ghi GSGS, lúc tách GS và SG, nên chưa xác nhận sạch toàn bộ ký hiệu GSSG.
- **c480** (không có mốc): no transcript evidence found in any chunk
- **c483** (04:32:24-04:32:39): Xác nhận các dạng phiên âm NA/DPH và NADH; việc người duyệt xác nhận NADPH không nằm trong transcript.
- **c551** (không có mốc): no transcript evidence found in any chunk

### Khác (chi tiết/diễn giải lệch nguồn) (22)

- **c034** (00:16:27-00:16:44): Transcript mô tả chất béo bị đốt cháy “dở dở đi”, không phải “quá mức”; phần ví dụ chiên rán và dùng sai dầu thực vật có trong nguồn.
- **c042** (00:35:16-00:35:45): Có enzyme SOD và ví dụ buộc hai gia đình thỏa thuận; không đọc đầy đủ tên superoxide dismutase.
- **c054** (00:45:54-00:46:02): Bản tóm tắt nhập hai bước: transcript mô tả thêm một oxy vào O₂ tạo cuộc tình tay ba, rồi mới nói ozon xen vào các gia đình khác; không nói ozon xen vào các phân tử oxy khác để tạo cuộc tình tay ba. | Đoạn này 
- **c068** (00:06:52-00:07:02): Có nói gốc tự do liên quan bệnh mãn tính và nhiều bệnh khác; chưa nói lão hóa hoặc hậu quả riêng của lipit peroxit.
- **c086** (01:08:34-01:08:45): Có nhận xét tự đọc tài liệu khó hiểu và cách giải thích giúp hiểu gốc tự do; chưa nói rõ tác dụng giúp dễ nhớ hơn. | Có lời bác sĩ nói cách diễn giải giúp dễ hiểu hơn tự đọc tài liệu; không nói rõ giúp dễ nhớ h
- **c110** (01:12:01-01:12:12): Người đưa ra nhận xét là chủ nhiệm khoa, không phải điều dưỡng. Nhận xét chỉ nói về magie, không phải toàn bộ vi chất.
- **c113** (01:13:48-01:14:01): Nguồn nói 'xương cổ đùi', tức một vị trí giải phẫu; tóm tắt tách thành xương cổ và xương đùi.
- **c123** (01:20:23-01:20:32): Người xem kể trước đây đau đầu kèm buồn nôn, nhưng phần kết quả chỉ xác nhận hết đau đầu, không xác nhận hết buồn nôn.
- **c129** (01:24:11-01:24:33): Loại sắt trong transcript là sắt hai 'xun phát khô', không phải sắt II fumarat khô. Các chi tiết ngày bắt đầu, liều sắt và B9 được nêu.
- **c192** (01:34:05-01:34:20): Phần này có câu hỏi và chưa có trả lời trực tiếp về vitamin D; phần bàn về vitamin D được dẫn chiếu chưa xuất hiện trong slice.
- **c212** (02:52:31-02:52:37): Ở lời tổng kết mười bình luận trong lát cắt này, bác sĩ gọi chủ đề liên quan là gốc tự do, không phải glutathion.
- **c253** (02:03:44-02:03:50): Trải nghiệm được bác sĩ thuật lại, nhưng tên Thủy chỉ là phỏng đoán của ông; tóm tắt bỏ sự không chắc chắn về tên.
- **c256** (01:13:22-01:13:32): Có nghề nghiệp, triệu chứng, lo ngại ung thư và uống nhiều thuốc không đỡ; đoạn này không xác nhận chi tiết càng uống càng nặng. | Các chi tiết về nghề nghiệp, đau xương và uống thuốc không đỡ được nói đến; câu
- **c264** (02:07:41-02:07:55): Transcript quy nghi vấn ban đầu về thiếu máu thiếu sắt cho chính người viết bình luận; không chứng minh người dẫn là người đặt nghi vấn.
- **c285** (04:12:57-04:13:05): Có nêu bo và silic là các thành phần bổ sung thêm; chưa nói chúng thường có sẵn trong sản phẩm bổ sung.
- **c286** (01:11:52-01:12:01): Có phần MC đọc lời điều dưỡng về bố chồng và đường huyết 5.5–6.8. Chưa có phần bác sĩ nói về chồng chị Ngân hoặc kết quả vàng da, vàng mắt của chị Ngọc Thơ. | Có lời bác sĩ về chồng chị Ngân và chị Ngọc Thơ; kh
- **c295** (02:21:13-02:21:26): Nguồn chỉ kể 'có những người' hết đau hoặc đỡ 90–95%; không khẳng định toàn bộ số còn lại đều chỉ đau nhẹ.
- **c299** (01:29:17-01:29:40): Nguồn nói ăn hoặc uống đường mía thô lúc mệt để thấy dễ chịu, không phải ăn 'đồng' để quên cơn đau. | Transcript nói ăn đường để quên đau, không phải ăn đồng.
- **c360** (03:23:25-03:23:36): Nguồn nói số lượng xe chở sắt giảm, không phải lượng sắt lưu hành giảm; trước đó còn nói lượng sắt lưu hành vẫn giữ được sự nhịp nhàng.
- **c415** (04:11:16-04:11:54): Thứ tự liệt kê là magie, canxi, D3, vitamin tổng hợp, C, kẽm, omega 3. Kẽm không được xếp thứ hai trong danh sách tuần tự.
- **c488** (04:37:48-04:38:02): Đoạn này không xác lập tổng cộng ba nguồn chính: sau tinh thần, ăn uống và thuốc, bác sĩ còn liệt kê kim loại nặng và gọi đó là cái thứ ba.
- **c510** (04:51:59-04:52:13): Có ADN riêng sát màng ti thể, bị phá hủy và đột biến; không xác định rõ là sát màng trong.

**Ghi chú.** Các nhóm do tôi phân theo từ khóa trong lý do reviewer, không phải kết luận của reviewer. Nhóm "Khác" cần đọc từng mục.
