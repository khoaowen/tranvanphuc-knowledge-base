# Independent second pass — eight selected current claims

Scope: c181,c182,c186,c193,c198,c206,c207,c208 only. Provisional source-fidelity findings; comparison only, no adjudication or corrections. Publication remains blocked; no publication-state operation was performed.

## Binding and independent process

All four manifest file hashes and `scripts/fidelity.py` matched before reading. Summary: `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64`; transcript: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`; extractor: `cc570d0b53168ebce3027af755d5c2a91045faa2c4e8bd2a93f78dea2538da0d`. Review/metadata bytes were hashed, not read as evidence. Contract, format, continuation, manifest and claims extraction were read. The operator-approved replacement model applies.

Full-reading attestation: read-tool sequential summary chunks 1–220, 221–263 (EOF; requested through 320, tool displayed a trailing blank line); transcript chunks 1–600, 601–1200, 1201–1800, 1801–2400, 2401–3000, 3001–3600, 3601–4200, 4201–4800, 4801–5330 (EOF), from [00:00:01] through [03:32:39], without gaps. All eight findings considered the whole transcript. Own classes were printed in an in-memory `PYTHONDONTWRITEBYTECODE=1 python3` command before reading `pass1-c181-c210.md` rationales: seven supported, c208 attribution_qualification. Required continuation reading had already exposed prior class labels/flags; thus this is rationale-independent, not label-blind. No prior historical verdicts/IDs used as evidence. No external knowledge, medical corrections, inferred identities or speaker conclusions from `>>` alone.

## Comparison

| ID | First pass | Independent lock | Comparison |
|---|---|---|---|
| c181 | supported | supported | Agreement; joint exchange and explicit later repetition. |
| c182 | supported | supported | Agreement; storage during transport, not a legal standard. |
| c186 | supported | supported | Agreement; spoken self-correction and earlier EPA context. |
| c193 | supported | supported | Agreement; contrasting sick/healthy groups supports condition. |
| c198 | supported | supported | Agreement; earlier literal ng/ml resolves capitalization only. |
| c206 | supported | supported | Agreement with retained ASR reservation; no canonical expansion. |
| c207 | supported | supported | Agreement; “nhìn chung” retains the spoken small exception. |
| c208 | attribution_qualification | attribution_qualification | Agreement; response boundary uncertain, likely mixed speakers. |

Counts: supported 7; mismatch 0; attribution_qualification 1; unresolved 0. Class agreements 8/8: c181,c182,c186,c193,c198,c206,c207,c208. Class disagreements: none. First-pass and independent rationales remain separate; no accepted disposition implied. For c208 the independent issue is mixed-speaker compression; first pass additionally flags loss of “tôi nghĩ rằng”. The summary's “nói thêm ... nên” retains recommendation rather than certainty, so I do not independently require that additional hedge objection.

```json
[
  {
    "id": "c181",
    "section": "[03:09:08] Nguyên nhân Omega-3 dễ bị biến tính và cách bảo quản",
    "claim": "Công thức cấu tạo của Omega-3 chứa nhiều liên kết pi nên rất dễ bị biến tính và oxy hóa qua các phản ứng hóa học.",
    "evidence": [
      {"timestamp":"[03:09:30]","quote":"trong công thức cấu tạo của nó có quá"},
      {"timestamp":"[03:09:32]","quote":"nhiều liên kết pi thì quá nhiều liên kết"},
      {"timestamp":"[03:09:36]","quote":"Dễ bị oxy hóa."},
      {"timestamp":"[03:09:37]","quote":"Đúng rồi. Nó dễ bị biến tính."},
      {"timestamp":"[03:09:52]","quote":"omega 3 đi là cái này rất dễ bị rất dễ"},
      {"timestamp":"[03:09:57]","quote":"bị biến tính."},
      {"timestamp":"[03:10:07]","quote":"Nhiều liên kết pi cho nên rất dễ bị oxy"},
      {"timestamp":"[03:10:10]","quote":"hóa, rất dễ bị các cái phản ứng hóa học."}
    ],
    "speaker":"Bác sĩ Phúc giải thích trong câu trả lời, có người dẫn đáp ôn bài; summary không gán riêng từng câu đáp.",
    "class":"supported",
    "note":"Độc lập: quan hệ cấu tạo–oxy hóa–biến tính được nhắc lại rõ; không sửa chữ ‘khoa học’ ở 03:09:42 vì 03:10:10 nói hóa học. Đồng ý first pass supported và lý do trao đổi chung."
  },
  {
    "id": "c182",
    "section": "[03:09:08] Nguyên nhân Omega-3 dễ bị biến tính và cách bảo quản",
    "claim": "Nếu bảo quản sai cách hoặc vận chuyển xách tay không đúng quy chuẩn, Omega-3 sẽ bị hỏng và khi uống vào không có tác dụng khác gì nước lã.",
    "evidence": [
      {"timestamp":"[03:10:30]","quote":"xách tay từ nước ngoài về vẫn mua được"},
      {"timestamp":"[03:10:33]","quote":"đấy là sản phẩm tốt. Nhưng cái quá trình"},
      {"timestamp":"[03:10:35]","quote":"vận chuyển cá quá trình đem về nhà quý"},
      {"timestamp":"[03:10:37]","quote":"vị có biết bảo quản hay không?"},
      {"timestamp":"[03:10:39]","quote":"Hay là chúng ta bảo quản nó bị sai? Nếu"},
      {"timestamp":"[03:10:41]","quote":"bảo quản bị sai thì dầu cá này, Omega"},
      {"timestamp":"[03:10:44]","quote":"này rất nhanh biến tính và nó trở thành"},
      {"timestamp":"[03:10:46]","quote":"chúng ta uống như uống nước lã."},
      {"timestamp":"[03:12:00]","quote":"quản được. Nó hỏng đi, nó biến tính đi"}
    ],
    "speaker":"Bác sĩ Phúc trong phần giải thích bảo quản, được đặt trong câu trả lời của ông.",
    "class":"supported",
    "note":"Độc lập: diễn đạt hợp lý về sai bảo quản trong vận chuyển, không nói mọi hàng xách tay đều hỏng; ‘quy chuẩn’ không được đọc thành quy định pháp lý. Đồng ý first pass supported với cùng giới hạn diễn giải."
  },
  {
    "id": "c186",
    "section": "[03:13:11] Lựa chọn tỷ lệ EPA và DHA theo tình trạng bệnh lý",
    "claim": "Bác sĩ Phúc đưa ra nguyên tắc lựa chọn dựa trên nơi các chất ưu tiên đi tới: DHA ưu tiên đi vào não và mắt, còn EPA ưu tiên đi vào tim; theo bác sĩ Phúc, phần EPA còn thừa cũng có thể bổ sung cho não (ở đoạn trước ông nói EPA có dành một phần rất nhiều cho não, nhưng ưu thế vẫn dành cho tim).",
    "evidence": [
      {"timestamp":"[03:14:44]","quote":"DHA thì ưu tiên đi vào não và"},
      {"timestamp":"[03:14:47]","quote":"mắt."},
      {"timestamp":"[03:14:48]","quote":"Còn DPA à EPA thì đi vào đâu ạ?"},
      {"timestamp":"[03:14:52]","quote":"Đi vào tim. Chúng ta nhớ nguyên tắc đó."},
      {"timestamp":"[03:14:54]","quote":"Và EPA nó xu hướng ở ngoài còn thừa nó"},
      {"timestamp":"[03:14:56]","quote":"sẽ bổ sung cho não."},
      {"timestamp":"[02:25:27]","quote":"Tất nhiên EPA dành có dành một phần rất"},
      {"timestamp":"[02:25:29]","quote":"nhiều cho não nữa."},
      {"timestamp":"[02:25:30]","quote":"Nhưng mà ưu thế thì nó vẫn dành cho tim."}
    ],
    "speaker":"Bác sĩ Phúc hướng dẫn nguyên tắc, có lời đáp của người dẫn; giải thích trước đó cũng thuộc phần trả lời của ông.",
    "class":"supported",
    "note":"Độc lập: nguồn tự sửa DPA thành EPA; summary giữ cả phần còn thừa và lời trước về phần cho não/ưu thế tim. Đồng ý first pass supported; không bổ sung giải thích sinh học ngoài nguồn."
  },
  {
    "id": "c193",
    "section": "[03:13:11] Lựa chọn tỷ lệ EPA và DHA theo tình trạng bệnh lý",
    "claim": "Còn những ai khỏe mạnh, xét nghiệm tốt đẹp, cơ thể không bị bệnh gì thì bác sĩ Phúc nói 'chúng ta mua cái DHA tăng lên một chút' để ưu tiên cho não và mắt, 'sẽ rất thông minh, sẽ mắt sẽ rất tinh'; các cháu không bị gan nhiễm mỡ, không bị mỡ máu uống DHA thì 'sẽ thông minh lên, mắt sáng hơn'.",
    "evidence": [
      {"timestamp":"[03:16:08]","quote":"Còn những ai khỏe mạnh, xét nghiệm tốt"},
      {"timestamp":"[03:16:11]","quote":"đẹp như tranh vẽ, cơ thể chúng ta không"},
      {"timestamp":"[03:16:13]","quote":"bị bệnh các thứ gì thì chúng ta mua cái"},
      {"timestamp":"[03:16:15]","quote":"DHA tăng lên một chút."},
      {"timestamp":"[03:16:19]","quote":"mua tăng lên một chút để nó ưu tiên cho"},
      {"timestamp":"[03:16:21]","quote":"não và mắt thì chúng ta sẽ rất thông"},
      {"timestamp":"[03:16:22]","quote":"minh, sẽ mắt sẽ rất tinh. Thì chính cái"},
      {"timestamp":"[03:16:26]","quote":"điều đó mà giúp cho các cháu không bị"},
      {"timestamp":"[03:16:28]","quote":"gan nhiễm mỡ, không bị mỡ máu các cháu"},
      {"timestamp":"[03:16:30]","quote":"uống DHA này vào thì các cháu sẽ thông"},
      {"timestamp":"[03:16:32]","quote":"minh lên,"},
      {"timestamp":"[03:16:34]","quote":"mắt sẽ sáng hơn. Thế nhưng ngược lại nếu"},
      {"timestamp":"[03:16:36]","quote":"các cháu lại đang bị gan nhiễm mỡ và mỡ"}
    ],
    "speaker":"Bác sĩ Phúc phát triển lời khuyên; người dẫn có tiếp lời về mắt, được phần giải thích nhắc lại.",
    "class":"supported",
    "note":"Độc lập: giữ tăng một chút, nhóm khỏe mạnh và mức ‘sẽ’ của nguồn; đoạn đối lập ‘ngược lại nếu ... đang bị’ hỗ trợ điều kiện trẻ không bệnh dù câu trước nói vấp. Đồng ý first pass supported, không đổi thành tuyên bố DHA ngừa gan nhiễm mỡ."
  },
  {
    "id": "c198",
    "section": "[03:19:08] Bộ 7 vi chất dinh dưỡng và xét nghiệm Omega-3 trong tế bào hồng cầu",
    "claim": "Vitamin D (theo quan điểm bác sĩ Phúc và các chuyên gia ông nhắc đến, ngưỡng máu lý tưởng là 50–70 ng/ml)",
    "evidence": [
      {"timestamp":"[03:19:24]","quote":"vitamin D. Đây là bộ ba tam giác vàng vô"},
      {"timestamp":"[03:19:37]","quote":"ngưỡng lý tưởng ngưỡng phù hợp mà theo"},
      {"timestamp":"[03:19:40]","quote":"quan điểm của tôi và nhiều chuyên gia"},
      {"timestamp":"[03:19:41]","quote":"dinh dưỡng trên thế giới thì người ta"},
      {"timestamp":"[03:19:46]","quote":"ạ? Từ 50 đến 70 Ng/ml đúng không ạ? Máu"},
      {"timestamp":"[03:19:51]","quote":"khi mà chúng ta xét nghiệm"},
      {"timestamp":"[01:24:15]","quote":"đưa lên từ 50 cho đến 70"},
      {"timestamp":"[01:24:18]","quote":"ng/ml ở trong máu ta xét nghiệm thì đây"},
      {"timestamp":"[01:24:22]","quote":"chính là cái con số lý tưởng đúng không"}
    ],
    "speaker":"Bác sĩ Phúc nêu quan điểm bản thân và các chuyên gia ông nhắc, không phải lời chứng thực độc lập của chuyên gia.",
    "class":"supported",
    "note":"Độc lập: nguồn trước ghi nguyên đơn vị ng/ml, nguồn cuối Ng/ml; không cần sửa đơn vị từ kiến thức ngoài. Summary giữ quan điểm và khoảng 50–70; không lẫn với kinh nghiệm 70–80. Đồng ý first pass supported."
  },
  {
    "id": "c206",
    "section": "[03:19:08] Bộ 7 vi chất dinh dưỡng và xét nghiệm Omega-3 trong tế bào hồng cầu",
    "claim": "Người ta có thể căn cứ vào màng hồng cầu để thực hiện các xét nghiệm vi chất như canxi trong hồng cầu, magie trong hồng cầu, omega 3 và nhiều yếu tố khác kèm theo.",
    "evidence": [
      {"timestamp":"[03:27:46]","quote":"hồng cầu thì người ta sẽ xét nghiệm ví"},
      {"timestamp":"[03:27:49]","quote":"dụ như là canxi ở trong hồng cầu, mai ở"},
      {"timestamp":"[03:27:52]","quote":"trong hồng cầu, thế rồi thì omega 3 các"},
      {"timestamp":"[03:27:55]","quote":"thứ này ở trong hồng cầu thì người ta"},
      {"timestamp":"[03:27:57]","quote":"căn cứ vào cái màng hồng cầu đấy để"},
      {"timestamp":"[03:27:59]","quote":"người ta xét nghiệm rất là nhiều những"},
      {"timestamp":"[03:28:01]","quote":"cái mà kèm theo nó."},
      {"timestamp":"[03:19:19]","quote":"tam giác vàng là mag, canxi và gì ạ? Và"},
      {"timestamp":"[01:50:46]","quote":"là chúng ta sẽ có ma dê để tán gái, có"}
    ],
    "speaker":"Bác sĩ Phúc tiếp tục phần giải thích xét nghiệm sau khi đáp đề xuất của Khánh Lành.",
    "class":"supported",
    "note":"Độc lập: danh sách và căn cứ màng được nói rõ; magie là cách đọc theo ngữ cảnh lặp mag/ma dê của cùng cuộc bàn vi chất, không phải tên mở rộng ngoài nguồn. Cục bộ vẫn là ASR ‘mai’, không được coi đã xác minh âm thanh hay âm thầm sửa quote. Đồng ý first pass supported cùng reservation này; đây là điểm rủi ro còn giữ cho người duyệt."
  },
  {
    "id": "c207",
    "section": "[03:19:08] Bộ 7 vi chất dinh dưỡng và xét nghiệm Omega-3 trong tế bào hồng cầu",
    "claim": "Bác sĩ Phúc nêu rằng hồng cầu người nhìn chung không có nhân mà vẫn hoạt động bình thường, lấy đó làm luận cứ cho quan điểm màng tế bào là bộ não của tế bào.",
    "evidence": [
      {"timestamp":"[03:26:49]","quote":"Thế thì Khánh lành nhớ lại là tế bào"},
      {"timestamp":"[03:26:51]","quote":"hồng cầu người có đặc điểm gì?"},
      {"timestamp":"[03:26:54]","quote":"Không có nhân. Khác với lại tế bào của"},
      {"timestamp":"[03:27:08]","quote":"Nếu giả sử như nhân của tế bào là bộ não"},
      {"timestamp":"[03:27:12]","quote":"thì bây giờ tế bào hồng cầu mất mất bộ"},
      {"timestamp":"[03:27:14]","quote":"não rồi thì làm sao nó thực hiện được"},
      {"timestamp":"[03:27:15]","quote":"chức năng."},
      {"timestamp":"[03:27:17]","quote":"Vâng. Vậy thì màng tế bào hồng cầu nó"},
      {"timestamp":"[03:27:20]","quote":"mới là bộ não của tế bào. Bởi vì nhân"},
      {"timestamp":"[03:27:25]","quote":"Chỉ có những hồng cầu non mà từ hồng cầu"},
      {"timestamp":"[03:27:27]","quote":"lưới đi ra ngoài máu ngoại vi thì cái số"},
      {"timestamp":"[03:27:29]","quote":"đấy rất ít có nhân không đáng kể. Còn"},
      {"timestamp":"[03:27:32]","quote":"lại toàn bộ là tế bào hồng cầu không"},
      {"timestamp":"[03:27:34]","quote":"nhân mà nó vẫn hoạt động chức năng được"},
      {"timestamp":"[03:27:36]","quote":"bình thường. Nó chỉ mất đi cơ quan sinh"}
    ],
    "speaker":"Bác sĩ Phúc hỏi Khánh Lành rồi giải thích luận cứ; lời đáp ngắn không phải căn cứ duy nhất cho attribution.",
    "class":"supported",
    "note":"Độc lập: ‘nhìn chung’ cô đọng ngoại lệ ít hồng cầu non mà ông nêu, và summary gọi đây là luận cứ/quan điểm chứ không kết luận y khoa được kiểm chứng. Đồng ý first pass supported, không sửa lời nguồn về hồng cầu."
  },
  {
    "id": "c208",
    "section": "[03:19:08] Bộ 7 vi chất dinh dưỡng và xét nghiệm Omega-3 trong tế bào hồng cầu",
    "claim": "Trong phần trao đổi, người dẫn chương trình nhắc rằng bác sĩ nhấn mạnh nên xét nghiệm vitamin D trước khi bổ sung, và nói thêm rằng trước khi bổ sung Omega-3 thì người cần bổ sung cũng nên xét nghiệm (ví dụ mỡ máu, tiểu đường) để chọn loại Omega-3 có hàm lượng EPA và DHA phù hợp, rồi nâng lên bước cao hơn là khám sức khỏe toàn thân, khám tổng quát.",
    "evidence": [
      {"timestamp":"[03:23:18]","quote":"Vâng, tôi thì lại cảm ơn bác sĩ Phúc"},
      {"timestamp":"[03:23:45]","quote":"thì bác sĩ có nhấn mạnh rằng là trước"},
      {"timestamp":"[03:23:48]","quote":"khi bổ sung vitamin D thì điều cần thiết"},
      {"timestamp":"[03:23:51]","quote":"là chúng ta nên xét nghiệm vitamin D và"},
      {"timestamp":"[03:23:54]","quote":"tôi nghĩ rằng trước khi chúng ta bổ sung"},
      {"timestamp":"[03:23:57]","quote":"Omega 3 thì bản thân những người cần"},
      {"timestamp":"[03:24:01]","quote":"được bổ sung cũng nên xét nghiệm để"},
      {"timestamp":"[03:24:03]","quote":"chúng ta xem chúng ta có mỡ máu hay"},
      {"timestamp":"[03:24:06]","quote":"khỏe như thế nào để chọn loại omega 3 có"},
      {"timestamp":"[03:24:10]","quote":"cái chứa hàm lượng epadaha cho phù hợp."},
      {"timestamp":"[03:24:15]","quote":"Ừ. Vâng, đương nhiên đấy là cái mà chúng"},
      {"timestamp":"[03:24:19]","quote":"lên một cái bước cao hơn nữa đấy là"},
      {"timestamp":"[03:24:21]","quote":"chúng ta khám sức khỏe toàn thân và khám"},
      {"timestamp":"[03:24:23]","quote":"tổng quát. Vâng,"},
      {"timestamp":"[03:24:28]","quote":"máu không, có tiểu đường không,"},
      {"timestamp":"[03:26:13]","quote":"mà vì Khánh lành nói rằng nên xét nghiệm"},
      {"timestamp":"[03:26:15]","quote":"vitamin D, xét nghiệm các cái khác để"},
      {"timestamp":"[03:26:18]","quote":"chúng ta bổ sung hợp lý. Thì tôi lại nói"}
    ],
    "speaker":"Khánh Lành nhắc vitamin D và đề xuất xét nghiệm trước bổ sung Omega-3; phần khám tổng quát/tiểu đường có vẻ là bác sĩ Phúc đáp. Caption không gắn tên tại ranh giới 03:24:15.",
    "class":"attribution_qualification",
    "note":"Độc lập: nội dung hiện diện nhưng câu gộp dưới chủ ngữ người dẫn có nguy cơ gán luôn đáp lời khám tổng quát và ví dụ tiểu đường cho Khánh Lành; hồi chỉ của bác sĩ ở 03:26:13–18 hỗ trợ phân chia, không dựa marker đơn lẻ. Đồng ý class first pass; first pass thêm objection mất ‘tôi nghĩ rằng’, còn tôi xem ‘nói thêm ... nên’ vẫn giữ tính đề xuất nên không độc lập khẳng định objection phụ ấy. Ranh giới speaker vẫn provisional, không adjudication."
  }
]
```

## Validation and residual risks

In-memory `PYTHONDONTWRITEBYTECODE=1 python3` validation: exact eight ordered IDs, exact claim/section strings from current 210-record extraction, exactly seven record keys and two evidence keys, allowed classes, nonempty literal quotes on actual cited timestamp lines, all four manifest file hashes and extractor unchanged. Mechanical integrity is not semantic adjudication. Validation PASS: 90/90 literal timestamp-line quotes; eight records match extraction. Source line counts via Python splitlines(): summary 263; transcript 5,330. The lock command initially described the summary endpoint as 264 from read-tool display; this is corrected here to 263 content lines, with no reading gap.

Residual risks: c206's local ‘mai’ remains ASR-uncertain despite contextual support; c193's spoken syntax and c208's unlabelled speaker boundary retain the reservations above. No audio verification or medical validity asserted. Existing first passes and all earlier independent slices preserved. No omission pass performed.

Process deviations: initial `claims.json` request exceeded the read tool's 50KB bound and returned lines 1–751; immediately continued at 752 through EOF without gaps. Summary/transcript bounded reads were not truncated and had no gaps. Mandatory continuation exposed class labels before the independent lock (disclosed above); first-pass rationales were read only after the lock. No scratch/temp/script files, sandbox execution, nested agents, commits or unrelated edits; only this new artifact written. Review and metadata accessed only for hash checks.
