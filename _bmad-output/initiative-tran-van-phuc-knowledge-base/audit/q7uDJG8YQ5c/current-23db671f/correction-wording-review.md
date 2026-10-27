# Independent literal correction-wording review — q7uDJG8YQ5c, current summary 23db671f

**Status: model advisory review only. All 20 proposals remain `pending-human-approval`.** A model `approve` means only that this reviewer found the exact proposed wording faithful to the current transcript. It is not human approval, it does not apply anything, and publication stays **blocked**. `proposed-corrections.md` and every earlier audit classification are unchanged. This file is the only one written.

## Binding and verification

- Summary `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/summary.md` SHA-256 `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64`: match.
- Transcript SHA-256 `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`: match.
- review.md `5f588b23…a41`, metadata.json `c3f19953…dcd` and `scripts/fidelity.py` (extractor) `cc570d0b…da0d` match `input-manifest.json`. I checked them before reading and again after writing (see Validation).
- Contract read: `spec-summary-source-audit.md`, `audit-record-format.md`. I read these for scope only, as opinions and not as semantic proof: `continuation.md`, `input-manifest.json`, `proposed-corrections.md` (in full) and targeted parts of `adjudication-recommendations.md` and `omissions.md`.

## Full-reading attestation

I read the full current summary (lines 1–264) and the full transcript (lines 1–5331, `[00:00:01]`–`[03:32:39]`) in order, in bounded Read-tool chunks with no gaps: 1–830, 831–1659, 1660–2509, 2510–3359, 3360–4209, 4210–5059, 5060–5331. I judged each proposal against the whole transcript, not only against its supplied anchor quotes. The only semantic evidence used is the current summary and transcript. I used no historical review verdicts, no outside knowledge, no medical correction and no inferred identity, and I did not rely on `>>` turn markers alone.

## Counts

- 20 proposals reviewed (p001–p020): **18 approve**, **2 reject** (p004, p020).
- All 20 records keep status `pending-human-approval`.
- The two rejection replacements are this reviewer's candidate alternatives for the next round. **They have not received any independent review.**

## Substantive findings

- **p004 / c024 — reject.** The prognosis-not-outcome fix is right. But the proposal sets the relative's words "tại bữa cơm chia tay". The transcript places those words at a hospital visit, where he says he wants to *invite* the doctor to a farewell meal: [00:40:33] "ấy xuống gặp tôi ở bệnh viện. Anh ấy nói" / [00:40:36] "rằng anh muốn mời chú đi ăn một bữa cơm". The setting is a new, unsupported fact. The replacement keeps the prognosis framing and the quoted prospective words, and puts the speech at the hospital visit.
- **p020 / o001 (optional) — reject.** The spoken wording "tìm đến để tìm hiểu" is correct. But "khiến chính người chia sẻ phải tiếp tục học hỏi, hoàn thiện" turns a first-person statement ([00:22:08]–[00:22:12] "bản thân tôi phải hoàn thiện, bản thân tôi phải học hỏi hơn nữa") into a general rule about anyone who shares. The replacement keeps it as his own statement.
- The other 18 were approved after a clause-by-clause check. Points the operator flagged:
  - **c030:** the literal "bác sĩ Quang" is kept; surgery practice is spoken ("tôi làm ngoại khoa").
  - **c051/c076:** the stronger wording appears only inside quotation, as reported speech, and is verbatim.
  - **c092/c112:** ASR tokens are left unresolved and an audio check is recommended.
  - **c115/c175/c208:** speakers whose identity the transcript does not establish are not named; c208 keeps "tôi nghĩ rằng".
  - **c010/c016/c064/c165:** the canonical-name changes stay within the bounded scope. The withdrawal condition still applies if a canonical-expansion policy is adopted.
- Minor non-blocking observations on approved items:
  - p014: "ngay sau đó" spans about 20 s, with GL and CL statements in between.
  - p019: "lời đáp tiếp theo" groups lines that carry several `>>` markers, but it explicitly names no speaker.

## Records (20)

```json
[
  {
    "id": "p001",
    "claim_id": "c010",
    "proposed_text": "Nhà toán học người Đức mà transcript ghi là \"Golden\" cũng phát biểu Định lý bất toàn năm 1931 minh chứng thế giới tự nhiên và khả năng con người chứa đựng vô vàn điều vô hạn.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[00:28:39]", "quote": "bất toàn là của nhà toán học người Đức"},
      {"timestamp": "[00:28:42]", "quote": "Golden."},
      {"timestamp": "[00:28:44]", "quote": "Phát biểu năm 1931."},
      {"timestamp": "[00:31:01]", "quote": "tự nhiên là vô hạn, khả năng con người"},
      {"timestamp": "[00:31:26]", "quote": "đó nó thể hiện rằng thế giới tự nhiên"},
      {"timestamp": "[00:31:29]", "quote": "của chúng ta có rất nhiều cái vô hạn."}
    ],
    "rationale": "The only change removes the unspoken given name and renders the spoken surname literally. Nationality ('người Đức'), year (1931) and the infinity content are spoken and unchanged. No identity is inferred and no historical correction is made. In scope under the bounded canonical-name policy.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p002",
    "claim_id": "c012",
    "proposed_text": "Bác sĩ Phúc cho rằng ngay cả bệnh nhân mắc căn bệnh ung thư, tưởng như đã đi tới cửa tử, nếu hiểu được cuộc sống, biết điều chỉnh lại lối sống, biết buông bỏ, bổ sung ít nhất 7 vi chất, sống khoa học, lạc quan và thực hành lối sống tích cực thì hoàn toàn có thể thoát khỏi căn bệnh ung thư.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[00:27:26]", "quote": "nhân có thể là mắc căn bệnh ung thư"},
      {"timestamp": "[00:27:29]", "quote": "tưởng là chúng ta đi tới cửa tử"},
      {"timestamp": "[00:27:34]", "quote": "đó hiểu được cuộc sống."},
      {"timestamp": "[00:27:36]", "quote": "biết bình chỉnh lại cái lối sống của"},
      {"timestamp": "[00:27:38]", "quote": "mình, biết buông bỏ, biết bổ sung đủ vi"},
      {"timestamp": "[00:27:40]", "quote": "chất, biết sống một cuộc sống khoa học"},
      {"timestamp": "[00:27:42]", "quote": "và lạc quan. Tất cả những điều đó tôi đã"},
      {"timestamp": "[00:27:48]", "quote": "nhất bảy vi chất, chúng ta sống tốt,"},
      {"timestamp": "[00:27:50]", "quote": "thực hành mọi lối sống tích cực và khoa"},
      {"timestamp": "[00:27:52]", "quote": "học thì người đó hoàn toàn có thể thoát"},
      {"timestamp": "[00:27:54]", "quote": "khỏi căn bệnh ung thư."}
    ],
    "rationale": "Every condition is spoken: understanding life, adjusting lifestyle, letting go, at least seven micronutrients, a scientific and optimistic life, positive practice. 'hoàn toàn có thể' and the outcome scoped to 'căn bệnh ung thư' are verbatim. The speaker is the doctor in an unbroken monologue ('tôi đã nói nhiều trong các số rồi'), so 'Bác sĩ Phúc cho rằng' is supported attribution and does not harden the claim. The illustrative 'có thể là mắc' becomes a plain example subject without changing the claim. Omitting 'chúng ta sống tốt' loses no condition.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p003",
    "claim_id": "c016",
    "proposed_text": "Mozart (transcript ghi \"Moa\", \"Moza\"): Chỉ sống 35 năm nhưng đã để lại 22 vở opera (như vở \"Cây sáo thần\"), 41 bản giao hưởng và 42 bản concerto.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[00:44:38]", "quote": "hạn như nhà nhạc sĩ thiên tài Moa chẳng"},
      {"timestamp": "[00:44:46]", "quote": "về chiều dài về tuổi thọ thì Moa có 35"},
      {"timestamp": "[00:44:55]", "quote": "22 vở Ober."},
      {"timestamp": "[00:45:02]", "quote": "ví dụ cây sáo thần của Moza thì quá hay."},
      {"timestamp": "[00:45:25]", "quote": "Ví dụ như là 41 bản giao"},
      {"timestamp": "[00:45:37]", "quote": "42 bản công sexo."},
      {"timestamp": "[00:46:24]", "quote": "ngắn ngủi 56 năm moza có 35 năm rõ ràng"}
    ],
    "rationale": "Removes the unspoken given names and shows the spoken forms. 35 years, 22 operas, 'Cây sáo thần', 41 symphonies and 42 concertos are spoken as given; the phonetic normalizations (Ober→opera, công sexo→concerto) were already accepted. No new facts. In scope under the bounded canonical-name policy.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p004",
    "claim_id": "c024",
    "proposed_text": "(Ví dụ bác sĩ Phúc kể để cho thấy chiều rộng cuộc sống (W) quan trọng hơn chiều dài: một người anh họ bác sĩ bị ung thư dạ dày giai đoạn cuối, đã được phẫu thuật nhưng được xác định thời gian sống chỉ hữu hạn, khoảng hơn năm trời, 'năm rưỡi là cùng'; nhờ tập trung lo liệu chu toàn cho gia đình nên theo lời bác sĩ, tại bữa cơm chia tay ông anh nói thấy trong khoảng thời gian 'hơn năm trời' đó mình làm được nhiều việc nhất trong cuộc đời và 'đến bây giờ anh ra đi anh thanh thản').",
    "verdict": "reject",
    "evidence": [
      {"timestamp": "[00:38:37]", "quote": "kéo dài được cuộc sống ngoài cái là phẫu"},
      {"timestamp": "[00:38:38]", "quote": "thuật cho anh ấy. Tức là phẫu thuật lấy"},
      {"timestamp": "[00:38:45]", "quote": "cái giai đoạn cuối. Thế thành ra là xác"},
      {"timestamp": "[00:38:48]", "quote": "định cái thời gian sống của anh ấy chỉ"},
      {"timestamp": "[00:38:51]", "quote": "hữu hạn thôi. Tức là ngắn trong vòng cơ"},
      {"timestamp": "[00:38:53]", "quote": "độ hơn năm trời, năm rưỡi là cùng."},
      {"timestamp": "[00:40:31]", "quote": "công việc xong xuôi đâu đấy rồi thì anh"},
      {"timestamp": "[00:40:33]", "quote": "ấy xuống gặp tôi ở bệnh viện. Anh ấy nói"},
      {"timestamp": "[00:40:36]", "quote": "rằng anh muốn mời chú đi ăn một bữa cơm"},
      {"timestamp": "[00:40:38]", "quote": "chia tay và anh đã lo anh đã chuẩn bị"},
      {"timestamp": "[00:40:45]", "quote": "tất cả mọi thứ và đến bây giờ anh ra đi"},
      {"timestamp": "[00:40:48]", "quote": "anh thanh thản"},
      {"timestamp": "[00:40:52]", "quote": "hơn năm trời thôi nhưng mà anh thấy anh"},
      {"timestamp": "[00:40:54]", "quote": "làm được nhiều việc nhất trong cuộc đời"}
    ],
    "rationale": "The prognosis-not-outcome correction is right: the source gives only a prognosis ('xác định cái thời gian sống ... hơn năm trời, năm rưỡi là cùng') and never narrates his death or total survival. The surgery, terminal stage and quoted prospective 'ra đi ... thanh thản' are supported. One clause adds an unsupported fact. 'tại bữa cơm chia tay ông anh nói' places the speech AT the farewell meal, but the transcript says he came to see the doctor at the hospital and said he wanted to invite him to a farewell meal ('xuống gặp tôi ở bệnh viện. Anh ấy nói rằng anh muốn mời chú đi ăn một bữa cơm chia tay'). The meal itself is never narrated. The replacement fixes only that setting and keeps every other element.",
    "replacement_text": "(Ví dụ bác sĩ Phúc kể để cho thấy chiều rộng cuộc sống (W) quan trọng hơn chiều dài: một người anh họ bác sĩ bị ung thư dạ dày giai đoạn cuối, đã được phẫu thuật nhưng được xác định thời gian sống chỉ hữu hạn, khoảng hơn năm trời, 'năm rưỡi là cùng'; nhờ tập trung lo liệu chu toàn cho gia đình nên theo lời bác sĩ, khi xuống bệnh viện gặp bác sĩ và nói muốn mời 'đi ăn một bữa cơm chia tay', ông anh nói 'đến bây giờ anh ra đi anh thanh thản' và thấy trong khoảng thời gian 'hơn năm trời' đó mình làm được nhiều việc nhất trong cuộc đời).",
    "status": "pending-human-approval"
  },
  {
    "id": "p005",
    "claim_id": "c030",
    "proposed_text": "Bác sĩ chia sẻ trải nghiệm cá nhân: ban đầu mơ trở thành bác sĩ y học cổ truyền, rồi mơ trở thành bác sĩ sản khoa, sau đó thích ngoại khoa và đã làm ngoại khoa, nhưng cuối cùng thấy làm \"bác sĩ Quang\" (cách ghi trong transcript) là phù hợp nhất, với công việc làm cho các hình ảnh đen trắng trên phim X-quang, siêu âm, CT, cộng hưởng từ \"cất lên tiếng nói\" để cứu giúp bệnh nhân.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[00:09:42]", "quote": "Lúc đấy tôi trở thành bác"},
      {"timestamp": "[00:09:45]", "quote": "sĩ ngoài khoa."},
      {"timestamp": "[00:54:42]", "quote": "mơ trở thành bác sĩ về y học cổ truyền."},
      {"timestamp": "[00:54:48]", "quote": "đó thì tôi lại mơ trở thành bác sĩ sản"},
      {"timestamp": "[00:54:53]", "quote": "Tôi lại thích ngoại khoa, tôi"},
      {"timestamp": "[00:54:54]", "quote": "làm ngoại khoa. Xong cuối cùng tôi mới"},
      {"timestamp": "[00:54:56]", "quote": "thấy hóa ra làm bác sĩ Quang là phù hợp"},
      {"timestamp": "[00:55:04]", "quote": "cho những cái hình ảnh đen trắng trên"},
      {"timestamp": "[00:55:06]", "quote": "phim X Quang hay trên siêu âm hay trên"},
      {"timestamp": "[00:55:10]", "quote": "trắng đó nó cất lên tiếng nói"},
      {"timestamp": "[00:55:19]", "quote": "trắng đó để mà cứu giúp những cái bệnh"},
      {"timestamp": "[00:55:48]", "quote": "trở lại tôi làm bác sĩ Quang."}
    ],
    "rationale": "Each stage in the sequence is spoken: dream of traditional medicine, dream of obstetrics, liking and practising surgery, then finding 'bác sĩ Quang' most suitable. The role label is kept literally, with no reconstructed title or career. The modalities and 'cất lên tiếng nói' purpose are verbatim ('cộng ngẩng từ' to 'cộng hưởng từ' is an accepted normalization). 'để cứu giúp bệnh nhân' shortens 'bệnh nhân đang ở bên bờ của vực thẳm' without changing meaning.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p006",
    "claim_id": "c047",
    "proposed_text": "Trước một công việc, năng lực thể hiện khả năng làm được, động lực quyết định những gì sẽ làm, nhưng chính thái độ mới quyết định kết quả làm tốt hay không tốt và dẫn đến thành công hay thất bại.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:15:55]", "quote": "cũng xin phép là trích lại nguyên văn."},
      {"timestamp": "[01:15:57]", "quote": "Trước một công việc cụ thể, năng lực thể"},
      {"timestamp": "[01:16:01]", "quote": "hiện khả năng bạn có thể làm được. Động"},
      {"timestamp": "[01:16:04]", "quote": "lực quyết định những gì bạn làm nhưng"},
      {"timestamp": "[01:16:07]", "quote": "chỉ có thái độ mới tạo nên kết quả làm"},
      {"timestamp": "[01:16:10]", "quote": "tốt hay là không tốt."},
      {"timestamp": "[01:19:02]", "quote": "thái độ mới quyết định được rằng là"},
      {"timestamp": "[01:19:04]", "quote": "chúng ta thành công hay thất bại."}
    ],
    "rationale": "Deleting 'nghiêm túc, tích cực' brings the sentence back to the maxim read verbatim, where attitude itself decides good or bad results, and to the doctor's restatement that attitude decides success or failure. Minimal deletion; no new content.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p007",
    "claim_id": "c051",
    "proposed_text": "Bác sĩ Phúc nói rằng với những cơn đau thể xác không giải thích được nguyên nhân dù đã đi khắp nơi chữa đủ thứ thuốc, sau khi đưa vitamin D lên ngưỡng lý tưởng và bổ sung các vi chất đúng và đủ thì, theo lời ông, \"tự dưng những cái cơn đau về thể xác đấy hết\", còn cơn đau về mặt tinh thần \"cũng giảm đi rất rất nhiều\" và ông nói \"có thể nói rằng là thậm chí\" không còn cơn đau về mặt tinh thần (đây là lời kể của bác sĩ Phúc trong video).",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:25:18]", "quote": "Đây là cái tôi ví rằng nó là thuốc giảm"},
      {"timestamp": "[01:25:25]", "quote": "đau đớn về mặt thể xác bao gồm đau xương"},
      {"timestamp": "[01:25:35]", "quote": "mà không giải thích được nguyên nhân tại"},
      {"timestamp": "[01:25:37]", "quote": "sao, đi khắp các cái nơi chữa đủ thứ"},
      {"timestamp": "[01:25:43]", "quote": "khi chúng ta đưa được vitamin D lên"},
      {"timestamp": "[01:25:45]", "quote": "ngưỡng lý tưởng, chúng ta bổ sung các"},
      {"timestamp": "[01:25:47]", "quote": "cái vi chất đúng và đủ thì tự dưng những"},
      {"timestamp": "[01:25:50]", "quote": "cái cơn đau về thể xác đấy hết."},
      {"timestamp": "[01:25:57]", "quote": "Cơn đau về mặt tinh thần nó cũng giảm đi"},
      {"timestamp": "[01:25:59]", "quote": "rất rất nhiều và có thể nói rằng là thậm"},
      {"timestamp": "[01:26:02]", "quote": "chí chúng ta không có cơn đau vào mặt"},
      {"timestamp": "[01:26:28]", "quote": "nói rằng vitamin D, vitamin D, mag và gì"}
    ],
    "rationale": "The stronger outcome wording appears only inside quotation marks, under explicit reported-speech framing ('theo lời ông', 'lời kể của bác sĩ Phúc'). Every quoted fragment is verbatim (some join adjacent caption lines). Both conditions, ideal vitamin D and correct and sufficient micronutrients, are kept. The 'không giải thích được nguyên nhân ... đi khắp các cái nơi chữa đủ thứ thuốc' scope is spoken. The concessive 'dù' reflects the spoken 'Nhưng mà sau khi'. 'có thể nói rằng' stays attached only to the 'thậm chí' clause, as spoken. Attribution to the doctor follows the continuous first-person passage ('tôi ví', 'tôi có thể nói'). No advice or endorsement is added.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p008",
    "claim_id": "c052",
    "proposed_text": "Ông gọi bộ ba Canxi, Magiê và Vitamin D là một loại “thuốc giảm đau tự nhiên rất thần kỳ”, và nêu các ví dụ về đau xương khớp, dạ dày, đại tràng, trầm cảm, căng thẳng và bế tắc.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:25:05]", "quote": "hôm trước tôi có nói rằng canxi, ma và"},
      {"timestamp": "[01:25:10]", "quote": "vitamin D nó là cái bộ ba gì Khánh Lành?"},
      {"timestamp": "[01:25:18]", "quote": "Đây là cái tôi ví rằng nó là thuốc giảm"},
      {"timestamp": "[01:25:21]", "quote": "đau tự nhiên rất thần kỳ."},
      {"timestamp": "[01:25:28]", "quote": "khớp khớp, đau khắp cơ thể, đau dạ dày"},
      {"timestamp": "[01:25:33]", "quote": "ruột, đau đại tràng, đau đủ các cái nơi"},
      {"timestamp": "[01:26:05]", "quote": "Những người đang bị trầm cảm, những"},
      {"timestamp": "[01:26:07]", "quote": "người đang bị căng thẳng, những người"},
      {"timestamp": "[01:26:14]", "quote": "cuộc sống rơi vào bế tắc thì tự dưng tất"},
      {"timestamp": "[01:26:37]", "quote": "giảm đau tự nhiên rất thần kỳ mà không"}
    ],
    "rationale": "When he names the trio he says 'vitamin D' each time, and the label inside the quotation marks is now verbatim with 'rất'. The examples are all spoken. 'Magiê' for 'ma'/'mag' is an accepted normalization. Nothing is added.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p009",
    "claim_id": "c064",
    "proposed_text": "Năm 1985 tại vùng biển Caribe, nhà sinh học người Mỹ Lipton (transcript ghi \"Trà Lip Tông\", \"Liptông\") trong quá trình soạn giáo án đã phát hiện ra các đặc tính của màng tế bào:",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:34:56]", "quote": "quan niệm này được một nhà sinh học thay"},
      {"timestamp": "[01:35:05]", "quote": "học người Mỹ,"},
      {"timestamp": "[01:35:13]", "quote": "Trà Lip Tông."},
      {"timestamp": "[01:35:30]", "quote": "biển Caribe"},
      {"timestamp": "[01:35:33]", "quote": "vào năm 1985"},
      {"timestamp": "[01:35:50]", "quote": "quá trình soạn giáo án thì ông soạn cấu"},
      {"timestamp": "[01:46:42]", "quote": "nhà khoa học, nhà sinh học Liptông tìm"}
    ],
    "rationale": "Only the unspoken given name is removed and the spoken forms are shown. Biologist, American, Caribbean, 1985 and lesson preparation are all spoken. No identity judgement. The heading and question strings that contain 'Bruce' stay a separate human decision, outside this claim.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p010",
    "claim_id": "c065",
    "proposed_text": "Màng tế bào gồm hai lớp phospholipid với đầu ưa nước quay ra ngoài/vào trong và đuôi kỵ nước giấu ở giữa, được sắp xếp trật tự theo dạng \"tinh thể màng\".",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:36:02]", "quote": "màng tế bào chúng ta biết rồi nó có hai"},
      {"timestamp": "[01:36:20]", "quote": "đầu phospho lipit."},
      {"timestamp": "[01:37:16]", "quote": "trong tế bào và toàn bộ cái phần kỵ nước"},
      {"timestamp": "[01:37:18]", "quote": "thì nó được giấu ở bên trong."},
      {"timestamp": "[01:38:06]", "quote": "sắp xếp xung quanh theo một cái trật tự"},
      {"timestamp": "[01:38:41]", "quote": "những tinh thể cứng nhưng mà chúng ta"},
      {"timestamp": "[01:38:43]", "quote": "lại có tinh thể lỏng."},
      {"timestamp": "[01:39:01]", "quote": "Thế thì ông nảy sinh ra một"},
      {"timestamp": "[01:39:03]", "quote": "cái đây là tinh thể màng."}
    ],
    "rationale": "Removes a likeness to liquid crystal that is never asserted. Liquid crystal is listed as a crystal type before 'tinh thể màng' is named, and he says only that the membrane is 'cũng là một cái dạng tinh thể'. Deletion only; the remaining clauses are unchanged.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p011",
    "claim_id": "c068",
    "proposed_text": "Năm 1985, nhà sinh học Liptông nhận thấy màng tế bào gồm các lớp chất béo sắp xếp theo trật tự, có các cửa và kênh dẫn (như kênh natri, kali, protein, chất béo) dẫn các chất vào và ra khỏi tế bào; từ đó, các nhà khoa học (transcript ghi \"Chính lông cũng như là các nhà khoa học khác\") bắt đầu đi vào nghiên cứu và thấy màng tế bào được cấu tạo bởi protein và các chất béo.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:37:56]", "quote": "hai cái hai cái chuỗi chất béo này."},
      {"timestamp": "[01:38:06]", "quote": "sắp xếp xung quanh theo một cái trật tự"},
      {"timestamp": "[01:42:53]", "quote": "những kênh ví dụ kênh kali, kênh natri,"},
      {"timestamp": "[01:42:56]", "quote": "kênh protein, kênh"},
      {"timestamp": "[01:42:58]", "quote": "chất béo để dẫn các cái chất đi vào"},
      {"timestamp": "[01:46:35]", "quote": "đầu từ năm 1985"},
      {"timestamp": "[01:46:44]", "quote": "ra được cái nguyên lý này. Từ đấy bắt"},
      {"timestamp": "[01:46:50]", "quote": "Chính lông cũng như là các nhà khoa học"},
      {"timestamp": "[01:46:52]", "quote": "khác bắt đầu đi vào nghiên cứu thì người"},
      {"timestamp": "[01:47:06]", "quote": "gì? Nó được cấu tạo bởi protein, được"},
      {"timestamp": "[01:47:09]", "quote": "cấu tạo bởi các chất béo."}
    ],
    "rationale": "Restores the two spoken stages: the 1985 insight (ordered fat layers, gates and channels), then later research ('Từ đấy bắt đầu') finding protein-plus-fat composition. The ASR token 'Chính lông' is kept literally inside quotation and not resolved to a person. All channel examples are spoken.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p012",
    "claim_id": "c076",
    "proposed_text": "Trả lời câu hỏi của khán giả, ông nói rằng \"nếu cá đó có nhiều DHA thì chúng ta ăn sẽ thông minh\" và mắt \"cũng sẽ sáng lên\", \"với điều kiện là DHA nó phải nhiều\"; nếu DHA ít thì khó đạt được điều đó (đây là lời trả lời của bác sĩ Phúc trong video).",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:49:14]", "quote": "khán giả đặt câu hỏi thì tôi có thể trả"},
      {"timestamp": "[01:49:16]", "quote": "lời rằng là nếu cá đó có nhiều DHA thì"},
      {"timestamp": "[01:49:19]", "quote": "chúng ta ăn sẽ thông minh"},
      {"timestamp": "[01:49:24]", "quote": "chúng ta nhìn cũng sẽ sáng lên nhưng với"},
      {"timestamp": "[01:49:26]", "quote": "điều kiện là DHA nó phải nhiều."},
      {"timestamp": "[01:49:29]", "quote": "nếu DHA ít thì chúng ta cũng khó để mà"}
    ],
    "rationale": "Each quoted fragment is verbatim, and the firm 'sẽ' is restored only as quoted reported speech answering the viewer. The 'có thể' at 01:49:14 belongs to 'tôi có thể trả lời'. The DHA-quantity condition and the low-DHA 'khó' clause are kept. No advice or endorsement is added.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p013",
    "claim_id": "c092",
    "proposed_text": "Để tối ưu hóa tỷ lệ, bài báo khuyên tránh các loại dầu thực vật và hạt chứa nhiều Omega-6 cũng như thực phẩm chế biến từ dầu và hạt: dầu đậu nành, dầu hướng dương, dầu ngô được biết là chứa hàm lượng lớn Omega-6, còn loại dầu mà transcript ghi là \"dầu ôu\" (tên dầu chưa xác định được từ transcript, cần kiểm tra âm thanh), dầu cọ, dầu dừa và quả bơ được biết là chứa ít Omega-6 hơn.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[01:54:12]", "quote": "Tôi xin trích dẫn nguyên văn nội"},
      {"timestamp": "[01:56:53]", "quote": "Để tối ưu hóa tỉ lệ, chúng ta cần tránh"},
      {"timestamp": "[01:56:55]", "quote": "tiêu thụ các loại dầu thực vật và hạt"},
      {"timestamp": "[01:56:57]", "quote": "chứa nhiều omega6 cũng như các loại thực"},
      {"timestamp": "[01:57:00]", "quote": "phẩm sử dụng dầu và hạt để chế biến. Dầu"},
      {"timestamp": "[01:57:03]", "quote": "đậu nành, dầu hướng dương, ngô được biết"},
      {"timestamp": "[01:57:06]", "quote": "là chứa hàm lượng lớn omega6. Còn dầu"},
      {"timestamp": "[01:57:09]", "quote": "ôu, dầu cọ, dầu dừa, quả bơ được biết là"},
      {"timestamp": "[01:57:13]", "quote": "chứa ít omega6 hơn."}
    ],
    "rationale": "The ASR token is not guessed: it is kept literally ('dầu ôu') and flagged for audio, with no oil name supplied. The article's evidential 'được biết là' is restored in both halves. The rest of the list and the read-article framing match the source.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p014",
    "claim_id": "c112",
    "proposed_text": "CLA vừa chống viêm vừa chống ung thư; về LA và ALA, transcript ghi bác sĩ Phúc nói \"la viêm còn Alla là chống viêm\" nhưng ngay sau đó lại ghi \"Còn cái Alla này thì nó lại gây viêm\" và \"Ala gây viêm\", nên chiều tác dụng gây viêm/chống viêm của từng chất không xác định được từ transcript (cần kiểm tra âm thanh);",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[02:10:17]", "quote": "thì cái này có nó có đặc điểm là viêm"},
      {"timestamp": "[02:10:22]", "quote": "nhưng mà cái AL thì nó lại có đặc điểm"},
      {"timestamp": "[02:10:31]", "quote": "la viêm còn Alla là chống viêm."},
      {"timestamp": "[02:10:43]", "quote": "Thế còn thì CL thì có tác dụng vừa chống"},
      {"timestamp": "[02:10:47]", "quote": "viêm vừa chống ung thư. Chống viêm cộng"},
      {"timestamp": "[02:10:50]", "quote": "với lại ung thư. Còn cái Alla này thì nó"},
      {"timestamp": "[02:10:53]", "quote": "lại gây viêm."},
      {"timestamp": "[02:10:56]", "quote": "Đúng chưa ạ? Ala gây viêm. Thế còn"},
      {"timestamp": "[02:14:02]", "quote": "thân này à ví dụ như alla hoặc aa này"}
    ],
    "rationale": "Both conflicting literal statements are quoted verbatim ('Còn cái Alla này thì nó lại gây viêm' joins 02:10:50/02:10:53). No direction is asserted and an audio check is advised. The speaker is the doctor's continuous monologue, as in the current claim. Minor note: 'ngay sau đó' covers about 20 s with the GL and CL statements in between. That is acceptable, not a fidelity defect.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p015",
    "claim_id": "c115",
    "proposed_text": "Để minh họa chuyện quá mức, trong phần trao đổi có ví dụ (transcript không xác định chắc người nói) rằng uống một chút rượu thì kích thích hệ tiêu hóa, kích thích tinh thần và khí huyết lưu thông, nhưng uống rượu quá nhiều thì sẽ hỏng, ảnh hưởng tới sức khỏe.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[02:20:03]", "quote": "Vâng. Có nghĩa là không cắt bỏ hoàn"},
      {"timestamp": "[02:20:05]", "quote": "Đúng rồi. Không cắt bỏ. Không thể cắt bỏ"},
      {"timestamp": "[02:20:08]", "quote": "Ví dụ như chúng ta đang nói là rượu là"},
      {"timestamp": "[02:20:12]", "quote": "Chúng ta uống một"},
      {"timestamp": "[02:20:14]", "quote": "chút rượu thôi thì nó sẽ kích thích hệ"},
      {"timestamp": "[02:20:17]", "quote": "tiêu hóa, kích thích tinh thần, kích"},
      {"timestamp": "[02:20:18]", "quote": "thích nhiều cái khí huyết lưu thông sẽ"},
      {"timestamp": "[02:20:20]", "quote": "rất là tốt. Nhưng mà chúng ta uống rượu"},
      {"timestamp": "[02:20:22]", "quote": "quá nhiều thì nó sẽ hỏng."},
      {"timestamp": "[02:20:24]", "quote": "Nó sẽ ảnh hưởng tới sức khỏe."},
      {"timestamp": "[02:20:33]", "quote": "Đấy lý do tôi nói lại là quý vị cần phải"}
    ],
    "rationale": "No speaker is named, which fits the possible turn change at 02:20:08 after the doctor's 'Đúng rồi ...' that the transcript leaves unresolved. The 'một chút' versus 'quá nhiều' condition and all effects are spoken. No endorsement of alcohol is added.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p016",
    "claim_id": "c122",
    "proposed_text": "Cơ thể chỉ có thể chuyển đổi ALA (từ dầu thực vật) thành EPA và DHA với tỷ lệ rất thấp, thực tế dưới 5% (các tài liệu nêu từ 0 đến 9%), nên \"không kỳ vọng lắm\" vào ăn dầu thực vật để bổ sung EPA và DHA.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[02:26:13]", "quote": "thì nó được bao nhiêu phần trăm? Rất ít"},
      {"timestamp": "[02:26:20]", "quote": "Trong các tài liệu là nói từ 0 cho đến"},
      {"timestamp": "[02:26:23]", "quote": "9%"},
      {"timestamp": "[02:26:24]", "quote": "nhưng mà thực ra thì nó chỉ dưới 5%"},
      {"timestamp": "[02:26:47]", "quote": "thực dầu thực vật thì nó chính là ALA,"},
      {"timestamp": "[02:27:08]", "quote": "Vậy chúng ta không kỳ vọng lắm vào ăn"},
      {"timestamp": "[02:27:10]", "quote": "dầu thực vật để bổ sung được EPA và DHA."}
    ],
    "rationale": "Restores the spoken degree wording 'không kỳ vọng lắm' verbatim, so the conclusion is no longer hardened. Numbers and targets are unchanged. No speaker is newly named.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p017",
    "claim_id": "c165",
    "proposed_text": "Dầu cá tái tổ hợp (rTG; lời nói: \"tái tổ hợp\", \"chữ R nhỏ và TG\"): Sau khi cô đặc ở dạng EE, nhà sản xuất dùng phản ứng hóa học tái tạo lại cấu trúc Triglycerid.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[02:59:23]", "quote": "sử dụng một cái gọi là tái tổ hợp. Dầu"},
      {"timestamp": "[02:59:26]", "quote": "cá tái tổ hợp là chữ R nhỏ và TG."},
      {"timestamp": "[02:59:34]", "quote": "trở lại cái này từ cái sau khi mà cô đặc"},
      {"timestamp": "[02:59:40]", "quote": "thành ety làm thêm một bước nữa là"},
      {"timestamp": "[02:59:48]", "quote": "pháp hóa học, phản ứng hóa học để nó tạo"},
      {"timestamp": "[02:59:50]", "quote": "thì nó có gắn chữ RTG này."}
    ],
    "rationale": "Removes the unspoken English expansion and shows the spoken label verbatim. The process wording is unchanged and supported. In scope under the bounded canonical-name policy.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p018",
    "claim_id": "c175",
    "proposed_text": "Từ 0,6 trở lên, bác sĩ Phúc nói chúng ta sẽ bỏ được nhiều sản phẩm thuốc như thuốc tiểu đường, thuốc mỡ máu, thuốc tim mạch ('Tôi thấy rất nhiều người bỏ được'), thuốc huyết áp; khớp đang đau 'bắt đầu hết đau'; phản ứng viêm dị ứng 'bắt đầu là hết'; viêm xoang, viêm mũi 'hết'; trí nhớ 'bắt đầu cải thiện'; trong cùng đoạn, transcript ghi câu 'Alzimer nhớ nhớ quên quên là cải thiện được rất nhiều, học hành nó tốt' nhưng không xác định chắc người nói câu này;",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[03:02:22]", "quote": "Lên tới 0,6 nếu quý vị nào mà uống từ"},
      {"timestamp": "[03:02:25]", "quote": "0,6 trở lên thì chúng ta sẽ bỏ được"},
      {"timestamp": "[03:02:32]", "quote": "thuốc tim mạch. Tôi thấy rất nhiều người"},
      {"timestamp": "[03:02:38]", "quote": "rồi thì khớp đang đau bắt đầu hết đau."},
      {"timestamp": "[03:02:41]", "quote": "Những cái phản ứng viêm dị ứng các thứ"},
      {"timestamp": "[03:02:42]", "quote": "bắt đầu là hết. Viêm xoang, viêm mũi các"},
      {"timestamp": "[03:02:44]", "quote": "thứ nọ kia hết. Thế rồi trí nhớ bắt đầu"},
      {"timestamp": "[03:02:47]", "quote": ">> Alzimer run rẩy tay chân Parkison."},
      {"timestamp": "[03:02:51]", "quote": "Alzimer nhớ nhớ quên quên là cải thiện"},
      {"timestamp": "[03:02:53]", "quote": "được rất nhiều, học hành nó tốt."}
    ],
    "rationale": "Only the Alzheimer clause changes. It becomes a verbatim quotation (joining 03:02:51/03:02:53) whose speaker is explicitly not established, and no speaker is named. The other clauses and each 'bắt đầu' qualifier are unchanged and spoken. The trailing ';' keeps the clause fitting the following Parkinson clause.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p019",
    "claim_id": "c208",
    "proposed_text": "Trong phần trao đổi, người dẫn chương trình nhắc rằng bác sĩ nhấn mạnh nên xét nghiệm vitamin D trước khi bổ sung, và nêu ý kiến riêng ('tôi nghĩ rằng') là trước khi bổ sung Omega-3 thì người cần bổ sung cũng nên xét nghiệm (ví dụ xem có mỡ máu hay không) để chọn loại Omega-3 có hàm lượng EPA và DHA phù hợp; lời đáp tiếp theo (transcript không ghi rõ người nói) nói nâng lên bước cao hơn là khám sức khỏe toàn thân và khám tổng quát, trong đó có các xét nghiệm như có mỡ máu không, có tiểu đường không.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[03:23:38]", "quote": "Ờ tuy nhiên tôi cũng muốn bổ sung một"},
      {"timestamp": "[03:23:45]", "quote": "thì bác sĩ có nhấn mạnh rằng là trước"},
      {"timestamp": "[03:23:51]", "quote": "là chúng ta nên xét nghiệm vitamin D và"},
      {"timestamp": "[03:23:54]", "quote": "tôi nghĩ rằng trước khi chúng ta bổ sung"},
      {"timestamp": "[03:24:01]", "quote": "được bổ sung cũng nên xét nghiệm để"},
      {"timestamp": "[03:24:03]", "quote": "chúng ta xem chúng ta có mỡ máu hay"},
      {"timestamp": "[03:24:10]", "quote": "cái chứa hàm lượng epadaha cho phù hợp."},
      {"timestamp": "[03:24:15]", "quote": "Ừ. Vâng, đương nhiên đấy là cái mà chúng"},
      {"timestamp": "[03:24:19]", "quote": "lên một cái bước cao hơn nữa đấy là"},
      {"timestamp": "[03:24:21]", "quote": "chúng ta khám sức khỏe toàn thân và khám"},
      {"timestamp": "[03:24:24]", "quote": ">> trong đó có những cái xét nghiệm để"},
      {"timestamp": "[03:24:28]", "quote": "máu không, có tiểu đường không,"}
    ],
    "rationale": "The host's 'tôi nghĩ rằng' is kept and the opinion is attributed to the host, as spoken. The tiểu đường example moves correctly from the host to the responsive turn, and that turn names no speaker. The general-examination step is spoken. Minor note: 'lời đáp tiếp theo' groups lines that carry several '>>' markers, but it identifies no one. Acceptable.",
    "replacement_text": null,
    "status": "pending-human-approval"
  },
  {
    "id": "p020",
    "claim_id": "o001",
    "proposed_text": "Trong phần trao đổi về kiến thức, bác sĩ Phúc nêu quan điểm chia sẻ thay vì giữ bí quyết: cho đi kiến thức giúp nhân lên kiến thức và khiến chính người chia sẻ phải tiếp tục học hỏi, hoàn thiện. Ông kể một số bác sĩ đã tìm đến để tìm hiểu về y khoa, vi chất và mong các bác sĩ giúp thêm bệnh nhân cũng như đồng nghiệp.",
    "verdict": "reject",
    "evidence": [
      {"timestamp": "[00:21:27]", "quote": "từ xưa tới nay thì người ta nói rằng"},
      {"timestamp": "[00:21:29]", "quote": "phải giữ ví dụ các thầy dạy võ phải giữ"},
      {"timestamp": "[00:21:37]", "quote": "những các cái bí quyết về các cái bài"},
      {"timestamp": "[00:21:55]", "quote": "là bí truyền. Nhưng với tôi thì tôi lại"},
      {"timestamp": "[00:21:57]", "quote": "quan điểm khác. Kiến thức luôn luôn là"},
      {"timestamp": "[00:21:59]", "quote": "cho đi và một khi cho đi thì chúng ta sẽ"},
      {"timestamp": "[00:22:02]", "quote": "được nhân lên rất nhiều. Khi tôi truyền"},
      {"timestamp": "[00:22:04]", "quote": "cái kiến thức cho một người khác thì"},
      {"timestamp": "[00:22:08]", "quote": "nhân lên. Không những nhân lên mà bản"},
      {"timestamp": "[00:22:10]", "quote": "thân tôi phải hoàn thiện, bản thân tôi"},
      {"timestamp": "[00:22:12]", "quote": "phải học hỏi hơn nữa thì tôi sẽ phát"},
      {"timestamp": "[00:22:15]", "quote": "thời gian vừa rồi có một số những bác sĩ"},
      {"timestamp": "[00:22:17]", "quote": "cũng tìm đến tôi để tìm hiểu về những"},
      {"timestamp": "[00:22:20]", "quote": "các cái lĩnh vực về y khoa, về vi chất."},
      {"timestamp": "[00:22:41]", "quote": "mong các bác sĩ là chúng ta sẽ giúp đỡ"},
      {"timestamp": "[00:22:44]", "quote": "được nhiều bệnh nhân hơn nữa, chúng ta"},
      {"timestamp": "[00:22:46]", "quote": "sẽ giúp đỡ được nhiều đồng nghiệp hơn"}
    ],
    "rationale": "OPTIONAL item. 'tìm đến để tìm hiểu' correctly replaces the omission draft's 'trao đổi', and the anti-secrecy stance, the doctors' visits and the hope for helping patients and colleagues are spoken. One clause changes the scope: 'khiến chính người chia sẻ phải tiếp tục học hỏi, hoàn thiện' turns the speaker's first-person statement ('Khi tôi truyền ... bản thân tôi phải hoàn thiện, bản thân tôi phải học hỏi hơn nữa') into a general rule for anyone who shares. The replacement keeps that statement as his own and adds no East-Asian generalization, so the hedge question does not arise. It adds no patient-benefit outcome.",
    "replacement_text": "Trong phần trao đổi về kiến thức, bác sĩ Phúc nêu quan điểm khác với việc phải giữ bí quyết, bí truyền mà theo ông nhiều người từ xưa tới nay vẫn nói: kiến thức luôn là cho đi và khi cho đi thì được nhân lên rất nhiều; ông nói khi truyền kiến thức cho người khác thì không những kiến thức được nhân lên mà bản thân ông phải hoàn thiện, phải học hỏi hơn nữa. Ông kể một số bác sĩ đã tìm đến để tìm hiểu về các lĩnh vực y khoa, vi chất, và ông mong các bác sĩ sẽ giúp đỡ được nhiều bệnh nhân hơn nữa, giúp đỡ được nhiều đồng nghiệp hơn.",
    "status": "pending-human-approval"
  }
]
```

## Handling notes

- Every record stays `pending-human-approval`. This review's `approve` or `reject` is advisory, model-only input to the human decision. It does not approve, apply or withdraw any proposal. The canonical-name policy choice (p001, p003, p009, p017) is still the human's.
- The p004 and p020 `replacement_text` values are candidate alternatives only. They have not been independently reviewed and should get their own literal check before any human approval. The original proposed texts are recorded above exactly as written and were not modified in `proposed-corrections.md`.
- Applying corrections, editing `summary.md` and changing publication state are outside this phase. Publication stays **blocked**.

## Validation

An in-memory `PYTHONDONTWRITEBYTECODE=1 python3` check was run after writing (no script or temp file). It covered:
- exactly 20 IDs p001–p020, each once;
- each `proposed_text` and `claim_id` exactly equal to `proposed-corrections.md`;
- claim IDs present in current `claims.json` (o001 present in `omissions.md`);
- verdicts in {approve, reject}; every status `pending-human-approval`;
- `replacement_text` non-empty exactly for the rejects;
- every evidence quote a verbatim substring of the transcript line starting with its timestamp;
- all manifest and extractor hashes unchanged.

The result is reported in the run's final response.
