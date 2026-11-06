# Báo cáo regenerated-timefix: V-Qfwjo28Zg

**Trạng thái:** chưa done, chờ chủ sở hữu duyệt. Video vẫn `blocked`. Không commit, stage, push, stash, publish.

## 1. Quyết định
Theo tư vấn của claude-opus-5-5 (chủ sở hữu duyệt phương án A): **giữ nguyên summary.md, chỉ báo cáo**. Không có mục nào thuộc nhóm (a) (chỉ cần đổi giờ heading và `?t=`), nên không sửa heading nào. Các mục lệch thuộc nhóm (b): bản lịch sử gộp phần hỏi (đọc thư/số liệu) với phần bác sĩ trả lời ở giờ sau; chỉ sửa được bằng cách di chuyển claim hoặc tách mục, việc này bị loại vì đổi SHA, làm lệch id claim, mất hiệu lực review.md và cần heading/câu Q mới chưa duyệt.

## 2. Bản sao (SHA-256)
| File | SHA-256 | So với regenerated/ |
|---|---|---|
| summary.md | 222a28efb8896dc3bf03f069156b1c815261be9ddc6da0bb4f8ab59183e122e5 | giống từng byte |
| transcript.md | dedb6e4d414945da6e0c7895fbcdf5344d5c366305b1bcc7a034eb6cc59776e4 | giống từng byte |
| metadata.json | e267743ff47d1ce43bd297f7225b464af33ebfe1be77201c72b1d2f19a285b08 | giống từng byte |

Vì summary.md giống từng byte nên text claim không đổi, id claim (c001…c565) và trường `section` vẫn khớp `regenerated/review.md`. Không cần review gate mới (không chạy mô hình ngoài).

## 3. Kiểm tra
- 113 heading: `[HH:MM:SS]` khớp `?t=<giây>s`, giờ lớn nhất ≤ 19415. Đạt.
- Hai heading đã đảo thứ tự từ bản lịch sử: 04:04:39 trước 04:03:09 và 04:14:18 trước 04:13:09 (validator không kiểm thứ tự; không sửa).
- `validate_summaries.py --videos-dir audit/V-Qfwjo28Zg`: exit 1, `regenerated-timefix: summarized (tags outside vocabulary: gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu thiếu sắt, lối sống lành mạnh)`. Đây là **lỗi tag vocabulary kế thừa** từ header lịch sử, giống hệt `regenerated/`; không vá.
- Review bound: `regenerated/review.md` (verdict fail, 47/565) vẫn gắn đúng SHA 222a28 của bản sao này.

## 4. Mục có khoảng thực lệch so với heading (nhóm b, không sửa)
Giờ bằng chứng lấy từ quote trong review.md, đối chiếu nguyên văn với transcript.md (±30 s). Cột "gần" = số claim trong [heading−120s, heading+420s]; "xa" = số claim ngoài khoảng đó.

| Heading hiện tại | Chủ đề | Claim gần | Claim xa | Giờ thực của claim xa |
|---|---|---|---|---|
| 00:19:12 | Superoxit: gốc tự do cơ bản nhất | 3 | 2 | 00:31:19–00:35:22 |
| 00:48:55 | Gốc tự do tấn công màng tế bào: lipid và lipit peroxit | 10 | 2 | 00:06:52–00:32:00 |
| 01:31:32 | Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý | 2 | 38 | 02:25:54–04:11:37 |
| 01:33:05 | Vitamin D 50.000 IU: liều, nồng độ mục tiêu và cách duy trì | 5 | 19 | 02:44:45–02:50:18 |
| 02:10:50 | Rối loạn tụy, tiểu đường và cân nặng sau khi bổ sung vi chất | 5 | 3 | 04:53:37–04:54:54 |
| 02:22:01 | Đau nửa đầu của chị Nhung và tim nhanh: kết quả sau khi bổ s | 5 | 4 | 01:29:34–02:44:15 |
| 02:53:59 | Hồ sơ bệnh nhân Lương Trắc Nghiên và chỉ số cơ thể | 8 | 4 | 03:09:46–03:10:57 |
| 02:55:58 | Công thức máu của bác Lương Trắc Nghiên: MPV, MCV, MCH | 4 | 4 | 03:13:53–03:15:27 |
| 02:56:30 | Chức năng gan, thận và mỡ máu của bác Lương Trắc Nghiên | 5 | 2 | 03:17:03–03:17:22 |
| 02:57:13 | Axit uric 459,1 và cholesterol tăng ở người gầy | 3 | 5 | 03:18:45–04:03:29 |
| 02:57:43 | Sắt, vitamin và khoáng chất: feritin, TSAT và biểu hiện thiế | 12 | 6 | 03:20:57–03:23:39 |
| 02:59:04 | Chụp CT lồng ngực của bác Lương Trắc Nghiên: tổn thương phổi | 5 | 8 | 03:28:54–03:32:04 |
| 03:36:48 | Học lại cách thở và các kỹ thuật thở cho bác Nghiên | 9 | 3 | 04:09:52–04:10:24 |
| 03:38:50 | Bảy nhóm vi chất, danh sách theo thứ tự và thời gian phục hồ | 5 | 3 | 04:11:00–04:11:16 |
| 04:19:29 | Đường, gốc tự do và trường hợp chị Hằng: vòng xoắn bệnh lý v | 3 | 5 | 02:41:03–04:45:52 |
| 04:21:40 | Cấu tạo, hoạt động và tái tạo của glutathion | 5 | 9 | 04:29:03–04:32:39 |

Mục stub đã có sẵn: 02:26:23, 02:34:11, 02:35:19 (→01:31:32); 02:43:43 (→02:22:01); 03:31:26 (→02:59:04); 04:03:09 (→02:57:13); 04:53:37 (→02:10:50). Mục 01:33:05 Vitamin D (19 claim ở 02:44:45–02:50:18) và các cặp đọc số liệu/bình luận không có stub.

## 5. Ví dụ trong yêu cầu
- c054 (00:45:22), c256 (02:04:21), c299 (02:22:01): không phải heading lệch. Bằng chứng reviewer ghi sai chỗ; nội dung thật ở 00:45:54, 02:04:21, 02:22:47, đúng heading.
- c068, c285, c286: claim fail/không có bằng chứng, đổi giờ heading không sửa được.
- Không định vị được giờ bằng quote: c087, c241, c308, c389, c480, c484, c551.

## 6. Hệ quả nếu sau này di chuyển/tách
Id claim và `section` của final_records.json/review.md sẽ không còn khớp 1-1 với audit; bản mới cần audit riêng và review gate mới trên SHA mới. Cách an toàn nếu làm: chỉ chuyển nguyên khối `**Q:` vào stub có sẵn (B-hẹp), lập file đối chiếu theo nội dung claim, chạy review gate (cần chủ sở hữu cho phép).
