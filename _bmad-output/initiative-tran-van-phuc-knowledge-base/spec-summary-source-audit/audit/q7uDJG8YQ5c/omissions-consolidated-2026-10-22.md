# Consolidated omission audit — q7uDJG8YQ5c

Date: 2026-10-22. **Analysis only; all decisions pending-human-approval.** No addition is approved or applied by this report. Recording a statement is not medical validation, correction, endorsement or advice, including statements about alcohol or stopping medication.

## Inputs and safeguards

Repository workspace: khoaowen/tranvanphuc-knowledge-base, khoaowen/Epic2-publish-videos; HEAD `d28dc443792a62e8b85283ea5e67ce52f5f27081`.

The requested summary hash was checked **first** and matched. The transcript hash also matches the required source. Only `transcript.md` is used as evidence of speech. Reviews and historical audits supply candidate topics, not evidence that something was said.

Paths below use V = `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/` and D = this audit directory.

| Input | Verified SHA-256 |
| --- | --- |
| V/summary.md | `04ba0755a8500d5e024f8de87027dda8ef3b67384e0eec0abec5d768e0d94ff8` |
| V/transcript.md | `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b` |
| V/review.md | `58ee9b33328c42eceb84281607e6da86724925ed5f09a6ce22a84a7fa6455d2c` |
| D/proposed-omissions.md (A) | `1666ae58654841766f13c40155f93e4e7ba38b1f686e971d7acefac10d60b8d7` |
| D/omissions-recheck.md (B) | `4c69c9619d9f4d5e7b05bd885c9a956e1056f1a042c6150195bd0b754461ef50` |
| D/omissions.md (B scope definitions) | `ef9c61dbfaeee208bcc894a66059d145b4afa6bf9888f20bb595f1a1dbd654bd` |
| D/fidelity-apply-2026-10-22.md | `92652762445317ecf6baa09bb726a6dc2286019e653b21a05b0b5d710890ce72` |
| scripts/fidelity.py | `cc570d0b53168ebce3027af755d5c2a91045faa2c4e8bd2a93f78dea2538da0d` |

The current review JSON binds to the verified current summary, unlike the older review described in the dated apply report. `review.md` already had a working-tree modification on entry; it is preserved, not reverted or overwritten. The apply report establishes the c068/c163 changes and unchanged claim numbering; it is not treated as the current review-state authority.

`fidelity.extract_claims(current_summary)` returned **194 claims, c001–c194**. Current claims were read and searched, including full-summary searches for muscle loss, alcohol, marketing/gifts, leaflets, numerical doses, channel disclosures, nuclei/hồng cầu and named diseases. Matches elsewhere were checked for the same context, not counted just because a disease or number occurs somewhere. Approved/applied text, especially c068 and c163, is not revised by any draft below. Placements mean a separate new sentence/paragraph **after the entire current claim**, never replacement or an insertion inside approved text.

B is a historical 2026-10-20 view against e8cef3b0…; its binary still-omitted bucket combined actual missing information with identity/attribution uncertainty. It is not rewritten here. A was against b60de9a9…; its proposed insertions are not carried forward automatically. C1/C2/C3 mean the three omission objects in the current review, in order.

Pre-output protected manifest: **59 existing files** under V and D; SHA-256 `c5005f4d02e0c2b34a74c52127402aac5f8783e2bd080f44acedbc025dba0b33`, computed over sorted lines `sha256  relative-path\n`. The new report is excluded from this manifest. No external/paid service, model review run, publication, git write, queue_state change or publishable change is part of this audit.

## Mapping: every A/B/C item retained

Compound historical items are split only where coverage and identity or genuinely different missing details require different decisions. Subparts are explanatory labels, not changes to the source files. B20 and the c055 comparison are retained as out-of-scope references, not re-audited fidelity questions.

| Consolidated ID | A | B | C | Atomic topic |
| --- | --- | --- | --- | --- |
| om01 | o01 | B1, observation | — | Greenland research origin |
| om02 | o02 | B1, reports | — | 15,000 reports and five properties |
| om03 | o03 | B2 | — | 600 UI versus 2000 comparison; c055 excluded |
| om04 | o04 | B3 | — | Albumin/DHA rationale; missing muscle-loss bridge |
| om05 | o05, substantive list | B4, oils | — | High/low Omega-6 oils |
| om06 | o05, unresolved name | B4, oil identity | — | Oil identity in caption |
| om07 | o06 | B4, meat/butter | — | Lean cuts, grass-fed animals, moderation |
| om08 | o07 | B6, beneficial roles | — | Omega-6 brain/reproduction/hair/skin/bone roles |
| om09 | o08, substantive effects | B7, represented effects | — | GLA/CLA/EPA/DHA profiles already represented |
| om10 | o08, name interpretation | B7, identity/ALA | — | GL/CL/Alla identity and conflicting anti-inflammatory statement |
| om11 | o09 | B6, do not eliminate Omega-6 | — | Excess-only qualification |
| om12 | — | B6, cooking-oil warning | — | Do not eliminate cooking oil |
| om13 | — | B8 | — | Alcohol moderation analogy |
| om14 | o10 | B9 | — | Reputable oil sellers and opened shelf life |
| om15 | o11 | B10 | — | Extra-ingredient advertising warning |
| om16 | o12 | — | — | Surplus DHA/EPA for other organs |
| om17 | o13 | B12, numbers | — | Natural oil example 0.06/≤0.3 |
| om18 | — | B12, advertising/gifts | — | Expensive advertised gifts still ≤0.3 |
| om19 | — | B11 | — | Optional form labels and reading leaflet |
| om20 | — | B13 | — | Krill safety requires more research |
| om21 | — | B14 | — | Skepticism about rTG absorption advertising |
| om22 | o14 | B16 | — | Doubling 0.35 versus refined 0.7 |
| om23 | o15 | B15 | — | <0.3 monitoring and possible lipid/liver effects |
| om24 | o16 | B17 | — | Vitamins D/A/E storage |
| om25 | o17 | B18 | — | Concentration by illness and avoiding imbalance |
| om26 | — | B19 | — | Children: sleep, games, videos and stated mechanism |
| om27 | — | B20 | — | Testing/check-up speaker attribution; c192 excluded |
| om28 | — | B21, availability | — | RBC test availability qualification |
| om29 | — | B21, dose variability | C2 (03:25:23) | Variable daily doses and RBC basis |
| om30 | — | B22 | — | Channel disclosures and refusing product links |
| om31 | — | — | C1 (02:29:52) | Additional diseases explicitly linked to 20:1 |
| om32 | — | — | C3 (03:26:51) | Functioning non-nucleated RBC argument |
| om33 | — | B5 | — | Article evidence caveat and fat type versus ratio |

Thus B3 ≈ o04, B4 spans o05/o06 plus an identity question, B6 spans o07/o09 plus a separate cooking-oil warning, and B21 overlaps C2 only for its dose subtopic. A-only o12 is retained as om16; C-only topics remain om31/om32.

## Context actually read

For in-scope speech passages, the cited passage and at least 60 seconds on **both** sides were read directly from the transcript. The following are the inclusive requested windows (caption times are discrete); overlapping windows serve multiple items. Excluded c055/c192 passages were encountered as context, not adjudicated.

| Read window | Items supported |
| --- | --- |
| 00:41:01–00:43:17 | om30 disclosure |
| 01:20:24–01:23:09 | om01–om02 |
| 01:26:03–01:28:37 | context only for excluded om03 |
| 01:29:08–01:32:12 | om04 |
| 01:52:28–02:00:06 | om05–om08, om30 links, om33 |
| 02:09:08–02:12:12 and 02:13:01–02:15:18 | om09–om10 |
| 02:18:53–02:21:30 | om11, om13 |
| 02:24:15–02:26:30 | om16 |
| 02:28:17–02:31:57 | om12, om31 |
| 02:31:58–02:35:24 | om14–om15 |
| 02:38:45–02:40:56 | om19 optional-label passage |
| 02:50:02–02:57:03 | om17–om18, om20 |
| 02:59:24–03:05:29 | om21–om23 |
| 03:05:02–03:07:09 | om19 leaflet passage |
| 03:07:33–03:12:19 | om23 second passage, om24 |
| 03:15:36–03:21:19 | om25–om26, om15 final reminder |
| 03:22:38–03:28:40 | om28–om29, om32; excluded om27 encountered only |

Quote ranges below are **computed caption ranges**, not inferred audio boundaries. Every displayed single-quoted fragment was checked with `scripts.fidelity.resolve_quote(quote, transcript, timestamp)`; quoted names remain transcription strings, not resolved scientific identities. A match proves text occurrence, not speaker identity or truth.

## Item-by-item decisions and minimal drafts

Importance is viewer relevance, not confidence in or approval of a health claim. For covered items it rates the topic, not a need to add it. For exclusions it does not substitute for fidelity adjudication. Every item remains **status: pending-human-approval**.

### om01 — Greenland research origin
- **Source timestamps:** 01:21:24–01:21:46. **Current claim IDs:** c053.
- **Classification:** covered. The 1970s observation and research transition are present and attributed to Khánh Lành.
- **Importance:** low — background already available, not an unresolved purchasing instruction.
- **Proposed insertion:** none. **A/o01:** no longer needed; do not duplicate c053 or infer a name correction from captions.
- **Quote → resolved:** 'kể từ những năm 1970' → 01:21:24 (PASS).
- **Status:** pending-human-approval.

### om02 — 15,000 reports and five properties
- **Source timestamps:** 01:21:49–01:22:09. **Current claim IDs:** c054.
- **Classification:** covered. Count and all five properties are present with host attribution.
- **Importance:** medium — conveys the programme’s stated evidence background, already represented.
- **Proposed insertion:** none. **A/o02:** no longer needed.
- **Quote → resolved:** '15.000 báo cáo đã chỉ ra rằng axit béo Omega 3 có đặc tính chống viêm, chống huyết khối, chống loạn nhịp tim, hạ lipit máu và giãn mạch' → 01:21:57–01:22:05 (PASS).
- **Status:** pending-human-approval.

### om03 — Vitamin D comparison, excluded fidelity item
- **Source timestamps:** 01:27:03–01:27:37 (candidate locator only). **Current claim IDs:** c055.
- **Classification:** out of scope. c055 is expressly excluded; no new attribution/qualification verdict is made. Its displayed comparison is not a fresh omission proposal.
- **Importance:** medium — dose-context wording belongs to the separate fidelity decision.
- **Proposed insertion:** none. **A/o03:** no longer needed as an omission insertion; c055’s fidelity remains separate, not approved here.
- **Quotes with resolved timestamps:** none reproduced; see related, not analysed.
- **Status:** pending-human-approval.

### om04 — Brain-fuel explanation and muscle-loss bridge
- **Source timestamps:** 01:30:08–01:31:12. **Current claim IDs:** c057–c060.
- **Classification:** partially covered. Nutrient list, albumin’s competing functions and DHA metabolism are present; missing is the dialogue linking use of protein to loss of muscle before turning to DHA.
- **Importance:** low — explanatory bridge, not a new product-selection rule.
- **Proposed insertion, after c060:** Trong phần hỏi đáp giữa bác sĩ Phúc và BTV Khánh Lành, việc dùng đạm để nuôi não còn được liên hệ với mất cơ, trước khi phần trao đổi chuyển sang DHA là phần chính được trông chờ.
- **A/o04:** should be revised to the sentence above. The old draft repeats albumin coverage but still does not supply B3’s missing muscle-loss explanation. Joint dialogue attribution avoids assigning the short response to a speaker the caption does not name.
- **Quotes → resolved:** 'albumin thì lại nó thực hiện nhiều chức năng quá dẫn tới là nó rất ít được dành cho não.' → 01:30:33–01:30:38; 'Thế còn đạm mà chúng ta cũng lại dùng thì đạm nó cũng quý quá nó tiêu mất gì?' → 01:30:44–01:30:46; 'Mất cơ đi.' → 01:30:49; 'Phần chính là DHA.' → 01:30:53 (all PASS).
- **Status:** pending-human-approval.

### om05 — Practical high/low Omega-6 oil list
- **Source timestamps:** 01:56:53–01:57:13. **Current claim IDs:** c087.
- **Classification:** covered. Substantive oil choices are already present. Identity of the ambiguous oil is deliberately separated into om06.
- **Importance:** high — concrete shopping guidance is already represented; another list adds no coverage.
- **Proposed insertion:** none. **A/o05 substantive draft:** no longer needed; its conservative list adds nothing to c087.
- **Quote → resolved:** 'Dầu đậu nành, dầu hướng dương, ngô được biết là chứa hàm lượng lớn omega6.' → 01:57:00–01:57:06 (PASS).
- **Status:** pending-human-approval.

### om06 — Ambiguous oil identity
- **Source timestamps:** 01:57:06–01:57:13. **Current claim IDs:** c087.
- **Classification:** fidelity-question-not-omission. Substantive advice is represented in om05; the caption does not establish that its unclear name means olive oil. c087’s parenthetical records the uncertainty but does not resolve it.
- **Importance:** low — resolve a name separately rather than add duplicate diet advice.
- **Proposed insertion:** none. **A/o05 name interpretation:** do not add or silently normalize it; the old draft’s omission of the unclear name does not settle identity.
- **Quote → resolved:** 'dầu ôu' → 01:57:06–01:57:09 (PASS; identity unresolved).
- **Status:** pending-human-approval.

### om07 — Lean meat, butter and grass-fed animals
- **Source timestamps:** 01:57:13–01:58:18. **Current claim IDs:** c088–c090.
- **Classification:** covered. Lean cuts, butter comparison, grain-feed rationale, if-possible grass-fed preference, and moderate chicken/pork with lean alternative are present.
- **Importance:** high — practical diet details, already covered with conditions.
- **Proposed insertion:** none. **A/o06:** no longer needed.
- **Quote → resolved:** 'Do đó, nếu có thể thì việc sử dụng các loại thịt từ động vật được nuôi bằng cỏ là tối ưu nhất.' → 01:57:49–01:57:58 (PASS).
- **Status:** pending-human-approval.

### om08 — Beneficial roles of Omega-6
- **Source timestamps:** 01:54:57–01:55:10. **Current claim IDs:** c075.
- **Classification:** covered. Brain, reproduction, hair, skin and bone roles are attributed to the article.
- **Importance:** medium — balances the reported harms; already present.
- **Proposed insertion:** none. **A/o07:** no longer needed.
- **Quote → resolved:** 'chức năng não, sức khỏe sinh sản, giúp tóc, da và xương khỏe mạnh.' → 01:55:05–01:55:10 (PASS).
- **Status:** pending-human-approval.

### om09 — Fatty-acid profiles, substantive coverage
- **Source timestamps:** 02:10:35–02:11:12; 02:14:01–02:14:18. **Current claim IDs:** c100, c106–c109.
- **Classification:** covered. The summary already represents GLA anti-inflammatory, CLA anti-inflammatory/anticancer and EPA/DHA anti-inflammatory effects, with LA/AA inflammation elsewhere. This is a coverage finding, not confirmation that the caption abbreviations identify those molecules.
- **Importance:** low — another effects paragraph duplicates current claims.
- **Proposed insertion:** none. **A/o08 substantive draft:** no longer needed. Its GL/CL-to-GLA/CLA interpretation must not be newly approved through an omission insertion; see om10.
- **Quote → resolved:** 'GL ở đây thì có tác dụng là cái này chống viêm.' → 02:10:35–02:10:39 (PASS; identity not established by matching).
- **Status:** pending-human-approval.

### om10 — GL/CL/Alla identity and ALA statement
- **Source timestamps:** 02:10:08–02:11:12; 02:14:01–02:14:18. **Current claim IDs:** c091–c094, c100, c106–c109.
- **Classification:** fidelity-question-not-omission. B7’s individual ALA anti-inflammatory sentence is not explicit in the summary, but the captions use AL/Alla and later assign the same apparent name the opposite effect. A confident new ALA sentence cannot be grounded by treating this as an ordinary missing fact. CL identification is also not established by its occurrence. Do not convert either uncertainty into an approved molecule identity.
- **Importance:** low — identity must be resolved before any extra biochemical detail is useful.
- **Proposed insertion:** none. **A/o08 identity wording:** not safe to reuse as a new insertion; no additional sentence is warranted while this remains a fidelity question.
- **Quotes → resolved:** 'CL thì có tác dụng vừa chống viêm vừa chống ung thư.' → 02:10:43–02:10:47; 'la viêm còn Alla là chống viêm.' → 02:10:31; 'Còn cái Alla này thì nó lại gây viêm.' → 02:10:50–02:10:53 (all PASS; identities/conflict unresolved).
- **Status:** pending-human-approval.

### om11 — Do not eliminate Omega-6
- **Source timestamps:** 02:19:53–02:20:07. **Current claim IDs:** c109.
- **Classification:** covered. Importance, excess-only inflammation, moderate-intake qualification and no complete elimination all appear.
- **Importance:** high — guards against interpreting reduction as elimination; already present.
- **Proposed insertion:** none. **A/o09:** no longer needed. Separate cooking-oil statement is om12, not a reason to repeat c109.
- **Quote → resolved:** 'Nó chỉ gây ra viêm khi nào? Khi mà nó quá nhiều.' → 02:19:57–02:19:59 (PASS).
- **Status:** pending-human-approval.

### om12 — Separate warning against eliminating cooking oil
- **Source timestamps:** 02:30:47–02:30:57. **Current claim IDs:** c109 and c117–c121 are related; no equivalent cooking-oil warning.
- **Classification:** omitted. A ceiling and an Omega-6 qualification do not state the separate claim that no cooking oil deprives cells of components.
- **Importance:** high — preserves the speaker’s limit on his reduction advice instead of inviting an elimination reading.
- **Proposed insertion, after c119:** Bác sĩ Phúc nói chỉ giảm bớt chứ không bỏ dầu ăn hoàn toàn, vì theo ông, không ăn dầu ăn khiến tế bào thiếu những thành phần đang được bàn tới và rất nguy hiểm.
- **Quote → resolved:** 'Nếu chúng ta không ăn dầu ăn thì các tế bào của chúng ta sẽ không có những thành phần này rất nguy hiểm.' → 02:30:47–02:30:53 (PASS).
- **Status:** pending-human-approval.

### om13 — Alcohol moderation analogy
- **Source timestamps:** 02:20:08–02:20:30. **Current claim IDs:** none; nearest c109.
- **Classification:** omitted. It is an explicit health aside in B8, albeit peripheral, not automatically out of scope.
- **Importance:** low — illustrative digression rather than a supplement-selection rule; adding it can distract from the core topic.
- **Proposed insertion, after c109, only if approved:** Để minh họa chuyện quá mức, bác sĩ Phúc cho rằng uống một chút rượu kích thích tiêu hóa, tinh thần và khí huyết lưu thông, nhưng uống quá nhiều thì ảnh hưởng sức khỏe.
- **Quotes → resolved:** 'Chúng ta uống một chút rượu thôi thì nó sẽ kích thích hệ tiêu hóa, kích thích tinh thần, kích thích nhiều cái khí huyết lưu thông sẽ rất là tốt.' → 02:20:12–02:20:20; 'Nhưng mà chúng ta uống rượu quá nhiều thì nó sẽ hỏng.' → 02:20:20–02:20:22 (both PASS).
- **Status:** pending-human-approval. Recommendation: do not add this peripheral aside; its documented omission is not an endorsement of drinking.

### om14 — Cooking-oil sellers, expiry and opened shelf life
- **Source timestamps:** 02:32:58–02:33:22. **Current claim IDs:** c120–c122.
- **Classification:** covered. Reputable sellers, expiry, instructed opened usage period, avoiding prolonged storage and restaurant-size cans are present.
- **Importance:** medium — actionable handling context, already available.
- **Proposed insertion:** none. **A/o10:** no longer needed.
- **Quote → resolved:** 'Mua dầu ăn phải mua ở những cái siêu thị cửa hàng uy tín, mua đúng hạn sử dụng.' → 02:33:03–02:33:08 (PASS).
- **Status:** pending-human-approval.

### om15 — Extra-ingredient advertising
- **Source timestamps:** 02:33:52–02:34:24; 03:20:10–03:20:19. **Current claim IDs:** c116, c123.
- **Classification:** partially covered. Not seeking extra Omega-6/9, dietary sufficiency and EPA/DHA focus are covered; missing is the explicit connection to manufacturers advertising extra components in Omega-3 products.
- **Importance:** medium — helps viewers recognize the marketing situation to which the existing advice applies.
- **Proposed insertion, after c123:** Bác sĩ Phúc nói lời khuyên này cũng áp dụng khi nhà sản xuất quảng cáo sản phẩm Omega-3 có thêm nhiều thành phần: theo ông, những thành phần ấy không cần thiết vì thực phẩm và dầu ăn đã có.
- **A/o11:** should be revised to the sentence above; its existing dietary/EPA/DHA content would otherwise be duplicated.
- **Quote → resolved:** 'Và rất nhiều những các cái nhà sản xuất người ta quảng cáo trong Omegan 3 có nhiều những cái sản phẩm này, sản phẩm kia thì chúng ta thấy rằng thực ra không cần thiết vì trong thực phẩm nó đã có, trong dầu ăn đã có rồi.' → 02:34:04–02:34:18 (PASS).
- **Status:** pending-human-approval.

### om16 — Surplus DHA/EPA for other organs (A only)
- **Source timestamps:** 02:25:15–02:25:30. **Current claim IDs:** c072, c113, c173.
- **Classification:** covered. c113 supplies the conditional surplus-organ list; c072/c173 supply brain/eye/heart priorities and EPA’s additional brain role.
- **Importance:** low — supporting explanation already present across claims.
- **Proposed insertion:** none. **A/o12:** no longer needed; conditional wording is already represented.
- **Quote → resolved:** 'DHA và EPA có nếu thừa ra thì sẽ dành cho các tạng địa phương gan mật tụy lách thận được' → 02:25:15–02:25:21 (PASS).
- **Status:** pending-human-approval.

### om17 — Natural-oil 0.06 example
- **Source timestamps:** 02:51:17–02:51:39; 02:53:39–02:53:44. **Current claim IDs:** c145–c149.
- **Classification:** covered. Natural-oil context, ≤0.3 limit, the doctor’s 0.06 calculation and a separately qualified low-value reaction are present. No speaker identity is inferred for that reaction.
- **Importance:** medium — relevant label example already covered.
- **Proposed insertion:** none. **A/o13:** no longer needed. The distinct price/advertising detail is om18.
- **Quote → resolved:** 'có sản phẩm đã xuống đến 0,06.' → 02:51:17–02:51:19 (PASS).
- **Status:** pending-human-approval.

### om18 — Expensive advertised gift oils
- **Source timestamps:** 02:51:02–02:51:32; 02:53:39–02:53:44. **Current claim IDs:** c148–c149.
- **Classification:** partially covered. The numbers are present; the specific warning about heavily advertised, very expensive gift products is absent. c154’s different absorption-advertising discussion does not cover this example.
- **Importance:** medium — explains why the speaker tells viewers to calculate rather than rely on prestige or price.
- **Proposed insertion, after c149:** Trong phần dầu cá tự nhiên, bác sĩ Phúc nói ngay cả sản phẩm được quảng cáo nhiều, rất đắt tiền và đem tặng nhau mà ông đề cập cũng cho tỷ lệ không quá 0,3 khi tính theo cách này.
- **Quote → resolved:** 'Kể cả những các cái sản phẩm mà được quảng cáo rất nhiều quý giá đủ thứ quý giá mà đem tặng nhau vô cùng đắt tiền. Chúng ta chia đi cũng đều là con số nhỏ hơn hoặc bằng 0,3 hết.' → 02:51:02–02:51:12 (PASS).
- **Status:** pending-human-approval.

### om19 — Optional form labels and reading the leaflet
- **Source timestamps:** 02:39:45–02:39:56; 03:06:02–03:06:09. **Current claim IDs:** c133, c144–c157; c171 is a different-purpose instruction.
- **Classification:** partially covered. Optional form labeling and TG advertising are covered; missing is reading the leaflet specifically to identify the oil type, not storage instructions or the concentration denominator.
- **Importance:** medium — small, practical identification step in the selection process.
- **Proposed insertion, after c157:** Bác sĩ Phúc còn dặn đọc kỹ tờ hướng dẫn sử dụng để biết sản phẩm là loại dầu cá gì.
- **Quote → resolved:** 'Thì khi quý vị mua phải đọc kỹ hướng dẫn sử dụng, đọc kỹ cái tờ hướng dẫn ấy để xem loại dầu cá gì.' → 03:06:02–03:06:07 (PASS).
- **Status:** pending-human-approval.

### om20 — Krill safety qualification
- **Source timestamps:** 02:54:41–02:56:03. **Current claim IDs:** c150.
- **Classification:** covered. Advertising rationale and the doctor’s explicit further-research caveat are distinguished.
- **Importance:** medium — important hedge already present.
- **Proposed insertion:** none.
- **Quote → resolved:** 'Thế còn an toàn hay không thì cũng phải chờ những các cái nghiên cứu nữa.' → 02:55:37–02:55:38 (PASS).
- **Status:** pending-human-approval.

### om21 — Skepticism about rTG absorption figures
- **Source timestamps:** 03:00:24–03:00:54. **Current claim IDs:** c154.
- **Classification:** covered. Competing figures, excess/exaggeration concern and tentative preference for 125% are all represented.
- **Importance:** medium — avoids strengthening an advertising claim; existing text already does so.
- **Proposed insertion:** none.
- **Quote → resolved:** 'Tôi nghĩ rằng là đến 125% thì có lẽ là hợp lý hơn chứ còn đôi khi người ta quảng cáo nó hơi nhiều.' → 03:00:47–03:00:53 (PASS).
- **Status:** pending-human-approval.

### om22 — Doubling 0.35 versus refined 0.7
- **Source timestamps:** 03:03:41–03:04:29. **Current claim IDs:** c165–c166; related c118.
- **Classification:** covered. Question, refinement response and added fat/oil analogy are present without needing a stronger categorical equivalence claim.
- **Importance:** high — directly addresses a purchase/dose substitution question, already covered.
- **Proposed insertion:** none. **A/o14:** no longer needed.
- **Quote → resolved:** '0,35 xong uống gấp đôi lên được hay không?' → 03:03:51–03:03:53 (PASS).
- **Status:** pending-human-approval.

### om23 — <0.3 monitoring qualification
- **Source timestamps:** 03:01:21–03:01:58; 03:08:33–03:08:42. **Current claim IDs:** c158–c159.
- **Classification:** covered. Trying and monitoring, variability between users and possible lipid/fatty-liver increases after a period of use are represented.
- **Importance:** high — preserves a stated adverse-effect/monitoring qualification, already present.
- **Proposed insertion:** none. **A/o15:** no longer needed.
- **Quote → resolved:** 'có những người uống xong một thời gian chúng ta có thể bị tăng cái mỡ máu hay gan nh mỡ hay gì gì đấy lên thì chúng ta phải kiểm tra theo dõi.' → 03:01:50–03:01:57 (PASS).
- **Status:** pending-human-approval.

### om24 — Vitamins D/A/E also need storage care
- **Source timestamps:** 03:10:49–03:11:19. **Current claim IDs:** c169–c171.
- **Classification:** covered. Vitamin list, degradation, even authentic reputable products being ineffective if poorly stored, and reading storage instructions are present.
- **Importance:** medium — meaningful handling warning already covered.
- **Proposed insertion:** none. **A/o16:** no longer needed.
- **Quote → resolved:** 'vitamin D này, vitamin A này, vitamin E này' → 03:10:52–03:10:57 (PASS).
- **Status:** pending-human-approval.

### om25 — Concentration by illness and avoiding imbalance
- **Source timestamps:** 03:18:04–03:18:45. **Current claim IDs:** c178, c180–c181.
- **Classification:** covered. Illness 0.6–0.7, preference ≥0.7, healthy 0.5–0.6, slightly increased DHA and no extreme imbalance in either direction are present. Concentration is not confused with EPA:DHA balance.
- **Importance:** high — core selection rule as reported, already covered.
- **Proposed insertion:** none. **A/o17:** no longer needed.
- **Quote → resolved:** 'nếu như mọi người bị bệnh tật thì bắt đầu chúng ta sẽ nên mua từ cái cỡ độ 0,6 0,7' → 03:18:07–03:18:12 (PASS).
- **Status:** pending-human-approval.

### om26 — Children: sleep, games, short videos
- **Source timestamps:** 03:16:36–03:17:56. **Current claim IDs:** c176–c177.
- **Classification:** covered. Sleep/stop-games/stop-short-videos advice, deeper study, emotional stimulation and stated autonomic/arrhythmia/emotional consequences are present.
- **Importance:** medium — lifestyle advice and the speaker’s explanation are already available.
- **Proposed insertion:** none.
- **Quote → resolved:** 'nên ngủ sớm, nên bỏ game online' → 03:17:10–03:17:12 (PASS).
- **Status:** pending-human-approval.

### om27 — Pre-supplement testing/check-up attribution, excluded
- **Source timestamps:** 03:23:38–03:24:32 (candidate locator only). **Current claim IDs:** c192.
- **Classification:** out of scope. B20’s concern includes speaker attribution at 03:24:15; the user expressly reserves c192 as a fidelity item. Neither the doctor’s endorsement nor the combined attribution is adjudicated here.
- **Importance:** high — consequential testing/attribution question for its separate human review.
- **Proposed insertion:** none. Not a request to add a second testing paragraph.
- **Quotes with resolved timestamps:** none reproduced; see related, not analysed.
- **Status:** pending-human-approval.

### om28 — RBC test availability in Vietnam
- **Source timestamps:** 03:24:36–03:26:08. **Current claim IDs:** c190.
- **Classification:** covered. Developed-country testing, the speaker’s current-knowledge qualification, Vietnam non-availability and demand explanation are present. This is not a checked statement about present-day service availability.
- **Importance:** medium — locally relevant qualification already present.
- **Proposed insertion:** none. Dose variability is separately retained in om29.
- **Quote → resolved:** 'hiện tại theo tôi được biết thì ở Việt Nam chưa làm bởi vì chúng ta chưa có nhu cầu.' → 03:24:50–03:24:55 (PASS).
- **Status:** pending-human-approval.

### om29 — Variable daily EPA/DHA doses and test basis
- **Source timestamps:** 03:25:05–03:25:38; broader B21 context 03:24:36–03:26:08. **Current claim IDs:** c190; c048’s single study dose is not this comparison.
- **Classification:** partially covered. RBC testing as a basis for amount is present; the 400/500/600/1000/2000 mg comparison and the skeptical framing of the largest amount are missing.
- **Importance:** medium — explains the stated need for a dosing basis rather than leaving readers with one uniform number.
- **Proposed insertion, after c190:** Bác sĩ Phúc nêu các khuyến cáo khác nhau, từ 400, 500, 600 mg đến 1000 mg mỗi ngày như nghiên cứu Khánh Lành dẫn; ông nói thậm chí có người hăng hái nêu 2000 mg, rồi đặt câu hỏi về cơ sở và chỉ vào xét nghiệm trong hồng cầu.
- This records a comparison, not a prescribed range or a recommendation to take 2000 mg. It does not modify c192 or assert local test availability.
- **Quotes → resolved:** 'Bởi vì có những khuyến cáo thì bổ sung 400 mg trong tổng số này. Có khuyến cáo thì 500, có khuyến cáo 600' → 03:25:21–03:25:26; 'Là 1000 và thậm chí có những người còn hăng hái nói bổ sung đến 2000. Vậy nó phải có cơ sở nào?' → 03:25:30–03:25:35; 'Cơ sở đó chính là xét nghiệm ở trong hồng cầu.' → 03:25:37–03:25:38 (all PASS).
- **Status:** pending-human-approval.

### om30 — Channel disclosures and no purchase links
- **Source timestamps:** 00:42:01–00:42:17; 01:53:28–01:53:53. **Current claim IDs:** none equivalent; c127 begins the article/selection material.
- **Classification:** omitted. Selection advice alone does not convey these declarations.
- **Importance:** medium — contextualizes commercial independence claimed by the programme, without verifying it.
- **Proposed insertion, after c074 and before the [01:53:28] section’s existing content:** Bác sĩ Phúc tuyên bố kênh không bán thuốc, không quảng cáo, không nhận sản phẩm; BTV Khánh Lành cũng nói chương trình không đưa link mua ngay mà hướng dẫn cách lựa chọn và sử dụng Omega-3.
- The placement is a separate paragraph at the boundary, not an edit to c074. The claim is about what the speakers declare, not independently established channel practices or a permanent promise about all links.
- **Quotes → resolved:** 'kênh chúng tôi không hề bán thuốc kênh chúng tôi không hề quảng cáo, kênh chúng tôi không hề nhận sản phẩm gì' → 00:42:07–00:42:13; 'Nhưng không thưa quý vị, chúng tôi sẽ hướng dẫn quý vị làm thế nào để có thể lựa chọn omega 3 cách thông minh và sử dụng một cách hiệu quả.' → 01:53:45–01:53:53 (both PASS; preceding 01:53:28–01:53:45 supplies the purchase-link question).
- **Status:** pending-human-approval.

### om31 — Additional diseases explicitly linked to 20:1 (C1)
- **Source timestamps:** 02:29:17–02:30:25. **Current claim IDs:** c100–c105, c112; c163 names diseases in a different, improvement context.
- **Classification:** partially covered. Imbalance, dilution and many inflammatory diseases are represented; the specific 20:1 passage additionally names vascular atherosclerosis and two caption-transcribed disease names, together with autoimmune diseases. c163 is not coverage of this claimed causal link and must remain unchanged.
- **Importance:** low — expands an already long disease list; less valuable than the remaining purchasing/qualification gaps.
- **Proposed insertion, after c112, only if approved:** Khi nói về tỷ lệ 20:1, bác sĩ Phúc còn nêu 'sơ vữa mạch máu', 'Anzimer', 'bakis' và các bệnh tự miễn như những hệ quả mà ông quy cho chế độ ăn mất cân bằng.
- The two disease strings are retained verbatim rather than silently equated to Alzheimer/Parkinson from the reviewer’s topic label. The missing list/link can be represented without deciding their word identities. This is not endorsement of causation; existing article caveats c084–c086 are not altered.
- **Quotes → resolved:** 'sơ vữa mạch máu' → 02:29:52; 'Anzimer' → 02:29:55; 'bakis' → 02:29:55; 'bệnh tự miễn' → 02:30:00 (all PASS; repeated proposal fragments use these same resolutions).
- **Status:** pending-human-approval. Recommendation: do not add this low-value list expansion unless the human specifically wants it.

### om32 — Functioning non-nucleated RBC argument (C3)
- **Source timestamps:** 03:26:34–03:27:38. **Current claim IDs:** c067–c068, c190–c191.
- **Classification:** partially covered. Membrane-as-brain/nucleus-as-reproduction account and RBC tests are present; the distinct inference from functioning non-nucleated human RBCs is absent.
- **Importance:** low — illustrates an existing explanation rather than adding a selection criterion.
- **Proposed insertion, after c191:** Bác sĩ Phúc nêu rằng hồng cầu người nhìn chung không có nhân mà vẫn hoạt động bình thường, lấy đó làm luận cứ cho quan điểm màng tế bào là bộ não của tế bào.
- The qualifier nhìn chung avoids turning his later small-exception wording about young cells into an all-cells statement. This reports his argument without endorsing it, importing a biological correction, or editing approved c068.
- **Quotes → resolved:** 'Không có nhân.' → 03:26:53; 'Còn lại toàn bộ là tế bào hồng cầu không nhân mà nó vẫn hoạt động chức năng được bình thường.' → 03:27:29–03:27:36; 'Vậy thì màng tế bào hồng cầu nó mới là bộ não của tế bào.' → 03:27:17–03:27:20 (all PASS).
- **Status:** pending-human-approval. Recommendation: do not add unless fuller coverage of this analogy is specifically desired.

### om33 — Article evidence caveat and type of fat
- **Source timestamps:** 01:58:18–01:59:06. **Current claim IDs:** c084–c086.
- **Classification:** covered. Insufficient-quality/scale evidence, no asserted chronic-disease causation, excess of either fat, industrial-food condition and greater importance of fat type are present.
- **Importance:** high — key limitation on the article’s claims, already preserved.
- **Proposed insertion:** none.
- **Quote → resolved:** 'Có thể nói đến nay vẫn chưa có nghiên cứu nào với chất lượng và quy mô thật sự để khẳng định Omega6 là nguyên nhân gây nên bệnh tim mạch hoặc làm gia tăng các dấu hiệu gây viêm.' → 01:58:15–01:58:30 (PASS). The computed start precedes the topic timestamp because the caption at 01:58:15 also begins this sentence.
- **Status:** pending-human-approval.

## Disposition of all original A drafts

No original A insertion should be applied verbatim to the current summary merely because its evidence matches. Matching speech is not evidence of continued omission.

| A draft | Current disposition |
| --- | --- |
| o01 | No longer needed — om01/c053. |
| o02 | No longer needed — om02/c054. |
| o03 | No longer needed as an omission insertion — om03/c055; fidelity excluded. |
| o04 | Revise — use only om04’s muscle-loss bridge, not the already-covered albumin paragraph. |
| o05 | No longer needed — om05/c087; identity separated as om06, not silently fixed. |
| o06 | No longer needed — om07/c088–c090. |
| o07 | No longer needed — om08/c075. |
| o08 | No longer needed as an omission insertion — om09/c106–c108; its inferred identities remain om10, not approved. |
| o09 | No longer needed — om11/c109; B6’s separate cooking-oil gap is om12. |
| o10 | No longer needed — om14/c122. |
| o11 | Revise — om15 supplies only the marketing connection missing from c123. |
| o12 | No longer needed — om16/c113, c072, c173. |
| o13 | No longer needed — om17/c148–c149; B12’s distinct marketing example is om18. |
| o14 | No longer needed — om22/c165–c166. |
| o15 | No longer needed — om23/c158–c159. |
| o16 | No longer needed — om24/c171. |
| o17 | No longer needed — om25/c178, c180–c181. |

## Quote verification of supplied historical evidence

In addition to all displayed evidence and the three quoted insertion fragments in om31, the supplied source anchors were re-run read-only. No quote-resolution failure was found. This does not validate any inferred name, attribution or medical claim.

### A: all 21 expanded evidence blocks

Each block is identified by its original A item and source range; the full text stays in the unchanged A file. Results from `resolve_quote`:

| A evidence | Resolved caption range | Result |
| --- | --- | --- |
| o01, 01:21:24–01:21:38 | 01:21:24–01:21:38 | PASS |
| o02, 01:21:54–01:22:05 | 01:21:54–01:22:05 | PASS |
| o03, 01:27:10–01:27:20 | 01:27:10–01:27:20 | PASS; text check only, c055 not analysed |
| o04, 01:30:16–01:30:17 | 01:30:16 | PASS |
| o04, 01:30:30–01:30:38 | 01:30:30–01:30:38 | PASS |
| o04, 01:30:49–01:30:53 | 01:30:49–01:30:53 | PASS |
| o05, 01:57:00–01:57:13 | 01:57:00–01:57:13 | PASS |
| o06, 01:57:13–01:57:29 | 01:57:13–01:57:29 | PASS |
| o06, 01:57:33–01:58:07 | 01:57:33–01:58:07 | PASS |
| o07, 01:54:57–01:55:10 | 01:54:57–01:55:10 | PASS |
| o08, 02:10:35–02:10:47 | 02:10:35–02:10:47 | PASS |
| o09, 02:19:53–02:20:07 | 02:19:53–02:20:07 | PASS |
| o10, 02:33:03–02:33:16 | 02:33:03–02:33:16 | PASS |
| o11, 02:33:55–02:34:23 | 02:33:55–02:34:23 | PASS |
| o12, 02:25:15–02:25:30 | 02:25:15–02:25:30 | PASS |
| o13, 02:51:17–02:51:25 | 02:51:17–02:51:25 | PASS |
| o13, 02:51:32–02:51:39 | 02:51:32–02:51:39 | PASS |
| o14, 03:03:43–03:04:00 | 03:03:43–03:04:00 | PASS |
| o15, 03:01:46–03:01:57 | 03:01:46–03:01:57 | PASS |
| o16, 03:10:49–03:11:19 | 03:10:49–03:11:19 | PASS |
| o17, 03:18:07–03:18:22 | 03:18:07–03:18:22 | PASS |

### B: all 24 original Anchor/Second anchor blocks

Text remains in the unchanged `omissions.md`; these are lexical checks only, including excluded-topic anchors, not fidelity adjudications.

| B evidence | Resolved caption range | Result |
| --- | --- | --- |
| B1 Anchor | 01:21:54–01:22:05 | PASS |
| B2 Anchor | 01:27:10–01:27:20 | PASS; c055 not analysed |
| B3 Anchor | 01:30:33–01:30:38 | PASS |
| B4 Anchor | 01:57:00–01:57:13 | PASS |
| B5 Anchor | 01:58:18–01:58:27 | PASS |
| B6 Anchor | 02:19:53–02:19:59 | PASS |
| B6 Second anchor | 02:30:47–02:30:53 | PASS |
| B7 Anchor | 02:10:43–02:10:47 | PASS |
| B8 Anchor | 02:20:12–02:20:17 | PASS |
| B9 Anchor | 02:33:03–02:33:08 | PASS |
| B10 Anchor | 02:34:04–02:34:13 | PASS |
| B11 Anchor | 02:39:45–02:39:47 | PASS |
| B12 Anchor | 02:51:02–02:51:07 | PASS |
| B13 Anchor | 02:55:37–02:55:38 | PASS |
| B14 Anchor | 03:00:47–03:00:53 | PASS |
| B15 Anchor | 03:01:50–03:01:57 | PASS |
| B16 Anchor | 03:03:47–03:03:55 | PASS |
| B17 Anchor | 03:10:49–03:10:59 | PASS |
| B18 Anchor | 03:18:07–03:18:16 | PASS |
| B18 Second anchor | 03:18:30–03:18:38 | PASS |
| B19 Anchor | 03:17:10–03:17:18 | PASS |
| B20 Anchor | 03:23:54–03:24:04 | PASS; c192 not analysed |
| B21 Anchor | 03:24:48–03:24:55 | PASS |
| B22 Anchor | 00:42:07–00:42:13 | PASS |

### C: original short review quotes

| C evidence | Resolved caption range | Result |
| --- | --- | --- |
| C1 | 02:29:52 | PASS |
| C2 | 03:25:23 | PASS |
| C3 | 03:26:51 | PASS |

The expanded evidence above, rather than those short snippets alone, grounds the new drafts. All **48 displayed single-quoted occurrences** also pass both the shared matcher and a case-/punctuation-preserving substring check after caption-prefix removal and whitespace joining. The protected 59-file manifest was rechecked after report creation and is identical to the pre-output manifest; the only new file is this report.

## Recommend NOT adding

- **om13:** peripheral alcohol analogy; document its omission without amplifying it as a health recommendation.
- **om31:** low-value expansion of an already extensive disease list, with unclear caption-transcribed names; causal linkage remains only the speaker’s claim.
- **om32:** explanatory RBC analogy rather than actionable supplement guidance; existing membrane discussion is already substantial.
- **om06/om10:** identity/conflicting-caption questions, not missing substantive advice. Resolve separately; do not add guesses.
- **All covered items:** duplicates, especially old A drafts now represented in the current summary. om03/om27 are excluded fidelity matters, not insertions to approve here.

These are recommendations only; none is a human rejection. The higher-priority remaining addition is om12; om15/om18/om19/om29 provide practical clarification, om30 supplies declared commercial context, and om04 is optional explanatory completeness.

## Related, not analysed

- **c019:** fidelity tracking only; no formula assessment here.
- **c055:** fidelity tracking only; A/o03 and B2 retained as om03, with no new fidelity verdict.
- **c192:** fidelity tracking only; B20 retained as om27. The speaker of the testing/check-up expansion is not established here.
- **c012/c124 review fails:** not analysed, corrected, endorsed or incorporated into omission drafts. In particular, no addition here authorizes stopping medication or treats clinical anecdotes as medical proof.
- **c068/c163:** approved/applied correction text is protected and unchanged. Nearby proposed insertions are independent paragraphs, not revisions of those claims.

## Closing tally and human checkpoint

**33 atomic topics:** 19 covered; 7 partially covered (om04, om15, om18, om19, om29, om31, om32); 3 omitted (om12, om13, om30); 2 fidelity-question-not-omission (om06, om10); 2 out of scope (om03, om27). **10 minimal insertion drafts**, none applied. Still-missing importance: 1 high, 5 medium, 4 low. All 17 A, all 22 B and all 3 C entries are mapped, including compound scopes and single-source topics.

**A draft disposition:** 15 no longer needed as omission insertions (including identity/exclusion qualifications), 2 should be revised (o04/o11), 0 old drafts recommended for verbatim application. **0 quote failures.** No endorsement follows from recording any item.

**33/33 statuses: pending-human-approval; 0 human approvals or rejections inferred.** Human decisions remain item-by-item, for example: `approve om12, om15; reject om13`. Approval of a topic must refer to its displayed draft; identity/fidelity questions and excluded claims require their separate process. Neither approval of this analysis nor an omission flag changes queue_state or publishable.
