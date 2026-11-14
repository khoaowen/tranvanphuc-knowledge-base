# Claim map, V-Qfwjo28Zg: run-6 input to applied summary (ticket 7, criterion 4)

Read-only audit. V-Qfwjo28Zg stays blocked, `publishable` false. No gate run on the applied file.

## 1. Inputs and method

| Item | Value |
|---|---|
| Run-6 input | `regenerated-2.6/summary-run6-input.md`, SHA-256 `5bdca9fc7fcdfc29b95de7f7bf7227e24a6fb398b6a0cf8a6072ec627fd561a0` |
| Applied file | `videos/2026-10-10-so-135-…-phan-tu/summary.md`, SHA-256 `8c910a25a0edc763e885db855c5d930fe4955ed061129dffcd46112366660979` (byte-identical to `regenerated-2.6/summary.md`) |
| Run-6 records | `regenerated-2.6/gate-run6/work/V-Qfwjo28Zg/review.md` (`claims[]`, 582 records, verdict `fail`; its `summary_sha256` equals the run-6 input hash) |
| Extractor | `scripts/fidelity.extract_claims`, same function as the gate, run on both files |
| Alignment | `difflib.SequenceMatcher` over (section, claim text) sequences, then an explicit position-by-position check of claim text, section, question and section window against the run-6 record |

Checks done first: run-6 records equal the claims extracted from the run-6 input (ID, text, section) for all 582; line diff of the two files shows only lines 280 and 435 differ (841 lines each).

## 2. Counts

| | Count |
|---|---|
| Claims in run-6 input / run-6 records | 582 / 582 |
| Claims in applied file | 583 |
| Mapped one-to-one (final claim to one run-6 record, and back) | 582 |
| Run-6 records with no final claim | 0 |
| Final claims with no run-6 record | 1 (the added sentence) |
| **583 = 582 + 1** | holds |
| Same ID, same text | 190 (c001–c190) |
| ID shift +1, same text | 391 (c192–c583 except c313) |
| Text changed | 1 |
| Added | 1 |
| Removed / split / merged | 0 / 0 / 0 |

## 3. Differences

| # | Type | Run-6 ID | Final ID | Location | Detail |
|---|---|---|---|---|---|
| 1 | ADDED | none | c191 | line 280, section `[01:47:01]`, after run-6 c190 | New sentence (the 01:50:49 sentence), appended to the existing paragraph: "Bác sĩ liên hệ rối loạn nhịp tim như block nhĩ thất và ngoại tâm thu với cảm giác giật mình, bóng đè." |
| 2 | TEXT CHANGED | c312 | c313 | line 435, section `[02:44:45]` | "5.600 UI" became "500 đến 600 UI". Old: "Có người chỉ cần khoảng 5.600 UI, có người lên tới 6.000 đến 7.000 UI (hai con số này là xác nhận của người duyệt; phiên âm chỉ ghi "5 600" và "6 7000"), nhưng đại đa số mọi người là con số trên dưới 2.000 UI." New: "Có người chỉ cần khoảng 500 đến 600 UI, có người lên tới 6.000 đến 7.000 UI (hai con số này là xác nhận của người duyệt; phiên âm chỉ ghi "5 600" và "6 7000"), nhưng đại đa số mọi người là con số trên dưới 2.000 UI." |
| 3 | ID SHIFT +1 | c191–c582 | c192–c583 | line 280 onward | 392 records shift by +1: 391 with identical text, plus the changed c312→c313 (row 2) |

Shift check: final ID = run-6 ID + 1 for every run-6 ID from c191 to c582; IDs c001–c190 are unchanged. Final c312 is run-6 c311 (text identical), not run-6 c312.

Unexplained differences: **0**. No split, merge, removal, reorder, section change, question change or section-window change.

## 4. Not gate-verified

| Final ID | Run-6 ID | Why |
|---|---|---|
| c191 | none | Added after run 6. No gate record exists. Final-record section 6 has only a second-reader check (speaker is the doctor, "Tôi đã nghe cái tiếng tim đó"). |
| c313 | c312 | Text changed after run 6. The run-6 record is status `fail` for the old text and does not cover the new text. Owner accepted it as it stands. |

## 5. The 10 accepted claims (run-6 status `fail`, owner-accepted, text unchanged)

| Run-6 ID | Final ID | Text identical | Run-6 status |
|---|---|---|---|
| c113 | c113 | yes | fail |
| c221 | c222 | yes | fail |
| c232 | c233 | yes | fail |
| c381 | c382 | yes | fail |
| c468 | c469 | yes | fail |
| c488 | c489 | yes | fail |
| c491 | c492 | yes | fail |
| c527 | c528 | yes | fail |
| c528 | c529 | yes | fail |
| c567 | c568 | yes | fail |

Run 6 had 11 `fail` records: these 10 plus c312 (section 4). Accepting them does not change the gate verdict (fail).

## 6. Verdict for criterion 4

**PASS.** 583 = 582 + 1; every run-6 record maps to exactly one final claim and back; the differences are the added sentence, the c312 text change and the +1 ID shift; 0 unexplained. c313 and c191 are marked not gate-verified; this map does not make the file gate-verified.

## Appendix: full one-to-one map (583 rows)

| Final ID | Run-6 ID | Run-6 status | Change | Final claim text (first 80 chars) |
|---|---|---|---|---|
| c001 | c001 | pass | same | Glutathion được mô tả là một "lá chắn" tự nhiên của cơ thể, được gọi là "vua của |
| c002 | c002 | pass | same | Bài nói về cuộc chiến giữa oxy hóa và khử ở cấp độ vi mô, trong đó các gốc tự do |
| c003 | c003 | pass | same | Glutathion được xem là chất chống lại gốc tự do quan trọng nhất. |
| c004 | c004 | pass | same | Chương trình có hai phần: (1) cơ chế sinh học của glutathion, và (2) cách bổ sun |
| c005 | c005 | pass | same | Chủ đề có tên "Glutathion cân bằng oxy hóa khử, phục hồi ti thể và bảo vệ tế bào |
| c006 | c006 | pass | same | Theo lời khánh lành, video chỉ được phát duy nhất trên kênh YouTube bác sĩ Trần  |
| c007 | c007 | pass | same | Bác sĩ Trần Văn Phúc chỉ có một fanpage chính thức và một trang Facebook cá nhân |
| c008 | c008 | pass | same | Ekip khẳng định không quảng cáo, không bảo trợ cho sản phẩm y tế, nhãn hàng hay  |
| c009 | c009 | pass | same | Bác sĩ ví von: quả chín, lá chuyển từ xanh sang vàng rồi đỏ và rụng là các hiện  |
| c010 | c010 | pass | same | Gốc tự do tấn công tế bào sống và mầm sống, làm cây kiệt quệ, héo úa. |
| c011 | c011 | pass | same | Đây vốn là một cơ chế bảo vệ của thực vật, nhưng nếu sự tấn công "quá đà" thì sẽ |
| c012 | c012 | pass | same | Bác sĩ nói "có thể nói rằng" hầu hết các loại bệnh tật, trong đó có bệnh mãn tín |
| c013 | c013 | pass | same | Bác sĩ nói “có thể nói rằng” hầu hết các loại bệnh tật có con đường đi từ quá tr |
| c014 | c014 | pass | same | Nếu không giải quyết được vấn đề gốc tự do thì có thể phát sinh nhiều bệnh khác  |
| c015 | c015 | pass | same | Glutathion được xếp vào "vua" chống gốc tự do và được nhắc đến như trọng tâm của |
| c016 | c016 | pass | same | Bài nói sẽ đi từ lý thuyết về gốc tự do đến các thành phần chống gốc tự do, và c |
| c017 | c017 | pass | same | Gốc tự do có hai nguồn chính. |
| c018 | c018 | pass | same | Thứ nhất là con đường nội sinh, tức là sinh ra từ bên trong cơ thể. |
| c019 | c019 | pass | same | Thứ hai là con đường ngoại nhập, tức là từ bên ngoài đưa vào cơ thể, gồm những c |
| c020 | c020 | pass | same | Ti thể được mô tả là "nhà máy điện" và "lò phản ứng" của tế bào, nơi diễn ra chu |
| c021 | c021 | pass | same | Quá trình đốt cháy này luôn sinh ra các yếu tố nguy hiểm gọi là gốc tự do (ROS). |
| c022 | c022 | pass | same | Phần lớn gốc tự do được sinh ra trong ti thể. |
| c023 | c023 | pass | same | Các bào quan khác như lưới nội chất và thể Golgi cũng tạo ra gốc tự do, nhưng lư |
| c024 | c024 | pass | same | Lý do là các cơ chất để tạo ATP gồm đường, mỡ và đạm; khi đốt cháy với oxy thì n |
| c025 | c025 | pass | same | Hệ miễn dịch cũng là một con đường nội sinh sinh ra gốc tự do. |
| c026 | c026 | pass | same | Tế bào lympho T, lympho B và tế bào NK khi phát hiện vi khuẩn, virus hay tác nhâ |
| c027 | c027 | pass | same | Tuy nhiên, nếu vũ khí này dùng sai cách thì có thể quay lại phá hủy chính tế bào |
| c028 | c028 | pass | same | Cuộc chiến của tế bào miễn dịch với vi khuẩn, virus cũng tạo thêm gốc tự do. |
| c029 | c029 | pass | same | Như vậy, cơ thể có hai con đường nội sinh: chuyển hóa và phản ứng trong cơ thể,  |
| c030 | c030 | pass | same | Thuốc lá được nêu là nguồn sinh ra rất nhiều gốc tự do. |
| c031 | c031 | pass | same | Bác sĩ nêu một thống kê: mỗi điếu thuốc lá rút ngắn tuổi thọ 11 phút. |
| c032 | c032 | pass | same | Rượu bia cũng được nhắc đến như một tác nhân ngoại nhập. |
| c033 | c033 | pass | same | Các nguyên nhân được nêu gồm: hóa chất và thuốc trừ sâu trong thực phẩm, chất bả |
| c034 | c034 | pass | same | Chất béo chuyển hóa được bác sĩ mô tả là những chất béo "bị đốt cháy là dở dở đi |
| c035 | c035 | pass | same | Thực phẩm không đảm bảo vệ sinh hay an toàn cũng có thể gây ra hiện tượng này. |
| c036 | c036 | pass | same | Bài nêu ô nhiễm không khí, ô nhiễm nước, ô nhiễm đất và "tất cả những ô nhiễm đề |
| c037 | c037 | pass | same | Ngoài ra còn có tia cực tím UV, tia X quang, tia tử ngoại và nhiều yếu tố vật lý |
| c038 | c038 | pass | same | Superoxit là gốc tự do ban đầu, cơ bản nhất, cần hiểu trước để hiểu các gốc tự d |
| c039 | c039 | pass | same | Ký hiệu của nó là O₂ với một electron dư (điện tích âm). |
| c040 | c040 | pass | same | Oxy có số hiệu 8, khối lượng nguyên tử 16, với 8 electron, và một phân tử O₂ gồm |
| c041 | c041 | pass | same | Khi có thêm một electron lạc, phân tử có 17 electron, ở trạng thái kích thích và |
| c042 | c042 | pass | same | Khi một gốc tự do cướp electron hoặc H+, nó biến phân tử bị cướp thành một gốc t |
| c043 | c043 | pass | same | Gốc mới đó lại đi cướp H+ hoặc electron tiếp, nên tạo thành vòng luẩn quẩn "cướp |
| c044 | c044 | pass | same | Có, H₂O₂ được nêu là một gốc tự do nguy hiểm. |
| c045 | c045 | pass | same | Nó có vẻ bề ngoài yên ổn vì đã cân bằng điện tích, nhưng bên trong là một cặp kh |
| c046 | c046 | pass | same | Theo bài, H₂O₂ được cho vào vết thương; bác sĩ nói nó phá hủy các mô, phá hủy vi |
| c047 | c047 | pass | same | Bài nêu enzyme SOD là thành phần giúp kiểm soát superoxit, buộc các phân tử này  |
| c048 | c048 | pass | same | Gốc hydroxyl là một nhóm OH có một electron lạc. |
| c049 | c049 | pass | same | Nó hình thành khi H₂O₂ bị phá vỡ bởi sắt (Fe²⁺) hoặc đồng (Cu²⁺), tách thành hai |
| c050 | c050 | pass | same | Bài nêu ba lý do: (1) nó ngụy trang, vì có 17 electron nên có H⁺ trung hòa điện, |
| c051 | c051 | pass | same | (2) nó chỉ có một nguyên tử oxy gánh một electron lạc nên rất nặng nề, phải tìm  |
| c052 | c052 | pass | same | (3) kích thước rất nhỏ nên rất cơ động. |
| c053 | c053 | pass | same | Nó tấn công mọi thứ trong cơ thể, đặc biệt cướp electron và H⁺. |
| c054 | c054 | pass | same | Ozon được nêu là "kẻ cướp thứ tư". |
| c055 | c055 | pass | same | Nó hình thành trong không khí khi có tia lửa điện, tiếng sét đánh xuống. |
| c056 | c056 | pass | same | Ozon được mô tả là có thêm một oxy nữa xen vào oxy hai nguyên tử, thành cuộc "tì |
| c057 | c057 | pass | same | Ba gốc tự do đầu tiên (superoxit, H₂O₂, hydroxyl) được nói là tấn công ba thành  |
| c058 | c058 | pass | same | Từ đó, bài nói rằng các gốc này sinh ra bệnh. |
| c059 | c059 | pass | same | Màng tế bào được cấu tạo từ lipid (chất béo màng). |
| c060 | c060 | pass | same | Gốc hydroxyl tấn công màng bằng cách cướp một electron và một H⁺ từ lipid màng,  |
| c061 | c061 | pass | same | Oxy và ozon là các chất xâm nhập vào lipit. |
| c062 | c062 | pass | same | Gốc tự do cướp ngay các phân tử lipit bên cạnh. |
| c063 | c063 | pass | same | Màng tế bào được ví như một bức tường gạch, mỗi phân tử lipit là một viên gạch. |
| c064 | c064 | pass | same | Một gốc tự do làm hỏng viên gạch đầu tiên, viên gạch đó lại đi cướp ở bên cạnh,  |
| c065 | c065 | pass | same | Tế bào hoại tử sinh ra các độc chất, và độc chất này lại tạo thêm gốc tự do. |
| c066 | c066 | pass | same | Bác sĩ thuật lại rằng người ta ví màng tế bào như một bãi xăng, nên chỉ cần một  |
| c067 | c067 | pass | same | Đây được gọi là gốc tự do thứ năm, lipit peroxit. |
| c068 | c068 | pass | same | Bác sĩ nói tế bào hoại tử, tế bào chết đi thì sẽ sinh ra bệnh mãn tính, sẽ bị lã |
| c069 | c069 | pass | same | Gốc tự do OH cướp electron và H+ của protein lành, khiến protein trở thành prote |
| c070 | c070 | pass | same | Protein có dấu chấm bị oxy lợi dụng xâm nhập, hoặc ozon nhường oxy vào, để thành |
| c071 | c071 | pass | same | PO trừ lại cướp H+ để tạo thành POOH. |
| c072 | c072 | pass | same | Bác sĩ nói protein đi theo con đường "y xì như lipit". |
| c073 | c073 | pass | same | Protein bao gồm các thành phần như enzyme, dùng để thực hiện phản ứng hóa học. |
| c074 | c074 | pass | same | Nếu enzyme bị tấn công, các phản ứng hóa học trong cơ thể sẽ ngừng lại, và từ đó |
| c075 | c075 | pass | same | ADN bị tấn công theo hai con đường. |
| c076 | c076 | pass | same | Con đường thứ nhất giống lipit màng: ADN bị cướp electron và H+. |
| c077 | c077 | pass | same | Con đường thứ hai là tấn công trực tiếp mã di truyền A, T, G, C. |
| c078 | c078 | pass | same | Guanin được bác sĩ nói là bị ưu tiên tấn công. |
| c079 | c079 | pass | same | Khi bị tấn công, G tạo ra sản phẩm 8oDG (ghi trong transcript), có đặc điểm gần  |
| c080 | c080 | pass | same | Khi tổng hợp ADN mới, G có thể bị nhầm thành T, dẫn đến đột biến gen. |
| c081 | c081 | pass | same | Đột biến gen có thể gây bệnh hiếm và ung thư. |
| c082 | c082 | pass | same | Bác sĩ nói có bảy gốc tự do cần nhớ, chưa kể các gốc tự do phụ khác. |
| c083 | c083 | pass | same | Gốc tự do là phân tử có xu hướng có một electron độc thân. |
| c084 | c084 | pass | same | Bác sĩ ví nó như đứa con lạc loài xâm nhập vào gia đình hạnh phúc. |
| c085 | c085 | pass | same | Nó khát khao được ổn định nên cướp electron và H+, và trong quá trình đó nó biến |
| c086 | c086 | pass | same | Bác sĩ nói nếu tự đi tìm đọc về gốc tự do thì "chắc chắn" sẽ không thể hiểu được |
| c087 | c087 | pass | same | Bác sĩ mô tả ba bước khi gốc tự do tấn công cơ thể: bước một là đội "cảm tử", bư |
| c088 | c088 | pass | same | Bước một là "lực lượng cảm tử" hy sinh để chống đỡ. |
| c089 | c089 | pass | same | Bước hai là "đội đặc nhiệm" giải quyết gốc tự do. |
| c090 | c090 | pass | same | Bước ba là đội đặc nhiệm phát tín hiệu về ADN để ADN sản xuất thêm đội đặc nhiệm |
| c091 | c091 | pass | same | Lực lượng cảm tử gồm ba thành phần chính: vitamin C, albumin và axit uric. |
| c092 | c092 | pass | same | Chúng xung phong nhường electron hoặc H+ để trung hòa gốc tự do. |
| c093 | c093 | pass | same | Bác sĩ nói axit uric quá nhiều sẽ gây bệnh gút, nhưng nếu vừa đủ thì nó cũng là  |
| c094 | c094 | pass | same | Sau khi đội đặc nhiệm xử lý gốc tự do, cơ thể phát tín hiệu ký hiệu là RnF2 về t |
| c095 | c095 | pass | same | ADN nhận tín hiệu rồi sản xuất thêm đội đặc nhiệm, và các đội này được huấn luyệ |
| c096 | c096 | pass | same | Bác sĩ nêu các thành phần chính. |
| c097 | c097 | pass | same | Catalaz là đội quân tinh nhuệ đứng im, chỉ ra trận khi gốc tự do quá lớn. |
| c098 | c098 | pass | same | Vitamin E tham gia trận đánh trung hòa gốc tự do. |
| c099 | c099 | pass | same | Vitamin C vừa là cảm tử, vừa tham gia trực tiếp, và còn nhường electron cho vita |
| c100 | c100 | pass | same | Licopen được nhắc đến như một thành phần quan trọng sẽ có số phát sóng riêng. |
| c101 | c101 | pass | same | Glutathion được chọn làm chủ đề chính của số hôm nay. |
| c102 | c102 | pass | same | Bác sĩ đối lập glutathion với Catalaz. |
| c103 | c103 | pass | same | Catalaz chỉ đánh những trận lớn và phá bom gốc tự do. |
| c104 | c104 | pass | same | Glutathion là đội quân di động, ở đâu có gốc tự do thì nó đến đó, và được gọi là |
| c105 | c105 | pass | same | Bác sĩ nói người ta quảng cáo rất nhiều về glutathion; người đáp là Khánh Lành n |
| c106 | c106 | pass | same | Số phát sóng sẽ trình bày hai phần: cơ chế tác dụng của glutathion trong từng tì |
| c107 | c107 | pass | same | Bác sĩ cũng nói nếu cơ thể cạn kiệt glutathion thì có thể sinh ra nhiều bệnh mãn |
| c108 | c108 | pass | same | Bác sĩ nói các số sau sẽ nói về vitamin E, vitamin C và licopen, tùy theo ý kiến |
| c109 | c109 | pass | same | Một điều dưỡng khoa phục hồi chức năng ở Hà Nội kể rằng bố chồng bị tiểu đường đ |
| c110 | c110 | pass | same | Điều dưỡng kể chủ nhiệm khoa nói không có cơ chế nào thể hiện “ma dê” (bản ghi â |
| c111 | c111 | pass | same | Trong đoạn này bác sĩ không trả lời về nội dung này. |
| c112 | c112 | pass | same | Một người xem kể từ năm 2024 theo dõi kênh và bổ sung đủ bảy loại vi chất. |
| c113 | c113 | fail | same | Họ nói đã hết đau cột sống, xương cổ, xương đùi và xương quai xanh, và không còn |
| c114 | c114 | pass | same | Đây là kết quả người xem tự kể. |
| c115 | c115 | pass | same | Một giáo viên ở Tokyo kể đã dùng canxi, magie, vitamin D3, vitamin C và omega 3. |
| c116 | c116 | pass | same | Sau ba tháng, tình trạng ho khi thời tiết thay đổi biến mất, tay chân hết tê và  |
| c117 | c117 | pass | same | Đây là kết quả người xem tự kể. |
| c118 | c118 | pass | same | Một người xem ở Đức kể gần một năm dùng bảy loại vi chất thì miệng không còn hôi |
| c119 | c119 | pass | same | Họ cũng nói không còn đau cổ vai gáy do bưng bê nặng. |
| c120 | c120 | pass | same | Đây là kết quả người xem tự kể. |
| c121 | c121 | pass | same | Một người xem 50 tuổi kể từng bị đại tràng co thắt gây táo bón, từng phải nhờ th |
| c122 | c122 | pass | same | Sau khi bổ sung canxi, magie, omega 3 và các vi chất khác theo hướng dẫn, họ nói |
| c123 | c123 | pass | same | Họ cũng kể trước đây mỗi khi đến chu kỳ kinh nguyệt bị đau đầu khủng khiếp và bu |
| c124 | c124 | pass | same | Đây là kết quả người xem tự kể. |
| c125 | c125 | pass | same | Khán giả tự kể vẫn mong khỏi nốt viêm xoang và hen phế quản. |
| c126 | c126 | pass | same | Người xem kể từ năm 2017 da vàng bợt, niêm mạc mắt và miệng vàng, hay hụt hơi và |
| c127 | c127 | pass | same | Hemoglobin luôn ở mức 10 đến 11 g/dL, thấp hơn khoảng tham chiếu 12 đến 16. |
| c128 | c128 | pass | same | Họ nghi ngờ thiếu sắt nhược sắc, nhưng chưa rõ chính xác. |
| c129 | c129 | pass | same | Trong đoạn này bác sĩ chưa đưa ra kết luận nào. |
| c130 | c130 | pass | same | Khán giả tự kể từ năm 2012 cơ hàm khó điều khiển, hay đơ cứng và khiến họ nói kh |
| c131 | c131 | pass | same | Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ |
| c132 | c132 | pass | same | Từ ngày 27/05/2026, họ nhịn ăn gián đoạn 168 từ 20 giờ tối đến 12 giờ trưa hôm s |
| c133 | c133 | pass | same | Người xem cũng đã tách dần viên vitamin tổng hợp thành viên lẻ với những loại có |
| c134 | c134 | pass | same | Người xem kể vàng da, vàng niêm mạc và hụt hơi khi nói, đi bộ nhanh, leo cầu tha |
| c135 | c135 | pass | same | Họ ngủ ngon, ít tiểu đêm, và tập thở 4-7-8 trước khi ngủ hiệu quả rõ. |
| c136 | c136 | pass | same | Từ 27/05/2026, họ giảm khoảng 4 kg, từ 56–57 kg xuống còn 52–53 kg, cao 1,6 m. |
| c137 | c137 | pass | same | Đây là kết quả người xem tự báo cáo. |
| c138 | c138 | pass | same | Khán giả tự kể: người xem cho các con ở tuổi vị thành niên uống theo và "nghiên  |
| c139 | c139 | pass | same | Đây là lời tự kể của khán giả, không phải lời khuyên của bác sĩ. |
| c140 | c140 | pass | same | Người xem 41 tuổi ở Đông Anh, Hà Nội, kể bị đau nửa đầu từ 15 tuổi, với khoảng b |
| c141 | c141 | pass | same | Bác sĩ chẩn đoán nang dưới nhện góc tiểu cầu não trái làm dây thần kinh số năm b |
| c142 | c142 | pass | same | Sau khi sinh, họ được chẩn đoán trầm cảm sau sinh. |
| c143 | c143 | pass | same | Sau ba tháng dùng vi chất, họ được bác sĩ Phúc khám trực tiếp vào tháng 5/2026 v |
| c144 | c144 | pass | same | Họ nói đã lấy lại 95% sức khỏe. |
| c145 | c145 | pass | same | Đây là kết quả người xem tự kể. |
| c146 | c146 | pass | same | Khán giả tự kể (không phải chẩn đoán, không phải quan hệ nhân quả đã được xác mi |
| c147 | c147 | pass | same | Người xem kể lúc mệt mỏi đã ăn hoặc uống đường mía thô, rồi lạm dụng; sau 3 thán |
| c148 | c148 | pass | same | Họ cũng kể gần hai năm không có giấc ngủ trọn vẹn, hay bị bóng đè và nhịp tim hẫ |
| c149 | c149 | pass | same | Các bác sĩ chẩn đoán là do trầm cảm. |
| c150 | c150 | pass | same | Khán giả tự kể sau khi cai đường, đi bấm huyệt và uống thuốc nam thì cơ thể đã đ |
| c151 | c151 | pass | same | Người xem đề nghị bác sĩ giải thích chi tiết về bóng đè khi ngủ và cơ chế ảnh hư |
| c152 | c152 | pass | same | Họ kể vẫn còn nhịp tim nhanh và thỉnh thoảng bị bóng đè khi ngủ. |
| c153 | c153 | pass | same | Khán giả tự kể Nguyễn Điểm sau khi bổ sung vi chất thấy đau đầu và đau cổ vai gá |
| c154 | c154 | pass | same | Người xem đang dùng vitamin D 50.000 IU theo hướng dẫn trên tờ hướng dẫn: một vi |
| c155 | c155 | pass | same | Sau 8 tuần, chỉ số vitamin D của họ là 54 ng/mL. |
| c156 | c156 | pass | same | Các thành viên khác trong gia đình đạt từ 59,63 đến 73,69 ng/mL. |
| c157 | c157 | pass | same | Họ đã duy trì một viên mỗi tháng và hỏi về tính an toàn và hợp lý. |
| c158 | c158 | pass | same | Người xem hỏi bác sĩ phân tích việc bổ sung duy trì vitamin D liều 50.000 đơn vị |
| c159 | c159 | pass | same | Bác sĩ nói cả mười bình luận đều rất liên quan tới chủ đề phát sóng hôm nay là g |
| c160 | c160 | pass | same | Bác sĩ nói không thể nói 100% nhưng có thể nói gần 100% người xem đạt kết quả rấ |
| c161 | c161 | pass | same | Bác sĩ nói học tập tốt bắt đầu từ sức khỏe thân thể. |
| c162 | c162 | pass | same | Muốn sức khỏe tốt thì phải ăn uống, ngủ nghỉ đúng khoa học, bổ sung vi chất và c |
| c163 | c163 | pass | same | Bác sĩ nói con người sinh ra không phải ông trời cũng cho tất cả mọi người trí t |
| c164 | c164 | pass | same | Bác sĩ nói ngoài cổng trường có nhiều đồ chiên, rán, nướng, thức ăn nhanh, trà c |
| c165 | c165 | pass | same | Bác sĩ nói các bạn ăn thức ăn nhanh, uống nhiều đồ uống có đường và rơi vào tình |
| c166 | c166 | pass | same | Ông kể hai đứa con của một chị bạn lười nhai, lười mọi thứ và chỉ muốn ăn sẵn, ă |
| c167 | c167 | pass | same | Bác sĩ nói việc này có thể khiến các em thất bại, nên phải thay đổi thói quen ăn |
| c168 | c168 | pass | same | Bác sĩ nói bắt đầu bằng cách dùng nắm tay để ước lượng khẩu phần, sau đó dùng tỉ |
| c169 | c169 | pass | same | Bác sĩ nói ở lứa tuổi học sinh, các bạn sẽ hấp thu chất rất tốt nếu thực hiện ch |
| c170 | c170 | pass | same | Bác sĩ khuyến khích lan tỏa kiến thức và hành vi tốt từ bạn bè tới trường học và |
| c171 | c171 | pass | same | Bác sĩ nói một ngày tối thiểu phải có hơn hai tiếng đồng hồ hoạt động ngoài trời |
| c172 | c172 | pass | same | Bác sĩ khuyên nên đi bộ, đi xe đạp hoặc đi xe buýt thay vì luôn được bố mẹ đưa đ |
| c173 | c173 | pass | same | Bác sĩ nói học sinh có thể tính toán số canxi cần mỗi ngày từ thịt, cá, cơm, rau |
| c174 | c174 | pass | same | Từ đó tự xác định lượng canxi còn thiếu và xây dựng khẩu phần ăn của mình. |
| c175 | c175 | pass | same | Bác sĩ nói y học tương lai lấy ăn làm đầu, dùng ăn để phòng bệnh và chữa bệnh. |
| c176 | c176 | pass | same | Bác sĩ cũng nói thuốc có thể được cá thể hóa cho từng người trong tương lai. |
| c177 | c177 | pass | same | Bác sĩ kể mình đọc đến mấy chục nghìn chữ mỗi ngày. |
| c178 | c178 | pass | same | Khi đọc, bác sĩ lướt theo đường chéo để xem tài liệu có quan trọng không, sau đó |
| c179 | c179 | pass | same | Bác sĩ cho rằng viết tay và rèn luyện các giác quan giúp nhớ kiến thức tốt hơn. |
| c180 | c180 | pass | same | Dạy và học có ba kỹ năng tương ứng ba chữ T (tay, tâm, trí) và cần rèn luyện cả  |
| c181 | c181 | pass | same | Mục tiêu tay: sau bài học làm được gì, đến mức độ nào. |
| c182 | c182 | pass | same | Mục tiêu tâm: sau bài học chia sẻ được điều đó với xã hội và các vấn đề đạo đức  |
| c183 | c183 | pass | same | Mục tiêu trí: sau bài học rút ra kiến thức gì quan trọng cho bản thân. |
| c184 | c184 | pass | same | Theo bác sĩ, viết bằng tay khi đọc tài liệu giúp tín hiệu từ bàn tay lên não và  |
| c185 | c185 | pass | same | Bác sĩ nói kiến thức sẽ bị quên sau một thời gian nên phải được lặp lại thường x |
| c186 | c186 | pass | same | Ông nói không có con đường tắt; cách đi là sống lành mạnh dựa trên kiến thức về  |
| c187 | c187 | pass | same | Bài hôm nay nói về glutathion, chất chống oxy hóa khử và chống gốc tự do. |
| c188 | c188 | pass | same | Bác sĩ liên tưởng mùa thu, hoa quả chín và lá rụng với gốc tự do trong thực vật, |
| c189 | c189 | pass | same | Ông cũng nói các chiến sĩ trong cách mạng có liên quan đến "cái gì đó giống như  |
| c190 | c190 | pass | same | Bác sĩ nói phải phân tích kiến thức dưới nhiều góc độ, như y khoa, toán học, vật |
| c191 | - | (none) | ADDED | Bác sĩ liên hệ rối loạn nhịp tim như block nhĩ thất và ngoại tâm thu với cảm giá |
| c192 | c191 | pass | id shift +1 | Theo bác sĩ, con đường đúng là sống và thực hành một lối sống lành mạnh, trong s |
| c193 | c192 | pass | id shift +1 | Ông nói từng bước đan xen kiến thức, tin rằng khi chuẩn bị những kỹ năng đó thì  |
| c194 | c193 | pass | id shift +1 | Ông nêu ví dụ điều dưỡng Ngân muốn tư vấn cho bệnh nhân nhưng nếu không cẩn thận |
| c195 | c194 | pass | id shift +1 | Điều này có thể ảnh hưởng đến cả tập thể, nên đôi khi phải thông cảm. |
| c196 | c195 | pass | id shift +1 | Ông nói phải đi từng bước, không thể làm vội. |
| c197 | c196 | pass | id shift +1 | Bác sĩ nói ông không đồng ý với nhận định rằng bác sĩ tốt rất khó tìm, vì đại đa |
| c198 | c197 | pass | id shift +1 | Tuy nhiên không phải ai cũng có điều kiện thể hiện hết, vì còn cơm áo gạo tiền v |
| c199 | c198 | pass | id shift +1 | Ông ví ngành y như chiếc áo choàng trắng: cứu được nhiều người nhưng không ai bi |
| c200 | c199 | pass | id shift +1 | Bác sĩ kể rằng trước Covid, khi vào một lớp học sinh tiểu học ở Nhật Bản, ông th |
| c201 | c200 | pass | id shift +1 | Ở châu Âu, mùa thu đông nhiều người đau xương khớp, chảy nước mũi và nhiễm Coron |
| c202 | c201 | pass | id shift +1 | Sau khi tìm câu trả lời, ông kết luận là thiếu nền tảng vi chất, tế bào bị "bỏ đ |
| c203 | c202 | pass | id shift +1 | Một bác ở Đức (bác sĩ nói "tôi đoán bác tên là Thủy") kể sau khi bổ sung vi chất |
| c204 | c203 | pass | id shift +1 | Cô Thu Trang ở Tokyo trước đây ốm giặt dẹo suốt, đau mỏi, nhưng nay hoàn toàn kh |
| c205 | c204 | pass | id shift +1 | Bác sĩ cũng mô tả người Nhật làm việc từ sáng đến tối, bữa trưa ăn vội, nên nếu  |
| c206 | c205 | pass | id shift +1 | Thầy Nguyễn Hiền, thầy giáo vật lý, đau cột sống, đau xương hông, cảm tưởng mình |
| c207 | c206 | pass | id shift +1 | Bác sĩ nói uống quá nhiều thuốc là một nguyên nhân quan trọng gây gốc tự do. |
| c208 | c207 | pass | id shift +1 | Trong đoạn nói về thuốc giảm đau, bản ghi âm nêu paracetamol "hại tới gan", rồi  |
| c209 | c208 | pass | id shift +1 | Bác sĩ cho rằng dùng nhiều hóa chất và thuốc không cần thiết đều sinh gốc tự do. |
| c210 | c209 | pass | id shift +1 | Bác sĩ nêu ví dụ có những người đau bên phần háng, dần dần đi chụp thì thấy hoại |
| c211 | c210 | pass | id shift +1 | Bác sĩ nói những bệnh nhân ấy, nếu đang hút thuốc lá, chỉ cần một động tác là dừ |
| c212 | c211 | pass | id shift +1 | Bác sĩ cũng nói thuốc lá, rượu bia, chế độ ăn sai và dùng thuốc sai đều gây nhiề |
| c213 | c212 | pass | id shift +1 | Một người xem, theo bình luận được đọc trên chương trình (bác sĩ nói "tôi đoán l |
| c214 | c213 | pass | id shift +1 | Xét nghiệm hemoglobin của chị luôn ở mức 10 đến 11 g/dL, trong khi bình thường l |
| c215 | c214 | pass | id shift +1 | Chị, người viết bình luận, tự cho rằng có lẽ mình thiếu sắt nhược sắc; bác sĩ th |
| c216 | c215 | pass | id shift +1 | Sau khi bổ sung vi chất, theo bác sĩ, tình trạng của chị thay đổi hoàn toàn. |
| c217 | c216 | pass | id shift +1 | Bác sĩ nói đây là thiếu máu vi thể nằm dưới da. |
| c218 | c217 | pass | id shift +1 | Da và mắt tiếp xúc với ánh sáng có tia UV và không khí ô nhiễm có bụi mịn PM2.5  |
| c219 | c218 | pass | id shift +1 | Bác sĩ nói gốc tự do ở da tấn công màng tế bào, protein và ADN; tấn công màng tế |
| c220 | c219 | pass | id shift +1 | Ông cho rằng gốc tự do này còn do thiếu vi chất làm hệ miễn dịch kém đi. |
| c221 | c220 | pass | id shift +1 | Bác sĩ nói rối loạn ở tụy có thể gây tiểu đường. |
| c222 | c221 | fail | id shift +1 | Bố chồng chị Ngân bổ sung vi chất và đường huyết giảm xuống (bác sĩ nói “chồng c |
| c223 | c222 | pass | id shift +1 | Bác sĩ nói nếu chị Ngân mang điều đó đến trưởng khoa để thuyết phục thì trưởng k |
| c224 | c223 | pass | id shift +1 | Theo phản ánh của bệnh nhân trên kênh, một số người giảm được liều thuốc hoặc bỏ |
| c225 | c224 | pass | id shift +1 | Bác sĩ nói gốc tự do tấn công gan, và khi xét nghiệm chức năng gan và thận bất t |
| c226 | c225 | pass | id shift +1 | Tế bào gan có thể vẫn bù trừ để men gan bình thường, nhưng một số chức năng đã n |
| c227 | c226 | pass | id shift +1 | Phần chuyển caroten thành vitamin A không còn làm được việc, nên ăn bao nhiêu ca |
| c228 | c227 | pass | id shift +1 | Khi thiếu vitamin A, mắt có thể rỉ ghèn, nhìn mờ. |
| c229 | c228 | pass | id shift +1 | Ông nói gốc tự do còn làm hỏng enzyme vì tấn công protein, và bổ sung vi chất có |
| c230 | c229 | pass | id shift +1 | Bác sĩ nhắc lại: “Vitamin C cũng là gốc tự do, vitamin E cũng là gốc tự do”; sau |
| c231 | c230 | pass | id shift +1 | Bác sĩ xác nhận các chất này hiệp đồng với nhau. |
| c232 | c231 | pass | id shift +1 | Người dẫn đọc bình luận của một điều dưỡng về bố chồng bị tiểu đường, đường huyế |
| c233 | c232 | fail | id shift +1 | Bác sĩ nói “chồng chị Ngân” sau khi uống thì đường huyết giảm trở lại bình thườn |
| c234 | c233 | pass | id shift +1 | Bác sĩ kể chị Nhung 41 tuổi bị đau dây thần kinh số 5 và khi chụp thấy một nang  |
| c235 | c234 | pass | id shift +1 | Bác sĩ, là người đọc nhiều phim CT và cộng hưởng từ, nói nang dưới nhện không ph |
| c236 | c235 | pass | id shift +1 | Ông không đồng ý với việc mổ dẫn lưu vì bệnh nhân sẽ thêm một vết mổ không cần t |
| c237 | c236 | pass | id shift +1 | Ông cho rằng đau có thể do gốc tự do tấn công thần kinh và cần tìm hướng khác. |
| c238 | c237 | pass | id shift +1 | Bác sĩ mô tả nang dưới nhện là chỗ tăng tích dịch tại khe rãnh cuộn não. |
| c239 | c238 | pass | id shift +1 | Bác sĩ nói dây thần kinh số 5 có ba nhánh: nhánh mắt, nhánh hàm trên và nhánh hà |
| c240 | c239 | pass | id shift +1 | Bác sĩ nói trên thế giới thường chọc kim vào hạch ở lỗ bầu dục để bơm hóa chất d |
| c241 | c240 | pass | id shift +1 | Nhóm của ông làm khác: chỉ chạm kim vào vỏ bao, không chạm vào hạch, rồi bơm hóa |
| c242 | c241 | pass | id shift +1 | Nếu tái phát thì tiêm tiếp, nhưng kết quả không quá tốt. |
| c243 | c242 | pass | id shift +1 | Bác sĩ nói khi tổn thương dây thần kinh số 5 bị viêm thì hầu hết bệnh nhân đều n |
| c244 | c243 | pass | id shift +1 | Bác sĩ nói một cơn gió nhẹ, đánh răng hay một nụ cười có thể khởi phát cơn đau d |
| c245 | c244 | pass | id shift +1 | Theo bác sĩ, sau khi những bệnh nhân đến bổ sung vi chất đúng và đủ thì có những |
| c246 | c245 | pass | id shift +1 | Ông cho rằng nguyên nhân vẫn là gốc tự do tấn công dây thần kinh số 5, và nếu hi |
| c247 | c246 | pass | id shift +1 | Chị Nhung 41 tuổi bị đau nửa đầu từ năm 15 tuổi, sinh ba con và bị gắn nhãn trầm |
| c248 | c247 | pass | id shift +1 | Mỗi cơn kéo dài 3 đến 5 ngày, một tháng có vài cơn, phải nằm co ro, tránh ánh sá |
| c249 | c248 | pass | id shift +1 | Chị ăn đường vào để quên cơn đau nên cân nặng tăng nhanh. |
| c250 | c249 | pass | id shift +1 | Uống đủ thuốc không đỡ, nhưng sau khi bổ sung vi chất, theo bác sĩ, chị thay đổi |
| c251 | c250 | pass | id shift +1 | Trước đây nhịp tim của chị lên tới 170. |
| c252 | c251 | pass | id shift +1 | Bác sĩ nói có người viêm đĩa đệm, có người thoát vị đĩa đệm rách bao sợi, và ngu |
| c253 | c252 | pass | id shift +1 | Ông cho rằng nhiều người mổ xong còn đau hơn, và các biện pháp như tiêm phong bế |
| c254 | c253 | pass | id shift +1 | Ông nói phải phòng ngay từ khi đừng để tình trạng ấy xảy ra, và muốn vậy thì phả |
| c255 | c254 | pass | id shift +1 | Bài hôm nay không đủ thời gian để giải thích sâu, nhưng cơ chế cơ bản theo bác s |
| c256 | c255 | pass | id shift +1 | Khi chuyển từ thức sang ngủ, cơ thể làm liệt vận động để khi mơ không đấm đá, nó |
| c257 | c256 | pass | id shift +1 | Nếu tỉnh mà tay chân bị khóa và miệng bị dán chặt thì sẽ rất khó chịu, đó là ngu |
| c258 | c257 | pass | id shift +1 | Bác sĩ nói giai đoạn đầu của giấc ngủ là ngủ mơ, y khoa gọi là REM, khi có nhiều |
| c259 | c258 | pass | id shift +1 | Nếu trong mơ người ta đánh nhau hoặc nói chuyện mà chân tay vận động theo thì sẽ |
| c260 | c259 | pass | id shift +1 | Vì vậy cơ thể phải ức chế vận động và cơ nói khi ngủ. |
| c261 | c260 | pass | id shift +1 | Ông ví não như người lái xe, tay chân và lời nói như bánh xe, còn liệt vận động  |
| c262 | c261 | pass | id shift +1 | Bác sĩ nói não dùng hai chất trung gian hóa học. |
| c263 | c262 | pass | id shift +1 | Chất thứ nhất được bản ghi ghi là "G3", đã được nhắc ở số trước, là một chất liê |
| c264 | c263 | pass | id shift +1 | Chất thứ hai là glycin, một thành phần tạo nên glutathion. |
| c265 | c264 | pass | id shift +1 | Hai chất này làm liệt cơ, khiến người ngủ không cử động, không vận động và không |
| c266 | c265 | pass | id shift +1 | Bản ghi âm ghi là “K G3” và “glycerin” cho cơ chế này; khi chuyển từ thức vào ng |
| c267 | c266 | pass | id shift +1 | Nếu chuyển từ ngủ sang thức mà phanh chưa nhả, não đã tỉnh và nhận biết được mọi |
| c268 | c267 | pass | id shift +1 | Ở chiều từ ngủ sang thức, bác sĩ nói hạch hạnh nhân báo động; người đó giãy giụa |
| c269 | c268 | pass | id shift +1 | Bác sĩ ví não như người lái xe, tay chân và lời nói như bánh xe, còn liệt vận độ |
| c270 | c269 | pass | id shift +1 | Bác sĩ nói hầu hết tài liệu khoa học cho rằng đây là hiện tượng không đáng ngại. |
| c271 | c270 | pass | id shift +1 | Bác sĩ nói hầu hết tài liệu khoa học khuyên khi xảy ra thì hít một hơi thật sâu, |
| c272 | c271 | pass | id shift +1 | Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, về mặt |
| c273 | c272 | pass | id shift +1 | Bác sĩ nói não chiếm khoảng 2% trọng lượng cơ thể nhưng dùng khoảng 20% năng lượ |
| c274 | c273 | pass | id shift +1 | Căng thẳng kéo dài làm não bị ức chế và tiêu tốn nhiều năng lượng, sinh thêm nhi |
| c275 | c274 | pass | id shift +1 | Người căng thẳng kéo dài dễ ngủ không yên, gặp ác mộng và bóng đè, và bác sĩ nói |
| c276 | c275 | pass | id shift +1 | Lời khuyên là sống bình thường, làm được gì thì làm, không làm được thì thôi, và |
| c277 | c276 | pass | id shift +1 | Ví dụ bác sĩ nêu việc người bị sốt hôm qua hôm nay đã đòi thuốc, trong khi có th |
| c278 | c277 | pass | id shift +1 | Ăn uống không đúng cách, lối sống sai và tiếp xúc với chất độc hại, tác nhân ngu |
| c279 | c278 | pass | id shift +1 | Để đi vào giấc ngủ REM, não cần tiết acetylcholine; để chuyển từ ngủ sang thức c |
| c280 | c279 | pass | id shift +1 | Theo bác sĩ, khoảng 95% serotonin được tiết ở ruột và khoảng 5% ở não. |
| c281 | c280 | pass | id shift +1 | Bác sĩ nói một số những người bị táo bón, bị hội chứng ruột kích thích, bị dạ dà |
| c282 | c281 | pass | id shift +1 | Bác sĩ cho rằng cần giải quyết tình trạng đường ruột này, và các con đường trên  |
| c283 | c282 | pass | id shift +1 | Bác sĩ nhắc tới catalase, licopen (bản ghi âm ghi là "licoben"), vitamin C, vita |
| c284 | c283 | pass | id shift +1 | Vitamin C, vitamin E, kẽm và selen (bản ghi âm ghi là "cen") là những yếu tố hợp |
| c285 | c284 | pass | id shift +1 | Nếu thiếu kẽm thì glutathione chẳng có giá trị. |
| c286 | c285 | pass | id shift +1 | Selen quá quan trọng trong chuyện là enzyme để chuyển hóa gốc tự do; nếu không c |
| c287 | c286 | pass | id shift +1 | Theo bác sĩ, khi bổ sung các chất này thì sẽ ngủ ngon, ngủ tốt; cùng với thực hà |
| c288 | c287 | pass | id shift +1 | Bác sĩ nói đó là nguyên nhân nhỏ, không phải nguyên nhân chính, vì cơ thể có cơ  |
| c289 | c288 | pass | id shift +1 | Bác sĩ cam kết rằng nếu bổ sung đầy đủ vi chất, thực hành lối sống và ăn uống tố |
| c290 | c289 | pass | id shift +1 | Bác sĩ khuyên sống chậm và thực hành hơi thở thiền định để kích thích sóng alpha |
| c291 | c290 | pass | id shift +1 | Không để sóng gamma và sóng beta tăng quá nhiều. |
| c292 | c291 | pass | id shift +1 | Bác sĩ nói bóng đè là biểu hiện tổn thương ở mức tế bào, phân tử do lối sống, tâ |
| c293 | c292 | pass | id shift +1 | Bác sĩ nói đã hướng dẫn trong bốn đến năm tiếng; sau đó, để bổ sung vi chất, ông |
| c294 | c293 | pass | id shift +1 | Bác sĩ nói hiệu quả thay đổi rõ rệt. |
| c295 | c294 | pass | id shift +1 | Hiện nay thỉnh thoảng vẫn còn nhịp tim tăng nhanh do yếu tố tâm lý. |
| c296 | c295 | pass | id shift +1 | Bác sĩ nói nếu mua được vi chất tốt, đúng và chuẩn thì bổ sung sẽ tốt lên nhiều. |
| c297 | c296 | pass | id shift +1 | Theo bác sĩ: dưới 30 ng/ml là mức "vô gia cư" (cách nói ví của bác sĩ), từ 30 đế |
| c298 | c297 | pass | id shift +1 | Bác sĩ nói cần cẩn thận khi duy trì ở mức trên 90 vì sẽ bị thừa, và thừa thì khô |
| c299 | c298 | pass | id shift +1 | Dược sĩ nước ngoài hướng dẫn bổ sung 50.000 UI mỗi tuần, liên tục 8 tuần thì nồn |
| c300 | c299 | pass | id shift +1 | Sau đó chuyển sang bổ sung một ống theo chu kỳ "trên 1 tháng" (phần ghi lời nói  |
| c301 | c300 | pass | id shift +1 | Bác sĩ nói lời khuyên này đúng, không có gì sai. |
| c302 | c301 | pass | id shift +1 | Ông nói thêm rằng nếu người ta chưa có kiến thức mà bị bắt ngày nào cũng uống vi |
| c303 | c302 | pass | id shift +1 | Bản ghi nêu tiếp: "Chính vì như vậy" mà ở giai đoạn đầu, trong một khoảng thì uố |
| c304 | c303 | pass | id shift +1 | Khi đã có kiến thức, theo ông, xu hướng là bổ sung vitamin liều thấp thay vì liề |
| c305 | c304 | pass | id shift +1 | Người khỏe mạnh, không còn bệnh tật gì khác, không bị nhiều mỡ, mỡ dưới da ít, k |
| c306 | c305 | pass | id shift +1 | Nếu có bệnh nền hoặc tích nhiều mỡ dưới da và mỡ nội tạng, bổ sung liều cao có t |
| c307 | c306 | pass | id shift +1 | Với người có bệnh nền hoặc đã có tuổi, nên giảm dần và bổ sung liều thấp thay ch |
| c308 | c307 | pass | id shift +1 | Uống dồn làm nồng độ lên xuống rõ rệt, đầu tháng cao, cuối tháng thấp. |
| c309 | c308 | pass | id shift +1 | Uống đều hàng ngày giữ nồng độ gần như đường thẳng, và bác sĩ nói cách này tốt h |
| c310 | c309 | pass | id shift +1 | 50.000 UI chia cho 30 ngày xấp xỉ 1.666 UI mỗi ngày. |
| c311 | c310 | pass | id shift +1 | Vitamin D tích lũy trong mỡ khoảng 6 tháng, nên người bận có thể uống dồn, nhưng |
| c312 | c311 | pass | id shift +1 | Theo bác sĩ, nghiên cứu cho thấy nhu cầu thường quanh 2.000 UI mỗi ngày, tùy từn |
| c313 | c312 | fail | TEXT CHANGED | Có người chỉ cần khoảng 500 đến 600 UI, có người lên tới 6.000 đến 7.000 UI (hai |
| c314 | c313 | pass | id shift +1 | Để dò liều, bác sĩ chọn 2.000 UI mỗi ngày, xét nghiệm vài lần để xác định mỗi ng |
| c315 | c314 | pass | id shift +1 | Bác sĩ nhấn mạnh mua vitamin D còn hạn sử dụng và bảo quản tránh ánh sáng, không |
| c316 | c315 | pass | id shift +1 | Bác là thương binh, từng làm nghề mộc, sống ở Hưng Yên. |
| c317 | c316 | pass | id shift +1 | Vợ bác mất đột ngột vì bệnh tim khi bác 37 tuổi, và bác nuôi con một mình. |
| c318 | c317 | pass | id shift +1 | Bác hút thuốc lá nhiều năm như cách giải tỏa. |
| c319 | c318 | pass | id shift +1 | Năm trước bác phải cấp cứu vì đợt cấp bệnh phổi tắc nghẽn mạn tính (COPD). |
| c320 | c319 | pass | id shift +1 | Từ đó thể trạng rất yếu, và bác còn viêm đường ruột dằng dai. |
| c321 | c320 | pass | id shift +1 | Bản tự giới thiệu ghi sinh năm 1973, còn phần nhận xét đọc sau đó ghi sinh năm 1 |
| c322 | c321 | pass | id shift +1 | Bác cao 1,50 m, nặng 42 kg. |
| c323 | c322 | pass | id shift +1 | Số đo vòng ngực 74 cm, vòng eo 55 cm, vòng mông 80 cm, vòng cánh tay 20 cm và vò |
| c324 | c323 | pass | id shift +1 | MPV (thể tích trung bình tiểu cầu) là 6,99, giảm nhẹ so với khoảng tham chiếu 7  |
| c325 | c324 | pass | id shift +1 | MCV (thể tích trung bình hồng cầu) là 98,9, ở cận trên của khoảng 80 đến 100. |
| c326 | c325 | pass | id shift +1 | MCH (lượng huyết sắc tố trung bình hồng cầu) là 33,7, tăng nhẹ so với khoảng 27  |
| c327 | c326 | pass | id shift +1 | Các chỉ số tế bào máu khác trong giới hạn bình thường. |
| c328 | c327 | pass | id shift +1 | AST là 53,7, tăng so với khoảng tham chiếu nhỏ hơn 37, còn ALT trong giới hạn bì |
| c329 | c328 | pass | id shift +1 | Ure máu là 7,4 (đơn vị phiên âm ghi là "m/l"), sát ngưỡng trên của khoảng tham c |
| c330 | c329 | pass | id shift +1 | Creatinin máu trong giới hạn bình thường. |
| c331 | c330 | pass | id shift +1 | Cholesterol toàn phần là 5,4, tăng nhẹ so với mức nhỏ hơn 5,2. |
| c332 | c331 | pass | id shift +1 | LDL-C là 3,1, bình thường. |
| c333 | c332 | pass | id shift +1 | Axit uric là 459,1, tăng so với khoảng 200 đến 420 ở nam. |
| c334 | c333 | pass | id shift +1 | Glucose máu và HbA1c trong giới hạn bình thường. |
| c335 | c334 | pass | id shift +1 | Tổng phân tích nước tiểu có pH 5,5, bình thường, các chỉ số khác âm tính hoặc tr |
| c336 | c335 | pass | id shift +1 | Feritin là 428,1, tăng so với khoảng 30 đến 400 ở nam. |
| c337 | c336 | pass | id shift +1 | Transferrin là 178, giảm so với 200 đến 360. |
| c338 | c337 | pass | id shift +1 | TIBC là 44,72, giảm nhẹ so với 45 đến 70. |
| c339 | c338 | pass | id shift +1 | Sắt huyết thanh là 12,9, bình thường. |
| c340 | c339 | pass | id shift +1 | Folat (B9) là 20,11 và bình thường. |
| c341 | c340 | pass | id shift +1 | B12 là 838,9, tăng nhẹ so với khoảng 197 đến 771. |
| c342 | c341 | pass | id shift +1 | Vitamin D là 31,76 (đơn vị phiên âm ghi là "n/ml"). |
| c343 | c342 | pass | id shift +1 | Canxi toàn phần là 2,2 và bình thường, canxi ion hóa là 1,15, giảm nhẹ so với 1, |
| c344 | c343 | pass | id shift +1 | Magie (bản ghi âm ghi là "Ma") là 0,82, bình thường. |
| c345 | c344 | pass | id shift +1 | Kẽm là 7,39, giảm so với 11 đến 24. |
| c346 | c345 | pass | id shift +1 | Đồng là 68,2, giảm nhẹ so với 70 đến 140. |
| c347 | c346 | pass | id shift +1 | Photpho trong giới hạn bình thường. |
| c348 | c347 | pass | id shift +1 | CT ghi nhận xẹp thùy giữa phổi phải, các ổ giãn phế nang trung tâm tiểu thùy ở h |
| c349 | c348 | pass | id shift +1 | Ba câu hỏi: (1) tổn thương phổi trên CT (xẹp thùy giữa phổi phải, giãn phế nang, |
| c350 | c349 | pass | id shift +1 | (2) biến động của men gan AST, axit uric, feritin tăng cùng thiếu kẽm, canxi ion |
| c351 | c350 | pass | id shift +1 | (3) với người nặng 42 kg, có viêm phổi tắc nghẽn mạn tính và viêm đường ruột, nê |
| c352 | c351 | pass | id shift +1 | Đoạn này chưa có phần trả lời cho các câu hỏi này. |
| c353 | c352 | pass | id shift +1 | Phần nhận xét tính BMI khoảng 18,67. |
| c354 | c353 | pass | id shift +1 | Phần nhận xét nói lớp mỡ dưới da gần như mất hoàn toàn và mỡ nội tạng bị giảm. |
| c355 | c354 | pass | id shift +1 | Điều đáng lo nhất là teo cơ nghiêm trọng, do quá trình dị hóa kéo dài nhiều thập |
| c356 | c355 | pass | id shift +1 | Nhận xét ghi BMI 18,67 ở ngưỡng gần suy kiệt. |
| c357 | c356 | pass | id shift +1 | Phần nhận xét cho rằng MPV giảm nghĩa là tiểu cầu nhỏ và kém sức sống, khả năng  |
| c358 | c357 | pass | id shift +1 | Phần nhận xét nói MCV và MCH “nằm ở ngưỡng cận trên và tăng nghệ” (bản ghi âm gh |
| c359 | c358 | pass | id shift +1 | Số lượng hồng cầu có thể chưa thấp đến mức thiếu máu cấp, nhưng cơ thể có thể đa |
| c360 | c359 | pass | id shift +1 | Nhận xét cho rằng nguyên nhân là tủy xương kiệt quệ sau nhiều năm, cộng với hít  |
| c361 | c360 | pass | id shift +1 | Phần nhận xét ví gan như bếp nấu năng lượng, AST tăng đơn độc giống ngọn khói từ |
| c362 | c361 | pass | id shift +1 | Nguyên nhân được nêu là khói thuốc lá kéo dài nhiều năm, uất ức kéo dài, cộng vớ |
| c363 | c362 | pass | id shift +1 | Phần nhận xét nói đây không phải bệnh của người ăn ngon mà là suy thoái chuyển h |
| c364 | c363 | pass | id shift +1 | Đường ruột viêm mạn tính làm không hấp thu được đạm, nên cơ thể tự phân hủy cơ b |
| c365 | c364 | pass | id shift +1 | Gan và thận thiếu vi chất nên giảm khả năng đào thải, và tinh thể urat có thể lắ |
| c366 | c365 | pass | id shift +1 | TSAT được tính bằng sắt huyết thanh chia cho TIBC nhân 100, ra 28,84%, trong kho |
| c367 | c366 | pass | id shift +1 | Phần nhận xét nói lượng sắt lưu hành vẫn ổn định. |
| c368 | c367 | pass | id shift +1 | Feritin 428,1 chỉ vượt nhẹ ngưỡng trên 400, không đáng lo về quá tải hay ngộ độc |
| c369 | c368 | pass | id shift +1 | Feritin tăng nhẹ được giải thích là do protein phản ứng pha cấp, phản ứng tự vệ  |
| c370 | c369 | pass | id shift +1 | Phần nhận xét nói sự kết hợp giữa kho sắt đóng cửa với số lượng xe chở sắt bị sụ |
| c371 | c370 | pass | id shift +1 | Biểu hiện gồm mệt mỏi dai dẳng, sức bền giảm, hồi phục chậm sau mỗi đợt ốm hoặc  |
| c372 | c371 | pass | id shift +1 | Kẽm tụt sâu xuống 7,39 (tham chiếu 11 đến 24). |
| c373 | c372 | pass | id shift +1 | Đồng giảm còn 68,2 (tham chiếu 70 đến 140). |
| c374 | c373 | pass | id shift +1 | Canxi ion hóa giảm nhẹ xuống 1,15 (tham chiếu 1,17 đến 1,29). |
| c375 | c374 | pass | id shift +1 | Transcript gọi kẽm và đồng là "những người thợ sửa chữa tí hon" của cơ thể. |
| c376 | c375 | pass | id shift +1 | Theo transcript, thiếu kẽm khiến niêm mạc ruột bị dò rỉ, dẫn tới viêm đường ruột |
| c377 | c376 | pass | id shift +1 | Người bệnh có thể khó tiêu, mất cảm giác ngon miệng, tóc dễ rụng, da khô ráp và  |
| c378 | c377 | pass | id shift +1 | Transcript cho rằng những thiếu hụt này xuất hiện sau nhiều thập kỷ hút thuốc lá |
| c379 | c378 | pass | id shift +1 | Phần nhận xét nói điều đáng bận tâm của bác không nằm ở con số feritin hay TSAT  |
| c380 | c379 | pass | id shift +1 | Việc cần làm là làm ấm lại đường ruột và lấp đầy những khoảng trống vi chất đã b |
| c381 | c380 | pass | id shift +1 | Phần nhận xét nói nhiều người có thể hoảng khi thấy chỉ số này cao, nhưng theo g |
| c382 | c381 | fail | id shift +1 | Ông so sánh với quy chuẩn tham chiếu của nhiều quốc gia phát triển như Nhật Bản  |
| c383 | c382 | pass | id shift +1 | Theo transcript, các bác sĩ chỉ thực sự lo khi vitamin B12 giảm nặng, gây thiếu  |
| c384 | c383 | pass | id shift +1 | Bác sĩ hiếm khi bận tâm khi chỉ số này tăng nhẹ, thậm chí tăng gấp rưỡi hoặc gấp |
| c385 | c384 | pass | id shift +1 | Lý do được nêu là B12 tan trong nước, phần dư thừa sẽ được thận đào thải qua nướ |
| c386 | c385 | pass | id shift +1 | Phần nhận xét nêu các lý do khiến chỉ số B12 tăng không đáng lo: B12 tan trong n |
| c387 | c386 | pass | id shift +1 | Thứ nhất, chỉ số B12 tăng thường đến từ dương tính giả hoặc nhiễu kỹ thuật. |
| c388 | c387 | pass | id shift +1 | Phân tử B12 lớn và có cấu trúc phức tạp, nên máy phân tích miễn dịch dễ nhầm với |
| c389 | c388 | pass | id shift +1 | Nguyên tố coban ở trung tâm phân tử có thể tương tác và bắt chước các kim loại k |
| c390 | c389 | pass | id shift +1 | Thứ hai, tổn thương gan mạn tính có thể giải phóng lượng B12 dự trữ vào máu, tạo |
| c391 | c390 | pass | id shift +1 | Transcript mô tả giãn phế nang trung tâm tiểu thùy ở cả hai lá phổi, khiến các v |
| c392 | c391 | pass | id shift +1 | Thùy giữa của phổi phải được mô tả là đã xẹp hoàn toàn do đàm đặc và tổ chức xơ  |
| c393 | c392 | pass | id shift +1 | Đường dẫn khí bị thu hẹp, xơ cứng và đóng cặn. |
| c394 | c393 | pass | id shift +1 | Theo transcript, nhựa thuốc lá kết hợp với bụi gỗ mịn bám chặt vào các phế nang  |
| c395 | c394 | pass | id shift +1 | Phần nhận xét liên hệ sự cô đơn sau cái chết của người bạn đời, việc hút thuốc l |
| c396 | c395 | pass | id shift +1 | Phần nhận xét nói một phần lá phổi của người thợ mộc đã vĩnh viễn ngừng trao đổi |
| c397 | c396 | pass | id shift +1 | Phần nhận xét nói gió mùa đông bắc hoặc vi khuẩn xâm nhập có thể khiến phế quản  |
| c398 | c397 | pass | id shift +1 | Transcript kể rằng đợt suy hô hấp cấp tính năm ngoái khiến bác phải cào xé từng  |
| c399 | c398 | pass | id shift +1 | CT cũng cho thấy động mạch chủ có các mảng vôi hóa kéo dài và thoái hóa cột sống |
| c400 | c399 | pass | id shift +1 | Phần nhận xét nói, canxi bị rút khỏi xương do suy dinh dưỡng, thiếu vitamin D và |
| c401 | c400 | pass | id shift +1 | Phần nhận xét nói bác Nghiên đã nhiều năm quên cách uống nước, chỉ uống khi cổ h |
| c402 | c401 | pass | id shift +1 | Theo transcript, điều này khiến máu đặc lại và đờm trong phế quản vón cục, cản t |
| c403 | c402 | pass | id shift +1 | Bác được khuyên nhấp từng ngụm nước ấm. |
| c404 | c403 | pass | id shift +1 | Phần nhận xét nói, việc đầu tiên là giải thoát tâm thức và xoa dịu lồng ngực đan |
| c405 | c404 | pass | id shift +1 | Transcript khuyên bác buông bỏ gánh nặng tinh thần sau khi vợ mất, vì khi tâm đư |
| c406 | c405 | pass | id shift +1 | Bác sĩ nói việc học lại cách thở là chìa khóa để mở lại luồng không khí cho tế b |
| c407 | c406 | pass | id shift +1 | Nếu hít thở nông và gấp gáp thì khí độc sẽ bị giam hãm bên trong, nên bác nên ki |
| c408 | c407 | pass | id shift +1 | Transcript nêu ba kỹ thuật: |
| c409 | c408 | pass | id shift +1 | Thở chúm môi kết hợp thở cơ hoành, nhịp 1:2: hít vào bằng mũi trong một nhịp, th |
| c410 | c409 | pass | id shift +1 | Sau đó chúm môi lại như đang thổi sáo và thở ra chậm trong hai nhịp dài gấp đôi  |
| c411 | c410 | pass | id shift +1 | Thở nhịp ba thì 1:1:1: hít vào một nhịp, giữ khí nhẹ nhàng một nhịp, rồi thở ra  |
| c412 | c411 | pass | id shift +1 | Transcript nói mỗi ngày bác có thể áp dụng thêm. |
| c413 | c412 | pass | id shift +1 | Thở 4-7-8: hít vào trong 4 giây, giữ hơi trong 7 giây, rồi thở ra bằng miệng tro |
| c414 | c413 | pass | id shift +1 | Theo transcript, kỹ thuật này dành cho những đêm trằn trọc khó ngủ. |
| c415 | c414 | pass | id shift +1 | Ngay sau đó, phần nhận xét nhắc tập thở trong sự tĩnh lặng của sáng sớm, trước 8 |
| c416 | c415 | pass | id shift +1 | Transcript khuyên giữ ấm tuyệt đối cho đôi bàn chân và vòng ngực mỗi khi gió mùa |
| c417 | c416 | pass | id shift +1 | Bác sĩ nói cơ thể không thể sửa chữa bằng thuốc cấp tính mà cần chữa lành từ nền |
| c418 | c417 | pass | id shift +1 | Bảy nhóm vi chất cần bổ sung đúng và đồng bộ gồm: canxi, magie, vitamin D, vitam |
| c419 | c418 | pass | id shift +1 | Bác sĩ nhấn mạnh đây không phải những viên thuốc rời rạc mà là một tập hợp các v |
| c420 | c419 | pass | id shift +1 | Phần nhận xét nói một thân thể đã mất 73 năm gánh chịu dông bão cần ít nhất nửa  |
| c421 | c420 | pass | id shift +1 | Trong thời gian này cần kiên nhẫn luyện thở đúng và duy trì dinh dưỡng tế bào ch |
| c422 | c421 | pass | id shift +1 | Bác sĩ nói gốc tự do là nguồn cơn của nhiều bệnh, và mọi căn bệnh đều đi qua một |
| c423 | c422 | pass | id shift +1 | Tuy nhiên ông nói có những bệnh ít liên quan hơn, ví dụ nhiễm virus, cảm cúm vặt |
| c424 | c423 | pass | id shift +1 | Ông vẫn cho rằng không thể nói hoàn toàn không liên quan, vì khi hệ miễn dịch su |
| c425 | c424 | pass | id shift +1 | Transcript nói phế (phổi) là nơi chứa nỗi buồn theo y học cổ truyền. |
| c426 | c425 | pass | id shift +1 | Bác sĩ nói tim và phổi nằm gần nhau và chịu chi phối của hệ thần kinh giao cảm,  |
| c427 | c426 | pass | id shift +1 | Bác sĩ cho rằng yếu tố tâm lý là yếu tố quan trọng số một để sinh ra gốc tự do. |
| c428 | c427 | pass | id shift +1 | Theo transcript, não tiêu tốn khoảng 20% năng lượng của cơ thể trong khi chỉ chi |
| c429 | c428 | pass | id shift +1 | Tim phải làm việc rất nhiều nên tốn nhiều năng lượng, và phổi cũng tiêu tốn nhiề |
| c430 | c429 | pass | id shift +1 | Bác sĩ coi cả ba tạng này là nguồn cơn sinh ra gốc tự do. |
| c431 | c430 | pass | id shift +1 | Bác sĩ nói người đàn ông dồn tình yêu vào người vợ nên nỗi đau mất vợ đè nặng lê |
| c432 | c431 | pass | id shift +1 | Bác Nghiên còn hút thuốc lá để quên nỗi buồn. |
| c433 | c432 | pass | id shift +1 | Bác sĩ nói thuốc lá sinh ra gốc tự do với số lượng rất lớn và đi thẳng vào phổi. |
| c434 | c433 | pass | id shift +1 | Theo transcript, gốc tự do phá vỡ ba thành phần chính là màng tế bào, protein và |
| c435 | c434 | pass | id shift +1 | Quá trình này tạo thành một vòng xoắn bệnh lý: các thành phần bị phá vỡ lại tiếp |
| c436 | c435 | pass | id shift +1 | Bác sĩ nói nghề thợ mộc rất vất vả, đặc biệt công việc cưa xẻ, và ông từng phải  |
| c437 | c436 | pass | id shift +1 | Ngày xưa không có khẩu trang, nên mùn cưa, bụi gỗ và hóa chất như sơn, đánh vecn |
| c438 | c437 | pass | id shift +1 | Các chất này đều là độc chất, và cũng tạo thành vòng xoắn sinh ra gốc tự do. |
| c439 | c438 | pass | id shift +1 | Theo transcript, gốc tự do làm men gan tăng cao và đi vào hệ tạo máu. |
| c440 | c439 | pass | id shift +1 | Hồng cầu to nhưng chất lượng không đảm bảo, tiểu cầu bé và không đủ khả năng vá  |
| c441 | c440 | pass | id shift +1 | Khi đó canxi lắng đọng trên thành mạch, làm loét mạch máu và dẫn tới vôi hóa thà |
| c442 | c441 | pass | id shift +1 | Bác sĩ nói người ta thường cho rằng axit uric cao là do béo, ăn nhiều đạm và mỡ, |
| c443 | c442 | pass | id shift +1 | Ông cho rằng đây cũng là một vòng xoắn liên quan đến gốc tự do. |
| c444 | c443 | pass | id shift +1 | Bác sĩ nói tế bào bị tổn thương ở cấp độ phân tử và tế bào sẽ tạo thành vòng xoắ |
| c445 | c444 | pass | id shift +1 | Từ đó bệnh có thể xuất hiện ở hết cơ quan này đến cơ quan khác, từ đường ruột, p |
| c446 | c445 | pass | id shift +1 | Cơ teo dần, tế bào cơ thoái hóa và tạo ra axit uric tăng. |
| c447 | c446 | pass | id shift +1 | Theo bác sĩ, chế độ ăn của người Việt không đủ vi chất. |
| c448 | c447 | pass | id shift +1 | Bác sĩ khen gia đình bác Nghiên chăm lo cẩn thận, chu đáo. |
| c449 | c448 | pass | id shift +1 | Ông kể con bác đã đưa bác đi khám và làm bệnh án. |
| c450 | c449 | pass | id shift +1 | Ông nói người cao tuổi khó tự tiếp cận kiến thức sâu nên cần con cháu hỗ trợ, nh |
| c451 | c450 | pass | id shift +1 | Bác sĩ nói nhiều người đến gặp ông và nói con cháu bận, không có thời gian chăm  |
| c452 | c451 | pass | id shift +1 | Ông cho rằng đây là điều chúng ta đang làm sai. |
| c453 | c452 | pass | id shift +1 | Ông kể một ca bệnh có người con gái chăm mẹ gầy yếu, và sau hơn một năm có kiến  |
| c454 | c453 | pass | id shift +1 | Bác sĩ nói không nên cố quá. |
| c455 | c454 | pass | id shift +1 | Bác có thể tập thở đơn giản theo "1 1,5", tức là cố gắng kéo dài thì thở ra một  |
| c456 | c455 | pass | id shift +1 | Bác sĩ nói bác có thể “chở thở 1 1,5 thôi đã” (bản ghi âm ghi như vậy), rồi nâng |
| c457 | c456 | pass | id shift +1 | Bác sĩ nhấn mạnh vitamin C và E rất quan trọng. |
| c458 | c457 | pass | id shift +1 | Bác sĩ nói đầu tiên là magie, rồi canxi, vitamin D3, vitamin tổng hợp (đặc biệt  |
| c459 | c458 | pass | id shift +1 | Ông gọi canxi, D3 và magie là "bộ ba tam giác vàng". |
| c460 | c459 | pass | id shift +1 | Ông nói nếu thiếu magie, kẽm hay các chất này thì các chất chống oxy hóa cũng mấ |
| c461 | c460 | pass | id shift +1 | Bác sĩ nói chủ đề chính của buổi hôm nay là giúp bác Nghiên hiểu sâu về gốc tự d |
| c462 | c461 | pass | id shift +1 | Ông cũng nhấn mạnh rằng trong bảy nhóm vi chất phải ít nhất có 18 sản phẩm, chưa |
| c463 | c462 | pass | id shift +1 | Bác sĩ nói ông đang hướng tới bước tiếp theo là 45 vi chất, rồi 60 vi chất. |
| c464 | c463 | pass | id shift +1 | Theo phần giới thiệu của chương trình, glutathion là cái tên xuất hiện nhiều gần |
| c465 | c464 | pass | id shift +1 | Khánh Lành, trong phần giới thiệu, nói đằng sau những lời truyền miệng hào nhoán |
| c466 | c465 | pass | id shift +1 | Hồ sơ cần có ngày tháng năm sinh, địa chỉ quê quán, nghề nghiệp hoặc công việc,  |
| c467 | c466 | pass | id shift +1 | Bác sĩ nói càng chi tiết càng tốt. |
| c468 | c467 | pass | id shift +1 | Hồ sơ thiếu ngày sinh, quê quán hoặc nghề nghiệp thì không thể phân tích đầy đủ. |
| c469 | c468 | fail | id shift +1 | Ông nêu bác Lương Trắc Nghiên (bác sĩ ở đây nói quê Hải Dương; hồ sơ bác đọc ở c |
| c470 | c469 | pass | id shift +1 | Phần giới thiệu nêu một số trường hợp: lạm dụng đường thô hoặc thực phẩm ngọt để |
| c471 | c470 | pass | id shift +1 | Nhiều người đi khám nơi nào cũng được nói là do "cơ địa". |
| c472 | c471 | pass | id shift +1 | Có người mẹ bị cạn kiệt năng lượng tế bào nhưng bị dán nhãn trầm cảm sau sinh ho |
| c473 | c472 | pass | id shift +1 | Bác sĩ dùng trường hợp chị Hằng (41 tuổi, bị bệnh từ năm 15 tuổi, sinh ba con, c |
| c474 | c473 | pass | id shift +1 | Bác sĩ nói chị ăn nhiều đường mía, và đường là kẻ thù hàng đầu tạo ra gốc tự do  |
| c475 | c474 | pass | id shift +1 | Theo bác sĩ, gốc tự do này tạo thành một vòng xoắn bệnh lý, ảnh hưởng đến não, g |
| c476 | c475 | pass | id shift +1 | Bác sĩ nói glutathion không hoạt động được nếu thiếu các yếu tố hiệp đồng. |
| c477 | c476 | pass | id shift +1 | Bác sĩ nêu kẽm, vitamin C và vitamin E cùng nhiều vi chất khác, và nói có đủ glu |
| c478 | c477 | pass | id shift +1 | Glutathion được tạo từ ba thành phần: glutamat (có trong mì chính), cystein (phầ |
| c479 | c478 | pass | id shift +1 | Bác sĩ ví glutathion như một chiếc kìm. |
| c480 | c479 | pass | id shift +1 | Phần mũi kìm là nhóm -SH (thiol). |
| c481 | c480 | pass | id shift +1 | Nhóm này có hydro và nguyên tử lưu huỳnh luôn sẵn sàng nhường electron và H+. |
| c482 | c481 | pass | id shift +1 | Glutamat giữ cho "kìm" ổn định, còn glycin là cánh tay chuyển động. |
| c483 | c482 | pass | id shift +1 | Bác sĩ nói liên kết cacbon gamma giữa glutamat và cystein là bước quan trọng nhấ |
| c484 | c483 | pass | id shift +1 | Glycin là cánh tay thứ hai và được gắn vào sau. |
| c485 | c484 | pass | id shift +1 | Để cơ thể tổng hợp được, khi ăn cần đủ glutamat, cystein và glycin. |
| c486 | c485 | pass | id shift +1 | Gốc tự do thì đi cướp electron và H+, nên glutathion gắp và trung hòa chúng. |
| c487 | c486 | pass | id shift +1 | Sau khi nhường electron và H+, mũi kìm bị hỏng, và glutathion được ký hiệu là GS |
| c488 | c487 | pass | id shift +1 | Hai glutathion hỏng sẽ khóa vào nhau tạo thành GSSG. |
| c489 | c488 | fail | id shift +1 | Ghi chú: GSSG là xác nhận của người duyệt; phiên âm không chứa (phiên âm ghi "GS |
| c490 | c489 | pass | id shift +1 | Được chuyển đến một "nhà máy" tái tạo (bản ghi viết là "redacta"), nơi cần năng  |
| c491 | c490 | pass | id shift +1 | NADPH cung cấp electron và H+ để tạo lại hai glutathion hoàn chỉnh. |
| c492 | c491 | fail | id shift +1 | Ghi chú: NADPH là xác nhận của người duyệt; phiên âm không ghi đúng "NADPH"; có  |
| c493 | c492 | pass | id shift +1 | Bác sĩ nhắc đến ba loại: superoxit (O2 với một electron dư, khởi điểm của các gố |
| c494 | c493 | pass | id shift +1 | Bác sĩ nói gốc hydroxyl là loại nguy hiểm bậc nhất vì nó nhỏ, linh động, không t |
| c495 | c494 | pass | id shift +1 | Bác sĩ cũng nói oxy già có thể trở thành loại nguy hiểm hơn khi có thêm sắt hai  |
| c496 | c495 | pass | id shift +1 | Bác sĩ nói việc cướp E và lấy H+ nhằm tạo thành H2O hiền hòa. |
| c497 | c496 | pass | id shift +1 | Đầu tiên bác sĩ nói cái thứ nhất là yếu tố tinh thần; tiếp theo ông đánh số: thứ |
| c498 | c497 | pass | id shift +1 | Thứ nhất là yếu tố tinh thần. |
| c499 | c498 | pass | id shift +1 | Tiếp theo là ăn uống: thực phẩm chứa hóa chất hoặc thuốc trừ sâu, và ăn quá nhiề |
| c500 | c499 | pass | id shift +1 | Tiếp theo là thuốc dùng không cần thiết, sai chỉ định hoặc uống quá đà, ví dụ pa |
| c501 | c500 | pass | id shift +1 | Bác sĩ cũng nhắc đến kim loại nặng như chì, thủy ngân và asen. |
| c502 | c501 | pass | id shift +1 | Bác sĩ nói những chất này có ba đặc điểm nguy hiểm: không tan nên cơ thể không đ |
| c503 | c502 | pass | id shift +1 | Khi glutathion gắp được chúng, nó bọc kín chất độc, làm mất khả năng bám dính và |
| c504 | c503 | pass | id shift +1 | Chất độc được bọc sẽ tan dễ hơn và được đào thải qua thận. |
| c505 | c504 | pass | id shift +1 | Gốc tự do nội sinh sinh ra từ ti thể, nơi chuyển hóa và hoạt động nhiều. |
| c506 | c505 | pass | id shift +1 | Bác sĩ xếp các cơ quan theo mức độ tập trung gốc tự do như sau: gan đứng đầu, rồ |
| c507 | c506 | pass | id shift +1 | Bác sĩ nói các cơ quan này thực hiện rất nhiều chức năng; riêng thận được gọi rõ |
| c508 | c507 | pass | id shift +1 | Bác sĩ nói enzyme GST có hai chức năng. |
| c509 | c508 | pass | id shift +1 | Thứ nhất là chỉ điểm: nó báo cho glutathion biết nơi nào có nhiều độc chất để gl |
| c510 | c509 | pass | id shift +1 | Thứ hai là yêu cầu mũi kìm mở ra để gắp độc chất. |
| c511 | c510 | pass | id shift +1 | Bác sĩ gọi enzyme này là "anh thợ" và nói glutathion không tự đến mà phụ thuộc v |
| c512 | c511 | pass | id shift +1 | Sau khi gắp, độc chất được đưa đến thận để đào thải. |
| c513 | c512 | pass | id shift +1 | Bác sĩ nói glutathion có thể giải độc ở gan, thận, ruột, não và các nơi khác. |
| c514 | c513 | pass | id shift +1 | Chị Hằng đã uống thuốc trầm cảm và thuốc thần kinh nhiều năm mà không đỡ. |
| c515 | c514 | pass | id shift +1 | Sau khi bổ sung vi chất, bác sĩ nói chị "tốt lên" và thoát khỏi trầm cảm, dù bác |
| c516 | c515 | pass | id shift +1 | Bác sĩ thuật lại (lời bác sĩ kể, không phải ca đã được kiểm chứng) rằng có người |
| c517 | c516 | pass | id shift +1 | Bác sĩ nói có những bạn trẻ được dán nhãn trầm cảm, tăng động giảm chú ý, tự kỷ  |
| c518 | c517 | pass | id shift +1 | Bác sĩ mô tả tế bào NK (tế bào tự nhiên) dùng gốc tự do làm vũ khí tấn công viru |
| c519 | c518 | pass | id shift +1 | Vũ khí này cũng có thể tấn công lại tế bào miễn dịch, và quá trình này có thể tạ |
| c520 | c519 | pass | id shift +1 | Glutathion có ba nhiệm vụ: trung hòa phần gốc tự do thừa để tránh bão cytokine,  |
| c521 | c520 | pass | id shift +1 | Bác sĩ nói glutathion còn điều chỉnh để vũ khí không bị thừa, thiếu hay cắm nhầm |
| c522 | c521 | pass | id shift +1 | Bác sĩ nói ti thể là nơi diễn ra trao đổi chất, đốt cháy đường, đạm và chất béo, |
| c523 | c522 | pass | id shift +1 | Ti thể có ADN riêng nằm sát màng ti thể, nên các gốc tự do thấm qua thì phá hủy  |
| c524 | c523 | pass | id shift +1 | Glutathion được đưa vào và bám dày đặc ở mặt trong màng ti thể để trung hòa gốc  |
| c525 | c524 | pass | id shift +1 | Bác sĩ nói khi ti thể được bảo vệ thì năng lượng tế bào được tạo ra tốt hơn. |
| c526 | c525 | pass | id shift +1 | Bác sĩ kể trường hợp chị Ngọc Thơ, giảm từ 56–57 kg xuống 52–53 kg sau khi bổ su |
| c527 | c526 | pass | id shift +1 | Bác sĩ giải thích rằng khi glutathion hoạt động hiệu quả, quá trình đốt cháy năn |
| c528 | c527 | fail | id shift +1 | Bác sĩ cũng kể trường hợp chị Ngân, điều dưỡng ở một bệnh viện lớn tại Hà Nội, c |
| c529 | c528 | fail | id shift +1 | Bác sĩ không nêu rõ liều hay điều kiện cụ thể. |
| c530 | c529 | pass | id shift +1 | Bác sĩ dùng hình ảnh một công xưởng trộn màu trong tế bào melanocyte. |
| c531 | c530 | pass | id shift +1 | Anh thợ tyrosinase phụ thuộc vào tia UV: khi tia UV nhiều, tyrosinase pha melani |
| c532 | c531 | pass | id shift +1 | Khi tia UV ít, nó pha màu trắng hơn. |
| c533 | c532 | pass | id shift +1 | Tia UV tạo ra gốc tự do làm tín hiệu báo động. |
| c534 | c533 | pass | id shift +1 | Glutathion trung hòa gốc tự do nên tín hiệu biến mất, và glutathion khóa tay tyr |
| c535 | c534 | pass | id shift +1 | Sau đó glutathion tự sử dụng công cụ pha màu trắng và làm da trắng hồng lên. |
| c536 | c535 | pass | id shift +1 | Bác sĩ nói "đấy là cái cơ chế làm trắng da là như vậy". |
| c537 | c536 | pass | id shift +1 | Bác sĩ tóm tắt các vai trò: giải độc (được ví là "vua của chống độc" ở gan, não, |
| c538 | c537 | pass | id shift +1 | Bác sĩ nhấn mạnh glutathion góp phần cùng nhiều vi chất khác, không phải một chấ |
| c539 | c538 | pass | id shift +1 | Bác sĩ nói cần đồng bộ hóa các lĩnh vực để khắc phục tình trạng. |
| c540 | c539 | pass | id shift +1 | Trên báo chí và mạng, glutathione thường được quảng cáo dưới dạng viên nén, viên |
| c541 | c540 | pass | id shift +1 | Bác sĩ cho rằng người xem cần có kiến thức để tự làm chủ sức khỏe của mình. |
| c542 | c541 | pass | id shift +1 | Theo bác sĩ, khi tìm kiếm các công trình nghiên cứu về glutathione sẽ thấy "khôn |
| c543 | c542 | pass | id shift +1 | Bác sĩ nói con số này cho thấy chất này rất được quan tâm, và nó đang thu hút ng |
| c544 | c543 | pass | id shift +1 | Glutathione khi uống theo đường miệng có hai dạng là viên nén hoặc viên nang và  |
| c545 | c544 | pass | id shift +1 | Bác sĩ cho rằng glutathione rất mong manh: khi đi qua dạ dày, axit và enzyme dạ  |
| c546 | c545 | pass | id shift +1 | Vì vậy uống các sản phẩm này "gần như không có tác dụng mấy". |
| c547 | c546 | pass | id shift +1 | Phần còn lại đi vào máu sau khi qua gan và quá trình chuyển hóa. |
| c548 | c547 | pass | id shift +1 | Tác dụng thực tế, theo bác sĩ, chủ yếu đến từ các thành phần đi kèm (kẽm, vitami |
| c549 | c548 | pass | id shift +1 | Liposome là công nghệ dẫn thuốc, dùng màng lipid bọc quanh hoạt chất, giống màng |
| c550 | c549 | pass | id shift +1 | Bác sĩ nêu hai điều cần lưu ý: thứ nhất, chất lượng phụ thuộc nhà sản xuất, vì c |
| c551 | c550 | pass | id shift +1 | Vì vậy, theo bác sĩ, không phải sản phẩm liposome nào uống cũng tốt. |
| c552 | c551 | pass | id shift +1 | Bác sĩ hẹn sẽ phân tích sâu hơn về công nghệ này trong một buổi khác nếu người x |
| c553 | c552 | pass | id shift +1 | Ngậm dưới lưỡi là đường thứ ba, vì niêm mạc lưỡi có mạch máu và thuốc không phải |
| c554 | c553 | pass | id shift +1 | Bác sĩ nói một số thuốc (như thuốc hạ sốt cho trẻ em) vẫn dùng cách này, nhưng v |
| c555 | c554 | pass | id shift +1 | Theo bác sĩ, ngậm dưới lưỡi là một giải pháp nhưng không phải là nhiều. |
| c556 | c555 | pass | id shift +1 | Bác sĩ cho rằng đường tiêm "quá nguy hiểm", có thể gây sốc và ngộ độc. |
| c557 | c556 | pass | id shift +1 | Bác sĩ nêu FDA của Mỹ không đồng ý và khuyến cáo không dùng đường này vì nguy cơ |
| c558 | c557 | pass | id shift +1 | Bác sĩ khuyên người xem không nên dại dột dùng đường tiêm. |
| c559 | c558 | pass | id shift +1 | Theo bác sĩ, cách khôn ngoan nhất là để cơ thể tự tổng hợp glutathione. |
| c560 | c559 | pass | id shift +1 | Quá trình này có hai enzyme chính, được ví như hai "anh thợ" (bản phiên âm ghi l |
| c561 | c560 | pass | id shift +1 | Enzyme thứ nhất, GCL, làm công đoạn khó nhất, tạo liên kết giữa glutamate và cys |
| c562 | c561 | pass | id shift +1 | Enzyme thứ hai, GS, tạo liên kết giữa cystein và glycin, công đoạn này dễ hơn. |
| c563 | c562 | pass | id shift +1 | Bác sĩ nói cơ thể có cơ chế điều hòa hai enzyme này để giảm sản xuất thừa, nên k |
| c564 | c563 | pass | id shift +1 | Để hai enzyme này hoạt động tốt, bác sĩ nhấn mạnh cần đủ selen, kẽm, vitamin C v |
| c565 | c564 | pass | id shift +1 | Bác sĩ nói “Fittain” (bản phiên âm ghi như vậy, chưa rõ) khá hiếm trong đồ ăn th |
| c566 | c565 | pass | id shift +1 | Vì vậy cần ăn đa dạng, phong phú thực phẩm. |
| c567 | c566 | pass | id shift +1 | Theo bác sĩ, nên ăn 25 loại thực phẩm trong một tuần, và 12 loại trong một ngày. |
| c568 | c567 | fail | id shift +1 | Ghi chú của người tóm tắt (không phải nội dung chương trình): đây là cách nói tr |
| c569 | c568 | pass | id shift +1 | Bác sĩ nói ăn đủ như vậy kết hợp với bổ sung đủ vi chất sẽ giúp cơ thể tổng hợp  |
| c570 | c569 | pass | id shift +1 | Điều quan trọng thứ ba là giảm gốc tự do để glutathione không bị tiêu hao. |
| c571 | c570 | pass | id shift +1 | Bác sĩ khuyên chỉ uống thuốc khi thật sự cần, không uống cả một vốc thuốc một ng |
| c572 | c571 | pass | id shift +1 | Ông cũng nói giảm rượu chè, giảm thuốc lá bỏ đi, tránh để thuốc trừ sâu và thuốc |
| c573 | c572 | pass | id shift +1 | Bác sĩ cũng nhắc nên giữ cân bằng, không ăn quá nhiều đường. |
| c574 | c573 | pass | id shift +1 | Cách tốt nhất, theo bác sĩ, là giảm các nguồn tạo gốc tự do và ăn uống cân bằng  |
| c575 | c574 | pass | id shift +1 | Nếu có điều kiện thì có thể bổ sung thêm bằng đường uống, dù ngấm không nhiều vì |
| c576 | c575 | pass | id shift +1 | Bác sĩ cho rằng chế độ ăn uống thường đã đủ các thành phần cơ bản, nên nếu không |
| c577 | c576 | pass | id shift +1 | Bác sĩ nói đừng tránh betacaroten như các chị đang bình luận. |
| c578 | c577 | pass | id shift +1 | Bác sĩ nói glutathione đang bán rất đắt và là sản phẩm "hot" trên thị trường. |
| c579 | c578 | pass | id shift +1 | Theo quan điểm cá nhân của bác sĩ, người ta hoàn toàn có thể hiểu cơ chế và kích |
| c580 | c579 | pass | id shift +1 | Nếu có tiền thì có thể mua thử và có hiệu quả, nhưng bác sĩ cho rằng nói hiệu qu |
| c581 | c580 | pass | id shift +1 | Bác sĩ nói trắng da ngoạn mục “chẳng qua là vì” bổ sung vi chất tốt, hiểu cơ chế |
| c582 | c581 | pass | id shift +1 | Người dẫn chương trình nhắc rằng các video trên kênh chỉ mang tính tham khảo, nh |
| c583 | c582 | pass | id shift +1 | Mỗi cơ thể là một trạng thái riêng với diễn biến bệnh lý phức tạp, nên khi có vấ |
