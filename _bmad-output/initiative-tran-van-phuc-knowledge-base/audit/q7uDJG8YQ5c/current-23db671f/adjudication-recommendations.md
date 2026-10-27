# Advisory adjudication recommendations — q7uDJG8YQ5c (current summary 23db671f)

**Status: ADVISORY ONLY. These recommendations are not human-accepted dispositions.** Every recommended class and correction direction below is `pending-human-acceptance` / `pending-human-approval`. Nothing has been applied. No video, review, progress, tool or publication-state file was changed. Publication status: **blocked**.

Reader: sole child on `anthropic/claude-opus-5-5`, as the operator directed after the GPT round. This is an adjudication of existing disagreements and residual non-supported findings. It does not rerun the first or second pass. All earlier opinions are preserved in their own artifacts (`pass1-*.md`, `pass2-*.md`, `omissions.md`). Where this file summarizes them, it does not replace them.

## 1. Binding and hash verification (done before any source reading)

Recomputed with `sha256sum`. All values match `input-manifest.json`:

| file | sha256 | result |
|---|---|---|
| summary.md | `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64` | match |
| transcript.md | `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b` | match |
| review.md | `5f588b23bda088c0e74837dffea6a452510af878299cc4950f25e594f7840a41` | match (hashed only, not read) |
| metadata.json | `c3f19953b8499eb724aa0b8d3126a83b94249c8df83b52951c0d8b429de76dcd` | match |
| scripts/fidelity.py (extractor) | `cc570d0b53168ebce3027af755d5c2a91045faa2c4e8bd2a93f78dea2538da0d` | match |

`claims.json` has 210 records. Section 9 records the final re-verification.

## 2. Reading attestation

- Contract: I read `spec-summary-source-audit.md` and `audit-record-format.md` in full, along with `continuation.md`, `input-manifest.json` and the target records in `claims.json`.
- Summary: I read all 263 lines (the file has 264 lines including the trailing newline) sequentially with the read tool, in chunks 1–259 and 259–263. The first chunk hit the 50 KB limit at line 259, and I continued from there. There was no gap.
- Transcript: I read all 5,330 lines sequentially with the read tool, without gaps. Chunks were 1–800, 801–1628, 1629–2458, 2459–3288, 3289–4118, 4119–4938 and 4939–5330. Each byte-limited chunk was continued at the exact next line the tool reported, so there was no overlap gap and no skipped span.
- I did not use section windows as a substitute for the full read. Every target was weighed against the whole transcript, including material outside its section (for example 00:09:42 for c030, 02:20:46 / 02:24:21 for c112/c120, and 03:26:13 for c208).
- Artifacts inspected within this folder: all seven completed first-pass files, the original draft `pass1-c091-c120.md` and its counterpart `pass1-c091-c120-completed.md`, all five `pass2-*-findings.md` files, and `omissions.md`. I read every target record (class, speaker, note, evidence) from every artifact that contains it.
- `review.md` and all historical reviews outside this folder were not read and were not used as evidence.

## 3. Mechanical verification of the target set

I parsed the pass artifacts in memory. The first-pass map uses the seven designated completed files, one per range; for c091–c120 that is the `-completed` file, and the draft is tracked separately. The second-pass map uses the five findings files.

- First pass: 210 IDs (187 supported, 14 attribution_qualification, 9 unresolved). Second pass: 70 IDs (55 supported, 9 attribution_qualification, 6 unresolved).
- Class disagreements between the first and second pass: **21**. They are c003, c004, c010, c016, c024, c030, c034, c037, c047, c051, c052, c064, c065, c068, c072, c076, c110, c115, c116, c120 and c167.
- Second-pass non-supported: **15**. They are c003, c004, c010, c012, c016, c024, c030, c064, c092, c096, c112, c122, c165, c175 and c208.
- Union: **29**. It is identical to the operator's exact target list, so no target was dropped or added.

## 4. Adjudication policy applied (source-only)

1. **Contract text controls.** `audit-record-format.md` defines `attribution_qualification` as a qualification "dropped, hardened **or added**" and names "có thể" explicitly. Under that definition, an added hedge on attributed speech (c051, c076) is a qualification change even when it is "conservative". This follows the contract's wording; it is not a default preference for the stricter reader.
2. **ASR normalization versus added identity.** A summary may render a garbled spoken token as the word it phonetically corresponds to when the correspondence is near-complete and the transcript context constrains it (Mozart←Moa/Moza, Lipton←Lip Tông/Liptông, lupus ban đỏ hệ thống←lú bút b đỏ hệ thống). Information that no spoken token corresponds to is an added identification and is **not supported** by this transcript. Examples are the given names Kurt, Wolfgang Amadeus and Bruce, and the English expansion Re-esterified. I did not use outside knowledge to confirm or refute any such addition. After a full read their absence is established, not ambiguous, so the contract's "after full reading may become another class" clause moves them out of `unresolved`.
3. **Paraphrase and evaluative descriptors.** Compression or a descriptor that adds no new proposition, condition, modality, dose/form specificity, time or entity remains `supported` (c004 "khoa học", c034 "flexible", c167 "cao cấp"). Narrowing a non-medical meta-statement to the channel's own stated domain is also supported (c003).
4. **Speaker attribution.** I did not treat `>>` markers or their absence as proof. Where the text cannot establish who spoke and the summary names a speaker, the record is `unresolved` and the correction direction is literal wording with no named speaker (c115, c175, part of c208).
5. **Entity labels inside the transcript.** Where the transcript's own repeated usage settles a label (GL/GLA and AL/ALA abbreviation habits; "la"/"La" = LA with formula C18:2n-6), I used that pattern. Where the same token is used for conflicting entities and the literal text conflicts (c112 "Ala gây viêm"), the record stays `unresolved`.
6. **No biomedical correctness.** I made no judgement on whether any medical, chemical or historical statement is true. The note on DHA's pi bonds is not in scope.

## 5. Decision table

The "draft" column shows the original `pass1-c091-c120.md` class only where relevant. AQ = attribution_qualification. Every advisory row is **pending-human-acceptance**.

| id | first pass | draft (orig. c091–c120) | second pass | advisory | agrees with | status |
|---|---|---|---|---|---|---|
| c003 | supported | — | AQ | supported | first | pending-human-acceptance |
| c004 | supported | — | AQ | supported | first | pending-human-acceptance |
| c010 | supported | — | AQ | AQ | second | pending-human-acceptance |
| c012 | AQ | — | AQ | AQ | both | pending-human-acceptance |
| c016 | supported | — | AQ | AQ | second | pending-human-acceptance |
| c024 | supported | — | AQ | AQ | second | pending-human-acceptance |
| c030 | supported | — | AQ | AQ | second | pending-human-acceptance |
| c034 | AQ | — | supported | supported | second | pending-human-acceptance |
| c037 | AQ | — | supported | supported | second | pending-human-acceptance |
| c047 | AQ | — | supported | AQ | first | pending-human-acceptance |
| c051 | AQ | — | supported | AQ | first | pending-human-acceptance |
| c052 | AQ | — | supported | AQ | first | pending-human-acceptance |
| c064 | AQ | — | unresolved | AQ | first | pending-human-acceptance |
| c065 | AQ | — | supported | AQ | first | pending-human-acceptance |
| c068 | AQ | — | supported | AQ | first | pending-human-acceptance |
| c072 | AQ | — | supported | supported | second | pending-human-acceptance |
| c076 | AQ | — | supported | AQ | first | pending-human-acceptance |
| c092 | unresolved | supported | unresolved | unresolved | first+second | pending-human-acceptance |
| c096 | unresolved | supported | unresolved | supported | draft only | pending-human-acceptance |
| c110 | unresolved | supported | supported | supported | second+draft | pending-human-acceptance |
| c112 | unresolved | unresolved | unresolved | unresolved | all | pending-human-acceptance |
| c115 | unresolved | unresolved | supported | unresolved | first+draft | pending-human-acceptance |
| c116 | unresolved | supported | supported | supported | second+draft | pending-human-acceptance |
| c120 | unresolved | unresolved | supported | supported | second | pending-human-acceptance |
| c122 | AQ | — | AQ | AQ | both | pending-human-acceptance |
| c165 | unresolved | — | unresolved | AQ | neither (reclassified after full read) | pending-human-acceptance |
| c167 | AQ | — | supported | supported | second | pending-human-acceptance |
| c175 | unresolved | — | unresolved | unresolved | both | pending-human-acceptance |
| c208 | AQ | — | AQ | AQ | both | pending-human-acceptance |

**Provisional advisory counts for the 29 targets:** supported 10, attribution_qualification 15, unresolved 4, mismatch 0.

**Implied provisional aggregate for all 210 claims, if the human accepts every advisory row:** supported 191, attribution_qualification 15, unresolved 4, mismatch 0. The 181 non-target claims are first-pass supported, and some of them are second-pass-confirmed. This aggregate is not accepted.

Close calls, where a human could reasonably take the other side: c037, c065, c068, c096, c120 and c167. Each note states the opposing reading.

## 6. Claim records (advisory)

```json
[
  {
    "id": "c003",
    "section": "[00:00:15] Định hướng sản xuất video dài truyền đạt kiến thức y khoa chuyên sâu",
    "claim": "Tuy nhiên, nội dung ngắn không thể truyền tải những kiến thức y khoa có chiều rộng và chiều sâu.",
    "evidence": [
      {"timestamp": "[00:00:30]", "quote": "trò chuyện với quý vị những kiến thức về"},
      {"timestamp": "[00:00:32]", "quote": "y khoa và chủ đề ngày hôm nay có tên Một"},
      {"timestamp": "[00:02:14]", "quote": "Tuy nhiên thì để có"},
      {"timestamp": "[00:02:16]", "quote": "kiến thức rộng và sâu thì video ngắn"},
      {"timestamp": "[00:02:18]", "quote": "hoàn toàn không thể đáp ứng được."},
      {"timestamp": "[00:02:28]", "quote": "thể truyền đạt những kiến thức sức khỏe"}
    ],
    "speaker": "Khánh Lành (host), who self-identifies at 00:00:18 and refers to bác sĩ Phúc in the third person. The summary sentence is unattributed narrator voice following c001 (attributed to Khánh Lành); no misattribution.",
    "class": "supported",
    "note": "Pass 1 (supported, minor scope note) and pass 2 (AQ, added 'y khoa') agree on the facts: the spoken sentence is generic 'kiến thức rộng và sâu'. Advisory: supported. The narrower 'y khoa' claim is entailed by the broader spoken one (if short video cannot meet broad/deep knowledge, it cannot meet broad/deep medical knowledge). It matches the channel's own stated domain, which the same host gives at 00:00:30–00:00:32 ('những kiến thức về y khoa'), and adds no hedge, condition or dose. Pass 2's objection is preserved as an optional literal edit ('kiến thức rộng và sâu'), not a fidelity defect."
  },
  {
    "id": "c004",
    "section": "[00:00:15] Định hướng sản xuất video dài truyền đạt kiến thức y khoa chuyên sâu",
    "claim": "Do đó, kênh quyết định thực hiện các video dài (từ vài chục phút cho đến thời lượng kỷ lục hơn 4 tiếng 30 phút) nhằm cung cấp cho cộng đồng kiến thức sức khỏe đầy đủ, khoa học và chuyên sâu.",
    "evidence": [
      {"timestamp": "[00:02:20]", "quote": "ngay từ khi thành lập kênh thì"},
      {"timestamp": "[00:02:26]", "quote": "chúng tôi sẽ dùng những video dài để có"},
      {"timestamp": "[00:02:28]", "quote": "thể truyền đạt những kiến thức sức khỏe"},
      {"timestamp": "[00:02:31]", "quote": "cả về chiều rộng lẫn chiều sâu"},
      {"timestamp": "[00:02:42]", "quote": "4 tiếng hơn 30 phút đúng không ạ?"},
      {"timestamp": "[00:14:46]", "quote": "độ 3 40 phút."},
      {"timestamp": "[03:32:01]", "quote": "thức khoa học chính thống sẽ được nhân"}
    ],
    "speaker": "Khánh Lành states the channel-founding agreement on long videos; bác sĩ Phúc gives the 4h30+ record and the staged 30–40-minute start. The summary's neutral 'kênh quyết định' covers both accounts.",
    "class": "supported",
    "note": "Pass 1 supported; pass 2 AQ because 'khoa học' (and loosely 'đầy đủ') is not in the decision sentence. Durations and the decision are supported. Advisory: supported. 'đầy đủ' ≈ 'chiều rộng' and 'chuyên sâu' ≈ 'chiều sâu'. 'khoa học' is an evaluative descriptor of the channel's own content that introduces no new health proposition, condition or modality, and the same host characterizes the channel's knowledge as 'kiến thức khoa học chính thống' (03:32:01). Pass 2's staged-versus-founding tension (host: from founding; doctor: gradual lengthening) is real but is not asserted either way by the summary. Optional literal edit: 'kiến thức sức khỏe cả về chiều rộng lẫn chiều sâu'."
  },
  {
    "id": "c010",
    "section": "[00:23:00] Khái niệm vô hạn trong toán học và khả năng phục hồi của cơ thể con người",
    "claim": "Nhà toán học Đức Kurt Gödel cũng phát biểu Định lý bất toàn năm 1931 minh chứng thế giới tự nhiên và khả năng con người chứa đựng vô vàn điều vô hạn.",
    "evidence": [
      {"timestamp": "[00:28:39]", "quote": "bất toàn là của nhà toán học người Đức"},
      {"timestamp": "[00:28:42]", "quote": "Golden."},
      {"timestamp": "[00:28:44]", "quote": "Phát biểu năm 1931."},
      {"timestamp": "[00:31:01]", "quote": "tự nhiên là vô hạn, khả năng con người"},
      {"timestamp": "[00:31:04]", "quote": "cũng là vô hạn."},
      {"timestamp": "[00:31:26]", "quote": "đó nó thể hiện rằng thế giới tự nhiên"},
      {"timestamp": "[00:31:29]", "quote": "của chúng ta có rất nhiều cái vô hạn."}
    ],
    "speaker": "bác sĩ Phúc introduces the theorem and its author; the summary attributes the theorem to its author, not to a speaker. No speaker issue.",
    "class": "attribution_qualification",
    "note": "Pass 1 supported (noting 'Kurt' is never spoken); pass 2 AQ for the same reason. Both agree on the facts; they differ on policy. Advisory: AQ (low severity). The surname rendering Gödel←'Golden' is a phonetic ASR normalization. The given name 'Kurt' corresponds to no spoken token and can only come from outside knowledge, so the summary adds an identification this transcript does not contain. Its absence is established by the full read, so this is not merely ambiguous. I make no judgement on whether the identification is historically correct. 'Đức', '1931' and the infinity content ('thể hiện… có rất nhiều cái vô hạn') are supported; 'minh chứng' ≈ 'thể hiện'."
  },
  {
    "id": "c012",
    "section": "[00:23:00] Khái niệm vô hạn trong toán học và khả năng phục hồi của cơ thể con người",
    "claim": "Ngay cả bệnh nhân ung thư khi đối mặt với nguy cơ tử vong, nếu biết điều chỉnh lối sống tích cực, giữ tinh thần lạc quan, sống khoa học, buông bỏ và bổ sung ít nhất 7 vi chất thì hoàn toàn có thể thoát khỏi bệnh tật.",
    "evidence": [
      {"timestamp": "[00:27:26]", "quote": "nhân có thể là mắc căn bệnh ung thư"},
      {"timestamp": "[00:27:29]", "quote": "tưởng là chúng ta đi tới cửa tử"},
      {"timestamp": "[00:27:34]", "quote": "đó hiểu được cuộc sống."},
      {"timestamp": "[00:27:36]", "quote": "biết bình chỉnh lại cái lối sống của"},
      {"timestamp": "[00:27:38]", "quote": "mình, biết buông bỏ, biết bổ sung đủ vi"},
      {"timestamp": "[00:27:40]", "quote": "chất, biết sống một cuộc sống khoa học"},
      {"timestamp": "[00:27:42]", "quote": "và lạc quan."},
      {"timestamp": "[00:27:48]", "quote": "nhất bảy vi chất, chúng ta sống tốt,"},
      {"timestamp": "[00:27:52]", "quote": "học thì người đó hoàn toàn có thể thoát"},
      {"timestamp": "[00:27:54]", "quote": "khỏi căn bệnh ung thư."}
    ],
    "speaker": "bác sĩ Phúc (sustained first-person monologue referring to his earlier episodes). The summary states this high-stakes outcome claim in narrator voice without naming him.",
    "class": "attribution_qualification",
    "note": "Both passes are AQ, with refined rationale: pass 2 notes that the 'ít nhất bảy vi chất' condition is kept. Advisory: AQ (moderate). Three issues. (1) The outcome is broadened: spoken 'thoát khỏi căn bệnh ung thư' becomes 'thoát khỏi bệnh tật'. (2) The spoken condition 'hiểu được cuộc sống' is dropped. (3) A medical outcome claim appears in narrator voice without 'bác sĩ Phúc cho rằng', although the speaker explicitly frames it as his own repeated view. 'Hoàn toàn có thể' is preserved. 'Đối mặt với nguy cơ tử vong' fairly renders 'tưởng là… đi tới cửa tử'. I make no medical judgement."
  },
  {
    "id": "c016",
    "section": "[00:31:36] Sự vô hạn trong sáng tạo nghệ thuật và thành tựu của các thiên tài",
    "claim": "Wolfgang Amadeus Mozart: Chỉ sống 35 năm nhưng đã để lại 22 vở opera (như vở \"Cây sáo thần\"), 41 bản giao hưởng và 42 bản concerto.",
    "evidence": [
      {"timestamp": "[00:44:38]", "quote": "hạn như nhà nhạc sĩ thiên tài Moa chẳng"},
      {"timestamp": "[00:44:46]", "quote": "về chiều dài về tuổi thọ thì Moa có 35"},
      {"timestamp": "[00:44:55]", "quote": "22 vở Ober."},
      {"timestamp": "[00:45:02]", "quote": "ví dụ cây sáo thần của Moza thì quá hay."},
      {"timestamp": "[00:45:25]", "quote": "Ví dụ như là 41 bản giao"},
      {"timestamp": "[00:45:37]", "quote": "42 bản công sexo."}
    ],
    "speaker": "bác sĩ Phúc ('Tôi lấy ví dụ'); the section's preceding sentence attributes the Mozart/Beethoven examples to him.",
    "class": "attribution_qualification",
    "note": "Pass 1 supported (noting the full name is supplied); pass 2 AQ, allowing a downgrade if canonical expansion is accepted as policy. Numbers (35; 22; 41; 42; Cây sáo thần) are kept as spoken, with no historical correction. Advisory: AQ (low), to keep the given-name policy consistent with c010, c064 and c165. 'Mozart'←'Moa/Moza' is phonetic normalization; 'Wolfgang Amadeus' has no spoken counterpart. The dropped aside 'không thiên nhiều về giao hưởng' does not hedge the numbers and is not the basis for this class. If the human adopts a canonical-expansion policy, this record (and c010/c064/c165) would become supported together. Residual risk: the same policy question affects non-target claims (e.g. 'Ludwig van Beethoven', 'Immanuel Kant') that both passes classed supported."
  },
  {
    "id": "c024",
    "section": "[00:34:05] Mô hình toán học về giá trị cuộc sống (Hàm V)",
    "claim": "(Ví dụ bác sĩ Phúc kể để cho thấy chiều rộng cuộc sống (W) quan trọng hơn chiều dài: một người anh họ bác sĩ bị ung thư dạ dày giai đoạn cuối chỉ sống thêm hơn 1 năm sau phẫu thuật, nhưng nhờ tập trung lo liệu chu toàn cho gia đình nên theo lời bác sĩ, ông anh thấy trong hơn một năm đó mình làm được nhiều việc nhất trong cuộc đời và ra đi thanh thản).",
    "evidence": [
      {"timestamp": "[00:38:19]", "quote": "người anh trong họ"},
      {"timestamp": "[00:38:28]", "quote": "ra ung thư dạ dày."},
      {"timestamp": "[00:38:45]", "quote": "cái giai đoạn cuối."},
      {"timestamp": "[00:38:51]", "quote": "hữu hạn thôi. Tức là ngắn trong vòng cơ"},
      {"timestamp": "[00:38:53]", "quote": "độ hơn năm trời, năm rưỡi là cùng."},
      {"timestamp": "[00:38:59]", "quote": "nhưng nếu phẫu thuật thì sẽ kéo dài ra"},
      {"timestamp": "[00:39:01]", "quote": "được năm hơn năm."},
      {"timestamp": "[00:40:36]", "quote": "rằng anh muốn mời chú đi ăn một bữa cơm"},
      {"timestamp": "[00:40:45]", "quote": "tất cả mọi thứ và đến bây giờ anh ra đi"},
      {"timestamp": "[00:40:48]", "quote": "anh thanh thản"},
      {"timestamp": "[00:40:52]", "quote": "hơn năm trời thôi nhưng mà anh thấy anh"},
      {"timestamp": "[00:40:54]", "quote": "làm được nhiều việc nhất trong cuộc đời"}
    ],
    "speaker": "bác sĩ Phúc narrates and relays the relative's farewell words; the summary's 'Ví dụ bác sĩ Phúc kể' / 'theo lời bác sĩ' attribution is correct.",
    "class": "attribution_qualification",
    "note": "Pass 1 supported (it recognized that the survival time is a prognosis and the death is not narrated, but accepted 'ra đi thanh thản' as being inside 'theo lời bác sĩ'). Pass 2 AQ (hardening). Advisory: AQ (low-moderate). The decisive phrase is 'chỉ sống thêm hơn 1 năm sau phẫu thuật'. It asserts an actual survival outcome, but the source gives a prognosis ('xác định cái thời gian sống… hơn năm trời, năm rưỡi là cùng'; 'nếu phẫu thuật thì sẽ kéo dài ra được năm hơn năm') and never narrates the death or the total survival. At the farewell meal the relative speaks prospectively ('đến bây giờ anh ra đi anh thanh thản'). Pass 1's point holds for the clause inside 'theo lời bác sĩ', but not for the survival phrase. Surgery, terminal stage and the width-over-length lesson are supported."
  },
  {
    "id": "c030",
    "section": "[00:49:35] Hàm định vị cuộc sống và trải nghiệm chọn ngành của bác sĩ",
    "claim": "Bác sĩ chia sẻ trải nghiệm cá nhân từng mơ làm bác sĩ y học cổ truyền, sản khoa, ngoại khoa, nhưng cuối cùng nhận ra bản thân phù hợp nhất với vị trí bác sĩ Chẩn đoán hình ảnh (X-quang, siêu âm, CT, cộng hưởng từ) để giải mã các hình ảnh đen trắng giúp cứu chữa bệnh nhân.",
    "evidence": [
      {"timestamp": "[00:09:42]", "quote": "Lúc đấy tôi trở thành bác"},
      {"timestamp": "[00:09:45]", "quote": "sĩ ngoài khoa."},
      {"timestamp": "[00:11:47]", "quote": "điện quang can thiệp"},
      {"timestamp": "[00:54:42]", "quote": "mơ trở thành bác sĩ về y học cổ truyền."},
      {"timestamp": "[00:54:48]", "quote": "đó thì tôi lại mơ trở thành bác sĩ sản"},
      {"timestamp": "[00:54:53]", "quote": "Tôi lại thích ngoại khoa, tôi"},
      {"timestamp": "[00:54:54]", "quote": "làm ngoại khoa. Xong cuối cùng tôi mới"},
      {"timestamp": "[00:54:56]", "quote": "thấy hóa ra làm bác sĩ Quang là phù hợp"},
      {"timestamp": "[00:55:06]", "quote": "phim X Quang hay trên siêu âm hay trên"},
      {"timestamp": "[00:55:08]", "quote": "CT cộng ngẩng từ."},
      {"timestamp": "[00:55:19]", "quote": "trắng đó để mà cứu giúp những cái bệnh"},
      {"timestamp": "[00:55:48]", "quote": "trở lại tôi làm bác sĩ Quang."}
    ],
    "speaker": "bác sĩ Phúc (first person).",
    "class": "attribution_qualification",
    "note": "Pass 1 supported (it flagged both the spoken 'bác sĩ Quang' label and the actual surgical practice, but judged them non-contradictory). Pass 2 AQ (practice reduced to aspiration; added specialty label). Advisory: AQ (moderate on point 1). (1) For surgery the speaker says 'thích ngoại khoa, tôi làm ngoại khoa' and elsewhere 'tôi trở thành bác sĩ ngoài khoa'. The summary's 'từng mơ làm… ngoại khoa' turns actual practice into an aspiration, which changes the career account even though c005 elsewhere mentions surgery. (2) The spoken role is 'bác sĩ Quang' (ASR), and his practice also included 'điện quang can thiệp'. 'Chẩn đoán hình ảnh' is a summary specialty label and is narrower than what is spoken. The listed modalities are supported, and 'giải mã hình ảnh đen trắng… cứu' fairly paraphrases 00:55:04–00:55:22."
  },
  {
    "id": "c034",
    "section": "[00:58:42] Đường hướng cuộc sống và tư duy chọn hướng đi",
    "claim": "Việc đi theo các đường cong flexible (như dòng nước chảy uốn lách qua các tảng đá để ra biển) mới mang lại hiệu quả cao nhất.",
    "evidence": [
      {"timestamp": "[00:59:38]", "quote": "chút, uốn éo một chút thì chúng ta mới"},
      {"timestamp": "[00:59:43]", "quote": "là hiệu quả. Cho nên là chúng ta hãy học"},
      {"timestamp": "[00:59:46]", "quote": "theo cái cách của một cái dòng nước."},
      {"timestamp": "[01:00:01]", "quote": "Bởi vì nó gặp tảng đá"},
      {"timestamp": "[01:00:12]", "quote": "nước đó để đi được ra biển nhanh nhất"},
      {"timestamp": "[01:00:24]", "quote": "luôn chậm nhất chúng ta muốn đi nhanh"},
      {"timestamp": "[01:00:25]", "quote": "nhất chúng ta phải đi bằng đường cong."}
    ],
    "speaker": "bác sĩ Phúc (same turn); the paragraph attributes the life-path reasoning to him.",
    "class": "supported",
    "note": "Pass 1 AQ (the word 'flexible' is unspoken; it read 'hiệu quả cao nhất' as an added superlative). Pass 2 supported (editorial paraphrase). Advisory: supported. 'flexible' is an English gloss for 'uốn éo/luồn lách', is not presented as a quotation, and adds no condition. In the A-to-B travel metaphor, the spoken superlatives are 'nhanh nhất' (curves are fastest; straight lines 'chậm nhất'), and bending 'thì chúng ta mới đạt được… hiệu quả'. Compressing these into 'hiệu quả cao nhất' preserves the claimed direction and scope, and the topic is non-medical. Pass 1's lexical observation is preserved as an optional literal edit ('nhanh nhất')."
  },
  {
    "id": "c037",
    "section": "[01:03:00] Nội hàm cuộc sống và hai điểm tựa gia đình, nhà trường",
    "claim": "Hai điểm tiêu cự $F1$ và $F2$ là hai điểm tựa chính: $F1$ đại diện cho gia đình (nơi tràn ngập tình yêu thương, hạnh phúc, là chỗ dựa trở về và bàn đạp phát triển), còn $F2$ đại diện cho nhà trường (bao gồm trường học các cấp, sách vở, thầy cô và những người dạy dỗ).",
    "evidence": [
      {"timestamp": "[01:04:36]", "quote": "nhất đấy chính là gia đình. Gia đình ở"},
      {"timestamp": "[01:04:38]", "quote": "đây là F1."},
      {"timestamp": "[01:04:42]", "quote": "trường. Nhà trường đấy chính là F2."},
      {"timestamp": "[01:04:48]", "quote": "chúng ta phải tìm ra được gia đình tốt,"},
      {"timestamp": "[01:05:11]", "quote": "được tất cả các trường học từ trường mẫu"},
      {"timestamp": "[01:05:29]", "quote": "từ trong sách vở"},
      {"timestamp": "[01:05:35]", "quote": "mình, những người thầy cô giáo hay những"},
      {"timestamp": "[01:06:01]", "quote": "rất mong muốn rằng xã hội phải xây dựng"},
      {"timestamp": "[01:06:06]", "quote": "gia đình mà ở đấy phải tràn ngập cái"},
      {"timestamp": "[01:06:08]", "quote": "tình yêu thương, hạnh phúc."},
      {"timestamp": "[01:06:10]", "quote": "phải là cái nơi để mà trở về."},
      {"timestamp": "[01:06:16]", "quote": "đấy làm cái bàn đạp để phát triển cho"}
    ],
    "speaker": "bác sĩ Phúc (ellipse life-model explanation).",
    "class": "supported",
    "note": "Pass 1 AQ (normative 'phải/tốt/mong muốn' dropped, so the description reads as fact). Pass 2 supported (the parenthesis describes the desired support in the model). Advisory: supported, as a close call. In the speaker's model the support point is precisely the good family ('phải tìm ra được gia đình tốt' at 01:04:48), and the summary's parenthesis describes what F1 stands for in that model. The very next summary sentence keeps the conditional requirement ('Phải kết hợp vững chắc cả hai điểm tựa này thì mới…'). Unlike c051/c076, no factual or medical outcome is strengthened or softened. Opposing reading preserved: a reader could take the parenthesis as describing families in general. Optional edit: '(gia đình tốt, nơi phải tràn ngập…)'. The F1/F2 mapping and school scope are directly supported."
  },
  {
    "id": "c047",
    "section": "[01:12:00] Bài toán thái độ và các yếu tố tạo nên kết quả công việc",
    "claim": "Trước một công việc, năng lực thể hiện khả năng làm được, động lực quyết định những gì sẽ làm, nhưng chính thái độ nghiêm túc, tích cực mới quyết định kết quả làm tốt hay không tốt và dẫn đến thành công hay thất bại.",
    "evidence": [
      {"timestamp": "[01:15:51]", "quote": "và gửi lại cho bác sĩ Phúc thì bác sĩ"},
      {"timestamp": "[01:15:57]", "quote": "Trước một công việc cụ thể, năng lực thể"},
      {"timestamp": "[01:16:01]", "quote": "hiện khả năng bạn có thể làm được. Động"},
      {"timestamp": "[01:16:04]", "quote": "lực quyết định những gì bạn làm nhưng"},
      {"timestamp": "[01:16:07]", "quote": "chỉ có thái độ mới tạo nên kết quả làm"},
      {"timestamp": "[01:16:10]", "quote": "tốt hay là không tốt."},
      {"timestamp": "[01:18:20]", "quote": "Đấy là thái độ của tôi nghiêm túc"},
      {"timestamp": "[01:19:02]", "quote": "thái độ mới quyết định được rằng là"},
      {"timestamp": "[01:19:04]", "quote": "chúng ta thành công hay thất bại."},
      {"timestamp": "[01:19:38]", "quote": "với một cái thái độ tích"}
    ],
    "speaker": "bác sĩ Phúc's text message, read verbatim by Khánh Lành ('trích lại nguyên văn') and later restated by him; the summary is unattributed (no misattribution).",
    "class": "attribution_qualification",
    "note": "Pass 1 AQ ('nghiêm túc, tích cực' inserted into the maxim). Pass 2 supported (contextual synthesis from nearby examples). Advisory: AQ (low). The summary sentence reproduces the read-aloud maxim almost word for word, so inserting adjectives modifies that maxim itself. The maxim treats attitude as the variable that decides whether the result is good or bad ('chỉ có thái độ mới tạo nên kết quả làm tốt hay là không tốt'). The summary makes a specific 'serious, positive' attitude the decider, which is a condition-like qualifier the maxim does not contain. The adjectives do occur nearby, but in different roles: the doctor describing his own attitude (01:18:20) and urging viewers to watch positively (01:19:38). Pass 2's contextual-support reading is preserved."
  },
  {
    "id": "c051",
    "section": "[01:20:24] Tác dụng của Omega-3, Vitamin D3 và bộ ba giảm đau tự nhiên",
    "claim": "Bác sĩ Phúc nói rằng sau khi đưa vitamin D lên ngưỡng lý tưởng và bổ sung vi chất đúng, đủ, các cơn đau thể xác có thể hết và cơn đau tinh thần có thể giảm nhiều.",
    "evidence": [
      {"timestamp": "[01:25:35]", "quote": "mà không giải thích được nguyên nhân tại"},
      {"timestamp": "[01:25:43]", "quote": "khi chúng ta đưa được vitamin D lên"},
      {"timestamp": "[01:25:45]", "quote": "ngưỡng lý tưởng, chúng ta bổ sung các"},
      {"timestamp": "[01:25:47]", "quote": "cái vi chất đúng và đủ thì tự dưng những"},
      {"timestamp": "[01:25:50]", "quote": "cái cơn đau về thể xác đấy hết."},
      {"timestamp": "[01:25:57]", "quote": "Cơn đau về mặt tinh thần nó cũng giảm đi"},
      {"timestamp": "[01:25:59]", "quote": "rất rất nhiều và có thể nói rằng là thậm"},
      {"timestamp": "[01:26:02]", "quote": "chí chúng ta không có cơn đau vào mặt"}
    ],
    "speaker": "bác sĩ Phúc (continuing his own explanation); the summary attributes it to him correctly.",
    "class": "attribution_qualification",
    "note": "Pass 1 AQ (hedge added; population framing dropped; mental-pain degree understated). Pass 2 supported (conservative compression). Both agree the conditions are retained. Advisory: AQ (low-moderate), following the contract's explicit 'added' clause. The sentence is reported speech ('Bác sĩ Phúc nói rằng'), but it represents a flat spoken outcome ('tự dưng những cái cơn đau về thể xác đấy hết') as 'có thể hết'. That misstates the speaker's certainty on a medical outcome, which matters for a human assessing what the doctor claimed. The 'có thể' at 01:25:59 modifies 'nói rằng… thậm chí không có', not the decrease itself. The summary also drops the scope that these are pains 'không giải thích được nguyên nhân' after many treatments ('đấy' refers back to them). No medical correction."
  },
  {
    "id": "c052",
    "section": "[01:20:24] Tác dụng của Omega-3, Vitamin D3 và bộ ba giảm đau tự nhiên",
    "claim": "Ông gọi bộ ba Canxi, Magiê và Vitamin D3 là một loại “thuốc giảm đau tự nhiên thần kỳ”, và nêu các ví dụ về đau xương khớp, dạ dày, đại tràng, trầm cảm, căng thẳng và bế tắc.",
    "evidence": [
      {"timestamp": "[01:23:28]", "quote": "vitamin D3 đúng không ạ? Vitamin D3."},
      {"timestamp": "[01:25:05]", "quote": "hôm trước tôi có nói rằng canxi, ma và"},
      {"timestamp": "[01:25:10]", "quote": "vitamin D nó là cái bộ ba gì Khánh Lành?"},
      {"timestamp": "[01:25:18]", "quote": "Đây là cái tôi ví rằng nó là thuốc giảm"},
      {"timestamp": "[01:25:21]", "quote": "đau tự nhiên rất thần kỳ."},
      {"timestamp": "[01:25:25]", "quote": "đau đớn về mặt thể xác bao gồm đau xương"},
      {"timestamp": "[01:25:33]", "quote": "ruột, đau đại tràng"},
      {"timestamp": "[01:26:05]", "quote": "Những người đang bị trầm cảm"},
      {"timestamp": "[01:26:14]", "quote": "cuộc sống rơi vào bế tắc"},
      {"timestamp": "[01:26:28]", "quote": "nói rằng vitamin D, vitamin D, mag và gì"},
      {"timestamp": "[01:26:37]", "quote": "giảm đau tự nhiên rất thần kỳ"}
    ],
    "speaker": "bác sĩ Phúc ('tôi ví rằng'); attribution correct.",
    "class": "attribution_qualification",
    "note": "Pass 1 AQ (D→D3 specificity; quotation not verbatim, 'rất' dropped). Pass 2 supported (D3 is contextual from the preceding study; the quote change is immaterial), and it keeps both points as editorial flags. Advisory: AQ (low). (a) Quotation precision: text inside quotation marks is presented as verbatim, but the spoken label, said twice, is 'thuốc giảm đau tự nhiên rất thần kỳ'. (b) Every time the speaker names the trio he says 'vitamin D' (01:25:10, 01:26:28, and again at 03:19:24). D3 belongs to the earlier study's regimen. Turning the trio's member into a specific supplement form adds form specificity in a supplement context, which the contract lists among qualifiers. The examples are supported."
  },
  {
    "id": "c064",
    "section": "[01:35:27] Cấu trúc màng tế bào và phát hiện của Bruce Lipton",
    "claim": "Năm 1985 tại vùng biển Caribe, nhà sinh học người Mỹ Bruce Lipton trong quá trình soạn giáo án đã phát hiện ra các đặc tính của màng tế bào:",
    "evidence": [
      {"timestamp": "[01:34:56]", "quote": "quan niệm này được một nhà sinh học thay"},
      {"timestamp": "[01:35:05]", "quote": "học người Mỹ,"},
      {"timestamp": "[01:35:13]", "quote": "Trà Lip Tông."},
      {"timestamp": "[01:35:15]", "quote": "Trà Lý Tông thì"},
      {"timestamp": "[01:35:30]", "quote": "biển Caribe"},
      {"timestamp": "[01:35:33]", "quote": "vào năm 1985"},
      {"timestamp": "[01:35:50]", "quote": "quá trình soạn giáo án thì ông soạn cấu"},
      {"timestamp": "[01:46:42]", "quote": "nhà khoa học, nhà sinh học Liptông tìm"}
    ],
    "speaker": "bác sĩ Phúc narrating a scientist's story; the scientist is heard only as 'Trà Lip Tông / Trà Lý Tông / Lip tông / Liptông'.",
    "class": "attribution_qualification",
    "note": "Pass 1 AQ (added identity 'Bruce'). Pass 2 unresolved (identity not established; not proof of a wrong identity). Both agree on the substance: 1985, Caribe, American biologist and lesson preparation are spoken, and 'Lipton'←'Lip Tông/Liptông' is phonetic normalization. Advisory: AQ (low), consistent with c010/c016/c165. After the full read, the given name 'Bruce' has no spoken counterpart. Its absence is established, not ambiguous, so the contract's full-read clause allows leaving 'unresolved'. 'Unresolved' would wrongly suggest the claim's core lacks evidence. I make no judgement on whether the identity is correct. The section heading carries the same name; a heading edit would change section strings and needs separate human handling."
  },
  {
    "id": "c065",
    "section": "[01:35:27] Cấu trúc màng tế bào và phát hiện của Bruce Lipton",
    "claim": "Màng tế bào gồm hai lớp phospholipid với đầu ưa nước quay ra ngoài/vào trong và đuôi kỵ nước giấu ở giữa, được sắp xếp trật tự theo dạng \"tinh thể màng\" (tương tự tinh thể lỏng).",
    "evidence": [
      {"timestamp": "[01:36:02]", "quote": "nó có hai"},
      {"timestamp": "[01:36:05]", "quote": "lớp"},
      {"timestamp": "[01:36:07]", "quote": "axit béo."},
      {"timestamp": "[01:36:20]", "quote": "đầu phospho lipit."},
      {"timestamp": "[01:36:25]", "quote": "cái đầu mà nó gọi là ưa nước."},
      {"timestamp": "[01:36:36]", "quote": "đuôi này nó được gọi là kỵ nước."},
      {"timestamp": "[01:37:16]", "quote": "trong tế bào và toàn bộ cái phần kỵ nước"},
      {"timestamp": "[01:37:18]", "quote": "thì nó được giấu ở bên trong."},
      {"timestamp": "[01:38:43]", "quote": "lại có tinh thể lỏng."},
      {"timestamp": "[01:38:54]", "quote": "Tinh thể cứng đó là các vật như"},
      {"timestamp": "[01:39:01]", "quote": "Thế thì ông nảy sinh ra một"},
      {"timestamp": "[01:39:03]", "quote": "cái đây là tinh thể màng."}
    ],
    "speaker": "bác sĩ Phúc narrating the scientist's first conclusion.",
    "class": "attribution_qualification",
    "note": "Pass 1 AQ ('hai lớp axit béo' → 'phospholipid'; liquid-crystal comparison added). Pass 2 supported (phospholipid summarizes the named heads; 'tương tự' is a loose analogy), while it preserves pass 1's objection. Advisory: AQ (low), as a close call. Split judgement: 'phospholipid' is acceptable compression, because the speaker himself names the heads 'phospho lipit' within the two-layer account. '(tương tự tinh thể lỏng)' asserts a specific comparison that is not spoken. The speaker lists hard crystals (diamond, salt) and liquid crystals (screens) as types and then names a third, 'tinh thể màng'. He never says the membrane resembles liquid crystal. Because the sentence presents the scientist's finding, an added scientific comparison is a qualification added. Opposing reading preserved: the 'Thế thì' transition right after the liquid-crystal example could suggest analogy."
  },
  {
    "id": "c068",
    "section": "[01:42:36] Khái niệm màng tế bào là bộ não của tế bào",
    "claim": "Năm 1985, nhà sinh học Liptông nhận thấy màng tế bào được cấu tạo bởi các lớp chất béo và protein sắp xếp theo trật tự, tạo thành các cửa và kênh dẫn (như kênh natri, kali, protein, chất béo) dẫn các chất vào và ra khỏi tế bào.",
    "evidence": [
      {"timestamp": "[01:37:56]", "quote": "hai cái hai cái chuỗi chất béo này."},
      {"timestamp": "[01:38:06]", "quote": "sắp xếp xung quanh theo một cái trật tự"},
      {"timestamp": "[01:39:33]", "quote": "thấy rằng protein nó muốn vào trong"},
      {"timestamp": "[01:42:53]", "quote": "những kênh ví dụ kênh kali, kênh natri,"},
      {"timestamp": "[01:42:56]", "quote": "kênh protein, kênh"},
      {"timestamp": "[01:42:58]", "quote": "chất béo để dẫn các cái chất đi vào"},
      {"timestamp": "[01:46:35]", "quote": "đầu từ năm 1985"},
      {"timestamp": "[01:46:50]", "quote": "Chính lông cũng như là các nhà khoa học"},
      {"timestamp": "[01:46:52]", "quote": "khác bắt đầu đi vào nghiên cứu thì người"},
      {"timestamp": "[01:47:06]", "quote": "Nó được cấu tạo bởi protein, được"},
      {"timestamp": "[01:47:09]", "quote": "cấu tạo bởi các chất béo."}
    ],
    "speaker": "bác sĩ Phúc narrating; the protein-plus-fat composition is narrated as found by later research of Liptông 'cũng như là các nhà khoa học khác'.",
    "class": "attribution_qualification",
    "note": "Pass 1 AQ (composition moved into the 1985 observation). Pass 2 supported (synthesis of a continuous account), while it preserves the temporal-precision risk. Advisory: AQ (low), as a close call. The speaker separates two stages. In 1985 there are ordered fat layers, with protein appearing only as a substance passing through channels (01:39:33, 'kênh protein'). After 'Từ đấy bắt đầu…', 'Chính lông cũng như là các nhà khoa học khác' research found the membrane 'được cấu tạo bởi protein… các chất béo'. The summary dates the composition finding to 1985 and to Liptông alone, which shifts time and scope. It is not a speaker misattribution, because Liptông is included in the later group. The ordered layers, gates and channel list are supported."
  },
  {
    "id": "c072",
    "section": "[01:42:36] Khái niệm màng tế bào là bộ não của tế bào",
    "claim": "Quan điểm màng tế bào là bộ não đã mở ra cuộc cách mạng trong tế bào học, ứng dụng vào việc nâng cao tuổi thọ, điều trị ung thư và đưa các chất từ bên ngoài vào trong tế bào một cách có chọn lọc.",
    "evidence": [
      {"timestamp": "[01:45:57]", "quote": "này. Và từ cái quan điểm màng tế bào là"},
      {"timestamp": "[01:46:04]", "quote": "Và sau này nó trở thành"},
      {"timestamp": "[01:46:06]", "quote": "một cái cuộc cách mạng về nghiên cứu tế"},
      {"timestamp": "[01:46:08]", "quote": "Cuộc cách mạng này nó liên quan"},
      {"timestamp": "[01:46:11]", "quote": "tới những các cái vấn đề nâng cao tuổi"},
      {"timestamp": "[01:46:18]", "quote": "trị ung thư, điều trị các cái căn bệnh"},
      {"timestamp": "[01:46:20]", "quote": "là đưa những các cái chất từ bên ngoài"},
      {"timestamp": "[01:46:22]", "quote": "vào bên trong tế bào một cách có chọn"},
      {"timestamp": "[01:46:24]", "quote": "Nhờ cái khái niệm là màng tế bào có"},
      {"timestamp": "[01:46:33]", "quote": "thì từ đấy nó mới ra được vấn đề."}
    ],
    "speaker": "bác sĩ Phúc's own narration; the summary paragraph frames the passage as his account ('Bác sĩ Phúc thuật lại…'), and this sentence follows that frame without repeating the name.",
    "class": "supported",
    "note": "Pass 1 AQ ('liên quan tới' hardened to 'ứng dụng vào'; unattributed). Pass 2 supported (the source's 'nhờ… mới ra được' supplies the enabling link). Advisory: supported. The speaker says not only that the revolution 'liên quan tới' these areas, but also that 'Nhờ cái khái niệm… màng tế bào là bộ não… thì từ đấy nó mới ra được vấn đề', an explicit enabling relation. 'Ứng dụng vào' is therefore a fair rendering and adds no outcome efficacy claim. The surrounding paragraph names bác sĩ Phúc as narrator, and repeating the attribution in each sentence is not required by the format. Pass 1's preference for the literal 'liên quan tới' is preserved as an optional edit."
  },
  {
    "id": "c076",
    "section": "[01:47:01] Vai trò của Omega-3, DHA và EPA trong cấu trúc màng tế bào",
    "claim": "Ông cũng cho rằng ăn cá giàu DHA có thể giúp thông minh hơn và mắt sáng hơn; nếu DHA ít thì khó đạt được điều đó.",
    "evidence": [
      {"timestamp": "[01:49:14]", "quote": "tôi có thể trả"},
      {"timestamp": "[01:49:16]", "quote": "lời rằng là nếu cá đó có nhiều DHA thì"},
      {"timestamp": "[01:49:19]", "quote": "chúng ta ăn sẽ thông minh"},
      {"timestamp": "[01:49:24]", "quote": "chúng ta nhìn cũng sẽ sáng lên nhưng với"},
      {"timestamp": "[01:49:26]", "quote": "điều kiện là DHA nó phải nhiều."},
      {"timestamp": "[01:49:29]", "quote": "nếu DHA ít thì chúng ta cũng khó để mà"}
    ],
    "speaker": "bác sĩ Phúc answering the viewer's question ('tôi có thể trả lời rằng'); attribution correct.",
    "class": "attribution_qualification",
    "note": "Pass 1 AQ ('sẽ' softened to 'có thể giúp'). Pass 2 supported (conservative entailment), while it preserves the modal concern. Advisory: AQ (low), for the same contract reason as c051. The speaker gives a firm conditional ('nếu cá đó có nhiều DHA thì chúng ta ăn sẽ thông minh… mắt… cũng sẽ sáng lên'). The 'có thể' at 01:49:14 belongs to 'tôi có thể trả lời', not to the outcome. Reported speech should not change the speaker's certainty in either direction. The DHA-quantity condition and the low-DHA 'khó' are correctly kept."
  },
  {
    "id": "c092",
    "section": "[01:53:28] Tỷ lệ Omega-6 và Omega-3 đối với các bệnh mãn tính",
    "claim": "Để tối ưu hóa tỷ lệ, bài báo khuyên tránh các loại dầu thực vật và hạt chứa nhiều Omega-6 cũng như thực phẩm chế biến từ dầu và hạt: dầu đậu nành, dầu hướng dương, dầu ngô chứa nhiều Omega-6, còn dầu ô liu, dầu cọ, dầu dừa và quả bơ chứa ít Omega-6 hơn.",
    "evidence": [
      {"timestamp": "[01:54:12]", "quote": "Tôi xin trích dẫn nguyên văn nội"},
      {"timestamp": "[01:56:53]", "quote": "Để tối ưu hóa tỉ lệ, chúng ta cần tránh"},
      {"timestamp": "[01:56:55]", "quote": "tiêu thụ các loại dầu thực vật và hạt"},
      {"timestamp": "[01:56:57]", "quote": "chứa nhiều omega6 cũng như các loại thực"},
      {"timestamp": "[01:57:00]", "quote": "phẩm sử dụng dầu và hạt để chế biến."},
      {"timestamp": "[01:57:03]", "quote": "đậu nành, dầu hướng dương, ngô được biết"},
      {"timestamp": "[01:57:06]", "quote": "là chứa hàm lượng lớn omega6. Còn dầu"},
      {"timestamp": "[01:57:09]", "quote": "ôu, dầu cọ, dầu dừa, quả bơ được biết là"},
      {"timestamp": "[01:57:13]", "quote": "chứa ít omega6 hơn."}
    ],
    "speaker": "Khánh Lành reading a newspaper article verbatim ('trích dẫn nguyên văn'); the summary's 'bài báo' attribution matches.",
    "class": "unresolved",
    "note": "Original draft supported ('ôu'→'ô liu' interpretive but immaterial). Completed pass 1 and pass 2 unresolved (oil identity not established). Advisory: unresolved, narrowly, for the single oil name. Unlike c110's near-complete syllable correspondence, the one-syllable ASR token 'ôu' corresponds only partially to the two-syllable 'ô liu'. Choosing olive over other oils would rest on outside knowledge of which oils are low in Omega-6, so the transcript cannot settle it. Everything else is supported: the advice, the high-Omega-6 list, palm, coconut and avocado, and 'ngô' inheriting 'dầu' from the list. Secondary low-severity point: the article's evidential frame 'được biết là' is dropped twice."
  },
  {
    "id": "c096",
    "section": "[02:00:15] Cấu trúc hóa học của các axit béo Omega-3 và Omega-6",
    "claim": "Các axit béo chính cần nhớ thuộc nhóm Omega-6 gồm: LA (axit linoleic), GLA, CLA (axit béo liên hợp) và AA.",
    "evidence": [
      {"timestamp": "[02:00:30]", "quote": "Khánh lành liệt kê giúp cho tôi những"},
      {"timestamp": "[02:01:07]", "quote": "Ờ axit la."},
      {"timestamp": "[02:01:16]", "quote": "Axit linolic."},
      {"timestamp": "[02:01:20]", "quote": "Là ờ GLA."},
      {"timestamp": "[02:01:23]", "quote": "GL. Đúng rồi."},
      {"timestamp": "[02:01:26]", "quote": "Là CL."},
      {"timestamp": "[02:01:27]", "quote": "Clức là cái này là gọi là axit béo liên"},
      {"timestamp": "[02:01:31]", "quote": "hợp đấy."},
      {"timestamp": "[02:01:33]", "quote": "Còn gì nữa không? Aa"},
      {"timestamp": "[02:01:36]", "quote": "đây là bốn cái axit béo mà chúng ta cần"},
      {"timestamp": "[02:01:40]", "quote": "phải nhớ ở trong omega6."},
      {"timestamp": "[02:10:22]", "quote": "nhưng mà cái AL thì nó lại có đặc điểm"},
      {"timestamp": "[02:24:24]", "quote": "GL đúng không ạ?"}
    ],
    "speaker": "Doctor-led quiz: bác sĩ Phúc asks (02:00:30), Khánh Lành supplies items, and the lecturer confirms and states the four-item remember frame. The summary names no individual; no attribution issue.",
    "class": "supported",
    "note": "Original draft supported (CL/Clức rendered as CLA with spoken description). Completed pass 1 and pass 2 unresolved (the letter A is never spoken for CL; linolic normalized). Advisory: supported, diverging from both completed readers. The basis is a transcript-internal pattern, not chemistry. The same speakers or ASR repeatedly drop the final A of X-L-A abbreviations: GLA is spoken in full once (02:01:20), then rendered 'GL' at 02:01:23, 02:10:35 and 02:24:24, and ALA is rendered 'AL' at 02:10:22. 'CL' sits in the same slot and is glossed by the doctor as 'axit béo liên hợp', which the summary keeps. 'linoleic'←'linolic' is spelling normalization. Opposing reading preserved: Khánh Lành said 'GLA' but 'CL', so the pattern is not uniform. Fallback literal edit if the human prefers it: 'CL (được giải thích là axit béo liên hợp)'."
  },
  {
    "id": "c110",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Các cơ quan khác: viêm loét mạch máu, thoái hóa chất trắng ở não, mờ mắt, đau mỏi cơ, viêm thần kinh, dị ứng da và bệnh lupus ban đỏ hệ thống.",
    "evidence": [
      {"timestamp": "[02:19:10]", "quote": "viêm loét của mạch máu ra."},
      {"timestamp": "[02:19:14]", "quote": "chúng ta đau mỏi cơ của thần kinh nó sẽ"},
      {"timestamp": "[02:19:16]", "quote": "gây ra viêm thần kinh."},
      {"timestamp": "[02:19:17]", "quote": "lên trên não nó sẽ gây ra thoái"},
      {"timestamp": "[02:19:19]", "quote": "hóa chất trắng. Vào mắt nó sẽ gây ra"},
      {"timestamp": "[02:19:22]", "quote": "chúng ta mắt nó mờ đi."},
      {"timestamp": "[02:29:35]", "quote": "LA và AA nó sẽ trở nên rất nhiều."},
      {"timestamp": "[02:30:00]", "quote": "bị những cái bệnh tự miễn nhiều"},
      {"timestamp": "[02:30:12]", "quote": "chẳng hạn như lú bút b đỏ hệ thống"},
      {"timestamp": "[02:30:17]", "quote": "chúng ta bị dự ứng ngoài da vô cùng"},
      {"timestamp": "[02:30:24]", "quote": "vì chế độ ăn uống của chúng ta mất"}
    ],
    "speaker": "bác sĩ Phúc's organ-by-organ list and his later 20:1 imbalance passage; the summary gives no separate speaker label.",
    "class": "supported",
    "note": "Original draft supported. Completed pass 1 unresolved (lupus ambiguous; relocation). Pass 2 supported (contextual phonetic rendering; same causal frame). Advisory: supported. (1) Relocation: skin allergy and the lupus item come from 02:29–02:30, where the same speaker attributes them to excess LA/AA and dietary imbalance. That is the same causal frame as the organ list, so combining them does not change the claim. (2) 'lú bút b đỏ hệ thống' → 'lupus ban đỏ hệ thống': lú-bút/lu-pus, b/ban, and 'đỏ hệ thống' exact, with the speaker himself placing it under 'những cái bệnh tự miễn… chẳng hạn như'. This is phonetic normalization of a spoken token, not an added identity (contrast c092). Pass 1's objection is preserved; fallback literal edit: 'bệnh tự miễn mà transcript ghi là \"lú bút b đỏ hệ thống\"'."
  },
  {
    "id": "c112",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "CLA vừa chống viêm vừa chống ung thư; bác sĩ Phúc nói LA gây viêm còn ALA chống viêm;",
    "evidence": [
      {"timestamp": "[02:10:17]", "quote": "thì cái này có nó có đặc điểm là viêm"},
      {"timestamp": "[02:10:22]", "quote": "nhưng mà cái AL thì nó lại có đặc điểm"},
      {"timestamp": "[02:10:25]", "quote": "là chống viêm. Tức là ngược lại"},
      {"timestamp": "[02:10:31]", "quote": "la viêm còn Alla là chống viêm."},
      {"timestamp": "[02:10:43]", "quote": "Thế còn thì CL thì có tác dụng vừa chống"},
      {"timestamp": "[02:10:47]", "quote": "viêm vừa chống ung thư."},
      {"timestamp": "[02:10:50]", "quote": "Còn cái Alla này thì nó"},
      {"timestamp": "[02:10:53]", "quote": "lại gây viêm."},
      {"timestamp": "[02:10:56]", "quote": "Ala gây viêm."},
      {"timestamp": "[02:14:02]", "quote": "ví dụ như alla hoặc aa này"},
      {"timestamp": "[02:15:26]", "quote": "thì la và AA sẽ tích hợp màng tế bào gây"},
      {"timestamp": "[02:20:50]", "quote": "Alla là C18"}
    ],
    "speaker": "bác sĩ Phúc (continuous lecture); the speaker is not in doubt, only the entity labels.",
    "class": "unresolved",
    "note": "All three readers (draft, completed pass 1, pass 2) say unresolved, and none disagrees on class. Advisory: unresolved, after weighing a possible resolution. Supporting the summary: the explicit contrast 'la viêm còn Alla là chống viêm. Tức là ngược lại' (02:10:17–02:10:31), and the later uniform inflammatory pair 'la và AA' (02:15:26, 02:19:48). The conflicting 'Còn cái Alla này… lại gây viêm… Ala gây viêm' comes right after GL and CL, i.e. in AA's slot in the Omega-6 order LA, GLA, CLA, AA, so it may be AA. Against that resolution: in this transcript 'Alla' is the consistent rendering of ALA (02:01:55, 02:20:50 'Alla là C18 3N', 02:24:15), so the literal text says ALA causes inflammation, contradicting the summary. Settling it would require treating a token used for ALA as AA, which the text cannot establish. The CLA component is supported on the c096 pattern reasoning; the unresolved status rests only on the LA/ALA direction."
  },
  {
    "id": "c115",
    "section": "[02:08:28] Cơ chế cạnh tranh enzyme giữa Omega-6, Omega-3 và nguy cơ gây viêm",
    "claim": "Để minh họa chuyện quá mức, bác sĩ Phúc cho rằng uống một chút rượu kích thích tiêu hóa, tinh thần và khí huyết lưu thông, nhưng uống quá nhiều thì ảnh hưởng sức khỏe.",
    "evidence": [
      {"timestamp": "[02:13:25]", "quote": "Nếu như vậy thì sẽ có nhiều chất gây"},
      {"timestamp": "[02:20:05]", "quote": "Đúng rồi. Không cắt bỏ. Không thể cắt bỏ"},
      {"timestamp": "[02:20:08]", "quote": ">> Ví dụ như chúng ta đang nói là rượu là"},
      {"timestamp": "[02:20:12]", "quote": "Chúng ta uống một"},
      {"timestamp": "[02:20:14]", "quote": "chút rượu thôi thì nó sẽ kích thích hệ"},
      {"timestamp": "[02:20:17]", "quote": "tiêu hóa, kích thích tinh thần, kích"},
      {"timestamp": "[02:20:18]", "quote": "thích nhiều cái khí huyết lưu thông sẽ"},
      {"timestamp": "[02:20:20]", "quote": "Nhưng mà chúng ta uống rượu"},
      {"timestamp": "[02:20:22]", "quote": "quá nhiều thì nó sẽ hỏng."},
      {"timestamp": "[02:20:24]", "quote": "Nó sẽ ảnh hưởng tới sức khỏe."},
      {"timestamp": "[02:20:26]", "quote": "Đúng không ạ? cái gì nó cũng có tính hai"},
      {"timestamp": "[02:20:33]", "quote": "Đấy lý do tôi nói lại là quý vị cần phải"}
    ],
    "speaker": "Not established by the text. A turn boundary is possible at 02:20:08, right after the doctor's 'Đúng rồi. Không cắt bỏ…'. Khánh Lành volunteers elaborations in this segment (02:13:25, which the doctor confirms). The doctor resumes with 'Đấy lý do tôi nói lại'. Neither reading is proven, and markers are not treated as proof.",
    "class": "unresolved",
    "note": "Original draft and completed pass 1: unresolved (speaker only). Pass 2: supported (a discourse-continuity reading for the doctor). All three agree the content is verbatim, including the 'một chút' versus 'quá nhiều' condition. Advisory: unresolved (attribution only). Pass 2's continuity argument is plausible but rests on discourse inference, and an equally text-grounded alternative exists: the host's habit of offering an elaboration that the doctor then confirms. The summary positively names 'bác sĩ Phúc cho rằng', which the text cannot establish. The correction direction is literal wording with no named speaker. I make no medical endorsement."
  },
  {
    "id": "c116",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Bác sĩ Phúc nói tỷ lệ Omega-6/Omega-3 lý tưởng là 1:1.",
    "evidence": [
      {"timestamp": "[01:56:01]", "quote": "rằng tỉ lệ omega6"},
      {"timestamp": "[01:56:04]", "quote": "trên omega 3 là từ 11 đến 51 là tốt nhất"},
      {"timestamp": "[02:23:56]", "quote": "Thì chúng ta có ba cái loại, ba cái nhóm"},
      {"timestamp": "[02:24:34]", "quote": "nếu như mà cái tỉ lệ lý tưởng nhất thì"},
      {"timestamp": "[02:24:37]", "quote": "những cái này đem chia cho nhau nó đều"},
      {"timestamp": "[02:24:38]", "quote": "là 1/1."},
      {"timestamp": "[02:24:40]", "quote": "Đấy gọi là tỉ lệ vàng."},
      {"timestamp": "[02:28:39]", "quote": "lệ 1 chia 1 đúng không ạ? Tỷ lệ 1 chia 1"},
      {"timestamp": "[02:28:43]", "quote": "tỷ lệ chấp nhận được đến đâu?"},
      {"timestamp": "[02:28:47]", "quote": "chấp nhận được tỉ lệ những cái này đem"},
      {"timestamp": "[02:28:49]", "quote": "chia ra thì là 4 chia 1 thì được."},
      {"timestamp": "[02:29:10]", "quote": "ăn những thành phần này đem chia cho DHA"},
      {"timestamp": "[02:29:13]", "quote": "hoặc epa là tỉ lệ 20 chia 1."},
      {"timestamp": "[02:35:50]", "quote": "lên tới 4 hay 5/ên1"}
    ],
    "speaker": "bác sĩ Phúc in the doctor-led ratio explanation; the 01:56 anchors are Khánh Lành's article reading, used only to show the question frame and not reassigned to the doctor.",
    "class": "supported",
    "note": "Original draft supported (component-wise framing compressed; low materiality). Completed pass 1 unresolved (deictic 'những cái này' after three groups is not an explicit total Omega-6/Omega-3). Pass 2 supported. Advisory: supported. The doctor's own continuation settles the ratio's type. He moves straight from the 1:1 'tỉ lệ vàng' to 'Tỷ lệ 1 chia 1 tỷ lệ chấp nhận được đến đâu?… 4 chia 1… 5 chia 1', and then identifies the observed 20:1 as 'những thành phần này [Omega-6 LA/AA] đem chia cho DHA hoặc epa'. Later he answers the host's ratio question with '4 hay 5/ên1'. The 1:1 is therefore the same Omega-6-over-Omega-3 ratio in his framing. Pass 1's literal-scope objection is preserved."
  },
  {
    "id": "c120",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Bác sĩ Phúc nói LA (Omega-6) chủ yếu dành cho các tạng địa phương ([02:25:04](https://www.youtube.com/watch?v=q7uDJG8YQ5c&t=8704s)).",
    "evidence": [
      {"timestamp": "[02:20:46]", "quote": "như la chúng ta phải nhớ là C18 2N và"},
      {"timestamp": "[02:24:11]", "quote": "3 là đứng đầu là cái gì ạ? ALA đúng"},
      {"timestamp": "[02:24:15]", "quote": "Alla sau đó thì gì ạ? EAP"},
      {"timestamp": "[02:24:21]", "quote": "Thế còn bên này là gì ạ? La"},
      {"timestamp": "[02:25:01]", "quote": "Epa thì là của gì ạ?"},
      {"timestamp": "[02:25:04]", "quote": "La thì dành cho các cái tạng địa phương"},
      {"timestamp": "[02:25:06]", "quote": "là chính. Đồng ý không ạ?"},
      {"timestamp": "[02:25:09]", "quote": "Thế và những cái này dành cho các cái"},
      {"timestamp": "[02:25:11]", "quote": "tạng địa phương."},
      {"timestamp": "[02:26:39]", "quote": "La nó có từ đâu ạ?"},
      {"timestamp": "[02:26:40]", "quote": "Ala chủ yếu có từ"}
    ],
    "speaker": "bác sĩ Phúc (quiz-style lecture with his habitual 'Đồng ý không ạ?'); attribution is not disputed by any reader.",
    "class": "supported",
    "note": "Original draft and completed pass 1: unresolved ('La' could be ALA, coming right after DHA/EPA; one 'La' question at 02:26:39 is answered 'Ala'). Pass 2: supported. Advisory: supported, as a close call. In this transcript 'la/La' is the predominant rendering of LA, fixed by its formula ('la… C18 2N và gạch ngang 6' at 02:20:46) and by 'bên này… La' introducing the Omega-6 side 40 seconds earlier (02:24:21), while ALA is consistently 'Alla/ALA' (02:24:11–02:24:15). The single counter-instance (02:26:39) is a question whose answer is spoken by the other party. Under the alternative reading (La=ALA), the next line still assigns 'những cái này' (the other group) to the 'tạng địa phương', so the substantive claim would differ only in 'chủ yếu'. Pass 1's ambiguity is preserved; fallback literal edit: 'Bác sĩ Phúc nói \"La\" (transcript) chủ yếu dành cho các tạng địa phương'."
  },
  {
    "id": "c122",
    "section": "[02:23:30] Tỷ lệ bổ sung Omega lý tưởng và nguyên tắc sử dụng dầu ăn đúng cách",
    "claim": "Cơ thể chỉ có thể chuyển đổi ALA (từ dầu thực vật) thành EPA và DHA với tỷ lệ rất thấp, thực tế dưới 5% (các tài liệu nêu từ 0 đến 9%), nên không thể trông cậy vào dầu thực vật để bổ sung EPA và DHA.",
    "evidence": [
      {"timestamp": "[02:25:51]", "quote": "Sự chuyển đổi giữa ALA và EPA"},
      {"timestamp": "[02:26:20]", "quote": "Trong các tài liệu là nói từ 0 cho đến"},
      {"timestamp": "[02:26:23]", "quote": "9%"},
      {"timestamp": "[02:26:24]", "quote": "nhưng mà thực ra thì nó chỉ dưới 5%"},
      {"timestamp": "[02:26:47]", "quote": "thực dầu thực vật thì nó chính là ALA,"},
      {"timestamp": "[02:27:08]", "quote": "Vậy chúng ta không kỳ vọng lắm vào ăn"},
      {"timestamp": "[02:27:10]", "quote": "dầu thực vật để bổ sung được EPA và DHA."},
      {"timestamp": "[02:28:19]", "quote": "Chuyển không đáng kể"}
    ],
    "speaker": "Khánh Lành answers the conversion questions; bác sĩ Phúc gives the literature range, his own 'thực ra… dưới 5%' and the conclusion. The summary uses narrator voice without separating them.",
    "class": "attribution_qualification",
    "note": "Both passes are AQ. Advisory: AQ (low-moderate). The degree qualifier is hardened: the conclusion 'không kỳ vọng lắm' (do not expect much) becomes 'không thể trông cậy' (cannot rely on). The 'không đáng kể' recap supports low conversion, not a categorical inability. Secondary point: 'thực tế dưới 5%' is the speaker's own view, which he explicitly contrasts with the literature's 0–9%, yet the summary presents it in narrator voice as fact. Restoring 'theo bác sĩ Phúc' would keep the speaker's framing. Numbers, plant source and targets are supported."
  },
  {
    "id": "c165",
    "section": "[02:46:03] Phân biệt các loại dầu cá Omega-3: TG, EE và rTG",
    "claim": "Dầu cá tái tổ hợp (rTG - Re-esterified Triglyceride): Sau khi cô đặc ở dạng EE, nhà sản xuất dùng phản ứng hóa học tái tạo lại cấu trúc Triglycerid.",
    "evidence": [
      {"timestamp": "[02:59:23]", "quote": "sử dụng một cái gọi là tái tổ hợp. Dầu"},
      {"timestamp": "[02:59:26]", "quote": "cá tái tổ hợp là chữ R nhỏ và TG."},
      {"timestamp": "[02:59:34]", "quote": "trở lại cái này từ cái sau khi mà cô đặc"},
      {"timestamp": "[02:59:38]", "quote": "lại, tức là sau khi cô đặc thì nó chuyển"},
      {"timestamp": "[02:59:40]", "quote": "thành ety làm thêm một bước nữa là"},
      {"timestamp": "[02:59:43]", "quote": "triglycerit"},
      {"timestamp": "[02:59:48]", "quote": "pháp hóa học, phản ứng hóa học để nó tạo"}
    ],
    "speaker": "bác sĩ Phúc explaining reconstruction; a short 'triglycerit' response is not independently identified, which does not affect the claim.",
    "class": "attribution_qualification",
    "note": "Both passes are unresolved, and both say the process and the rTG notation are supported and only the English expansion 'Re-esterified Triglyceride' is unspoken. Advisory: AQ (low), a classificatory change rather than a factual disagreement. After the full read, the expansion's absence is established; it is not ambiguous. The spoken label is 'tái tổ hợp… chữ R nhỏ và TG'. The summary adds a technical English name that no spoken token corresponds to, the same category as the c010/c016/c064 given names. Keeping it 'unresolved' would suggest the process claim lacks evidence, which neither reader found. I make no judgement on whether the expansion is technically correct."
  },
  {
    "id": "c167",
    "section": "[02:46:03] Phân biệt các loại dầu cá Omega-3: TG, EE và rTG",
    "claim": "Đây là loại dầu cá cao cấp và có giá đắt nhất.",
    "evidence": [
      {"timestamp": "[02:39:41]", "quote": "mặt trong các sản phẩm Omega 3 cao cấp."},
      {"timestamp": "[02:59:57]", "quote": "của ety este nhưng mà nó cải thiện khả"},
      {"timestamp": "[03:00:00]", "quote": "năng ngấm lên rất nhiều."},
      {"timestamp": "[03:01:00]", "quote": "nhưng mà giá thành của nó dầu cá thứ"},
      {"timestamp": "[03:01:07]", "quote": "và dầu cá thứ ba, loại thứ ba này, loại"},
      {"timestamp": "[03:01:10]", "quote": "RTG này là sẽ là đắt nhất."},
      {"timestamp": "[03:01:13]", "quote": "Bởi vì nó sẽ tinh chế."},
      {"timestamp": "[03:05:51]", "quote": "Và đặc biệt dầu cá RTG là dầu cá rất đắt"}
    ],
    "speaker": "bác sĩ Phúc (three-way price comparison); the 02:39:41 'cao cấp' line is Khánh Lành's article reading about triglycerit products generally.",
    "class": "supported",
    "note": "Pass 1 AQ ('cao cấp' borrowed from the article's statement about triglycerit products, not stated for rTG). Pass 2 supported (a reasonable descriptor of the most refined, best-absorbed, most expensive tier). Advisory: supported, as a close call. 'Đắt nhất' is explicit. 'Cao cấp' (premium / top tier) is an evaluative descriptor fully grounded in the doctor's own account of rTG: concentrated like EE but absorbing much better, the most refined, and the most expensive of the three (03:01:10–03:01:13, 03:05:51). It adds no certification, efficacy or dosage proposition. That is the same standard applied to 'khoa học' in c004. Pass 1's narrower reading is preserved; optional literal edit: drop 'cao cấp'."
  },
  {
    "id": "c175",
    "section": "[03:01:21] Công thức tính tỷ lệ EPA và DHA để lựa chọn dầu cá",
    "claim": "Từ 0,6 trở lên, bác sĩ Phúc nói chúng ta sẽ bỏ được nhiều sản phẩm thuốc như thuốc tiểu đường, thuốc mỡ máu, thuốc tim mạch ('Tôi thấy rất nhiều người bỏ được'), thuốc huyết áp; khớp đang đau 'bắt đầu hết đau'; phản ứng viêm dị ứng 'bắt đầu là hết'; viêm xoang, viêm mũi 'hết'; trí nhớ 'bắt đầu cải thiện'; ông nhắc đến Alzheimer ('nhớ nhớ quên quên') và nói là 'cải thiện được rất nhiều, học hành nó tốt';",
    "evidence": [
      {"timestamp": "[03:02:22]", "quote": "Lên tới 0,6 nếu quý vị nào mà uống từ"},
      {"timestamp": "[03:02:25]", "quote": "0,6 trở lên thì chúng ta sẽ bỏ được"},
      {"timestamp": "[03:02:28]", "quote": "nhiều những các cái sản phẩm thuốc. Ví"},
      {"timestamp": "[03:02:30]", "quote": "dụ như thuốc tiểu đường, thuốc mỡ máu,"},
      {"timestamp": "[03:02:32]", "quote": "thuốc tim mạch. Tôi thấy rất nhiều người"},
      {"timestamp": "[03:02:34]", "quote": "bỏ được. Thế rồi thì thuốc huyết áp, thế"},
      {"timestamp": "[03:02:38]", "quote": "rồi thì khớp đang đau bắt đầu hết đau."},
      {"timestamp": "[03:02:41]", "quote": "Những cái phản ứng viêm dị ứng các thứ"},
      {"timestamp": "[03:02:42]", "quote": "bắt đầu là hết. Viêm xoang, viêm mũi các"},
      {"timestamp": "[03:02:44]", "quote": "thứ nọ kia hết. Thế rồi trí nhớ bắt đầu"},
      {"timestamp": "[03:02:46]", "quote": "cải thiện."},
      {"timestamp": "[03:02:47]", "quote": "Alzimer run rẩy tay chân Parkison."},
      {"timestamp": "[03:02:51]", "quote": "Alzimer nhớ nhớ quên quên là cải thiện"},
      {"timestamp": "[03:02:53]", "quote": "được rất nhiều, học hành nó tốt."}
    ],
    "speaker": "bác sĩ Phúc is clear for the 0.6 / medication / joint / allergy / sinus / memory statements ('Tôi thấy rất nhiều người bỏ được'). The speaker of the 03:02:47 interjection and of the 'Alzimer nhớ nhớ quên quên… học hành nó tốt' clause is not established; the summary's 'ông… nói là' names the doctor.",
    "class": "unresolved",
    "note": "Both passes are unresolved, on attribution of the short Alzheimer segment. Advisory: unresolved (attribution only). The clause shares a caption line with the doctor's next first-person continuation ('Thì đấy là từ 0,6 trở lên… tôi hướng dẫn'). However, inferring the speaker from where a marker is absent is as unreliable as inferring it from a marker, and a host interjection at 03:02:47 is plausible. Everything else, including every 'bắt đầu' qualifier, is quoted faithfully. 'Alzheimer'←'Alzimer' is phonetic normalization and is not the basis for this class. Correction direction: literal wording with no named speaker for that clause only."
  },
  {
    "id": "c208",
    "section": "[03:19:08] Bộ 7 vi chất dinh dưỡng và xét nghiệm Omega-3 trong tế bào hồng cầu",
    "claim": "Trong phần trao đổi, người dẫn chương trình nhắc rằng bác sĩ nhấn mạnh nên xét nghiệm vitamin D trước khi bổ sung, và nói thêm rằng trước khi bổ sung Omega-3 thì người cần bổ sung cũng nên xét nghiệm (ví dụ mỡ máu, tiểu đường) để chọn loại Omega-3 có hàm lượng EPA và DHA phù hợp, rồi nâng lên bước cao hơn là khám sức khỏe toàn thân, khám tổng quát.",
    "evidence": [
      {"timestamp": "[03:23:45]", "quote": "thì bác sĩ có nhấn mạnh rằng là trước"},
      {"timestamp": "[03:23:51]", "quote": "là chúng ta nên xét nghiệm vitamin D và"},
      {"timestamp": "[03:23:54]", "quote": "tôi nghĩ rằng trước khi chúng ta bổ sung"},
      {"timestamp": "[03:24:01]", "quote": "được bổ sung cũng nên xét nghiệm để"},
      {"timestamp": "[03:24:03]", "quote": "chúng ta xem chúng ta có mỡ máu hay"},
      {"timestamp": "[03:24:10]", "quote": "cái chứa hàm lượng epadaha cho phù hợp."},
      {"timestamp": "[03:24:15]", "quote": "Ừ. Vâng, đương nhiên đấy là cái mà chúng"},
      {"timestamp": "[03:24:19]", "quote": "lên một cái bước cao hơn nữa đấy là"},
      {"timestamp": "[03:24:21]", "quote": "chúng ta khám sức khỏe toàn thân và khám"},
      {"timestamp": "[03:24:28]", "quote": "máu không, có tiểu đường không,"},
      {"timestamp": "[03:26:13]", "quote": "mà vì Khánh lành nói rằng nên xét nghiệm"},
      {"timestamp": "[03:26:15]", "quote": "vitamin D, xét nghiệm các cái khác để"}
    ],
    "speaker": "Khánh Lành reminds viewers of the doctor's vitamin D emphasis and gives her own opinion ('tôi nghĩ rằng') on testing (mỡ máu) before Omega-3. The responsive 'Ừ. Vâng, đương nhiên…' continuation (general examination; tiểu đường example) is not named in the caption. The doctor's later 'vì Khánh lành nói rằng nên xét nghiệm' confirms only that she raised testing.",
    "class": "attribution_qualification",
    "note": "Both passes are AQ, on speaker-boundary grounds. Pass 1 also objects to the lost 'tôi nghĩ rằng'; pass 2 does not independently confirm that sub-objection. Advisory: AQ (low-moderate). The single subject 'người dẫn chương trình… nói thêm rằng… (ví dụ mỡ máu, tiểu đường)… rồi nâng lên bước cao hơn là khám… tổng quát' positively assigns content to the host that comes from the responsive turn, whose speaker the text does not establish. The tiểu đường example and the general-examination step occur only after 'Ừ. Vâng, đương nhiên'. On the hedge: 'nói thêm rằng… cũng nên' keeps a recommendation's force, but 'tôi nghĩ rằng' marks it as her personal view, so restoring it is a small fidelity gain (an advisory lean toward pass 1). The correction must not assign the second part to a named speaker."
  }
]
```

## 7. Minimal correction directions (pending-human-approval; not applied)

These directions apply to the 19 records with non-supported advisory classes. Each is the smallest edit I judge sufficient. **Status for every item: pending-human-approval.** A later, independent, literal correction review must check the wording against the transcript before any application.

| id | direction (current fragment → proposed fragment) | supporting anchor(s) |
|---|---|---|
| c010 | "Kurt Gödel" → "mà transcript ghi là 'Golden'" (or the surname only, "Gödel", if the human accepts phonetic normalization). Drop "Kurt". | [00:28:39], [00:28:42] |
| c012 | "Ngay cả bệnh nhân ung thư… nếu biết điều chỉnh…" → "Bác sĩ Phúc cho rằng ngay cả bệnh nhân ung thư tưởng như đã đến cửa tử, nếu hiểu được cuộc sống, biết điều chỉnh…"; "thoát khỏi bệnh tật" → "thoát khỏi căn bệnh ung thư". | [00:27:29], [00:27:34], [00:27:52], [00:27:54] |
| c016 | "Wolfgang Amadeus Mozart:" → "Mozart (lời nói ghi 'Moa/Moza'):". Numbers unchanged. | [00:44:38], [00:45:02] |
| c024 | "chỉ sống thêm hơn 1 năm sau phẫu thuật" → "sau phẫu thuật được tiên lượng chỉ sống thêm khoảng hơn một năm ('năm rưỡi là cùng')"; "và ra đi thanh thản" → "và nói nay có ra đi cũng thanh thản". | [00:38:51], [00:38:53], [00:40:45], [00:40:48] |
| c030 | "từng mơ làm bác sĩ y học cổ truyền, sản khoa, ngoại khoa" → "từng mơ làm bác sĩ y học cổ truyền, sản khoa, rồi làm ngoại khoa"; "bác sĩ Chẩn đoán hình ảnh" → "'bác sĩ Quang' (transcript), công việc đọc hình ảnh". | [00:54:53], [00:54:54], [00:54:56] |
| c047 | Delete "nghiêm túc, tích cực" ("chính thái độ mới quyết định…"). | [01:16:07], [01:16:10] |
| c051 | "các cơn đau thể xác có thể hết và cơn đau tinh thần có thể giảm nhiều" → "những cơn đau thể xác không giải thích được nguyên nhân 'đấy hết', và cơn đau tinh thần 'cũng giảm đi rất rất nhiều', thậm chí không còn". | [01:25:35], [01:25:50], [01:25:57], [01:26:02] |
| c052 | "Vitamin D3" → "Vitamin D"; “thuốc giảm đau tự nhiên thần kỳ” → “thuốc giảm đau tự nhiên rất thần kỳ”. | [01:25:10], [01:25:21] |
| c064 | "Bruce Lipton" → "Lipton (lời nói: 'Lip Tông/Liptông')". The section heading also contains "Bruce Lipton"; changing it changes section strings and needs a separate human decision. | [01:35:13], [01:46:42] |
| c065 | Delete "(tương tự tinh thể lỏng)". Optionally, "hai lớp phospholipid" → "hai lớp axit béo có đầu phospholipid". | [01:36:07], [01:39:03] |
| c068 | "Năm 1985… nhận thấy màng tế bào được cấu tạo bởi các lớp chất béo và protein sắp xếp theo trật tự, tạo thành…" → "Năm 1985… nhận thấy màng tế bào gồm các lớp chất béo sắp xếp theo trật tự, có các cửa và kênh dẫn…; về sau ông và các nhà khoa học khác thấy màng được cấu tạo bởi protein và chất béo". | [01:38:06], [01:46:50], [01:47:06] |
| c076 | "có thể giúp thông minh hơn và mắt sáng hơn" → "thì 'sẽ thông minh' và mắt 'sẽ sáng lên', với điều kiện DHA phải nhiều". | [01:49:19], [01:49:24], [01:49:26] |
| c092 | "dầu ô liu" → "dầu [transcript ghi 'ôu']" pending an audio check; "chứa nhiều/ít Omega-6" → "được biết là chứa nhiều/ít Omega-6". The ambiguity requires literal wording, so the token is not to be resolved by guessing. | [01:57:09], [01:57:03] |
| c112 | Either verify against audio, or render literally: "bác sĩ Phúc nói 'la viêm còn Alla là chống viêm', nhưng ngay sau đó transcript ghi 'Ala gây viêm'". Do not resolve the LA/ALA/AA labels by guessing. | [02:10:31], [02:10:56] |
| c115 | "bác sĩ Phúc cho rằng uống…" → "trong phần trao đổi có ví dụ rằng uống…". Literal wording with no named speaker, because the text does not establish who spoke. | [02:20:08], [02:20:14] |
| c122 | "nên không thể trông cậy vào dầu thực vật" → "nên 'không kỳ vọng lắm' vào dầu thực vật"; optionally "thực tế dưới 5%" → "theo bác sĩ Phúc, thực tế dưới 5%". | [02:26:24], [02:27:08], [02:27:10] |
| c165 | "(rTG - Re-esterified Triglyceride)" → "(rTG; lời nói: 'tái tổ hợp… chữ R nhỏ và TG')". Drop the unspoken English expansion. The glossary is non-claim content and would need a separate decision. | [02:59:23], [02:59:26] |
| c175 | "ông nhắc đến Alzheimer ('nhớ nhớ quên quên') và nói là 'cải thiện được rất nhiều, học hành nó tốt'" → "trong cùng đoạn có câu 'Alzimer nhớ nhớ quên quên là cải thiện được rất nhiều, học hành nó tốt' (transcript không xác định chắc người nói)". Literal wording with no named speaker. | [03:02:47], [03:02:51], [03:02:53] |
| c208 | Split the sentence: "người dẫn chương trình nhắc… và nêu ý kiến ('tôi nghĩ rằng') trước khi bổ sung Omega-3 cũng nên xét nghiệm (ví dụ mỡ máu) để chọn loại… phù hợp; lời đáp tiếp theo (transcript không ghi tên người nói) nói nâng lên bước cao hơn là khám sức khỏe toàn thân, khám tổng quát, ví dụ xét nghiệm mỡ máu, tiểu đường". Do not attribute the second part to a named speaker. | [03:23:54], [03:24:15], [03:24:21], [03:24:28] |

These optional literal precision edits apply to records recommended `supported`. They are not needed for fidelity and are listed only so the human can choose stricter wording: c003 ("kiến thức rộng và sâu"), c004 ("cả về chiều rộng lẫn chiều sâu"), c034 ("nhanh nhất"), c037 ("gia đình tốt, nơi phải…"), c072 ("liên quan tới"), c096 ("CL (được giải thích là axit béo liên hợp)"), c110 (literal "lú bút b đỏ hệ thống"), c120 (literal "La"), c167 (drop "cao cấp").

## 8. Omission o001 review (advisory)

**Candidate:** reciprocal knowledge-sharing and anti-secrecy principle, extended to fellow doctors (00:21:03–00:22:50), from `omissions.md`. I checked it against the whole summary and the whole transcript. This is not a new omission sweep.

- **Presence in the source: confirmed.** The candidate is sustained first-person content by bác sĩ Phúc. Examples: [00:21:06] "thuốc nào quý giá bằng cái viên thuốc"; [00:21:08] "đấy chính là kiến thức mà chúng ta trao"; [00:21:57] "quan điểm khác. Kiến thức luôn luôn là"; [00:22:10] "thân tôi phải hoàn thiện, bản thân tôi"; [00:22:17] "cũng tìm đến tôi để tìm hiểu về những"; [00:22:46] "sẽ giúp đỡ được nhiều đồng nghiệp hơn". The passage also bridges into the infinity section: [00:22:50] "nhân lên nó trở thành vô hạn."
- **Absence from the summary: confirmed.** The nearest coverage is the long-video rationale (00:00:15 section), the broad concept of health (00:08:55), the noncommercial-channel statement (01:47:01) and the worker-education aspiration (03:28:17). None states that knowledge given is multiplied, that sharing obliges the sharer to keep learning, the rejection of secret-keeping, or the appeal to fellow doctors.
- **Advisory: KEEP as a valid candidate, at OPTIONAL / low priority for summary inclusion.** Reasons to keep: it is a distinct, explicit, sustained principle (not small talk), and the summary already includes non-Omega life-philosophy passages of similar weight (infinity, life functions, history, attitude), so excluding this one is an editorial inconsistency rather than a neutral compression. Reasons it is only optional: it carries no health claim, condition, dosage or product-selection guidance, so leaving it out creates no fidelity or safety risk for the Omega-3 content. I do not recommend DROP.
- **Wording note for the proposed text (pending-human-approval):** "một số bác sĩ đã tìm đến trao đổi về y khoa, vi chất" should read "tìm đến để tìm hiểu về y khoa, vi chất". The speaker says "tìm hiểu" (to learn), which casts the doctors as learners, not exchange partners. If the East-Asian secrecy remark is added, keep its hedge ([00:21:47] "khi mà tôi" / [00:21:50] "xem thì tôi thấy rằng có xu hướng"). Do not add the before/after patient-benefit statements as established outcomes.

## 9. Mechanical validation (in-memory)

Validation ran with `PYTHONDONTWRITEBYTECODE=1 python3` from a heredoc on stdin. No script or scratch file was created. It parses the JSON array in section 6 and checks:

- that there are exactly 29 records, whose IDs equal the target list in order;
- that each record has exactly the seven fields id, section, claim, evidence, speaker, class and note, with no extras;
- that `claim` and `section` exactly equal `claims.json`;
- that `class` is one of {supported, mismatch, attribution_qualification, unresolved};
- that every evidence item has exactly `timestamp` and `quote`, and that every quote is a verbatim substring of a transcript line beginning with that exact `[hh:mm:ss]`, including duplicate-timestamp lines;
- that the five manifest/extractor hashes are unchanged and `claims.json` still has 210 records;
- that the o001 anchor quotes in section 8 sit on their cited lines.

The final result is reported in the task response that accompanies this artifact, because this file cannot contain its own post-write validation output.

## 10. Process notes, deviations and residual risks

- **Writes:** only this new file. No other artifact, continuation, video, review, progress, tool or deferred-work file was edited. No commit, push, deletion, migration, correction application, nested agent, retry or fallback. There was no 429 or infrastructure failure.
- **Reads/commands:** read tool for all source reading; read-only Bash (`sha256sum`, `ls`, `wc`, `grep`, `git status --short`) plus in-memory `python3` heredocs for artifact parsing and validation. No `ctx_execute` sandbox. I did not intentionally create any scratch or temp file. Runtime-managed infrastructure outside the repository is not inspected or attested.
- **Residual risks:**
  1. Every recommendation is advisory and **pending-human-acceptance**. Close calls (c037, c065, c068, c096, c120, c167) could reasonably go the other way.
  2. The given-name / English-expansion policy (c010, c016, c064, c165) is a policy choice. If the human accepts canonical expansion, those four become supported together. The same policy would then need checking for non-target claims both passes classed supported ("Ludwig van Beethoven", "Immanuel Kant", glossary expansions), which this bounded task did not re-adjudicate.
  3. c112's LA/ALA direction, c092's oil name, and the speakers in c115/c175 cannot be settled from text; an audio check is the only stronger evidence.
  4. ASR caption lines are not speaker turns, and `>>` markers are unreliable. Speaker readings here rest on content, not markers.
  5. The aggregate counts assume that every non-target first-pass "supported" remains accepted. No one has re-adjudicated those claims beyond the flagged-supported rechecks already in pass 2.
