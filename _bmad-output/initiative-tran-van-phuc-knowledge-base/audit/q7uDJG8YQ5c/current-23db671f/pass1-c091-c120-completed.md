# Recovered first pass — c091–c120 — PROVISIONAL

## Binding, reading and recovery report

Summary SHA-256: `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64`.
Transcript SHA-256: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`.
Both manifest-path hashes matched BEFORE evidence reading. Operator's explicit `openai-codex/gpt-6.1-sol` amendment supersedes the historical Anthropic-only instruction; requested model is not an independently inspected runtime receipt.

Read the contract and record-format companion, continuation, manifest, recovered draft, current claims extraction (target records in full), and current summary lines 95–159. Claims and sections below are copied exactly from claims.json, not historical IDs. Only the current summary and transcript determine findings; draft verdicts were reconsidered, not adopted as authority. Completed c001–c090 were not rerun or opened.

Full-transcript reading attestation: read transcript.md sequentially, with no gaps, using read-tool ranges 1–650, 651–1300, 1301–1950, 1951–2600, 2601–3250, 3251–3900, 3901–4550, 4551–5200, 5201–EOF. Python splitlines reports 5,330 content lines; read-tool EOF accounting includes an additional trailing empty line. Coverage runs from [00:00:01] through [03:32:39]. Every target claim was considered against this full reading, not only section windows. No global omission pass or later batch is claimed.

The original draft remains untouched. Its 302 evidence entries were checked in memory: 299 passed and THREE failed: c105 and c112 put the same quote at [02:14:01] instead of [02:14:02]; c106 put its quote at [02:15:31] instead of [02:15:29]. Corrected anchors appear below. This is more than the initially reported c105 failure. Selected valid draft anchors and rationales are retained; redundant anchors are condensed and missing list continuations added. All new-artifact quotes must pass the timestamp-line substring check independently.

Speaker convention: the transcript introduces Khánh Lành and bác sĩ Trần Văn Phúc at the beginning and explicitly establishes the article-reading and doctor-led questioning segments. Speaker fields report these textual roles, not inferred identities from ASR markers, vocal characteristics or outside knowledge. A claim's named attribution is not independently audio-verified; ambiguous local turns remain explicitly unresolved. `>>` alone is never proof. ASR spellings in evidence are unaltered; no medical correctness verdict is made. Summary editorial commentary is not used as source evidence.

## Provisional counts and independent-recheck flags

- supported: 23; unresolved: 7; mismatch: 0; attribution_qualification: 0.
- Required independent recheck: c092, c096, c110, c112, c115, c116, c120. The recovered draft's supported findings for c092/c096/c110/c116 are downgraded here because the supplied text does not settle the oil name, CLA expansion, lupus expansion, or component-versus-group ratio respectively. These are proposed first-pass dispositions, not final acceptance.
- Supported but flagged: c093 (implicit comparator); c097 (non-exhaustive list); c100 (spoken numbers, no medical correction); c101 (ASR technical-name normalization and joint quiz explanation); c103 (30% referent varies elsewhere); c105 (LA/ALA/AA ASR conflict and merged hypotheticals); c108 (metabolic-chain compression and ASR cẩu/cầu); c109 (ASR thyroid/disease labels and joint quiz attribution); c111 (GL/GLA cross-reference); c114 (deictic referent); c117 (citation boundary and 4-versus-5 formulations); c118 (deictic numerator and gold metaphor). Flags are part of the note field to retain the existing seven-field record schema.
- Publication remains blocked as an audit disposition; no queue-state API was invoked or publication clearance attempted.

## Records

```json
[
  {
    "id": "c091",
    "section": "[01:53:28] Tỷ lệ Omega-6 và Omega-3 đối với các bệnh mãn tính",
    "claim": "Bài báo còn nói nếu ăn thức ăn chế biến sẵn kiểu công nghiệp hàng ngày thì tỷ lệ Omega-6/Omega-3 'chẳng còn quan trọng gì nữa'; loại chất béo dùng quan trọng hơn nhiều so với tỷ lệ này.",
    "evidence": [
      {"timestamp":"[01:54:12]","quote":"nước. Tôi xin trích dẫn nguyên văn nội"},
      {"timestamp":"[01:58:54]","quote":"nếu bạn ăn thức ăn chế biến sẵn theo"},
      {"timestamp":"[01:58:56]","quote":"kiểu công nghiệp hàng ngày thì tỉ lệ"},
      {"timestamp":"[01:58:58]","quote":"omega6/ên omega 3 chẳng còn quan trọng"},
      {"timestamp":"[01:59:01]","quote":"gì nữa. Vì vậy, loại chất béo bạn dùng"},
      {"timestamp":"[01:59:03]","quote":"quan trọng hơn rất nhiều so với tỉ lệ"},
      {"timestamp":"[01:59:26]","quote":"bài báo được Khánh lành trích dẫn từ một"}
    ],
    "speaker": "Khánh Lành reading an article, explicitly identified as her quotation at [01:59:26]; summary attributes to the article.",
    "class": "supported",
    "note": "Daily industrial-food condition and comparative importance preserved. No independent-recheck flag beyond routine review."
  },
  {
    "id": "c092",
    "section": "[01:53:28] Tỷ lệ Omega-6 và Omega-3 đối với các bệnh mãn tính",
    "claim": "Để tối ưu hóa tỷ lệ, bài báo khuyên tránh các loại dầu thực vật và hạt chứa nhiều Omega-6 cũng như thực phẩm chế biến từ dầu và hạt: dầu đậu nành, dầu hướng dương, dầu ngô chứa nhiều Omega-6, còn dầu ô liu, dầu cọ, dầu dừa và quả bơ chứa ít Omega-6 hơn.",
    "evidence": [
      {"timestamp":"[01:56:53]","quote":"Để tối ưu hóa tỉ lệ, chúng ta cần tránh"},
      {"timestamp":"[01:56:55]","quote":"tiêu thụ các loại dầu thực vật và hạt"},
      {"timestamp":"[01:56:57]","quote":"chứa nhiều omega6 cũng như các loại thực"},
      {"timestamp":"[01:57:00]","quote":"phẩm sử dụng dầu và hạt để chế biến. Dầu"},
      {"timestamp":"[01:57:03]","quote":"đậu nành, dầu hướng dương, ngô được biết"},
      {"timestamp":"[01:57:06]","quote":"là chứa hàm lượng lớn omega6. Còn dầu"},
      {"timestamp":"[01:57:09]","quote":"ôu, dầu cọ, dầu dừa, quả bơ được biết là"},
      {"timestamp":"[01:57:13]","quote":"chứa ít omega6 hơn."}
    ],
    "speaker": "Article-reading role, explicitly attributed to Khánh Lành in the surrounding exchange; summary says bài báo.",
    "class": "unresolved",
    "note": "Most content is direct. RECHECK: the supplied text says ôu, not ô liu; the full reading does not establish this oil's exact identity. Do not silently resolve that ASR spelling. Also retain được biết là rather than treating this as independently verified composition."
  },
  {
    "id": "c093",
    "section": "[01:53:28] Tỷ lệ Omega-6 và Omega-3 đối với các bệnh mãn tính",
    "claim": "Muốn giảm Omega-6 trong thịt thì chọn phần gầy; bơ thực vật chứa nhiều Omega-6 hơn, nên dùng bơ từ động vật ăn cỏ để có nhiều Omega-3 hơn.",
    "evidence": [
      {"timestamp":"[01:57:13]","quote":"Nếu muốn giảm lượng"},
      {"timestamp":"[01:57:17]","quote":"omega6 có trong thịt thì hãy chọn các"},
      {"timestamp":"[01:57:20]","quote":"loại thịt ở những phần gầy hơn."},
      {"timestamp":"[01:57:23]","quote":"Bơ thực vật chứa nhiều omega6 hơn, thay"},
      {"timestamp":"[01:57:26]","quote":"vào đó, sử dụng bơ từ động vật ăn cỏ cho"},
      {"timestamp":"[01:57:29]","quote":"nhiều omega 3 hơn bơ thông thường."}
    ],
    "speaker": "Article-reading role; the summary paragraph attributes this advice to the article.",
    "class": "supported",
    "note": "Conditional and advice match. SUPPORTED FLAG: summary leaves the explicit comparator bơ thông thường implicit in hơn; independently check whether that compression changes the comparison."
  },
  {
    "id": "c094",
    "section": "[01:53:28] Tỷ lệ Omega-6 và Omega-3 đối với các bệnh mãn tính",
    "claim": "Vì gia súc, gia cầm ngày nay thường được nuôi bằng thức ăn từ hạt (nhiều bắp, đậu nành) nên mỡ tích trữ của chúng chủ yếu là Omega-6, rất ít Omega-3; nếu có thể, nên dùng thịt từ động vật nuôi bằng cỏ.",
    "evidence": [
      {"timestamp":"[01:57:33]","quote":"Ngày nay, các loài gia súc da cầm thường"},
      {"timestamp":"[01:57:35]","quote":"được nuôi bằng thực phẩm dựa trên các"},
      {"timestamp":"[01:57:37]","quote":"loại hạt, trong đó có chứa nhiều bắp và"},
      {"timestamp":"[01:57:40]","quote":"đậu nành, vốn là các loại thực vật nhiều"},
      {"timestamp":"[01:57:42]","quote":"omega6."},
      {"timestamp":"[01:57:44]","quote":"Điều này dẫn đến lượng mỡ tích trữ trong"},
      {"timestamp":"[01:57:46]","quote":"các loài động vật này cũng hầu như là"},
      {"timestamp":"[01:57:49]","quote":"omega6, rất ít omega 3. Do đó, nếu có"},
      {"timestamp":"[01:57:53]","quote":"thể thì việc sử dụng các loại thịt từ"},
      {"timestamp":"[01:57:56]","quote":"động vật được nuôi bằng cỏ là tối ưu"}
    ],
    "speaker": "Article-reading role, not independent advice newly assigned to the doctor.",
    "class": "supported",
    "note": "Usually, predominantly, very little and if possible remain; da cầm retained literally in evidence."
  },
  {
    "id": "c095",
    "section": "[01:53:28] Tỷ lệ Omega-6 và Omega-3 đối với các bệnh mãn tính",
    "claim": "Thịt gà, thịt lợn vốn có sẵn nhiều Omega-6 vẫn có thể dùng ở mức vừa phải, hoặc chọn phần nạc ít mỡ nếu muốn giảm tối đa lượng Omega-6.",
    "evidence": [
      {"timestamp":"[01:58:01]","quote":"vốn đã có hàm lượng omega6 cao sẵn, ví"},
      {"timestamp":"[01:58:05]","quote":"dụ như là thịt gà hay thịt lợn thì bạn"},
      {"timestamp":"[01:58:07]","quote":"vẫn có thể dùng ở mức độ vừa phải. Hoặc"},
      {"timestamp":"[01:58:10]","quote":"nếu bạn đang có nhu cầu giảm tải lượng"},
      {"timestamp":"[01:58:12]","quote":"omega 6 tối đa thì vẫn có thể dùng nhưng"},
      {"timestamp":"[01:58:15]","quote":"với điều kiện là chọn phần nạc ít mỡ."}
    ],
    "speaker": "Article-reading role; matches the paragraph's article attribution.",
    "class": "supported",
    "note": "Moderation and lean-cut condition both preserved."
  },
  {
    "id": "c096",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "Các axit béo chính cần nhớ thuộc nhóm Omega-6 gồm: LA (axit linoleic), GLA, CLA (axit béo liên hợp) và AA.",
    "evidence": [
      {"timestamp":"[02:01:07]","quote":"Ờ axit la."},
      {"timestamp":"[02:01:16]","quote":"Axit linolic. Rồi đúng rồi."},
      {"timestamp":"[02:01:20]","quote":"Là ờ GLA."},
      {"timestamp":"[02:01:23]","quote":"GL. Đúng rồi."},
      {"timestamp":"[02:01:26]","quote":"Là CL."},
      {"timestamp":"[02:01:27]","quote":"Clức là cái này là gọi là axit béo liên"},
      {"timestamp":"[02:01:31]","quote":"hợp đấy."},
      {"timestamp":"[02:01:33]","quote":"Còn gì nữa không? Aa"},
      {"timestamp":"[02:01:36]","quote":"đây là bốn cái axit béo mà chúng ta cần"},
      {"timestamp":"[02:01:40]","quote":"phải nhớ ở trong omega6."}
    ],
    "speaker": "Doctor-led quiz with Khánh Lành, explicitly established by the request to her at [02:00:30]; the summary names no individual speaker here.",
    "class": "unresolved",
    "note": "Four-item remember-frame and spoken list are present. RECHECK: CL/Clức does not explicitly spell CLA; linolic versus linoleic is also normalized by the summary. Preserve the spoken forms; do not establish the missing letter from outside chemistry knowledge."
  },
  {
    "id": "c097",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "Nhóm Omega-3 gồm: ALA, EPA và DHA.",
    "evidence": [
      {"timestamp":"[02:01:47]","quote":"Tiếp tục omega 3 thì ta cần phải nhớ mấy"},
      {"timestamp":"[02:01:53]","quote":"Là ALA."},
      {"timestamp":"[02:01:58]","quote":"Ờ EPA."},
      {"timestamp":"[02:02:01]","quote":"Và rất quan trọng đó là DHA."},
      {"timestamp":"[02:02:04]","quote":"Đấy là ba cái mà rất quan trọng. Thế còn"},
      {"timestamp":"[02:02:09]","quote":"ví dụ như là DPA chẳng hạn đúng không?"}
    ],
    "speaker": "Doctor-led quiz exchange; summary is unattributed list text.",
    "class": "supported",
    "note": "These three are stated. SUPPORTED FLAG: DPA is also named; support depends on reading gồm as the preceding main-items-to-remember frame, not an exhaustive taxonomy."
  },
  {
    "id": "c098",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "LA (Omega-6) có công thức cấu tạo C18:2n-6, gồm 18 nguyên tử cacbon, 2 liên kết pi và liên kết pi đầu tiên xuất hiện ở vị trí cacbon số 6, kết thúc bằng nhóm COOH.",
    "evidence": [
      {"timestamp":"[02:02:37]","quote":"LA. Bất kỳ một cái nào trong này chúng"},
      {"timestamp":"[02:03:09]","quote":"à? C18 ạ. C18 đúng không ạ?"},
      {"timestamp":"[02:03:13]","quote":"Hai chấm"},
      {"timestamp":"[02:03:15]","quote":"2n"},
      {"timestamp":"[02:03:17]","quote":"gạch ngang"},
      {"timestamp":"[02:03:18]","quote":"ngang 6"},
      {"timestamp":"[02:03:20]","quote":"6 đúng không ạ? Đấy là cấu tạo của la."},
      {"timestamp":"[02:03:44]","quote":"Là có 18 nguyên tử cacbon."},
      {"timestamp":"[02:03:47]","quote":"có hai liên kết pi."},
      {"timestamp":"[02:03:49]","quote":"Liên kết pi đầu tiên đứng ở vị trí"},
      {"timestamp":"[02:03:50]","quote":"cacbon số 6."},
      {"timestamp":"[02:04:35]","quote":"ở đây cuối cùng đây chính là gắn với lại"},
      {"timestamp":"[02:04:41]","quote":"oxy đúng không ạ? Tức là COOH chính là"},
      {"timestamp":"[02:04:50]","quote":"la. Ta chỉ cần thuộc cái nắm được cái"}
    ],
    "speaker": "Question-and-answer construction in the doctor-led quiz; summary does not assign each fragment to one speaker.",
    "class": "supported",
    "note": "Uses the corrected C18 answer, not the earlier C16 false start; notation, counts, position and terminal group follow the supplied text."
  },
  {
    "id": "c099",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "ALA (Omega-3) có công thức cấu tạo C18:3n-3, gồm 18 nguyên tử cacbon, 3 liên kết pi và liên kết pi đầu tiên xuất hiện ở vị trí cacbon số 3, kết thúc bằng nhóm COOH.",
    "evidence": [
      {"timestamp":"[02:03:25]","quote":"Tôi lại hỏi luôn cấu tạo của ALA là gì?"},
      {"timestamp":"[02:03:30]","quote":"Ờ C18"},
      {"timestamp":"[02:03:34]","quote":"3N"},
      {"timestamp":"[02:03:36]","quote":"gì? Gạch ngang"},
      {"timestamp":"[02:03:38]","quote":"3 Đúng rồi."},
      {"timestamp":"[02:05:03]","quote":"cũng là 18"},
      {"timestamp":"[02:05:07]","quote":"kết pi đầu tiên ở"},
      {"timestamp":"[02:05:10]","quote":"số 3 số 3."},
      {"timestamp":"[02:05:53]","quote":"Alla của Omega 3."},
      {"timestamp":"[02:06:00]","quote":"nhau ở chỗ là đều có 18 nguyên tử cacbon"},
      {"timestamp":"[02:06:03]","quote":"đều có nhóm COOH"},
      {"timestamp":"[02:06:09]","quote":"cái thì có hai liên kết pi còn một cái"},
      {"timestamp":"[02:06:13]","quote":"Ba liên kết pi"}
    ],
    "speaker": "Doctor-led quiz exchange; no individual attribution in this summary item.",
    "class": "supported",
    "note": "Three-bond count is explicit in the comparison despite garbling earlier at [02:05:04]; notation and shared COOH support the item without medical correction."
  },
  {
    "id": "c100",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "Trong nguồn, bác sĩ Phúc nói DHA có 22 nguyên tử cacbon và 5 liên kết pi.",
    "evidence": [
      {"timestamp":"[02:07:37]","quote":"Và đến DHA này nó có tới tận năm liên"},
      {"timestamp":"[02:07:40]","quote":"kết pi cơ cho nên là nó rất quý. có 22"},
      {"timestamp":"[02:07:44]","quote":"nguyên tử cacbon mà lại có đến năm liên"},
      {"timestamp":"[02:07:46]","quote":"kết pi thì đương nhiên rất quý và chúng"},
      {"timestamp":"[02:07:59]","quote":"khó. Nào Khánh Lành đã thấy rất dễ chưa"},
      {"timestamp":"[02:21:00]","quote":"C22"},
      {"timestamp":"[02:21:02]","quote":"à 5N chứ"}
    ],
    "speaker": "Lecturer in the established doctor-led quiz, addressing Khánh Lành; summary explicitly reports what the source says.",
    "class": "supported",
    "note": "SUPPORTED FLAG: 22 and five are spoken; support is source fidelity only. Do not substitute the summary's external editorial correction or medical knowledge."
  },
  {
    "id": "c101",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "Bác sĩ Phúc giải thích rằng liên kết pi dễ bị phá vỡ, giúp axit béo được cắt thành các phân tử acetyl-CoA hai cacbon để đốt cháy tạo năng lượng trong ti thể.",
    "evidence": [
      {"timestamp":"[02:06:35]","quote":"Liên kết pi là liên kết không bền vững"},
      {"timestamp":"[02:06:37]","quote":"cho nên dễ dàng bị phá vỡ ở chỗ này."},
      {"timestamp":"[02:06:44]","quote":"cắt nhỏ để tạo thành các"},
      {"timestamp":"[02:06:47]","quote":"Axetin coenzyma ở trong đâu?"},
      {"timestamp":"[02:06:51]","quote":"ở trong ti thể"},
      {"timestamp":"[02:07:21]","quote":"coenzym a tức là những các cái mảnh nhỏ"},
      {"timestamp":"[02:07:23]","quote":"có hai nguyên tử cacbon để chúng ta thực"},
      {"timestamp":"[02:07:25]","quote":"hiện cái quá trình đốt cháy cho nó dễ"},
      {"timestamp":"[02:07:27]","quote":"dàng ở trong ti thể."},
      {"timestamp":"[02:12:21]","quote":"vào trong tiể thực hiện đốt cháy để sinh"},
      {"timestamp":"[02:12:24]","quote":"ra năng lượng và sinh ra khí số 2 và"}
    ],
    "speaker": "Explanation in the doctor-led quiz, built with interlocutor answers; not every short answer is assigned to the doctor.",
    "class": "supported",
    "note": "Two-carbon fragments, breaking and mitochondrial burning are explicit; energy is stated in the later repetition. SUPPORTED FLAG: acetyl-CoA is the summary's normalization of Axetin coenzyma/coenzym a, not a verbatim spelling; independently recheck entity fidelity and joint-exchange attribution."
  },
  {
    "id": "c102",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "Ông nhận xét axit béo càng nhiều liên kết pi thì càng quý.",
    "evidence": [
      {"timestamp":"[02:07:12]","quote":"Và nó càng nhiều liên kết pi thì nó càng"},
      {"timestamp":"[02:07:14]","quote":"quý."},
      {"timestamp":"[02:07:15]","quote":"Để chúng ta cắt được nó ra."}
    ],
    "speaker": "Continuing lecturer explanation in the established doctor-led segment; matches ông in context.",
    "class": "supported",
    "note": "Value judgement is stated directly; the dropped cutting rationale is not a hedge or contrary condition."
  },
  {
    "id": "c103",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Màng tế bào chứa rất nhiều enzyme để tiếp nhận axit béo vào cấu tạo màng (chất béo chiếm 30% cấu trúc màng).",
    "evidence": [
      {"timestamp":"[02:08:37]","quote":"tạo bởi các axit béo mà axit béo ở đây"},
      {"timestamp":"[02:08:40]","quote":"chiếm tới 30%."},
      {"timestamp":"[02:08:42]","quote":"30% để cấu tạo lên cái màng tế bào này."},
      {"timestamp":"[02:08:57]","quote":"màng tế bào này nó có chứa rất nhiều"},
      {"timestamp":"[02:08:59]","quote":"enzyme. Nó chứa enzyme. Enzyme này để"},
      {"timestamp":"[02:09:13]","quote":"hiện cái enzyme phát ra tín hiệu để tiếp"},
      {"timestamp":"[02:09:16]","quote":"nhận cái chất béo đó vào trong màng."},
      {"timestamp":"[01:48:21]","quote":"Omega3 chiếm tới bao nhiêu ạ? Chiếm tới"},
      {"timestamp":"[01:48:24]","quote":"30%"}
    ],
    "speaker": "Lecturer explanation in the doctor-led segment; summary sentence does not newly name a speaker.",
    "class": "supported",
    "note": "Local passage supports both parts. SUPPORTED FLAG: earlier passage assigns 30% to Omega3, while this passage says axit béo and [02:22:06] says omega; preserve this variation, not reconcile medically."
  },
  {
    "id": "c104",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Do Omega-6 và Omega-3 có cấu trúc hóa học hao hao giống nhau, các enzyme dùng chung rất khó phân biệt và sẽ cạnh tranh dựa trên số lượng: loại axit béo nào xuất hiện nhiều hơn sẽ được enzyme ưu tiên nhận vào để cấu tạo màng tế bào, còn loại ít hơn sẽ bị đẩy vào trong ti thể chỉ để đốt cháy tạo năng lượng.",
    "evidence": [
      {"timestamp":"[02:11:14]","quote":"ngăm ở chỗ rằng là cái omega6 và cái"},
      {"timestamp":"[02:11:18]","quote":"omega 3 này những cái thành phần này có"},
      {"timestamp":"[02:11:20]","quote":"cấu tạo nó cứ hao hao giống nhau. Cho"},
      {"timestamp":"[02:11:23]","quote":"nên là các enzyme này nó rất khó nhận"},
      {"timestamp":"[02:11:25]","quote":"rất khó nhận biết và rất khó phân biệt."},
      {"timestamp":"[02:12:38]","quote":"cùng chung một enzyme và vì cấu tạo của"},
      {"timestamp":"[02:12:48]","quote":"nó cứ nhịn dựa vào cái số lượng để nó"},
      {"timestamp":"[02:12:53]","quote":"của cái nào nhiều thì nó sẽ tích hợp vào"},
      {"timestamp":"[02:12:55]","quote":"cấu tạo màng."},
      {"timestamp":"[02:12:56]","quote":"Còn cái nào ít thì nó sẽ đẩy vào"},
      {"timestamp":"[02:12:59]","quote":"bên trong tiể để thực hiện đốt cháy."},
      {"timestamp":"[02:12:24]","quote":"ra năng lượng và sinh ra khí số 2 và"},
      {"timestamp":"[02:13:53]","quote":"bị viêm thì lại đi vào bên trong để chỉ"},
      {"timestamp":"[02:13:55]","quote":"thực hiện công việc đơn giản là đốt cháy"}
    ],
    "speaker": "Lecturer restating the mechanism in the established doctor-led exchange.",
    "class": "supported",
    "note": "Shared enzyme, similarity, quantity selection, membrane versus burning destinations and chỉ are present; no medical validation of the mechanism."
  },
  {
    "id": "c105",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Nếu chế độ ăn có quá nhiều Omega-6 (LA và AA) và ít Omega-3 (ALA, DHA), các chất LA và AA sẽ tích tụ trên màng tế bào và kích hoạt sản sinh chất gây viêm Prostaglandin E2 (PGE2) cùng nhiều yếu tố gây viêm khác.",
    "evidence": [
      {"timestamp":"[02:11:57]","quote":"nhiều la và ít ala"},
      {"timestamp":"[02:12:06]","quote":"enzyme nó phát tín hiệu là tiếp nhận LA"},
      {"timestamp":"[02:12:12]","quote":"mạng tế bào. Trong khi đấy là ALA vì số"},
      {"timestamp":"[02:13:12]","quote":"Nếu chúng ta ăn ít DHA và ăn nhiều AA"},
      {"timestamp":"[02:14:02]","quote":"thân này à ví dụ như alla hoặc aa này"},
      {"timestamp":"[02:14:22]","quote":"tình trạng viêm nữa thì không ổn. Na và"},
      {"timestamp":"[02:14:25]","quote":"AA khi mà nó tích hợp ở màng tế bào này"},
      {"timestamp":"[02:14:30]","quote":"kích hoạt để tạo lên cái chất viêm là PG"},
      {"timestamp":"[02:14:35]","quote":"E2."},
      {"timestamp":"[02:14:36]","quote":"PGE2 chính là Protagladin E2."},
      {"timestamp":"[02:14:52]","quote":"nó còn có những yếu tố gây viêm nữa. Một"},
      {"timestamp":"[02:14:59]","quote":"ra bởi những cái chất của Omega 6 này."},
      {"timestamp":"[02:15:23]","quote":"quá nhiều omega6"},
      {"timestamp":"[02:15:26]","quote":"thì la và AA sẽ tích hợp màng tế bào gây"}
    ],
    "speaker": "Lecturer's expressly hypothetical examples in the doctor-led segment; summary maintains the if-condition.",
    "class": "supported",
    "note": "SUPPORTED FLAG: summary merges two hypothetical pairs; later la và AA directly supports the central pair despite alla/Na ambiguity elsewhere. Do not silently replace those conflicting ASR forms. Prostaglandin is the summary spelling versus spoken Protagladin. Corrected draft timestamp [02:14:01] to [02:14:02]; independent semantic recheck recommended."
  },
  {
    "id": "c106",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Tình trạng này dẫn đến phản ứng đau, tăng tính thấm thành mạch, tăng tính thấm mô liên kết và gây ra nhiều bệnh lý:",
    "evidence": [
      {"timestamp":"[02:15:03]","quote":"Thì ngoài cái phản ứng viêm ra nó còn có"},
      {"timestamp":"[02:15:06]","quote":"những phản ứng đau, có những phản ứng"},
      {"timestamp":"[02:15:08]","quote":"tăng tính thấm thành mạch. có những phản"},
      {"timestamp":"[02:15:11]","quote":"ứng mà tăng tính thấm của mô liên kết"},
      {"timestamp":"[02:15:29]","quote":"viêm. Vậy thì nó sẽ gây viêm ở những cái"},
      {"timestamp":"[02:15:31]","quote":"nơi nào?"},
      {"timestamp":"[02:15:33]","quote":"rất rất nhiều trong cơ thể chúng ta nó"}
    ],
    "speaker": "Continuing lecturer explanation; summary introduces the ensuing disease list.",
    "class": "supported",
    "note": "All three reactions and many sites are explicit. Repaired the second distinct draft timestamp error: the viêm. Vậy thì quote belongs to [02:15:29], not [02:15:31]."
  },
  {
    "id": "c107",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Tại khớp: gây đau, dày bao hoạt dịch, tràn dịch ổ khớp, về lâu dài dẫn đến viêm khớp mãn tính và viêm khớp dạng thấp.",
    "evidence": [
      {"timestamp":"[02:15:40]","quote":"là viêm ở các khớp."},
      {"timestamp":"[02:16:15]","quote":"đau, gây đau đớn."},
      {"timestamp":"[02:16:37]","quote":"thì sẽ dày bao hoạt dịch lên và đi siêu"},
      {"timestamp":"[02:16:44]","quote":"dịch ổ khớp và tràn dịch ổ khớp nó thành"},
      {"timestamp":"[02:16:58]","quote":"thì cái quá trình viêm nó cứ lặp đi lặp"},
      {"timestamp":"[02:17:00]","quote":"lại cuối cùng nó trở thành từ viêm cấp"},
      {"timestamp":"[02:17:03]","quote":"tính chuyển thành viêm mãn tính và cuối"},
      {"timestamp":"[02:17:05]","quote":"cùng nó trở thành viêm khớp dạng thấp nó"}
    ],
    "speaker": "Lecturer explanation in the established doctor-led segment.",
    "class": "supported",
    "note": "Symptoms and repeated-inflammation progression match; chronic joint inflammation is a contextual paraphrase, not a medical correction."
  },
  {
    "id": "c108",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Tại gan, tụy, thận: gây tổn thương tế bào gan, gan nhiễm mỡ, rối loạn chuyển hóa mỡ máu, tiểu đường, viêm thận kẽ, viêm cầu thận, viêm ống thận, viêm thận tự miễn.",
    "evidence": [
      {"timestamp":"[02:17:34]","quote":"vào trong gan thì nó sẽ gây tổn thương"},
      {"timestamp":"[02:17:38]","quote":"tế bào gan, nó sẽ làm cho gan của chúng"},
      {"timestamp":"[02:17:41]","quote":"ta bị nhiễm mỡ."},
      {"timestamp":"[02:17:47]","quote":"loạn chuyển hóa của gan. Mà rối loạn"},
      {"timestamp":"[02:17:51]","quote":"tượng gì ạ? mỡ trong máu tăng lên."},
      {"timestamp":"[02:18:00]","quote":"tăng. Nó đi vào trong tụy thì sẽ gì ạ?"},
      {"timestamp":"[02:18:05]","quote":"hạn như là gì? Như là tiểu đường."},
      {"timestamp":"[02:18:13]","quote":"thận nó sẽ gây ra tổn thương của những"},
      {"timestamp":"[02:18:17]","quote":"viêm thận kẽ, viêm cẩu thận, viêm ống"},
      {"timestamp":"[02:18:20]","quote":"thận vân vân. Tất cả thậm chí là viêm"},
      {"timestamp":"[02:18:23]","quote":"thận tự miễn nó tấn công vào cái đường"}
    ],
    "speaker": "Lecturer's organ-by-organ explanation; no new named attribution in the summary item.",
    "class": "supported",
    "note": "List matches the spoken sequence. SUPPORTED FLAG: rối loạn chuyển hóa mỡ máu compresses liver metabolic disorder followed by raised blood lipids; source says cẩu, summary cầu. Recheck compression/spelling without external medical inference."
  },
  {
    "id": "c109",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Tại đường ruột: gây viêm dạ dày ruột, hội chứng ruột kích thích, rò rỉ ruột, trào ngược dạ dày thực quản, táo bón; khi đã tổn thương đường ruột thì 'rất dễ gây ra' tổn thương tuyến giáp (Hashimoto và Basedow), theo bác sĩ Phúc.",
    "evidence": [
      {"timestamp":"[02:18:25]","quote":"ruột của chúng ta nó sẽ gây ra viêm của"},
      {"timestamp":"[02:18:28]","quote":"dạ dày ruột nó sẽ gây ra hội chứng ruột"},
      {"timestamp":"[02:18:31]","quote":"Ruột kích thích."},
      {"timestamp":"[02:18:35]","quote":"giò rỉ ruột gây ra hội chứng gì nữa? Gây"},
      {"timestamp":"[02:18:37]","quote":"ra những tổn thương trào ngược dạ dày"},
      {"timestamp":"[02:18:40]","quote":"thực quản"},
      {"timestamp":"[02:18:41]","quote":"gây ra những các cái gì? Táo bón"},
      {"timestamp":"[02:18:50]","quote":"tổn thương đường ruột rất dễ gây ra tổn"},
      {"timestamp":"[02:18:52]","quote":"thương tiến giáp với hai bệnh là hai"},
      {"timestamp":"[02:18:56]","quote":"Hasimoto và ba đô."},
      {"timestamp":"[02:19:00]","quote":"Khánh lành phải nói thật nhanh lên nữa,"}
    ],
    "speaker": "Doctor-led quiz explanation, with interlocutor answers; the questioner explicitly addresses Khánh Lành. Individual fragments are not all assigned to one person.",
    "class": "supported",
    "note": "Condition and rất dễ gây ra are preserved. SUPPORTED FLAG: summary normalizes tiến giáp, Hasimoto, ba đô into tuyến giáp, Hashimoto, Basedow; those full spellings are not verbatim at these anchors. Independently recheck labels and the joint-exchange attribution, without assuming medical identity from outside the transcript."
  },
  {
    "id": "c110",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Các cơ quan khác: viêm loét mạch máu, thoái hóa chất trắng ở não, mờ mắt, đau mỏi cơ, viêm thần kinh, dị ứng da và bệnh lupus ban đỏ hệ thống.",
    "evidence": [
      {"timestamp":"[02:19:10]","quote":"viêm loét của mạch máu ra."},
      {"timestamp":"[02:19:14]","quote":"chúng ta đau mỏi cơ của thần kinh nó sẽ"},
      {"timestamp":"[02:19:16]","quote":"gây ra viêm thần kinh."},
      {"timestamp":"[02:19:17]","quote":"lên trên não nó sẽ gây ra thoái"},
      {"timestamp":"[02:19:19]","quote":"hóa chất trắng. Vào mắt nó sẽ gây ra"},
      {"timestamp":"[02:19:22]","quote":"chúng ta mắt nó mờ đi."},
      {"timestamp":"[02:29:35]","quote":"LA và AA nó sẽ trở nên rất nhiều. Chúng"},
      {"timestamp":"[02:30:12]","quote":"chẳng hạn như lú bút b đỏ hệ thống đúng"},
      {"timestamp":"[02:30:17]","quote":"chúng ta bị dự ứng ngoài da vô cùng"}
    ],
    "speaker": "Lecturer's organ list and later 20:1 explanation; summary combines those passages without a separate speaker label.",
    "class": "unresolved",
    "note": "First five effects and later skin-allergy wording have anchors in the same excess-LA/AA frame. RECHECK: lú bút b đỏ hệ thống is ambiguous ASR; supplied text does not unambiguously establish lupus ban đỏ hệ thống. Do not medically expand it. Also recheck relocation of the final two items from the later ratio discussion."
  },
  {
    "id": "c111",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Về tác dụng của từng axit béo, bác sĩ Phúc nói GLA chống viêm;",
    "evidence": [
      {"timestamp":"[02:01:20]","quote":"Là ờ GLA."},
      {"timestamp":"[02:01:23]","quote":"GL. Đúng rồi."},
      {"timestamp":"[02:10:35]","quote":"Thế và GL ở đây thì có tác dụng là cái"},
      {"timestamp":"[02:10:39]","quote":"này chống viêm."},
      {"timestamp":"[02:11:03]","quote":"đó có tác dụng là chống viêm. Đây tôi"},
      {"timestamp":"[02:11:06]","quote":"chỉ nói lấy một cái cái viêm thôi."}
    ],
    "speaker": "Continuing lecturer explanation in the doctor-led segment, retaining the single-effect discussion frame.",
    "class": "supported",
    "note": "SUPPORTED FLAG: local term is GL, but earlier explicit GLA immediately followed by GL confirmation gives an internal-text cross-reference; independently check this mapping, not external pharmacology."
  },
  {
    "id": "c112",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "CLA vừa chống viêm vừa chống ung thư; bác sĩ Phúc nói LA gây viêm còn ALA chống viêm;",
    "evidence": [
      {"timestamp":"[02:10:31]","quote":"la viêm còn Alla là chống viêm."},
      {"timestamp":"[02:10:43]","quote":"Thế còn thì CL thì có tác dụng vừa chống"},
      {"timestamp":"[02:10:47]","quote":"viêm vừa chống ung thư."},
      {"timestamp":"[02:10:50]","quote":"với lại ung thư. Còn cái Alla này thì nó"},
      {"timestamp":"[02:10:53]","quote":"lại gây viêm."},
      {"timestamp":"[02:10:56]","quote":"Đúng chưa ạ? Ala gây viêm."},
      {"timestamp":"[02:14:02]","quote":"thân này à ví dụ như alla hoặc aa này"},
      {"timestamp":"[02:14:10]","quote":"là nó gây viêm."}
    ],
    "speaker": "Continuing lecturer in the doctor-led discussion; no reliable individual identity is extracted from a marker.",
    "class": "unresolved",
    "note": "RECHECK: la/Alla/Ala directionality conflicts within the text, and CL is expanded to CLA in the summary. Keep the ambiguity; neither medical knowledge nor an ASR guess establishes the intended entities. Corrected repeated draft timestamp to [02:14:02]."
  },
  {
    "id": "c113",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "EPA và DHA có nhiều tác dụng, trong đó có chống viêm.",
    "evidence": [
      {"timestamp":"[02:10:59]","quote":"EPADHA này thì có nhiều tác dụng. Trong"},
      {"timestamp":"[02:11:03]","quote":"đó có tác dụng là chống viêm."},
      {"timestamp":"[02:11:12]","quote":"DHA cũng chống viêm."}
    ],
    "speaker": "Lecturer explanation; summary has no individual attribution in this sentence.",
    "class": "supported",
    "note": "Many-effects/among-them frame and anti-inflammatory statement match directly."
  },
  {
    "id": "c114",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Ông nói Omega-6 (như LA, AA) rất quan trọng và chỉ gây viêm khi quá nhiều, còn vừa phải thì không gây viêm, nên không thể cắt bỏ hoàn toàn Omega-6 mà chỉ cần giảm xuống.",
    "evidence": [
      {"timestamp":"[02:19:48]","quote":"chúng ta phải giảm những cái la giảm"},
      {"timestamp":"[02:19:50]","quote":"những cái AA này đi bằng cách là chúng"},
      {"timestamp":"[02:19:53]","quote":"ta phải giảm cái omega6 xuống. Nhưng mà"},
      {"timestamp":"[02:19:55]","quote":"tất cả những cái này nó lại rất quan"},
      {"timestamp":"[02:19:57]","quote":"trọng. Nó chỉ gây ra viêm khi nào? Khi"},
      {"timestamp":"[02:19:59]","quote":"mà nó quá nhiều."},
      {"timestamp":"[02:20:01]","quote":"Còn nếu như vừa phải thì nó không gây ra"},
      {"timestamp":"[02:20:03]","quote":"viêm."},
      {"timestamp":"[02:20:05]","quote":"Đúng rồi. Không cắt bỏ. Không thể cắt bỏ"},
      {"timestamp":"[02:20:07]","quote":"hoàn toàn được."}
    ],
    "speaker": "Doctor-led explanation followed by an interlocutor's elimination paraphrase and explicit confirmation; summary reports the confirmed position.",
    "class": "supported",
    "note": "Excess-versus-moderate condition preserved. SUPPORTED FLAG: những cái này is deictic; la/AA immediately precede it. Chỉ cần giảm is read as reduction versus elimination, not a new promise that reduction alone suffices for all outcomes."
  },
  {
    "id": "c115",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Để minh họa chuyện quá mức, bác sĩ Phúc cho rằng uống một chút rượu kích thích tiêu hóa, tinh thần và khí huyết lưu thông, nhưng uống quá nhiều thì ảnh hưởng sức khỏe.",
    "evidence": [
      {"timestamp":"[02:20:08]","quote":"Ví dụ như chúng ta đang nói là rượu là"},
      {"timestamp":"[02:20:12]","quote":"rượu rất tốt, rất hay. Chúng ta uống một"},
      {"timestamp":"[02:20:14]","quote":"chút rượu thôi thì nó sẽ kích thích hệ"},
      {"timestamp":"[02:20:17]","quote":"tiêu hóa, kích thích tinh thần, kích"},
      {"timestamp":"[02:20:18]","quote":"thích nhiều cái khí huyết lưu thông sẽ"},
      {"timestamp":"[02:20:20]","quote":"rất là tốt. Nhưng mà chúng ta uống rượu"},
      {"timestamp":"[02:20:22]","quote":"quá nhiều thì nó sẽ hỏng."},
      {"timestamp":"[02:20:24]","quote":"Nó sẽ ảnh hưởng tới sức khỏe."},
      {"timestamp":"[02:20:33]","quote":"Đấy lý do tôi nói lại là quý vị cần phải"}
    ],
    "speaker": "Local speaker not explicitly named. Summary attributes the analogy to bác sĩ Phúc; continuity and ASR turn markers alone do not establish who supplied it.",
    "class": "unresolved",
    "note": "RECHECK: analogy content, small-amount condition and excessive-amount consequence are present, but named attribution remains uncertain. No speaker identity is inferred to resolve it."
  },
  {
    "id": "c116",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Bác sĩ Phúc nói tỷ lệ Omega-6/Omega-3 lý tưởng là 1:1.",
    "evidence": [
      {"timestamp":"[02:23:56]","quote":"Thì chúng ta có ba cái loại, ba cái nhóm"},
      {"timestamp":"[02:23:58]","quote":"Omega. Omega 3 là 1, omega 6 là 2 và"},
      {"timestamp":"[02:24:03]","quote":"Omega9 là 3."},
      {"timestamp":"[02:24:06]","quote":"cái omega này thì tốt nhất là những"},
      {"timestamp":"[02:24:09]","quote":"thành phần trong đó."},
      {"timestamp":"[02:24:34]","quote":"nếu như mà cái tỉ lệ lý tưởng nhất thì"},
      {"timestamp":"[02:24:37]","quote":"những cái này đem chia cho nhau nó đều"},
      {"timestamp":"[02:24:38]","quote":"là 1/1."},
      {"timestamp":"[02:28:34]","quote":"vàng là tất cả những cái này chia cho"},
      {"timestamp":"[02:28:36]","quote":"nhau một cách hợp lý và tốt nhất là tỉ"},
      {"timestamp":"[02:28:39]","quote":"lệ 1 chia 1 đúng không ạ? Tỷ lệ 1 chia 1"}
    ],
    "speaker": "Lecturer in the established doctor-led ratio discussion; summary assigns the statement to bác sĩ Phúc, not the earlier article reader.",
    "class": "unresolved",
    "note": "RECHECK: ideal 1:1 is explicit, but referent is những cái này after three groups and their components, not an explicit group-total Omega-6/Omega-3 fraction. Earlier article's explicit fraction cannot establish the doctor's identical scope. Keep deictic scope ambiguous rather than authorize summary compression."
  },
  {
    "id": "c117",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Ông dẫn lời một số nghiên cứu/tài liệu rằng 4:1 được chấp nhận, cùng lắm 5:1; đồng thời nhận xét 5:1 đã quá nhiều và khuyên không để tỷ lệ lên tới 4 hoặc 5:1.",
    "evidence": [
      {"timestamp":"[02:28:43]","quote":"tỷ lệ chấp nhận được đến đâu? Có những"},
      {"timestamp":"[02:28:45]","quote":"nghiên cứu và những tài liệu nói rằng"},
      {"timestamp":"[02:28:47]","quote":"chấp nhận được tỉ lệ những cái này đem"},
      {"timestamp":"[02:28:49]","quote":"chia ra thì là 4 chia 1 thì được. Cùng"},
      {"timestamp":"[02:28:53]","quote":"lắm là đến 5 chia 1. 5 chia 1 thì đã là"},
      {"timestamp":"[02:28:56]","quote":"quá nhiều rồi."},
      {"timestamp":"[02:34:29]","quote":"ăn đừng để cho cái tỉ lệ nó vượt quá con"},
      {"timestamp":"[02:34:32]","quote":"số 4 chứ con số năm là tôi không tin"},
      {"timestamp":"[02:35:41]","quote":"Thì tôi cho rằng là cái tỉ lệ mà Khánh"},
      {"timestamp":"[02:35:43]","quote":"lành đặt ra cái câu hỏi với tôi là tỉ lệ"},
      {"timestamp":"[02:35:48]","quote":"rằng là chúng ta đừng có để cái tỉ lệ"},
      {"timestamp":"[02:35:50]","quote":"lên tới 4 hay 5/ên1 cái này là không ổn"}
    ],
    "speaker": "Lecturer responding to Khánh Lành's question, distinguishing cited studies/documents from his own judgement.",
    "class": "supported",
    "note": "Numbers and source-versus-own position preserved. SUPPORTED FLAG: boundary of cited material at cùng lắm is not explicit; also vượt quá 4 differs from later lên tới 4, which the summary follows. No conflict is silently harmonized."
  },
  {
    "id": "c118",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Tuy nhiên, bác sĩ Phúc nói các nghiên cứu ở Mỹ và châu Âu thấy các thành phần này trong khẩu phần, đem chia cho DHA hoặc EPA, có tỷ lệ tới 20:1, khiến các dưỡng chất quý như EPA và DHA bị hòa loãng, không còn ý nghĩa.",
    "evidence": [
      {"timestamp":"[02:29:03]","quote":"nghiên cứu đến bây giờ phút này, đặc"},
      {"timestamp":"[02:29:06]","quote":"biệt là ở Mỹ hay là quốc các quốc gia"},
      {"timestamp":"[02:29:08]","quote":"Châu Âu người ta thấy rằng chúng ta đang"},
      {"timestamp":"[02:29:10]","quote":"ăn những thành phần này đem chia cho DHA"},
      {"timestamp":"[02:29:13]","quote":"hoặc epa là tỉ lệ 20 chia 1."},
      {"timestamp":"[02:29:20]","quote":"nhận thấy rằng toàn bộ những vàng này nó"},
      {"timestamp":"[02:29:23]","quote":"sẽ bị hòa loãng ra vô nghĩa rồi."},
      {"timestamp":"[02:29:25]","quote":"Chả còn ý nghĩa gì nữa cả. Nó cũng không"},
      {"timestamp":"[02:29:28]","quote":"đưa được lên trên mắt, không đưa được"},
      {"timestamp":"[02:29:29]","quote":"lên trên não, không đưa được vào tim."}
    ],
    "speaker": "Continuing lecturer reporting research; summary keeps bác sĩ Phúc nói rather than presenting independent scientific validation.",
    "class": "supported",
    "note": "20:1, alternative DHA/EPA denominators and dilution match. SUPPORTED FLAG: numerator remains deictic in both texts; vàng metaphor is rendered as EPA/DHA. Do not replace this with a group-total fraction or external study identification."
  },
  {
    "id": "c119",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Khi nói về tỷ lệ 20:1, bác sĩ Phúc còn nêu 'sơ vữa mạch máu', 'Anzimer', 'bakis' và các bệnh tự miễn như những hệ quả mà ông quy cho chế độ ăn mất cân bằng.",
    "evidence": [
      {"timestamp":"[02:29:42]","quote":"rất nhiều. Và đấy chính là nguyên nhân"},
      {"timestamp":"[02:29:52]","quote":"mỡ nhiều, bị sơ vữa mạch máu nhiều, bị"},
      {"timestamp":"[02:29:55]","quote":"Anzimer nhiều, bị bakis nhiều, bị mắt mờ"},
      {"timestamp":"[02:30:00]","quote":"không ạ? bị những cái bệnh tự miễn nhiều"},
      {"timestamp":"[02:30:24]","quote":"nhiều vì chế độ ăn uống của chúng ta mất"},
      {"timestamp":"[02:30:25]","quote":"cân bằng"}
    ],
    "speaker": "Lecturer continuing the 20:1 discussion; summary explicitly frames causation as his attribution.",
    "class": "supported",
    "note": "Spoken/ASR labels are preserved literally, not converted to inferred medical diagnoses; causal attribution and imbalance context match."
  },
  {
    "id": "c120",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Bác sĩ Phúc nói LA (Omega-6) chủ yếu dành cho các tạng địa phương ([02:25:04](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=8704s)).",
    "evidence": [
      {"timestamp":"[02:24:11]","quote":"3 là đứng đầu là cái gì ạ? ALA đúng"},
      {"timestamp":"[02:24:21]","quote":"Thế còn bên này là gì ạ? La"},
      {"timestamp":"[02:25:01]","quote":"Epa thì là của gì ạ?"},
      {"timestamp":"[02:25:03]","quote":"Của tim."},
      {"timestamp":"[02:25:04]","quote":"La thì dành cho các cái tạng địa phương"},
      {"timestamp":"[02:25:06]","quote":"là chính. Đồng ý không ạ?"},
      {"timestamp":"[02:25:09]","quote":"Thế và những cái này dành cho các cái"},
      {"timestamp":"[02:25:11]","quote":"tạng địa phương."},
      {"timestamp":"[02:26:39]","quote":"La nó có từ đâu ạ?"},
      {"timestamp":"[02:26:40]","quote":"Ala chủ yếu có từ"},
      {"timestamp":"[02:26:47]","quote":"thực dầu thực vật thì nó chính là ALA,"}
    ],
    "speaker": "Lecturer/questioner in the established doctor-led exchange; summary assigns the statement to bác sĩ Phúc.",
    "class": "unresolved",
    "note": "RECHECK: location and mainly-local-organs wording match exactly, but La's identity does not. The same rendering appears in Omega-6 listing and in a question answered as Ala/ALA; its position after DHA/Epa and before a second deictic group does not settle LA (Omega-6). Keep ambiguous, without chemical or speaker-identity inference."
  }
]
```

## Validation and process boundary

Validation protocol: `PYTHONDONTWRITEBYTECODE=1 python3`, in-memory only. Check exactly c091–c120 in order and once each; exact section/claim strings against extraction; seven required fields and allowed classes; every evidence quote as a literal substring of an actual transcript line beginning with its timestamp (including repeated timestamps); summary and transcript hashes unchanged. Saved-artifact result: PASS — 30/30 exact IDs, claims and sections; seven-field schema and classes valid; 270/270 timestamp-line quotes match literally, zero failures; summary and transcript hashes unchanged. Counts recomputed as 23 supported and 7 unresolved. Mechanical validity does not prove semantic support. Parent must independently validate the saved artifact and recheck non-supported and flagged supported items before adjudication.

Only this new artifact was written by this child. Original draft, completed batches, continuation, videos, review/progress, deferred-work, tools and publication state were not edited. No scratch files, temporary scripts, nested agents, medical corrections, commits, pushes, deletions, migration, provider fallback or retry loops. No 429 occurred in this child. Historical scratch/runtime-location disclosures in continuation were read, not removed or represented as this child's actions. No process violation by this child is known; harness-managed infrastructure was not inspected.
