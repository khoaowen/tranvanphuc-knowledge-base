# Independent literal check of the two candidate replacements (p004/c024, p020/o001), q7uDJG8YQ5c, summary 23db671f

**Status: model advisory check only. Both records are `pending-human-approval`.** This check covers only the two `replacement_text` candidates in `correction-wording-review.md`. They were written there after the original p004 and p020 wordings were rejected. A model `approve` here means only that this reviewer found the exact candidate wording faithful to the current transcript, clause by clause. It is not human approval and nothing is applied. If a human accepts them, these candidates would replace the **original rejected p004/p020 wording**, and only for approval consideration. All 20 proposals (p001–p020) are still pending human approval. `summary.md`, `proposed-corrections.md`, `correction-wording-review.md` and every earlier audit artifact are unchanged. Publication stays **blocked**. The 18 approved proposals and the completed claim passes were not rerun.

## Binding and verification (checked before reading and again after writing)

- `summary.md` SHA-256 `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64`: match.
- `transcript.md` SHA-256 `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`: match.
- `review.md` `5f588b23…0a41`, `metadata.json` `c3f19953…cd`: match `input-manifest.json`.
- Extractor `scripts/fidelity.py` `cc570d0b53168ebce3027af755d5c2a91045faa2c4e8bd2a93f78dea2538da0d`: matches `input-manifest.json`.
- Contract read: `spec-summary-source-audit.md` and `audit-record-format.md`. I read these to locate the targets, not as semantic proof: `continuation.md`, `input-manifest.json`, the `claims.json` record for c024, `proposed-corrections.md` (p004/p020 rows and notes, o001 placement), `omissions.md` (o001), and `correction-wording-review.md` (header, the p004 and p020 records, handling notes).

## Full-reading attestation

- I read the full current summary in order with the Read tool: lines 1–259 and 260–263, the whole file.
- I read the full transcript in order with no gaps, in bounded Read-tool chunks: lines 1–800, 801–1600, 1601–2400, 2401–3200, 3201–4000, 4001–4700, and 4701–5330 (`[00:00:01]`–`[03:32:39]`, end of file).
- I judged each clause against the whole transcript, not only against the cited windows. The earlier review's rationale served as a lead only.
- Semantic evidence used: only the current summary and transcript. I used no outside knowledge, no medical correction, no historical review verdicts and no inferred speaker identity, and I never relied on `>>` turn markers alone.

## Clause-by-clause findings

### p004 / c024 — approve

| clause in candidate | transcript basis | finding |
|---|---|---|
| "Ví dụ bác sĩ Phúc kể để cho thấy chiều rộng cuộc sống (W) quan trọng hơn chiều dài" | 00:38:08–00:38:14 "Tôi nhớ … khi tôi làm bác sĩ ngoại khoa"; 00:39:09–00:39:12 "chiều dài cuộc sống không quan trọng bằng chiều rộng cuộc sống" | Supported. The speaker identifies himself by content (his own surgical career and his own analysis), not by `>>`. |
| "một người anh họ bác sĩ bị ung thư dạ dày giai đoạn cuối" | 00:38:17–00:38:28 "người anh trong họ … ung thư dạ dày"; 00:38:43–00:38:45 "bị ung thư vào cái giai đoạn cuối" | Supported. |
| "đã được phẫu thuật" | 00:38:37–00:38:43 "phẫu thuật cho anh ấy. Tức là phẫu thuật lấy được toàn bộ khối u dạ dày và hạ nạo vét hạch" | Supported. The later "Nếu không phẫu thuật … nếu phẫu thuật thì" (00:38:55–00:39:01) is the prognosis comparison and does not contradict this. |
| "được xác định thời gian sống chỉ hữu hạn, khoảng hơn năm trời, 'năm rưỡi là cùng'" | 00:38:45–00:38:53 "xác định cái thời gian sống của anh ấy chỉ hữu hạn thôi … hơn năm trời, năm rưỡi là cùng." | Supported, worded as a **prognosis, not an outcome**. The transcript never narrates his death or how long he actually lived, and the candidate asserts neither. |
| "nhờ tập trung lo liệu chu toàn cho gia đình nên theo lời bác sĩ" | 00:40:29–00:40:33 "tập trung làm các cái công việc xong xuôi đâu đấy rồi thì"; 00:40:38–00:40:48 "anh đã chuẩn bị hết cho vợ con … gia đình họ hàng. Anh đã chuẩn bị tất cả mọi thứ và đến bây giờ anh ra đi anh thanh thản" | Supported. In the relative's own words the preparation is what lets him feel at peace, and the doctor's earlier analysis (00:39:28–00:40:11) sets up the same link. The candidate adds no new cause, including the doctor's advice. It is framed as "theo lời bác sĩ". |
| "khi xuống bệnh viện gặp bác sĩ và nói muốn mời 'đi ăn một bữa cơm chia tay'" | 00:40:33–00:40:38 "xuống gặp tôi ở bệnh viện. Anh ấy nói rằng anh muốn mời chú đi ăn một bữa cơm chia tay" | Supported. The setting is the **hospital visit**, and the meal is only an **invitation**. The candidate does not say the meal took place. The quoted phrase is verbatim across the caption boundary. |
| "ông anh nói 'đến bây giờ anh ra đi anh thanh thản'" | 00:40:45–00:40:48 | Verbatim. It belongs to the same reported speech at the hospital visit. "ra đi" stays inside quotation as a prospective statement. |
| "và thấy trong khoảng thời gian 'hơn năm trời' đó mình làm được nhiều việc nhất trong cuộc đời" | 00:40:52–00:40:54 "hơn năm trời thôi nhưng mà anh thấy anh làm được nhiều việc nhất trong cuộc đời" | Supported. "thấy" is used, not "nói". That fits whether the line is his speech or the doctor's report of his view, and both readings are covered by "theo lời bác sĩ". |

There is no added detail. Age, "nông dân" and the doctor's counselling are left out, which only shortens the text. Speaker, hedge and number wording are preserved ("hơn năm trời", "năm rưỡi là cùng"). The blocker from the earlier review (moving the speech to the farewell meal) is fixed. **No remaining blocker.**

### p020 / o001 (optional, low priority) — approve

| clause in candidate | transcript basis | finding |
|---|---|---|
| "Trong phần trao đổi về kiến thức, bác sĩ Phúc nêu quan điểm khác" | 00:08:55 is the reply to the host's question. The speaker is identified by content: 00:09:40–00:09:45 "mới tốt nghiệp trường đạo y Hà Nội … tôi trở thành bác sĩ", and 00:22:35–00:22:41 thanks bác sĩ Đỗ Huy for the encouragement given to him (Đỗ Huy's comment at 00:06:34–00:06:45 thanks "bác sĩ Phúc"). 00:21:55–00:21:57 "Nhưng với tôi thì tôi lại quan điểm khác." | Supported. "quan điểm khác" is spoken. |
| "khác với việc phải giữ bí quyết, bí truyền mà theo ông nhiều người từ xưa tới nay vẫn nói" | 00:21:23–00:21:39 "Có nhiều người từ xưa tới nay thì người ta nói rằng phải giữ … miếng võ cổ bí truyền … bí quyết về các cái bài thuốc" | Supported and attributed ("theo ông"). The East-Asian generalization (00:21:39–00:21:55) is left out, so its hedge is not at risk. |
| "kiến thức luôn là cho đi và khi cho đi thì được nhân lên rất nhiều" | 00:21:57–00:22:02 | Supported ("luôn luôn là" shortened to "luôn là"). |
| "ông nói khi truyền kiến thức cho người khác thì không những kiến thức được nhân lên mà bản thân ông phải hoàn thiện, phải học hỏi hơn nữa" | 00:22:02–00:22:12 "Khi tôi truyền cái kiến thức cho một người khác thì ngay lập tức là cái kiến thức ấy được nhân lên. Không những nhân lên mà bản thân tôi phải hoàn thiện, bản thân tôi phải học hỏi hơn nữa" | Supported and kept as a **personal, first-person** statement ("bản thân ông"), not a rule for every sharer. The blocker from the earlier review is fixed. |
| "Ông kể một số bác sĩ đã tìm đến để tìm hiểu về các lĩnh vực y khoa, vi chất" | 00:22:15–00:22:20 "có một số những bác sĩ cũng tìm đến tôi để tìm hiểu về những các cái lĩnh vực về y khoa, về vi chất." | Supported. It keeps the spoken "**tìm đến để tìm hiểu**". |
| "và ông mong các bác sĩ sẽ giúp đỡ được nhiều bệnh nhân hơn nữa, giúp đỡ được nhiều đồng nghiệp hơn" | 00:22:39–00:22:48 "tôi cũng mong các bác sĩ là chúng ta sẽ giúp đỡ được nhiều bệnh nhân hơn nữa, chúng ta sẽ giúp đỡ được nhiều đồng nghiệp hơn" | Supported as a hope ("mong … sẽ"), not an outcome. The doctors' reported feedback that patients were helped (00:22:22–00:22:30) is **not** added, so no outcome is invented. |

Non-blocking observation: the spoken "chúng ta" (inclusive, speaker plus doctors) becomes "các bác sĩ". This is within an address to the doctors and does not change scope materially. There is no medical claim, dose or product guidance. Inclusion stays **optional/low priority** at the placement given in `proposed-corrections.md`. **No remaining blocker.**

## Records (2)

```json
[
  {
    "id": "p004",
    "claim_id": "c024",
    "candidate_text": "(Ví dụ bác sĩ Phúc kể để cho thấy chiều rộng cuộc sống (W) quan trọng hơn chiều dài: một người anh họ bác sĩ bị ung thư dạ dày giai đoạn cuối, đã được phẫu thuật nhưng được xác định thời gian sống chỉ hữu hạn, khoảng hơn năm trời, 'năm rưỡi là cùng'; nhờ tập trung lo liệu chu toàn cho gia đình nên theo lời bác sĩ, khi xuống bệnh viện gặp bác sĩ và nói muốn mời 'đi ăn một bữa cơm chia tay', ông anh nói 'đến bây giờ anh ra đi anh thanh thản' và thấy trong khoảng thời gian 'hơn năm trời' đó mình làm được nhiều việc nhất trong cuộc đời).",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[00:38:14]", "quote": "trường khi tôi làm bác sĩ ngoại khoa có"},
      {"timestamp": "[00:38:17]", "quote": "một người họ hàng của tôi đấy là một"},
      {"timestamp": "[00:38:19]", "quote": "người anh trong họ khi thời điểm đó gọi"},
      {"timestamp": "[00:38:28]", "quote": "ra ung thư dạ dày. Và lúc đó tôi vẫn"},
      {"timestamp": "[00:38:37]", "quote": "kéo dài được cuộc sống ngoài cái là phẫu"},
      {"timestamp": "[00:38:38]", "quote": "thuật cho anh ấy. Tức là phẫu thuật lấy"},
      {"timestamp": "[00:38:41]", "quote": "được toàn bộ khối u dạ dày và hạ nạo vét"},
      {"timestamp": "[00:38:43]", "quote": "hạch nhưng mà anh ấy lại bị ung thư vào"},
      {"timestamp": "[00:38:45]", "quote": "cái giai đoạn cuối. Thế thành ra là xác"},
      {"timestamp": "[00:38:48]", "quote": "định cái thời gian sống của anh ấy chỉ"},
      {"timestamp": "[00:38:51]", "quote": "hữu hạn thôi. Tức là ngắn trong vòng cơ"},
      {"timestamp": "[00:38:53]", "quote": "độ hơn năm trời, năm rưỡi là cùng."},
      {"timestamp": "[00:39:09]", "quote": "chỉ ra cho anh ấy rằng chiều dài cuộc"},
      {"timestamp": "[00:39:10]", "quote": "sống không quan trọng bằng chiều rộng"},
      {"timestamp": "[00:40:29]", "quote": "anh ấy về, anh ấy tập trung làm các cái"},
      {"timestamp": "[00:40:31]", "quote": "công việc xong xuôi đâu đấy rồi thì anh"},
      {"timestamp": "[00:40:33]", "quote": "ấy xuống gặp tôi ở bệnh viện. Anh ấy nói"},
      {"timestamp": "[00:40:36]", "quote": "rằng anh muốn mời chú đi ăn một bữa cơm"},
      {"timestamp": "[00:40:38]", "quote": "chia tay và anh đã lo anh đã chuẩn bị"},
      {"timestamp": "[00:40:41]", "quote": "hết cho vợ con anh đâu đuôi đấy xong"},
      {"timestamp": "[00:40:43]", "quote": "xuôi, gia đình họ hàng. Anh đã chuẩn bị"},
      {"timestamp": "[00:40:45]", "quote": "tất cả mọi thứ và đến bây giờ anh ra đi"},
      {"timestamp": "[00:40:48]", "quote": "anh thanh thản, anh không phải suy nghĩ"},
      {"timestamp": "[00:40:52]", "quote": "hơn năm trời thôi nhưng mà anh thấy anh"},
      {"timestamp": "[00:40:54]", "quote": "làm được nhiều việc nhất trong cuộc đời"}
    ],
    "rationale": "Every clause is supported by the full transcript. The candidate states the source's prognosis ('xác định cái thời gian sống ... hơn năm trời, năm rưỡi là cùng'), not an outcome; neither his death nor his actual survival is narrated or asserted. The speech is now set at the hospital visit ('xuống gặp tôi ở bệnh viện'), and the farewell meal is only the invitation he spoke of ('muốn mời chú đi ăn một bữa cơm chia tay'). The meal is not presented as having happened, which fixes the earlier blocker. Surgery, terminal stage, the cousin relation and the W-over-L framing are spoken. 'ra đi ... thanh thản' stays a verbatim prospective quotation. The 'nhờ ... nên' link mirrors the relative's own 'Anh đã chuẩn bị tất cả mọi thứ và đến bây giờ anh ra đi anh thanh thản' under 'theo lời bác sĩ', so the causality is not false and no new cause is added. 'thấy ... làm được nhiều việc nhất' matches 00:40:52–00:40:54. No added detail, speaker inference or number change. No remaining blocker.",
    "status": "pending-human-approval"
  },
  {
    "id": "p020",
    "claim_id": "o001",
    "candidate_text": "Trong phần trao đổi về kiến thức, bác sĩ Phúc nêu quan điểm khác với việc phải giữ bí quyết, bí truyền mà theo ông nhiều người từ xưa tới nay vẫn nói: kiến thức luôn là cho đi và khi cho đi thì được nhân lên rất nhiều; ông nói khi truyền kiến thức cho người khác thì không những kiến thức được nhân lên mà bản thân ông phải hoàn thiện, phải học hỏi hơn nữa. Ông kể một số bác sĩ đã tìm đến để tìm hiểu về các lĩnh vực y khoa, vi chất, và ông mong các bác sĩ sẽ giúp đỡ được nhiều bệnh nhân hơn nữa, giúp đỡ được nhiều đồng nghiệp hơn.",
    "verdict": "approve",
    "evidence": [
      {"timestamp": "[00:09:40]", "quote": "đầu mà mới tốt nghiệp trường đạo y Hà"},
      {"timestamp": "[00:09:42]", "quote": "Nội ra trường. Lúc đấy tôi trở thành bác"},
      {"timestamp": "[00:21:23]", "quote": "điểm của tôi là thân này. Có nhiều người"},
      {"timestamp": "[00:21:27]", "quote": "từ xưa tới nay thì người ta nói rằng"},
      {"timestamp": "[00:21:29]", "quote": "phải giữ ví dụ các thầy dạy võ phải giữ"},
      {"timestamp": "[00:21:32]", "quote": "những các cái miếng võ cổ bí truyền hay"},
      {"timestamp": "[00:21:35]", "quote": "là những cái người thầy thuốc phải giữ"},
      {"timestamp": "[00:21:37]", "quote": "những các cái bí quyết về các cái bài"},
      {"timestamp": "[00:21:55]", "quote": "là bí truyền. Nhưng với tôi thì tôi lại"},
      {"timestamp": "[00:21:57]", "quote": "quan điểm khác. Kiến thức luôn luôn là"},
      {"timestamp": "[00:21:59]", "quote": "cho đi và một khi cho đi thì chúng ta sẽ"},
      {"timestamp": "[00:22:02]", "quote": "được nhân lên rất nhiều. Khi tôi truyền"},
      {"timestamp": "[00:22:04]", "quote": "cái kiến thức cho một người khác thì"},
      {"timestamp": "[00:22:06]", "quote": "ngay lập tức là cái kiến thức ấy được"},
      {"timestamp": "[00:22:08]", "quote": "nhân lên. Không những nhân lên mà bản"},
      {"timestamp": "[00:22:10]", "quote": "thân tôi phải hoàn thiện, bản thân tôi"},
      {"timestamp": "[00:22:12]", "quote": "phải học hỏi hơn nữa thì tôi sẽ phát"},
      {"timestamp": "[00:22:15]", "quote": "thời gian vừa rồi có một số những bác sĩ"},
      {"timestamp": "[00:22:17]", "quote": "cũng tìm đến tôi để tìm hiểu về những"},
      {"timestamp": "[00:22:20]", "quote": "các cái lĩnh vực về y khoa, về vi chất."},
      {"timestamp": "[00:22:35]", "quote": "ví dụ như bác sĩ Đỗ Huy. Tôi cảm ơn bác"},
      {"timestamp": "[00:22:37]", "quote": "sĩ Đỗ Huy là đã có những cái lời động"},
      {"timestamp": "[00:22:39]", "quote": "viên tôi, khích lệ tôi. Nhưng tôi cũng"},
      {"timestamp": "[00:22:41]", "quote": "mong các bác sĩ là chúng ta sẽ giúp đỡ"},
      {"timestamp": "[00:22:44]", "quote": "được nhiều bệnh nhân hơn nữa, chúng ta"},
      {"timestamp": "[00:22:46]", "quote": "sẽ giúp đỡ được nhiều đồng nghiệp hơn"}
    ],
    "rationale": "OPTIONAL, low-priority insertion. Every clause is spoken in 00:21:23–00:22:48. The speaker is identified by content, not by '>>': it is his own medical-graduate history, and he thanks bác sĩ Đỗ Huy for encouraging him. The secrecy tradition is attributed ('theo ông nhiều người từ xưa tới nay'), and the hedged East-Asian generalization is left out. Self-improvement stays a personal statement ('bản thân ông phải hoàn thiện, phải học hỏi hơn nữa') rather than a rule for all sharers, which fixes the earlier blocker. 'tìm đến để tìm hiểu' is kept verbatim. The closing is a hope ('mong ... sẽ'), and the reported patient-benefit feedback (00:22:22–00:22:30) is not added, so no outcome is invented. Minor non-blocking change: inclusive 'chúng ta' is rendered as 'các bác sĩ' inside his address to the doctors. No remaining blocker.",
    "status": "pending-human-approval"
  }
]
```

## Handling notes

- Both records stay `pending-human-approval`. These model approvals are advisory. If a human accepts them, the candidates would supersede only the **original rejected** p004/p020 wording, and only for approval consideration. All 20 proposals remain pending human approval. Nothing is applied, accepted, published or migrated.
- `proposed-corrections.md`, `correction-wording-review.md`, `summary.md`, `transcript.md`, `review.md` and the earlier audit artifacts were not modified. This file is the only output.
- No substitute wording is proposed and no retry was needed.

## Validation

After writing, I ran an in-memory `PYTHONDONTWRITEBYTECODE=1 python3` check with no script or temp file. It checked:
- exactly two IDs, p004 and p020, with claim_ids c024 and o001;
- each `candidate_text` exactly equal to the `replacement_text` for the same ID in `correction-wording-review.md`;
- verdict in {approve, reject}, status `pending-human-approval`, and the required keys;
- every evidence quote a verbatim substring of the transcript line that starts with its timestamp;
- all manifest and extractor hashes unchanged.

The result is reported in the run's final response.
