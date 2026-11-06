# Review narrative: bản nháp summary đã sửa của V-Qfwjo28Zg

**Block hiện tại:** không còn; review đã hoàn tất, xem [Wrap-up](#wrap-up)

**Nhật ký review:** [walkthrough-revised-summary-draft-log.md](walkthrough-revised-summary-draft-log.md)

## Block 1: Intent

- [x] **Trạng thái:** đã được người review chấp nhận. Không thay đổi trong review.

**Nguồn của phần này:** tóm tắt từ [plan audit V-Qfwjo28Zg](../initiative-tran-van-phuc-knowledge-base/tickets/epic-summary-source-audit/tickets/story-full-source-grounded-audit-of-v-qfwjo28zg-554-claims-plan.md) và bối cảnh do người giao việc cung cấp. Plan không nói về bản nháp, nên đây không phải đoạn trích nguyên văn.

**Vấn đề theo plan:** audit có 554 claim nhưng không còn summary ở HEAD, vì summary đã bị xóa khỏi [videos/](../../videos/) tại commit `4e31e57`. Audit vì thế gắn với summary lịch sử ở `4e31e57^`.

**Bản nháp này làm gì:** lấy summary lịch sử đó và thay đúng 15 đề xuất trong [additional-corrections.json](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/additional-corrections.json).

**Không làm gì:** không sửa [videos/](../../videos/), [final_records.json](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/final_records.json) hay [check_audit.py](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/check_audit.py), và chưa xuất bản.

**Câu hỏi cho người review:** từng đoạn đã thay có bám đúng lời nói trong bản ghi, giữ đúng người nói và mức độ dè dặt, và có nên được chấp nhận hay không?

## Block 2: Broad strokes

- [x] **Trạng thái:** đã được người review chấp nhận. Không thay đổi trong review.

Thay đổi là một tệp summary mới, tạo bằng cách thay 15 đoạn trong summary lịch sử. Nên mở theo thứ tự:

1. [additional-corrections.json](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/additional-corrections.json): danh sách 15 đề xuất được áp dụng.
2. [revised-summary-draft.md](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md): target, tức bản nháp sau khi thay.
3. [plan audit](../initiative-tran-van-phuc-knowledge-base/tickets/epic-summary-source-audit/tickets/story-full-source-grounded-audit-of-v-qfwjo28zg-554-claims-plan.md): bối cảnh của audit 554 claim.

## Block 3: Slice, 15 đề xuất trong target

- [x] **Trạng thái:** đã được người review chấp nhận. Không thay đổi trong review.

Mỗi đề xuất thay một đoạn của summary lịch sử; 15 đề xuất nằm ở 13 vị trí, vì hai cặp claim dùng chung một dòng. Số dòng lấy từ bản nháp ở thời điểm khởi tạo và sẽ lệch nếu target thay đổi. Kết luận cho từng vị trí được ghi vào [log](walkthrough-revised-summary-draft-log.md), cùng các điểm còn mở cần kiểm tra khi xem block này.

| # | Claim | Vị trí trong target | Mục | Class gốc |
|---|-------|---------------------|-----|-----------|
| 1 | c013 | [dòng 33](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L33) | [00:06:34] Gốc tự do liên quan đến bệnh mãn tính và ung thư như thế nào? | attribution_qualification |
| 2 | c156, c158 | [dòng 210](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L210) | [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý | mismatch (c156), supported (c158) |
| 3 | c213 | [dòng 271](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L271) | [01:40:58] Đĩa thức ăn hạnh phúc: cách chia khẩu phần | supported |
| 4 | c242 | [dòng 324](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L324) | [02:02:00] Quan sát ở Nhật và châu Âu: khẩu trang, bệnh mùa đông và thiếu vi chất | supported |
| 5 | c260 | [dòng 349](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L349) | [02:09:17] Cơ chế vàng da: gốc tự do từ tia UV và bụi mịn | supported |
| 6 | c275, c278 | [dòng 367](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L367) | [02:13:40] Vitamin C, E, glutathion và các vi chất phối hợp với nhau | attribution_qualification (c275), supported (c278) |
| 7 | c279 | [dòng 372](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L372) | [02:16:47] Đau dây thần kinh số 5 và nang dưới nhện: quan điểm không mổ | supported |
| 8 | c286 | [dòng 377](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L377) | [02:19:04] Tiêm vào vỏ bao hạch dây thần kinh số 5: kỹ thuật và tái phát | supported |
| 9 | c318 | [dòng 430](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L430) | [02:55:58] Công thức máu của bác Lương Trắc Nghiên: MPV, MCV, MCH | supported |
| 10 | c402 | [dòng 523](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L523) | [03:36:48] Học lại cách thở và các kỹ thuật thở cho bác Nghiên | supported |
| 11 | c538 | [dòng 707](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L707) | [05:15:59] Thực phẩm chứa cơ chất tổng hợp glutathione và số loại thực phẩm mỗi ngày | supported |
| 12 | c544 | [dòng 712](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L712) | [05:17:28] Giảm gốc tự do, lối sống và cách ăn uống để bảo vệ glutathione | supported |
| 13 | c552 | [dòng 717](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md#L717) | [05:19:25] Quan điểm của bác sĩ về sản phẩm glutathione đắt tiền | supported |

## Block 4: Periphery

- [x] **Trạng thái:** đã được người review chấp nhận. Không thay đổi trong review.

- [videos/](../../videos/): không bị bản nháp này sửa.
- [final_records.json](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/final_records.json): bản ghi audit, không bị sửa.
- [check_audit.py](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/check_audit.py): checker của audit, không bị sửa.

## Wrap-up

- [x] **Trạng thái:** đã được người review chấp nhận. Review đã hoàn tất.

Toàn bộ 4 block đã được người review chấp nhận.

**Follow-through được chọn:** giữ [revised-summary-draft.md](../initiative-tran-van-phuc-knowledge-base/audit/V-Qfwjo28Zg/revised-summary-draft.md) là bản nháp audit đã áp dụng 15 thay thế, không đưa vào [videos/](../../videos/) và không xuất bản. Mọi áp dụng vào pipeline hoặc source chuẩn cần ticket và phạm vi riêng.
