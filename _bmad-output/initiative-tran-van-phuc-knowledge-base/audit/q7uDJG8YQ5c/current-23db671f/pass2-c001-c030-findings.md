# Pass 2 (independent recheck, provisional): q7uDJG8YQ5c, assigned c003, c004, c010, c012, c016, c024, c030

**Status: PROVISIONAL.** These findings still need parent validation and the required independent recheck. No corrections are proposed or applied. Publication status: `blocked`.

## Binding
- summary.md SHA-256 `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64`: recomputed, **match**.
- transcript.md SHA-256 `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`: recomputed, **match**.
- Claim and section text is copied from `claims.json`. A script confirmed that each claim string, and each section heading text, occurs verbatim in summary.md.

## Method and limitations
- The full transcript (`[00:00:01]` → `[03:32:39]`, 5331 lines) was read end to end in sequential chunks before `pass1-c001-c030.md` was opened. Each assigned claim was checked against the whole transcript. Relevant material outside each section window was used: 00:09:42 and 00:11:47 for c030; 00:14:29–00:17:38, 00:15:58 and 03:32:01 for c004; 00:09:29 for c003.
- `review.md` and historical claim IDs/verdicts were not consulted.
- Evidence quotes are single-line verbatim substrings of the transcript line that starts with the cited `[hh:mm:ss]`. There is no whitespace normalization and there are no ellipses. A read-only script checked them: **7 records, 126 quotes, 0 failures**. On the first script run, 4 quotes failed because their timestamps were off by one line; they were re-anchored to the actual lines before the final run.
- Speaker identity is taken from content (self-identification, first/third-person reference), not from ASR `>>` markers alone. No attribution here is left unresolved.
- ASR forms (Golden, Moa/Moza, bác sĩ Quang, VDUP) limit how far term fidelity can be judged. No medical, historical or mathematical correction was applied.
- Severity tags (low/moderate) are this auditor's judgement. The class boundary between paraphrase and `attribution_qualification` is policy-sensitive for c003, c004 and c016.
- Process note: verification scripts were kept as scratch files under `/tmp/p2/`, outside the repository. Nothing in the repository was modified other than this output file.

## Records

```json
[
  {
    "id": "c003",
    "section": "[00:00:15] Định hướng sản xuất video dài truyền đạt kiến thức y khoa chuyên sâu",
    "claim": "Tuy nhiên, nội dung ngắn không thể truyền tải những kiến thức y khoa có chiều rộng và chiều sâu.",
    "evidence": [
      {
        "timestamp": "[00:00:18]",
        "quote": "Official và tôi là Khánh Lành."
      },
      {
        "timestamp": "[00:01:00]",
        "quote": ">> Vâng, thưa quý vị khán giả, khi bắt đầu"
      },
      {
        "timestamp": "[00:01:11]",
        "quote": "nhiên thì bác sĩ Phúc lại không nghĩ như"
      },
      {
        "timestamp": "[00:02:06]",
        "quote": "thức lấp đầy những khoảng thời gian này"
      },
      {
        "timestamp": "[00:02:08]",
        "quote": "thì những video ngắn với những nội dung"
      },
      {
        "timestamp": "[00:02:14]",
        "quote": "hảo cho nhu cầu này. Tuy nhiên thì để có"
      },
      {
        "timestamp": "[00:02:16]",
        "quote": "kiến thức rộng và sâu thì video ngắn"
      },
      {
        "timestamp": "[00:02:18]",
        "quote": "hoàn toàn không thể đáp ứng được. Chính"
      },
      {
        "timestamp": "[00:02:28]",
        "quote": "thể truyền đạt những kiến thức sức khỏe"
      },
      {
        "timestamp": "[00:02:31]",
        "quote": "cả về chiều rộng lẫn chiều sâu và thời"
      },
      {
        "timestamp": "[00:09:29]",
        "quote": "nhưng mà nó sẽ không có được cái tầm"
      },
      {
        "timestamp": "[00:09:31]",
        "quote": "chiều cao và không có được cái chiều"
      },
      {
        "timestamp": "[00:09:33]",
        "quote": "sâu. À đấy là một cái điều mà tôi rất"
      }
    ],
    "speaker": "Khánh Lành (host) speaks 00:01:00–00:02:41; she self-identifies at 00:00:18 and refers to 'bác sĩ Phúc' in the third person at 00:01:11, so identity rests on content, not only on the >> marker. The summary sentence is unattributed narrator voice following c001, which names Khánh Lành; no misattribution.",
    "class": "attribution_qualification",
    "note": "Added qualification: the spoken claim is generic 'kiến thức rộng và sâu' (00:02:16) that short video cannot meet; the summary narrows it to 'kiến thức y khoa'. 'y khoa' is not spoken here; the nearest spoken scope is 'kiến thức sức khỏe' (00:02:28, the long-video purpose), and Dr. Phúc's parallel remark (00:09:29–00:09:33) is also generic (life/simplification). Low severity; 'video ngắn'→'nội dung ngắn' is a harmless paraphrase."
  },
  {
    "id": "c004",
    "section": "[00:00:15] Định hướng sản xuất video dài truyền đạt kiến thức y khoa chuyên sâu",
    "claim": "Do đó, kênh quyết định thực hiện các video dài (từ vài chục phút cho đến thời lượng kỷ lục hơn 4 tiếng 30 phút) nhằm cung cấp cho cộng đồng kiến thức sức khỏe đầy đủ, khoa học và chuyên sâu.",
    "evidence": [
      {
        "timestamp": "[00:02:20]",
        "quote": "vì vậy, ngay từ khi thành lập kênh thì"
      },
      {
        "timestamp": "[00:02:22]",
        "quote": "bác sĩ Phúc cũng như toàn bộ ekip chương"
      },
      {
        "timestamp": "[00:02:24]",
        "quote": "trình đã thống nhất quan điểm rằng là"
      },
      {
        "timestamp": "[00:02:26]",
        "quote": "chúng tôi sẽ dùng những video dài để có"
      },
      {
        "timestamp": "[00:02:28]",
        "quote": "thể truyền đạt những kiến thức sức khỏe"
      },
      {
        "timestamp": "[00:02:31]",
        "quote": "cả về chiều rộng lẫn chiều sâu và thời"
      },
      {
        "timestamp": "[00:02:38]",
        "quote": "nhớ rằng là thời lượng kỷ lực của chúng"
      },
      {
        "timestamp": "[00:02:42]",
        "quote": ">> 4 tiếng hơn 30 phút đúng không ạ?"
      },
      {
        "timestamp": "[00:02:44]",
        "quote": ">> Vâng đúng rồi ạ. Và có lẽ là quý vị khán"
      },
      {
        "timestamp": "[00:14:29]",
        "quote": "của mình. Chính vì như vậy mà tôi quyết"
      },
      {
        "timestamp": "[00:14:31]",
        "quote": "định rằng là sẽ phải làm dài nhưng tôi"
      },
      {
        "timestamp": "[00:14:42]",
        "quote": "những số phát sóng đầu tiên là tôi với"
      },
      {
        "timestamp": "[00:14:46]",
        "quote": "độ 3 40 phút. Trong khoảng thời gian như"
      },
      {
        "timestamp": "[00:17:36]",
        "quote": "Khánh lành nói đó là lên tới hơn 4 tiếng"
      },
      {
        "timestamp": "[00:17:38]",
        "quote": "rưỡi đồng hồ và cũng thấy rằng đến giờ"
      },
      {
        "timestamp": "[00:15:58]",
        "quote": "có những cái bài báo mà viết rất đầy đủ"
      },
      {
        "timestamp": "[03:32:00]",
        "quote": "Và điều quan trọng nhất là những kiến"
      },
      {
        "timestamp": "[03:32:01]",
        "quote": "thức khoa học chính thống sẽ được nhân"
      }
    ],
    "speaker": "Khánh Lành (host) states that Dr. Phúc and the whole crew agreed from the channel's founding to use long videos (00:02:20–00:02:31). Dr. Phúc answers the record question '4 tiếng hơn 30 phút đúng không ạ?' and Khánh Lành confirms (00:02:42–00:02:44). Dr. Phúc separately says he decided on long form with a gradual path from 30–40-minute episodes (00:14:29–00:14:46) and repeats 'hơn 4 tiếng rưỡi' (00:17:36–00:17:38). The summary's 'kênh quyết định' is neutral between the two accounts.",
    "class": "attribution_qualification",
    "note": "Durations are supported ('vài chục phút' ≈ 'độ 3 40 phút'; record 'hơn 4 tiếng 30 phút' ≈ '4 tiếng hơn 30 phút'/'hơn 4 tiếng rưỡi'). Added qualifiers: the spoken purpose is 'kiến thức sức khỏe cả về chiều rộng lẫn chiều sâu'. 'chuyên sâu' ≈ 'chiều sâu' is fine and 'đầy đủ' loosely maps to 'chiều rộng', but 'khoa học' is not said about this decision; 'đầy đủ' and 'khoa học' appear only in other contexts (newspaper articles at 00:15:58; a closing remark at 03:32:01). Low severity: the adjective is added, not contradicted. Minor: the host frames the decision as dating 'ngay từ khi thành lập kênh', while the doctor describes a staged lengthening; the summary leaves this unstated."
  },
  {
    "id": "c010",
    "section": "[00:23:00] Khái niệm vô hạn trong toán học và khả năng phục hồi của cơ thể con người",
    "claim": "Nhà toán học Đức Kurt Gödel cũng phát biểu Định lý bất toàn năm 1931 minh chứng thế giới tự nhiên và khả năng con người chứa đựng vô vàn điều vô hạn.",
    "evidence": [
      {
        "timestamp": "[00:28:27]",
        "quote": "về vô hạn thì tôi rất thích cái định lý"
      },
      {
        "timestamp": "[00:28:39]",
        "quote": "bất toàn là của nhà toán học người Đức"
      },
      {
        "timestamp": "[00:28:42]",
        "quote": "Golden. Hôm trước tôi mới Khánh Lành có"
      },
      {
        "timestamp": "[00:28:44]",
        "quote": "nói đấy. Phát biểu năm 1931."
      },
      {
        "timestamp": "[00:29:11]",
        "quote": ">> Đúng. Chính xác. Đấy là một cái diễn"
      },
      {
        "timestamp": "[00:29:12]",
        "quote": "ngôn cái định lý bất toàn của nhà toán"
      },
      {
        "timestamp": "[00:29:15]",
        "quote": "học người Đức. Có thể nói rằng định lý"
      },
      {
        "timestamp": "[00:30:59]",
        "quote": "định lý bất toàn và thấy rằng thế giới"
      },
      {
        "timestamp": "[00:31:01]",
        "quote": "tự nhiên là vô hạn, khả năng con người"
      },
      {
        "timestamp": "[00:31:04]",
        "quote": "cũng là vô hạn. Nhưng đừng lấy cái vô"
      },
      {
        "timestamp": "[00:31:23]",
        "quote": "chỉnh lại. Thế thì cái định lý bất toàn"
      },
      {
        "timestamp": "[00:31:26]",
        "quote": "đó nó thể hiện rằng thế giới tự nhiên"
      },
      {
        "timestamp": "[00:31:29]",
        "quote": "của chúng ta có rất nhiều cái vô hạn."
      },
      {
        "timestamp": "[00:31:31]",
        "quote": "Trong cơ thể con người chúng ta cũng có"
      },
      {
        "timestamp": "[00:31:33]",
        "quote": "rất nhiều những cái vô hạn. Tôi lấy ví"
      }
    ],
    "speaker": "Dr. Phúc (he introduces the theorem and asks Khánh Lành whether she remembers it at 00:28:47–00:28:52; he confirms her paraphrase at 00:29:11). Attribution in the summary is to the theorem's author; that is not a speaker issue.",
    "class": "attribution_qualification",
    "note": "Added identification: the spoken author is 'nhà toán học người Đức Golden' (ASR form, 00:28:39–00:28:42). The summary supplies 'Kurt Gödel'; the given name 'Kurt' and the spelling come from outside knowledge, not the transcript. 'Đức' and '1931' are kept as spoken, with no correction applied or proposed here. Content check: the speaker frames the infinitude conclusion as what people found when they 'quay trở lại xem cái định lý bất toàn' (00:30:59–00:31:04) and as what the theorem 'thể hiện' (00:31:26–00:31:33). 'Minh chứng ... chứa đựng vô vàn điều vô hạn' is a fair paraphrase of 'có rất nhiều cái vô hạn'. Escalated only because of the unspoken added identity. Low-to-moderate severity."
  },
  {
    "id": "c012",
    "section": "[00:23:00] Khái niệm vô hạn trong toán học và khả năng phục hồi của cơ thể con người",
    "claim": "Ngay cả bệnh nhân ung thư khi đối mặt với nguy cơ tử vong, nếu biết điều chỉnh lối sống tích cực, giữ tinh thần lạc quan, sống khoa học, buông bỏ và bổ sung ít nhất 7 vi chất thì hoàn toàn có thể thoát khỏi bệnh tật.",
    "evidence": [
      {
        "timestamp": "[00:27:23]",
        "quote": "nó cũng sẽ là vô hạn. Một người một bệnh"
      },
      {
        "timestamp": "[00:27:26]",
        "quote": "nhân có thể là mắc căn bệnh ung thư"
      },
      {
        "timestamp": "[00:27:29]",
        "quote": "tưởng là chúng ta đi tới cửa tử tức là"
      },
      {
        "timestamp": "[00:27:32]",
        "quote": "đi đến cuối đoạn đầu đài nhưng cái người"
      },
      {
        "timestamp": "[00:27:34]",
        "quote": "đó hiểu được cuộc sống. cái người đó"
      },
      {
        "timestamp": "[00:27:36]",
        "quote": "biết bình chỉnh lại cái lối sống của"
      },
      {
        "timestamp": "[00:27:38]",
        "quote": "mình, biết buông bỏ, biết bổ sung đủ vi"
      },
      {
        "timestamp": "[00:27:40]",
        "quote": "chất, biết sống một cuộc sống khoa học"
      },
      {
        "timestamp": "[00:27:42]",
        "quote": "và lạc quan. Tất cả những điều đó tôi đã"
      },
      {
        "timestamp": "[00:27:44]",
        "quote": "nói nhiều trong các số rồi. Bổ sung ít"
      },
      {
        "timestamp": "[00:27:48]",
        "quote": "nhất bảy vi chất, chúng ta sống tốt,"
      },
      {
        "timestamp": "[00:27:50]",
        "quote": "thực hành mọi lối sống tích cực và khoa"
      },
      {
        "timestamp": "[00:27:52]",
        "quote": "học thì người đó hoàn toàn có thể thoát"
      },
      {
        "timestamp": "[00:27:54]",
        "quote": "khỏi căn bệnh ung thư. Một cái căn bệnh"
      },
      {
        "timestamp": "[00:28:00]",
        "quote": "nhưng tự dưng chúng ta lại thoát khỏi"
      }
    ],
    "speaker": "Dr. Phúc (continuous first-person monologue 00:22:53–00:28:20, including 'tôi đã nói nhiều trong các số rồi' at 00:27:42–00:27:44). The summary sentence is in narrator voice without naming him; the section context implies him.",
    "class": "attribution_qualification",
    "note": "Outcome object generalized: spoken 'hoàn toàn có thể thoát khỏi căn bệnh ung thư' (00:27:52–00:27:54) becomes 'thoát khỏi bệnh tật'. The cancer subject is kept, but the outcome term is broadened. Condition dropped: 'người đó hiểu được cuộc sống' (00:27:34). Conditions kept: lifestyle adjustment, letting go, scientific and optimistic life, and at least seven micronutrients (both 'đủ vi chất' and 'ít nhất bảy vi chất' are spoken; the summary keeps the latter). 'Hoàn toàn có thể' is preserved as spoken. 'Ngay cả' is added emphasis. 'Đối mặt với nguy cơ tử vong' fairly renders 'tưởng là chúng ta đi tới cửa tử'. No medical correction is made."
  },
  {
    "id": "c016",
    "section": "[00:31:36] Sự vô hạn trong sáng tạo nghệ thuật và thành tựu của các thiên tài",
    "claim": "Wolfgang Amadeus Mozart: Chỉ sống 35 năm nhưng đã để lại 22 vở opera (như vở \"Cây sáo thần\"), 41 bản giao hưởng và 42 bản concerto.",
    "evidence": [
      {
        "timestamp": "[00:44:38]",
        "quote": "hạn như nhà nhạc sĩ thiên tài Moa chẳng"
      },
      {
        "timestamp": "[00:44:46]",
        "quote": "về chiều dài về tuổi thọ thì Moa có 35"
      },
      {
        "timestamp": "[00:44:49]",
        "quote": "tuổi thôi. 35 tuổi nhưng mà ông viết"
      },
      {
        "timestamp": "[00:44:52]",
        "quote": "được bao nhiêu bản nhạc? Ông viết được"
      },
      {
        "timestamp": "[00:44:55]",
        "quote": "22 vở Ober. 22 vở Ober thì quá kinh"
      },
      {
        "timestamp": "[00:45:02]",
        "quote": "ví dụ cây sáo thần của Moza thì quá hay."
      },
      {
        "timestamp": "[00:45:25]",
        "quote": "được bao nhiêu? Ví dụ như là 41 bản giao"
      },
      {
        "timestamp": "[00:45:28]",
        "quote": "hưởng. Tất nhiên là Ma thì không thiên"
      },
      {
        "timestamp": "[00:45:31]",
        "quote": "nhiều về giao hưởng, không phải là cái"
      },
      {
        "timestamp": "[00:45:37]",
        "quote": "công secto của ông ấy 42 bản công sexo."
      },
      {
        "timestamp": "[00:46:24]",
        "quote": "ngắn ngủi 56 năm moza có 35 năm rõ ràng"
      }
    ],
    "speaker": "Dr. Phúc (first-person example, 'Tôi lấy ví dụ' at 00:44:34–00:44:38; personal opera-viewing remarks at 00:45:06–00:45:09). The summary attributes the Mozart/Beethoven examples to Dr. Phúc in the preceding line of the same section.",
    "class": "attribution_qualification",
    "note": "Numbers match as spoken (35; 22 vở Ober; 41 bản giao hưởng; 42 bản công secto; Cây sáo thần), with no historical correction. Added identification: the spoken forms are 'Moa/Moza/Ma'. 'Mozart' is a reasonable normalization, but the given names 'Wolfgang Amadeus' are never spoken and come from outside knowledge. Dropped aside: the speaker notes that Mozart 'không thiên nhiều về giao hưởng' (00:45:28–00:45:32). This does not hedge the numbers. 'Chỉ sống 35 năm' matches '35 tuổi thôi'/'moza có 35 năm'. Low severity; the parent may downgrade to supported if canonical full-name expansion is accepted as policy."
  },
  {
    "id": "c024",
    "section": "[00:34:05] Mô hình toán học về giá trị cuộc sống (Hàm V)",
    "claim": "(Ví dụ bác sĩ Phúc kể để cho thấy chiều rộng cuộc sống (W) quan trọng hơn chiều dài: một người anh họ bác sĩ bị ung thư dạ dày giai đoạn cuối chỉ sống thêm hơn 1 năm sau phẫu thuật, nhưng nhờ tập trung lo liệu chu toàn cho gia đình nên theo lời bác sĩ, ông anh thấy trong hơn một năm đó mình làm được nhiều việc nhất trong cuộc đời và ra đi thanh thản).",
    "evidence": [
      {
        "timestamp": "[00:34:30]",
        "quote": "sống. Ngoài ra hàm về chiều rộng cuộc"
      },
      {
        "timestamp": "[00:34:33]",
        "quote": "sống tức là VDUP cũng tương ứng với lại"
      },
      {
        "timestamp": "[00:38:14]",
        "quote": "trường khi tôi làm bác sĩ ngoại khoa có"
      },
      {
        "timestamp": "[00:38:17]",
        "quote": "một người họ hàng của tôi đấy là một"
      },
      {
        "timestamp": "[00:38:19]",
        "quote": "người anh trong họ khi thời điểm đó gọi"
      },
      {
        "timestamp": "[00:38:26]",
        "quote": "lúc ấy hơn 70 tuổi thì anh bị phát hiện"
      },
      {
        "timestamp": "[00:38:28]",
        "quote": "ra ung thư dạ dày. Và lúc đó tôi vẫn"
      },
      {
        "timestamp": "[00:38:34]",
        "quote": "như ngày hôm nay để mà hướng dẫn anh ấy"
      },
      {
        "timestamp": "[00:38:37]",
        "quote": "kéo dài được cuộc sống ngoài cái là phẫu"
      },
      {
        "timestamp": "[00:38:38]",
        "quote": "thuật cho anh ấy. Tức là phẫu thuật lấy"
      },
      {
        "timestamp": "[00:38:41]",
        "quote": "được toàn bộ khối u dạ dày và hạ nạo vét"
      },
      {
        "timestamp": "[00:38:43]",
        "quote": "hạch nhưng mà anh ấy lại bị ung thư vào"
      },
      {
        "timestamp": "[00:38:45]",
        "quote": "cái giai đoạn cuối. Thế thành ra là xác"
      },
      {
        "timestamp": "[00:38:48]",
        "quote": "định cái thời gian sống của anh ấy chỉ"
      },
      {
        "timestamp": "[00:38:51]",
        "quote": "hữu hạn thôi. Tức là ngắn trong vòng cơ"
      },
      {
        "timestamp": "[00:38:53]",
        "quote": "độ hơn năm trời, năm rưỡi là cùng."
      },
      {
        "timestamp": "[00:38:55]",
        "quote": ">> Nếu không phẫu thuật thì anh ấy chỉ 1"
      },
      {
        "timestamp": "[00:38:56]",
        "quote": "hai tháng không thể vượt qua được. Thế"
      },
      {
        "timestamp": "[00:38:59]",
        "quote": "nhưng nếu phẫu thuật thì sẽ kéo dài ra"
      },
      {
        "timestamp": "[00:39:01]",
        "quote": "được năm hơn năm. Thế khi anh ấy gặp tôi"
      },
      {
        "timestamp": "[00:39:09]",
        "quote": "chỉ ra cho anh ấy rằng chiều dài cuộc"
      },
      {
        "timestamp": "[00:39:10]",
        "quote": "sống không quan trọng bằng chiều rộng"
      },
      {
        "timestamp": "[00:40:23]",
        "quote": "khi tôi phân tích cho anh hiểu rằng cái"
      },
      {
        "timestamp": "[00:40:26]",
        "quote": "chiều rộng cuộc sống thì anh ấy vui vẻ,"
      },
      {
        "timestamp": "[00:40:29]",
        "quote": "anh ấy về, anh ấy tập trung làm các cái"
      },
      {
        "timestamp": "[00:40:33]",
        "quote": "ấy xuống gặp tôi ở bệnh viện. Anh ấy nói"
      },
      {
        "timestamp": "[00:40:36]",
        "quote": "rằng anh muốn mời chú đi ăn một bữa cơm"
      },
      {
        "timestamp": "[00:40:38]",
        "quote": "chia tay và anh đã lo anh đã chuẩn bị"
      },
      {
        "timestamp": "[00:40:45]",
        "quote": "tất cả mọi thứ và đến bây giờ anh ra đi"
      },
      {
        "timestamp": "[00:40:48]",
        "quote": "anh thanh thản, anh không phải suy nghĩ"
      },
      {
        "timestamp": "[00:40:49]",
        "quote": "gì. Và đây là cái thời gian mặc dù có"
      },
      {
        "timestamp": "[00:40:52]",
        "quote": "hơn năm trời thôi nhưng mà anh thấy anh"
      },
      {
        "timestamp": "[00:40:54]",
        "quote": "làm được nhiều việc nhất trong cuộc đời"
      }
    ],
    "speaker": "Dr. Phúc narrates in the first person and relays the relative's farewell words in reported speech ('Anh ấy nói rằng anh muốn mời chú...' 00:40:33–00:40:36). The summary's 'theo lời bác sĩ' attribution is correct for the relayed words.",
    "class": "attribution_qualification",
    "note": "Hardening of prognosis or elapsed time into a definite survival outcome. Spoken: after surgery the expected survival was 'hơn năm trời, năm rưỡi là cùng' and 'nếu phẫu thuật thì sẽ kéo dài ra được năm hơn năm' (prognosis, 00:38:48–00:39:01). At the farewell meal the relative calls the period so far 'hơn năm trời thôi' (00:40:49–00:40:52). The relative's death, and the total survival time, are never narrated. 'Anh ra đi anh thanh thản' (00:40:45–00:40:48) is his anticipatory statement that he can now go in peace. The summary's 'chỉ sống thêm hơn 1 năm sau phẫu thuật' and the closing 'và ra đi thanh thản' can be read as a reported death and outcome. The causal 'nhờ tập trung lo liệu' omits that the change followed the doctor's counselling (00:40:23–00:40:29), which is minor. Surgery itself appears to have been performed (00:38:37–00:38:43: 'phẫu thuật cho anh ấy. Tức là phẫu thuật lấy được toàn bộ khối u'), so 'sau phẫu thuật' is supported. Who operated is not stated. 'Anh họ' ≈ 'người anh trong họ' is fine. '(W)' is a summary symbol; ASR has 'VDUP' (00:34:33). Moderate severity."
  },
  {
    "id": "c030",
    "section": "[00:49:35] Hàm định vị cuộc sống và trải nghiệm chọn ngành của bác sĩ",
    "claim": "Bác sĩ chia sẻ trải nghiệm cá nhân từng mơ làm bác sĩ y học cổ truyền, sản khoa, ngoại khoa, nhưng cuối cùng nhận ra bản thân phù hợp nhất với vị trí bác sĩ Chẩn đoán hình ảnh (X-quang, siêu âm, CT, cộng hưởng từ) để giải mã các hình ảnh đen trắng giúp cứu chữa bệnh nhân.",
    "evidence": [
      {
        "timestamp": "[00:09:42]",
        "quote": "Nội ra trường. Lúc đấy tôi trở thành bác"
      },
      {
        "timestamp": "[00:09:45]",
        "quote": "sĩ ngoài khoa. Thời kỳ đầu tôi có đi phụ"
      },
      {
        "timestamp": "[00:11:47]",
        "quote": "điện quang can thiệp là đưa một cái kim"
      },
      {
        "timestamp": "[00:54:39]",
        "quote": "ngày xưa tôi học nào là tôi ban đầu tôi"
      },
      {
        "timestamp": "[00:54:42]",
        "quote": "mơ trở thành bác sĩ về y học cổ truyền."
      },
      {
        "timestamp": "[00:54:48]",
        "quote": "đó thì tôi lại mơ trở thành bác sĩ sản"
      },
      {
        "timestamp": "[00:54:50]",
        "quote": "khoa. Thế xong rồi tôi lại phấn đấu sau"
      },
      {
        "timestamp": "[00:54:53]",
        "quote": "ra trường. Tôi lại thích ngoại khoa, tôi"
      },
      {
        "timestamp": "[00:54:54]",
        "quote": "làm ngoại khoa. Xong cuối cùng tôi mới"
      },
      {
        "timestamp": "[00:54:56]",
        "quote": "thấy hóa ra làm bác sĩ Quang là phù hợp"
      },
      {
        "timestamp": "[00:54:58]",
        "quote": "nhất. Bởi vì khả năng của tôi chỉ là cái"
      },
      {
        "timestamp": "[00:55:04]",
        "quote": "cho những cái hình ảnh đen trắng trên"
      },
      {
        "timestamp": "[00:55:06]",
        "quote": "phim X Quang hay trên siêu âm hay trên"
      },
      {
        "timestamp": "[00:55:08]",
        "quote": "CT cộng ngẩng từ. những cái hình ảnh đen"
      },
      {
        "timestamp": "[00:55:19]",
        "quote": "trắng đó để mà cứu giúp những cái bệnh"
      },
      {
        "timestamp": "[00:55:22]",
        "quote": "nhân đang ở bên bờ của vực thẳm. Thì tôi"
      },
      {
        "timestamp": "[00:55:30]",
        "quote": "trên mình một cái tấm áo của bác sĩ"
      },
      {
        "timestamp": "[00:55:32]",
        "quote": "ngoại khoa rất hoành tráng. Thế rồi đi"
      },
      {
        "timestamp": "[00:55:37]",
        "quote": "mổ những cái ca đại phẫu sau đó thì ra"
      },
      {
        "timestamp": "[00:55:46]",
        "quote": "hợp với tôi lắm. Không phù hợp tôi quay"
      },
      {
        "timestamp": "[00:55:48]",
        "quote": "trở lại tôi làm bác sĩ Quang. Vậy thì"
      }
    ],
    "speaker": "Dr. Phúc (first person, 00:54:36–00:55:51).",
    "class": "attribution_qualification",
    "note": "Two issues. (1) Actual practice reduced to aspiration: for y học cổ truyền and sản khoa he says 'mơ trở thành'. For surgery, however, he says 'Tôi lại thích ngoại khoa, tôi làm ngoại khoa' (00:54:53–00:54:54), and elsewhere 'tôi trở thành bác sĩ ngoài khoa' (00:09:42–00:09:45) and that he wore the surgeon's coat and operated before returning (00:55:30–00:55:48). The summary's 'từng mơ làm ... ngoại khoa' drops the fact that he actually practised surgery. (2) Added specialty name: the spoken role is 'bác sĩ Quang' (ASR; context includes 'điện quang can thiệp' at 00:11:47). 'Chẩn đoán hình ảnh' is a summary label, not spoken; the modalities listed (X Quang, siêu âm, CT, 'cộng ngẩng từ') do match. 'Giải mã các hình ảnh đen trắng giúp cứu chữa bệnh nhân' fairly paraphrases 00:55:04–00:55:22. Moderate severity for (1); low for (2)."
  }
]
```

Counts (this pass, 7 claims): supported 0 · attribution_qualification 7 · mismatch 0 · unresolved 0.

## Comparison with pass-1 dispositions (read only after the fresh assessment above)

| id | pass 1 | pass 2 | agree? | rationale |
|---|---|---|---|---|
| c003 | supported (recheck) | attribution_qualification (low) | **disagree** | Pass 1 saw the 'y khoa' narrowing but excused it as a "minor scope specification". The contract counts an added qualification as `attribution_qualification`. The spoken claim is generic knowledge, and 'y khoa' is not said. We agree on the speaker (Khánh Lành) and that no hedge changed. |
| c004 | supported (recheck) | attribution_qualification (low) | **disagree** | We agree that the durations and the decision are supported. Pass 1 treated 'đầy đủ, khoa học' as paraphrase. 'Khoa học' is not spoken for this purpose; it is an added descriptor of the content's quality, so per contract it should not be silently excused. Pass 1's evidence at 00:14:46 and 00:17:36 matches mine. |
| c010 | supported (recheck) | attribution_qualification (low–moderate) | **disagree** | We agree that the content (infinitude of nature and human capacity), 'người Đức' and 1931 are supported as spoken. Pass 1 itself noted that 'Kurt' is never spoken and the ASR form is 'Golden'. An unspoken added identity based on outside knowledge is a material added identification under the task rules. |
| c012 | attribution_qualification | attribution_qualification | **agree** | Same findings (a) and (b): 'hiểu được cuộc sống' is dropped, and 'thoát khỏi căn bệnh ung thư' becomes 'bệnh tật'. A refinement on pass 1's (a): 'đủ vi chất' is not really dropped. Both 'đủ vi chất' and 'ít nhất bảy vi chất' are spoken and the summary keeps the stricter one. I weight (c), narrator voice, lower: the section context implies the doctor, so this is not misattribution. |
| c016 | supported (recheck) | attribution_qualification (low) | **disagree (narrow)** | We agree that all numbers match as spoken and the dropped symphony aside is not a hedge on the numbers. The difference is only the unspoken given names 'Wolfgang Amadeus', which are an added identification. If the parent's policy accepts canonical name expansion, supported is defensible; I flag it rather than silently excuse it. |
| c024 | supported (recheck) | attribution_qualification (moderate) | **disagree** | Pass 1 correctly observed that '1 năm+' is a prognosis and that the death is not narrated, but then accepted it. In my reading, 'chỉ sống thêm hơn 1 năm sau phẫu thuật' asserts a completed survival outcome. Together with the trailing 'ra đi thanh thản', the summary can be read as a reported peaceful death, whereas the transcript has only a prognosis, elapsed time at the farewell, and an anticipatory statement. On surgery we agree: it appears actually performed. |
| c030 | supported (recheck) | attribution_qualification (moderate) | **disagree** | Pass 1 itself noted that he actually practised surgery ('tôi làm ngoại khoa') and that 'Chẩn đoán hình ảnh' is not spoken, but called the result 'weaker but not contradictory'. Reducing actual practice to a dream changes a factual element of his biography, and the specialty label is added. Both are qualification changes that should be recorded. |

## Residual risks
- One second-pass reader. The class thresholds for c003, c004 and c016 (low-severity added descriptors or names) depend on how the parent sets policy for term and name normalization.
- c024 reading: someone could argue that 'hơn năm trời' at the farewell, plus the farewell context, implies the actual survival. The transcript still never narrates the death, so this stays a judgement call.
- ASR noise ('Golden', 'bác sĩ Quang', 'VDUP', 'cộng ngẩng từ') limits term-level certainty.
- Findings are provisional, no corrections were drafted, and omission review is out of scope for this run.
