# Báo cáo ticket 2.4: summary V-Qfwjo28Zg dựng từ bản lịch sử + 15 thay thế đã duyệt

**Trạng thái:** chưa done, chờ chủ sở hữu duyệt. Video vẫn `blocked` (publishable = False). Không commit, không stage, không publish. Chỉ ghi dưới `audit/V-Qfwjo28Zg/regenerated/` và plan file của ticket.

**summary.md:** SHA-256 `90c7e4aa6f160052663fe934b1c8c3867c79a05267580650be4f4d1a72cb1fec` (565 claim; bản lịch sử 554 claim).

## 1. Chín tiêu chí

| # | Tiêu chí | Kết quả | Ghi chú |
|---|---|---|---|
| 1 | Đầu vào cố định, hash trước khi sinh | **Đạt** | 6/6 hash khớp ticket, xem `provenance.json`. |
| 2 | Chỉ dựng trong regenerated/, khác biệt chỉ ở các mục được duyệt | **Đạt theo intent đã đóng băng** | Không chạm videos/, không chạy generator. Chủ sở hữu chọn áp dụng toàn bộ quyết định đã ghi (xem mục 3), rộng hơn danh sách tối thiểu của ticket. |
| 3 | Hợp đồng + validator + review gate | **Không đạt** | validate_summaries.py: FAIL vì 8 tag header ngoài `topics/vocabulary.md` (đúng lý do 4e31e57 gỡ bản cũ). Với vocabulary chẩn đoán tạm ở /tmp, mọi kiểm tra cấu trúc đạt. Review gate (codex gpt-6.1-sol) chạy xong: verdict **fail**, 47/565 claim fail, coverage_complete=False, review nêu đúng SHA của summary. Không vá. |
| 4 | Trích dẫn thêm vào được kiểm nguyên văn | **Đạt** | 74 trích dẫn (15 thay thế, 7 mục đã chốt, các đoạn tôi viết thêm), 0 lỗi (verify_quotes.py, dung sai 5 s). Mọi đoạn “…” trong câu đổi đều là chuỗi con của phiên âm. |
| 5 | 15 thay thế, đếm một lần | **Đạt** | 15 applied, 0 not applied (mục 2). c013, c156, c275 không đếm lại từ proposed-corrections.json. |
| 6 | Từ ngữ cố định | **Đạt** | c156: thức → ngủ trong một câu. c278: có cả "bố chồng" và "chồng chị Ngân". c279: "u não" nằm trong lời bác sĩ, không gán nghi ngờ cho chị Nhung. |
| 7 | 63 mục non-supported: followed / not followed / undecided | **Đạt** | followed 17, not followed 0, undecided 46 (mục 4). Không có mục chưa quyết nào bị áp dụng. Không thêm nội dung y khoa ngoài phiên âm. |
| 8 | Claim ánh xạ 1-1 vào audit | **Đạt một phần** (chưa có bảng claim→record, chỉ có số liệu và danh sách khác biệt; có khác biệt đã liệt kê) | Mỗi claim mới ánh xạ tối đa một record, không sửa record audit. Khác biệt đều do thay đổi đã duyệt (mục 5), không có khác biệt ngoài dự kiến nên không dừng. |
| 9 | Không đổi lịch sử, video vẫn blocked | **Đạt** | Mục 6. |

## 2. Bảng 15 thay thế

| Mục | Kết quả | Dòng trong regenerated/summary.md | Mục (section) | Claim mới | Lý do |
|---|---|---|---|---|---|
| c318 | applied | 430 | [02:55:58] Công thức máu của bác Lương Trắc Nghiên: MPV, MCV, MCH | c326 | Bản tóm tắt diễn đạt kết luận liền mạch và bỏ các cụm phiên âm chưa rõ của phần nhận xét. |
| c156 | applied | 210 | [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý | c161 | Câu cũ nói “không được kịp nhả”, trong khi đoạn này nói về chiều từ thức vào ngủ và phanh chưa kịp làm |
| c275 | applied | 367 | [02:13:40] Vitamin C, E, glutathion và các vi chất phối hợp với nhau | c283 | Câu cũ gán phần này cho người dẫn và làm nhẹ cách nói “cũng là gốc tự do” |
| c544 | applied | 712 | [05:17:28] Giảm gốc tự do, lối sống và cách ăn uống để bảo vệ glutathione | c554, c555 | Câu cũ thay “rượu chè” bằng “rượu bia”, bỏ cách nói về thuốc lá, và chuẩn hóa “Glutaton”. |
| c552 | applied | 717 | [05:19:25] Quan điểm của bác sĩ về sản phẩm glutathione đắt tiền | c563 | Câu cũ bỏ ý “hiểu cơ chế” và thêm kết luận “không phải từ một sản phẩm cụ thể”, vốn không có trong câu được dẫn. |
| c286 | applied | 377 | [02:19:04] Tiêm vào vỏ bao hạch dây thần kinh số 5: kỹ thuật và tái phát | c294 | Câu cũ bỏ điều kiện “bị viêm” và làm nhẹ lượng từ “hầu hết”. |
| c158 | applied | 210 | [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý | c163 | Câu cũ gộp “tim đập nhanh” từ chiều thức sang ngủ vào mô tả chiều ngủ sang thức. |
| c242 | applied | 324 | [02:02:00] Quan sát ở Nhật và châu Âu: khẩu trang, bệnh mùa đông và thiếu vi chất | c250 | Bản ghi không nêu ai “giải thích” cho ông; đó là phần bác sĩ kể tiếp sau quan sát. |
| c260 | applied | 349 | [02:09:17] Cơ chế vàng da: gốc tự do từ tia UV và bụi mịn | c268 | Câu cũ gộp các bước và bỏ điều kiện “gốc tự do ở da”; đề xuất giữ thứ tự nguyên nhân được nói trong bản ghi. |
| c402 | applied | 523 | [03:36:48] Học lại cách thở và các kỹ thuật thở cho bác Nghiên | c410 | Câu cũ biến lời hướng dẫn thành các “nhịp” xác định |
| c213 | applied | 271 | [01:40:58] Đĩa thức ăn hạnh phúc: cách chia khẩu phần | c221 | Câu cũ đổi chủ thể sang “đứa trẻ” và rút mất mốc “lứa tuổi học sinh” cùng điều kiện được nói tiếp về người mẹ. |
| c538 | applied | 707 | [05:15:59] Thực phẩm chứa cơ chất tổng hợp glutathione và số loại thực phẩm mỗi ngày | c548 | Bản ghi không xác định “Fittain” là cơ chất nào; đề xuất giữ nguyên phiên âm và cách gọi số nhiều trong đoạn sau. |
| c278 | applied | 367 | [02:13:40] Vitamin C, E, glutathion và các vi chất phối hợp với nhau | c286 | Câu cũ gộp các lời kể ca cụ thể thành kết luận chung |
| c279 | applied | 372 | [02:16:47] Đau dây thần kinh số 5 và nang dưới nhện: quan điểm không mổ | c287 | Câu cũ gán việc nghi u não cho chị Nhung |
| c013 | applied | 33 | [00:06:34] Gốc tự do liên quan đến bệnh mãn tính và ung thư như thế nào? | c013 | Câu cũ tách một phần của “con đường đi” của bệnh tật thành khẳng định chung về sự hình thành gốc tự do, đồng thời bỏ giới hạn và nguồn nội sinh được nói riêng. |

Tổng: applied 15 + not applied 0 = 15. Đối chiếu: 15 câu thay thế khớp từng chữ với `revised-summary-draft.md` (bản tham chiếu); c013 đứng sau câu mở đầu cũng có “có thể nói rằng” nên đọc hơi lặp, giữ nguyên như đã duyệt.

## 3. Mục đã chốt ngoài 15 (áp dụng theo human-decisions.md)

| Mục | Việc đã làm |
|---|---|
| c456 | Bỏ câu; giữ lời miễn trừ chung ở c553 (không đụng). |
| c509 | Sửa còn: Bác sĩ nói "đấy là cái cơ chế làm trắng da là như vậy". |
| c541 | Giữ câu, nhãn "Ghi chú của người tóm tắt (không phải nội dung chương trình)". |
| o19–o22 | Thêm hai đoạn dưới nhãn "Khán giả tự kể" (o19 ở mục 01:24:59; o20–o22 ở mục 01:26:58), không trình bày như chẩn đoán/nhân quả/lời khuyên. |
| c377 | Giữ "Nhật Bản" kèm nhãn "xác nhận của người duyệt; phiên âm không chứa"; khôi phục "nhiều quốc gia phát triển", "thường được mở rộng". |
| c201 | "trên dưới 2.000 UI". Nhãn hai số 5.600 và 6.000–7.000: "xác nhận của người duyệt; phiên âm chỉ ghi \"5 600\" và \"6 7000\"" (phiên âm có chứa chuỗi gần đúng nên không dùng nguyên văn "không chứa"). "Trên dưới 2000" thực ra có trong phiên âm (02:49:17). |
| c471, c473 | Giữ câu gốc, thêm câu ghi chú: GSSG/NADPH là xác nhận của người duyệt; phiên âm ghi "GSGS", "NA DPH"/"NADH". |
| c401 | Sửa theo hướng nhịp thở "1 1,5", kéo dài thì thở ra, không nín thở (nhất quán với c402). Ghi rõ phiên âm ghi "thì sau ra". |
| c070, c250, c488 | Áp dụng câu đề xuất đã được đồng ý. |
| c111 | Giữ nguyên. |
| Thức → ngủ | Đã gộp vào c156, không đếm lại. |
| Vitamin D giai đoạn đầu | Thêm ba câu ở mục 01:33:05; không đoán "200.000đ". |
| Thư người khủng hoảng tâm lý | Thêm một câu ở mục 04:19:29, ghi là lời bác sĩ thuật lại. |

Ghi chú: bốn nhóm cuối (c401, c070/c250/c488, vitamin D, thư) nằm ngoài danh sách tối thiểu trong ticket; được áp dụng theo lựa chọn của chủ sở hữu "áp dụng tất cả quyết định đã ghi".

## 4. 63 mục non-supported

followed 17: c013, c070, c111, c125, c135, c156, c166, c201, c250, c275, c377, c401, c456, c471, c488, c509, c541.

**Chưa quyết: 46 mục** (giữ câu cũ, không áp dụng): c034, c045, c054, c066, c068, c079, c084, c103, c105, c108, c121, c127, c140, c144, c161, c162, c172, c176, c177, c182, c193, c208, c210, c211, c235, c245, c248, c251, c252, c254, c256, c282, c287, c291, c294, c319, c333, c352, c373, c407, c447, c449, c478, c500, c529, c549.

Lệch số: bạn nêu 48. Tôi đếm 46: 63 − 17 mục đã có quyết định, trong đó 3 (c013, c156, c275) trùng với 15 thay thế và c125/c135/c166 là quyết định "giữ câu cũ". Con số 48 ≈ 63 − 15 không khớp vì chỉ 3 trong 15 mục thuộc 63. c473, c402, c278, c279 không thuộc 63.

| Mục chưa quyết | Lớp | Câu cũ (giữ) |
|---|---|---|
| c034 | attribution_qualification | Chất béo chuyển hóa được mô tả là chất béo bị đốt cháy quá mức, ví dụ đồ chiên rán, hoặc dầu thực vật bị dùng … |
| c045 | attribution_qualification | Theo bài, H₂O₂ được cho vào vết thương để phá hủy mô hoại tử, virus và vi khuẩn, làm sạch vết thương, và sủi b… |
| c054 | mismatch | Ozon không cướp trực tiếp như các gốc khác, mà xen vào các phân tử oxy khác, tạo thành cuộc "tình tay ba", và … |
| c066 | attribution_qualification | Bác sĩ ví màng tế bào như một bãi xăng, nên một gốc tự do cũng đủ làm sụp đổ hệ thống. |
| c068 | attribution_qualification | Bác sĩ nói hậu quả có thể là bệnh mãn tính, lão hóa và nhiều bệnh khác. |
| c079 | attribution_qualification | Đột biến gen có thể gây bệnh hiếm và ung thư. |
| c084 | attribution_qualification | Bác sĩ nói nếu chỉ đọc tài liệu thông thường thì khó hiểu, nhưng cách phân tích này giúp dễ nhớ hơn. |
| c103 | attribution_qualification | Bác sĩ nói glutathion đang được quảng cáo là chất chống oxy hóa giúp trắng da và nhiều người mua về bổ sung. |
| c105 | attribution_qualification | Bác sĩ cũng nói nếu cơ thể cạn kiệt glutathion thì có thể sinh ra nhiều bệnh mãn tính, một số bệnh ung thư và … |
| c108 | mismatch | Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào cho thấy vi chất làm giảm đường huyết. |
| c121 | attribution_qualification | Họ cũng kể đau đầu và buồn nôn khi có chu kỳ đã hết sau nhiều tháng. |
| c127 | mismatch | Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ sắt II fumarat khô cùng 250 m… |
| c140 | attribution_qualification | Người xem kể sau khi mệt là uống đường mía thô, và dùng lâu dài thì có khó thở, nhịp tim tăng 170 nhịp mỗi phú… |
| c144 | attribution_qualification | Họ kể vẫn còn nhịp tim nhanh và thỉnh thoảng bị bóng đè khi ngủ. |
| c161 | attribution_qualification | Khi xảy ra, hít một hơi thật sâu rồi thở ra từ khoảng 15 đến 30 giây, sau đó lấy lại bình tĩnh thì sẽ thoát kh… |
| c162 | attribution_qualification | Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, tác dụng chủ yếu là trấn an tâm lý, … |
| c172 | attribution_qualification | Bác sĩ nói những người bị táo bón, hội chứng ruột kích thích, viêm dạ dày ruột không tiết được serotonin, nên … |
| c176 | mismatch | Kẽm là yếu tố hợp đồng với glutathione: nếu thiếu kẽm thì glutathione không có giá trị, vì selen là enzyme chu… |
| c177 | attribution_qualification | Theo bác sĩ, bổ sung đủ các chất này giúp ngủ ngon và tế bào não hoạt động bình thường. |
| c182 | attribution_qualification | Bác sĩ nói bóng đè là biểu hiện tổn thương ở mức tế bào, phân tử do lối sống, tâm sinh lý, ăn uống và môi trườ… |
| c193 | attribution_qualification | Người khỏe mạnh, không có bệnh nền, không có mỡ máu, tiểu đường hay huyết áp cao thì bổ sung liều cao lên nồng… |
| c208 | attribution_qualification | Bác sĩ nói trí tuệ không phải do trời cho mà đến từ sự cần cù, chịu khó và quyết tâm. |
| c210 | attribution_qualification | Học sinh cũng lười nhai và thường chỉ muốn ăn nhanh, hấp thu năng lượng nhanh, dẫn đến calo rỗng. |
| c211 | attribution_qualification | Bác sĩ nói việc này có thể khiến các em thất bại, nên phải thay đổi thói quen ăn uống từ hàng ngày. |
| c235 | attribution_qualification | Ông nói từng bước đan xen kiến thức, và tin rằng người làm như vậy sẽ thành công, không phải người gặp khó khă… |
| c245 | attribution_qualification | Bác Thủy ở Đức kể sau khi bổ sung vi chất, mọi người xung quanh ốm nhưng bác không sao. |
| c248 | attribution_qualification | Thầy Nguyễn Hiền, giáo viên vật lý, đau cột sống và đau xương hông, nghi có thể là ung thư xương, uống đủ loại… |
| c251 | attribution_qualification | Ông kể một bệnh nhân đau vùng háng, chụp thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải khoan giảm áp và… |
| c252 | attribution_qualification | Bệnh nhân này đang hút thuốc, khi chỉ dừng hút thuốc lá thì cơn đau đã giảm đi nhiều. |
| c254 | attribution_qualification | Chị Ngọc Thơ, theo bình luận được đọc trên chương trình, từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt, … |
| c256 | attribution_qualification | Người dẫn chương trình đặt nghi vấn chị đang bị thiếu máu nhược sắc do thiếu sắt, gây tan hồng cầu và vàng da. |
| c282 | attribution_qualification | Ông cho rằng đau có thể do gốc tự do tấn công thần kinh và cần tìm hướng khác. |
| c287 | attribution_qualification | Theo bác sĩ, một số bệnh nhân đến bổ sung vi chất đúng và đủ thì cơn đau biến mất hẳn, có người đỡ 90 đến 95%,… |
| c291 | mismatch | Chị ăn nhiều đồng để quên cơn đau nên cân nặng tăng nhanh. |
| c294 | attribution_qualification | Bác sĩ hướng dẫn trong vài tiếng đồng hồ, và sau đó chị bổ sung vi chất theo từng bước, nâng dần liều. |
| c319 | attribution_qualification | Số lượng hồng cầu có thể chưa thấp đến mức thiếu máu cấp, nhưng cơ thể có thể đang thiếu máu chức năng và đói … |
| c333 | attribution_qualification | Gan và thận thiếu vi chất nên giảm khả năng đào thải, và tinh thể urat có thể lắng đọng ở khớp và thành mạch, … |
| c352 | mismatch | Phần nhận xét nói kết hợp kho sắt đóng và lượng sắt lưu hành giảm không gây nguy hiểm đến tính mạng, nhưng làm… |
| c373 | attribution_qualification | Transcript cho rằng những thiếu hụt này xuất hiện sau nhiều thập kỷ hút thuốc lá và thiếu vi chất. |
| c407 | mismatch | Bác sĩ nói đầu tiên là magie, rồi kẽm, canxi, vitamin D3, vitamin tổng hợp (đặc biệt nhóm B), vitamin C và cuố… |
| c447 | attribution_qualification | Ông cũng nhắc rằng ngoài bảy nhóm vi chất còn có khoảng 18 sản phẩm thuộc các nhóm này, cùng các thành phần kh… |
| c449 | attribution_qualification | Bác sĩ nói những lời truyền miệng này "hào nhoáng" và cần nhìn lại dưới góc nhìn y khoa. |
| c478 | mismatch | Bác sĩ nêu ba nguồn chính. |
| c500 | attribution_qualification | Ti thể có ADN riêng nằm sát màng trong, nên gốc tự do thấm qua có thể phá hủy ADN này và gây đột biến. |
| c529 | attribution_qualification | Bác sĩ cho rằng đường tiêm "quá nguy hiểm", có thể gây sốc và ngộ độc. |
| c549 | attribution_qualification | Bác sĩ nói glutathione đang bán rất đắt và là sản phẩm "hot" trên thị trường. |

## 5. Ánh xạ claim (phương pháp extract_claims của audit)

- Lịch sử 554 claim, bản mới 565. Thay thế/sửa: 26 claim; thêm: 9; xoá: c456.
- Tách: c070 → 3 claim, c544 → 2 claim. Gộp: không. Cặp thay thế 2→2: c278+c279, c401+c402.
- Thêm (claim mới, chưa có record audit): c136 (Khán giả tự kể: người xem cho các con ở tuổi vị thành niên u…), c137 (Đây là lời tự kể của khán giả, không phải lời khuyên của bác…), c144 (Khán giả tự kể (không phải chẩn đoán, không phải quan hệ nhâ…), c198 (Ông nói thêm rằng nếu người ta chưa có kiến thức mà bị bắt n…), c199 (Bản ghi nêu tiếp: "Chính vì như vậy" mà ở giai đoạn đầu, tro…), c200 (Khi đã có kiến thức, theo ông, xu hướng là bổ sung vitamin l…), c468 (Bác sĩ thuật lại (lời bác sĩ kể, không phải ca đã được kiểm …), c480 (Ghi chú: GSSG là xác nhận của người duyệt; phiên âm không ch…), c483 (Ghi chú: NADPH là xác nhận của người duyệt; phiên âm không c…).
- Id claim dịch chuyển sau chỗ thêm/xoá; record audit không bị sửa. Muốn bản này có record riêng cần chạy audit mới (ngoài phạm vi).

## 6. Hash trước/sau

Chụp sha256 của toàn bộ 575 file (tracked + untracked) trước và sau: **không file nào có sẵn bị đổi**; `git diff` của file tracked giống hệt trước; `git status` chỉ thêm 2 mục untracked mới (`regenerated/`, plan file). Không commit, stage, stash. `final_records.json`, `claims.json`, `raw/`, `proposed-corrections.json` (63 mục, pending-human-approval), `additional-corrections.json`, `videos/`, `scripts/`, tests: byte-identical. HEAD vẫn f7980cf.

Hash 6 đầu vào sau chạy: xem `provenance.json` (đều khớp).

## 7. Validator và review gate

- `validate_summaries.py --videos-dir audit/V-Qfwjo28Zg`: `regenerated: summarized (tags outside vocabulary: gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu thiếu sắt, lối sống lành mạnh)`, exit 1. Đây là lỗi kế thừa từ header lịch sử; sửa tag hoặc duyệt vocabulary là quyết định của chủ sở hữu, không vá ở đây.
- Với vocabulary chẩn đoán (/tmp, không đưa vào repo): chỉ còn "no passing review bound to this summary" trước khi chạy review.
- Review gate: `review.md` verdict **fail**, summary_sha256 khớp, 11 chunk, 565 claim, 48 fail, 26 concern, 14 omission (SHA `90c7e4aa…`, chạy lại sau các sửa ở §9), coverage_complete=False.
- Fail nằm ở claim **đổi/thêm trong lần này**: 6: c209 (←c201), c286 (←c278), c385 (←c377), c480 (←mới), c483 (←mới), c551 (←c541).
- Fail ở claim **không thuộc 6 claim đổi/thêm ở trên**: 42 (phần lớn kế thừa từ bản lịch sử; c086, c177, c409, c479, c537 mới xuất hiện ở lần chạy lại, chưa đối chiếu với bản lịch sử): c034, c042, c045, c054, c068, c086, c087, c110, c113, c123, c129, c167, c177, c192, c201, c212, c216, c241, c253, c256, c264, c285, c295, c299, c308, c360, c367, c370, c382, c384, c389, c394, c397, c409, c415, c455, c457, c479, c484, c488, c510, c537.
- 5/6 fail ở claim đổi là nhãn/ghi chú của người duyệt hoặc người tóm tắt (c209, c385, c480, c483, c551), không có trong phiên âm nên reviewer không tìm được bằng chứng. c286 (←c278) là câu ghép hai lời ở hai thời điểm (01:11:52 và 02:14:12), reviewer đánh fail; cần chủ sở hữu đọc `review.md` để quyết định. Tôi không sửa summary theo review.

## 8. Điều cần chú ý khi duyệt

- Tiêu đề mục trong bản lịch sử có thời gian lệch so với phiên âm ở nhiều chỗ (ví dụ mục "[01:33:05] Vitamin D" nội dung ở ~02:45 trong phiên âm). Là lỗi của bản lịch sử, không sửa vì ngoài phạm vi.
- Không có tiêu chí nào đặt trạng thái done. Ticket 2.2 giữ ở review. Việc đổi trạng thái JSON, chuyển vào videos/, refresh review.md thuộc ticket sau.

## 9. Cập nhật sau triage (owner chấp thuận)

- summary.md sửa 3 chỗ nhỏ (ghi chú nhịn được/nín thở ở [03:36:48]; ghi chú NADPH; bỏ chữ "nồng độ" ở vitamin D). SHA-256 mới ở đầu báo cáo (`90c7e4aa6f160052663fe934b1c8c3867c79a05267580650be4f4d1a72cb1fec`).
- Review gate đã chạy lại trên SHA mới (codex gpt-6.1-sol, `--no-commit`, trên bản sao /tmp để chỉ duyệt thư mục này); `review.md` và `provenance.json` đã cập nhật theo SHA `90c7e4aa…`. Số liệu §7 là của bản trước; bản mới: verdict **fail**, 565 claim, 48 fail, 26 concern, 14 omission, coverage_complete=False. Tập claim fail lệch nhẹ do reviewer không tất định: thêm c086, c177, c409, c479, c537; hết c187, c418, c425, c453. c209, c385, c480, c483, c551, c286 vẫn fail như trước (c483 vẫn fail dù đã sửa ghi chú NADPH).
- Tiêu chí 3 vẫn không đạt (8 tag ngoài vocabulary, review fail 47/565, c286): chuyển ticket riêng. Heading thời gian lệch (vitamin D, thư khủng hoảng): ticket riêng. c156 không thêm "tim đập nhanh"; c013 giữ nguyên văn đã duyệt (lặp "có thể nói rằng" là có chủ đích).
