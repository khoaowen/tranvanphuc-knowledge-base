# PR #9 decision pack: V-Qfwjo28Zg audit

Video: **V-Qfwjo28Zg**, "Số 135: GLUTATHIONE…", 5:23:35 long, https://www.youtube.com/watch?v=V-Qfwjo28Zg

**How to use this pack**
- Every ▶ link opens YouTube 5 s before the cited moment, so you hear the lead-in.
- Transcript excerpts show 15 s before to 25 s after each cited quote. Lines marked `▶` are the exact quoted caption lines.
- The captions are auto-generated and unpunctuated. Where the audit says "bản ghi âm ghi như vậy", trust your ears over the caption.
- **BEFORE** is the claim as it stood in the summary bound by the audit: `git show 4e31e57^:videos/2026-10-10-so-135-glutathione-can-bang-oxy-hoa-khu-phuc-hoi-ty-the-va-bao-ve-te-bao-tu-cap-do-phan-tu/summary.md`, SHA-256 `fbae11bf…a98203c`. That file has since been deleted from `videos/`. **AFTER** is the audit's proposed text, status `pending-human-approval`.
- Generated read-only from PR #9 head `3834732`; nothing in the repo was changed.

## Part 1. The 13 decisions

### D1. Which summary do the corrections target?
**Context.** All 63 corrections are written against the summary with SHA `fbae11bf…`. Commit `4e31e57` ("re-queue summaries failing the tag vocabulary", 2026-10-29) deleted that `summary.md` and `review.md`. At HEAD the video has only `transcript.md` and `metadata.json`. The pipeline will regenerate the summary, and a new summary gets new claim ids (`audit-summary.md`: "any regenerated summary invalidates these claim ids").
**Before:** there is no summary at HEAD; the corrections point at a deleted file.
**Options:**
- (a) Restore the `fbae11bf` summary and apply the approved corrections to it.
- (b) Let it regenerate, and use the 63 items only as a checklist of known failure modes for auditing the new summary.
- (c) Both: regenerate, then reuse the corrections wherever the same claim reappears.
**Nothing to watch.** This is a process choice.

### D2. Accept that 461 supported claims were checked by one pass only?
**Context.** Pass 1 read all 554 claims. The blind pass 2 re-checked 93: all 63 non-supported plus 30 supported. Among those 30 supported claims, pass 2 disagreed once (c282: pass 2 found an added hedge "có thể"; see [c282](#c282)). My own spot check of 25 random pass-1-only supported claims found 0 errors. Together that is 1 error in 55, which statistically leaves up to about 10% (about 44 claims) possibly wrong. The q7uDJG8YQ5c audit used the same sampling design, plus a third read for disagreements.
**Options:** accept as is · run a second pass on a wider sample (for example 100 supported claims) · run a full second pass on all 461.
**To judge it yourself,** here are the 25 claims I spot-checked:

- c020 [▶ 00:09:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=568s): Ti thể được mô tả là "nhà máy điện" và "lò phản ứng" của tế bào, nơi diễn ra chu trình trao đổi chất (chu trình Krebs) để tạo ATP, đồng tiền năng lượng của tế bào.  
  quote: "Và đây chính là cái lò phản ứng hạt nhân và đây cũng chính là cái nhà máy điện."
- c024 [▶ 00:11:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=658s): Lý do là các cơ chất để tạo ATP gồm đường, mỡ và đạm; khi đốt cháy với oxy thì ngoài năng lượng còn sinh ra nhiều thành phần khác, trong đó có gốc tự do.  
  quote: "Vì tất cả những cái cơ chất để mà tạo ra ATP thì chúng ta bao gồm có gì ạ? Đường"
- c043 [▶ 00:34:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2050s): Có, H₂O₂ được nêu là một gốc tự do nguy hiểm.  
  quote: "Thì đây cũng là một cái gốc tự do rất nguy hiểm."
- c047 [▶ 00:40:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2450s): Nó hình thành khi H₂O₂ bị phá vỡ bởi sắt (Fe²⁺) hoặc đồng (Cu²⁺), tách thành hai nhóm OH, mỗi nhóm mang một electron lạc.  
  quote: "là có cái thanh kiếm kim loại là sắt hai cộng. Hai là cái thanh kiếm kim loại khác nữa đó là cồng đồng hai cộng."
- c064 [▶ 00:52:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3170s): Một gốc tự do làm hỏng viên gạch đầu tiên, viên gạch đó lại đi cướp ở bên cạnh, nên tường thành dần sụp đổ và tế bào hoại tử.  
  quote: "viên gạch đầu tiên. Viên gạch đó ngay lập tức lại đi cướp ở bên cạnh."
- c097 [▶ 01:04:51](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3886s): Vitamin C vừa là cảm tử, vừa tham gia trực tiếp, và còn nhường electron cho vitamin E.  
  quote: "Ngoài ra nó vừa là cảm tử, vừa tham gia"
- c131 [▶ 01:25:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5121s): Họ ngủ ngon, ít tiểu đêm, và tập thở 4-7-8 trước khi ngủ hiệu quả rõ.  
  quote: "Em ngủ ngon, thẳng giấc, ít hẳn tiểu đêm. Đặc biệt hiệu quả rõ rệt vào những hôm tập thở 4 78 trước khi đi ngủ."
- c139 [▶ 01:26:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5213s): Đây là kết quả người xem tự kể.  
  quote: "Kính chào bác sĩ Trần Văn Phúc, vị bác"
- c145 [▶ 02:24:46](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8681s): Bài hôm nay không đủ thời gian để giải thích sâu, nhưng cơ chế cơ bản theo bác sĩ là: thức đi kèm với hoạt động, ngủ đi kèm với ngừng hoạt động.  
  quote: "thì cái thời lượng của chương trình ngày hôm nay nó không có đủ thời gian để tôi nói thật sâu về cái bóng đè"
- c152 [▶ 02:29:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8958s): Bác sĩ nói não dùng hai chất trung gian hóa học.  
  quote: "phải dùng một cái chất trung gian hóa"
- c155 [▶ 02:30:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8996s): Hai chất này làm liệt cơ, khiến người ngủ không cử động, không vận động và không nói lung tung.  
  quote: "học này có tác dụng là làm liệt cơ để"
- c173 [▶ 02:40:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9613s): Bác sĩ cho rằng cần giải quyết tình trạng đường ruột này, và các con đường trên đều dẫn tới gốc tự do.  
  quote: "quyết được cái câu chuyện đó thì sẽ hết."
- c196 [▶ 02:47:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10064s): Uống dồn làm nồng độ lên xuống rõ rệt, đầu tháng cao, cuối tháng thấp.  
  quote: "cái chiều hướng này. Cứ lúc thì bác lên lúc thì lại xuống, lúc thì lên lúc lại xuống. Bởi vì đây là đầu tháng đang uống đúng không ạ? Đây là đầu tháng đến đây là bắt đầu là đến giữa tháng và đến đây là cuối tháng. Biên độ đi lên đi xuống rất nhiều."
- c239 [▶ 01:59:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7139s): Bác sĩ nói ông không đồng ý với nhận định rằng bác sĩ tốt rất khó tìm, vì đại đa số bác sĩ ông tiếp xúc đều tốt và giỏi, nhiều người dám dấn thân và hy sinh.  
  quote: "bác sĩ tốt là rất khó. Thế nhưng mà tôi nghĩ không phải như vậy. Đại đa số bác sĩ tôi tiếp xúc đến giờ phút này, tôi có thể nói hầu hết đại đa số đều là bác sĩ rất tốt, đều là bác sĩ rất giỏi. Khi đã"
- c305 [▶ 02:54:46](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10481s): Từ đó thể trạng rất yếu, và bác còn viêm đường ruột dằng dai.  
  quote: "xuất viện đến nay, thể trạng của tôi rất yếu và lại mang thêm trứng viêm đường ruột dằng."
- c326 [▶ 03:17:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11818s): Phần nhận xét ví gan như bếp nấu năng lượng, AST tăng đơn độc giống ngọn khói từ một bếp bị tổn thương vi thể.  
  quote: "Để dễ hình dung, các thể nằm sâu bên trong tế bào gan giống như những gian bếp nhỏ ngày đêm nấu nướng tạo ra năng lượng cho toàn bộ cơ thể."
- c356 [▶ 03:29:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12594s): Thùy giữa của phổi phải được mô tả là đã xẹp hoàn toàn do đàm đặc và tổ chức xơ hóa xâm lấn kéo dài.  
  quote: "Chua chát hơn cả thủy giữa của lá phổi bên phải do bị đầm đặc biệt kín và tổ chức sơ hóa xâm lấn kéo dài đã rơi vào tình trạng dẹp hoàn toàn."
- c361 [▶ 03:31:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12699s): CT cũng cho thấy động mạch chủ có các mảng vôi hóa kéo dài và thoái hóa cột sống ngực nghiêm trọng.  
  quote: "gian và số phận còn hằn sâu lên cung động mạch chủ [âm nhạc] với những mảng vôi hóa kéo dài và tình trạng thoái hóa của sống ngực nghiêm trọng"
- c369 [▶ 03:24:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12255s): Canxi ion hóa giảm nhẹ xuống 1,15 (tham chiếu 1,17 đến 1,29).  
  quote: "và canxi yông hóa giảm nhẹ xuống 1,15 tham chiếu từ 1,17 đến 1,29."
- c395 [▶ 03:37:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13048s): Sau đó chúm môi lại như đang thổi sáo và thở ra chậm trong hai nhịp dài gấp đôi nhịp hít vào.  
  quote: "phổi rồi trúm nhẹ đôi môi lại như đang huyết sáo. Chầm chậm thở ra trong hai nhịp dài gấp đôi nhịp hít vào để tạo nên"
- c455 [▶ 04:20:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15649s): Theo bác sĩ, gốc tự do này tạo thành một vòng xoắn bệnh lý, ảnh hưởng đến não, giấc ngủ (bóng đè) và nhịp tim (lên 170 nhịp mỗi phút), liên quan đến dopamin, serotonin và đường ruột.  
  quote: "cái vòng xoắn và vòng xoắn đó sẽ ảnh hưởng tới chính cái não bộ, ảnh hưởng tới đủ thứ nào là chị rơi vào trạng thái là ngủ thì bị bóng đè. Thế rồi nhịp tim thì bắt đầu là nó rối loạn nó tăng lên 170 nhịp trên phút. Có đúng không ạ? Bởi"
- c469 [▶ 04:24:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15853s): Glutamat giữ cho "kìm" ổn định, còn glycin là cánh tay chuyển động.  
  quote: "Tức là toàn bộ cái cụm này là glutamat sẽ là cái tay chính để giữ cho cái kìm nó luôn luôn ổn định, nó luôn luôn chắc. Giữ cho kìm nó luôn luôn ổn định chắc thì chính là glutamat."
- c474 [▶ 04:30:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16248s): Bác sĩ dùng cách này để giải thích vì sao cơ thể không vứt bỏ glutathion sau khi dùng.  
  quote: "nó hỏng mũi rồi thì không hoạt động được nữa. Mà không hoạt động được nữa, vất nó đi thì phí quá. Cho nên phải có quá trình gì ạ? Tái tạo lại."
- c482 [▶ 04:39:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16745s): Bác sĩ cũng nhắc đến kim loại nặng như chì, thủy ngân và asen.  
  quote: "Vâng. kim loại nặng ví dụ như là chủy trì đúng không ạ? Ví dụ như thủy ngân ví dụ như aen vân vân đúng không ạ? Tất cả những cái kim loại nặng này."
- c537 [▶ 05:15:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18927s): Để hai enzyme này hoạt động tốt, bác sĩ nhấn mạnh cần đủ selen, kẽm, vitamin C và vitamin E; thiếu những chất này thì hai "anh thợ" không làm việc được.  
  quote: "Nhất là hai anh này rất cần celen."

### D3. Do the omissions meet R2 ("full-transcript pass")?
**Context.** The 47 kept omissions (plus 19 excluded) were merged from 23 first-pass readers. Each reader listed omissions only within its own time range, so this was not a single read of the whole transcript; q7uDJG8YQ5c had one. Two stretches of the video have neither summary evidence nor an omission anchor:
- 03:01–03:09 [▶ 03:01:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10855s): Khánh Lành reads aloud the biographical tribute to bác Lương Trác Nghiêm (war veteran, carpenter, Hưng Yên).
- 03:40–03:46 [▶ 03:40:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13195s): same tribute and the doctor's reflection on "bài học" (lessons of history and life).

The section "[02:23:53] Thoát vị đĩa đệm…" in the summary covers about 30 minutes with only 3 claims (c298–c300). Its content (bóng đè, serotonin, vitamin D dosing) is covered under other sections: c145–c175 and c193–c196.
**Options:** accept · ask for a dedicated full-transcript omission pass.
**Review:** all 47 omission cards are in [Part 3](#part-3-omissions-47-kept), and the excluded viewer-comment items are in [Part 4](#part-4-excluded-viewer-comment-candidates-batch-06).

### D4. The 24 pass-1 / pass-2 disagreements
Pass 1 and the blind pass 2 classified these claims differently, and a reconciliation step chose the final class. For each, confirm the final class (or overrule it).

| Claim | Pass 1 | Pass 2 | Final | Card |
|---|---|---|---|---|

| c003 | attribution_qualification | supported | **supported** | [c003](#c003) |
| c013 | attribution_qualification | supported | **attribution_qualification** | [c013](#c013) |
| c034 | attribution_qualification | supported | **attribution_qualification** | [c034](#c034) |
| c054 | mismatch | supported | **mismatch** | [c054](#c054) |
| c103 | attribution_qualification | supported | **attribution_qualification** | [c103](#c103) |
| c111 | mismatch | unresolved | **unresolved** | [c111](#c111) |
| c121 | attribution_qualification | supported | **attribution_qualification** | [c121](#c121) |
| c125 | attribution_qualification | supported | **attribution_qualification** | [c125](#c125) |
| c135 | attribution_qualification | supported | **attribution_qualification** | [c135](#c135) |
| c166 | attribution_qualification | supported | **attribution_qualification** | [c166](#c166) |
| c177 | attribution_qualification | supported | **attribution_qualification** | [c177](#c177) |
| c182 | attribution_qualification | supported | **attribution_qualification** | [c182](#c182) |
| c193 | attribution_qualification | supported | **attribution_qualification** | [c193](#c193) |
| c235 | attribution_qualification | supported | **attribution_qualification** | [c235](#c235) |
| c254 | attribution_qualification | supported | **attribution_qualification** | [c254](#c254) |
| c282 | supported | attribution_qualification | **attribution_qualification** | [c282](#c282) |
| c294 | attribution_qualification | supported | **attribution_qualification** | [c294](#c294) |
| c352 | mismatch | supported | **mismatch** | [c352](#c352) |
| c377 | attribution_qualification | supported | **attribution_qualification** | [c377](#c377) |
| c456 | attribution_qualification | unresolved | **unresolved** | [c456](#c456) |
| c471 | mismatch | supported | **mismatch** | [c471](#c471) |
| c478 | mismatch | supported | **mismatch** | [c478](#c478) |
| c500 | attribution_qualification | supported | **attribution_qualification** | [c500](#c500) |
| c509 | attribution_qualification | unresolved | **attribution_qualification** | [c509](#c509) |

Focus on the cases where the final class kept the stricter reading over a pass-2 "supported": c054, c352, c471 and c478 (mismatch), and the 16 attribution_qualification cases. Also check c509: pass 2 said unresolved, but the final class is attribution_qualification. c003 is the only case resolved toward `supported`, so it has no correction.

### D5. Removals: approve deleting sentences?
These four proposals delete or replace a sentence rather than reword it: [c456](#c456), [c541](#c541), [c172](#c172), [c373](#c373).

### D6. c456 and c541: keep `unresolved` or reclassify to `mismatch`?
Both claims are absent from the transcript: c456 is a disclaimer attributed to the doctor, and c541 is an editorial note by the summarizer. The record format allows `mismatch` once a full read confirms absence. The audit kept `unresolved` as the cautious choice. Cards: [c456](#c456), [c541](#c541).

### D7. Keep the caption's literal wording (no chemistry or spelling correction)?
- [c471](#c471): "GSGS" as spoken vs the chemically standard "GSSG".
- [c127](#c127): "sắt hai xun phát khô" (most likely sulfate) vs the summary's "fumarat".
- [c201](#c201): "5 600" / "6 7000 UI", numbers that are unclear in the captions.
Listen and decide whether to quote the caption as is, or to write what you hear.

### D8. Facts to settle by listening
- [c377](#c377): which country? The caption says "như bản" (probably "Nhật Bản"); the summary says Japan.
- [c070](#c070): who says "y xì như lipit" after the speaker-change mark?
- [c488](#c488): who says "Gan, não, thận trong ruột…", and which organs are called detox organs?
- [c111](#c111): "xương cổ đùi" (femoral neck, one site) or "xương cổ, đùi" (two sites)?

### D9. Safety items
- [c401](#c401): breathing instruction. The summary tells a frail patient (42 kg, collapsed lung lobe) to hold his breath 1–1.5 s; the audit reads "1 1,5" as an inhale:exhale ratio. This is the highest-risk item.
- Viewer-comment safety omissions to keep or drop: [o19](#o19-m-safety-viewer-gives-supplements-to-her-teenage-children), [o20](#o20-m-safety-side-effects-of-neurological-and-anti-epileptic-drugs), [o21](#o21-m-safety-fear-of-western-medicine-from-online-healing-groups), [o22](#o22-m-safety-whole-body-rigidity-emergency-care-and-iv-calcium).
- Excluded item 06#8 (no supplements in pregnancy, restricted diet, too little breast milk): see [Part 4](#part-4-excluded-viewer-comment-candidates-batch-06).

### D10. c478 and its dependants c479–c482
The audit says the summary's "ba nguồn chính" loses the numbering: tinh thần comes first unnumbered, then 1 ăn uống, 2 thuốc, 3 kim loại nặng. But c479–c482 (classed supported) number them tinh thần = 1, ăn uống = 2, thuốc = 3, and kim loại nặng as an extra. If you accept c478, c479–c482 need matching edits. Cards: [c478](#c478), [c479](#c479), [c480](#c480), [c481](#c481), [c482](#c482).

### D11. Approve each of the 63 corrections
Every card in [Part 2](#part-2-the-63-proposed-corrections) is a separate yes / no / edit decision. Also decide whether an independent review of all 63 should happen first. So far only a quick-lens review has run, which found and fixed 7 defects: c070, c488, c377, c135, o05, o22, and the checker.

### D12. Committing audit artifacts
The initiative constraint says "no git commit" and the epic done-when says nothing "committed". Ticket 2.2's plan says "commit in logical batches", and PR #9 does commit. Decide which rule applies.

### D13. Ticket 2.2 status
Keep it `in-review` until D2 and D3 are settled, or accept it as done with the documented caveats. The PR body says "do not merge pending human approval".

## Part 2. The 63 proposed corrections
Ordered by claim id. Tags show which decisions each card feeds.

### c013

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 00:06:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=398s)  ·  section start [▶ 00:06:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=389s)  
**Summary section:** [00:06:34] Gốc tự do liên quan đến bệnh mãn tính và ung thư như thế nào?  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** BS Phúc; summary unattributed

- **BEFORE (current summary):** Hình thành gốc tự do bắt đầu từ việc các chất xâm nhập vào cơ thể.
- **AFTER (proposed):** Bác sĩ nói "có thể nói rằng" hầu hết các loại bệnh tật có con đường đi từ quá trình các chất xâm nhập vào cơ thể, hình thành gốc tự do, rồi cuối cùng phát sinh bệnh tật; còn gốc tự do thì ông nói có hai nguồn, trong đó có con đường nội sinh.
- **Why:** The sentence describes the path of disease, not free-radical formation in general. The doctor separately names an endogenous source, so the summary's general statement is too broad.
- **Pass-1 note:** Context 'con đường đi của bệnh tật' dropped; stated as general mechanism of free-radical formation, which the transcript later qualifies (endogenous route from mitochondria/immune system).
- **Pass-2 note (blind):** Matches doctor's description of disease pathway starting from substances entering the body; doctor separately also describes endogenous formation
- **Reconciliation:** The source describes one disease pathway starting with incoming substances, but also names endogenous sources. The summary states the route as general, so retain the conservative qualification issue.
- **Surrounding summary claims:**
  - previous (c012): Bác sĩ nói "có thể nói rằng" hầu hết các loại bệnh tật, trong đó có bệnh mãn tính, bệnh nguy hiểm và cả ung thư, đều đi theo con đường của gốc tự do.
  - next (c014): Nếu không giải quyết được vấn đề gốc tự do thì có thể phát sinh nhiều bệnh khác nhau.
- **Quotes cited:**
  - [▶ 00:06:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=398s) "từ quá trình khi mà các cái chất nó xâm nhập vào cơ thể chúng ta, hình thành ra gốc tự do và đi trên cái con đường của gốc tự do"
  - [▶ 00:09:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=540s) "gốc tự do này nó được phát sinh từ đâu? Nó có hai nguồn."
  - [▶ 00:06:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=389s) "Có thể nói rằng hầu hết tất cả các cái loại bệnh tật"

  Transcript 00:06:19–00:07:08 · [▶ watch from 00:06:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=379s)

  ```text
    [00:06:19] tới hiện tượng rụng lá sẽ dẫn tới là hoa
    [00:06:22] quả bắt đầu là chín và thối giữa ra và
    [00:06:25] rụng xuống cũng như là củ quả bắt đầu là
    [00:06:27] đến cái mùa thu hoạch. Đấy chính là cái
    [00:06:29] lý do của gốc tự do ở bên trong cơ thể
    [00:06:32] của các loài thực vật. Và trong cơ thể
  ▶ [00:06:34] con người chúng ta cũng vậy. Có thể nói
  ▶ [00:06:37] rằng hầu hết tất cả các cái loại bệnh
  ▶ [00:06:39] tật, những cái con đường đi của nó từ
  ▶ [00:06:43] các cái bước quá từ quá trình khi mà các
  ▶ [00:06:45] cái chất nó xâm nhập vào cơ thể chúng
  ▶ [00:06:47] ta, hình thành ra gốc tự do và đi trên
  ▶ [00:06:50] cái con đường của gốc tự do để cuối cùng
    [00:06:52] nó phát sinh ra những bệnh tật và hầu
    [00:06:54] hết những các cái bệnh tật mãn tính,
    [00:06:56] những bệnh tật cực kỳ nguy hiểm và đặc
    [00:06:58] biệt kể cả những bệnh về ung thư đều
    [00:07:00] xuất phát từ cái con đường của gốc tự
    [00:07:02] do. Và nếu như không giải quyết được vấn
    [00:07:04] đề gốc tự do thì chúng ta sẽ phát sinh
    [00:07:07] ra rất rất nhiều các cái bệnh tật khác
    [00:07:08] nhau. Đó chính là cái lý do mà ngày hôm
  ```

  Transcript 00:08:50–00:09:30 · [▶ watch from 00:08:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=530s)

  ```text
    [00:08:50] glutathon là một cái thành phần để chống
    [00:08:52] lại các gốc tự do. Nhưng để biết được
    [00:08:54] tác dụng của glutathon như thế nào thì
    [00:08:57] chúng ta rất quan trọng là chúng ta phải
    [00:08:59] hiểu cái gốc tự do. Vậy gốc tự do nếu
    [00:09:02] như ta viết tắt thì là chữ R, chữ O, chữ
  ▶ [00:09:05] S gì? À gốc tự do này nó được phát sinh
  ▶ [00:09:08] từ đâu? Nó có hai nguồn. Đó, một là cái
    [00:09:10] con ng đường theo con đường gọi là nội
    [00:09:12] sinh. Nội sinh có nghĩa là cái gì? có
    [00:09:15] nghĩa là từ trong chính cơ thể của chúng
    [00:09:17] ta sinh ra. Thế thì con đường nội sinh
    [00:09:20] này nó được sinh ra như thế nào? Chúng
    [00:09:23] ta sẽ hình dung rằng trong tế bào của
    [00:09:25] chúng ta có một cái bào quan vô cùng
    [00:09:27] quan trọng đó chính là gì ạ? Chính là ti
    [00:09:30] thể đúng không ạ?
  ```

### c034

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 00:16:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=984s)  ·  section start [▶ 00:15:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=939s)  
**Summary section:** [00:15:44] Gốc tự do ngoại nhập từ chế độ ăn uống  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** BS Trần Văn Phúc; summary unattributed

- **BEFORE (current summary):** Chất béo chuyển hóa được mô tả là chất béo bị đốt cháy quá mức, ví dụ đồ chiên rán, hoặc dầu thực vật bị dùng sai khi rán, dẫn đến chuyển hóa thành chất béo trung gian.
- **AFTER (proposed):** Chất béo chuyển hóa được bác sĩ mô tả là những chất béo "bị đốt cháy là dở dở đi" (bản ghi âm ghi như vậy, nghĩa chưa rõ), ví dụ đồ chiên rán; còn dầu thực vật dùng sai khi rán thì chuyển hóa thành chất béo trung gian.
- **Why:** 'Quá mức' (excessive) is not what the caption says. The caption is garbled, so the proposal keeps it as spoken and marks it unclear instead of interpreting it.
- **Pass-1 note:** Added/hardened qualifier: summary says 'đốt cháy quá mức' but transcript says 'đốt cháy là dở dở' (half/partially burned, ambiguous); rest (fried food, misused vegetable oil -> intermediate fat) matches.
- **Pass-2 note (blind):** Borderline: transcript 'đốt cháy là dở dở đi' is garbled; summary renders it as 'đốt cháy quá mức'; examples and 'chất béo trung gian' match
- **Reconciliation:** The source wording “đốt cháy là dở dở” is garbled/ambiguous; “quá mức” is not securely established. Retain the qualification issue.
- **Surrounding summary claims:**
  - previous (c033): Các nguyên nhân được nêu gồm: hóa chất và thuốc trừ sâu trong thực phẩm, chất bảo quản thực phẩm; ăn sai, ăn thừa, ăn mất cân đối, đặc biệt là đường; chất béo ăn sai, nhất là chất béo no bão hòa, và chất béo chuyển hóa được xem là nguy hiểm hơn.
  - next (c035): Thực phẩm không đảm bảo vệ sinh hay an toàn cũng có thể gây ra hiện tượng này.
- **Quotes cited:**
  - [▶ 00:16:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=984s) "những chất béo mà khi chúng ta bị đốt cháy là dở dở đi ấy. Ví dụ như là đồ chiên dàn chẳng hạn."
  - [▶ 00:16:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=993s) "là dầu thực vật mà chúng ta thực hiện trên dán thì nó sẽ chuyển hóa thành cái chất béo trung gian."

  Transcript 00:16:14–00:17:03 · [▶ watch from 00:16:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=974s)

  ```text
    [00:16:15] nguy hiểm đúng không ạ? Đường thứ hai đó
    [00:16:17] là chất béo mà chúng ta ăn sai cũng cực
    [00:16:19] kỳ nguy hiểm. Đặc biệt là ăn chất béo gì
    [00:16:22] ạ?
    [00:16:23] >> Chất béo no bão hòa. Chất béo chuyển hóa
    [00:16:25] là nguy hiểm hơn nữa.
    [00:16:27] >> Chất béo chuyển hóa đó là gì? Đó là
  ▶ [00:16:29] những chất béo mà khi chúng ta bị đốt
  ▶ [00:16:32] cháy là dở dở đi ấy. Ví dụ như là đồ
  ▶ [00:16:34] chiên dàn chẳng hạn.
    [00:16:36] >> Thế rồi chúng ta sử dụng sai ví dụ như
  ▶ [00:16:38] là dầu thực vật mà chúng ta thực hiện
  ▶ [00:16:41] trên dán thì nó sẽ chuyển hóa thành cái
  ▶ [00:16:44] chất béo trung gian. Ngoài mất cân bằng
    [00:16:47] về tỉ lệ thì còn có những cái quá trình
    [00:16:49] mà chúng ta chế biến sai thì chất béo sẽ
    [00:16:51] ảnh hưởng. Cộng với lại ví dụ như đạn
    [00:16:54] cũng thế. đạn chúng ta ăn sai, ăn không
    [00:16:56] đúng cách, ăn quá nhiều hoặc ăn quá ít
    [00:16:58] cũng là những cái nguyên nhân để gây ra
    [00:17:00] gốc tự do. Đó. Thế thì nh cái con đường
    [00:17:03] ăn uống chúng ta tưởng rằng là ăn tốt
  ```

### c045

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 00:38:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2305s)  ·  section start [▶ 00:33:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2017s)  
**Summary section:** [00:33:42] Hydro peroxit (H₂O₂, oxy già)  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** BS Trần Văn Phúc ('sủi bọt' first prompted after a >> speaker change, then repeated by doctor); summary unattributed

- **BEFORE (current summary):** Theo bài, H₂O₂ được cho vào vết thương để phá hủy mô hoại tử, virus và vi khuẩn, làm sạch vết thương, và sủi bọt.
- **AFTER (proposed):** Theo bài, H₂O₂ được cho vào vết thương; bác sĩ nói nó phá hủy các mô, phá hủy virus vi khuẩn, làm sạch vết thương và sủi bọt.
- **Why:** The transcript says 'các cái mô' (tissues). 'Hoại tử' (necrotic) is a qualifier the summary added.
- **Pass-1 note:** Added qualifier: summary says 'mô hoại tử' but transcript says generic 'các cái mô' (destroys tissue), not specifically necrotic tissue.
- **Pass-2 note (blind):** Added qualifier: transcript says destroys 'các cái mô' (tissues), summary narrows to 'mô hoại tử'
- **Surrounding summary claims:**
  - previous (c044): Nó có vẻ bề ngoài yên ổn vì đã cân bằng điện tích, nhưng bên trong là một cặp không bền vững, nên có thể dễ dàng phân ly.
  - next (c046): Gốc hydroxyl là một nhóm OH có một electron lạc.
- **Quotes cited:**
  - [▶ 00:38:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2305s) "thành phần mà tại sao oxy già chúng ta sẽ cho vào những vết thương."
  - [▶ 00:38:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2312s) "nó phá hủy các cái mô, nó phá hủy virus vi khuẩn, nó làm sạch những cái vết thương"
  - [▶ 00:38:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2319s) "trên sủi bọt lên."

  Transcript 00:38:15–00:39:09 · [▶ watch from 00:38:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2295s)

  ```text
    [00:38:15] bề ngoài thì nó yên ổn nhưng bên trong
    [00:38:18] là hai vợ chồng nó đang ủ mưu rất khủng
    [00:38:21] khiếp.
    [00:38:22] Đấy, nó ủ mưu nó ủ mưu tính đến chuyện
    [00:38:25] bắt đầu nó đi cướp bóc phá làng phá xóm
    [00:38:27] thì chúng ta sẽ thấy H2O2 chính là cái
  ▶ [00:38:30] thành phần mà tại sao oxy già chúng ta
  ▶ [00:38:32] sẽ cho vào những vết thương. những cái
    [00:38:34] vết thương cho vào cái ngay lập tức nó
    [00:38:36] tiêu hủy,
  ▶ [00:38:37] >> nó phá hủy các cái mô, nó phá hủy virus
  ▶ [00:38:40] vi khuẩn, nó làm sạch những cái vết
  ▶ [00:38:42] thương và nó đùn đẩy lên
    [00:38:44] >> sủi bọt
  ▶ [00:38:44] >> trên sủi bọt lên. Đấy chính là cái lý do
    [00:38:47] của H2O2 này.
    [00:38:48] >> Vâng.
    [00:38:49] >> Vậy chúng ta sẽ thấy rằng à khi cái gia
    [00:38:52] đình này, cái gia đình này thì hai gia
    [00:38:54] đình, gia đình thứ nhất lừa gia đình thứ
    [00:38:56] hai để chuyển cái đứa con hư hỏng của
    [00:38:58] mình sang, cái đứa con lạc loài sang thì
    [00:39:00] trở thành gia đình hạnh phúc. Nhưng gia
    [00:39:02] đình thứ hai bất ổn ở chỗ là nó không có
    [00:39:04] phòng, nó đi kiếm hai nó cướp ngay lập
    [00:39:07] tức cướp H+ để trở thành H2O2. Và nó
  ```

### c054

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 00:45:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2754s)  ·  section start [▶ 00:45:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2717s)  
**Summary section:** [00:45:22] Ozon: gốc tự do thứ tư  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc; consistent

- **BEFORE (current summary):** Ozon không cướp trực tiếp như các gốc khác, mà xen vào các phân tử oxy khác, tạo thành cuộc "tình tay ba", và từ đó sinh ra gốc tự do.
- **AFTER (proposed):** Ozon được mô tả là có thêm một oxy nữa xen vào oxy hai nguyên tử, thành cuộc "tình tay ba"; ozon không đi ăn cướp, nhưng gặp chỗ nào xen được thì xen vào câu chuyện của các gia đình khác, và từ đó cũng tạo ra một gốc tự do.
- **Why:** In the transcript the love triangle is ozone itself (a third oxygen joining O2). Ozone interjects into other 'families' only afterward; the summary moves the metaphor to that later step.
- **Pass-1 note:** In transcript the 'tình tay ba' is ozone's own structure (a third oxygen inserted into O2), and ozone then pushes one oxygen into other 'families'; summary says ozone inserts into other oxygen molecules to create the love triangle — mechanism/entity mis-stated. 'Không cướp' and 'sinh ra gốc tự do' parts are supported.
- **Pass-2 note (blind):** Borderline: in transcript the 'tình tay ba' is ozone itself (third O joining O2), and ozone then interjects into 'các gia đình khác'; summary compresses ordering but core claims (no direct robbing, interjecting, generates free radicals) match
- **Reconciliation:** The “tình tay ba” is ozone formation (a third oxygen joins O2); only afterward does ozone interject into other families. The summary relocates the metaphor. Final mismatch.
- **Surrounding summary claims:**
  - previous (c053): Nó hình thành trong không khí khi có tia lửa điện, tiếng sét đánh xuống.
  - next (c055): Ba gốc tự do đầu tiên (superoxit, H₂O₂, hydroxyl) được nói là tấn công ba thành phần quan trọng: màng tế bào, protein và nhân (ADN).
- **Quotes cited:**
  - [▶ 00:45:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2754s) "Thế bây giờ có thêm một cái oxy nữa nó xen vào đây trở thành cuộc tình tay ba."
  - [▶ 00:47:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2823s) "không đi ăn cướp nhưng cái này nó đi nó xen vào câu chuyện của các gia đình khác"
  - [▶ 00:46:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2804s) "Từ đây nó sẽ dẫn tới là ozon này cứ đi gặp bất cứ chỗ nào mà có thể xen được vào là nó xen."
  - [▶ 00:47:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2819s) "Đây là cái lý do mà cũng lại tạo ra một cái gốc tự do."

  Transcript 00:45:44–00:47:33 · [▶ watch from 00:45:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2744s)

  ```text
    [00:45:44] mà khi có tia lửa điện khi mà tiếng sét
    [00:45:47] nó đánh xuống ấy
    [00:45:48] >> thì không khí bắt đầu xuất hiện cái khí
    [00:45:50] ozon là O3.
    [00:45:51] >> Vâng.
    [00:45:51] >> Thì ozon thì nó lại là như thế này.
    [00:45:54] Chúng ta hình dung rằng oxy hạnh phúc đó
    [00:45:57] chính là chỉ có hai thôi.
  ▶ [00:45:59] >> Thế bây giờ có thêm một cái oxy nữa nó
  ▶ [00:46:02] xen vào đây trở thành cuộc tình tay ba.
    [00:46:05] Thì cái này chính là cái này chính là
    [00:46:07] cuộc tình tay ba.
    [00:46:09] Và cái cuộc tình tai ba này mới là cái
    [00:46:12] cuộc tình mà rất nguy hiểm. Nó nguy hiểm
    [00:46:14] ở chỗ rằng là cái ông bây giờ một cái
    [00:46:18] ông chồng ông có hai bà vợ. Thế thì hai
    [00:46:21] bà vợ đó thì hai bà vợ lại có vai trò nó
    [00:46:24] cứ giống giống nhau.
    [00:46:25] >> Ông ấ lúc thì ông phân vân bên này, lúc
    [00:46:27] ông phân vân bên kia và hai bà vợ không
    [00:46:29] để cho ông yên cho nên ông ấy luôn luôn
    [00:46:32] có xu hướng là đẩy cái một bà vợ đi để
    [00:46:35] trở thành một cái gia đình yên ổn. Thế
    [00:46:38] thôi. Và nếu cứ để ba thế này thì gia
    [00:46:40] đình nhà ông luôn luôn lục đục. Vậy bất
    [00:46:42] cứ lúc nào có cơ hội thì ông sẽ đẩy một
    [00:46:45] bà vợ đi.
    [00:46:46] >> Vâng.
    [00:46:46] >> Thế thôi để ông ấy tạo thành một gia
  ▶ [00:46:49] đình hạnh phúc. Từ đây nó sẽ dẫn tới là
  ▶ [00:46:52] ozon này cứ đi gặp bất cứ chỗ nào mà có
  ▶ [00:46:55] thể xen được vào là nó xen.
    [00:46:57] >> Vâng.
    [00:46:58] >> Đấy. Cứ gặp chỗ nào xen được vào thì bắt
    [00:47:00] đầu là nó xen vào. Nó x để nó cho một
    [00:47:02] cái oxy này.
  ▶ [00:47:04] >> Vâng. Đây là cái lý do mà cũng lại tạo
  ▶ [00:47:06] ra một cái gốc tự do. Thế thì cái này nó
  ▶ [00:47:08] không đi ăn cướp nhưng cái này nó đi nó
  ▶ [00:47:10] xen vào câu chuyện của các gia đình khác
    [00:47:13] và từ đây nó sẽ gây ra một cái vấn đề
    [00:47:15] rất phức tạp về sau. Thì đấy chính là
    [00:47:18] cái gốc tự do thứ tư. Thế bây giờ ba cái
    [00:47:22] gốc tự do trên này, gốc tự do số 1, số
    [00:47:25] 2, số 3 thì nó sẽ như thế nào? Gốc tự do
    [00:47:29] số 1, số 2, số 3 này nó sẽ đi nó tấn
    [00:47:31] công vào tất cả những cái thành phần và
  ```

### c066

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 00:53:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3224s)  ·  section start [▶ 00:48:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2930s)  
**Summary section:** [00:48:55] Gốc tự do tấn công màng tế bào: lipid và lipit peroxit  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Doctor reports the analogy as 'người ta ví' (others' comparison); summary attributes the analogy to the doctor himself

- **BEFORE (current summary):** Bác sĩ ví màng tế bào như một bãi xăng, nên một gốc tự do cũng đủ làm sụp đổ hệ thống.
- **AFTER (proposed):** Bác sĩ thuật lại rằng người ta ví màng tế bào như một bãi xăng, nên chỉ cần một gốc tự do tấn công màng tế bào là ngay lập tức sụp đổ hệ thống.
- **Why:** The doctor reports the comparison as 'người ta ví rằng' (others compare it); the summary credits it to him.
- **Pass-1 note:** Attribution shifted: 'người ta ví rằng' → 'Bác sĩ ví'; content otherwise matches.
- **Pass-2 note (blind):** Source of analogy shifted from 'người ta ví' to the doctor
- **Surrounding summary claims:**
  - previous (c065): Tế bào hoại tử sinh ra các độc chất, và độc chất này lại tạo thêm gốc tự do.
  - next (c067): Đây được gọi là gốc tự do thứ năm, lipit peroxit.
- **Quotes cited:**
  - [▶ 00:53:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3224s) "người ta ví rằng màng tế bào nó giống như là một bãi"
  - [▶ 00:53:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3228s) "Vậy chỉ cần một gốc tự do tấn công màn tế bào ngay lập tức nó sụp đổ hệ"

  Transcript 00:53:34–00:54:18 · [▶ watch from 00:53:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3214s)

  ```text
    [00:53:37] l có dấu chấm, hai là lo 3 là loh đều là
    [00:53:42] gốc tự do hết.
    [00:53:43] >> Vâng.
    [00:53:44] >> Và nó trở thành những kẻ cướp. Và chúng
    [00:53:46] ta sẽ thấy rằng khi phản ứng xảy ra ở
  ▶ [00:53:49] màng tế bào thế này, người ta ví rằng
  ▶ [00:53:52] màng tế bào nó giống như là một bãi
  ▶ [00:53:53] xăng. Vậy chỉ cần một gốc tự do tấn công
  ▶ [00:53:56] màn tế bào ngay lập tức nó sụp đổ hệ
    [00:53:58] thống.
    [00:53:59] >> Vâng.
    [00:53:59] >> Với một tốc độ rất nhanh nó giống như là
    [00:54:01] đám cháy của bãi xăng. Không có con
    [00:54:03] đường nào ngăn chặn nữa cả và lập tức sẽ
    [00:54:06] hủy hoại tế bào ngay lập tức. Thì đây là
    [00:54:09] cái mà tấn công vào lipit màng tế bào là
    [00:54:11] tấn công khủng khiếp nhất và đây là cuộc
    [00:54:14] cướp tàn bạo nhất. Nó tạo thành ra cả
    [00:54:17] một làng xóm đen cướp với nhau và dẫn
  ```

### c068

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 00:53:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3198s)  ·  section start [▶ 00:48:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2930s)  
**Summary section:** [00:48:55] Gốc tự do tấn công màng tế bào: lipid và lipit peroxit  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc; summary 'Bác sĩ nói' — speaker correct

- **BEFORE (current summary):** Bác sĩ nói hậu quả có thể là bệnh mãn tính, lão hóa và nhiều bệnh khác.
- **AFTER (proposed):** Bác sĩ nói tế bào hoại tử, tế bào chết đi thì sẽ sinh ra bệnh mãn tính, sẽ bị lão hóa và sẽ bị đủ thứ bệnh.
- **Why:** Softened hedge only: the doctor says 'sẽ' (will), the summary says 'có thể'. The proposal restores his wording.
- **Pass-1 note:** Hedge added: doctor states categorically 'sẽ' (will); summary softens to 'có thể'.
- **Pass-2 note (blind):** Softened: doctor says 'sẽ' (will); summary says 'có thể là'
- **Surrounding summary claims:**
  - previous (c067): Đây được gọi là gốc tự do thứ năm, lipit peroxit.
  - next (c069): Gốc tự do OH cướp electron và H+ của protein lành, khiến protein trở thành protein có dấu chấm (gốc tự do).
- **Quotes cited:**
  - [▶ 00:53:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3198s) "sinh ra bệnh mãn tính, chúng ta sẽ bị lão hóa"
  - [▶ 00:53:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3202s) "chúng ta sẽ bị đủ thứ bệnh trên"
  - [▶ 00:53:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3196s) "tế bào chết đi tức là chúng ta sẽ sinh ra bệnh mãn tính"

  Transcript 00:53:06–00:53:52 · [▶ watch from 00:53:06](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3186s)

  ```text
    [00:53:06] tế bào bị gì ạ? Tế bào bị hoại tử.
    [00:53:08] >> Vâng.
    [00:53:09] >> Tế bào hoại tử và nó sẽ tạo ra những các
    [00:53:12] cái độc chất
    [00:53:14] >> rất nguy hiểm đối với cơ thể và chính
    [00:53:16] những độc chất này lại quay trở lại tạo
    [00:53:18] thành gốc tự do.
    [00:53:19] >> Vâng.
    [00:53:19] >> Vậy chúng ta sẽ thấy rằng tế bào hoại
  ▶ [00:53:21] tử, tế bào chết đi tức là chúng ta sẽ
  ▶ [00:53:23] sinh ra bệnh mãn tính, chúng ta sẽ bị
  ▶ [00:53:25] lão hóa, chúng ta sẽ bị già nua.
  ▶ [00:53:27] >> Vâng. chúng ta sẽ bị đủ thứ bệnh trên
    [00:53:30] đời này. Đó chính là gốc tự do thứ năm
    [00:53:33] đó là lipit peroit. Nó bao gồm có một là
    [00:53:37] l có dấu chấm, hai là lo 3 là loh đều là
    [00:53:42] gốc tự do hết.
    [00:53:43] >> Vâng.
    [00:53:44] >> Và nó trở thành những kẻ cướp. Và chúng
    [00:53:46] ta sẽ thấy rằng khi phản ứng xảy ra ở
    [00:53:49] màng tế bào thế này, người ta ví rằng
    [00:53:52] màng tế bào nó giống như là một bãi
  ```

### c070

**Decisions:** D8, D11 (correction approval)  
**Watch:** [▶ 00:55:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3310s)  ·  section start [▶ 00:54:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3259s)  
**Summary section:** [00:54:24] Gốc tự do tấn công protein và enzyme (gốc tự do thứ sáu)  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Bác sĩ Trần Văn Phúc; consistent

- **BEFORE (current summary):** Oxy hoặc ozon sau đó xâm nhập vào để tạo thành POOH, và protein này giống hệt protein bị hỏng.
- **AFTER (proposed):** Protein có dấu chấm bị oxy lợi dụng xâm nhập, hoặc ozon nhường oxy vào, để thành PO trừ; PO trừ lại cướp H+ để tạo thành POOH. Protein đi theo con đường giống hệt lipit (câu này đứng sau dấu đổi người nói trong bản ghi âm).
- **Why:** 'Giống hệt protein bị hỏng' is not in the transcript: the comparison is to the lipid pathway. The summary also skips the PO- step before POOH. The 'y xì như lipit' line follows a speaker-change mark, so the proposal names no speaker for it. Human to confirm the speaker.
- **Pass-1 note:** Oxy/ozon forms PO⁻, which then steals H+ to form POOH (step omitted); transcript's comparison is that the protein pathway is identical to the lipid pathway, not that POOH 'giống hệt protein bị hỏng' — summary's 'protein bị hỏng' is not said.
- **Pass-2 note (blind):** Transcript never says POOH is 'giống hệt protein bị hỏng'; the 'giống hệt' comparison is to the lipid pathway; also oxy/ozon forms PO− first, POOH only after stealing H+
- **Surrounding summary claims:**
  - previous (c069): Gốc tự do OH cướp electron và H+ của protein lành, khiến protein trở thành protein có dấu chấm (gốc tự do).
  - next (c071): Protein bao gồm các thành phần như enzyme, dùng để thực hiện phản ứng hóa học.
- **Quotes cited:**
  - [▶ 00:55:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3310s) "hoặc là ozon nó nhường oxy vào đây để trở thành gì ạ? PO tr-"
  - [▶ 00:55:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3324s) "Để tạo thành là POOH giống hệt protein"
  - [▶ 00:55:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3331s) "y xì như lipit và protein cũng lại giống"
  - [▶ 00:55:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3317s) "Sau đó PO trừ lại không đang thiếu vật liệu để xây phòng lại cướp gì ạ? Cướp H+ đúng không ạ?"

  Transcript 00:55:00–00:56:01 · [▶ watch from 00:55:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3300s)

  ```text
    [00:55:01] sẽ cướp cái
    [00:55:02] >> electron và
    [00:55:02] >> E và cướp H+. Đúng rồi. Vâng.
    [00:55:05] >> Từ đây nó sẽ trở thành protein có dấu
    [00:55:09] chấm ở đây. Protein này lúc này lại bị
    [00:55:12] gì ạ? Oxy nó lợi dụng.
    [00:55:14] >> Vâng.
    [00:55:14] >> Nó xâm nhập vào.
  ▶ [00:55:15] >> Vâng. hoặc là ozon nó nhường oxy vào đây
  ▶ [00:55:18] để trở thành gì ạ? PO tr- đúng không ạ?
    [00:55:22] >> Vâng.
  ▶ [00:55:22] >> Sau đó PO trừ lại không đang thiếu vật
  ▶ [00:55:25] liệu để xây phòng lại cướp gì ạ? Cướp H+
  ▶ [00:55:28] đúng không ạ?
  ▶ [00:55:29] >> Để tạo thành là POOH giống hệt protein
    [00:55:33] rồi.
    [00:55:33] >> Vâng.
    [00:55:34] >> Thế thì chúng ta sẽ lại có
  ▶ [00:55:36] >> y xì như lipit và protein cũng lại giống
    [00:55:38] hệt nhau.
    [00:55:39] >> Vâng. con đường đi thế mà protein thì
    [00:55:42] chính là các cái thành phần tôi lấy ví
    [00:55:44] dụ như là enzyme chẳng hạn.
    [00:55:46] >> Vâng.
    [00:55:46] >> Enzyme để thực hiện phản ứng hóa học.
    [00:55:48] Thế thì nếu như mà nó tấn công vào
    [00:55:51] protein, tức là tấn công vào enzyme, vậy
    [00:55:53] thì các phản ứng hóa học trong cơ thể
    [00:55:56] của chúng ta bị ngừng lại.
    [00:55:57] >> Vâng.
    [00:55:57] >> Chúng ta sẽ sinh ra một loạt bệnh.
    [00:56:00] >> Các hoạt động trong cơ thể của chúng ta
    [00:56:01] cần phải có enzyme mà.
  ```

### c079

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 00:58:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3504s)  ·  section start [▶ 00:56:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3366s)  
**Summary section:** [00:56:11] Gốc tự do tấn công ADN và mã di truyền G (gốc tự do thứ bảy)  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Phúc; summary implicit bác sĩ (correct)

- **BEFORE (current summary):** Đột biến gen có thể gây bệnh hiếm và ung thư.
- **AFTER (proposed):** Đột biến gen sẽ gây ra bệnh nguy hiểm, bệnh hiếm và ung thư.
- **Why:** Softened hedge: the doctor says 'sẽ gây ra', the summary says 'có thể gây'. 'Bệnh nguy hiểm' was also dropped. The proposal restores his wording.
- **Pass-1 note:** CHANGED from pass-1 'supported': hedge ADDED (softened) — doctor states categorically 'sẽ gây ra' bệnh nguy hiểm/bệnh hiếm and ung thư (also 00:59:07 'sinh ra đủ các cái thứ bệnh, bệnh hiếm, bệnh ung thư'); summary says 'có thể gây'. Also drops 'bệnh nguy hiểm'. Low severity (summary is more cautious than speaker).
- **Pass-2 note (blind):** Softened: 'sẽ gây ra' becomes 'có thể gây'
- **Surrounding summary claims:**
  - previous (c078): Khi tổng hợp ADN mới, G có thể bị nhầm thành T, dẫn đến đột biến gen.
  - next (c080): Bác sĩ nói có bảy gốc tự do cần nhớ, chưa kể các gốc tự do phụ khác.
- **Quotes cited:**
  - [▶ 00:58:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3504s) "mà đột biến gen này thì sẽ gây ra một là"
  - [▶ 00:58:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3507s) "bệnh nguy hiểm, bệnh hiếm đúng không ạ?"
  - [▶ 00:58:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3509s) "Hai là gây ra gì ạ? Ung thư."

  Transcript 00:58:14–00:58:59 · [▶ watch from 00:58:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3494s)

  ```text
    [00:58:15] bị gì ạ? Sẽ bị lỗi. Vâng.
    [00:58:17] >> Lỗi bằng cách là đang nhầm cái G với lại
    [00:58:19] cái gì ạ? Cái T. [hắng giọng]
    [00:58:20] >> Thì G thì nó lại cứ tưởng là T thì T nó
    [00:58:23] ghép G vào.
    [00:58:24] >> Vâng. Vậy từ đây suy ra tổng hợp gì ạ?
    [00:58:27] Nó bị đột biến gen.
    [00:58:28] >> Đột biến gen
  ▶ [00:58:29] >> mà đột biến gen này thì sẽ gây ra một là
  ▶ [00:58:32] bệnh nguy hiểm, bệnh hiếm đúng không ạ?
  ▶ [00:58:34] >> Hai là gây ra gì ạ? Ung thư. Nó gây ra
    [00:58:38] những các cái con đường đó.
    [00:58:40] >> Vâng.
    [00:58:40] >> Thì đây chính là tấn công vào ADN. Vậy
    [00:58:44] ta nhớ rằng ADN nó còn nguy hiểm hơn ở
    [00:58:46] chỗ một là gì ạ? Là nó tạo ra gốc tự do.
    [00:58:52] Hai là nó gây ra đột biến gì ạ? Đột biến
    [00:58:54] gen mà đột biến là từ cái guanin này,
    [00:58:58] >> từ cái mã mật mã di truyền này nó rất dễ
  ```

### c084

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 00:59:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3569s)  ·  section start [▶ 00:59:12](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3547s)  
**Summary section:** [00:59:12] Tóm tắt bảy gốc tự do và cách hiểu gốc tự do  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Phúc; summary attributes to bác sĩ (correct)

- **BEFORE (current summary):** Bác sĩ nói nếu chỉ đọc tài liệu thông thường thì khó hiểu, nhưng cách phân tích này giúp dễ nhớ hơn.
- **AFTER (proposed):** Bác sĩ nói nếu tự đi tìm đọc về gốc tự do thì "chắc chắn" sẽ không thể hiểu được vì nó rất rắc rối, nhưng nếu hiểu theo cách ông phân tích thì từ nay sẽ nhớ được.
- **Why:** Softened hedge: 'chắc chắn ... sẽ không thể hiểu được' became 'khó hiểu'. 'Tài liệu thông thường' is the summary's own wording.
- **Pass-1 note:** Softened: doctor says self-reading 'chắc chắn ... không thể hiểu được' (repeated 01:08:34 'tự đọc sách, tự đọc tài liệu, chúng ta sẽ không hiểu'); summary says only 'khó hiểu'. 'tài liệu thông thường' is summary wording. Pass-1 confirmed.
- **Pass-2 note (blind):** Borderline: softened 'chắc chắn ... sẽ không thể hiểu được' to 'khó hiểu'
- **Surrounding summary claims:**
  - previous (c083): Nó khát khao được ổn định nên cướp electron và H+, và trong quá trình đó nó biến các đối tượng bị cướp thành tội phạm khác.
  - next (c085): Bác sĩ mô tả ba bước.
- **Quotes cited:**
  - [▶ 00:59:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3569s) "gốc tự do là gì thì chắc chắn quý vị sẽ"
  - [▶ 00:59:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3572s) "không thể hiểu được và Khánh lành cũng"
  - [▶ 00:59:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3582s) "nay trở đi chúng ta sẽ nhớ được gốc tự"
  - [▶ 00:59:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3575s) "bởi vì nó sẽ rất rắc rối"

  Transcript 00:59:19–01:00:12 · [▶ watch from 00:59:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3559s)

  ```text
    [00:59:19] khác nhưng ít nhất quý vị phải nhớ được
    [00:59:21] bảy gốc tự do này. Và Khánh Lành có thấy
    [00:59:24] khó quá về gốc tự do không? Vâng, tôi
    [00:59:26] thấy sau khi phân tích thì tôi cũng thấy
    [00:59:29] khá là dễ hiểu.
    [00:59:31] >> Tôi cho rằng là nếu quý vị đi tìm đọc về
  ▶ [00:59:34] gốc tự do là gì thì chắc chắn quý vị sẽ
  ▶ [00:59:37] không thể hiểu được và Khánh lành cũng
    [00:59:39] sẽ không thể hiểu được gốc tự do là cái
  ▶ [00:59:40] gì bởi vì nó sẽ rất rắc rối. Nhưng nếu
    [00:59:44] chúng ta hiểu theo cái cách mà tôi phân
    [00:59:46] tích một cách tường minh như thế này, từ
  ▶ [00:59:47] nay trở đi chúng ta sẽ nhớ được gốc tự
    [00:59:49] do nó là gì. Vậy gốc tự do ở đây nó là
    [00:59:53] có gì ạ? xu hướng có một electron độc
    [00:59:55] thân.
    [00:59:56] >> Vâng.
    [00:59:56] >> Đó là đứa con lạc loài xâm nhập vào một
    [00:59:58] gia đình hạnh phúc.
    [01:00:00] >> Sau đó thì đứa con độc thân đó nó khát
    [01:00:02] khao được kẹt đôi.
    [01:00:04] >> Vâng.
    [01:00:04] >> Nó khát khao có một gia đình ổn định.
    [01:00:06] >> Vâng.
    [01:00:07] >> Nó muốn trở thành gì ạ? Đứa con lương
    [01:00:09] thiện. Một gia đình lương thiện. Do vậy
    [01:00:11] nó cướp tiếp h+ nữa.
  ```

### c103

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 01:06:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3978s)  ·  section start [▶ 01:06:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3974s)  
**Summary section:** [01:06:19] Glutathion được quảng cáo để làm trắng da: nội dung số phát sóng  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Doctor asks what it is advertised for; the phrase 'chất chống oxy hóa giúp trắng da' is answered by Khánh Lành (>> marker), doctor confirms 'Giúp trắng da'; summary attributes all to doctor

- **BEFORE (current summary):** Bác sĩ nói glutathion đang được quảng cáo là chất chống oxy hóa giúp trắng da và nhiều người mua về bổ sung.
- **AFTER (proposed):** Bác sĩ nói người ta quảng cáo rất nhiều về glutathion; người đáp là Khánh Lành nêu chủ yếu với tác dụng là chất chống oxy hóa giúp trắng da, bác sĩ xác nhận "giúp trắng da" và nói rất nhiều người mua về, nhất là chị em phụ nữ.
- **Why:** Speaker split: the antioxidant wording is the host's answer after a speaker change. The doctor confirms only whitening and that many people buy it.
- **Pass-1 note:** Speaker split: antioxidant/whitening wording is MC's answer, doctor only confirms whitening and that many (esp. women) buy it.
- **Pass-2 note (blind):** Borderline attribution: the 'chống oxy hóa' wording is the MC's answer, which the doctor affirms
- **Reconciliation:** The host supplies the “chất chống oxy hóa” wording and the doctor confirms the whitening effect; the summary attributes the whole formulation to the doctor. Retain attribution issue.
- **Surrounding summary claims:**
  - previous (c102): Glutathion là đội quân di động, ở đâu có gốc tự do thì nó đến đó, và được gọi là "ông vua" chống các chất khử và chất gốc oxy hóa.
  - next (c104): Số phát sóng sẽ trình bày hai phần: cơ chế tác dụng của glutathion trong từng tình huống, và cách bổ sung để có hiệu quả và có thực sự hiệu quả hay không.
- **Quotes cited:**
  - [▶ 01:06:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3978s) "ta quảng cáo rất nhiều về glutathion để"
  - [▶ 01:06:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3983s) "Chủ yếu là với tác dụng là chất chống"
  - [▶ 01:06:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3989s) "nhiều mu người mua cái sản phẩm này về"
  - [▶ 01:06:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3987s) "Giúp trắng da đúng không ạ?"

  Transcript 01:06:08–01:06:59 · [▶ watch from 01:06:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3968s)

  ```text
    [01:06:09] E, vitamin C, licopen vân vân. Nhưng mà
    [01:06:12] hôm nay chúng ta dành cho đầu tiên để
    [01:06:14] nói về cái cuộc chiến này đó chính là
    [01:06:17] glutathion.
    [01:06:19] Thì trong thời gian vừa qua trên các cái
    [01:06:21] phương tiện truyền thông đại chúng người
  ▶ [01:06:23] ta quảng cáo rất nhiều về glutathion để
    [01:06:26] bổ sung làm cái gì ạ?
  ▶ [01:06:28] >> Chủ yếu là với tác dụng là chất chống
    [01:06:30] oxy hóa giúp trắng da.
  ▶ [01:06:32] >> Giúp trắng da đúng không ạ? Và rất rất
  ▶ [01:06:34] nhiều mu người mua cái sản phẩm này về
    [01:06:36] nhất là các chị em phụ nữ muốn da trắng
    [01:06:38] da
    [01:06:39] >> thì các chị em mua về để bổ sung cái sản
    [01:06:41] phẩm này. Vậy thực sự nó là gì? Nó như
    [01:06:44] thế nào? Bổ sung có hiệu quả hay không?
    [01:06:46] Cơ chế của nó ra làm sao? thì chúng ta
    [01:06:49] sẽ đi vào hai phần chính của chủ đề phát
    [01:06:52] sóng ngày hôm nay đó chính là glutathion
    [01:06:55] với phần một đó là các cái cơ chế tác
    [01:06:58] dụng của glutathion trong từng cái tình
  ```

### c105

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:07:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4030s)  ·  section start [▶ 01:06:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3974s)  
**Summary section:** [01:06:19] Glutathion được quảng cáo để làm trắng da: nội dung số phát sóng  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Phúc

- **BEFORE (current summary):** Bác sĩ cũng nói nếu cơ thể cạn kiệt glutathion thì có thể sinh ra nhiều bệnh mãn tính, một số bệnh ung thư và lão hóa nhanh.
- **AFTER (proposed):** Bác sĩ cũng nói một khi đã cạn kiệt glutathion thì sẽ sinh ra một loạt bệnh, trong đó có vô cùng nhiều các bệnh mãn tính, có những bệnh ung thư, có những bệnh nguy hiểm, và đặc biệt lão hóa rất nhanh.
- **Why:** Softened hedge: 'sẽ sinh ra' became 'có thể sinh ra', and 'bệnh nguy hiểm' was dropped. The proposal restores his wording.
- **Pass-1 note:** Hedge added: doctor states categorically 'sẽ sinh ra'; summary softens to 'có thể'. Content otherwise matches (also 'bệnh nguy hiểm' omitted).
- **Pass-2 note (blind):** Softened: 'sẽ sinh ra' becomes 'có thể sinh ra'
- **Surrounding summary claims:**
  - previous (c104): Số phát sóng sẽ trình bày hai phần: cơ chế tác dụng của glutathion trong từng tình huống, và cách bổ sung để có hiệu quả và có thực sự hiệu quả hay không.
  - next (c106): Bác sĩ nói các số sau sẽ nói về vitamin E, vitamin C và licopen, tùy theo ý kiến của khán giả, và sẽ dùng kiến thức chuyên sâu để giải thích tác dụng của từng sản phẩm.
- **Quotes cited:**
  - [▶ 01:07:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4030s) "cạn kiệt glutathon thì chúng ta sẽ sinh"
  - [▶ 01:07:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4034s) "nhiều các bệnh mãn tính, có những bệnh"
  - [▶ 01:07:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4040s) "biệt chúng ta lão hóa rất nhanh."

  Transcript 01:07:00–01:07:50 · [▶ watch from 01:07:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4020s)

  ```text
    [01:07:01] huống cụ thể nó ra sao.
    [01:07:02] >> Vâng.
    [01:07:02] >> Thứ hai đó chính là chúng ta bổ sung như
    [01:07:05] thế nào để nó
    [01:07:06] >> có hiệu quả và nó có thực sự hiệu quả
    [01:07:08] hay không chúng ta phải rất hiểu nó.
    [01:07:10] Chúng ta làm thế nào để cơ thể không bị
    [01:07:12] cạn kiệt glutathion. Còn một khi đã bị
  ▶ [01:07:15] cạn kiệt glutathon thì chúng ta sẽ sinh
    [01:07:17] ra một loạt bệnh trong đó có vô cùng
  ▶ [01:07:19] nhiều các bệnh mãn tính, có những bệnh
    [01:07:22] ung thư, có những bệnh nguy hiểm và đặc
  ▶ [01:07:25] biệt chúng ta lão hóa rất nhanh.
    [01:07:26] >> Thì đấy chính là cái nội dung phát sóng
    [01:07:29] chính của chủ đề ngày hôm nay. Và cái
    [01:07:32] phần mở đầu này tôi cho rằng nó vô cùng
    [01:07:34] quan trọng ở chỗ đấy là chúng ta đã hiểu
    [01:07:37] được về gốc tự do. Và khi hiểu được gốc
    [01:07:40] tự do rồi thì lúc đó chúng ta mới hiểu
    [01:07:42] được toàn bộ những các cái thành phần
    [01:07:44] này tác động như thế nào. Và chúng ta sẽ
    [01:07:46] thấy rằng chúng tôi sẽ phát sóng từng số
    [01:07:49] một, từng vấn đề một. Nếu quý vị cảm
  ```

### c108

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:12:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4322s)  ·  section start [▶ 01:11:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4276s)  
**Summary section:** [01:11:21] Điều dưỡng kể về bố chồng tiểu đường dùng vi chất  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Viewer comment read by Khánh Lành; department head quoted

- **BEFORE (current summary):** Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào cho thấy vi chất làm giảm đường huyết.
- **AFTER (proposed):** Khi chia sẻ với chủ nhiệm khoa, người này nói không có cơ chế nào thể hiện "ma dê" (bản ghi âm ghi như vậy) giúp làm giảm đường huyết.
- **Why:** Entity changed: the comment read out names 'ma dê', not micronutrients in general. The doctor later says the case was not only about ma dê, but that is his reply, not the head of department's statement.
- **Pass-1 note:** Entity changed: head said no mechanism for magnesium ('ma dê') lowering glucose, not micronutrients in general; doctor later confirms it was about magnesium.
- **Pass-2 note (blind):** Entity changed: the head of department spoke about 'ma dê' (magnesium), not micronutrients ('vi chất') in general
- **Surrounding summary claims:**
  - previous (c107): Một điều dưỡng khoa phục hồi chức năng ở Hà Nội kể rằng bố chồng bị tiểu đường được bổ sung vi chất và đường huyết kiểm soát tốt, chỉ ở mức 5,5 đến 6,8.
  - next (c109): Trong đoạn này bác sĩ không trả lời về nội dung này.
- **Quotes cited:**
  - [▶ 01:12:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4322s) "chủ nhiệm khoa em nói rằng không có cơ"
  - [▶ 01:12:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4324s) "chế nào thể hiện ma dê giúp làm giảm"
  - [▶ 02:11:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7855s) "ma dê nó không hẳn chỉ ma dê."

  Transcript 01:11:52–01:12:34 · [▶ watch from 01:11:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4312s)

  ```text
    [01:11:52] nghe nữa. Em cũng đã bổ sung vi chất cho
    [01:11:55] bố chồng bị tiểu đường, kết quả là đường
    [01:11:57] huyết kiểm soát rất tốt, chỉ ở mức 5.5
    [01:12:01] đến 6.8. Em đã chia sẻ lại điều này cho
    [01:12:04] chỉ huy khoa và các bác sĩ khác. Nhưng
  ▶ [01:12:07] chủ nhiệm khoa em nói rằng không có cơ
  ▶ [01:12:09] chế nào thể hiện ma dê giúp làm giảm
    [01:12:12] đường huyết cả.
    [01:12:16] Vâng và tôi cũng muốn nhắc đến một bình
    [01:12:19] luận của một bác khán giả có tên là
    [01:12:21] Nguyễn Hiền. Chào bác sĩ Phúc, biên tập
    [01:12:23] viên Khánh Lành và đội ngũ ekip. Trước
    [01:12:26] hết tôi xin cảm ơn bác sĩ và toàn bộ
    [01:12:28] ekip rất nhiều. Tôi cũng sinh ra ở vùng
    [01:12:32] đồng quê Bắc Bộ và thuổ nhỏ cũng vất vả.
  ```

  Transcript 02:10:45–02:11:25 · [▶ watch from 02:10:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7845s)

  ```text
    [02:10:45] những cái rối loạn hết cơ quan nọ đến cơ
    [02:10:47] quan kia. Nếu gây rối loạn cơ quan nào
    [02:10:50] sẽ bị tổn thương cơ quan đó. Thế người
    [02:10:53] rối loạn ở tụy thì sẽ gây tiểu đường.
    [02:10:54] Như là chị Ngân nói rằng chồng chị là bị
    [02:10:58] tiểu đường bổ sung vi chất. Chị nói là
  ▶ [02:11:00] ma dê nó không hẳn chỉ ma dê.
    [02:11:02] >> Vâng.
    [02:11:02] >> Mà tất cả vi chất nó cùng tạo hiệp đồng
    [02:11:05] với nhau để giúp cho cộng hưởng lại.
    [02:11:08] >> Thế thì chồng chị bổ sung cái thì đường
    [02:11:09] huyết nó giảm xuống. Chị mang cái điều
    [02:11:11] đó đến trưởng khoa để thuyết phục thì
    [02:11:13] trưởng khoa sẽ không đồng ý. Thế thì bởi
    [02:11:16] vì sao? Tôi đã giải thích rồi rằng tất
    [02:11:18] cả những kiến thức về dinh dưỡng học nó
    [02:11:20] đòi hỏi là đến bây giờ để đưa ra thành
    [02:11:24] những các cái nghiên cứu để cái mà người
  ```

### c111

**Decisions:** D4, D8, D11 (correction approval)  
**Watch:** [▶ 01:13:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4423s)  ·  section start [▶ 01:12:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4336s)  
**Summary section:** [01:12:21] Người xem bị đau lưng, thoái hóa, theo dõi kênh từ năm 2024  
**Final class:** `unresolved` (pass 1 `mismatch`, pass 2 `unresolved`)  
**Speaker:** Viewer Nguyễn Hiền, read by Khánh Lành

- **BEFORE (current summary):** Họ nói đã hết đau cột sống, xương cổ, xương đùi và xương quai xanh, và không còn tê nửa người bên trái.
- **AFTER (proposed):** Họ nói không còn đau cột sống, "xương cổ đùi" (bản ghi âm ghi như vậy, không rõ là một vị trí hay hai vị trí) và xương quai xanh, và không còn tê dọc nửa người bên trái.
- **Why:** Stays unresolved. The unpunctuated 'xương cổ đùi' could be one site or two, and the transcript does not settle it. The proposal keeps the spoken words and states the doubt.
- **Pass-1 note:** 'xương cổ đùi' (femoral neck) split into separate 'xương cổ' and 'xương đùi' — adds a neck-bone site not stated; rest matches.
- **Pass-2 note (blind):** Transcript reads 'không còn bị đau cột sống, xương cổ đùi và xương quai xanh' [01:13:48]; with no punctuation, 'xương cổ đùi' could mean femoral neck (the doctor later mentions 'xương hông') or 'xương cổ, đùi'. Summary's split into 'xương cổ, xương đùi' cannot be confirmed or ruled out; 'tê nửa người bên trái' is supported
- **Reconciliation:** Both passes agree the unpunctuated “xương cổ đùi” is ambiguous; the transcript does not resolve femoral-neck vs separate sites. Final unresolved.
- **Surrounding summary claims:**
  - previous (c110): Một người xem kể từ năm 2024 theo dõi kênh và bổ sung đủ bảy loại vi chất.
  - next (c112): Đây là kết quả người xem tự kể.
- **Quotes cited:**
  - [▶ 01:13:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4423s) "Tôi nhận thấy mình không còn bị đau cột"
  - [▶ 01:13:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4425s) "sống, xương cổ đùi và xương quai xanh"
  - [▶ 01:13:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4433s) "xương. Tôi cũng không còn bị tê dọc nửa"

  Transcript 01:13:33–01:14:23 · [▶ watch from 01:13:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4413s)

  ```text
    [01:13:36] bài viết về chất gây ung thư của bác sĩ.
    [01:13:38] Từ đó tôi vào theo dõi kênh xem các bài
    [01:13:41] giảng và mua vi chất về bổ sung dần. Đến
    [01:13:44] nay tôi đã bổ sung đủ bảy loại vi chất.
  ▶ [01:13:48] Tôi nhận thấy mình không còn bị đau cột
  ▶ [01:13:50] sống, xương cổ đùi và xương quai xanh
    [01:13:53] nữa. Những nơi mà trước đây đau đến mức
    [01:13:56] tôi từng tưởng như là mình bị ung thư
  ▶ [01:13:58] xương. Tôi cũng không còn bị tê dọc nửa
    [01:14:01] người bên trái.
    [01:14:03] Gặp được kênh của bác sĩ, tôi giống như
    [01:14:06] được gặp phao cứu sinh. giúp cho cuộc
    [01:14:08] đời mình. Trước đây chưa từng có bác sĩ
    [01:14:11] nào nói cho tôi biết vi chất là gì. Tôi
    [01:14:15] như người mù đi trong đêm tối.
    [01:14:18] Số phát sóng nào của bác sĩ tôi cũng xem
    [01:14:20] và ghi chép đầy đủ. Mục nào cũng rất
    [01:14:23] hay. Có số tôi chép đến 16 trang giấy.
  ```

### c121

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 01:20:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4797s)  ·  section start [▶ 01:18:51](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4726s)  
**Summary section:** [01:18:51] Người 50 tuổi: đại tràng co thắt, táo bón, đầy đau đầu chu kỳ  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Viewer

- **BEFORE (current summary):** Họ cũng kể đau đầu và buồn nôn khi có chu kỳ đã hết sau nhiều tháng.
- **AFTER (proposed):** Họ cũng kể trước đây mỗi khi đến chu kỳ kinh nguyệt bị đau đầu khủng khiếp và buồn nôn; sau "năm tháng" bổ sung vi chất, họ nói đã hết đau đầu.
- **Why:** The viewer says only the headache ended, not the nausea. 'Năm tháng' became 'nhiều tháng', which changes the stated duration.
- **Pass-1 note:** Added/softened: viewer says headaches gone after 'năm tháng' (likely five months), summary says 'nhiều tháng'; nausea resolution not explicitly stated (only headache).
- **Pass-2 note (blind):** Borderline: the viewer explicitly says only the headache ended (nausea ending is implied); 'năm tháng' becomes 'nhiều tháng'
- **Reconciliation:** The source says headache ended after five months; it does not explicitly say nausea ended. “Many months” also changes the stated duration. Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c120): Sau khi bổ sung canxi, magie, omega 3 và các vi chất khác theo hướng dẫn, họ nói hết táo bón, hết đi ngoài phân sống.
  - next (c122): Đây là kết quả người xem tự kể.
- **Quotes cited:**
  - [▶ 01:20:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4797s) "chu kỳ kinh nguyệt là tôi bị đau đầu"
  - [▶ 01:20:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4822s) "năm tháng bổ sung vi chất, giờ tôi đã"
  - [▶ 01:20:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4824s) "hết đau đầu, hết viêm da dị ứng và hết"
  - [▶ 01:20:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4799s) "khủng khiếp và buồn nôn nữa"

  Transcript 01:19:47–01:20:54 · [▶ watch from 01:19:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4787s)

  ```text
    [01:19:47] canxi, ma, omega 3 và các loại vi chất
    [01:19:50] theo hướng dẫn. Tình trạng bệnh cải
    [01:19:52] thiện rõ dệt, hết táo bón, hết phân sống
    [01:19:55] và chấm dứt luôn cái nỗi ám ảnh mỗi lần
    [01:19:58] đi vệ sinh.
    [01:20:00] Không những thế, trước đây mỗi khi đến
  ▶ [01:20:02] chu kỳ kinh nguyệt là tôi bị đau đầu
  ▶ [01:20:04] khủng khiếp và buồn nôn nữa. Cứ đến ngày
    [01:20:07] đó là tôi phải nghỉ làm. Nằm bẹp dí
    [01:20:10] trong phòng kín, sợ ánh sáng, sợ âm
    [01:20:12] thanh. Tiếng ồn kéo dài từ hai đến ba
    [01:20:15] ngày. Mỗi lần đau tôi chỉ biết uống
    [01:20:17] thuốc giảm đau dù biết là không tốt. Đau
    [01:20:20] đến mức chỉ mong nhanh chóng đến tuổi
    [01:20:23] mãn kinh cho đỡ đớn đau. Kỳ lạ thay, sau
  ▶ [01:20:27] năm tháng bổ sung vi chất, giờ tôi đã
  ▶ [01:20:29] hết đau đầu, hết viêm da dị ứng và hết
    [01:20:32] cả ghen mắt lèm nghèm mỗi sáng. Giờ tôi
    [01:20:35] chỉ mong khỏi nốt bệnh viêm xoang và hen
    [01:20:38] phế quản nữa là không còn gì hạnh phúc
    [01:20:40] bằng.
    [01:20:42] Con trai tôi thấy vậy bảo ngày nào mẹ
    [01:20:45] cũng xem ông vi chất thì mẹ nhớ uống
    [01:20:48] đúng như bác hướng dẫn nhé.
    [01:20:51] Con mong mẹ nghe theo bác để khỏe hơn
    [01:20:53] mỗi ngày. Cháu gọi bác sĩ Phúc bằng cái
  ```

### c125

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s)  ·  section start [▶ 01:21:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4892s)  
**Summary section:** [01:21:37] Người xem bị da vàng, hemoglobin thấp, nghi thiếu sắt nhược sắc  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Viewer

- **BEFORE (current summary):** Họ nghi ngờ thiếu sắt nhược sắc, nhưng chưa rõ chính xác.
- **AFTER (proposed):** Họ cho rằng có lẽ vấn đề nằm ở việc thiếu sắt nhược sắc; riêng thông tin đọc được về xác hồng cầu bị phá hủy làm da có ánh vàng thì họ nói không rõ độ chính xác.
- **Why:** The doubt is misplaced: 'không rõ độ chính xác' refers to the hemolysis information the viewer read, not to the iron-deficiency suspicion, whose hedge is 'có lẽ'.
- **Pass-1 note:** Uncertainty misattached: viewer hedges 'có lẽ' on iron-deficiency suspicion; 'không rõ độ chính xác' refers to the read claim that hemolysed RBCs make skin yellow, not to the diagnosis.
- **Pass-2 note (blind):** 'có lẽ' hedge is kept as 'nghi ngờ ... chưa rõ'; the viewer's separate 'không rõ độ chính xác' applies to the hemolysis info, so the wording is borderline
- **Reconciliation:** “Không rõ độ chính xác” refers to the reported hemolysis information, not the viewer’s iron-deficiency suspicion. Retain attribution/qualification issue.
- **Surrounding summary claims:**
  - previous (c124): Hemoglobin luôn ở mức 10 đến 11 g/dL, thấp hơn khoảng tham chiếu 12 đến 16.
  - next (c126): Trong đoạn này bác sĩ chưa đưa ra kết luận nào.
- **Quotes cited:**
  - [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s) "nhận ra có lẽ vấn đề nằm ở việc bị thiếu"
  - [▶ 01:23:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4999s) "vàng. Nhưng em không rõ độ chính xác của"
  - [▶ 01:23:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4989s) "Em có xem một số tài liệu nói rằng khi thiếu sắt hồng cầu mỏng manh dễ bị phá hủy hàng loạt"

  Transcript 01:22:43–01:23:49 · [▶ watch from 01:22:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4963s)

  ```text
    [01:22:45] đến 11 g/dl.
    [01:22:48] So với khoảng tam chiếu là từ 12 đến 16.
    [01:22:51] nhưng không có bác sĩ nào đề cập hay là
    [01:22:53] lưu ý cả. Chỉ sau này khi theo dõi kênh
    [01:22:56] của bác sĩ Phúc và lụp lại hồ sơ, em mới
  ▶ [01:22:58] nhận ra có lẽ vấn đề nằm ở việc bị thiếu
    [01:23:02] sắt nhược sắc.
    [01:23:04] Do chế độ ăn của em đã quen kiểm soát
    [01:23:06] lượng ăn nên khi muốn cố ăn tăng số
    [01:23:10] lượng để thêm dinh dưỡng thì em ăn không
    [01:23:13] nổi.
  ▶ [01:23:14] Em có xem một số tài liệu nói rằng khi
  ▶ [01:23:16] thiếu sắt hồng cầu mỏng manh dễ bị phá
  ▶ [01:23:19] hủy hàng loạt và xác hồng cầu bị phá hủy
    [01:23:21] tồn tại trên bề mặt da làm da có ánh
  ▶ [01:23:24] vàng. Nhưng em không rõ độ chính xác của
    [01:23:27] thông tin này như thế nào. Em đã đi khám
    [01:23:30] khoảng năm bệnh viện phòng khám. và bác
    [01:23:33] sĩ bệnh viện tư. Em
    [01:23:37] nhận được câu trả lời luôn là họ thừa
    [01:23:40] nhận nhìn da của em vàng thật nhưng giải
    [01:23:43] thích đó là do cơ địa, do nguồn nước. Dù
    [01:23:47] em đã chuyển chỗ ở vài lần, nguồn nước
    [01:23:49] đã thay đổi nhưng vẫn không cải thiện.
  ```

### c127

**Decisions:** D7, D11 (correction approval)  
**Watch:** [▶ 01:24:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5046s)  ·  section start [▶ 01:24:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5044s)  
**Summary section:** [01:24:09] Phác đồ người xem đang dùng: sắt, vitamin B9, nhịn ăn gián đoạn 168  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Viewer letter read by MC; summary attributes to viewer (correct)

- **BEFORE (current summary):** Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ sắt II fumarat khô cùng 250 mcg vitamin B9, cùng bộ vi chất của bác sĩ.
- **AFTER (proposed):** Từ ngày 22/04/2026, người xem dùng mỗi ngày một viên chứa 50 mg sắt nguyên tố từ "sắt hai xun phát khô" (bản ghi âm ghi như vậy) cùng 250 mcg vitamin B9, cùng bộ vi chất của bác sĩ.
- **Why:** Iron salt changed: the transcript says 'xun phát', the summary says 'fumarat'. Date and both amounts match.
- **Pass-1 note:** Transcript says iron (II) 'xun phát' (sulfate) khô, not fumarat; salt entity changed. Date, 50 mg, 250 mcg B9 match.
- **Pass-2 note (blind):** Iron salt changed: transcript 'sắt hai xun phát khô' (sulfate), summary says 'sắt II fumarat'
- **Surrounding summary claims:**
  - previous (c126): Trong đoạn này bác sĩ chưa đưa ra kết luận nào.
  - next (c128): Từ ngày 27/05/2026, họ nhịn ăn gián đoạn 168 từ 20 giờ tối đến 12 giờ trưa hôm sau.
- **Quotes cited:**
  - [▶ 01:24:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5046s) "2026. Từ ngày 22 tháng 04 năm 2026, em"
  - [▶ 01:24:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5059s) "sắt chứa 50 mg sắt nguyên tố từ sắt hai xun phát khô cộng với 250 micrg vitamin"

  Transcript 01:23:56–01:24:49 · [▶ watch from 01:23:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5036s)

  ```text
    [01:23:57] Điều này từng khiến em tự cắt bỏ gần như
    [01:24:00] 100% thực phẩm có màu vàng, màu cam và
    [01:24:02] màu đỏ. Nghĩ lại em vẫn rất tiếc cái
    [01:24:05] nguồn beta cararoten đã bỏ lỡ.
    [01:24:09] Thứ hai là quá trình điều chỉnh từ năm
  ▶ [01:24:11] 2026. Từ ngày 22 tháng 04 năm 2026, em
    [01:24:17] đã bắt đầu dùng bộ vi chất bác sĩ phổ
    [01:24:19] biến chung kết hợp xem các số phát sóng
    [01:24:22] về sắt. Mỗi ngày em bổ sung một phiên
  ▶ [01:24:24] sắt chứa 50 mg sắt nguyên tố từ sắt hai
  ▶ [01:24:29] xun phát khô cộng với 250 micrg vitamin
    [01:24:33] B9.
    [01:24:35] Từ ngày 27 tháng năm 2026, em thực hiện
    [01:24:39] nhịn ăn gián đoạn 168 từ 2000 tối đến
    [01:24:44] 12:00 trưa hôm sau. Trong quá trình sử
    [01:24:46] dụng từ bộ vi chất cơ bản ban đầu, em
  ```

### c135

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 01:27:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5239s)  ·  section start [▶ 01:26:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5213s)  
**Summary section:** [01:26:58] Người 41 tuổi ở Đông Anh: đau nửa đầu, trầm cảm sau sinh, gan nhiễm mỡ  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Diagnosis by unnamed hospital doctors as reported in viewer's letter; summary says 'Bác sĩ chẩn đoán' without reported-speech framing, readable as Dr. Phúc

- **BEFORE (current summary):** Bác sĩ chẩn đoán nang dưới nhện góc tiểu cầu não trái làm dây thần kinh số năm bị chèn ép.
- **AFTER (proposed):** Người xem kể đã chữa trị ở nhiều bệnh viện lớn tại Hà Nội, và bác sĩ ở đó (không phải bác sĩ Phúc) chẩn đoán họ bị nang dưới nhện góc tiểu cầu não trái, dây thần kinh số năm bị chèn ép dẫn đến đau nửa đầu.
- **Why:** As written, 'Bác sĩ chẩn đoán' reads as Dr. Phúc. The viewer is reporting a diagnosis from Hanoi hospitals, and Dr. Phúc later plays down the cyst.
- **Pass-1 note:** Speaker/framing: diagnosis belongs to Hanoi hospital doctors per the viewer, not Dr. Phúc; Dr. Phúc later (~02:16:55–02:23:50) downplays the cyst's significance.
- **Pass-2 note (blind):** Content matches. Risk: 'Bác sĩ' means the viewer's hospital doctors, not Dr. Phúc, who later downplays the cyst
- **Reconciliation:** The viewer reports a diagnosis by Hanoi hospital doctors; wording “Bác sĩ chẩn đoán” can wrongly suggest Dr. Phúc. Retain attribution issue.
- **Surrounding summary claims:**
  - previous (c134): Người xem 41 tuổi ở Đông Anh, Hà Nội, kể bị đau nửa đầu từ 15 tuổi, với khoảng bảy cơn mỗi tháng.
  - next (c136): Sau khi sinh, họ được chẩn đoán trầm cảm sau sinh.
- **Quotes cited:**
  - [▶ 01:27:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5239s) "chữa trị ở nhiều bệnh viện lớn tại Hà Nội."
  - [▶ 01:27:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5241s) "Bác sĩ chẩn đoán tôi bị nang dưới nhện góc tiểu cầu não trái. Dây thần kinh số năm bị chèn ép dẫn đến đau nửa đầu."
  - [▶ 02:18:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8286s) "con nang dưới nhện và người ta đang chung sống hòa bình. Nếu chúng ta mà mổ dẫn lưu như vậy thì vô tình bệnh nhân lại thêm một cái vết mổ chứ không cần thiết."

  Transcript 01:27:09–01:27:51 · [▶ watch from 01:27:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5229s)

  ```text
    [01:27:10] với quê hương của bác sĩ. Tôi mới biết
    [01:27:13] đến kênh được 10 tháng.
    [01:27:16] Trước đó là chuỗi ngày tăm tối nhất khi
    [01:27:17] sức khỏe của tôi suy sụp hoàn toàn. Tôi
    [01:27:20] mắc trứng đau nửa đầu từ năm 15 tuổi, đã
  ▶ [01:27:24] chữa trị ở nhiều bệnh viện lớn tại Hà
  ▶ [01:27:26] Nội. Bác sĩ chẩn đoán tôi bị nang dưới
  ▶ [01:27:29] nhện góc tiểu cầu não trái. Dây thần
  ▶ [01:27:32] kinh số năm bị chèn ép dẫn đến đau nửa
  ▶ [01:27:35] đầu. Bình quân mỗi tháng tôi bị bảy cơn
    [01:27:37] đau, đặc biệt là vào đầu và cuối chu kỳ
    [01:27:41] kinh nguyệt.
    [01:27:43] Ngoài ra, mỗi năm tôi bị khoảng ba đợt
    [01:27:45] đau kéo dài cả tháng với triệu chứng mệt
    [01:27:48] mỏi, chóng mặt, chân tay tự co gồng cho
  ```

  Transcript 02:17:56–02:18:36 · [▶ watch from 02:17:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8276s)

  ```text
    [02:17:56] anh bác sĩ phẫu thuật thần kinh phó khoa
    [02:17:58] một khoa phẫu thuật kinh lớn có đặt vấn
    [02:18:00] đề với tôi rằng có nên mổ phẫu thuật
    [02:18:03] những các cái khoang dưới nhện mà có
    [02:18:04] nang như thế này hay không?
    [02:18:06] Tôi nói rằng tôi đọc rất rất nhiều những
    [02:18:09] các cái phim CT và phim cộng hường từ
  ▶ [02:18:11] con nang dưới nhện và người ta đang
  ▶ [02:18:13] chung sống hòa bình. Nếu chúng ta mà mổ
  ▶ [02:18:16] dẫn lưu như vậy thì vô tình bệnh nhân
  ▶ [02:18:18] lại thêm một cái vết mổ chứ không cần
  ▶ [02:18:20] thiết. Thì tôi có lập luận là như vậy.
    [02:18:22] Và tôi cho rằng cái này nó do những cái
    [02:18:25] đau đầu hay là những cái triệu chứng gì
    [02:18:26] đó chúng ta hãy đi tìm theo cái hướng
    [02:18:28] khác và dường như có những cái ẩn chứa
    [02:18:30] phía sau. Thì đến bây giờ tôi thấy rằng
    [02:18:33] như của chị Nhung chị nói rằng là tổn
  ```

### c140

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:29:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5352s)  ·  section start [▶ 01:29:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5357s)  
**Summary section:** [01:29:22] Lạm dụng đường mía thô: nhịp tim 170 lần/phút và các triệu chứng  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Viewer letter read by MC; summary: viewer

- **BEFORE (current summary):** Người xem kể sau khi mệt là uống đường mía thô, và dùng lâu dài thì có khó thở, nhịp tim tăng 170 nhịp mỗi phút, tăng cân, bụng to và gan bắt đầu nhiễm mỡ.
- **AFTER (proposed):** Người xem kể lúc mệt mỏi đã ăn hoặc uống đường mía thô, rồi lạm dụng; sau 3 tháng dùng lượng đường quá nhiều thì bị khó thở, nhịp tim tăng lên 170 nhịp một phút, tăng cân, bụng to và gan bắt đầu nhiễm mỡ.
- **Why:** 'Sau 3 tháng' and the excess amount became 'dùng lâu dài', and 'ăn hoặc uống' was narrowed to 'uống'.
- **Pass-1 note:** Qualifier changed: specific 'sau 3 tháng' (excessive amount) generalized to 'dùng lâu dài'; 'ăn hoặc uống' narrowed to 'uống'. Symptoms (170 bpm, weight gain, big belly, fatty liver at 01:29:42) match.
- **Pass-2 note (blind):** Specific duration 'Sau 3 tháng' replaced by vague 'dùng lâu dài'; 'ăn hoặc là uống' narrowed to 'uống'
- **Surrounding summary claims:**
  - previous (c139): Đây là kết quả người xem tự kể.
  - next (c141): Họ cũng kể gần hai năm không có giấc ngủ trọn vẹn, hay bị bóng đè và nhịp tim hẫng.
- **Quotes cited:**
  - [▶ 01:29:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5352s) "Trong lúc mệt mỏi, tôi ăn hoặc là uống đường mía thô"
  - [▶ 01:29:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5364s) "Sau 3 tháng sử dụng lượng đường quá nhiều"
  - [▶ 01:29:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5369s) "Tôi bị khó thở, nhịp tim tăng lên 170 nhịp một phút"
  - [▶ 01:29:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5357s) "Từ đó tôi lạm dụng."

  Transcript 01:29:02–01:29:59 · [▶ watch from 01:29:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5342s)

  ```text
    [01:29:03] nhưng kết luận chung vẫn chỉ là trầm cảm
    [01:29:05] sau sinh. Vì đang cho con bú nên tôi
    [01:29:09] không dùng thuốc bệnh và được giáo sư
    [01:29:11] chỉ định điều trị từ trường não rất tốn
    [01:29:13] kém mà người vẫn mệt mỏi, không khá hơn.
  ▶ [01:29:17] Tôi rơi vào tuyệt vọng. Trong lúc mệt
  ▶ [01:29:19] mỏi, tôi ăn hoặc là uống đường mía thô
  ▶ [01:29:22] thì thấy rằng cơ thể dễ chịu hơn. Từ đó
  ▶ [01:29:26] tôi lạm dụng. Cứ mệt là tôi uống đường.
  ▶ [01:29:29] Sau 3 tháng sử dụng lượng đường quá
  ▶ [01:29:31] nhiều, cơ thể tôi gióng lên hồi chuông
  ▶ [01:29:34] thê thảm nhất. Tôi bị khó thở, nhịp tim
  ▶ [01:29:37] tăng lên 170 nhịp một phút, mệt mỏi,
    [01:29:40] chân tay tê dại, tăng cân không phanh,
    [01:29:42] bụng to, gan bắt đầu nhiễm mỡ. Tôi ra
    [01:29:45] vào phòng cấp cứu liên tục nhưng bác sĩ
    [01:29:48] vẫn chỉ kết luận là do trầm cảm. Tôi nói
    [01:29:51] không ra hơi, nói hai câu lại phải ngồi
    [01:29:54] thở. không leo được cầu thang, không
    [01:29:56] chịu được tiếng ồn và rất sợ chỗ đông
    [01:29:58] người.
  ```

### c144

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:31:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5479s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Viewer letter read by MC; summary: viewer

- **BEFORE (current summary):** Họ kể vẫn còn nhịp tim nhanh và thỉnh thoảng bị bóng đè khi ngủ.
- **AFTER (proposed):** Họ kể nhịp tim đôi lúc bị nhanh và khi ngủ thỉnh thoảng vẫn bị bóng đè.
- **Why:** Hedge dropped: heart rate is fast 'đôi lúc' (at times), while 'vẫn còn nhịp tim nhanh' reads as constant.
- **Pass-1 note:** Hedge dropped: heart rate is 'đôi lúc' fast; summary 'vẫn còn nhịp tim nhanh' reads as persistent.
- **Pass-2 note (blind):** Borderline: dropped the 'đôi lúc' frequency hedge on fast heart rate ('vẫn còn nhịp tim nhanh')
- **Surrounding summary claims:**
  - previous (c143): Người xem đề nghị bác sĩ giải thích chi tiết về bóng đè khi ngủ và cơ chế ảnh hưởng của việc lạm dụng đường mía thô lên nhịp tim.
  - next (c145): Bài hôm nay không đủ thời gian để giải thích sâu, nhưng cơ chế cơ bản theo bác sĩ là: thức đi kèm với hoạt động, ngủ đi kèm với ngừng hoạt động.
- **Quotes cited:**
  - [▶ 01:31:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5479s) "Nhịp tim đôi lúc bị nhanh và khi ngủ thỉnh thoảng vẫn bị hiện tượng bóng đè."

  Transcript 01:31:09–01:31:49 · [▶ watch from 01:31:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5469s)

  ```text
    [01:31:09] mỡ, mọi chỉ số đều ổn định. Giờ đây tôi
    [01:31:13] đã lấy lại được 95% sức khỏe. Bệnh đau
    [01:31:16] nửa đầu gần như hết hẳn, ngủ ngon và sâu
    [01:31:19] giấc, luôn vui vẻ yêu đời. Tuy nhiên,
    [01:31:22] thi thoảng tôi vẫn chưa điều chỉnh được
  ▶ [01:31:24] cảm xúc. Nhịp tim đôi lúc bị nhanh và
  ▶ [01:31:27] khi ngủ thỉnh thoảng vẫn bị hiện tượng
  ▶ [01:31:30] bóng đè.
    [01:31:32] Tôi rất mong trong chương trình này bác
    [01:31:34] sĩ có thể giải thích chi tiết về hiện
    [01:31:37] tượng bóng đè khi ngủ và cơ chế ảnh
    [01:31:40] hưởng của việc lạm dụng đường mía thô
    [01:31:42] lên nhịp tim để người dân biết cách
    [01:31:44] phòng tránh. Xin chân thành cảm ơn bác
    [01:31:46] sĩ Phúc Biên tập viên Khánh Lành và toàn
    [01:31:48] thể ekip. Vâng, cảm ơn bác và tôi cũng
  ```

### c156

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:31:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9066s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** BS Trần Văn Phúc; matches

- **BEFORE (current summary):** Bản ghi âm ghi là "K G3" và "glycerin" cho cùng cơ chế này; cơ chế liệt vận động không được kịp nhả.
- **AFTER (proposed):** Bản ghi âm ghi là "K G3" và "glycerin" cho cơ chế này; khi chuyển vào giấc ngủ mà việc làm liệt vận động không làm được kịp thời ("cái phanh này không được kịp thời"), người ngủ sẽ nói và vận động trong mơ.
- **Why:** Wrong scenario: going into sleep, the brake is not applied in time. 'Không kịp nhả' (not released) belongs to the separate sleep-to-wake case, which c157 already covers.
- **Pass-1 note:** 'K G3'/'glycerin' wording correct, but transcript says the brake is not APPLIED in time when going thức→ngủ (REM) causing talking/moving in dreams; summary says 'không được kịp nhả' (not released), which is the opposite scenario.
- **Pass-2 note (blind):** 'K G3'/'glycerin' wording is correct, but in this falling-asleep scenario the paralysis/brake fails to engage in time; summary says it 'không được kịp nhả' (fails to release), which is the separate waking scenario
- **Surrounding summary claims:**
  - previous (c155): Hai chất này làm liệt cơ, khiến người ngủ không cử động, không vận động và không nói lung tung.
  - next (c157): Nếu chuyển từ ngủ sang thức mà phanh chưa nhả, não đã tỉnh và nhận biết được mọi thứ nhưng tay chân và lời nói không cử động được.
- **Quotes cited:**
  - [▶ 02:31:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9066s) "G3 và tiết ra glycerin này nó lại không"
  - [▶ 02:31:16](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9071s) "Tức là cái phanh này không được kịp"
  - [▶ 02:32:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9138s) "lại không có phanh."
  - [▶ 02:31:31](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9086s) "Nói trong mơ và vận động trong mơ."

  Transcript 02:30:56–02:31:56 · [▶ watch from 02:30:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9056s)

  ```text
    [02:30:56] >> Thế bây giờ khi mà chúng ta chuyển vào
    [02:30:58] giấc ngủ mà mới bắt đầu vào giấc ngủ thì
    [02:31:01] đang là ngủ gì ạ? Ngủ remâng
    [02:31:03] >> mà ngủ rem thì mơ rất nhiều.
    [02:31:06] >> Mơ thấy nói, mơ thấy hành động. Nhưng mà
    [02:31:08] cái làm liệt vận động tức là tiết ra K
  ▶ [02:31:11] G3 và tiết ra glycerin này nó lại không
    [02:31:14] làm được kịp thời.
    [02:31:15] >> Vâng.
  ▶ [02:31:16] >> Tức là cái phanh này không được kịp
    [02:31:17] thời. Khánh Lành có hình dung ra không
    [02:31:20] ạ? Tức là nó chưa kịp làm thì dẫn tới là
    [02:31:22] gì? Dẫn tới là chúng ta sẽ bị gì ạ?
    [02:31:26] Chúng ta sẽ bị vận động.
    [02:31:27] >> Vâng.
    [02:31:28] >> Chúng ta sẽ bị gì ạ? Chúng ta sẽ bị nói
    [02:31:30] lung tung.
    [02:31:31] >> Nói trong mơ. Vâng.
  ▶ [02:31:31] >> Nói trong mơ và vận động trong mơ.
    [02:31:34] >> Vâng.
    [02:31:34] >> Và khi nói trong mơ, vận động trong mơ
    [02:31:36] thấy những các cái hoạt động như thế quá
    [02:31:38] đà. Và lúc đó chúng ta khi bừng tỉnh một
    [02:31:41] cái thôi chúng ta sẽ rơi vào trạng thái
    [02:31:43] rất sợ hãi. Đó chính là các cái hạch
    [02:31:45] hạnh nhân ở trong não nó bị kích hoạt.
    [02:31:48] >> Ngay lập tức mà xảy ra cái hiện tượng
    [02:31:49] này thì hạch hạnh nhân ở trong não nó
    [02:31:52] kích hoạt để nó thấy rằng đang rơi vào
    [02:31:54] tình trạng nguy hiểm nó báo động.
    [02:31:55] >> Vâng.
    [02:31:55] >> Nó báo động thì cách báo động tốt nhất
  ```

  Transcript 02:32:08–02:32:48 · [▶ watch from 02:32:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9128s)

  ```text
    [02:32:09] đang mơ thấy rằng là đang nói những cái
    [02:32:10] câu đang hét lên hay gì đấy chẳng hạn,
    [02:32:12] tự dưng chúng ta tỉnh đột ngột một cái
    [02:32:14] và chúng ta toát mồ hôi ra chúng ta sợ.
    [02:32:16] >> Vâng.
    [02:32:16] >> Và tim đập nhanh. Đó là gì? Đó là chúng
    [02:32:20] ta đang từ thức chuyển sang ngủ nhưng
  ▶ [02:32:23] lại không có phanh.
    [02:32:24] >> Ừ.
    [02:32:25] >> Được chưa ạ?
    [02:32:25] >> Vâng.
    [02:32:26] >> Hoặc là một cái trạng thái thứ hai là
    [02:32:28] chiều ngược lại. Trạng thái thứ hai là
    [02:32:30] chiều ngược lại đang từ ngủ sang thức.
    [02:32:33] Thì đây là cái trạng thái thứ hai. Thì
    [02:32:35] lúc đó không được phép liệt nữa mà chúng
    [02:32:37] ta phải nhả phanh ra. Vâng.
    [02:32:39] >> Tức là chúng ta đang dừng xe thì chúng
    [02:32:40] ta đang lái xe đi thì phải nhả phanh ra.
    [02:32:42] >> Vâng.
    [02:32:43] >> Để cho xe nó đi.
    [02:32:44] >> Thế nhưng mà bây giờ chúng ta ngủ nhưng
    [02:32:46] chuyển sang thức thì lúc đấy lại vẫn
    [02:32:48] liệt vận động. Vậy lúc đấy chúng ta nhận
  ```

### c161

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:34:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9264s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** BS Trần Văn Phúc relaying common/literature advice; summary presents it as straightforward advice

- **BEFORE (current summary):** Khi xảy ra, hít một hơi thật sâu rồi thở ra từ khoảng 15 đến 30 giây, sau đó lấy lại bình tĩnh thì sẽ thoát khỏi tình trạng này.
- **AFTER (proposed):** Bác sĩ nói hầu hết tài liệu khoa học khuyên khi xảy ra thì hít một hơi thật sâu, rồi thở ra từ 15 đến 30 giây ("đại ý"), sau đó lấy lại bình tĩnh thì thoát; nhưng ông nói "cứ khuyên nhau thế thôi nhưng mà ai cũng sợ", và sau đó nhận xét nói thế thì rất đơn giản.
- **Why:** The summary states this as plain advice. The doctor reports it as what the literature says, doubts it, and later calls it too simple.
- **Pass-1 note:** Dropped framing: transcript presents breathing tip as what literature/people advise ('đại ý', 'cứ khuyên nhau thế thôi'), and doctor later calls it too simplistic, insisting on root-cause fixes (02:43:30-02:43:40).
- **Pass-2 note (blind):** Dropped the attribution to 'các tài liệu khoa học' and the doctor's skepticism
- **Surrounding summary claims:**
  - previous (c160): Bác sĩ nói hầu hết tài liệu khoa học cho rằng đây là hiện tượng không đáng ngại.
  - next (c162): Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, tác dụng chủ yếu là trấn an tâm lý, không phải hiệu quả thực sự.
- **Quotes cited:**
  - [▶ 02:34:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9264s) "bóng đè này hít một hơi thật sâu quãng"
  - [▶ 02:34:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9267s) "sau đó thì bắt đầu thở ra từ 15 đến 30"
  - [▶ 02:34:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9277s) "khuyên nhau thế thôi nhưng mà ai cũng sợ"
  - [▶ 02:34:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9253s) "hầu hết tất cả các tài liệu khoa học đều nói rằng đây là hiện tượng không có gì đáng ngại cả."
  - [▶ 02:43:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9803s) "hướng dẫn nhau hít một hơi thở thật sâu rồi chúng ta bình tĩnh lại. Nói thế thì nó rất là đơn giản"

  Transcript 02:34:03–02:35:07 · [▶ watch from 02:34:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9243s)

  ```text
    [02:34:05] thì cái sự kết hợp này nó không nhịp
    [02:34:07] nhàng. Nó không nhịp nhàng thì sẽ dẫn
    [02:34:09] tới hiện tượng bóng đè. Vậy bản thân cái
    [02:34:11] này nó có đáng sợ lắm không ạ? Nó cũng
    [02:34:14] không phải là đáng sợ. Nhưng tại sao nó
    [02:34:16] lại xảy ra hiện tượng bóng đè này? Thì
  ▶ [02:34:18] hầu hết tất cả các tài liệu khoa học đều
  ▶ [02:34:22] nói rằng đây là hiện tượng không có gì
  ▶ [02:34:24] đáng ngại cả. Chúng ta chỉ cần gì thôi?
    [02:34:26] Chúng ta chỉ cần khi xảy ra hiện tượng
  ▶ [02:34:29] bóng đè này hít một hơi thật sâu quãng
  ▶ [02:34:32] sau đó thì bắt đầu thở ra từ 15 đến 30
    [02:34:35] giây đại ý. Thế thì sau đó thì bắt đầu
    [02:34:38] là chúng ta lấy lại bình tĩnh thì chúng
    [02:34:40] ta sẽ thoát khỏi cái chuyện đấy là cứ
  ▶ [02:34:42] khuyên nhau thế thôi nhưng mà ai cũng sợ
    [02:34:44] có đúng không ạ? đấy là khuyên rằng nó
    [02:34:46] không có vấn đề gì hết cả. Thế rồi một
    [02:34:49] số người đi ngủ sẽ đặt con dao ở dưới
    [02:34:51] giường, nghĩ rằng đấy là do ma làm, đặt
    [02:34:53] con dao dưới giường, thế rồi tỏi, thế
    [02:34:55] rồi hành, thế rồi thì gì đủ thứ làm các
    [02:34:58] cái việc đó thì chúng ta làm cái đấy đấy
    [02:35:01] là liệu pháp giả dược.
    [02:35:03] >> Vâng.
    [02:35:03] >> Tức là về mặt tinh thần để chúng ta trấn
    [02:35:05] an tâm lý. Vâng.
    [02:35:06] >> Chứ còn nó hiệu quả thực sự thì nó không
  ```

  Transcript 02:43:13–02:43:53 · [▶ watch from 02:43:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9793s)

  ```text
    [02:43:14] phanh này nó không nhịp nhàng giữa người
    [02:43:16] lái xe và bánh xe. Từ đấy chúng ta sẽ
    [02:43:20] rơi vào cái trạng thái bóng đè. Tôi cho
    [02:43:22] rằng đây là một vấn đề quan trọng.
    [02:43:24] >> Vâng.
    [02:43:24] >> Chứ không phải rằng là trên các tài liệu
    [02:43:26] nói rằng đây là vấn đề không có gì quá
  ▶ [02:43:28] quan trọng và hướng dẫn nhau hít một hơi
  ▶ [02:43:30] thở thật sâu rồi chúng ta bình tĩnh lại.
  ▶ [02:43:33] Nói thế thì nó rất là đơn giản đúng
    [02:43:34] không ạ? Vâng,
    [02:43:35] >> chúng ta phải giải quyết triệt để cái
    [02:43:37] câu chuyện này bằng cách là nâng cao thể
    [02:43:40] trạng, nâng cao cuộc sống lên. Thì đó là
    [02:43:43] câu chuyện của chị Nhung mà bây giờ sau
    [02:43:46] khi mà chị bổ sung thì chị sẽ thấy rằng
    [02:43:49] là thỉnh thoảng chỉ còn cái tình trạng
    [02:43:50] là nhịp tim chưa kiểm soát được hết về
    [02:43:53] tâm lý dẫn tới thỉnh thoảng có nhịp tim
  ```

### c162

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:34:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9284s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** BS Trần Văn Phúc; matches

- **BEFORE (current summary):** Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, tác dụng chủ yếu là trấn an tâm lý, không phải hiệu quả thực sự.
- **AFTER (proposed):** Còn đặt dao, tỏi, hành dưới giường, bác sĩ gọi đây là liệu pháp giả dược, về mặt tinh thần để trấn an tâm lý; ông nói "chứ còn nó hiệu quả thực sự thì nó không hẳn chủ yếu là trấn an tâm lý" (bản ghi âm ghi như vậy) rồi đi sâu hơn vào nguyên nhân.
- **Why:** Hedge hardened: 'không hẳn' became a flat 'không phải hiệu quả thực sự'. The spoken sentence is itself unclear, so the proposal quotes it instead of interpreting it.
- **Pass-1 note:** Hedge hardened: transcript 'hiệu quả thực sự thì nó không hẳn chủ yếu là trấn an tâm lý' (not entirely); summary states flatly 'không phải hiệu quả thực sự'.
- **Pass-2 note (blind):** Borderline: placebo/reassurance matches, but doctor's hedge 'không hẳn' is hardened to 'không phải hiệu quả thực sự'
- **Surrounding summary claims:**
  - previous (c161): Khi xảy ra, hít một hơi thật sâu rồi thở ra từ khoảng 15 đến 30 giây, sau đó lấy lại bình tĩnh thì sẽ thoát khỏi tình trạng này.
  - next (c163): Bác sĩ nói não chiếm khoảng 2% trọng lượng cơ thể nhưng dùng khoảng 20% năng lượng; ti thể tạo năng lượng (ATP) đồng thời sinh gốc tự do với số lượng rất lớn.
- **Quotes cited:**
  - [▶ 02:34:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9284s) "số người đi ngủ sẽ đặt con dao ở dưới"
  - [▶ 02:35:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9296s) "là liệu pháp giả dược."
  - [▶ 02:35:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9304s) "hẳn chủ yếu là trấn an tâm lý."
  - [▶ 02:35:06](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9301s) "Chứ còn nó hiệu quả thực sự thì nó không hẳn chủ yếu là trấn an tâm lý."

  Transcript 02:34:34–02:35:34 · [▶ watch from 02:34:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9274s)

  ```text
    [02:34:35] giây đại ý. Thế thì sau đó thì bắt đầu
    [02:34:38] là chúng ta lấy lại bình tĩnh thì chúng
    [02:34:40] ta sẽ thoát khỏi cái chuyện đấy là cứ
    [02:34:42] khuyên nhau thế thôi nhưng mà ai cũng sợ
    [02:34:44] có đúng không ạ? đấy là khuyên rằng nó
    [02:34:46] không có vấn đề gì hết cả. Thế rồi một
  ▶ [02:34:49] số người đi ngủ sẽ đặt con dao ở dưới
    [02:34:51] giường, nghĩ rằng đấy là do ma làm, đặt
    [02:34:53] con dao dưới giường, thế rồi tỏi, thế
    [02:34:55] rồi hành, thế rồi thì gì đủ thứ làm các
    [02:34:58] cái việc đó thì chúng ta làm cái đấy đấy
  ▶ [02:35:01] là liệu pháp giả dược.
    [02:35:03] >> Vâng.
    [02:35:03] >> Tức là về mặt tinh thần để chúng ta trấn
    [02:35:05] an tâm lý. Vâng.
  ▶ [02:35:06] >> Chứ còn nó hiệu quả thực sự thì nó không
  ▶ [02:35:09] hẳn chủ yếu là trấn an tâm lý. Nhưng đi
    [02:35:12] sâu hơn, tất cả những cái này tài liệu
    [02:35:14] sẽ không nói đến đi sâu hơn. Thì vấn đề
    [02:35:17] nó là thế này.
    [02:35:19] Chúng ta để ức chế thần kinh, căng thẳng
    [02:35:21] thần kinh quá lâu, chúng ta bức xúc cái
    [02:35:23] gì đó, cuộc sống của chúng ta không
    [02:35:25] thanh thản thì như lúc nãy tôi nói cái
    [02:35:28] phần sinh giới gốc tự do ấ là yếu tố
    [02:35:31] tinh thần vô cùng quan trọng. Não của
    [02:35:34] chúng ta chiếm bao nhiêu phần trăm trọng
  ```

### c166

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 02:37:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9417s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** BS Trần Văn Phúc describing his own practice; summary turns it into general advice

- **BEFORE (current summary):** Lời khuyên là sống bình thường, làm được gì thì làm, không làm được thì thôi, và không tiếp nhận năng lượng xấu như đọc tin tiêu cực quá nhiều.
- **AFTER (proposed):** Bác sĩ khuyên "aq quy một chút": cuộc sống diễn ra bình thường, cái gì làm được thì làm, không làm được thì thôi. Ông kể bản thân không tiếp cận năng lượng xấu vào cơ thể, còn thông tin xấu trên mạng xã hội thì ông chỉ đọc lướt qua để xem hôm nay xảy ra chuyện gì.
- **Why:** The news part is the doctor's own habit, and the summary turns it into general advice. 'Quá nhiều' (too much) is not said.
- **Pass-1 note:** Doctor's personal anecdote generalized; he says he does read bad news but only skims and doesn't dwell, never says 'đọc tin tiêu cực quá nhiều' — wording/qualification altered.
- **Pass-2 note (blind):** Borderline: the 'năng lượng xấu'/negative-news part is the doctor's personal practice (skimming news), which the summary turns into general advice
- **Reconciliation:** The source describes the doctor’s own habit of skimming bad news; the summary turns it into general advice and adds “too much.” Retain attribution/qualification issue.
- **Surrounding summary claims:**
  - previous (c165): Người căng thẳng kéo dài dễ ngủ không yên, gặp ác mộng và bóng đè, và bác sĩ nói gốc tự do gây lão hóa nhanh.
  - next (c167): Bác sĩ cho rằng dùng nhiều hóa chất và thuốc không cần thiết đều sinh gốc tự do.
- **Quotes cited:**
  - [▶ 02:37:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9417s) "ta làm được thì làm, còn không làm được"
  - [▶ 02:37:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9447s) "tiếp cận những cái năng lượng xấu vào cơ"
  - [▶ 02:37:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9451s) "đọc những cái thông tin xấu. Tôi đọc chỉ"
  - [▶ 02:37:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9451s) "Tôi đọc chỉ là để tôi lướt qua tôi xem ngày hôm nay đang xảy ra chuyện gì."

  Transcript 02:36:47–02:38:01 · [▶ watch from 02:36:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9407s)

  ```text
    [02:36:48] trong cuộc sống không giải tỏa được thì
    [02:36:50] trong đêm chúng ta sẽ dễ gặp ác mộng,
    [02:36:53] chúng ta sẽ dễ bị bóng đè.
    [02:36:55] Vậy điều đầu tiên đó là chúng ta phải aq
    [02:36:58] quy một chút đi. Cuộc sống mọi cái nó
    [02:37:00] phải diễn ra bình thường. Cái gì chúng
  ▶ [02:37:02] ta làm được thì làm, còn không làm được
    [02:37:04] chúng ta thôi. Ông trời chỉ cho chúng ta
    [02:37:06] làm đến đấy thôi. Đúng không ạ? Nó aq
    [02:37:08] quy một tí thì tôi chả bao giờ tôi bức
    [02:37:10] xúc gì với ai. Cái việc mà giả sử có đôi
    [02:37:13] khi tôi nói nặng lời với một ai đó hay
    [02:37:15] gì đó. Mục đích của tôi là gì? Là muốn
    [02:37:17] tạo cái ấn tượng mạnh cho người ta để
    [02:37:19] người ta thay đổi lối sống cuộc sống.
    [02:37:21] Còn tôi chả hơi đâu tôi đi tôi chấp
    [02:37:22] người ngoài làm cái gì đúng không ạ?
    [02:37:24] Chẳng qua là ví dụ tôi muốn dùng ngôn
    [02:37:27] ngữ hay muốn dùng cái gì đó để tôi tác
    [02:37:29] động tới những cái người mà đối diện với
    [02:37:31] tôi thôi chứ còn tôi không bao giờ tôi
  ▶ [02:37:32] tiếp cận những cái năng lượng xấu vào cơ
    [02:37:33] thể cả. Tôi lên mạng xã hội hầu như tôi
  ▶ [02:37:36] đọc những cái thông tin xấu. Tôi đọc chỉ
  ▶ [02:37:38] là để tôi lướt qua tôi xem ngày hôm nay
  ▶ [02:37:40] đang xảy ra chuyện gì. Còn tôi coi đấy
    [02:37:42] là hiện tượng bình thường của xã hội.
    [02:37:44] Nếu hiện tượng đó tôi tác động được vào
    [02:37:46] tích cực để nó thay đổi đi thì tôi làm.
    [02:37:49] còn không tác động được tích cực thôi
    [02:37:51] không cần quan tâm đến cái việc ấy nữa.
    [02:37:53] Đúng rồi. Chà hơi đâu để mà bức xúc cái
    [02:37:54] đấy thì chúng ta sẽ không rơi vào cái
    [02:37:58] trạng thái là tiêu tốn quá nhiều năng
    [02:38:00] lượng mà ti thể ở trong tế bào não hoạt
  ```

### c172

**Decisions:** D5, D11 (correction approval)  
**Watch:** [▶ 02:40:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9598s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** BS Trần Văn Phúc; matches

- **BEFORE (current summary):** Bác sĩ nói những người bị táo bón, hội chứng ruột kích thích, viêm dạ dày ruột không tiết được serotonin, nên dễ bị bóng đè khi mơ màng lúc ngủ, thức.
- **AFTER (proposed):** Bác sĩ nói một số những người bị táo bón, bị hội chứng ruột kích thích, bị dạ dày ruột thì không thể tiết được serotonin, nên cứ mơ màng, thức ngủ thì rất dễ bị bóng đè.
- **Why:** Qualifier dropped: 'một số' (some) was removed, so the claim covers everyone with these conditions.
- **Pass-1 note:** Qualifier 'một số' (some of these people) dropped; summary generalizes to all people with constipation/IBS/gut issues.
- **Pass-2 note (blind):** Dropped the 'một số' (some) population qualifier, so the claim covers all such people
- **Surrounding summary claims:**
  - previous (c171): Theo bác sĩ, khoảng 95% serotonin được tiết ở ruột và khoảng 5% ở não.
  - next (c173): Bác sĩ cho rằng cần giải quyết tình trạng đường ruột này, và các con đường trên đều dẫn tới gốc tự do.
- **Quotes cited:**
  - [▶ 02:40:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9598s) "thấy rằng một số những người mà bị táo"
  - [▶ 02:40:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9604s) "dày ruột thì nó không thể tiết được"
  - [▶ 02:40:16](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9611s) "dễ bị bóng đè."

  Transcript 02:39:48–02:40:41 · [▶ watch from 02:39:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9588s)

  ```text
    [02:39:49] Tới 95%.
    [02:39:50] >> Vâng.
    [02:39:50] >> Ở trên não tới gì ạ? Trên não khoảng 5%.
    [02:39:55] Đối ngược với lại à cùng với serotonin
    [02:39:57] nó còn có một loạt những cái đấy là ep
    [02:40:01] ferin các thứ. Đấy. Thế thì chúng ta sẽ
  ▶ [02:40:03] thấy rằng một số những người mà bị táo
    [02:40:06] bón, bị hội chứng ruột kích thích, bị dạ
  ▶ [02:40:09] dày ruột thì nó không thể tiết được
    [02:40:11] serotonin. Vậy thì chúng ta cứ mơ mơ
    [02:40:14] màng màng, thức ngủ ngủ thì chúng ta rất
  ▶ [02:40:16] dễ bị bóng đè.
    [02:40:17] >> Vâng.
    [02:40:17] >> Đúng không ạ? Còn nếu chúng ta giải
    [02:40:18] quyết được cái câu chuyện đó thì sẽ hết.
    [02:40:21] Mà ruột chúng ta bị là vì sao? Vì hội
    [02:40:24] chứng giò rỉ ruột, bị táo bón, bị giò rỉ
    [02:40:27] ruột, bị viêm đường ruột.
    [02:40:29] >> Hội chứng ruột kích thích.
    [02:40:30] >> Hội chứng ruột kích thích.
    [02:40:31] >> Vâng. nói đi nói lại các số rồi.
    [02:40:33] >> Vâng.
    [02:40:33] >> Đúng rồi. Vậy chúng ta phải có cái giải
    [02:40:34] pháp tổng thể. Thế thì ở đây chúng ta
    [02:40:38] thấy mọi con đường nó đều dẫn đến đó
    [02:40:40] chính là gì? Đó chính là chất gốc tự do.
  ```

### c176

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:41:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9669s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Bác sĩ Trần Văn Phúc trực tiếp nói; tóm tắt quy cho bác sĩ.

- **BEFORE (current summary):** Kẽm là yếu tố hợp đồng với glutathione: nếu thiếu kẽm thì glutathione không có giá trị, vì selen là enzyme chuyển hóa gốc tự do.
- **AFTER (proposed):** Vitamin C, vitamin E, kẽm và selen (bản ghi âm ghi là "cen") là những yếu tố hợp đồng với glutathione. Nếu thiếu kẽm thì glutathione chẳng có giá trị. Selen quá quan trọng trong chuyện là enzyme để chuyển hóa gốc tự do; nếu không có selen thì glutathione vất đi.
- **Why:** The transcript makes two separate statements. The summary invents a causal link (zinc matters 'vì selen...') and says selenium 'is' the enzyme.
- **Pass-1 note:** Tách hai ý thiếu kẽm và thiếu cen; bản ghi nói cen quan trọng trong chuyện enzyme chuyển hóa, không gọi selen là enzyme hay nói thiếu kẽm vô giá trị vì selen.
- **Pass-2 note (blind):** Transcript gives C, E, kẽm and selen as cofactors with separate statements for zinc and selenium; summary invents a causal link (zinc matters 'vì selen...') and says selenium 'is' an enzyme instead of being important for the enzyme
- **Surrounding summary claims:**
  - previous (c175): Bác sĩ nhấn mạnh vitamin C và E rất quan trọng.
  - next (c177): Theo bác sĩ, bổ sung đủ các chất này giúp ngủ ngon và tế bào não hoạt động bình thường.
- **Quotes cited:**
  - [▶ 02:41:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9669s) "là những cái yếu tố hợp đồng với lại glutathion."
  - [▶ 02:41:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9673s) "Nếu bây giờ các bạn thiếu kẽm thì glutathion chẳng có giá trị. Cen quá quan trọng trong cái chuyện là enzyme để mà chuyển hóa gốc tự do. Nếu không có cen thì glutat vất đi."
  - [▶ 02:41:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9658s) "Tôi nhắc lại là vitamin C là một này, E là hai này, kẽm là ba này, cen là 4 này."

  Transcript 02:40:48–02:41:43 · [▶ watch from 02:40:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9648s)

  ```text
    [02:40:49] thì chúng ta sẽ có nhiều cái ví dụ như
    [02:40:52] là gì ạ? Catalas đúng không ạ? Vâng.
    [02:40:55] >> Thế rồi ví dụ như là licoben, ví dụ như
    [02:40:59] là vitamin C, vitamin E và kẽm celen.
  ▶ [02:41:03] >> Tôi nhắc lại là vitamin C là một này, E
  ▶ [02:41:06] là hai này, kẽm là ba này, cen là 4 này.
    [02:41:10] Tất cả bốn cái này là giải quyết những
    [02:41:12] cái gốc tự do vô cùng quan trọng. Và đây
  ▶ [02:41:14] là những cái yếu tố hợp đồng với lại
  ▶ [02:41:16] glutathion.
    [02:41:17] >> Vâng.
  ▶ [02:41:18] >> Nếu bây giờ các bạn thiếu kẽm thì
  ▶ [02:41:20] glutathion chẳng có giá trị. Cen quá
  ▶ [02:41:23] quan trọng trong cái chuyện là enzyme để
  ▶ [02:41:27] mà chuyển hóa gốc tự do. Nếu không có
  ▶ [02:41:29] cen thì glutat vất đi.
    [02:41:31] >> Vâng.
    [02:41:31] >> Chẳng giải quyết được cái gì hết cả.
    [02:41:33] Vitamin C, vitamin E vô cùng quan trọng.
    [02:41:37] Vậy khi bổ sung nó thì chúng ta sẽ ngủ
    [02:41:38] ngon, chúng ta ngủ tốt, thực hành lối
    [02:41:40] sống tốt, ngủ ngon, ngủ tốt thì chúng ta
    [02:41:42] các tế bào não hoạt động bình thường,
  ```

### c177

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 02:41:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9688s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc trực tiếp nói; tóm tắt quy cho bác sĩ.

- **BEFORE (current summary):** Theo bác sĩ, bổ sung đủ các chất này giúp ngủ ngon và tế bào não hoạt động bình thường.
- **AFTER (proposed):** Theo bác sĩ, khi bổ sung các chất này thì sẽ ngủ ngon, ngủ tốt; cùng với thực hành lối sống tốt, ngủ ngon, ngủ tốt thì các tế bào não hoạt động bình thường.
- **Why:** The transcript pairs supplementation with 'thực hành lối sống tốt'. The summary credits supplementation alone.
- **Pass-1 note:** Bỏ điều kiện đi kèm “thực hành lối sống tốt” khi quy kết ngủ ngon và tế bào não hoạt động bình thường chỉ cho bổ sung.
- **Pass-2 note (blind):** Matches; the transcript also mentions good lifestyle alongside supplementation
- **Reconciliation:** The transcript pairs supplementation with practicing a good lifestyle; the summary attributes the outcome solely to supplementation. Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c176): Kẽm là yếu tố hợp đồng với glutathione: nếu thiếu kẽm thì glutathione không có giá trị, vì selen là enzyme chuyển hóa gốc tự do.
  - next (c178): Bác sĩ nói đó là nguyên nhân nhỏ, không phải nguyên nhân chính, vì cơ thể có cơ chế bù trừ.
- **Quotes cited:**
  - [▶ 02:41:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9688s) "Vitamin C, vitamin E vô cùng quan trọng. Vậy khi bổ sung nó thì chúng ta sẽ ngủ ngon, chúng ta ngủ tốt, thực hành lối sống tốt, ngủ ngon, ngủ tốt thì chúng ta các tế bào não hoạt động bình thường,"

  Transcript 02:41:18–02:41:58 · [▶ watch from 02:41:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9678s)

  ```text
    [02:41:18] >> Nếu bây giờ các bạn thiếu kẽm thì
    [02:41:20] glutathion chẳng có giá trị. Cen quá
    [02:41:23] quan trọng trong cái chuyện là enzyme để
    [02:41:27] mà chuyển hóa gốc tự do. Nếu không có
    [02:41:29] cen thì glutat vất đi.
    [02:41:31] >> Vâng.
    [02:41:31] >> Chẳng giải quyết được cái gì hết cả.
  ▶ [02:41:33] Vitamin C, vitamin E vô cùng quan trọng.
  ▶ [02:41:37] Vậy khi bổ sung nó thì chúng ta sẽ ngủ
  ▶ [02:41:38] ngon, chúng ta ngủ tốt, thực hành lối
  ▶ [02:41:40] sống tốt, ngủ ngon, ngủ tốt thì chúng ta
  ▶ [02:41:42] các tế bào não hoạt động bình thường,
    [02:41:45] các tế bào trong cơ thể chúng ta hoạt
    [02:41:46] động bình thường, nó sẽ không rơi vào
    [02:41:49] cái trạng thái là bóng đè. Thế thì nhiều
    [02:41:53] người trong dân gian, trong cuộc sống
    [02:41:54] của chúng ta hay nói là bóng đè là vì
    [02:41:56] sao ạ? Là
    [02:41:57] >> do ngủ thiếu oxy chẳng hạn hoặc là do tư
  ```

### c182

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 02:42:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9765s)  ·  section start [▶ 01:31:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5487s)  
**Summary section:** [01:31:32] Bóng đè khi ngủ: hiện tượng, cơ chế và cách xử lý  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc trực tiếp nói; tóm tắt quy cho bác sĩ.

- **BEFORE (current summary):** Bác sĩ nói bóng đè là biểu hiện tổn thương ở mức tế bào, phân tử do lối sống, tâm sinh lý, ăn uống và môi trường sai, làm gốc tự do gây mất nhịp giữa "người lái" và "bánh xe".
- **AFTER (proposed):** Bác sĩ nói "tôi cho rằng" bóng đè thể hiện cơ thể đang tổn thương ở mức độ tế bào, phân tử, do lối sống, tâm sinh lý, ăn uống và tiếp xúc tác nhân môi trường sai, làm xuất hiện gốc tự do, và gốc tự do làm cho cái phanh không nhịp nhàng giữa người lái xe và bánh xe.
- **Why:** Hedge dropped: the doctor marks this as his view with 'Tôi cho rằng', and the summary drops it. The proposal restores his wording.
- **Pass-1 note:** Bỏ hedge “Tôi cho rằng” khỏi diễn giải tổn thương tế bào/phân tử và nguyên nhân bóng đè của bác sĩ.
- **Pass-2 note (blind):** Causes (lifestyle, psychology, diet, environment) and the driver/wheel imagery match
- **Reconciliation:** The source explicitly hedges the interpretation with “Tôi cho rằng”; the summary states it without that hedge. Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c181): Không để sóng gamma và sóng beta tăng quá nhiều.
  - next (c183): Người xem đang dùng vitamin D 50.000 IU theo hướng dẫn trên tờ hướng dẫn: một viên mỗi tuần trong 8 tuần, sau đó một viên mỗi tháng.
- **Quotes cited:**
  - [▶ 02:42:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9765s) "cuộc sống. Tôi cho rằng là bóng đè là một cái nó thể hiện cơ thể chúng ta đang thể hiện rằng đang tổn thương ở mức độ tế bào,"
  - [▶ 02:42:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9774s) "tổn thương ở mức độ phân tử. Do chúng ta thực hành lối sống sai, do tâm sinh lý chúng ta sai, do ăn uống, do tiếp xúc với lại các cái yếu tố tác nhân môi trường sai để xuất hiện những cái chất"
  - [▶ 02:43:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9784s) "gốc tự do. Gốc tự do và chính gốc tự do này nó là cái nguyên nhân để làm cho cái phanh này nó không nhịp nhàng giữa người lái xe và bánh xe. Từ đấy chúng ta sẽ rơi vào cái trạng thái bóng đè. Tôi cho"

  Transcript 02:42:35–02:43:34 · [▶ watch from 02:42:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9755s)

  ```text
    [02:42:35] teta
    [02:42:35] >> xong dần dần tới sóng gì ạ? Delta. Chúng
    [02:42:38] ta đi tới như thế chứ đừng để sóng gamma
    [02:42:40] nó lên. Đừng để sóng beta nó lên quá
    [02:42:42] nhiều. Đừng để kịch phát beta. Tất cả
    [02:42:45] những cái đó chúng ta tập thì chúng ta
    [02:42:47] dần dần chúng ta sẽ bình ổn được lại
  ▶ [02:42:50] cuộc sống. Tôi cho rằng là bóng đè là
  ▶ [02:42:53] một cái nó thể hiện cơ thể chúng ta đang
  ▶ [02:42:56] thể hiện rằng đang tổn thương ở mức độ
  ▶ [02:42:58] tế bào,
  ▶ [02:42:59] >> tổn thương ở mức độ phân tử. Do chúng ta
  ▶ [02:43:01] thực hành lối sống sai, do tâm sinh lý
  ▶ [02:43:03] chúng ta sai, do ăn uống, do tiếp xúc
  ▶ [02:43:05] với lại các cái yếu tố tác nhân môi
  ▶ [02:43:07] trường sai để xuất hiện những cái chất
  ▶ [02:43:09] >> gốc tự do. Gốc tự do và chính gốc tự do
  ▶ [02:43:12] này nó là cái nguyên nhân để làm cho cái
  ▶ [02:43:14] phanh này nó không nhịp nhàng giữa người
  ▶ [02:43:16] lái xe và bánh xe. Từ đấy chúng ta sẽ
  ▶ [02:43:20] rơi vào cái trạng thái bóng đè. Tôi cho
    [02:43:22] rằng đây là một vấn đề quan trọng.
    [02:43:24] >> Vâng.
    [02:43:24] >> Chứ không phải rằng là trên các tài liệu
    [02:43:26] nói rằng đây là vấn đề không có gì quá
    [02:43:28] quan trọng và hướng dẫn nhau hít một hơi
    [02:43:30] thở thật sâu rồi chúng ta bình tĩnh lại.
    [02:43:33] Nói thế thì nó rất là đơn giản đúng
    [02:43:34] không ạ? Vâng,
  ```

### c193

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 02:46:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9999s)  ·  section start [▶ 01:33:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5580s)  
**Summary section:** [01:33:05] Vitamin D 50.000 IU: liều, nồng độ mục tiêu và cách duy trì  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc trực tiếp nói; tóm tắt quy cho bác sĩ.

- **BEFORE (current summary):** Người khỏe mạnh, không có bệnh nền, không có mỡ máu, tiểu đường hay huyết áp cao thì bổ sung liều cao lên nồng độ dễ và hiệu quả.
- **AFTER (proposed):** Người khỏe mạnh, không còn bệnh tật gì khác, không bị nhiều mỡ, mỡ dưới da ít, không có mỡ nội tạng, không bị mỡ máu, tiểu đường hay huyết áp thì bổ sung liều cao sẽ lên được dễ và hiệu quả.
- **Why:** Conditions dropped: the doctor also limits this to people with little body, subcutaneous and visceral fat.
- **Pass-1 note:** Bỏ điều kiện ít mỡ dưới da, không mỡ nội tạng/không nhiều mỡ khi mô tả nhóm dùng liều cao dễ và hiệu quả.
- **Pass-2 note (blind):** Conditions and outcome match
- **Reconciliation:** The source also limits the example to low body/subcutaneous/visceral fat; the summary omits those conditions. Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c192): Bác sĩ nói lời khuyên này đúng, không có gì sai.
  - next (c194): Nếu có bệnh nền hoặc tích nhiều mỡ dưới da và mỡ nội tạng, bổ sung liều cao có thể làm tế bào quá tải, gây "bẫy mỡ", mụn nội tiết hoặc ngứa.
- **Quotes cited:**
  - [▶ 02:46:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9999s) "tật gì khác, rất khỏe rồi, không bị nhiều mỡ, mỡ dưới da ít, mỡ nội tạng không có, không bị mỡ máu, không bị tiểu đường, không bị huyết áp thì khánh lành bổ sung liều cao thì nó sẽ lên được dễ và nó hiệu quả. Nhưng nếu chúng ta có"

  Transcript 02:46:29–02:47:09 · [▶ watch from 02:46:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9989s)

  ```text
    [02:46:29] sung vitamin liều thấp thay vì cái liều
    [02:46:32] cao toàn bộ liều cao ngay một lúc. Bổ
    [02:46:35] sung liều thấp nó có những cái tác dụng
    [02:46:36] gì? Nếu những người khỏe mạnh, ví dụ như
    [02:46:39] Khánh Lành bây giờ đang xinh đẹp, đang
    [02:46:41] khỏe, tất cả trong cơ thể không còn bệnh
  ▶ [02:46:44] tật gì khác, rất khỏe rồi, không bị
  ▶ [02:46:46] nhiều mỡ, mỡ dưới da ít, mỡ nội tạng
  ▶ [02:46:48] không có, không bị mỡ máu, không bị tiểu
  ▶ [02:46:50] đường, không bị huyết áp thì khánh lành
  ▶ [02:46:52] bổ sung liều cao thì nó sẽ lên được dễ
  ▶ [02:46:56] và nó hiệu quả. Nhưng nếu chúng ta có
    [02:46:58] bệnh nền, chúng ta có tích mỡ dưới da
    [02:47:01] nhiều, tích mỡ nội tạng nhiều mà chúng
    [02:47:03] ta bổ sung vitamin D liều cao nó có thể
    [02:47:05] gây ra cái tình trạng là tế bào quá tải.
    [02:47:08] >> Vâng.
    [02:47:08] >> Bẫy mỡ. Bẫy mỡ và qu tế bào quá tải nó
  ```

### c201

**Decisions:** D7, D11 (correction approval)  
**Watch:** [▶ 02:49:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10148s)  ·  section start [▶ 01:33:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5580s)  
**Summary section:** [01:33:05] Vitamin D 50.000 IU: liều, nồng độ mục tiêu và cách duy trì  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Bác sĩ Trần Văn Phúc nói; bản tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Có người chỉ cần khoảng 5.600 UI (bản ghi âm ghi như vậy), có người lên tới 6.000 đến 7.000 UI, nhưng đa số dưới 2.000 UI.
- **AFTER (proposed):** Có người chỉ có "5 600 UI" (bản ghi âm ghi như vậy, con số không rõ) đã đủ, có người lên tới "6 7000 UI", nhưng đại đa số mọi người là con số trên dưới 2.000 UI.
- **Why:** 'Trên dưới 2000' (around 2000) became 'dưới 2.000' (under 2000). '5 600' is also ambiguous, so the summary's 5.600 is not confirmed.
- **Pass-1 note:** Bản ghi nói đa số “trên dưới 2000 UI”, không phải dưới 2.000; chuỗi “5 600” cũng mơ hồ, không xác nhận chắc 5.600.
- **Pass-2 note (blind):** Doctor says the majority need 'trên dưới 2000 UI' (around 2000); summary says 'dưới 2.000 UI' (under 2000)
- **Surrounding summary claims:**
  - previous (c200): Theo bác sĩ, nghiên cứu cho thấy nhu cầu thường quanh 2.000 UI mỗi ngày, tùy từng người.
  - next (c202): Để dò liều, bác sĩ chọn 2.000 UI mỗi ngày, xét nghiệm vài lần để xác định mỗi ngày cần bao nhiêu, rồi duy trì uống đều đặn.
- **Quotes cited:**
  - [▶ 02:49:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10148s) "Có người chỉ có 5 600 UI đã đủ rồi nhưng có người lên tới 6 7000 UI cơ."
  - [▶ 02:49:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10152s) "Vâng. Nhưng đại đa số mọi người là con số trên dưới 2000 UI. Cho nên khi dò liều tôi"

  Transcript 02:48:58–02:49:42 · [▶ watch from 02:48:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10138s)

  ```text
    [02:48:59] >> Vâng. Thế thì các nghiên cứu trên thế
    [02:49:02] giới người ta thấy rằng thông thường nhu
    [02:49:04] cầu bổ sung vitamin D của mọi người nó
    [02:49:07] hay duy trì con số loanh quanh là 2000
    [02:49:10] một ngày tùy theo từng người.
    [02:49:12] >> Vâng.
  ▶ [02:49:13] >> Có người chỉ có 5 600 UI đã đủ rồi nhưng
  ▶ [02:49:15] có người lên tới 6 7000 UI cơ.
  ▶ [02:49:17] >> Vâng.
  ▶ [02:49:17] >> Nhưng đại đa số mọi người là con số trên
  ▶ [02:49:20] dưới 2000 UI. Cho nên khi dò liều tôi
    [02:49:23] hay nói rằng ta chọn cái liều là 2000 UI
    [02:49:26] một ngày để ta dò. Dò là gì? là ta đi
    [02:49:29] xét nghiệm vài lần để trả lời xem mỗi
    [02:49:31] ngày ta cần bao nhiêu ui. Nếu như trả
    [02:49:33] lời được cái câu hỏi đấy rồi thì lúc đấy
    [02:49:35] ta cứ uống đều đặn hàng ngày để ta duy
    [02:49:38] trì cái vitamin theo D theo đường thẳng.
    [02:49:41] Thế còn ai bận công việc ai không uống
  ```

### c208

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:37:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5835s)  ·  section start [▶ 01:36:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5778s)  
**Summary section:** [01:36:23] Lời khuyên cho học sinh hay quên bị mẹ mắng  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc nói; bản tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Bác sĩ nói trí tuệ không phải do trời cho mà đến từ sự cần cù, chịu khó và quyết tâm.
- **AFTER (proposed):** Bác sĩ nói con người sinh ra không phải ông trời cũng cho tất cả mọi người trí tuệ tốt, trí nhớ siêu phàm hay năng lực tuyệt vời; riêng bản thân ông nói mình có trí tuệ không được tốt lắm và chỉ nhờ sự cần cù chịu khó, sự quyết tâm trong những năm tháng tuổi ấu thơ.
- **Why:** Overgeneralized: he says heaven does not give everyone good intellect and describes his own diligence. He does not say intellect in general comes from diligence.
- **Pass-1 note:** Khái quát hóa lời tự thuật: bác sĩ nói không phải mọi người được trời cho trí tuệ tốt, còn sự cần cù/quyết tâm là chuyện bản thân; không phủ nhận phổ quát trí tuệ do trời cho.
- **Pass-2 note (blind):** Overgeneralized: doctor says heaven does not give everyone good intellect and that he himself succeeded through diligence; summary hardens this into 'trí tuệ không phải do trời cho mà đến từ sự cần cù'
- **Surrounding summary claims:**
  - previous (c207): Muốn sức khỏe tốt thì phải ăn uống, ngủ nghỉ đúng khoa học, bổ sung vi chất và chế độ ăn cân đối.
  - next (c209): Bác sĩ nói ngoài cổng trường có nhiều đồ chiên, rán, nướng, thức ăn nhanh, trà có đường, nước đóng chai và nước ga.
- **Quotes cited:**
  - [▶ 01:37:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5835s) "Anh, con người ta sinh ra không phải ông trời cũng cho tất cả mọi người có được cái trí tuệ tốt, có được cái trí nhớ siêu phàm hay là có những cái năng lực tuyệt vời. Như tôi vẫn tâm sự trong"
  - [▶ 01:37:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5850s) "thân tôi là người mà có trí tuệ không được tốt cho lắm."
  - [▶ 01:37:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5854s) "học cũng mọi cái của tôi cũng không phải là thông minh giỏi giang các thứ gì mà chỉ nhờ vào cái sự cần cù chịu khó, cái sự quyết tâm trong những năm tháng của tuổi ấu thơ với cái điều kiện thiếu ăn"

  Transcript 01:37:05–01:38:04 · [▶ watch from 01:37:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5825s)

  ```text
    [01:37:06] đối với chúng tôi. Và tôi cho rằng những
    [01:37:08] thế hệ trẻ, những các bạn học sinh mà đã
    [01:37:11] theo dõi những các cái chương trình như
    [01:37:12] thế này thì tôi nghĩ rằng là đây cũng là
    [01:37:16] một trong những cái chìa khóa để sau này
    [01:37:18] các bạn thành công. Và thưa với bạn anh
  ▶ [01:37:20] Anh, con người ta sinh ra không phải ông
  ▶ [01:37:24] trời cũng cho tất cả mọi người có được
  ▶ [01:37:26] cái trí tuệ tốt, có được cái trí nhớ
  ▶ [01:37:28] siêu phàm hay là có những cái năng lực
  ▶ [01:37:30] tuyệt vời. Như tôi vẫn tâm sự trong
    [01:37:33] nhiều số phát sóng trước đây, đó là bản
  ▶ [01:37:35] thân tôi là người mà có trí tuệ không
  ▶ [01:37:37] được tốt cho lắm.
  ▶ [01:37:39] học cũng mọi cái của tôi cũng không phải
  ▶ [01:37:42] là thông minh giỏi giang các thứ gì mà
  ▶ [01:37:44] chỉ nhờ vào cái sự cần cù chịu khó, cái
  ▶ [01:37:47] sự quyết tâm trong những năm tháng của
  ▶ [01:37:49] tuổi ấu thơ với cái điều kiện thiếu ăn
    [01:37:52] thiếu mặc rất khó khăn, tôi bị suy dinh
    [01:37:54] dưỡng, tôi cũng từ cõi chết trở về nhưng
    [01:37:57] mà vượt qua chính bản thân mình đấy là
    [01:37:58] cái điều khó khăn nhất để tôi có thể
    [01:38:00] thành công được đến ngày hôm nay.
    [01:38:03] Thế và có thể nói rằng những năm tháng
    [01:38:04] tuổi Âu thơ của tôi là vì thiếu các cái
  ```

### c210

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:40:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6009s)  ·  section start [▶ 01:39:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5983s)  
**Summary section:** [01:39:48] Thói quen ăn uống của học sinh: thức ăn nhanh, đường và nước ga  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc nói; bản tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Học sinh cũng lười nhai và thường chỉ muốn ăn nhanh, hấp thu năng lượng nhanh, dẫn đến calo rỗng.
- **AFTER (proposed):** Bác sĩ nói các bạn ăn thức ăn nhanh, uống nhiều đồ uống có đường và rơi vào tình trạng calo rỗng rất nhiều. Ông kể hai đứa con của một chị bạn lười nhai, lười mọi thứ và chỉ muốn ăn sẵn, ăn nhanh.
- **Why:** Causal link added: empty calories are tied to sugary drinks and fast food, not to lazy chewing. The chewing story is about a friend's two children, not students in general.
- **Pass-1 note:** Thêm quan hệ nhân quả “lười nhai…dẫn đến calo rỗng”; bản ghi nói calo rỗng trước, rồi kể hai con của người bạn lười nhai và nhận xét lối sống nhanh.
- **Pass-2 note (blind):** Laziness in chewing is said of a friend's two children ('các bạn ấy'), generalized to students; calo rỗng is tied to sugary drinks/fast food, not caused by wanting fast energy (that leads to 'thất bại'); causal link added
- **Surrounding summary claims:**
  - previous (c209): Bác sĩ nói ngoài cổng trường có nhiều đồ chiên, rán, nướng, thức ăn nhanh, trà có đường, nước đóng chai và nước ga.
  - next (c211): Bác sĩ nói việc này có thể khiến các em thất bại, nên phải thay đổi thói quen ăn uống từ hàng ngày.
- **Quotes cited:**
  - [▶ 01:40:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6009s) "cái calor rỗng các bạn đang rơi vào cái tình trạng đấy rất nhiều. Thế và các bạn ăn những các cái đồ ăn của thức ăn nhanh. Đến nỗi mà tôi có chị bạn có hai"
  - [▶ 01:40:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6029s) "thịt cũng thế phải say nó ra để đỡ khỏi nhai. Các bạn ấy lười nhai, các bạn ấy lười tất cả mọi thứ và chỉ muốn rằng ăn sẵn ăn nhanh."
  - [▶ 01:40:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6037s) "Vậy khi chúng ta duy trì một cái lối sống mà nhanh gấp gáp, chỉ muốn rằng là tiếp thu những cái gì mà nó nhanh chóng tạo ra năng lượng thì chúng ta sẽ thất"
  - [▶ 01:40:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6000s) "các bạn uống rất nhiều đường"

  Transcript 01:39:50–01:41:07 · [▶ watch from 01:39:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5990s)

  ```text
    [01:39:50] ta sẽ thấy ngay từ trường mẫu giáo,
    [01:39:52] trường mầm non cho đến trường cấp ba,
    [01:39:54] trường đại học, ngay ngoài cổng trường
    [01:39:56] rất nhiều những các cái đồ thịt cá chiên
    [01:39:58] dán động đến chỗ nào cũng thấy đường,
    [01:40:00] động đến chỗ nào cũng thấy nướng. Thế
    [01:40:03] rồi các bạn ăn những cái món thức ăn
  ▶ [01:40:05] nhanh, các bạn uống rất nhiều đường, các
    [01:40:07] bạn uống đủ các cái loại trà có đường,
    [01:40:10] uống đủ các cái loại nước đóng chai,
    [01:40:12] những các cái nước ga. Thế rồi những các
  ▶ [01:40:14] cái calor rỗng các bạn đang rơi vào cái
  ▶ [01:40:17] tình trạng đấy rất nhiều. Thế và các bạn
  ▶ [01:40:20] ăn những các cái đồ ăn của thức ăn
  ▶ [01:40:21] nhanh. Đến nỗi mà tôi có chị bạn có hai
    [01:40:25] đứa con không bao giờ ăn cá thì tôi hỏi
    [01:40:27] lý do tại sao không ăn cá thì các cháu
    [01:40:30] trả lời rằng ăn cá gọ xương phải mất
    [01:40:31] công để mà nhằn xương ra. Thế rồi ăn
  ▶ [01:40:34] thịt cũng thế phải say nó ra để đỡ khỏi
  ▶ [01:40:36] nhai. Các bạn ấy lười nhai, các bạn ấy
  ▶ [01:40:38] lười tất cả mọi thứ và chỉ muốn rằng ăn
  ▶ [01:40:40] sẵn ăn nhanh.
  ▶ [01:40:42] Vậy khi chúng ta duy trì một cái lối
  ▶ [01:40:44] sống mà nhanh gấp gáp, chỉ muốn rằng là
  ▶ [01:40:47] tiếp thu những cái gì mà nó nhanh chóng
  ▶ [01:40:50] tạo ra năng lượng thì chúng ta sẽ thất
    [01:40:52] bại. Vậy đầu tiên là ta phải thay đổi
    [01:40:54] ngay từ cái thói quen ăn uống hàng ngày.
    [01:40:57] Phải ăn uống làm sao thật khoa học mà
    [01:40:58] tôi vẫn nói rằng cái đĩa thức ăn gì ạ?
    [01:41:00] Cái đĩa thức ăn hạnh phúc đúng không ạ?
    [01:41:03] tôi đã xây dựng đầu tiên là tôi dùng nắm
    [01:41:05] đấm xong tiếp theo nữa là các cái tỉ lệ
    [01:41:07] và sau đấy dần dần bắt đầu tôi xây dựng
  ```

### c211

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:40:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6037s)  ·  section start [▶ 01:39:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5983s)  
**Summary section:** [01:39:48] Thói quen ăn uống của học sinh: thức ăn nhanh, đường và nước ga  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc nói; bản tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Bác sĩ nói việc này có thể khiến các em thất bại, nên phải thay đổi thói quen ăn uống từ hàng ngày.
- **AFTER (proposed):** Bác sĩ nói khi duy trì lối sống nhanh, gấp gáp, chỉ muốn những gì nhanh chóng tạo ra năng lượng thì "chúng ta sẽ thất bại", nên đầu tiên phải thay đổi ngay từ thói quen ăn uống hàng ngày.
- **Why:** Softened hedge: 'chúng ta sẽ thất bại' became 'có thể khiến các em thất bại'. The proposal restores his wording and his 'chúng ta'.
- **Pass-1 note:** Thêm hedge “có thể”: bác sĩ nói “chúng ta sẽ thất bại”, rồi yêu cầu thay đổi thói quen ăn uống hằng ngày.
- **Pass-2 note (blind):** Hedge added: transcript 'chúng ta sẽ thất bại' (definite, said of 'chúng ta') softened to 'có thể khiến các em thất bại'
- **Surrounding summary claims:**
  - previous (c210): Học sinh cũng lười nhai và thường chỉ muốn ăn nhanh, hấp thu năng lượng nhanh, dẫn đến calo rỗng.
  - next (c212): Bác sĩ nói bắt đầu bằng cách dùng nắm tay để ước lượng khẩu phần, sau đó dùng tỉ lệ, rồi dần đi sâu vào từng khối vi chất và tính theo gam.
- **Quotes cited:**
  - [▶ 01:40:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6037s) "Vậy khi chúng ta duy trì một cái lối sống mà nhanh gấp gáp, chỉ muốn rằng là tiếp thu những cái gì mà nó nhanh chóng tạo ra năng lượng thì chúng ta sẽ thất bại. Vậy đầu tiên là ta phải thay đổi ngay từ cái thói quen ăn uống hàng ngày."

  Transcript 01:40:27–01:41:07 · [▶ watch from 01:40:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6027s)

  ```text
    [01:40:27] lý do tại sao không ăn cá thì các cháu
    [01:40:30] trả lời rằng ăn cá gọ xương phải mất
    [01:40:31] công để mà nhằn xương ra. Thế rồi ăn
    [01:40:34] thịt cũng thế phải say nó ra để đỡ khỏi
    [01:40:36] nhai. Các bạn ấy lười nhai, các bạn ấy
    [01:40:38] lười tất cả mọi thứ và chỉ muốn rằng ăn
    [01:40:40] sẵn ăn nhanh.
  ▶ [01:40:42] Vậy khi chúng ta duy trì một cái lối
  ▶ [01:40:44] sống mà nhanh gấp gáp, chỉ muốn rằng là
  ▶ [01:40:47] tiếp thu những cái gì mà nó nhanh chóng
  ▶ [01:40:50] tạo ra năng lượng thì chúng ta sẽ thất
  ▶ [01:40:52] bại. Vậy đầu tiên là ta phải thay đổi
  ▶ [01:40:54] ngay từ cái thói quen ăn uống hàng ngày.
    [01:40:57] Phải ăn uống làm sao thật khoa học mà
    [01:40:58] tôi vẫn nói rằng cái đĩa thức ăn gì ạ?
    [01:41:00] Cái đĩa thức ăn hạnh phúc đúng không ạ?
    [01:41:03] tôi đã xây dựng đầu tiên là tôi dùng nắm
    [01:41:05] đấm xong tiếp theo nữa là các cái tỉ lệ
    [01:41:07] và sau đấy dần dần bắt đầu tôi xây dựng
  ```

### c235

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 01:52:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6755s)  ·  section start [▶ 01:52:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6734s)  
**Summary section:** [01:52:19] Lối sống lành mạnh là con đường thay cho lối tắt  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Bác sĩ nói riêng với bạn Anh Anh; tóm tắt khái quát thành người làm như vậy.

- **BEFORE (current summary):** Ông nói từng bước đan xen kiến thức, và tin rằng người làm như vậy sẽ thành công, không phải người gặp khó khăn khi bước vào đời.
- **AFTER (proposed):** Ông nói từng bước đan xen kiến thức, tin rằng khi chuẩn bị những kỹ năng đó thì đến một ngày không xa bạn sẽ thành công; và ông nói riêng với bạn Anh Anh, người xem kênh, biết đặt câu hỏi, biết quan tâm trăn trở, rằng ông tin bạn sẽ là người thành công chứ không phải người sau này bước vào đời gặp phải khó khăn.
- **Why:** Scope lost: the last prediction is addressed to Anh Anh and rests on asking questions and showing concern. The summary generalizes it to anyone who follows the steps.
- **Pass-1 note:** Bỏ phạm vi lời dự đoán dành riêng cho Anh Anh và điều kiện bạn biết đặt câu hỏi, quan tâm trăn trở.
- **Pass-2 note (blind):** Content and 'tin rằng' hedge preserved; addressed to Anh Anh, summary slightly generalizes
- **Reconciliation:** The prediction addresses Anh Anh and the behaviors of asking questions and showing concern; the summary generalizes beyond that context. Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c234): Theo bác sĩ, con đường đúng là sống và thực hành một lối sống lành mạnh, trong sáng, dựa trên hiểu biết khoa học về chế độ ăn uống, ngủ nghỉ, làm việc, học tập và rèn kỹ năng học tập.
  - next (c236): Ông nêu ví dụ điều dưỡng Ngân muốn tư vấn cho bệnh nhân nhưng nếu không cẩn thận có thể bị quy kết là quảng cáo thực phẩm chức năng, hoặc đưa thông tin chưa được xác thực và kiểm chứng.
- **Quotes cited:**
  - [▶ 01:52:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6755s) "cái kỹ năng đó khi bạn chuẩn bị cho mình thì tôi tin rằng đến một ngày không xa bạn sẽ thành công. Và ngày hôm nay bạn xem kênh của chúng tôi biết đặt ra câu hỏi như thế này, biết quan tâm trăn trở như thế này, tôi tin rằng bạn sẽ là cái người thành công chứ không phải là cái người mà sau này bạn bước vào đời gặp phải những cái khó khăn. Tôi tin rằng"
  - [▶ 01:52:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6750s) "đan xen các cái kiến thức với nhau."
  - [▶ 01:52:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6773s) "Thì đấy là bạn Anh Anh sau khi"

  Transcript 01:52:20–01:53:23 · [▶ watch from 01:52:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6740s)

  ```text
    [01:52:22] hãy sống thực hành một lối sống thật
    [01:52:25] lành mạnh thật trong sáng dựa trên cái
    [01:52:27] kiến thức cái hiểu biết về khoa học từ
    [01:52:29] chế độ ăn uống, chế độ ngủ nghỉ, chế độ
    [01:52:31] làm việc, chế độ học tập, rèn luyện
    [01:52:34] những cái kỹ năng trong học tập. Cứ từng
  ▶ [01:52:35] bước từng bước chúng ta đi lên đan xen
  ▶ [01:52:38] các cái kiến thức với nhau. Tất cả những
  ▶ [01:52:40] cái kỹ năng đó khi bạn chuẩn bị cho mình
  ▶ [01:52:42] thì tôi tin rằng đến một ngày không xa
  ▶ [01:52:44] bạn sẽ thành công. Và ngày hôm nay bạn
  ▶ [01:52:46] xem kênh của chúng tôi biết đặt ra câu
  ▶ [01:52:47] hỏi như thế này, biết quan tâm trăn trở
  ▶ [01:52:50] như thế này, tôi tin rằng bạn sẽ là cái
  ▶ [01:52:52] người thành công chứ không phải là cái
  ▶ [01:52:54] người mà sau này bạn bước vào đời gặp
  ▶ [01:52:56] phải những cái khó khăn. Tôi tin rằng
  ▶ [01:52:58] như thế. Thì đấy là bạn Anh Anh sau khi
    [01:53:01] bình luận Khánh Lành đọc lên, tôi cảm
    [01:53:02] thấy rằng vô cùng hạnh phúc, vô cùng xúc
    [01:53:04] động khi mà bạn đã chia sẻ với chúng tôi
    [01:53:07] những cái kiến thức mà bạn đang muốn
    [01:53:10] hướng tới nhưng mà bạn lại đang rất lo
    [01:53:12] ngại, e ngại đó chính là hay bị mẹ mắng
    [01:53:15] vì rằng là nhớ nhớ quên quên. thì thôi
    [01:53:18] cứ từ từ dần dần thời gian nó sẽ trả
    [01:53:20] lời. Thế và trong số những cái bình luận
    [01:53:23] thì tôi thấy rằng là quý vị và các bạn
  ```

### c245

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:03:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7417s)  ·  section start [▶ 02:03:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7412s)  
**Summary section:** [02:03:37] Chia sẻ của khán giả ở Đức và Tokyo sau khi bổ sung vi chất  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ thuật lại khán giả ở Đức và đoán tên Thủy; tóm tắt xác định tên bác Thủy.

- **BEFORE (current summary):** Bác Thủy ở Đức kể sau khi bổ sung vi chất, mọi người xung quanh ốm nhưng bác không sao.
- **AFTER (proposed):** Một bác ở Đức (bác sĩ nói "tôi đoán bác tên là Thủy") kể sau khi bổ sung vi chất, mọi người xung quanh đều quay ra ốm nhưng bác không sao.
- **Why:** Hedge dropped: the name is the doctor's guess, and the summary states it as fact.
- **Pass-1 note:** Bỏ điều kiện tên chỉ là phỏng đoán: tôi đoán bác tên là Thủy.
- **Pass-2 note (blind):** Content matches; the name 'Thủy' is the doctor's guess ('tôi đoán bác tên là Thủy'), presented in summary as fact (hedge dropped)
- **Surrounding summary claims:**
  - previous (c244): Sau khi tìm câu trả lời, ông kết luận là thiếu nền tảng vi chất, tế bào bị "bỏ đói" và phân tử bị tổn thương, dẫn đến nhiều bệnh.
  - next (c246): Cô Thu Trang ở Tokyo trước đây ốm giặt dẹo suốt, đau mỏi, nhưng nay hoàn toàn khỏe mạnh và buổi trưa không cần ngủ nữa.
- **Quotes cited:**
  - [▶ 02:03:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7417s) "Thì bác ở bên Đức tôi đoán bác tên là Thủy. Thì bác thấy rằng sau khi bác bổ sung vi chất tất cả mọi người xung quanh đều quay ra ốm nhưng bác chẳng làm sao hết cả. Thế hoặc là cô giáo thu trang ở"

  Transcript 02:03:27–02:04:07 · [▶ watch from 02:03:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7407s)

  ```text
    [02:03:28] những cái nền tảng về vi chất, chúng ta
    [02:03:30] bỏ đói tế bào, chúng ta để tổn thương
    [02:03:32] những các cái phân tử của chúng ta. Thế
    [02:03:35] dẫn tới là một loạt những cái bệnh tật
    [02:03:37] và đấy bác Thủy, bác Thủy cô và bác Thủy
    [02:03:40] đúng không ạ?
  ▶ [02:03:42] >> Thì bác ở bên Đức tôi đoán bác tên là
  ▶ [02:03:44] Thủy. Thì bác thấy rằng sau khi bác bổ
  ▶ [02:03:46] sung vi chất tất cả mọi người xung quanh
  ▶ [02:03:48] đều quay ra ốm nhưng bác chẳng làm sao
  ▶ [02:03:50] hết cả. Thế hoặc là cô giáo thu trang ở
    [02:03:53] bên Tokyo Nhật Bản cô thấy rằng là trước
    [02:03:56] đây cô ốm giặt dẹo suốt, cô đau mỏi
    [02:03:58] nhưng đến bây giờ cô hoàn toàn khỏe
    [02:04:00] mạnh. buổi trưa không cần thiết phải ngủ
    [02:04:02] nghê nữa. Tôi nhìn cái cành ở bên Nhật
    [02:04:04] họ làm việc đó là làm việc quần quật từ
    [02:04:07] sáng cho đến tối. Bữa trưa chỉ ăn vội
  ```

### c248

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:04:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7459s)  ·  section start [▶ 02:04:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7456s)  
**Summary section:** [02:04:21] Thầy Nguyễn Hiền: đau cột sống, uống nhiều thuốc và paracetamol  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ thuật lại thầy Nguyễn Hiền; tóm tắt thêm diễn tiến càng uống càng nặng.

- **BEFORE (current summary):** Thầy Nguyễn Hiền, giáo viên vật lý, đau cột sống và đau xương hông, nghi có thể là ung thư xương, uống đủ loại thuốc kể cả kháng sinh nhưng không đỡ mà càng uống càng nặng.
- **AFTER (proposed):** Thầy Nguyễn Hiền, thầy giáo vật lý, đau cột sống, đau xương hông, cảm tưởng mình bị đến ung thư xương, uống đủ các loại thuốc cả kháng sinh nhưng cuối cùng không đỡ.
- **Why:** 'Càng uống càng nặng' is not stated: the doctor's sentence breaks off at 'thầy càng uống vào'. 'Cảm tưởng' is also closer to the transcript than 'nghi có thể'.
- **Pass-1 note:** Thêm mức độ càng uống càng nặng: transcript chỉ nói không đỡ rồi câu thầy càng uống vào bị ngắt.
- **Pass-2 note (blind):** Most content supported; 'càng uống càng nặng' is not stated (doctor's sentence trails off at 'thầy càng uống vào') — outcome added/hardened
- **Surrounding summary claims:**
  - previous (c247): Bác sĩ cũng mô tả người Nhật làm việc từ sáng đến tối, bữa trưa ăn vội, nên nếu sức khỏe không tốt thì dễ ốm.
  - next (c249): Bác sĩ nói uống quá nhiều thuốc là một nguyên nhân quan trọng gây gốc tự do.
- **Quotes cited:**
  - [▶ 02:04:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7459s) "Nguyễn Hiền, thầy giáo vật lý bắt đầu vào trường Đại học Sư phạm tôi nhớ là năm 1971. Sau đó thầy đi dạy thầy về quê thầy chuyển chỗ này chỗ khác và thầy bị đau cột sống đau xương hông rồi bị một loạt những các cái bệnh tật mà thầy cảm tưởng rằng thầy bị đến ung thư xương."
  - [▶ 02:04:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7475s) "Thế thì uống đủ các loại thuốc cả kháng sinh đủ các thứ nhưng cuối cùng không đỡ thầy càng uống vào. Mà lúc nãy tôi có"

  Transcript 02:04:09–02:05:05 · [▶ watch from 02:04:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7449s)

  ```text
    [02:04:10] bữa tối của người ta mới là ăn chính.
    [02:04:12] Thế với cái điều kiện làm việc như vậy,
    [02:04:14] nếu như sức khỏe không tốt chúng ta rất
    [02:04:16] dễ bị ốm. Nhưng từ khi cô bổ sung vi
    [02:04:18] chất cái cô thấy rằng mọi thứ nó khỏe và
    [02:04:21] trở nên rất là tốt đẹp. Như là thầy
  ▶ [02:04:24] Nguyễn Hiền, thầy giáo vật lý bắt đầu
  ▶ [02:04:26] vào trường Đại học Sư phạm tôi nhớ là
  ▶ [02:04:28] năm 1971. Sau đó thầy đi dạy thầy về quê
  ▶ [02:04:31] thầy chuyển chỗ này chỗ khác và thầy bị
  ▶ [02:04:33] đau cột sống đau xương hông rồi bị một
  ▶ [02:04:35] loạt những các cái bệnh tật mà thầy cảm
  ▶ [02:04:37] tưởng rằng thầy bị đến ung thư xương.
  ▶ [02:04:40] Thế thì uống đủ các loại thuốc cả kháng
  ▶ [02:04:43] sinh đủ các thứ nhưng cuối cùng không đỡ
  ▶ [02:04:45] thầy càng uống vào. Mà lúc nãy tôi có
    [02:04:48] nói trong cái gốc tự do. Một trong những
    [02:04:50] cái gốc tự do đó chính là một cái nguyên
    [02:04:52] nhân vô cùng quan trọng là chúng ta uống
    [02:04:54] quá nhiều thuốc vào.
    [02:04:55] >> Vâng. Đặc biệt là những cái thuốc giảm
    [02:04:57] đau. Thuốc giảm đau như paracetamol nó
    [02:04:59] hại tới gan đúng không ạ?
    [02:05:01] >> Thế rồi thì nó hại tới thận, hại tới tất
    [02:05:03] cả các nơi thì thuốc này nó sinh ra đây
  ```

### c250

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:04:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7490s)  ·  section start [▶ 02:04:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7456s)  
**Summary section:** [02:04:21] Thầy Nguyễn Hiền: đau cột sống, uống nhiều thuốc và paracetamol  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Khánh Lành hỏi và nêu hại gan; bác sĩ tiếp lời hại thận, các nơi và gốc tự do; tóm tắt gộp thành lời bác sĩ.

- **BEFORE (current summary):** Khi được hỏi về paracetamol, bác sĩ cho rằng thuốc này có thể hại gan, và cũng hại thận và nhiều cơ quan khác, vì sinh ra một hóa chất gây gốc tự do rất lớn.
- **AFTER (proposed):** Trong đoạn nói về thuốc giảm đau, bản ghi âm nêu paracetamol "hại tới gan", rồi "hại tới thận, hại tới tất cả các nơi"; thuốc này là một hóa chất vào trong cơ thể và gây ra gốc tự do rất lớn.
- **Why:** No one asks about paracetamol, and 'có thể' softens a definite statement. Pass 1 and pass 2 read the liver line's speaker differently, so the proposal does not name a speaker for it. Human to confirm the speaker.
- **Pass-1 note:** Gộp nhận định hại gan của người dẫn thành kết luận bác sĩ; thêm có thể so với lời hỏi khẳng định của người dẫn.
- **Pass-2 note (blind):** No one asks about paracetamol (framing added); transcript states it definitively 'nó hại tới gan', summary adds hedge 'có thể'
- **Surrounding summary claims:**
  - previous (c249): Bác sĩ nói uống quá nhiều thuốc là một nguyên nhân quan trọng gây gốc tự do.
  - next (c251): Ông kể một bệnh nhân đau vùng háng, chụp thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải khoan giảm áp và thay khớp háng.
- **Quotes cited:**
  - [▶ 02:04:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7490s) "Vâng. Đặc biệt là những cái thuốc giảm đau. Thuốc giảm đau như paracetamol nó hại tới gan đúng không ạ?"
  - [▶ 02:05:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7496s) "Thế rồi thì nó hại tới thận, hại tới tất cả các nơi thì thuốc này nó sinh ra đây là một cái hóa chất vào trong cơ thể chúng ta. Nó gây ra gốc tự do rất là lớn. Thế thì những cái gốc tự do đấy"

  Transcript 02:04:40–02:05:26 · [▶ watch from 02:04:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7480s)

  ```text
    [02:04:40] Thế thì uống đủ các loại thuốc cả kháng
    [02:04:43] sinh đủ các thứ nhưng cuối cùng không đỡ
    [02:04:45] thầy càng uống vào. Mà lúc nãy tôi có
    [02:04:48] nói trong cái gốc tự do. Một trong những
    [02:04:50] cái gốc tự do đó chính là một cái nguyên
    [02:04:52] nhân vô cùng quan trọng là chúng ta uống
    [02:04:54] quá nhiều thuốc vào.
  ▶ [02:04:55] >> Vâng. Đặc biệt là những cái thuốc giảm
  ▶ [02:04:57] đau. Thuốc giảm đau như paracetamol nó
  ▶ [02:04:59] hại tới gan đúng không ạ?
  ▶ [02:05:01] >> Thế rồi thì nó hại tới thận, hại tới tất
  ▶ [02:05:03] cả các nơi thì thuốc này nó sinh ra đây
  ▶ [02:05:06] là một cái hóa chất vào trong cơ thể
  ▶ [02:05:08] chúng ta. Nó gây ra gốc tự do rất là
  ▶ [02:05:10] lớn. Thế thì những cái gốc tự do đấy
    [02:05:13] chúng ta sẽ thấy rằng gì ạ? Thầy đau
    [02:05:15] xương hông. Tôi nhớ rằng ờ ví dụ như thế
    [02:05:18] này, có những người đau ở bên phần háng
    [02:05:20] ấy. Thế đến khi dần dần đi chụp ích
    [02:05:22] quang một ngày bắt đầu thấy hoại tử vô
    [02:05:24] khuẩn trỏm xương đùi, cuối cùng là phải
  ```

### c251

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:05:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7513s)  ·  section start [▶ 02:05:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7534s)  
**Summary section:** [02:05:39] Hoại tử chỏm xương đùi, bỏ thuốc lá và tuổi thọ  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt quy cho bác sĩ.

- **BEFORE (current summary):** Ông kể một bệnh nhân đau vùng háng, chụp thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải khoan giảm áp và thay khớp háng.
- **AFTER (proposed):** Bác sĩ nêu ví dụ có những người đau bên phần háng, dần dần đi chụp thì thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải "xuyên giảm áp" (bản ghi âm ghi như vậy) rồi thay cả khớp háng.
- **Why:** Population changed: he gives a general example ('có những người'), not one specific patient. The caption says 'xuyên giảm áp'; 'khoan' is the summary's word.
- **Pass-1 note:** Bác sĩ nói khái quát «có những người/những bệnh nhân», không kể một bệnh nhân cá biệt xác định như tóm tắt.
- **Pass-2 note (blind):** Doctor gives a generic illustrative example about 'những người' (plural); summary turns it into one specific patient
- **Surrounding summary claims:**
  - previous (c250): Khi được hỏi về paracetamol, bác sĩ cho rằng thuốc này có thể hại gan, và cũng hại thận và nhiều cơ quan khác, vì sinh ra một hóa chất gây gốc tự do rất lớn.
  - next (c252): Bệnh nhân này đang hút thuốc, khi chỉ dừng hút thuốc lá thì cơn đau đã giảm đi nhiều.
- **Quotes cited:**
  - [▶ 02:05:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7513s) "này, có những người đau ở bên phần háng ấy. Thế đến khi dần dần đi chụp ích quang một ngày bắt đầu thấy hoại tử vô khuẩn trỏm xương đùi, cuối cùng là phải"
  - [▶ 02:05:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7522s) "xuyên giảm áp, cuối cùng là phải thay cả khớp háng. Thế nhưng mà những bệnh nhân ấy chỉ cần yêu cầu gì thôi là đang hút"

  Transcript 02:05:03–02:05:52 · [▶ watch from 02:05:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7503s)

  ```text
    [02:05:03] cả các nơi thì thuốc này nó sinh ra đây
    [02:05:06] là một cái hóa chất vào trong cơ thể
    [02:05:08] chúng ta. Nó gây ra gốc tự do rất là
    [02:05:10] lớn. Thế thì những cái gốc tự do đấy
    [02:05:13] chúng ta sẽ thấy rằng gì ạ? Thầy đau
    [02:05:15] xương hông. Tôi nhớ rằng ờ ví dụ như thế
  ▶ [02:05:18] này, có những người đau ở bên phần háng
  ▶ [02:05:20] ấy. Thế đến khi dần dần đi chụp ích
  ▶ [02:05:22] quang một ngày bắt đầu thấy hoại tử vô
  ▶ [02:05:24] khuẩn trỏm xương đùi, cuối cùng là phải
  ▶ [02:05:27] xuyên giảm áp, cuối cùng là phải thay cả
  ▶ [02:05:29] khớp háng. Thế nhưng mà những bệnh nhân
  ▶ [02:05:31] ấy chỉ cần yêu cầu gì thôi là đang hút
    [02:05:33] thuốc lá chỉ cần có một động tác đó là
    [02:05:36] dừng hút thuốc lá lại nó đã giảm đau đi
    [02:05:38] rất nhiều.
    [02:05:39] >> Bởi vì lúc ấy tôi nói thuốc lá là gì ạ?
    [02:05:41] Thuốc lá gây gốc tự do rất nhiều,
    [02:05:44] >> rượu bia gây gốc tự do rất nhiều. Nếu
    [02:05:46] chúng ta lạm dụng chúng ta sai, chế độ
    [02:05:48] ăn uống sai. Thế rồi dùng những cái
    [02:05:49] thuốc này sai
    [02:05:50] >> chúng ta giảm đi nó đã thay đổi rất
    [02:05:52] nhiều. Tại sao tôi nói thuốc lá là giảm
  ```

### c252

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:05:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7524s)  ·  section start [▶ 02:05:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7534s)  
**Summary section:** [02:05:39] Hoại tử chỏm xương đùi, bỏ thuốc lá và tuổi thọ  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt quy cho bác sĩ.

- **BEFORE (current summary):** Bệnh nhân này đang hút thuốc, khi chỉ dừng hút thuốc lá thì cơn đau đã giảm đi nhiều.
- **AFTER (proposed):** Bác sĩ nói những bệnh nhân ấy, nếu đang hút thuốc lá, chỉ cần một động tác là dừng hút thuốc lá lại thì đã giảm đau đi rất nhiều.
- **Why:** Population changed: 'những bệnh nhân ấy ... chỉ cần' is a general statement, which the summary turns into an outcome for one patient.
- **Pass-1 note:** Chuyển ví dụ khái quát «những bệnh nhân ấy/chỉ cần» thành kết quả đã xảy ra ở một bệnh nhân cụ thể.
- **Pass-2 note (blind):** Content supported but population changed: 'những bệnh nhân ấy' (general group) becomes a single 'Bệnh nhân này'
- **Surrounding summary claims:**
  - previous (c251): Ông kể một bệnh nhân đau vùng háng, chụp thấy hoại tử vô khuẩn chỏm xương đùi, cuối cùng phải khoan giảm áp và thay khớp háng.
  - next (c253): Bác sĩ cũng nói thuốc lá, rượu bia, chế độ ăn sai và dùng thuốc sai đều gây nhiều gốc tự do, và cho biết mỗi điếu thuốc lá giảm đi 11 phút tuổi thọ.
- **Quotes cited:**
  - [▶ 02:05:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7524s) "khớp háng. Thế nhưng mà những bệnh nhân ấy chỉ cần yêu cầu gì thôi là đang hút thuốc lá chỉ cần có một động tác đó là"
  - [▶ 02:05:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7531s) "dừng hút thuốc lá lại nó đã giảm đau đi rất nhiều."

  Transcript 02:05:14–02:06:01 · [▶ watch from 02:05:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7514s)

  ```text
    [02:05:15] xương hông. Tôi nhớ rằng ờ ví dụ như thế
    [02:05:18] này, có những người đau ở bên phần háng
    [02:05:20] ấy. Thế đến khi dần dần đi chụp ích
    [02:05:22] quang một ngày bắt đầu thấy hoại tử vô
    [02:05:24] khuẩn trỏm xương đùi, cuối cùng là phải
    [02:05:27] xuyên giảm áp, cuối cùng là phải thay cả
  ▶ [02:05:29] khớp háng. Thế nhưng mà những bệnh nhân
  ▶ [02:05:31] ấy chỉ cần yêu cầu gì thôi là đang hút
  ▶ [02:05:33] thuốc lá chỉ cần có một động tác đó là
  ▶ [02:05:36] dừng hút thuốc lá lại nó đã giảm đau đi
  ▶ [02:05:38] rất nhiều.
    [02:05:39] >> Bởi vì lúc ấy tôi nói thuốc lá là gì ạ?
    [02:05:41] Thuốc lá gây gốc tự do rất nhiều,
    [02:05:44] >> rượu bia gây gốc tự do rất nhiều. Nếu
    [02:05:46] chúng ta lạm dụng chúng ta sai, chế độ
    [02:05:48] ăn uống sai. Thế rồi dùng những cái
    [02:05:49] thuốc này sai
    [02:05:50] >> chúng ta giảm đi nó đã thay đổi rất
    [02:05:52] nhiều. Tại sao tôi nói thuốc lá là giảm
    [02:05:54] đi mỗi điếu giảm đi 11 phút về thời gian
    [02:05:56] sống, về tuổi thọ. Chúng ta thấy rằng
    [02:05:58] con số nó rất lớn. chúng ta không thể
    [02:06:01] ngờ được rằng là những cái con số cụ thể
  ```

### c254

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 01:21:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4897s)  ·  section start [▶ 02:06:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7579s)  
**Summary section:** [02:06:24] Trường hợp chị Ngọc Thơ: vàng da, vàng củng mạc mắt và hemoglobin thấp  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Khánh Lành đọc bình luận; bác sĩ kể lại và đoán tên Ngọc Thơ.

- **BEFORE (current summary):** Chị Ngọc Thơ, theo bình luận được đọc trên chương trình, từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt, khiến chị xấu hổ và không dám chụp ảnh với ai.
- **AFTER (proposed):** Một người xem, theo bình luận được đọc trên chương trình (bác sĩ nói "tôi đoán là chị Ngọc Thơ" vì tài khoản không dấu), từ năm 2017 đến nay bị vàng da và vàng củng mạc mắt; bác sĩ kể lại chị xấu hổ, ngại ngùng, không dám chụp ảnh với ai.
- **Why:** Hedge dropped: the doctor guesses the name because the account has no diacritics. The summary states the name as fact.
- **Pass-1 note:** Nội dung có, nhưng tên Ngọc Thơ được bác sĩ nói «tôi đoán» vì tài khoản không dấu; tóm tắt bỏ mức bất định này.
- **Pass-2 note (blind):** Jaundice/scleral yellowing since 2017, shame and not daring to take photos all supported; doctor also cites general illness for the photo avoidance
- **Reconciliation:** The doctor guesses the commenter’s name (“tôi đoán”); the summary states Ngọc Thơ without that uncertainty. Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c253): Bác sĩ cũng nói thuốc lá, rượu bia, chế độ ăn sai và dùng thuốc sai đều gây nhiều gốc tự do, và cho biết mỗi điếu thuốc lá giảm đi 11 phút tuổi thọ.
  - next (c255): Xét nghiệm hemoglobin của chị luôn ở mức 10 đến 11 g/dL, trong khi bình thường là từ 12 đến 16 (có tài liệu lấy tới 17,5).
- **Quotes cited:**
  - [▶ 01:21:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4897s) "Tình trạng của em trước đây. Từ năm 2017 đến nay, da của em đặc biệt là lòng bàn tay, lòng bàn chân và da mặt, luôn bị vàng bợt, thiếu sức sống. Niêm mạc mắt"
  - [▶ 02:06:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7588s) "Ngọc hay là Ngọc Thơ? Tôi đoán là chị Ngọc Thơ không có dấu không có dấu cho nên tôi đoán là chị Ngọc Thơ. Thế thì chị Ngọc Thơ có bình"
  - [▶ 02:06:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7600s) "xấu hổ, chị ngại ngùng, không dám đi đâu, không dám chụp ảnh với ai vì rằng là cơ thể mình ốm yếu đã đành, mệt mỏi"

  Transcript 01:21:27–01:22:07 · [▶ watch from 01:21:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4887s)

  ```text
    [01:21:29] đội ngũ kỹ thuật có thể hiển thị
    [01:21:32] ờ tài khoản cùng các khán giả đã gửi
    [01:21:34] bình luận về cho chương trình như thế
    [01:21:35] này ạ.
    [01:21:37] Em xin phép được gửi vài dòng chia sẻ
    [01:21:39] tới bác sĩ và chương trình.
  ▶ [01:21:42] Tình trạng của em trước đây. Từ năm 2017
  ▶ [01:21:45] đến nay, da của em đặc biệt là lòng bàn
  ▶ [01:21:48] tay, lòng bàn chân và da mặt, luôn bị
  ▶ [01:21:50] vàng bợt, thiếu sức sống. Niêm mạc mắt
    [01:21:54] và miệng vàng như 50% màu nước cam. Mặc
    [01:21:58] dù hồi bé và trẻ em luôn có làn da trắng
    [01:22:00] hồng. Khi nói chuyện hay đi cầu thang,
    [01:22:03] em luôn bị hụt hơi. Người lúc nào cũng
    [01:22:06] thiếu lượng, mất tập trung, hay quên và
  ```

  Transcript 02:06:18–02:07:10 · [▶ watch from 02:06:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7578s)

  ```text
    [02:06:19] phân tử và tạo ra các gốc tự do. gốc tự
    [02:06:22] do nó tấn công cơ thể của chúng ta để
    [02:06:24] sinh ra rất nhiều những các cái bệnh tật
    [02:06:26] khác nhau. Tôi lấy ví dụ như là bình
    [02:06:29] luận thứ tám của một chị là gì ạ? Thơ
  ▶ [02:06:33] Ngọc hay là Ngọc Thơ? Tôi đoán là chị
  ▶ [02:06:35] Ngọc Thơ
  ▶ [02:06:36] >> không có dấu
  ▶ [02:06:37] >> không có dấu cho nên tôi đoán là chị
  ▶ [02:06:38] Ngọc Thơ. Thế thì chị Ngọc Thơ có bình
    [02:06:41] luận rằng là bao nhiêu năm trời đó chị
  ▶ [02:06:45] xấu hổ, chị ngại ngùng, không dám đi
  ▶ [02:06:48] đâu, không dám chụp ảnh với ai vì rằng
  ▶ [02:06:50] là cơ thể mình ốm yếu đã đành, mệt mỏi
    [02:06:52] rồi đủ thứ bệnh trên đời. Nhưng có một
    [02:06:55] cái mà làm cho chị rất là ngại ngùng,
    [02:06:58] rất là chán nản đó là gì ạ? Đó là vàng
    [02:07:00] da, vàng củng mạc mắt. Về chị ví rằng là
    [02:07:03] giảng cái mức vàng nó giống như 50% của
    [02:07:07] nước cam vắt ra.
    [02:07:08] >> Vâng. có nghĩa rằng là chúng ta vàng rất
    [02:07:09] nhiều đúng không ạ? Chị đi xét nghiệm
  ```

### c256

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s)  ·  section start [▶ 02:06:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7579s)  
**Summary section:** [02:06:24] Trường hợp chị Ngọc Thơ: vàng da, vàng củng mạc mắt và hemoglobin thấp  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Khán giả tự đặt nghi vấn; Khánh Lành đọc và bác sĩ thuật lại, không phải nghi vấn riêng của người dẫn.

- **BEFORE (current summary):** Người dẫn chương trình đặt nghi vấn chị đang bị thiếu máu nhược sắc do thiếu sắt, gây tan hồng cầu và vàng da.
- **AFTER (proposed):** Chị, người viết bình luận, tự cho rằng có lẽ mình thiếu sắt nhược sắc; bác sĩ thuật lại câu hỏi chị đặt ra là có phải thiếu máu nhược sắc do thiếu sắt gây tan hồng cầu và vàng da hay không.
- **Why:** Speaker misattributed: the viewer raises this question ('chị đặt ra'), not the host.
- **Pass-1 note:** Sai chủ thể đặt nghi vấn: chính người bình luận; giữ lời «có lẽ» và sự không chắc về tài liệu.
- **Pass-2 note (blind):** Speaker misattributed: the question is raised by the viewer ('chị đặt ra'), not posed by the host
- **Surrounding summary claims:**
  - previous (c255): Xét nghiệm hemoglobin của chị luôn ở mức 10 đến 11 g/dL, trong khi bình thường là từ 12 đến 16 (có tài liệu lấy tới 17,5).
  - next (c257): Sau khi bổ sung vi chất, theo bác sĩ, tình trạng của chị thay đổi hoàn toàn.
- **Quotes cited:**
  - [▶ 01:22:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4973s) "nhận ra có lẽ vấn đề nằm ở việc bị thiếu sắt nhược sắc."
  - [▶ 01:23:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4999s) "vàng. Nhưng em không rõ độ chính xác của thông tin này như thế nào. Em đã đi khám"
  - [▶ 02:07:41](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7656s) "này. Cuối cùng là cái vàng đó chị đặt ra một cái điều rất hay đó là có phải sau"
  - [▶ 02:07:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7671s) "thiếu máu nhược sắc do thiếu sắt và nó gây ra một cái hiện tượng là tan hồng cầu."

  Transcript 01:22:43–01:23:49 · [▶ watch from 01:22:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4963s)

  ```text
    [01:22:45] đến 11 g/dl.
    [01:22:48] So với khoảng tam chiếu là từ 12 đến 16.
    [01:22:51] nhưng không có bác sĩ nào đề cập hay là
    [01:22:53] lưu ý cả. Chỉ sau này khi theo dõi kênh
    [01:22:56] của bác sĩ Phúc và lụp lại hồ sơ, em mới
  ▶ [01:22:58] nhận ra có lẽ vấn đề nằm ở việc bị thiếu
  ▶ [01:23:02] sắt nhược sắc.
    [01:23:04] Do chế độ ăn của em đã quen kiểm soát
    [01:23:06] lượng ăn nên khi muốn cố ăn tăng số
    [01:23:10] lượng để thêm dinh dưỡng thì em ăn không
    [01:23:13] nổi.
    [01:23:14] Em có xem một số tài liệu nói rằng khi
    [01:23:16] thiếu sắt hồng cầu mỏng manh dễ bị phá
    [01:23:19] hủy hàng loạt và xác hồng cầu bị phá hủy
    [01:23:21] tồn tại trên bề mặt da làm da có ánh
  ▶ [01:23:24] vàng. Nhưng em không rõ độ chính xác của
  ▶ [01:23:27] thông tin này như thế nào. Em đã đi khám
    [01:23:30] khoảng năm bệnh viện phòng khám. và bác
    [01:23:33] sĩ bệnh viện tư. Em
    [01:23:37] nhận được câu trả lời luôn là họ thừa
    [01:23:40] nhận nhìn da của em vàng thật nhưng giải
    [01:23:43] thích đó là do cơ địa, do nguồn nước. Dù
    [01:23:47] em đã chuyển chỗ ở vài lần, nguồn nước
    [01:23:49] đã thay đổi nhưng vẫn không cải thiện.
  ```

  Transcript 02:07:26–02:08:21 · [▶ watch from 02:07:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7646s)

  ```text
    [02:07:26] đấy con số bình thường là phải từ bao
    [02:07:28] nhiêu? Từ 12 cho đến 16 đúng không ạ? Và
    [02:07:31] có những cái tài liệu có thể lấy tới
    [02:07:33] 17,5. Thế thì con số bình thường chị đưa
    [02:07:36] ra là từ 12 cho đến 16. Trong khi đó là
    [02:07:39] chị luôn luôn xét nghiệm ở cái mức thiếu
  ▶ [02:07:41] này. Cuối cùng là cái vàng đó chị đặt ra
  ▶ [02:07:45] một cái điều rất hay đó là có phải sau
    [02:07:49] khi tìm hiểu cũng như nghe trên kênh tìm
    [02:07:51] hiểu các tài liệu thì chị thấy rằng đây
    [02:07:53] chị đang rơi vào trường hợp là thiếu máu
    [02:07:55] thiếu sắt,
  ▶ [02:07:56] >> thiếu máu nhược sắc do thiếu sắt và nó
  ▶ [02:08:00] gây ra một cái hiện tượng là tan hồng
  ▶ [02:08:02] cầu. tan hồng cầu gây ra vàng da. Thế
    [02:08:05] rồi thì chị đặt cái câu hỏi là có phải
    [02:08:08] do ăn caroten mà dẫn tới là nó vàng da
    [02:08:11] các thứ như thế không? Chị cắt hoàn toàn
    [02:08:13] chế độ caroten vẫn không đủ. Thế nhưng
    [02:08:15] sau khi chị bổ sung vi chất thì thế nào
    [02:08:18] ạ? Thay đổi hoàn toàn.
    [02:08:19] >> Vâng. Các bệnh của chị đẩy lui hết, vàng
  ```

### c275

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:13:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8014s)  ·  section start [▶ 02:13:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8015s)  
**Summary section:** [02:13:40] Vitamin C, E, glutathion và các vi chất phối hợp với nhau  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ nói vitamin C/E và gợi tên; Khánh Lành đáp «Glutat».

- **BEFORE (current summary):** Người dẫn nói vitamin C và vitamin E cũng là các chất liên quan đến gốc tự do, và glutathion cũng vậy.
- **AFTER (proposed):** Trong đoạn bác sĩ nhắc lại ("lúc ấy tôi nói là gì ạ?"), bản ghi âm ghi "Vitamin C cũng là gốc tự do, vitamin E cũng là gốc tự do" (có dấu đổi người nói giữa câu), rồi nhắc đến glutathion đang nói hôm nay.
- **Why:** The doctor leads this recall, not the host. The caption says 'cũng là gốc tự do', which the summary softens to 'liên quan'. A speaker-change mark sits mid-sentence, so the speaker of that half needs a human check. The wording is kept as spoken with no correction.
- **Pass-1 note:** Sai người nói C/E: bác sĩ, không phải người dẫn; bản chép còn nói cụ thể «cũng là gốc tự do», không chỉ «liên quan».
- **Pass-2 note (blind):** Speaker attribution to host not clearly supported (doctor leads the recall); wording 'liên quan đến gốc tự do' rephrases 'cũng là gốc tự do'
- **Surrounding summary claims:**
  - previous (c274): Ông nói gốc tự do còn làm hỏng enzyme vì tấn công protein, và bổ sung vi chất có thể giúp chuyển hóa hoạt động trở lại.
  - next (c276): Bác sĩ xác nhận các chất này hiệp đồng với nhau.
- **Quotes cited:**
  - [▶ 02:13:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8014s) "quyết cái vấn đề gốc tự do. Lúc ấy tôi nói là gì ạ? Vitamin C cũng là gốc tự do, vitamin E cũng là gốc tự do đúng không ạ?"
  - [▶ 02:13:46](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8021s) "Gluten cái gì đấy? Glutat. Glutat mà chúng ta đang nói hôm nay"

  Transcript 02:13:24–02:14:11 · [▶ watch from 02:13:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8004s)

  ```text
    [02:13:26] đầu nó mù mờ, xương mờ. Trong khi đới
    [02:13:28] caroten không chuyển hóa được thì gây ra
    [02:13:30] vàng da, vàng mắt. Nhưng khi chị bổ sung
    [02:13:33] vi chất thì vi chất nó sẽ vực dậy cái hệ
    [02:13:36] thống tế bào của chị. Vi chất nó sẽ giải
  ▶ [02:13:39] quyết cái vấn đề gốc tự do. Lúc ấy tôi
  ▶ [02:13:40] nói là gì ạ? Vitamin C
  ▶ [02:13:42] >> cũng là gốc tự do, vitamin E cũng là gốc
  ▶ [02:13:45] tự do đúng không ạ?
  ▶ [02:13:46] >> Gluten cái gì đấy?
  ▶ [02:13:49] >> Glutat.
  ▶ [02:13:50] >> Glutat mà chúng ta đang nói hôm nay
    [02:13:52] licomen đúng không ạ? Vân vân. Tất cả
    [02:13:55] những cái đó là hiệp đồng với nhau. Chưa
    [02:13:56] kể những cái thành phần ví dụ sen
    [02:13:58] >> đúng không ạ? Thế rồi hôm trước tôi nói
    [02:14:00] rằng là
    [02:14:01] >> trong số trước đó là gì ạ? Bo thế rồi
    [02:14:03] thì gì ạ? Silic. Đây là những các cái
    [02:14:05] thành phần vô cùng quan trọng là ẩn ở
    [02:14:08] trong cái sản phẩm mình bổ sung ấy.
    [02:14:09] Người ta kê cho vào trong đấy. Thế thì
  ```

### c282

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 02:18:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8297s)  ·  section start [▶ 02:16:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8202s)  
**Summary section:** [02:16:47] Đau dây thần kinh số 5 và nang dưới nhện: quan điểm không mổ  
**Final class:** `attribution_qualification` (pass 1 `supported`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt quy cho bác sĩ (các ca bệnh do bác sĩ kể lại).

- **BEFORE (current summary):** Ông cho rằng đau có thể do gốc tự do tấn công thần kinh và cần tìm hướng khác.
- **AFTER (proposed):** Ông cho rằng với những đau đầu hay triệu chứng đó thì hãy đi tìm theo hướng khác; còn đau dây thần kinh số 5, đến giờ phút này ông cho rằng vẫn là nguyên nhân gốc tự do tấn công vào đây và gây tổn thương dây thần kinh số năm.
- **Why:** Added hedge: 'tôi cho rằng vẫn là nguyên nhân' has no 'có thể'. This follows the reconciliation rationale; the record's note is stale pass-1 text.
- **Pass-1 note:** Hướng tìm nguyên nhân khác và nhận định gốc tự do tấn công thần kinh đều có mặt.
- **Pass-2 note (blind):** BORDERLINE: hedge added/softened — doctor says 'tôi cho rằng vẫn là nguyên nhân gốc tự do' (no 'có thể'); summary says pain 'có thể do' free radicals. 'cần tìm hướng khác' is supported.
- **Reconciliation:** The source says “tôi cho rằng vẫn là nguyên nhân”; “có thể” is an added hedge. Final attribution/qualification.
- **Surrounding summary claims:**
  - previous (c281): Ông không đồng ý với việc mổ dẫn lưu vì bệnh nhân sẽ thêm một vết mổ không cần thiết.
  - next (c283): Bác sĩ nói trên thế giới thường chọc kim vào hạch ở lỗ bầu dục để bơm hóa chất diệt hạch, nhưng sau khi diệt, mặt có thể tê bì mất cảm giác, và theo tài liệu ông đọc thì khoảng hai năm sau có thể tái phát và đau hơn.
- **Quotes cited:**
  - [▶ 02:18:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8297s) "Và tôi cho rằng cái này nó do những cái đau đầu hay là những cái triệu chứng gì đó chúng ta hãy đi tìm theo cái hướng khác và dường như có những cái ẩn chứa phía sau. Thì đến bây giờ tôi thấy rằng"
  - [▶ 02:21:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8493s) "sao nó lại như thế? Đau dây thần kinh số 5 đến giờ phút này tôi cho rằng vẫn là nguyên nhân gốc tự do nó tấn công vào đây này. Gốc tự do nó tấn công vào đây và gây tổn thương dây thần kinh số năm."

  Transcript 02:18:07–02:18:47 · [▶ watch from 02:18:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8287s)

  ```text
    [02:18:09] các cái phim CT và phim cộng hường từ
    [02:18:11] con nang dưới nhện và người ta đang
    [02:18:13] chung sống hòa bình. Nếu chúng ta mà mổ
    [02:18:16] dẫn lưu như vậy thì vô tình bệnh nhân
    [02:18:18] lại thêm một cái vết mổ chứ không cần
    [02:18:20] thiết. Thì tôi có lập luận là như vậy.
  ▶ [02:18:22] Và tôi cho rằng cái này nó do những cái
  ▶ [02:18:25] đau đầu hay là những cái triệu chứng gì
  ▶ [02:18:26] đó chúng ta hãy đi tìm theo cái hướng
  ▶ [02:18:28] khác và dường như có những cái ẩn chứa
  ▶ [02:18:30] phía sau. Thì đến bây giờ tôi thấy rằng
    [02:18:33] như của chị Nhung chị nói rằng là tổn
    [02:18:37] thương dây thần kinh số 5 thế và khoang
    [02:18:39] dưới nhện của vùng tiểu não gây tổn
    [02:18:41] thương dây thần kinh số 5. Dây thần kinh
    [02:18:43] số 5 nó đi ở đây này. Nó đi chi nhánh
    [02:18:45] gì? Nhánh hàm trên, hàm dưới và nhánh ở
    [02:18:47] phía trên này nữa. Ba nhánh thế nhánh
  ```

  Transcript 02:21:23–02:22:03 · [▶ watch from 02:21:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8483s)

  ```text
    [02:21:25] cái gì nữa đâu ạ? người ta bảo chỉ còn
    [02:21:26] hơi hơi không đáng kể nữa thôi. Thế còn
    [02:21:29] có những người nói rằng khỏi sau khi bổ
    [02:21:32] sung vi chất xong chẳng còn thấy đau dây
    [02:21:33] thần kinh số năm đâu nữa và cuộc sống
    [02:21:35] trở nên vui vẻ thoải mái. Thế thì tại
  ▶ [02:21:38] sao nó lại như thế? Đau dây thần kinh số
  ▶ [02:21:40] 5 đến giờ phút này tôi cho rằng vẫn là
  ▶ [02:21:43] nguyên nhân gốc tự do nó tấn công vào
  ▶ [02:21:45] đây này. Gốc tự do nó tấn công vào đây
  ▶ [02:21:47] và gây tổn thương dây thần kinh số năm.
    [02:21:49] Còn chúng ta bổ sung vi chất và chúng ta
    [02:21:51] hiểu được cơ chế của nó ngày hôm nay
    [02:21:53] chúng ta đừng để rơi vào gốc tự do nó
    [02:21:54] quá nhiều như thế nữa thì tôi tin rằng
    [02:21:57] những người đau dây thần kinh số năm này
    [02:21:59] sẽ thoát. Cũng như thế chúng ta sẽ thấy
    [02:22:01] rằng như là bác Nhung đau nửa đầu thế
  ```

### c287

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:21:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8466s)  ·  section start [▶ 02:21:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8462s)  
**Summary section:** [02:21:07] Một số bệnh nhân đau dây thần kinh số 5 đỡ sau khi bổ sung vi chất  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt quy cho bác sĩ (các ca bệnh do bác sĩ kể lại).

- **BEFORE (current summary):** Theo bác sĩ, một số bệnh nhân đến bổ sung vi chất đúng và đủ thì cơn đau biến mất hẳn, có người đỡ 90 đến 95%, và số còn lại chỉ còn đau nhẹ không đáng kể.
- **AFTER (proposed):** Theo bác sĩ, sau khi những bệnh nhân đến bổ sung vi chất đúng và đủ thì có những người nói tự dưng hết hẳn, có những người đỡ được đến "8 90% 95%" và người ta bảo chỉ còn hơi hơi không đáng kể; có những người nói khỏi sau khi bổ sung vi chất.
- **Why:** Residual slight pain describes the same 90-95% group, not a separate 'số còn lại'. The patient-reported framing ('có những người nói') was dropped.
- **Pass-1 note:** Bỏ giới hạn lời kể “có những người”; “số còn lại” biến phần đau nhẹ còn sót ở người đỡ 90–95% thành kết quả của toàn bộ những bệnh nhân còn lại.
- **Pass-2 note (blind):** Residual slight pain describes the same 90–95% group, not a separate 'số còn lại'; patient-reported framing dropped; '8 90%' simplified
- **Surrounding summary claims:**
  - previous (c286): Ông cũng nói nhiều bệnh nhân đau dây thần kinh số 5 nghĩ đến việc kết thúc sớm cuộc đời.
  - next (c288): Ông cho rằng nguyên nhân vẫn là gốc tự do tấn công dây thần kinh số 5, và nếu hiểu cơ chế, tránh để gốc tự do tích tụ quá nhiều thì người bệnh có thể thoát khỏi cơn đau.
- **Quotes cited:**
  - [▶ 02:21:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8466s) "những bệnh nhân đến bổ sung vi chất đúng và đủ thì có những người nói tự dưng hết hẳn không còn đau dây thần kinh số năm nữa. Thế có những người đỡ được đến 8 90% 95%. Đỡ tới 90 95% là khỏi rồi. Còn"
  - [▶ 02:21:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8476s) "90% 95%. Đỡ tới 90 95% là khỏi rồi. Còn cái gì nữa đâu ạ? người ta bảo chỉ còn hơi hơi không đáng kể nữa thôi. Thế còn"
  - [▶ 02:21:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8484s) "có những người nói rằng khỏi sau khi bổ sung vi chất xong chẳng còn thấy đau dây thần kinh số năm đâu nữa và cuộc sống trở nên vui vẻ thoải mái. Thế thì tại"

  Transcript 02:20:56–02:21:54 · [▶ watch from 02:20:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8456s)

  ```text
    [02:20:56] người ta mất cảm giác hoặc người ta liệt
    [02:20:58] mặt nặng quá. Sau này nếu có tái phát
    [02:21:00] thì bắt đầu lại tiêm tiếp. Nó vẫn còn có
    [02:21:02] đất để mà tiêm để làm được nhưng mà vẫn
    [02:21:05] không ăn thua lắm. Nó cứ thời gian sau
    [02:21:07] lại tái phát. Nhưng kỳ lạ cái là sau khi
  ▶ [02:21:11] những bệnh nhân đến bổ sung vi chất đúng
  ▶ [02:21:13] và đủ thì có những người nói tự dưng hết
  ▶ [02:21:16] hẳn không còn đau dây thần kinh số năm
  ▶ [02:21:18] nữa. Thế có những người đỡ được đến 8
  ▶ [02:21:21] 90% 95%. Đỡ tới 90 95% là khỏi rồi. Còn
  ▶ [02:21:25] cái gì nữa đâu ạ? người ta bảo chỉ còn
  ▶ [02:21:26] hơi hơi không đáng kể nữa thôi. Thế còn
  ▶ [02:21:29] có những người nói rằng khỏi sau khi bổ
  ▶ [02:21:32] sung vi chất xong chẳng còn thấy đau dây
  ▶ [02:21:33] thần kinh số năm đâu nữa và cuộc sống
  ▶ [02:21:35] trở nên vui vẻ thoải mái. Thế thì tại
    [02:21:38] sao nó lại như thế? Đau dây thần kinh số
    [02:21:40] 5 đến giờ phút này tôi cho rằng vẫn là
    [02:21:43] nguyên nhân gốc tự do nó tấn công vào
    [02:21:45] đây này. Gốc tự do nó tấn công vào đây
    [02:21:47] và gây tổn thương dây thần kinh số năm.
    [02:21:49] Còn chúng ta bổ sung vi chất và chúng ta
    [02:21:51] hiểu được cơ chế của nó ngày hôm nay
    [02:21:53] chúng ta đừng để rơi vào gốc tự do nó
    [02:21:54] quá nhiều như thế nữa thì tôi tin rằng
  ```

### c291

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 02:22:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8564s)  ·  section start [▶ 02:22:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8516s)  
**Summary section:** [02:22:01] Đau nửa đầu của chị Nhung và tim nhanh: kết quả sau khi bổ sung vi chất  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt quy cho bác sĩ (các ca bệnh do bác sĩ kể lại).

- **BEFORE (current summary):** Chị ăn nhiều đồng để quên cơn đau nên cân nặng tăng nhanh.
- **AFTER (proposed):** Chị ăn đường vào để quên cơn đau nên cân nặng tăng nhanh.
- **Why:** Wrong substance: the transcript says 'đường' (sugar), the summary says 'đồng' (copper). 'Nhiều' is also not stated.
- **Pass-1 note:** Sai chất: transcript nói ăn đường, không phải ăn đồng.
- **Pass-2 note (blind):** Entity wrong: transcript says 'đường' (sugar); summary says 'đồng' (copper) — likely typo but materially different
- **Surrounding summary claims:**
  - previous (c290): Mỗi cơn kéo dài 3 đến 5 ngày, một tháng có vài cơn, phải nằm co ro, tránh ánh sáng, tiếng động và ăn uống.
  - next (c292): Uống đủ thuốc không đỡ, nhưng sau khi bổ sung vi chất, theo bác sĩ, chị thay đổi hoàn toàn, không còn đau nửa đầu và đau dây thần kinh số 5.
- **Quotes cited:**
  - [▶ 02:22:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8564s) "nỗi mà bắt đầu bác ăn đường vào để cho quên hết tất cả. Lấy cái ngọt ngào để che lấp đi tất cả những cái cơn đau này dẫn tới là cân nặng tăng lên vù vù. Thế"

  Transcript 02:22:34–02:23:14 · [▶ watch from 02:22:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8554s)

  ```text
    [02:22:34] đau bùng phát luôn luôn có một tư thế
    [02:22:35] bắt đầu mà nằm co ro và hai tay ôm đầu.
    [02:22:38] Tránh âm thanh tránh ánh sáng tránh
    [02:22:40] tiếng động tránh ăn uống. Mỗi một cơn
    [02:22:43] đau như thế 3 đến 5 ngày khủng khiếp.
    [02:22:45] Thế mà một tháng bác bị đến mấy cái cơn
    [02:22:47] đau như vậy còn gì là người nữa. Đau đến
  ▶ [02:22:49] nỗi mà bắt đầu bác ăn đường vào để cho
  ▶ [02:22:51] quên hết tất cả. Lấy cái ngọt ngào để
  ▶ [02:22:54] che lấp đi tất cả những cái cơn đau này
  ▶ [02:22:57] dẫn tới là cân nặng tăng lên vù vù. Thế
    [02:23:00] rồi thì đấy chị Ngân vâng tất cả mọi cái
    [02:23:03] từ chị Ngân cho đến chị Nhung chia sẻ
    [02:23:06] thì chúng ta đã thấy rằng sau khi bổ
    [02:23:08] sung vi chất nó thay đổi đi rất nhiều.
    [02:23:11] Nguyên nhân vì sao? Vì đó chính là gốc
    [02:23:13] tự do.
    [02:23:14] >> Vâng. ta tổn thương ở cấp độ tế bào, tổn
  ```

### c294

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 02:44:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9835s)  ·  section start [▶ 02:22:01](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8516s)  
**Summary section:** [02:22:01] Đau nửa đầu của chị Nhung và tim nhanh: kết quả sau khi bổ sung vi chất  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt quy cho bác sĩ (các ca bệnh do bác sĩ kể lại).

- **BEFORE (current summary):** Bác sĩ hướng dẫn trong vài tiếng đồng hồ, và sau đó chị bổ sung vi chất theo từng bước, nâng dần liều.
- **AFTER (proposed):** Bác sĩ hướng dẫn trong mấy tiếng đồng hồ ("4 năm tiếng đồng hồ" theo bản ghi âm) để bổ sung vi chất, và sau đó chị trải qua từng bước một, "cứ nâng cao nâng cao dần".
- **Why:** 'Liều' (dose) is added: 'nâng cao dần' is in a micronutrient context, but dose is not named.
- **Pass-1 note:** Thêm cụ thể “liều”: bác sĩ nói hướng dẫn 4–5 tiếng, từng bước “nâng cao nâng cao dần”, không xác định đó là nâng liều.
- **Pass-2 note (blind):** Several hours (4–5) of guidance and stepwise gradual increase supported
- **Reconciliation:** “Nâng cao dần” is in the micronutrient context but does not explicitly name dosage; the summary adds “liều.” Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c293): Trước đây nhịp tim của chị lên tới 170.
  - next (c295): Bác sĩ nói hiệu quả thay đổi rõ rệt.
- **Quotes cited:**
  - [▶ 02:44:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9835s) "nhưng mà sau đó ba mẹ con đến khám thì tôi đã hướng dẫn cho ngày đấy hướng dẫn mấy tiếng đồng hồ cơ 4 năm tiếng đồng hồ cơ. Vâng."
  - [▶ 02:44:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9842s) "Để mà bổ sung vi chất thì sau khi hướng dẫn tôi trải qua từng bước một cứ nâng cao nâng cao dần thì đã thấy rằng cái hiệu quả đã thay đổi ngoạn mục trông thấy. Và nếu chị mua được các cái vi"

  Transcript 02:43:45–02:44:32 · [▶ watch from 02:43:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=9825s)

  ```text
    [02:43:46] khi mà chị bổ sung thì chị sẽ thấy rằng
    [02:43:49] là thỉnh thoảng chỉ còn cái tình trạng
    [02:43:50] là nhịp tim chưa kiểm soát được hết về
    [02:43:53] tâm lý dẫn tới thỉnh thoảng có nhịp tim
    [02:43:55] nó lên tăng nhanh chứ còn trước đây là
    [02:43:57] chị rơi vào nhịp tim lên tới gì ạ? 170
  ▶ [02:44:00] nhưng mà sau đó ba mẹ con đến khám thì
  ▶ [02:44:02] tôi đã hướng dẫn cho ngày đấy hướng dẫn
  ▶ [02:44:04] mấy tiếng đồng hồ cơ 4 năm tiếng đồng hồ
  ▶ [02:44:06] cơ.
  ▶ [02:44:06] >> Vâng.
  ▶ [02:44:07] >> Để mà bổ sung vi chất thì sau khi hướng
  ▶ [02:44:09] dẫn tôi trải qua từng bước một cứ nâng
  ▶ [02:44:11] cao nâng cao dần thì đã thấy rằng cái
  ▶ [02:44:13] hiệu quả đã thay đổi ngoạn mục trông
  ▶ [02:44:15] thấy. Và nếu chị mua được các cái vi
    [02:44:18] chất tốt, vi chất đúng và chuẩn thì chị
    [02:44:20] sẽ bổ sung nó sẽ tốt lên rất nhiều. Thế
    [02:44:23] và đặc biệt là bình luận của bác điểm
    [02:44:27] cuối cùng đúng không? Bác thứ 10 đó là
    [02:44:29] bác có băn khoăn về cái câu chuyện là bổ
    [02:44:32] sung vitamin D
  ```

### c319

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 03:15:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11706s)  ·  section start [▶ 02:55:58](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10553s)  
**Summary section:** [02:55:58] Công thức máu của bác Lương Trắc Nghiên: MPV, MCV, MCH  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Khánh Lành đọc bản nhận xét của bác sĩ Trần Văn Phúc.

- **BEFORE (current summary):** Số lượng hồng cầu có thể chưa thấp đến mức thiếu máu cấp, nhưng cơ thể có thể đang thiếu máu chức năng và đói oxy.
- **AFTER (proposed):** Số lượng hồng cầu trên giấy tờ có thể chưa tụt xuống mức báo động của thiếu máu cấp tính, nhưng cơ thể bác đang ở tình trạng thiếu máu chức năng và đói oxy vô cùng trầm trọng.
- **Why:** Softened hedge: only the first half has 'có thể'. The review asserts functional anemia and oxygen hunger 'vô cùng trầm trọng'. The proposal restores that wording.
- **Pass-1 note:** Thêm hedge: bản nhận xét chỉ nói số lượng hồng cầu «có thể» chưa giảm tới thiếu máu cấp; thiếu máu chức năng và đói oxy được khẳng định, không nói «có thể đang».
- **Pass-2 note (blind):** Hedge added on second half: transcript asserts functional anemia/oxygen hunger 'vô cùng trầm trọng'; summary softens to 'có thể đang' and drops severity
- **Surrounding summary claims:**
  - previous (c318): MCV và MCH ở cận trên cho thấy hồng cầu to nhưng nhả oxy kém.
  - next (c320): Nhận xét cho rằng nguyên nhân là tủy xương kiệt quệ sau nhiều năm, cộng với hít bụi gỗ, khói thuốc và chế độ ăn thiếu đạm, thiếu vi chất.
- **Quotes cited:**
  - [▶ 03:15:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11706s) "Mặc dù số lượng hồng cầu trên giấy tờ có thể chưa tụt xuống đến mức báo động của thiếu máu cấp tính, nhưng cơ thể bác lại giơ vào tình trạng thiếu máu chức năng và đói oxy vô cùng trầm trọng."

  Transcript 03:14:56–03:15:36 · [▶ watch from 03:14:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11696s)

  ```text
    [03:14:57] hụt vi chất kéo dài, tủy xương đã tạo ra
    [03:15:01] những gã hồng cầu to xác nhưng vụng dại.
    [03:15:05] Vỏ tế bào mỏng dính và khả năng nhả oxy
    [03:15:08] cho các mô bị trạch nhịp.
  ▶ [03:15:11] Mặc dù số lượng hồng cầu trên giấy tờ có
  ▶ [03:15:13] thể chưa tụt xuống đến mức báo động của
  ▶ [03:15:15] thiếu máu cấp tính, nhưng cơ thể bác lại
  ▶ [03:15:18] giơ vào tình trạng thiếu máu chức năng
  ▶ [03:15:20] và đói oxy vô cùng trầm trọng.
    [03:15:25] Tất cả những rối loạn ấy bắt nguồn từ
    [03:15:27] đâu? Chúng là cái quả của một tủy xương
    [03:15:31] đã kiệt quệ sau những năm tháng tuổi trẻ
    [03:15:34] hít thở khói đạn bom nơi chiến trường.
  ```

### c333

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 03:19:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11965s)  ·  section start [▶ 02:57:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10628s)  
**Summary section:** [02:57:13] Axit uric 459,1 và cholesterol tăng ở người gầy  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Khánh Lành đọc nguyên văn bản nhận xét do bác sĩ Trần Văn Phúc viết; tóm tắt quy về phần nhận xét.

- **BEFORE (current summary):** Gan và thận thiếu vi chất nên giảm khả năng đào thải, và tinh thể urat có thể lắng đọng ở khớp và thành mạch, gây đau gút.
- **AFTER (proposed):** Gan và thận kiệt sức vì thiếu vi chất nên mất đi khả năng đào thải, và những tinh thể urat âm thầm đọng lại nơi khớp xương và thành mạch, đe dọa mang đến những cơn đau gút.
- **Why:** Hedges moved in both directions: 'mất đi' became 'giảm', 'đọng lại' became 'có thể lắng đọng', and 'đe dọa mang đến' hardened to 'gây'.
- **Pass-1 note:** Bỏ điều kiện nguy cơ: bản nhận xét nói tinh thể đọng lại và “Đe dọa mang đến” cơn đau gút; tóm tắt đổi thành “có thể lắng đọng” nhưng khẳng định “gây đau gút”.
- **Pass-2 note (blind):** Qualifications shifted: 'mất đi' softened to 'giảm'; definite 'âm thầm đọng lại' softened to 'có thể lắng đọng'; 'Đe dọa mang đến' (threat) hardened to 'gây đau gút'
- **Surrounding summary claims:**
  - previous (c332): Đường ruột viêm mạn tính làm không hấp thu được đạm, nên cơ thể tự phân hủy cơ bắp, giải phóng purin khiến axit uric tăng vọt.
  - next (c334): Bác sĩ nói người ta thường cho rằng axit uric cao là do béo, ăn nhiều đạm và mỡ, nhưng nhiều người rất gầy vẫn có mỡ máu và axit uric cao cùng chức năng gan có vấn đề.
- **Quotes cited:**
  - [▶ 03:19:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11965s) "tăng vọt. Trong khi đó, lá gan và quả thận đã kiệt sức vì thiếu vi chất nên mất đi khả năng đảo thải."
  - [▶ 03:19:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11974s) "Những tinh thể uras sắc nhọn như vô số mũi kim nhỏ âm thầm đọng lại nơi khấp xương và thành mạch. Đe dọa mang đến"
  - [▶ 03:19:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11982s) "những cơn đau gút, xé thịt, xé da như muốn bóc nghẹt thân thể vốn đã gầy gộc."

  Transcript 03:19:15–03:20:12 · [▶ watch from 03:19:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11955s)

  ```text
    [03:19:15] hủy chính các khối cơ bắc còn sót lại
    [03:19:18] trên bắp tay, bắp đùi để lấy năng lượng
    [03:19:21] sống.
    [03:19:23] Sự tan dã của nhân tế bào cơ bóc nội
    [03:19:25] sinh ấy giải phóng ra một lượng khổng lồ
    [03:19:27] nhân purin khiến axit uric trong máu
  ▶ [03:19:30] tăng vọt. Trong khi đó, lá gan và quả
  ▶ [03:19:34] thận đã kiệt sức vì thiếu vi chất nên
  ▶ [03:19:36] mất đi khả năng đảo thải.
  ▶ [03:19:39] Những tinh thể uras sắc nhọn như vô số
  ▶ [03:19:42] mũi kim nhỏ âm thầm đọng lại nơi khấp
  ▶ [03:19:45] xương và thành mạch. Đe dọa mang đến
  ▶ [03:19:47] những cơn đau gút, xé thịt, xé da như
  ▶ [03:19:50] muốn bóc nghẹt thân thể vốn đã gầy gộc.
    [03:19:56] Đặc biệt khi nhìn vào bức tranh chuyển
    [03:19:58] hóa sắt của bác, chúng ta sẽ thấy một
    [03:20:00] câu chuyện giao thông đầy trầm lắng và
    [03:20:03] trăn trở trong lòng mạch máu.
    [03:20:06] Để khán giả dễ hình dung, hãy tưởng
    [03:20:08] tượng hệ thống truyền hóa sắt như một
    [03:20:10] tuyến đường vận tải huyết mạch.
  ```

### c352

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 03:23:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12200s)  ·  section start [▶ 02:57:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10658s)  
**Summary section:** [02:57:43] Sắt, vitamin và khoáng chất: feritin, TSAT và biểu hiện thiếu sắt  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `supported`)  
**Speaker:** Khánh Lành đọc bản nhận xét sức khỏe của bác sĩ Trần Văn Phúc; tóm tắt quy về bản nhận xét/bác sĩ.

- **BEFORE (current summary):** Phần nhận xét nói kết hợp kho sắt đóng và lượng sắt lưu hành giảm không gây nguy hiểm đến tính mạng, nhưng làm chậm phân phối năng lượng tạo máu.
- **AFTER (proposed):** Phần nhận xét nói sự kết hợp giữa kho sắt đóng cửa với số lượng xe chở sắt bị sụt giảm không gây nguy cấp tử sinh, nhưng tạo nên sự trì trệ trong việc phân phối năng lượng tạo máu.
- **Why:** Entity changed: the number of iron-transport vehicles fell, not circulating iron, which the review says earlier has not run down.
- **Pass-1 note:** Bản nhận xét nói số xe chở sắt (transferrin) giảm, không phải lượng sắt lưu hành giảm; đoạn trước khẳng định sắt lưu hành chưa cạn kiệt.
- **Pass-2 note (blind):** Closed iron store + reduced circulating transport, not life-threatening, slows distribution — matches
- **Reconciliation:** The source says the number of iron-transport vehicles fell, not circulating iron itself. Final mismatch.
- **Surrounding summary claims:**
  - previous (c351): Feritin tăng nhẹ được giải thích là do protein phản ứng pha cấp, phản ứng tự vệ của cơ thể trước viêm mạn tính, và cơ thể đang giữ bớt sắt trong kho để ngăn vi khuẩn lợi dụng.
  - next (c353): Biểu hiện gồm mệt mỏi dai dẳng, sức bền giảm, hồi phục chậm sau mỗi đợt ốm hoặc đợt cấp COPD, và đôi lúc lồng ngực có cảm giác nén nặng.
- **Quotes cited:**
  - [▶ 03:23:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12200s) "Sự kết hợp giữa một kho sắt đóng mất cửa với số lượng xe trở sắt bị sụt giảm, không gây ra nguy cấp tử sinh nhưng nó"
  - [▶ 03:23:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12209s) "tạo nên một sự trì trệ [âm nhạc] trong việc phân phối năng lượng tạo máu."
  - [▶ 03:21:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12104s) "chứng minh rằng dẫu số lượng xe vận tải bị thu hệp, lượng sắt thực sự lưu hành trong dòng máu của bác vẫn đang giữ được sự nhịp nhàng, chưa hề bị rơi vào cảnh suy kiệt cạn kiệt."

  Transcript 03:21:34–03:22:14 · [▶ watch from 03:21:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12094s)

  ```text
    [03:21:36] [âm nhạc] tỉ lệ nằm hoàn toàn trong
    [03:21:37] ngưỡng an toàn và bình ổn của sinh học.
    [03:21:40] Ngưỡng bình thường dao động từ 20 đến
    [03:21:43] 50%.
    [03:21:45] Con số TSAT 28,84%
  ▶ [03:21:49] chứng minh rằng dẫu số lượng xe vận tải
  ▶ [03:21:52] bị thu hệp, lượng sắt thực sự lưu hành
  ▶ [03:21:55] trong dòng máu của bác vẫn đang giữ được
  ▶ [03:21:57] sự nhịp nhàng, chưa hề bị rơi vào cảnh
  ▶ [03:22:00] suy kiệt cạn kiệt.
    [03:22:04] Nhìn vào chỉ số feretin 428,1 ng/ml,
    [03:22:09] nếu chỉ thoáng qua, nhiều người có thể
    [03:22:12] vội vã lo sợ về một sự nhiễm độc hay ngộ
    [03:22:14] độc sắt lắng đọng nguy hiểm.
  ```

  Transcript 03:23:10–03:23:59 · [▶ watch from 03:23:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12190s)

  ```text
    [03:23:10] cho các tác nhân, viêm hay là vi khuẩn
    [03:23:13] có cơ hội lợi dụng nguyên liệu này để
    [03:23:15] [âm nhạc] phát triển. Vậy các chỉ số xét
    [03:23:18] nghiệm sắt này biểu hiện ra thành tình
    [03:23:20] trạng bệnh [âm nhạc] lý và triệu chứng
    [03:23:22] gì trên thực tế?
  ▶ [03:23:25] Sự kết hợp giữa một kho sắt đóng mất cửa
  ▶ [03:23:28] với số lượng xe trở sắt bị sụt giảm,
  ▶ [03:23:30] không gây ra nguy cấp tử sinh nhưng nó
  ▶ [03:23:34] tạo nên một sự trì trệ [âm nhạc] trong
  ▶ [03:23:36] việc phân phối năng lượng tạo máu.
    [03:23:39] Biểu hiện lâm sàng của nó là nỗi mệt
    [03:23:41] mỏi, u hoài day dẳng, bò dọc thân thể,
    [03:23:44] sự dẻo dai bị bào mòn, sức hồi phục sau
    [03:23:47] mỗi đợt ốm hay đợt cấp
    [03:23:50] và COPD tức là viêm phổi tắc nghẽn mạn
    [03:23:53] tính. bị chậm lại và lồng ngực đôi lúc
    [03:23:56] thấy nén nặng như có ngọn gió lạnh đi
    [03:23:59] qua.
  ```

### c373

**Decisions:** D5, D11 (correction approval)  
**Watch:** [▶ 03:24:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12270s)  ·  section start [▶ 03:24:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12238s)  
**Summary section:** [03:24:03] Kẽm, đồng và canxi ion hóa: đọc kết quả và triệu chứng thiếu kẽm  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Khánh Lành đọc bản nhận xét sức khỏe của bác sĩ Trần Văn Phúc; tóm tắt quy về bản nhận xét/bác sĩ.

- **BEFORE (current summary):** Transcript cho rằng những thiếu hụt này xuất hiện sau nhiều thập kỷ hút thuốc lá và thiếu vi chất.
- **AFTER (proposed):** Transcript nói kẽm và đồng dường như đã cạn kiệt sau hàng thập kỷ bác sống trong khói thuốc lá và thiếu hụt vi chất.
- **Why:** Hedge dropped: 'dường như' was removed, and the statement covers zinc and copper only, while 'những thiếu hụt này' also takes in ionized calcium.
- **Pass-1 note:** Bỏ dè dặt "dường như" khi khẳng định các thiếu hụt xuất hiện sau nhiều thập kỷ; bản gốc ví kẽm và đồng dường như đã cạn kiệt.
- **Pass-2 note (blind):** Hedge 'dường như' dropped; transcript applies this to kẽm và đồng only, while 'những thiếu hụt này' may also cover canxi ion
- **Surrounding summary claims:**
  - previous (c372): Người bệnh có thể khó tiêu, mất cảm giác ngon miệng, tóc dễ rụng, da khô ráp và khả năng tự lành vết thương bị suy giảm.
  - next (c374): Theo bác sĩ, điều đáng bận tâm hơn nằm ở ngọn lửa viêm mạn tính.
- **Quotes cited:**
  - [▶ 03:24:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12270s) "xương lành dường như đã cạn kiệt sau hàng thập kỷ bác sống trong khói thuốc lá và thiếu hụt vi chất."
  - [▶ 03:24:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12264s) "Kẽm và đồng chính là những người thợ sửa [âm nhạc] chữa tí hon."

  Transcript 03:24:14–03:25:00 · [▶ watch from 03:24:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12254s)

  ```text
    [03:24:15] 68,2 tham chiếu từ 70 đến 140
    [03:24:20] và canxi yông hóa giảm nhẹ xuống 1,15
    [03:24:24] tham chiếu từ 1,17 đến 1,29.
    [03:24:27] [âm nhạc]
  ▶ [03:24:29] Kẽm và đồng chính là những người thợ sửa
  ▶ [03:24:32] [âm nhạc] chữa tí hon. Là những giọt
  ▶ [03:24:35] xương lành dường như đã cạn kiệt sau
  ▶ [03:24:37] hàng thập kỷ bác sống trong khói thuốc
  ▶ [03:24:39] lá và thiếu hụt vi chất.
    [03:24:43] Thiếu kẽm khiến niêm mạc ruột bị dò rỉ,
    [03:24:46] gây ra bệnh viêm đường ruột kéo dài, làm
    [03:24:49] bác ăn uống khó tiêu, mất cảm giác ngon
    [03:24:51] miệng, tóc điểm xương dễ rụng, da rẻ khô
    [03:24:55] rác và khả năng tự lành vết thương bị
    [03:24:57] suy giảm.
    [03:25:00] Như vậy, điều đáng bận tâm của bác không
  ```

### c377

**Decisions:** D4, D8, D11 (correction approval)  
**Watch:** [▶ 03:25:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12338s)  ·  section start [▶ 03:25:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12312s)  
**Summary section:** [03:25:17] Vitamin B12 838,9: có đáng lo không và các nguyên nhân tăng giả  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Khánh Lành đọc bản nhận xét do bác sĩ Trần Văn Phúc viết; tóm tắt quy nội dung cho bác sĩ.

- **BEFORE (current summary):** Ông so sánh với quy chuẩn của một số nước phát triển như Nhật Bản, nơi giới hạn trên có thể được mở rộng lên 1000 hoặc thậm chí 1500 pg/ml, và cho rằng con số của bác vẫn nằm trong ngưỡng an toàn.
- **AFTER (proposed):** Ông so sánh với quy chuẩn tham chiếu của nhiều quốc gia phát triển như "bản" (bản ghi âm ghi như vậy), nơi giới hạn trên thường được mở rộng lên tới 1000 hoặc thậm chí 1500 pg/ml, và cho rằng con số của bác vẫn hoàn toàn nằm trong ngưỡng an toàn.
- **Why:** The caption says 'như bản'; naming Japan is not safely grounded in it. 'Nhiều' and 'thường' were also softened to 'một số' and 'có thể'. Human to confirm the country from the audio.
- **Pass-1 note:** Các ngưỡng 1000/1500 và kết luận an toàn có mặt; transcript chỉ ghi “như bản”, không xác định rõ tên Nhật Bản như bản tóm tắt.
- **Pass-2 note (blind):** Values and conclusion match; minor hedge shifts ('nhiều'→'một số', 'thường'→'có thể') judged non-material; 'bản' is a garbled 'Nhật Bản'
- **Reconciliation:** The transcript caption says “như bản”; identifying Japan and adjusting “many/usually” to “some/could” is not safely grounded in that wording. Retain qualification issue.
- **Surrounding summary claims:**
  - previous (c376): Bác sĩ nói rằng nhiều người có thể hoảng khi thấy chỉ số này cao, nhưng theo góc nhìn y khoa hiện đại thì đây là chỉ số cần được hiểu một cách điềm tĩnh.
  - next (c378): Theo transcript, các bác sĩ chỉ thực sự lo khi vitamin B12 giảm nặng, gây thiếu máu và tổn thương thần kinh.
- **Quotes cited:**
  - [▶ 03:25:43](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12338s) "Nếu so sánh với quy chuẩn tham chiếu của nhiều quốc gia phát triển như bản, nơi giới hạn trên của vitamin P12 thường được mở rộng lên tới 1000 picog"
  - [▶ 03:25:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12348s) "[âm nhạc] ml hoặc thậm chí là 1500 thì con số của bác vẫn hoàn toàn nằm trong ngưỡng an toàn của cơ thể."

  Transcript 03:25:28–03:26:18 · [▶ watch from 03:25:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12328s)

  ```text
    [03:25:30] mình cho rằng chỉ số này đang tăng cao
    [03:25:32] nguy hiểm.
    [03:25:34] Nhưng đứng dưới góc nhìn y khoa hiện đại
    [03:25:35] [âm nhạc] và chăm sóc sức khỏe toàn
    [03:25:37] diện, đây lại là một chỉ số cần được
    [03:25:39] thấu hiểu bằng sự điềm tĩnh và thấu đáo.
  ▶ [03:25:43] Nếu so sánh với quy chuẩn tham chiếu của
  ▶ [03:25:44] nhiều quốc gia phát triển như bản, nơi
  ▶ [03:25:47] giới hạn trên của vitamin P12 thường
  ▶ [03:25:50] được mở rộng lên tới 1000 picog
  ▶ [03:25:53] [âm nhạc] ml hoặc thậm chí là 1500 thì
  ▶ [03:25:57] con số của bác vẫn hoàn toàn nằm trong
  ▶ [03:25:59] ngưỡng an toàn của cơ thể.
    [03:26:02] Trong thực tế lâm sàng, các bác sĩ chỉ
    [03:26:04] thực sự lo lắng khi vitamin B12 bị sụt
    [03:26:07] giảm nặng nề, gây ra thiếu máu và tổn
    [03:26:09] thương thần kinh.
    [03:26:12] Chứ hiếm khi bận tâm khi chỉ số này tăng
    [03:26:14] nhẹ, thậm chí tăng gấp rưỡi, gấp đôi. Lý
    [03:26:17] do là bởi vitamin B12 thuộc nhóm vitamin
  ```

### c401

**Decisions:** D9, D11 (correction approval)  
**Watch:** [▶ 04:09:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14987s)  ·  section start [▶ 03:36:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13003s)  
**Summary section:** [03:36:48] Học lại cách thở và các kỹ thuật thở cho bác Nghiên  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Bác sĩ Trần Văn Phúc trực tiếp nói; phù hợp quy thuộc bác sĩ trong tóm tắt.

- **BEFORE (current summary):** Bác có thể bắt đầu với việc nín thở khoảng 1 đến 1,5 giây, và nếu nhịn được 10 hoặc 15 giây thì chỉ giảm xuống khoảng 8 đến 9 giây để giữ an toàn.
- **AFTER (proposed):** Bác có thể tập thở đơn giản theo "1 1,5", tức là cố gắng kéo dài thì sau ra một chút để đẩy khí cạn ra, tuyệt đối không cố gắng; và nếu nhịn được 15 giây, 10 giây thì chỉ giảm xuống độ 8, 9 giây để giữ an toàn.
- **Why:** Safety-relevant: '1 1,5' is about lengthening the later phase of the breath, not holding the breath for 1 to 1.5 seconds. A reader could follow the current text wrongly. The 8-9 second part matches.
- **Pass-1 note:** 1–1,5 là nhịp thở/kéo dài thì thở ra, không phải thời gian nín thở 1–1,5 giây; phần giảm xuống 8–9 giây có trong lời nói.
- **Pass-2 note (blind):** '1 1,5' is an inhale:exhale ratio (lengthen the exhale), not breath-holding for 1–1.5 seconds; second half (10–15 s → 8–9 s) supported
- **Surrounding summary claims:**
  - previous (c400): Bác sĩ nói không nên cố quá.
  - next (c402): Sau đó nâng dần lên nhịp 1, rồi 3, rồi 4-7-8.
- **Quotes cited:**
  - [▶ 04:09:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14987s) "thế này thôi. Chỉ là 1 1,5 thôi đã đã là quý rồi. 1 1,5 tức là ta cố gắng là kéo dài cái thì sau ra một chút để ta đẩy"
  - [▶ 04:09:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14994s) "dài cái thì sau ra một chút để ta đẩy được các cái khí cạn ra. Nhưng bác tuyệt đối không cố gắng bởi vì nếu cố quá nó sẽ thành ra là nguy hiểm. Vì sao? Vì sức"
  - [▶ 04:10:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15006s) "lẽ ra nếu bác thở bác nhịn được chẳng hạn như là 15 giây, 10 giây chẳng hạn thì bác chỉ giảm xuống độ 8 9 giây thôi để giữ cái an toàn như mình đã. Thế thì"
  - [▶ 04:10:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15013s) "Thế thì có thể không cần thiết là bác phải thở 1 luôn mà bác có thể chở thở 1 1,5 thôi đã."

  Transcript 04:09:37–04:10:43 · [▶ watch from 04:09:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14977s)

  ```text
    [04:09:37] chúng ta sống buông đi tất cả những cái
    [04:09:39] muộn phiền đó và hướng tới một cái tương
    [04:09:41] lai tốt đẹp. Tiếp nữa là một trong những
    [04:09:44] cái bí quyết đó chính là bác tập thở.
    [04:09:47] Thì bác tập thở những cái bài mà thở
    [04:09:49] trong đấy tôi nói là cũng hơi khó một
    [04:09:50] chút. Có thể đơn giản bác chỉ tập thở
  ▶ [04:09:52] thế này thôi. Chỉ là 1 1,5 thôi đã đã là
  ▶ [04:09:55] quý rồi. 1 1,5 tức là ta cố gắng là kéo
  ▶ [04:09:59] dài cái thì sau ra một chút để ta đẩy
  ▶ [04:10:01] được các cái khí cạn ra. Nhưng bác tuyệt
  ▶ [04:10:03] đối không cố gắng bởi vì nếu cố quá nó
  ▶ [04:10:06] sẽ thành ra là nguy hiểm. Vì sao? Vì sức
    [04:10:08] bác đang rất yếu, bác phải từ từ. Đáng
  ▶ [04:10:11] lẽ ra nếu bác thở bác nhịn được chẳng
  ▶ [04:10:13] hạn như là 15 giây, 10 giây chẳng hạn
  ▶ [04:10:16] thì bác chỉ giảm xuống độ 8 9 giây thôi
  ▶ [04:10:18] để giữ cái an toàn như mình đã. Thế thì
  ▶ [04:10:21] có thể không cần thiết là bác phải thở 1
  ▶ [04:10:24] luôn mà bác có thể chở thở 1 1,5 thôi
  ▶ [04:10:26] đã. Thế xong cứ nâng dần lên 1 xong thở
    [04:10:29] đến ba thì xong bắt đầu dần dần thở đến
    [04:10:31] 478 thì hơi thở là cái rất quan trọng để
    [04:10:34] bác lập lại tất cả những các cái đường
    [04:10:36] thở của mình. Sau khi những các cái hơi
    [04:10:39] thở đấy rồi thì một cái nền tảng vô cùng
    [04:10:41] quan trọng đó chính là bổ sung vi chất.
  ```

### c407

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 04:10:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15051s)  ·  section start [▶ 03:38:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13125s)  
**Summary section:** [03:38:50] Bảy nhóm vi chất, danh sách theo thứ tự và thời gian phục hồi  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Bác sĩ Trần Văn Phúc trực tiếp nói; phù hợp quy thuộc bác sĩ trong tóm tắt.

- **BEFORE (current summary):** Bác sĩ nói đầu tiên là magie, rồi kẽm, canxi, vitamin D3, vitamin tổng hợp (đặc biệt nhóm B), vitamin C và cuối cùng là omega 3.
- **AFTER (proposed):** Bác sĩ nói đầu tiên là magie, rồi canxi, vitamin D3, vitamin tổng hợp (đặc biệt nhóm B), vitamin C, kẽm và cuối cùng là omega 3.
- **Why:** Order wrong: zinc comes after vitamin C. The early mention of zinc is an aside about cofactors, not a list position.
- **Pass-1 note:** Sai thứ tự: bác sĩ nêu magie rồi canxi, D3; kẽm ở đoạn đầu là ví dụ các yếu tố hiệp đồng, còn danh sách đặt kẽm sau vitamin C, trước omega 3.
- **Pass-2 note (blind):** Order wrong: doctor lists magie, canxi, vitamin D3, vitamin tổng hợp (nhóm B), vitamin C, kẽm, omega 3; summary puts kẽm second
- **Surrounding summary claims:**
  - previous (c406): Bác sĩ nhấn mạnh đây không phải những viên thuốc rời rạc mà là một tập hợp các viên gạch sinh học.
  - next (c408): Ông gọi canxi, D3 và magie là "bộ ba tam giác vàng".
- **Quotes cited:**
  - [▶ 04:10:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15051s) "sung thì những cái gì. Đó là đầu tiên là cái mag rất quan trọng mà lúc nãy tôi vừa mới nói đó là chúng ta ma kẽm cen vân vân các thứ nếu chúng ta không có đủ"
  - [▶ 04:11:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15069s) "gì hết cả. Chân ma là rất quan trọng. Sau đó đến gì ạ? Đến canxi. Xong đến vitamin D3 đúng không ạ? Thì đây chính là bộ ba tam giác vàng. Tiếp theo nữa là"
  - [▶ 04:11:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15104s) "vitamin C xong tiếp nữa là đến gì ạ? Đến kẽm mà lúc đấy tôi vừa nói xong cuối cùng là gì ạ? Omega 3 thì chúng ta phải"
  - [▶ 04:11:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15076s) "Tiếp theo nữa là vitamin gì ạ? Vitamin tổng hợp."

  Transcript 04:10:41–04:12:14 · [▶ watch from 04:10:41](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15041s)

  ```text
    [04:10:41] quan trọng đó chính là bổ sung vi chất.
    [04:10:44] Bác kiểu gì bác cũng phải mua được vi
    [04:10:45] chất thật tốt và bổ sung cho nó thật là
    [04:10:48] đầy đủ. Thế thì vi chất tốt đầy đủ thì
    [04:10:50] tôi vẫn nhắc đi nhắc lại trong tất cả
    [04:10:52] các số rồi mà rất rất nhiều người vẫn
    [04:10:54] bình luận trên kênh hỏi rằng vi chất bổ
  ▶ [04:10:56] sung thì những cái gì. Đó là đầu tiên là
  ▶ [04:10:58] cái mag rất quan trọng mà lúc nãy tôi
  ▶ [04:11:00] vừa mới nói đó là chúng ta ma kẽm cen
  ▶ [04:11:04] vân vân các thứ nếu chúng ta không có đủ
    [04:11:06] thì tất cả những chất oxy hóa, những các
    [04:11:09] cái chống gốc tự do của chúng ta cũng
    [04:11:12] đều vô nghĩa hết. Nó cũng chẳng ý nghĩa
  ▶ [04:11:14] gì hết cả. Chân ma là rất quan trọng.
  ▶ [04:11:16] Sau đó đến gì ạ? Đến canxi. Xong đến
  ▶ [04:11:19] vitamin D3 đúng không ạ? Thì đây chính
  ▶ [04:11:21] là bộ ba tam giác vàng. Tiếp theo nữa là
  ▶ [04:11:23] vitamin gì ạ? Vitamin tổng hợp. Vitamin
    [04:11:26] tổng hợp quá quan trọng trong cuộc sống
    [04:11:29] của chúng ta mà nếu chúng ta không bổ
    [04:11:31] sung đủ đặc biệt là nhóm B thì chúng ta
    [04:11:33] sẽ thảm họa. Tiếp theo nữa là vitamin gì
    [04:11:36] ạ? Vitamin C.
    [04:11:37] >> Và vitamin C lúc ấy tôi nói rồi C này
    [04:11:39] thế rồi kẽm này, thế rồi gì? E này thế
    [04:11:42] rồi sen này không có thì chủ đề ngày hôm
    [04:11:44] nay sẽ thành vô nghĩa.
    [04:11:45] >> Vâng.
    [04:11:46] >> Nó hiệp đồng với nhau không thể nào
    [04:11:48] thiếu được những cái thành phần này. Vậy
  ▶ [04:11:49] vitamin C xong tiếp nữa là đến gì ạ? Đến
  ▶ [04:11:52] kẽm mà lúc đấy tôi vừa nói xong cuối
  ▶ [04:11:54] cùng là gì ạ? Omega 3 thì chúng ta phải
    [04:11:56] nhớ rằng bổ sung đầy đủ những các cái vi
    [04:11:59] chất này thì lúc đó chúng ta mới có được
    [04:12:01] cái sức khỏe thực sự, thân khỏe, tâm an
    [04:12:03] và trí sáng. Và tôi tin rằng là trong
    [04:12:07] cái bệnh phổi tắc nghẽn mán tính của bác
    [04:12:09] ấy bị như thế này thì cơ thể nó rất mệt
    [04:12:11] mỏi và nó suy sụp rất nhanh. Nhưng nếu
    [04:12:14] bác làm được theo tôi hướng dẫn, tôi tin
  ```

### c447

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 04:12:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15163s)  ·  section start [▶ 04:13:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15184s)  
**Summary section:** [04:13:09] Glutathione là chủ đề của ngày hôm nay và được truyền thông mô tả thế nào  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc; phù hợp quy thuộc trong tóm tắt.

- **BEFORE (current summary):** Ông cũng nhắc rằng ngoài bảy nhóm vi chất còn có khoảng 18 sản phẩm thuộc các nhóm này, cùng các thành phần khác như vitamin B7, B8, bo, silic và glutathione.
- **AFTER (proposed):** Ông cũng nhấn mạnh rằng trong bảy nhóm vi chất phải ít nhất có 18 sản phẩm, chưa kể những sản phẩm phải thêm như vitamin B7, B8, bo, silic, và hôm nay là glutathion.
- **Why:** Threshold changed: 'phải ít nhất có 18' (at least) became 'khoảng 18' (about).
- **Pass-1 note:** Đổi ngưỡng bắt buộc “phải ít nhất có 18” thành ước lượng “khoảng 18”, làm mất giới hạn tối thiểu.
- **Pass-2 note (blind):** Qualifier changed: 'ít nhất 18' (at least) rendered as 'khoảng 18' (about)
- **Surrounding summary claims:**
  - previous (c446): Bác sĩ nói chủ đề chính của buổi hôm nay là giúp bác Nghiên hiểu sâu về gốc tự do và khắc phục gốc tự do bằng glutathione.
  - next (c448): Theo phần giới thiệu của chương trình, glutathion là cái tên xuất hiện nhiều gần đây, được truyền miệng gọi là hoạt chất vàng cho làn da tươi sáng, được coi là thần dược để gan giải độc, và là bí quyết giữ tuổi thanh xuân.
- **Quotes cited:**
  - [▶ 04:12:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15163s) "cái vi chất này là bảy cái nhóm cơ bản nhưng mà đến giờ Giờ phút này thì tôi vẫn nhấn mạnh là chúng ta phải ít nhất có 18 cái sản phẩm đúng không ạ? 18 sản phẩm nằm trong bảy nhóm này. Chưa kể"
  - [▶ 04:12:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15174s) "những các cái sản phẩm mà chúng ta phải thêm đó là vitamin B7, nào là vitamin B8 đúng không ạ? Nào là bo, nào là silic. Hôm nay chúng ta lại đến Glutathion đúng"

  Transcript 04:12:33–04:13:24 · [▶ watch from 04:12:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15153s)

  ```text
    [04:12:33] phải bổ sung vi chất thật tốt cộng với
    [04:12:35] lại tập thở thật tốt giải phóng những
    [04:12:37] cái vấn đề tinh thần để nó hồi phục lại
    [04:12:39] những các cái phổi của chúng ta còn nếu
    [04:12:41] không thì chúng ta chỉ càng ngày nó càng
    [04:12:43] đẩy xấu đi cái tình trạng của chúng ta
    [04:12:45] nó xấu đi rất nhiều thì vai trò của các
  ▶ [04:12:48] cái vi chất này là bảy cái nhóm cơ bản
  ▶ [04:12:51] nhưng mà đến giờ Giờ phút này thì tôi
  ▶ [04:12:52] vẫn nhấn mạnh là chúng ta phải ít nhất
  ▶ [04:12:54] có 18 cái sản phẩm đúng không ạ? 18 sản
  ▶ [04:12:57] phẩm nằm trong bảy nhóm này. Chưa kể
  ▶ [04:12:59] những các cái sản phẩm mà chúng ta phải
  ▶ [04:13:01] thêm đó là vitamin B7, nào là vitamin B8
  ▶ [04:13:05] đúng không ạ? Nào là bo, nào là silic.
  ▶ [04:13:09] Hôm nay chúng ta lại đến Glutathion đúng
    [04:13:11] không ạ? Tới này chúng ta lại làm một
    [04:13:13] loạt các cái thành phần khác nữa. Còn vô
    [04:13:15] cùng nhiều cái khác nữa cơ mà. Tôi đang
    [04:13:17] hướng tới là gì? Đến cái bước tiếp theo
    [04:13:19] là 45 xong đến gì ạ? 60 vi chất. Tôi cứ
    [04:13:23] nâng nâng dần lên các cái thành phần như
  ```

### c449

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 04:17:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15457s)  ·  section start [▶ 04:13:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15184s)  
**Summary section:** [04:13:09] Glutathione là chủ đề của ngày hôm nay và được truyền thông mô tả thế nào  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Khánh Lành; tóm tắt gán nhầm cho bác sĩ Trần Văn Phúc.

- **BEFORE (current summary):** Bác sĩ nói những lời truyền miệng này "hào nhoáng" và cần nhìn lại dưới góc nhìn y khoa.
- **AFTER (proposed):** Khánh Lành, trong phần giới thiệu, nói đằng sau những lời truyền miệng hào nhoáng ấy, báo chí và truyền thông cũng ghi nhận không ít những khoảng tối, và đặt câu hỏi glutathion thực sự là gì dưới góc nhìn y khoa.
- **Why:** Speaker misattributed: both lines are Khánh Lành's segment intro, before the host invites the doctor to speak.
- **Pass-1 note:** Sai người nói: lời “hào nhoáng” và câu hỏi góc nhìn y khoa là Khánh Lành, không phải bác sĩ.
- **Pass-2 note (blind):** Speaker misattributed: 'hào nhoáng' and the call for a medical view come from Khánh Lành's segment intro
- **Surrounding summary claims:**
  - previous (c448): Theo phần giới thiệu của chương trình, glutathion là cái tên xuất hiện nhiều gần đây, được truyền miệng gọi là hoạt chất vàng cho làn da tươi sáng, được coi là thần dược để gan giải độc, và là bí quyết giữ tuổi thanh xuân.
  - next (c450): Phần giới thiệu nêu một số trường hợp: lạm dụng đường thô hoặc thực phẩm ngọt để chữa lành nhanh, dẫn đến hoảng sợ về ban đêm, nhịp tim dồn dập đến 170 lần một phút, hoặc làn da vàng bợt héo hon.
- **Quotes cited:**
  - [▶ 04:17:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15457s) "Vâng. Thế nhưng đằng sau những lời chuyển miệng hào nhoáng ấy, báo chí và truyền thông cũng ghi nhận không ít những khoảng tối hoang mang. Đó là gì ạ?"
  - [▶ 04:18:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15510s) "Vậy glutathe thực sự là gì dưới góc nhìn y khoa chân chính? Và tại sao sự thiếu"
  - [▶ 04:18:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15528s) "Khánh Lành xin kính mời bác sĩ Phúc"

  Transcript 04:17:27–04:18:07 · [▶ watch from 04:17:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15447s)

  ```text
    [04:17:27] thời gian gần đây. Người ta truyền tay
    [04:17:29] nhau gọi đây là hoạt chất vàng
    [04:17:33] cho làn da tươi sáng, là thần dược để
    [04:17:36] gan có thể dài độc hay là bí quyết để
    [04:17:39] níu giữ tuổi thanh xuân.
  ▶ [04:17:42] Vâng. Thế nhưng đằng sau những lời
  ▶ [04:17:44] chuyển miệng hào nhoáng ấy, báo chí và
  ▶ [04:17:47] truyền thông cũng ghi nhận không ít
  ▶ [04:17:49] những khoảng tối hoang mang. Đó là gì ạ?
    [04:17:52] Rất nhiều trong
    [04:17:54] chúng ta vì mong muốn chữa lành cấp tốc
    [04:17:58] đã vội vã tìm đến những trào lưu đề tốc
    [04:18:02] cực đoan bao gồm là lạm dụng đường thô
    [04:18:05] hay là thực phẩm ngọt để có thể
  ```

  Transcript 04:18:20–04:19:18 · [▶ watch from 04:18:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15500s)

  ```text
    [04:18:22] Vâng. Và cay đắng hơn thì có những người
    [04:18:24] mẹ bị cạn kiệt năng lượng tế bào nhưng
    [04:18:27] vẫn bị dán cái nhãn là
    [04:18:31] ờ trầm cảm sau sinh hay là rối loạn thần
    [04:18:33] kinh.
  ▶ [04:18:35] >> Vậy glutathe thực sự là gì dưới góc nhìn
  ▶ [04:18:37] y khoa chân chính? Và tại sao sự thiếu
    [04:18:41] hụt của nó lại gieo xuống cơ thể nhiều
    [04:18:44] nỗi oan và những cơn ác mộng da dằng đến
    [04:18:47] như vậy? Mở đầu cho phần một có tên là
    [04:18:50] cơ chế sinh học của glutathon. Thì ngay
  ▶ [04:18:53] bây giờ Khánh Lành xin kính mời bác sĩ
  ▶ [04:18:55] Phúc sẽ cởi bỏ đi những lấc mờ của
    [04:18:57] truyền thông. chúng ta sẽ
    [04:19:00] thấu hiểu một cách trần trụ nhất
    [04:19:02] glutathum là gì và bản chất thực sự của
    [04:19:06] hoạt chất này đối với cơ thể của con
    [04:19:08] người là như thế nào.
    [04:19:11] >> Vâng, Khánh Lành vừa mới kết nối chúng
    [04:19:13] ta cái chủ đề chính glutathon với lại
    [04:19:16] những cái phần trước đó là phần giao lưu
    [04:19:18] khán giả cũng như là phần sức khỏe của
  ```

### c456

**Decisions:** D4, D5, D6, D11 (correction approval)  
**Watch:** [▶ 05:22:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19340s)  ·  section start [▶ 04:19:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15564s)  
**Summary section:** [04:19:29] Đường, gốc tự do và trường hợp chị Hằng: vòng xoắn bệnh lý và sau khi bổ sung vi chất  
**Final class:** `unresolved` (pass 1 `attribution_qualification`, pass 2 `unresolved`)  
**Speaker:** Khánh Lành nêu miễn trừ cuối chương trình; tóm tắt gán giới hạn này cho bác sĩ.

- **BEFORE (current summary):** Bác sĩ dùng lập luận này để giải thích cơ chế, không phải để khẳng định chẩn đoán cho bất kỳ ai.
- **AFTER (proposed):** Đề xuất bỏ câu này vì transcript không có lời nào như vậy của bác sĩ. Nếu muốn giữ một lời nhắc, ghi rõ đây là lời chung của Khánh Lành cuối chương trình (đã có ở c553), không quy cho bác sĩ.
- **Why:** Stays unresolved. The only related text is the host's general closing disclaimer, which does not say that this explanation is not a diagnosis. The quote shows that closing text only and does not support the claim.
- **Pass-1 note:** Thêm giới hạn không khẳng định chẩn đoán vào lời bác sĩ; lời miễn trừ tham khảo/không thay chẩn đoán là Khánh Lành nói cuối chương trình.
- **Pass-2 note (blind):** After full read, no transcript statement that the reasoning is for mechanism only and not a diagnosis; appears to be a summarizer disclaimer attributed to the doctor
- **Reconciliation:** The transcript has a host’s general closing disclaimer, but does not clearly state that this specific explanation is not a diagnosis for anyone. Final unresolved.
- **Surrounding summary claims:**
  - previous (c455): Theo bác sĩ, gốc tự do này tạo thành một vòng xoắn bệnh lý, ảnh hưởng đến não, giấc ngủ (bóng đè) và nhịp tim (lên 170 nhịp mỗi phút), liên quan đến dopamin, serotonin và đường ruột.
  - next (c457): Bác sĩ nói glutathion không hoạt động được nếu thiếu các yếu tố hiệp đồng.
- **Quotes cited:**
  - [▶ 05:22:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19340s) "video trên kênh đều trị mang tính chất tham khảo và với mục đích là nâng cao nhận thức kiến thức chăm sóc sức khỏe cho cộng đồng và hoàn toàn không thay thế cho việc chẩn đoán và yểu điều trị y khoa trực tiếp và mỗi cơ thể là một"

  Transcript 05:22:10–05:22:50 · [▶ watch from 05:22:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19330s)

  ```text
    [05:22:10] Khánh Lành cũng xin phép được lưu ý tất
    [05:22:14] cả quý vị đó là tất cả những kiến thức
    [05:22:17] khoa học hay là phác đồ vi chất được bác
    [05:22:20] sĩ Trần Phan Phúc chia sẻ trong số phát
    [05:22:22] sóng này. ờ cũng như là toàn bộ các
  ▶ [05:22:25] video trên kênh đều trị mang tính chất
  ▶ [05:22:27] tham khảo và với mục đích là nâng cao
  ▶ [05:22:30] nhận thức kiến thức chăm sóc sức khỏe
  ▶ [05:22:32] cho cộng đồng và hoàn toàn không thay
  ▶ [05:22:34] thế cho việc chẩn đoán và yểu điều trị y
  ▶ [05:22:37] khoa trực tiếp và mỗi cơ thể là một
    [05:22:40] trạng thái riêng biệt với những diễn
    [05:22:42] biến bệnh lý vô cùng phức tạp. Vì vậy
    [05:22:45] khi có bất kỳ vấn đề nào về sức khỏe thì
    [05:22:47] quý vị chắc chắn phải đến các cơ sở y tế
    [05:22:50] chuyên môn để có thể được các bác sĩ
  ```

### c471

**Decisions:** D4, D7, D11 (correction approval)  
**Watch:** [▶ 04:31:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16299s)  ·  section start [▶ 04:21:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15695s)  
**Summary section:** [04:21:40] Cấu tạo, hoạt động và tái tạo của glutathion  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt quy nội dung cho bác sĩ.

- **BEFORE (current summary):** Hai glutathion hỏng sẽ khóa vào nhau tạo thành GSSG.
- **AFTER (proposed):** Hai glutathion hỏng tạm thời đám vào nhau tạo nên một phức hợp gọi là "GSGS" (bản ghi âm ghi như vậy).
- **Why:** The doctor says 'GSGS', the summary says 'GSSG'. Changing it to either form as a chemistry correction is out of scope, so the proposal keeps the spoken form. 'Tạm thời' is restored.
- **Pass-1 note:** Bác sĩ gọi rõ phức hợp là GSGS, khác GSSG trong tóm tắt; đoạn sau lại đọc GS/SG rời nên ký hiệu bản ghi không nhất quán.
- **Pass-2 note (blind):** Two spent glutathione lock together into GSSG (transcribed 'GSGS'); 'tạm thời' omitted, non-material
- **Reconciliation:** The transcript says “GSGS”; converting it to “GSSG” would be an external correction, out of scope. Final mismatch.
- **Surrounding summary claims:**
  - previous (c470): Sau khi nhường electron và H+, mũi kìm bị hỏng, và glutathion được ký hiệu là GSH.
  - next (c472): Được chuyển đến một "nhà máy" tái tạo (bản ghi viết là "redacta"), nơi cần năng lượng NADPH từ hô hấp tế bào.
- **Quotes cited:**
  - [▶ 04:31:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16299s) "vào trạng thái là chúng ta thấy gì? Cả hai kìm này đều hỏng thì các mũi kìm nó đám vào nhau tạm thời để tạo nên một cái phức hợp gọi là GSGS. Thế phức hợp GSGS này thì không hoạt"
  - [▶ 04:32:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16362s) "electron và 2H+ của cái gì? cho vào cái GS đúng không ạ? SG SìG để từ đây lại tạo ra hai cái kìm hoàn chỉnh. Vâng."

  Transcript 04:31:29–04:32:09 · [▶ watch from 04:31:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16289s)

  ```text
    [04:31:29] liên kết với nhau chỉ bỏ cái gì thôi ạ?
    [04:31:31] Chỉ bỏ H đi thôi.
    [04:31:32] >> Vâng.
    [04:31:34] >> Đúng chưa? Thế thì
    [04:31:36] kia nó sẽ còn có GS thì liên kết GS thì
    [04:31:39] nó bỏ H này đi rồi, bỏ electron đi rồi
    [04:31:42] thì cái hai cái kìm này bây giờ sẽ rơi
  ▶ [04:31:44] vào trạng thái là chúng ta thấy gì? Cả
  ▶ [04:31:46] hai kìm này đều hỏng thì các mũi kìm nó
  ▶ [04:31:49] đám vào nhau tạm thời để tạo nên một cái
  ▶ [04:31:52] phức hợp gọi là GSGS.
  ▶ [04:31:55] Thế phức hợp GSGS này thì không hoạt
    [04:31:58] động được nữa. Bây giờ nó đưa đến một
    [04:32:00] cái nhà máy. Nó đưa đến một cái nhà máy
    [04:32:03] để một cái phân xưởng để tái tạo lại thì
    [04:32:07] cái này sẽ đưa đến một cái nhà máy và
    [04:32:09] nhà máy đây có tên gọi là Glutathion.
  ```

  Transcript 04:32:32–04:33:12 · [▶ watch from 04:32:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16352s)

  ```text
    [04:32:33] trong quá trình hô hớp tế bào, tức là
    [04:32:34] quá trình chu trình CRP để nó tạo ra
    [04:32:37] năng lượng để sửa cái kìm kia.
    [04:32:38] >> Vâng.
    [04:32:39] >> Thế thì NADH này sẽ cho gì ạ? Sẽ cho
    [04:32:43] electron và cho H+ của cái gì ạ? Cho hai
  ▶ [04:32:47] electron và 2H+ của cái gì? cho vào cái
  ▶ [04:32:50] GS
  ▶ [04:32:52] đúng không ạ?
  ▶ [04:32:53] >> SG
  ▶ [04:32:53] >> SìG để từ đây lại tạo ra hai cái kìm
  ▶ [04:32:56] hoàn chỉnh.
  ▶ [04:32:56] >> Vâng.
    [04:32:57] >> Chúng ta thấy cơ thể nó khôn chưa ạ? Nó
    [04:32:59] khôn ở chỗ rằng sau khi hoạt động xong
    [04:33:01] thì kìm hỏng. Kìm hỏng hai cái nó tạm
    [04:33:03] thời gá vào nhau đã xong đẩy đến gì ạ?
    [04:33:06] Nhà máy Glutathion Ridacta là cái nhà
    [04:33:09] máy để tái tạo lại cái kìm đó bằng cách
    [04:33:12] là năng lượng ở đây nó sẽ cung cấp thêm
  ```

### c478

**Decisions:** D4, D10, D11 (correction approval)  
**Watch:** [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s)  ·  section start [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s)  
**Summary section:** [04:37:48] Những nguồn nào sinh ra gốc tự do?  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Bác sĩ nêu ba nguồn chính.
- **AFTER (proposed):** Đầu tiên bác sĩ nói cái thứ nhất là yếu tố tinh thần; tiếp theo ông đánh số: thứ nhất là ăn uống, thứ hai là thuốc, thứ ba là kim loại nặng.
- **Why:** 'Three sources' loses the source's numbering: mental factors come first, then diet, medicine and heavy metals are numbered 1 to 3. Note for the human: c479 to c482 number these differently and were classed supported, so they may need the same wording if this item is accepted.
- **Pass-1 note:** Không nêu đúng ba nguồn tổng cộng: yếu tố tinh thần được nói trước, rồi ăn uống, thuốc và kim loại nặng; số thứ nhất/hai/ba được dùng lại cho ba nhóm sau.
- **Pass-2 note (blind):** Doctor enumerates thứ nhất/thứ hai/thứ ba (ăn uống, thuốc, kim loại nặng) after first recalling mental stress; borderline since tinh thần is also called 'cái thứ nhất'
- **Reconciliation:** The transcript labels mental factors first, then separately numbers diet, medicine and heavy metals; “three sources” loses the source’s enumeration. Final mismatch.
- **Surrounding summary claims:**
  - previous (c477): Bác sĩ cũng nói oxy già có thể trở thành loại nguy hiểm hơn khi có thêm sắt hai hoặc đồng hai.
  - next (c479): Thứ nhất là yếu tố tinh thần.
- **Quotes cited:**
  - [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s) "Thì đầu tiên cái thứ nhất là liên quan tới yếu tố tinh thần mà lúc nãy chúng ta phân tích suốt rồi đúng không ạ?"
  - [▶ 04:38:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16709s) "Nó gắn tất cả những cái này gắn vào nó sẽ thành chất nguy hiểm. Thứ hai nữa là chúng ta ngoài cái ăn uống ra thì chúng ta có gì ạ? Có thuốc. các sản phẩm thuốc"
  - [▶ 04:39:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16739s) "bắt đầu nó nguy hiểm. Cái thứ ba đó là chúng ta rất chú ý là những cái kim loại nặng."
  - [▶ 04:38:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16679s) "Do đồ ăn thức uống thứ nhất là do ăn uống."

  Transcript 04:37:33–04:39:29 · [▶ watch from 04:37:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16653s)

  ```text
    [04:37:34] >> Thế thì dẫn tới là đột biến gen và rất
    [04:37:37] nguy hiểm. Thì đây chính là ta nhớ lại
    [04:37:39] cái gốc tự do mà tôi nói từ ban đầu. Thế
    [04:37:42] thì gốc tự do này nó sinh ra nó bị như
    [04:37:46] thế nào? Tại sao nó lại sinh ra như thế?
  ▶ [04:37:48] Thì đầu tiên cái thứ nhất là liên quan
  ▶ [04:37:50] tới yếu tố tinh thần mà lúc nãy chúng ta
  ▶ [04:37:53] phân tích suốt rồi đúng không ạ?
    [04:37:54] >> Yếu tố tinh thần rất quan trọng. Tiếp
    [04:37:57] theo đó là do cái gì? Những các cái gì
    [04:38:00] nó gây ra? Ta nhắc lại cái là do đồ ăn
    [04:38:02] thức uống của chúng ta đúng không ạ?
    [04:38:04] Vâng.
  ▶ [04:38:04] >> Do đồ ăn thức uống thứ nhất là do ăn
  ▶ [04:38:06] uống. Ăn uống của chúng ta có những độc
    [04:38:08] chất ví dụ như hóa chất đúng không ạ?
    [04:38:10] >> Thuốc trừ sâu đúng không ạ?
    [04:38:12] >> Vân vân. Tất cả những cái này chúng ta
    [04:38:14] ăn uống ăn quá nhiều đường, ăn quá nhiều
    [04:38:16] đạm, ăn quá nhiều chất béo vân vân đều
    [04:38:19] tất cả những cái đó thì những cái đó khi
    [04:38:22] vào ăn thừa thì lập tức là nó sẽ biến
    [04:38:25] thành gốc tự do. Nó gắn với những các
    [04:38:26] cái thành phần này.
    [04:38:28] >> Những thành phần này khi gắn vào lập tức
    [04:38:30] những cái đó sẽ trở thành
    [04:38:32] >> chất nguy hiểm.
    [04:38:33] >> Vâng.
  ▶ [04:38:34] >> Nó gắn tất cả những cái này gắn vào nó
  ▶ [04:38:36] sẽ thành chất nguy hiểm. Thứ hai nữa là
  ▶ [04:38:39] chúng ta ngoài cái ăn uống ra thì chúng
  ▶ [04:38:41] ta có gì ạ? Có thuốc. các sản phẩm thuốc
    [04:38:43] mà chúng ta uống vào không cần thiết. Ví
    [04:38:46] dụ như paracetamol ghê ngộ độc gát, ví
    [04:38:48] dụ như là các cái thuốc mà chúng ta đau
    [04:38:50] khớp, chúng ta uống đủ thứ xong sẽ uống
    [04:38:53] những các cái gì cocticoid chẳng hạn.
    [04:38:55] Đúng rồi thế rồi nhiều những thuốc khác
    [04:38:57] nếu chúng ta uống sai chỉ định, chúng
    [04:38:59] tôi uống quá đà sẽ dẫn tới là nó sẽ gắn
    [04:39:03] những cái gốc tự do này vào và lúc ấy
  ▶ [04:39:04] bắt đầu nó nguy hiểm. Cái thứ ba đó là
  ▶ [04:39:08] chúng ta rất chú ý là những cái kim loại
  ▶ [04:39:09] nặng.
    [04:39:10] >> Vâng. kim loại nặng ví dụ như là chủy
    [04:39:13] trì đúng không ạ? Ví dụ như thủy ngân ví
    [04:39:15] dụ như aen vân vân đúng không ạ? Tất cả
    [04:39:17] những cái kim loại nặng này.
    [04:39:19] >> Thế thì ừ những thành phần này khi mà nó
    [04:39:23] bị oxy hóa tạo thành gốc tự do, oxy hóa
    [04:39:26] tạo thành gốc tự do thì nó sẽ rất nguy
    [04:39:28] hiểm. Nó nguy hiểm thể hiện ở mấy cái
  ```

### c488

**Decisions:** D8, D11 (correction approval)  
**Watch:** [▶ 04:41:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16909s)  ·  section start [▶ 04:41:31](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16886s)  
**Summary section:** [04:41:31] Gốc tự do tập trung nhiều ở đâu trong cơ thể?  
**Final class:** `mismatch` (pass 1 `mismatch`, pass 2 `mismatch`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Các cơ quan này đều thực hiện nhiều chức năng thải độc.
- **AFTER (proposed):** Đây là những cơ quan thực hiện rất nhiều chức năng; về thải độc, bản ghi âm ghi "thận cũng thải độc rất nhiều. Gan, não, thận trong ruột của chúng ta rất nhiều" và "thận là cái nơi thải độc" (chưa rõ những cơ quan nào được nói là thải độc).
- **Why:** The transcript says these organs have many functions, and the summary turns this into all of them performing many detox functions. The captions clearly call the kidney a detox site, but the unpunctuated 'Gan, não, thận trong ruột ... rất nhiều' follows a speaker change and is affirmed at the next turn, so it is unclear which organs it covers. The proposal keeps the caption's wording. Human to check which organs detox and who says it.
- **Pass-1 note:** Bác sĩ nói các cơ quan thực hiện nhiều chức năng/hoạt động; chỉ riêng thận được gọi rõ là thải độc, không nói mọi cơ quan này đều thực hiện nhiều chức năng thải độc.
- **Pass-2 note (blind):** Doctor says these organs perform many functions; only thận is called the detox site — summary turns it into all organs performing many detox functions
- **Surrounding summary claims:**
  - previous (c487): Bác sĩ xếp các cơ quan theo mức độ tập trung gốc tự do như sau: gan đứng đầu, rồi thận, ruột, não, tim và phổi.
  - next (c489): Bác sĩ nói enzyme GST có hai chức năng.
- **Quotes cited:**
  - [▶ 04:41:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16909s) "và thận cũng thải độc rất nhiều. Gan, não, thận trong ruột của chúng ta rất nhiều. Vâng. Đúng rồi. Đấy là những cơ quan mà"
  - [▶ 04:42:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16934s) "đang lục phủ ngũ tạng của chúng ta đang thực hiện những chức năng rất nhiều tim rồi đến phổi vân vân. Tất cả như thế này"
  - [▶ 04:41:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16914s) "Đấy là những cơ quan mà chúng ta thực hiện rất nhiều chức năng"
  - [▶ 04:42:06](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16921s) "Thứ hai là là gì ạ? Là thận là cái nơi thải độc đúng không ạ?"

  Transcript 04:41:39–04:42:44 · [▶ watch from 04:41:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16899s)

  ```text
    [04:41:40] Từ ti thể.
    [04:41:41] >> Vâng.
    [04:41:42] >> Từ những các cái nơi mà tham gia chuyển
    [04:41:44] hóa, những nơi hoạt động nhiều, nơi nào
    [04:41:46] chuyển hóa nhiều nhất, hoạt động nhiều
    [04:41:48] nhất trong cơ thể chúng ta
    [04:41:49] >> gan.
    [04:41:50] >> Đó là gan.
    [04:41:51] >> Tiếp nữa là trên não hoạt động rất
    [04:41:52] nhiều. Có đúng không ạ? Gan, não
  ▶ [04:41:54] >> và thận cũng thải độc rất nhiều. Gan,
  ▶ [04:41:57] não, thận trong ruột của chúng ta rất
  ▶ [04:41:59] nhiều.
  ▶ [04:41:59] >> Vâng. Đúng rồi. Đấy là những cơ quan mà
  ▶ [04:42:01] chúng ta thực hiện rất nhiều chức năng
    [04:42:03] nhưng gan là đứng số một. Gan là số một.
  ▶ [04:42:06] Gan là đầu tiên. Thứ hai là là gì ạ? Là
  ▶ [04:42:09] thận là cái nơi thải độc đúng không ạ?
    [04:42:11] Thế rồi ruột đúng không ạ? Thế rồi gì ạ?
    [04:42:13] Não sau đó thì đến gì? Tim. Rồi đến gì
    [04:42:17] ạ? Phổi. Đấy là những nơi mà chúng ta
  ▶ [04:42:19] đang lục phủ ngũ tạng của chúng ta đang
  ▶ [04:42:20] thực hiện những chức năng rất nhiều tim
  ▶ [04:42:23] rồi đến phổi vân vân. Tất cả như thế này
    [04:42:25] thì những cái nơi này đang tập trung gốc
    [04:42:27] tự do rất nhiều.
    [04:42:29] tập trung gốc tự do rất nhiều. Thì ở đây
    [04:42:32] chúng ta sẽ khi mà cái hoạt động gắp này
    [04:42:34] nó sẽ như thế nào, cái hoạt động gắp thì
    [04:42:37] chúng ta sẽ hình dung rằng cái
    [04:42:41] glutathion này đóng vai trò là chiếc kìm
    [04:42:44] này. Nhưng chiếc kìm này nó di động.
  ```

### c500

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 04:51:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17512s)  ·  section start [▶ 04:50:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17430s)  
**Summary section:** [04:50:35] Glutathion bảo vệ ti thể và năng lượng tế bào  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Ti thể có ADN riêng nằm sát màng trong, nên gốc tự do thấm qua có thể phá hủy ADN này và gây đột biến.
- **AFTER (proposed):** Ti thể có ADN riêng nằm sát màng ti thể, nên các gốc tự do thấm qua thì phá hủy ADN riêng này, tạo thành gốc tự do và bị đột biến.
- **Why:** 'Màng trong' (inner membrane) is added: the doctor says only 'sát màng ti thể'. 'Có thể' also softens his direct statement.
- **Pass-1 note:** Thêm định vị màng trong: bác sĩ chỉ nói ADN sát màng ti thể, không xác định màng trong; phá hủy và đột biến có trong bản ghi.
- **Pass-2 note (blind):** Supported; transcript says 'sát màng ti thể' without specifying inner membrane ('màng trong' is a minor added specificity)
- **Reconciliation:** The transcript places DNA near the mitochondrial membrane but does not specify the inner membrane; retain qualification issue.
- **Surrounding summary claims:**
  - previous (c499): Bác sĩ nói ti thể là nơi diễn ra trao đổi chất, đốt cháy đường, đạm và chất béo, nên có rất nhiều gốc tự do.
  - next (c501): Glutathion được đưa vào và bám dày đặc ở mặt trong màng ti thể để trung hòa gốc tự do ngay khi chúng vừa xuất hiện.
- **Quotes cited:**
  - [▶ 04:51:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17512s) "ADN là vật chất di truyền rất quan trọng. Thế mà nằm ở sát màng ti thể này dẫn tới là các gốc tự do nó thấm qua đây thì phá hủy gì ạ? ADN"
  - [▶ 04:52:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17522s) "Đúng rồi. Phá hủy ADN nó có hai cái. Một là chính ADN này tạo thành gốc tự do. Hai là gì ạ? Là bị đột biến. Vâng."

  Transcript 04:51:42–04:52:32 · [▶ watch from 04:51:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17502s)

  ```text
    [04:51:43] biệt đó là có ADN riêng.
    [04:51:46] Nó khác với lại tế bào có một cái cơ
    [04:51:48] quan ADN chung nằm ở nhân nhưng riêng
    [04:51:51] tiể có ADN riêng nó nằm ở xung quanh này
    [04:51:54] này nằm xung quanh ti thể là ADN riêng.
  ▶ [04:51:57] ADN là vật chất di truyền rất quan
  ▶ [04:51:59] trọng. Thế mà nằm ở sát màng ti thể này
  ▶ [04:52:02] dẫn tới là các gốc tự do nó thấm qua đây
  ▶ [04:52:04] thì phá hủy gì ạ? ADN
    [04:52:06] >> riêng của ti thể.
  ▶ [04:52:07] >> Đúng rồi. Phá hủy ADN nó có hai cái. Một
  ▶ [04:52:10] là chính ADN này tạo thành gốc tự do.
  ▶ [04:52:13] Hai là gì ạ? Là bị đột biến. Vâng.
    [04:52:15] >> Có đúng không ạ? Từ đó chính là gây ra
    [04:52:17] bệnh tật.
    [04:52:18] >> Vâng.
    [04:52:19] >> Thế thì như vậy sẽ rất nguy hiểm rồi, sẽ
    [04:52:21] không được nữa. Vậy thì lúc này sẽ có gì
    [04:52:25] ạ? Glutat có một nhiệm vụ chuyên biệt,
    [04:52:28] một nhiệm vụ mà vô cùng đặc biệt đó là
    [04:52:32] cơ thể tế bào của chúng ta nó đẩy
  ```

### c509

**Decisions:** D4, D11 (correction approval)  
**Watch:** [▶ 05:01:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18077s)  ·  section start [▶ 04:55:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17730s)  
**Summary section:** [04:55:35] Glutathion làm trắng da theo cơ chế nào?  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `unresolved`)  
**Speaker:** Bác sĩ chỉ nói 'đấy là cái cơ chế'; không có câu 'không phải lời khuyên' từ bác sĩ

- **BEFORE (current summary):** Bác sĩ nói đây là cơ chế, không phải lời khuyên.
- **AFTER (proposed):** Bác sĩ nói "đấy là cái cơ chế làm trắng da là như vậy".
- **Why:** 'Không phải lời khuyên' is not said. The host's closing disclaimer is general and not tied to this mechanism.
- **Pass-1 note:** Thêm qualification: vế 'không phải lời khuyên' không được nói ở đoạn này; lời miễn trừ chung (tham khảo, không thay thế chẩn đoán) ở cuối chương trình là của Khánh Lành, không gắn với cơ chế làm trắng da.
- **Pass-2 note (blind):** After full read, the doctor explains the whitening mechanism but never says 'đây là cơ chế, không phải lời khuyên'; disclaimer appears summarizer-added
- **Reconciliation:** The doctor explains the whitening mechanism but does not say “not advice”; the closing disclaimer is the host’s and is not that claim. Final attribution/qualification.
- **Surrounding summary claims:**
  - previous (c508): Sau đó glutathion tự sử dụng công cụ pha màu trắng và làm da trắng hồng lên.
  - next (c510): Bác sĩ tóm tắt các vai trò: giải độc (được ví là "vua của chống độc" ở gan, não, thận và ruột), nâng cao hệ miễn dịch, bảo vệ ti thể và tăng năng lượng tế bào (góp phần giảm cân, giảm mỡ, giảm đường), và làm trắng da.
- **Quotes cited:**
  - [▶ 05:01:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18077s) "đấy là cái cơ chế làm trắng da là như vậy."

  Transcript 05:01:07–05:01:47 · [▶ watch from 05:01:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18067s)

  ```text
    [05:01:07] nữa. Bởi vì anh nay chỉ có trộn sơn
    [05:01:09] trắng là sơn đen là chính thôi.
    [05:01:10] >> Vâng.
    [05:01:11] >> Và khóa luôn tay anh này không cho trộn
    [05:01:13] nữa. Và nó chính thức nó bắt tay với lại
    [05:01:15] cái công cụ trộn sơn trắng này và
    [05:01:18] glutathum trực tiếp trộn sơn trắng để
    [05:01:20] làm cho da của chúng ta trắng lên.
  ▶ [05:01:22] >> Vâng. đấy là cái cơ chế làm trắng da là
  ▶ [05:01:25] như vậy.
    [05:01:25] >> Vâng, tôi nghĩ là rất nhiều khán giả,
    [05:01:28] đặc biệt là khán giả nữ sẽ rất hào hứng
    [05:01:29] với thông tin này.
    [05:01:31] >> Vâng. Thế thì đây là toàn bộ tất cả
    [05:01:34] những các cái tác dụng của glutathion
    [05:01:36] >> thì chúng ta thấy quan trọng hàng đầu
    [05:01:38] vẫn là cái gì ạ? Cái mũi kìm này. Vâng.
    [05:01:41] >> Đó chính là gấp độc chất.
    [05:01:44] >> Mũi kìm thiông này gấp độc chất thông
    [05:01:46] qua cái là nó luôn luôn cái đây là sẵn
  ```

### c529

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 05:12:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18750s)  ·  section start [▶ 05:06:37](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18392s)  
**Summary section:** [05:06:37] Các đường đưa glutathione vào cơ thể: uống, ngậm dưới lưỡi, tiêm, liposome  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc nói; tóm tắt quy cho bác sĩ

- **BEFORE (current summary):** Bác sĩ cho rằng đường tiêm "quá nguy hiểm", có thể gây sốc và ngộ độc.
- **AFTER (proposed):** Bác sĩ nói đường tiêm "quá nguy hiểm", và đường tiêm này thì "sẽ một là sốc và hai là ngộ độc".
- **Why:** Softened hedge: 'sẽ một là sốc và hai là ngộ độc' became 'có thể gây'. The proposal restores his wording.
- **Pass-1 note:** Hedge added: bác sĩ nói khẳng định 'sẽ ... sốc ... ngộ độc'; tóm tắt làm mềm thành 'có thể gây'.
- **Pass-2 note (blind):** 'quá nguy hiểm' verbatim, but definite 'sẽ một là sốc và hai là ngộ độc' softened to 'có thể gây sốc và ngộ độc'
- **Surrounding summary claims:**
  - previous (c528): Theo bác sĩ, ngậm dưới lưỡi là một giải pháp nhưng không phải là nhiều.
  - next (c530): Bác sĩ nêu FDA của Mỹ không đồng ý và khuyến cáo không dùng đường này vì nguy cơ sốc và ngộ độc.
- **Quotes cited:**
  - [▶ 05:12:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18750s) "Thì con đường này quá nguy hiểm."
  - [▶ 05:12:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18754s) "Con đường tiêm này thì sẽ một là sốc và hai là ngộ độc."

  Transcript 05:12:20–05:13:04 · [▶ watch from 05:12:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18740s)

  ```text
    [05:12:20] pháp nhưng cũng không nhiều.
    [05:12:23] Thế thì đây là ba con đường chính nhưng
    [05:12:26] mà chúng ta thấy rằng bịt mù hiệu quả nó
    [05:12:28] không phải là quá cao như quý vị đang
    [05:12:31] thần tượng và đang kỳ vọng vào
    [05:12:32] glutathion.
    [05:12:33] >> Vâng.
    [05:12:34] >> Còn một cái con đường cuối cùng đó là
  ▶ [05:12:35] con đường tiêm. Thì con đường này quá
  ▶ [05:12:38] nguy hiểm.
  ▶ [05:12:39] Con đường tiêm này thì sẽ một là sốc và
  ▶ [05:12:42] hai là ngộ độc. Vậy thì con đường này ví
    [05:12:46] dụ như là
    [05:12:48] FDA của Mỹ là không đồng ý với con đường
    [05:12:52] này, khuyến cáo rằng không dùng vì nó
    [05:12:54] quá nguy hiểm, rơi vào tình trạng sốc và
    [05:12:56] ngộ độc.
    [05:12:57] >> Vâng.
    [05:12:57] >> Cho nên là con đường tiêm ta xóa bỏ đi.
    [05:13:00] >> Vâng.
    [05:13:00] >> Chúng ta lưu ý rằng cẩn thận quý vị đừng
    [05:13:02] dại dột mà đi sử dụng con đường tiêm
    [05:13:04] nhưng ba con đường này nó bịt mù mất
  ```

### c541

**Decisions:** D5, D6, D11 (correction approval)  
**Watch:** [▶ 05:15:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18954s)  ·  section start [▶ 05:15:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18954s)  
**Summary section:** [05:15:59] Thực phẩm chứa cơ chất tổng hợp glutathione và số loại thực phẩm mỗi ngày  
**Final class:** `unresolved` (pass 1 `unresolved`, pass 2 `unresolved`)  
**Speaker:** Không áp dụng (ghi chú biên tập)

- **BEFORE (current summary):** Lưu ý: đây là cách nói trong bản phiên âm, nên người xem nên đối chiếu lại nếu cần.
- **AFTER (proposed):** Đề xuất bỏ ghi chú này, hoặc đánh dấu rõ đây là ghi chú của người tóm tắt, không phải nội dung chương trình.
- **Why:** Stays unresolved. This is an editorial note about transcript reliability, not something said in the video, so no supporting quote exists. The figures it refers to were checked at c540.
- **Pass-1 note:** Ghi chú biên tập về độ tin cậy phiên âm, không phải nội dung phát biểu; con số nguyên văn đã đối chiếu ở c540.
- **Pass-2 note (blind):** Meta note about transcript wording; no transcript content to verify
- **Surrounding summary claims:**
  - previous (c540): Theo bác sĩ, nên ăn 25 loại thực phẩm trong một tuần, và 12 loại trong một ngày.
  - next (c542): Bác sĩ nói ăn đủ như vậy kết hợp với bổ sung đủ vi chất sẽ giúp cơ thể tổng hợp glutathione tốt hơn.
- **Quotes cited:** none (no supporting text found in the transcript). Context below is from the section start.

  Transcript 05:15:44–05:16:24 · [▶ watch from 05:15:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18944s)

  ```text
    [05:15:44] >> Vâng.
    [05:15:44] >> Cho nên là chúng ta phải bổ sung vi
    [05:15:46] chất. Việc thứ hai đó chính là chế độ ăn
    [05:15:49] uống của chúng ta phải đa dạng cân bằng.
    [05:15:52] Đặc biệt là cái anh Fittain này này là
    [05:15:54] cái anh mà khá hiếm trong các cái đồ ăn
    [05:15:56] thức uống cho nên là chúng ta phải ăn
    [05:15:58] đầy đủ.
    [05:15:59] Những các cái cơ chất này nó có trong
    [05:16:01] cái gì? Có trong một là da cầm tức là
    [05:16:05] thịt gà, thịt ngan, thịt vịt. Thứ hai
    [05:16:07] nữa là trứng. da cầm này trứng này thế
    [05:16:10] rồi thì có trong những sản phẩm ví dụ
    [05:16:12] sữa cũng có thế rồi rau cải xanh rau cải
    [05:16:15] xanh thế rồi các cái loại bì các loại da
    [05:16:18] ví dụ da gà da lợn các loại bì thế rồi
    [05:16:20] nước xương hầm thì có dầu những cái
    [05:16:23] thành phần này thế cho nên là chúng ta
  ```

### c549

**Decisions:** D11 (correction approval)  
**Watch:** [▶ 05:19:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19160s)  ·  section start [▶ 05:19:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19160s)  
**Summary section:** [05:19:25] Quan điểm của bác sĩ về sản phẩm glutathione đắt tiền  
**Final class:** `attribution_qualification` (pass 1 `attribution_qualification`, pass 2 `attribution_qualification`)  
**Speaker:** Bác sĩ Trần Văn Phúc nói; tóm tắt quy cho bác sĩ

- **BEFORE (current summary):** Bác sĩ nói glutathione đang bán rất đắt và là sản phẩm "hot" trên thị trường.
- **AFTER (proposed):** Bác sĩ nói trên thế giới có những sản phẩm glutathion bán rất đắt, và nó đã trở thành một sản phẩm khá hot trên thị trường.
- **Why:** Qualifier dropped: 'có những sản phẩm' (some products) and 'khá hot' became glutathione in general being 'rất đắt' and 'hot'.
- **Pass-1 note:** Qualifier dropped: bác sĩ nói 'có những sản phẩm' bán rất đắt và 'khá hot'; tóm tắt khái quát thành glutathione nói chung bán rất đắt, 'hot'.
- **Pass-2 note (blind):** Qualifier dropped/hardened: source says 'có những sản phẩm' (some products) sell very expensively and became 'khá hot'; summary generalizes to glutathione overall being 'rất đắt' and 'hot'.
- **Surrounding summary claims:**
  - previous (c548): Bác sĩ cho rằng chế độ ăn uống thường đã đủ các thành phần cơ bản, nên nếu không có tiền thì vẫn có thể yên tâm bằng cách tăng tổng hợp nội sinh, bổ sung vi chất đầy đủ, và ngăn gốc tự do.
  - next (c550): Theo quan điểm cá nhân của bác sĩ, người ta hoàn toàn có thể hiểu cơ chế và kích hoạt cơ thể có đủ glutathione, không nhất thiết phải dùng sản phẩm bổ sung đắt tiền.
- **Quotes cited:**
  - [▶ 05:19:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19160s) "sản phẩm Glutathion trên thế giới có những sản phẩm bán rất đắt và nó đã trở thành một cái sản phẩm khá hot trên thị trường"

  Transcript 05:19:10–05:19:50 · [▶ watch from 05:19:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19150s)

  ```text
    [05:19:11] lúc đấy glutathum trong cơ thể của chúng
    [05:19:13] ta nó sẽ hoạt động một cách hiệu quả
    [05:19:15] nhất. Nó sản xuất đầy đủ nhất và chúng
    [05:19:17] ta sẽ trẻ ra, chúng ta sẽ phòng tránh
    [05:19:19] được bệnh tật bằng chính con đường nội
    [05:19:21] sinh của chúng ta rất rẻ mà không tốn
    [05:19:23] kém tiền bạc gì. Còn đến giờ phút này có
  ▶ [05:19:25] thể nói rằng sản phẩm Glutathion trên
  ▶ [05:19:28] thế giới có những sản phẩm bán rất đắt
  ▶ [05:19:30] và nó đã trở thành một cái sản phẩm khá
  ▶ [05:19:32] hot trên thị trường để mọi người lão vào
    [05:19:35] bổ sung. Tuy nhiên theo quan điểm của cá
    [05:19:37] nhân tôi thì chúng ta hoàn toàn có thể
    [05:19:40] hiểu cái cơ chế như thế này và chúng ta
    [05:19:42] vẫn kích hoạt được cơ thể chúng ta có đủ
    [05:19:45] glutathion để chúng ta hoạt động và
    [05:19:47] chúng ta trẻ hóa, chúng ta thoát khỏi
    [05:19:49] các cái tình trạng bệnh tật khác mà
  ```

## Related records without a correction

### c003

**Decisions:** D4  
**Watch:** [▶ 00:07:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=429s)  ·  section start [▶ 00:01:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=99s)  
**Summary section:** [00:01:44] Glutathion là gì và có vai trò gì trong cơ thể?  
**Final class:** `supported` (pass 1 `attribution_qualification`, pass 2 `supported`)  
**Speaker:** BS Trần Văn Phúc; summary unattributed

- **BEFORE (current summary):** Glutathion được xem là chất chống lại gốc tự do quan trọng nhất.
- **AFTER:** no correction proposed (record is `supported`).
- **Pass-1 note:** Hedge 'Có thể nói' dropped and 'vô cùng quan trọng'/'vua' hardened to flat 'quan trọng nhất'.
- **Pass-2 note (blind):** 'vua của chống gốc tự do' (with hedge 'có thể nói') matches 'được xem là ... quan trọng nhất'
- **Reconciliation:** “Được xem là” retains the source hedge “có thể nói”; “vua” supports the highest-importance paraphrase. Final supported.
- **Surrounding summary claims:**
  - previous (c002): Bài nói về cuộc chiến giữa oxy hóa và khử ở cấp độ vi mô, trong đó các gốc tự do có thể bòn rút năng lượng sống, tàn phá ti thể và các mảng tế bào.
  - next (c004): Chương trình có hai phần: (1) cơ chế sinh học của glutathion, và (2) cách bổ sung glutathion.
- **Quotes cited:**
  - [▶ 00:07:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=429s) "glutaton là một cái chất mà chống lại gốc tự do vô cùng quan trọng. Có thể nói đây là cái chất được xếp vào vua của chống gốc tự do."

  Transcript 00:06:59–00:07:39 · [▶ watch from 00:06:59](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=419s)

  ```text
    [00:07:00] xuất phát từ cái con đường của gốc tự
    [00:07:02] do. Và nếu như không giải quyết được vấn
    [00:07:04] đề gốc tự do thì chúng ta sẽ phát sinh
    [00:07:07] ra rất rất nhiều các cái bệnh tật khác
    [00:07:08] nhau. Đó chính là cái lý do mà ngày hôm
    [00:07:11] nay chúng tôi có đề cập tới một cái chủ
  ▶ [00:07:14] đề cực kỳ quan trọng đó là glutaton là
  ▶ [00:07:17] một cái chất mà chống lại gốc tự do vô
  ▶ [00:07:20] cùng quan trọng. Có thể nói đây là cái
  ▶ [00:07:22] chất được xếp vào vua của chống gốc tự
  ▶ [00:07:25] do.
    [00:07:25] Và chúng tôi muốn rằng cái chủ đề ngày
    [00:07:27] hôm nay sẽ chuyển tải đến quý vị và các
    [00:07:30] bạn từ lý thuyết của gốc tự do như thế
    [00:07:33] nào cho đến những các cái thành phần để
    [00:07:35] chống lại gốc tự do đó ra sao. Và cuối
    [00:07:37] cùng cái trọng tâm của cái chủ điểm ngày
    [00:07:39] hôm nay đó chính là Glutathion tức là
  ```

### c479

**Decisions:** D10  
**Watch:** [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s)  ·  section start [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s)  
**Summary section:** [04:37:48] Những nguồn nào sinh ra gốc tự do?  
**Final class:** `supported` (pass 1 `supported`, pass 2 `not checked`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Thứ nhất là yếu tố tinh thần.
- **AFTER:** no correction proposed (record is `supported`).
- **Pass-1 note:** Yếu tố tinh thần được nêu đầu tiên.
- **Surrounding summary claims:**
  - previous (c478): Bác sĩ nêu ba nguồn chính.
  - next (c480): Thứ hai là ăn uống: thực phẩm chứa hóa chất hoặc thuốc trừ sâu, và ăn quá nhiều đường, đạm hoặc chất béo, khi thừa sẽ biến thành gốc tự do.
- **Quotes cited:**
  - [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s) "Thì đầu tiên cái thứ nhất là liên quan tới yếu tố tinh thần mà lúc nãy chúng ta phân tích suốt rồi đúng không ạ? Yếu tố tinh thần rất quan trọng. Tiếp"

  Transcript 04:37:33–04:38:13 · [▶ watch from 04:37:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16653s)

  ```text
    [04:37:34] >> Thế thì dẫn tới là đột biến gen và rất
    [04:37:37] nguy hiểm. Thì đây chính là ta nhớ lại
    [04:37:39] cái gốc tự do mà tôi nói từ ban đầu. Thế
    [04:37:42] thì gốc tự do này nó sinh ra nó bị như
    [04:37:46] thế nào? Tại sao nó lại sinh ra như thế?
  ▶ [04:37:48] Thì đầu tiên cái thứ nhất là liên quan
  ▶ [04:37:50] tới yếu tố tinh thần mà lúc nãy chúng ta
  ▶ [04:37:53] phân tích suốt rồi đúng không ạ?
  ▶ [04:37:54] >> Yếu tố tinh thần rất quan trọng. Tiếp
    [04:37:57] theo đó là do cái gì? Những các cái gì
    [04:38:00] nó gây ra? Ta nhắc lại cái là do đồ ăn
    [04:38:02] thức uống của chúng ta đúng không ạ?
    [04:38:04] Vâng.
    [04:38:04] >> Do đồ ăn thức uống thứ nhất là do ăn
    [04:38:06] uống. Ăn uống của chúng ta có những độc
    [04:38:08] chất ví dụ như hóa chất đúng không ạ?
    [04:38:10] >> Thuốc trừ sâu đúng không ạ?
    [04:38:12] >> Vân vân. Tất cả những cái này chúng ta
  ```

### c480

**Decisions:** D10  
**Watch:** [▶ 04:38:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16679s)  ·  section start [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s)  
**Summary section:** [04:37:48] Những nguồn nào sinh ra gốc tự do?  
**Final class:** `supported` (pass 1 `supported`, pass 2 `not checked`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Thứ hai là ăn uống: thực phẩm chứa hóa chất hoặc thuốc trừ sâu, và ăn quá nhiều đường, đạm hoặc chất béo, khi thừa sẽ biến thành gốc tự do.
- **AFTER:** no correction proposed (record is `supported`).
- **Pass-1 note:** Có hóa chất, thuốc trừ sâu và điều kiện ăn thừa đường/đạm/chất béo.
- **Surrounding summary claims:**
  - previous (c479): Thứ nhất là yếu tố tinh thần.
  - next (c481): Thứ ba là thuốc dùng không cần thiết, sai chỉ định hoặc uống quá đà, ví dụ paracetamol (ngộ độc gan) hoặc corticoid.
- **Quotes cited:**
  - [▶ 04:38:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16679s) "Vâng. Do đồ ăn thức uống thứ nhất là do ăn uống. Ăn uống của chúng ta có những độc chất ví dụ như hóa chất đúng không ạ? Thuốc trừ sâu đúng không ạ?"
  - [▶ 04:38:14](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16689s) "ăn uống ăn quá nhiều đường, ăn quá nhiều đạm, ăn quá nhiều chất béo vân vân đều tất cả những cái đó thì những cái đó khi"
  - [▶ 04:38:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16697s) "vào ăn thừa thì lập tức là nó sẽ biến thành gốc tự do. Nó gắn với những các cái thành phần này."

  Transcript 04:37:49–04:38:47 · [▶ watch from 04:37:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16669s)

  ```text
    [04:37:50] tới yếu tố tinh thần mà lúc nãy chúng ta
    [04:37:53] phân tích suốt rồi đúng không ạ?
    [04:37:54] >> Yếu tố tinh thần rất quan trọng. Tiếp
    [04:37:57] theo đó là do cái gì? Những các cái gì
    [04:38:00] nó gây ra? Ta nhắc lại cái là do đồ ăn
    [04:38:02] thức uống của chúng ta đúng không ạ?
  ▶ [04:38:04] Vâng.
  ▶ [04:38:04] >> Do đồ ăn thức uống thứ nhất là do ăn
  ▶ [04:38:06] uống. Ăn uống của chúng ta có những độc
  ▶ [04:38:08] chất ví dụ như hóa chất đúng không ạ?
  ▶ [04:38:10] >> Thuốc trừ sâu đúng không ạ?
    [04:38:12] >> Vân vân. Tất cả những cái này chúng ta
  ▶ [04:38:14] ăn uống ăn quá nhiều đường, ăn quá nhiều
  ▶ [04:38:16] đạm, ăn quá nhiều chất béo vân vân đều
  ▶ [04:38:19] tất cả những cái đó thì những cái đó khi
  ▶ [04:38:22] vào ăn thừa thì lập tức là nó sẽ biến
  ▶ [04:38:25] thành gốc tự do. Nó gắn với những các
  ▶ [04:38:26] cái thành phần này.
    [04:38:28] >> Những thành phần này khi gắn vào lập tức
    [04:38:30] những cái đó sẽ trở thành
    [04:38:32] >> chất nguy hiểm.
    [04:38:33] >> Vâng.
    [04:38:34] >> Nó gắn tất cả những cái này gắn vào nó
    [04:38:36] sẽ thành chất nguy hiểm. Thứ hai nữa là
    [04:38:39] chúng ta ngoài cái ăn uống ra thì chúng
    [04:38:41] ta có gì ạ? Có thuốc. các sản phẩm thuốc
    [04:38:43] mà chúng ta uống vào không cần thiết. Ví
    [04:38:46] dụ như paracetamol ghê ngộ độc gát, ví
  ```

### c481

**Decisions:** D10  
**Watch:** [▶ 04:38:41](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16716s)  ·  section start [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s)  
**Summary section:** [04:37:48] Những nguồn nào sinh ra gốc tự do?  
**Final class:** `supported` (pass 1 `supported`, pass 2 `not checked`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Thứ ba là thuốc dùng không cần thiết, sai chỉ định hoặc uống quá đà, ví dụ paracetamol (ngộ độc gan) hoặc corticoid.
- **AFTER:** no correction proposed (record is `supported`).
- **Pass-1 note:** Nội dung về dùng thuốc không cần thiết, sai chỉ định/quá đà và hai ví dụ đều có; thứ ba là thứ tự kể lại của tóm tắt.
- **Surrounding summary claims:**
  - previous (c480): Thứ hai là ăn uống: thực phẩm chứa hóa chất hoặc thuốc trừ sâu, và ăn quá nhiều đường, đạm hoặc chất béo, khi thừa sẽ biến thành gốc tự do.
  - next (c482): Bác sĩ cũng nhắc đến kim loại nặng như chì, thủy ngân và asen.
- **Quotes cited:**
  - [▶ 04:38:41](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16716s) "ta có gì ạ? Có thuốc. các sản phẩm thuốc mà chúng ta uống vào không cần thiết. Ví dụ như paracetamol ghê ngộ độc gát, ví"
  - [▶ 04:38:50](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16725s) "khớp, chúng ta uống đủ thứ xong sẽ uống những các cái gì cocticoid chẳng hạn. Đúng rồi thế rồi nhiều những thuốc khác"
  - [▶ 04:38:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16732s) "nếu chúng ta uống sai chỉ định, chúng tôi uống quá đà sẽ dẫn tới là nó sẽ gắn những cái gốc tự do này vào và lúc ấy"

  Transcript 04:38:26–04:39:22 · [▶ watch from 04:38:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16706s)

  ```text
    [04:38:26] cái thành phần này.
    [04:38:28] >> Những thành phần này khi gắn vào lập tức
    [04:38:30] những cái đó sẽ trở thành
    [04:38:32] >> chất nguy hiểm.
    [04:38:33] >> Vâng.
    [04:38:34] >> Nó gắn tất cả những cái này gắn vào nó
    [04:38:36] sẽ thành chất nguy hiểm. Thứ hai nữa là
    [04:38:39] chúng ta ngoài cái ăn uống ra thì chúng
  ▶ [04:38:41] ta có gì ạ? Có thuốc. các sản phẩm thuốc
  ▶ [04:38:43] mà chúng ta uống vào không cần thiết. Ví
  ▶ [04:38:46] dụ như paracetamol ghê ngộ độc gát, ví
    [04:38:48] dụ như là các cái thuốc mà chúng ta đau
  ▶ [04:38:50] khớp, chúng ta uống đủ thứ xong sẽ uống
  ▶ [04:38:53] những các cái gì cocticoid chẳng hạn.
  ▶ [04:38:55] Đúng rồi thế rồi nhiều những thuốc khác
  ▶ [04:38:57] nếu chúng ta uống sai chỉ định, chúng
  ▶ [04:38:59] tôi uống quá đà sẽ dẫn tới là nó sẽ gắn
  ▶ [04:39:03] những cái gốc tự do này vào và lúc ấy
    [04:39:04] bắt đầu nó nguy hiểm. Cái thứ ba đó là
    [04:39:08] chúng ta rất chú ý là những cái kim loại
    [04:39:09] nặng.
    [04:39:10] >> Vâng. kim loại nặng ví dụ như là chủy
    [04:39:13] trì đúng không ạ? Ví dụ như thủy ngân ví
    [04:39:15] dụ như aen vân vân đúng không ạ? Tất cả
    [04:39:17] những cái kim loại nặng này.
    [04:39:19] >> Thế thì ừ những thành phần này khi mà nó
  ```

### c482

**Decisions:** D10  
**Watch:** [▶ 04:39:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16745s)  ·  section start [▶ 04:37:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16663s)  
**Summary section:** [04:37:48] Những nguồn nào sinh ra gốc tự do?  
**Final class:** `supported` (pass 1 `supported`, pass 2 `not checked`)  
**Speaker:** Bác sĩ Trần Văn Phúc; tóm tắt cũng quy cho bác sĩ.

- **BEFORE (current summary):** Bác sĩ cũng nhắc đến kim loại nặng như chì, thủy ngân và asen.
- **AFTER:** no correction proposed (record is `supported`).
- **Pass-1 note:** Có chì, thủy ngân, asen (bản ghi nhận dạng là trì/aen).
- **Surrounding summary claims:**
  - previous (c481): Thứ ba là thuốc dùng không cần thiết, sai chỉ định hoặc uống quá đà, ví dụ paracetamol (ngộ độc gan) hoặc corticoid.
  - next (c483): Bác sĩ nói những chất này có ba đặc điểm nguy hiểm: không tan nên cơ thể không đào thải được, bám dính chặt vào các thành phần và gây bệnh, và phá hủy các thành phần như đâm thủng màng tế bào.
- **Quotes cited:**
  - [▶ 04:39:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16745s) "Vâng. kim loại nặng ví dụ như là chủy trì đúng không ạ? Ví dụ như thủy ngân ví dụ như aen vân vân đúng không ạ? Tất cả những cái kim loại nặng này."

  Transcript 04:38:55–04:39:35 · [▶ watch from 04:38:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=16735s)

  ```text
    [04:38:55] Đúng rồi thế rồi nhiều những thuốc khác
    [04:38:57] nếu chúng ta uống sai chỉ định, chúng
    [04:38:59] tôi uống quá đà sẽ dẫn tới là nó sẽ gắn
    [04:39:03] những cái gốc tự do này vào và lúc ấy
    [04:39:04] bắt đầu nó nguy hiểm. Cái thứ ba đó là
    [04:39:08] chúng ta rất chú ý là những cái kim loại
    [04:39:09] nặng.
  ▶ [04:39:10] >> Vâng. kim loại nặng ví dụ như là chủy
  ▶ [04:39:13] trì đúng không ạ? Ví dụ như thủy ngân ví
  ▶ [04:39:15] dụ như aen vân vân đúng không ạ? Tất cả
  ▶ [04:39:17] những cái kim loại nặng này.
    [04:39:19] >> Thế thì ừ những thành phần này khi mà nó
    [04:39:23] bị oxy hóa tạo thành gốc tự do, oxy hóa
    [04:39:26] tạo thành gốc tự do thì nó sẽ rất nguy
    [04:39:28] hiểm. Nó nguy hiểm thể hiện ở mấy cái
    [04:39:31] điểm. Điểm thứ nhất là tất cả những gốc
    [04:39:33] tự do gắn với những cái này thì nó lại
  ```

## Part 3. Omissions (47 kept)

Each kept omission is a transcript topic that the summary does not state. Accepting one means a future summary should include it. H/M/L is the auditor's importance judgment.

### o01 [L] Plants' weak antioxidant defense in the autumn analogy

**Decisions:** D3  
**Watch:** [▶ 00:06:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=365s)

- **Timestamp range:** [00:06:10]-[00:06:27]
- **Anchor** [00:06:12]: "cái thành phần để chống lại các cái gốc tự do ở trong các cái loài thực vật vô cùng yếu kém"
- **Why it matters:** The causal link in the autumn analogy: weak plant defenses lead to leaf fall and rotting fruit.
- **Partial coverage only:** c009-c011 give the analogy but not the weak defenses.
- **Source:** batch 01#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:05:57–00:06:37 · [▶ watch from 00:05:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=357s)

  ```text
    [00:05:58] đông với lá vàng rơi, với lá đỏ, với cây
    [00:06:01] rụng lá đó chính là những các cái cơn
    [00:06:03] bão của những các cái yếu tố gọi là chất
    [00:06:07] oxy hóa khử hoặc là các cái gốc tự do.
    [00:06:10] Và trong cái hoàn cảnh đó thì những các
  ▶ [00:06:12] cái thành phần để chống lại các cái gốc
  ▶ [00:06:14] tự do ở trong các cái loài thực vật vô
  ▶ [00:06:17] cùng yếu kém. Và lúc đó cây cối sẽ dẫn
    [00:06:19] tới hiện tượng rụng lá sẽ dẫn tới là hoa
    [00:06:22] quả bắt đầu là chín và thối giữa ra và
    [00:06:25] rụng xuống cũng như là củ quả bắt đầu là
    [00:06:27] đến cái mùa thu hoạch. Đấy chính là cái
    [00:06:29] lý do của gốc tự do ở bên trong cơ thể
    [00:06:32] của các loài thực vật. Và trong cơ thể
    [00:06:34] con người chúng ta cũng vậy. Có thể nói
    [00:06:37] rằng hầu hết tất cả các cái loại bệnh
  ```

### o02 [M] Glutathione framed as the way out of dangerous disease and cancer

**Decisions:** D3  
**Watch:** [▶ 00:07:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=457s)

- **Timestamp range:** [00:07:42]-[00:08:21]
- **Anchor** [00:07:42]: "ông vua để chúng ta thoát khỏi những các cái bệnh hiểm nghèo"
- **Why it matters:** A broad health-benefit framing that a reader should see stated as the doctor's own.
- **Partial coverage only:** c015 and c105 say 'vua' and describe depletion, not this benefit.
- **Source:** batch 01#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:07:27–00:08:07 · [▶ watch from 00:07:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=447s)

  ```text
    [00:07:27] hôm nay sẽ chuyển tải đến quý vị và các
    [00:07:30] bạn từ lý thuyết của gốc tự do như thế
    [00:07:33] nào cho đến những các cái thành phần để
    [00:07:35] chống lại gốc tự do đó ra sao. Và cuối
    [00:07:37] cùng cái trọng tâm của cái chủ điểm ngày
    [00:07:39] hôm nay đó chính là Glutathion tức là
  ▶ [00:07:42] ông vua của chống lại gốc tự do. ông vua
  ▶ [00:07:45] để chúng ta thoát khỏi những các cái
  ▶ [00:07:46] bệnh hiểm nghèo, thoát khỏi những các
    [00:07:48] cái bệnh mãn tính nguy hiểm và đặc biệt
    [00:07:50] chúng ta cũng thoát khỏi những cái tình
    [00:07:52] trạng đó chính là chúng ta không rơi vào
    [00:07:55] cái bệnh lý cực kỳ nguy hiểm mà ai cũng
    [00:07:57] sợ hãi đấy chính là bệnh lý ung thư.
    [00:07:59] thì xuyên suất một cái số phát sóng ngày
    [00:08:02] hôm nay chúng tôi sẽ đề cập tới rất
    [00:08:05] nhiều những cái vấn đề có thể nói là vô
    [00:08:07] cùng khó khăn và tôi cũng muốn rằng
  ```

### o03 [L] Mitochondrion has four compartments

**Decisions:** D3  
**Watch:** [▶ 00:09:31](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=566s)

- **Timestamp range:** [00:09:31]-[00:09:38]
- **Anchor** [00:09:31]: "Có bốn ngăn tất cả"
- **Why it matters:** An anatomical statement made as fact and not captured.
- **Partial coverage only:** c020 describes the mitochondrion without this detail.
- **Source:** batch 01#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:09:16–00:09:56 · [▶ watch from 00:09:16](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=556s)

  ```text
    [00:09:17] ta sinh ra. Thế thì con đường nội sinh
    [00:09:20] này nó được sinh ra như thế nào? Chúng
    [00:09:23] ta sẽ hình dung rằng trong tế bào của
    [00:09:25] chúng ta có một cái bào quan vô cùng
    [00:09:27] quan trọng đó chính là gì ạ? Chính là ti
    [00:09:30] thể đúng không ạ?
  ▶ [00:09:31] >> Ti thể có mấy ngăn này? Có bốn ngăn tất
  ▶ [00:09:33] cả. Và đây chính là cái lò phản ứng hạt
    [00:09:36] nhân và đây cũng chính là cái nhà máy
    [00:09:38] điện. Ở đây là thực hiện tất cả những
    [00:09:41] quá trình trao đổi chất vô cùng quan
    [00:09:43] trọng. Và cái quá trình trao đổi chất
    [00:09:45] đó, trọng tâm của nó chính là chu trình
    [00:09:47] gì ạ?
    [00:09:48] >> Chu trình CRB.
    [00:09:49] >> Chu trình CRB này thực hiện ở trong ti
    [00:09:51] thể và nó sẽ tạo ra cái gì ạ? Cái ATP.
    [00:09:54] >> Vâng.
    [00:09:55] >> ATP đây chính là đồng tiền năng lượng để
  ```

### o04 [M] About 6000 reactions as an endogenous source

**Decisions:** D3  
**Watch:** [▶ 00:11:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=709s)

- **Timestamp range:** [00:11:54]-[00:12:09]
- **Anchor** [00:11:57]: "khoa học đã ghi nhận được có khoảng 6000 phản ứng khoa học"
- **Why it matters:** A quantitative claim behind the endogenous pathway.
- **Partial coverage only:** c029 names the pathway without the figure.
- **Source:** batch 01#4
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:11:42–00:12:22 · [▶ watch from 00:11:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=702s)

  ```text
    [00:11:44] bên trong tế bào. Ngoài ra còn những cái
    [00:11:48] quá trình chuyển hóa đó còn có rất nhiều
    [00:11:50] những cái quá trình kèm theo. Ví dụ như
    [00:11:52] các cái phản ứng hoa hồng trong cơ thể.
    [00:11:54] Trong cơ thể của chúng ta ước chừng đến
  ▶ [00:11:57] giờ phút này thì khoa học đã ghi nhận
  ▶ [00:11:58] được có khoảng 6000 phản ứng khoa học
    [00:12:01] liên tục thực hiện với những cái đơn vị
    [00:12:03] hàng phần nghìn phần vạn phần triệu của
    [00:12:05] dây. Và những phản ứng hóa học thực hiện
    [00:12:07] như thế này cũng là một cái quá trình
    [00:12:09] tạo ra rất nhiều gốc tự do khác nhau.
    [00:12:12] >> Vậy con đường nội sinh là một cái con
    [00:12:14] đường mà từ đó tạo ra vô cùng nhiều gốc
    [00:12:18] tự do ở trong cơ thể của chúng ta. Thế
    [00:12:20] cũng có một cái con đường nội sinh nữa
  ```

### o05 [M] Too little protein as a cause of free radicals

**Decisions:** D3  
**Watch:** [▶ 00:16:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=1009s)

- **Timestamp range:** [00:16:54]-[00:17:07]
- **Anchor** [00:16:54]: "đạn chúng ta ăn sai, ăn không đúng cách, ăn quá nhiều hoặc ăn quá ít cũng là những cái nguyên nhân để gây ra gốc tự do."
- **Why it matters:** Eating too little protein is also named as a cause, not only excess.
- **Partial coverage only:** c033 and c253 cover wrong diet in general and c480 covers excess protein; none states too little protein.
- **Source:** batch 02#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:16:39–00:17:19 · [▶ watch from 00:16:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=999s)

  ```text
    [00:16:41] trên dán thì nó sẽ chuyển hóa thành cái
    [00:16:44] chất béo trung gian. Ngoài mất cân bằng
    [00:16:47] về tỉ lệ thì còn có những cái quá trình
    [00:16:49] mà chúng ta chế biến sai thì chất béo sẽ
    [00:16:51] ảnh hưởng. Cộng với lại ví dụ như đạn
  ▶ [00:16:54] cũng thế. đạn chúng ta ăn sai, ăn không
  ▶ [00:16:56] đúng cách, ăn quá nhiều hoặc ăn quá ít
  ▶ [00:16:58] cũng là những cái nguyên nhân để gây ra
  ▶ [00:17:00] gốc tự do. Đó. Thế thì nh cái con đường
    [00:17:03] ăn uống chúng ta tưởng rằng là ăn tốt
    [00:17:05] nhưng chưa chắc đã là tốt nếu như chúng
    [00:17:07] ta không có cái sự hiểu biết. Thế rồi
    [00:17:09] những các cái ăn uống khác ví dụ như là
    [00:17:12] chúng ta thực hiện những cái chế độ ăn
    [00:17:14] mà mất cân đối về chế độ ăn. Thế hoặc là
    [00:17:17] trong đồ ăn của thức uống của chúng ta
    [00:17:19] không đảm bảo vệ sinh, không đảm bảo an
  ```

### o06 [M] Why the doctor teaches free radicals first

**Decisions:** D3  
**Watch:** [▶ 00:19:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=1135s)

- **Timestamp range:** [00:19:00]-[00:19:09]
- **Anchor** [00:19:00]: "Nhưng mà chúng ta không hiểu gốc tự do là gì thì tôi cho rằng chúng ta sẽ thất bại trong cái công cuộc phòng chống."
- **Why it matters:** His stated reason: without this understanding, prevention fails however much one knows about antioxidants.
- **Partial coverage only:** c016 gives the lesson order only.
- **Source:** batch 02#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:18:45–00:19:25 · [▶ watch from 00:18:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=1125s)

  ```text
    [00:18:45] chúng ta không hiểu gốc tự do là cái gì
    [00:18:47] thì tôi cho rằng là chúng ta sẽ thất bại
    [00:18:50] trong cái chuyện là phòng chống gốc tự
    [00:18:52] do. Chúng ta có tìm hiểu về glutathion
    [00:18:54] đến mấy chăng nữa, giỏi về vitamin E,
    [00:18:57] vitamin C hay là các cái chất gì đấy
  ▶ [00:19:00] gicen vân vân. Nhưng mà chúng ta không
  ▶ [00:19:03] hiểu gốc tự do là gì thì tôi cho rằng
  ▶ [00:19:05] chúng ta sẽ thất bại trong cái công cuộc
  ▶ [00:19:07] phòng chống. Vậy cụ thể gốc tự do nó là
    [00:19:09] cái gì? Chúng ta đi vào từng cái một.
    [00:19:12] Cái đầu tiên, cái gốc tự do đầu tiên
    [00:19:14] quan trọng nhất mà chúng ta cũng lại rất
    [00:19:16] hay gặp đó chính là chất tự gốc tự do có
    [00:19:20] tên là superit.
    [00:19:22] Superit là một cái gốc tự do ban đầu.
    [00:19:25] Khởi điểm ban đầu chúng ta cần phải hiểu
  ```

### o07 [L] Four-generation family model of oxygen's electrons

**Decisions:** D3  
**Watch:** [▶ 00:27:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=1657s)

- **Timestamp range:** [00:27:42]-[00:27:49]
- **Anchor** [00:27:42]: "Đây là một gia đình oxy hạnh phúc."
- **Why it matters:** The teaching model used for every later radical.
- **Partial coverage only:** c040 and c082 give the electrons and the 'happy family' image, not this model.
- **Source:** batch 02#4
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:27:27–00:28:07 · [▶ watch from 00:27:27](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=1647s)

  ```text
    [00:27:27] >> Đây là gia đình có bốn thế hệ. Cái này
    [00:27:30] là chính là 2 P gì ạ? P2. Đó. Thì trong
    [00:27:34] đại gia đình Tứ Đại Đồng Đường này đang
    [00:27:36] có tổng số là bao người tất cả
    [00:27:38] >> 16 người.
    [00:27:39] >> Tổng số bằng 16 người đúng không ạ? Bằng
  ▶ [00:27:42] 16 người. Đây là một gia đình oxy hạnh
  ▶ [00:27:44] phúc. Gia đình oxy hạnh phúc này thì
    [00:27:46] không có chuyện gì xảy ra cả. Đó chính
    [00:27:49] là oxy mà chúng ta hít thở hàng ngày.
    [00:27:51] Chúng ta sinh hoạt hàng ngày bằng chính
    [00:27:54] cái oxy này. Oxy này rất hiền dịu và rất
    [00:27:56] tốt với chúng ta. Tuy nhiên là trong cái
    [00:28:00] quá trình trong cuộc sống, trong thế
    [00:28:02] giới tự nhiên, đặc biệt là trong cơ thể
    [00:28:04] của chúng ta thì lại luôn có những đứa
    [00:28:07] con đi lạc, những đứa con lạc loài. Thế
  ```

### o08 [M] SOD outcome: one family becomes normal oxygen, the other forms H2O2

**Decisions:** D3  
**Watch:** [▶ 00:36:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2177s)

- **Timestamp range:** [00:36:22]-[00:37:59]
- **Anchor** [00:37:57]: "Thì lúc đấy nó sẽ tạo thành oxy già chính là H2O2"
- **Why it matters:** SOD's product is the dangerous H2O2, which changes how c042's 'không còn gây nguy hiểm' reads.
- **Partial coverage only:** c042 and c043 do not link SOD to H2O2.
- **Source:** batch 02#6
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:37:42–00:38:22 · [▶ watch from 00:37:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2262s)

  ```text
    [00:37:42] cướp ngay lập tức.
    [00:37:43] >> Cướp H+. Đúng rồi. Nó cướp H+ thì bây
    [00:37:46] giờ nó sẽ cướp 2H+ để nó xây phòng
    [00:37:49] >> thì lúc đó là trở thành
    [00:37:50] >> nước ạ.
    [00:37:51] >> Không phải nước mà H2O2 chứ.
    [00:37:53] >> À oxy
    [00:37:54] >> là oxy già.
    [00:37:55] >> Vâng.
    [00:37:56] >> Đúng không ạ?
    [00:37:56] >> Vâng.
  ▶ [00:37:57] >> Thì lúc đấy nó sẽ tạo thành oxy già
  ▶ [00:37:59] chính là H2O2 tức là hydrogen.
    [00:38:02] >> Hydrogen beroxit.
    [00:38:04] >> Thế thì cái gia đình này bây giờ cái
    [00:38:06] phòng của nó thì nghe có vẻ là yên ổn
    [00:38:09] bởi vì nó cân bằng về điện tích.
    [00:38:11] >> Vâng. Bởi vì âm dương bây giờ nó cân
    [00:38:13] bằng rồi, nó không còn âm đây nữa. Nhìn
    [00:38:15] bề ngoài thì nó yên ổn nhưng bên trong
    [00:38:18] là hai vợ chồng nó đang ủ mưu rất khủng
    [00:38:21] khiếp.
    [00:38:22] Đấy, nó ủ mưu nó ủ mưu tính đến chuyện
  ```

### o09 [L] Hydroxyl attacks at very high speed

**Decisions:** D3  
**Watch:** [▶ 00:44:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2656s)

- **Timestamp range:** [00:44:21]-[00:44:27]
- **Anchor** [00:44:21]: "Và tấn công với tốc độ siêu nhanh và luôn luôn có tư tưởng để ăn cướp."
- **Why it matters:** Adds speed and severity to the account of the most dangerous radical.
- **Partial coverage only:** c050 and c476 say mobile and agile, not this speed.
- **Source:** batch 03#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:44:06–00:44:46 · [▶ watch from 00:44:06](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2646s)

  ```text
    [00:44:07] nguy hiểm. Tiếp nữa là nó quá cơ động.
    [00:44:10] Vậy thì nhóm hyroxin là nhóm mà nó tấn
    [00:44:14] công tất cả mọi thứ trong cơ thể chúng
    [00:44:16] ta. Nó không trừ một cái gì hết cả.
    [00:44:18] >> Vâng.
    [00:44:19] >> Cái gì nó cũng tấn công được.
    [00:44:20] >> Vâng.
  ▶ [00:44:21] >> Và tấn công với tốc độ siêu nhanh và
  ▶ [00:44:23] luôn luôn có tư tưởng để ăn cướp. Ăn
    [00:44:25] cướp cái gì?
    [00:44:27] Ăn cướp
    [00:44:27] >> ăn cướp electron và hyro.
    [00:44:29] >> Vâng.
    [00:44:30] >> Chúng ta nhớ rằng gốc tự do luôn luôn đi
    [00:44:32] cướp electron và hyro.
    [00:44:34] >> Vâng.
    [00:44:35] >> Hyro cộng.
    [00:44:36] >> Vâng.
    [00:44:36] >> Cướp electron để gì ạ? Để nó kẹp đôi. Nó
    [00:44:39] không cô đơn.
    [00:44:40] >> Không bao giờ nó chấp nhận cô đơn cả.
    [00:44:42] >> Thứ hai nữ là cướp hyro để nó tạo thành
    [00:44:44] căn phòng ấm áp.
    [00:44:45] >> Vâng.
    [00:44:46] >> Hạnh phúc của nó. Đấy chính là cái quá
  ```

### o10 [M] Doctor accepts the host's remark that ozone is H2O2

**Decisions:** D3  
**Watch:** [▶ 00:45:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2728s)

- **Timestamp range:** [00:45:33]-[00:45:40]
- **Anchor** [00:45:33]: "Ozon chính là H2O2 cũng không sai đâu."
- **Why it matters:** A chemical statement the doctor makes on air. It is recorded as spoken, with no correction here.
- **Source:** batch 03#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:45:18–00:45:58 · [▶ watch from 00:45:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2718s)

  ```text
    [00:45:19] nguy hiểm. Thế còn một lúc ấy Khánh lành
    [00:45:22] tôi định là thôi không nói về cái ozone
    [00:45:24] như thôi nói nốt. Ozon nó chính là một
    [00:45:26] cái kẻ cướp thứ tư.
    [00:45:27] >> Vâng.
    [00:45:28] >> Kẻ cướp thứ tư đó chính là ozone. Ozon
    [00:45:31] thì bản chất gánh lành nói đúng rồi.
  ▶ [00:45:33] Ozon chính là H2O2 cũng không sai đâu.
    [00:45:36] Thế nhưng mà ta tách riêng nó ra thành
    [00:45:38] ozone.
    [00:45:40] Ozon hay còn gọi là O3 đúng không ạ?
    [00:45:42] Vâng.
    [00:45:43] >> Và chúng ta nhớ rằng đây là cái phản ứng
    [00:45:44] mà khi có tia lửa điện khi mà tiếng sét
    [00:45:47] nó đánh xuống ấy
    [00:45:48] >> thì không khí bắt đầu xuất hiện cái khí
    [00:45:50] ozon là O3.
    [00:45:51] >> Vâng.
    [00:45:51] >> Thì ozon thì nó lại là như thế này.
    [00:45:54] Chúng ta hình dung rằng oxy hạnh phúc đó
    [00:45:57] chính là chỉ có hai thôi.
  ```

### o11 [M] Danger ranking of the first three radicals

**Decisions:** D3  
**Watch:** [▶ 00:48:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2892s)

- **Timestamp range:** [00:48:17]-[00:48:22]
- **Anchor** [00:48:17]: "Hyroen cái thứ hai thì lại đứng thứ hai."
- **Why it matters:** Hydroxyl first, hydrogen peroxide second, superoxide less dangerous.
- **Partial coverage only:** c476 gives only hydroxyl's rank.
- **Source:** batch 03#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:48:02–00:48:42 · [▶ watch from 00:48:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2882s)

  ```text
    [00:48:02] >> Vâng.
    [00:48:02] >> Tôi nhắc lại là ba gốc tự do đầu tiên.
    [00:48:06] Gốc tự do thứ nhất là superocit, gốc tự
    [00:48:09] do thứ hai là hyrogen peroit và gốc tự
    [00:48:12] do thứ ba là hyroxin. Thì hyroxin nguy
    [00:48:15] hiểm số một đúng không ạ?
    [00:48:16] >> Vâng.
  ▶ [00:48:17] >> Hyroen cái thứ hai thì lại đứng thứ hai.
    [00:48:20] Còn cái đầu thì là nguy hiểm. Ít nguy
    [00:48:22] hiểm hơn. Thế ba gốc tự do này nó sẽ tấn
    [00:48:25] công gì? tấn công màng tế bào, tấn công
    [00:48:28] protein và tấn công ADN và từ đó nó sinh
    [00:48:31] ra chuyện.
    [00:48:32] >> Nó tấn công nó sẽ như thế nào? Đầu tiên
    [00:48:35] tôi nói là tấn công màng tế bào đã. Màng
    [00:48:38] tế bào thì nó được cấu tạo bởi các cái
    [00:48:42] gì ạ? Các lipit màng tức là chất béo
  ```

### o12 [L] Why hydroxyl robs: it becomes harmless H2O

**Decisions:** D3  
**Watch:** [▶ 00:49:51](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2986s)

- **Timestamp range:** [00:49:51]-[00:50:08]
- **Anchor** [00:50:01]: "nó trở thành gì ạ? Trở thành H2O về H2O thì hiền lành rồi."
- **Why it matters:** Explains the purpose of the robbing cycle.
- **Partial coverage only:** c041 and c083 say 'ổn định', not this end state.
- **Source:** batch 03#4
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:49:46–00:50:26 · [▶ watch from 00:49:46](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=2986s)

  ```text
    [00:49:46] >> Hyxin tức là OH. Thì bây giờ nó sẽ cướp
    [00:49:48] hai cái thành phần. Cướp cái thứ nhất đó
    [00:49:51] là
    [00:49:51] >> electron. electron 1e cướp thứ hai là
    [00:49:54] cướp H+ đúng rồi
    [00:49:55] >> đấy nó cướp hai cái này
    [00:49:57] >> cướp 1e và cướp hai cướp H+ để cuối cùng
  ▶ [00:50:01] nó trở thành gì ạ? Trở thành H2O về H2O
  ▶ [00:50:04] thì hiền lành rồi.
    [00:50:05] >> Vâng [khịt mũi]
    [00:50:06] >> không còn nguy hiểm nữa. Mục đích của nó
    [00:50:08] là đi cướp như vậy.
    [00:50:09] >> Vâng.
    [00:50:09] >> Thế vậy thì nó xông thẳng vào cái lipit
    [00:50:12] màng và nó sẽ cướp electron và cướp H+
    [00:50:16] của chính cái lipit màng. Và khi nó cướp
    [00:50:20] như vậy thì nó sẽ tạo ra cái sản phẩm đó
    [00:50:22] chính là L đang có đang quyết đi
    [00:50:26] electron tức là L dấu chấm. Đúng rồi.
  ```

### o13 [L] Lipid peroxidation intermediates are all radicals

**Decisions:** D3  
**Watch:** [▶ 00:52:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3134s)

- **Timestamp range:** [00:52:19]-[00:52:30]
- **Anchor** [00:52:19]: "cho đến lo trừ đến loh tất cả đều là gốc tự do."
- **Why it matters:** The summary names only L· and 'lipit peroxit', while the doctor lists three forms.
- **Partial coverage only:** c058 and c067 cover part of this.
- **Source:** batch 03#5
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:52:04–00:52:44 · [▶ watch from 00:52:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3124s)

  ```text
    [00:52:04] >> Đi cướp H+ thì nó sẽ trở thành gì ạ? Loh
    [00:52:09] loh thì bây giờ H+ này lại xu hướng đi
    [00:52:12] kiếp cướp electron tiếp. Nó cứ thành một
    [00:52:14] cái vòng luần quẩn cướp H+ cướp
    [00:52:15] electron. Rồi chúng ta đã hình dung cái
    [00:52:18] này chưa?
    [00:52:18] >> Vâng.
  ▶ [00:52:19] >> Từ đây tất cả những cái này chấm này cho
  ▶ [00:52:22] đến lo trừ đến loh tất cả đều là gốc tự
  ▶ [00:52:27] do.
    [00:52:27] >> Vâng.
    [00:52:27] >> Gốc tự do này lúc này nó cướp E lúc kia
    [00:52:30] nó cướp H+. Lúc này cướp E lúc kia lại
    [00:52:32] cướp H+. Cứ thế nó liên tục.
    [00:52:34] >> Vâng.
    [00:52:34] >> Cướp ở đâu? nó sẽ cướp ngay chính phân
    [00:52:36] tử lipit bên cạnh.
    [00:52:38] >> Vâng.
    [00:52:39] >> Vậy màng tế bào thì chúng ta sẽ thấy
    [00:52:41] rằng màng tế bào là các phân tử lipit nó
    [00:52:43] xếp vào. Vậy mỗi phân tử lipit nó giống
  ```

### o14 [L] Membrane attack called the worst and most brutal

**Decisions:** D3  
**Watch:** [▶ 00:54:06](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3241s)

- **Timestamp range:** [00:54:06]-[00:54:21]
- **Anchor** [00:54:11]: "tấn công khủng khiếp nhất và đây là cuộc cướp tàn bạo nhất."
- **Why it matters:** Severity framing for membrane attack.
- **Partial coverage only:** c064 and c066 describe collapse, not this ranking.
- **Source:** batch 03#6
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:53:56–00:54:36 · [▶ watch from 00:53:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3236s)

  ```text
    [00:53:56] màn tế bào ngay lập tức nó sụp đổ hệ
    [00:53:58] thống.
    [00:53:59] >> Vâng.
    [00:53:59] >> Với một tốc độ rất nhanh nó giống như là
    [00:54:01] đám cháy của bãi xăng. Không có con
    [00:54:03] đường nào ngăn chặn nữa cả và lập tức sẽ
    [00:54:06] hủy hoại tế bào ngay lập tức. Thì đây là
    [00:54:09] cái mà tấn công vào lipit màng tế bào là
  ▶ [00:54:11] tấn công khủng khiếp nhất và đây là cuộc
  ▶ [00:54:14] cướp tàn bạo nhất. Nó tạo thành ra cả
    [00:54:17] một làng xóm đen cướp với nhau và dẫn
    [00:54:19] tới sụp đổ hết cả một hệ thống tế bào.
    [00:54:21] >> Vâng.
    [00:54:22] >> Đó. Thế thì gốc tự do thứ năm đó chính
    [00:54:24] là lipit peroxit. Gốc tự do thứ sáu là
    [00:54:29] protein cũng lại đi theo con đường y hệt
    [00:54:31] như vậy không khác gì cả. Y hệt như là
    [00:54:33] lipit. Vậy sáu là nó tấn công vào
  ```

### o15 [M] DNA attack has two harms at once

**Decisions:** D3  
**Watch:** [▶ 00:58:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3515s)

- **Timestamp range:** [00:58:40]-[00:59:01]
- **Anchor** [00:58:44]: "ta nhớ rằng ADN nó còn nguy hiểm hơn ở chỗ một là gì ạ? Là nó tạo ra gốc tự do."
- **Why it matters:** The doctor's summary of why DNA damage is worse: it creates radicals and mutations.
- **Partial coverage only:** c073-c079 give each route, not this framing.
- **Source:** batch 04#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 00:58:29–00:59:09 · [▶ watch from 00:58:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3509s)

  ```text
    [00:58:29] >> mà đột biến gen này thì sẽ gây ra một là
    [00:58:32] bệnh nguy hiểm, bệnh hiếm đúng không ạ?
    [00:58:34] >> Hai là gây ra gì ạ? Ung thư. Nó gây ra
    [00:58:38] những các cái con đường đó.
    [00:58:40] >> Vâng.
    [00:58:40] >> Thì đây chính là tấn công vào ADN. Vậy
  ▶ [00:58:44] ta nhớ rằng ADN nó còn nguy hiểm hơn ở
  ▶ [00:58:46] chỗ một là gì ạ? Là nó tạo ra gốc tự do.
    [00:58:52] Hai là nó gây ra đột biến gì ạ? Đột biến
    [00:58:54] gen mà đột biến là từ cái guanin này,
    [00:58:58] >> từ cái mã mật mã di truyền này nó rất dễ
    [00:59:01] bị nhầm với lại T.
    [00:59:02] >> Vâng.
    [00:59:03] >> Từ đấy trở đi là các cái tổng hợp sau
    [00:59:05] này nó bị nhầm, nó tạo nên đột biến gen
    [00:59:07] và sinh ra đủ các cái thứ bệnh, bệnh
    [00:59:09] hiếm, bệnh ung thư. Vậy tổng số chúng ta
  ```

### o16 [M] Why the sacrificial step alone is not enough

**Decisions:** D3  
**Watch:** [▶ 01:01:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3709s)

- **Timestamp range:** [01:01:54]-[01:02:19]
- **Anchor** [01:01:59]: "hai cái quá trình cảm tử này nó sẽ tạo thành một loạt gốc tự do. Tiếp nữa là bản thân gốc tự do tấn công nhưng cái này không đủ để chống trả lại."
- **Why it matters:** Explains why the body moves to the second step.
- **Partial coverage only:** c085-c087 list the steps only.
- **Source:** batch 04#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:01:44–01:02:24 · [▶ watch from 01:01:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3704s)

  ```text
    [01:01:45] electron, nhường H+ để nói trung hòa. Và
    [01:01:48] sau đó bắt đầu cái này quay trở lại các
    [01:01:49] cái vòng tuần hoàn của nó.
    [01:01:51] >> Vâng.
    [01:01:51] >> Thế thì cảm tử là những chất này. Đấy là
    [01:01:54] bước số một là cảm tử ra để cánh đỡ. Sau
    [01:01:57] khi cảm tử ra cánh đỡ rồi thì bước thứ
  ▶ [01:01:59] hai cái quá trình cảm tử này nó sẽ tạo
  ▶ [01:02:02] thành một loạt gốc tự do. Tiếp nữa là
  ▶ [01:02:04] bản thân gốc tự do tấn công nhưng cái
  ▶ [01:02:06] này không đủ để chống trả lại. Thì lúc
    [01:02:08] đó đến bước thứ hai là các cái chất, các
    [01:02:12] cái gọi là đội đặc nhiệm đấy. Các đội
    [01:02:15] đặc nhiệm đội đặc nhiệm sẽ thực hiện ra
    [01:02:19] để mà giải quyết gốc tự do là ROS.
    [01:02:22] đội đặc nhiệm đi ra để trung hòa cái gốc
  ```

### o17 [M] Catalase uses Fe2+ to destroy radical 'bombs'

**Decisions:** D3  
**Watch:** [▶ 01:04:05](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3840s)

- **Timestamp range:** [01:04:05]-[01:04:26]
- **Anchor** [01:04:10]: "chính là thanh kiếm sắt hai cộng. thanh kiếm sắt 2+ để nó phá hủy nó nó làm nổ tung những các quả bom gốc tự do ra."
- **Why it matters:** Fe2+ was earlier named as what splits H2O2, so this role matters. Found in batches 04 and 05 and merged here.
- **Partial coverage only:** c095 and c101 omit the Fe2+.
- **Source:** batch 04#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:03:55–01:04:35 · [▶ watch from 01:03:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3835s)

  ```text
    [01:03:55] tinh nhuệ cực kỳ tinh nhuệ đứng ra để
    [01:03:57] trung hòa gốc tự do. Nhưng thành phần
    [01:04:00] này nó đứng im một chỗ. Chỉ khi nào gốc
    [01:04:03] tự do quá lớn nó mới trung hòa, nó mới
    [01:04:05] đứng ra để nó giải quyết. Và Catala nó
    [01:04:08] có một cái nó sử dụng thanh kiếm đó
  ▶ [01:04:10] chính là thanh kiếm sắt hai cộng.
  ▶ [01:04:12] thanh kiếm sắt 2+ để nó phá hủy nó nó
  ▶ [01:04:16] làm nổ tung những các quả bom gốc tự do
  ▶ [01:04:18] ra. Nhưng cái này chỉ là đánh những trận
    [01:04:20] đánh lớn là gốc tự do. Đối với lại
    [01:04:24] katana là một trong những các cái thành
    [01:04:26] phần để trung hòa chống lại gốc tự do.
    [01:04:28] Thành phần thứ hai đó chính là vitamin
    [01:04:31] E.
    [01:04:33] Thì vitamin E cũng tham gia vào cái trận
  ```

### o18 [L] Sacrificial substances return to their cycle

**Decisions:** D3  
**Watch:** [▶ 01:01:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3700s)

- **Timestamp range:** [01:01:45]-[01:01:51]
- **Anchor** [01:01:48]: "sau đó bắt đầu cái này quay trở lại các cái vòng tuần hoàn của nó."
- **Why it matters:** They are described as recycled, not used up.
- **Source:** batch 04#4
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:01:33–01:02:13 · [▶ watch from 01:01:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3693s)

  ```text
    [01:01:33] một cái thành phần chất cảm tử. Thì ba
    [01:01:35] cái thành phần cảm tử này đầu tiên nó
    [01:01:38] xung phong ra để sẵn sàng chấp nhận cho
    [01:01:41] gốc tự do tấn công.
    [01:01:42] >> Vâng.
    [01:01:43] >> Và trung hòa. Những cái này nó sẽ nhường
    [01:01:45] electron, nhường H+ để nói trung hòa. Và
  ▶ [01:01:48] sau đó bắt đầu cái này quay trở lại các
  ▶ [01:01:49] cái vòng tuần hoàn của nó.
    [01:01:51] >> Vâng.
    [01:01:51] >> Thế thì cảm tử là những chất này. Đấy là
    [01:01:54] bước số một là cảm tử ra để cánh đỡ. Sau
    [01:01:57] khi cảm tử ra cánh đỡ rồi thì bước thứ
    [01:01:59] hai cái quá trình cảm tử này nó sẽ tạo
    [01:02:02] thành một loạt gốc tự do. Tiếp nữa là
    [01:02:04] bản thân gốc tự do tấn công nhưng cái
    [01:02:06] này không đủ để chống trả lại. Thì lúc
    [01:02:08] đó đến bước thứ hai là các cái chất, các
    [01:02:12] cái gọi là đội đặc nhiệm đấy. Các đội
  ```

### o19 [M] Safety: viewer gives supplements to her teenage children

**Decisions:** D3, D9  
**Watch:** [▶ 01:26:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5163s)

- **Timestamp range:** [01:26:08]-[01:26:27]
- **Anchor** [01:26:08]: "Em cũng cho các con ở tuổi vị thành niên uống theo và nghiên cứu điều chỉnh theo thể trạng từng cháu."
- **Why it matters:** Self-directed use in minors, adjusted by the parent. Viewer self-report.
- **Source:** batch 06#6
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:25:53–01:26:33 · [▶ watch from 01:25:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5153s)

  ```text
    [01:25:53] giảm 4 kg một cách khỏe mạnh, không bị
    [01:25:56] là người nhờ uống đủ bộ vì chất. Em cao
    [01:25:59] 1,6 từ khung 56 đến 57 kg, sau ăn nay
    [01:26:04] còn 52 đến 53 kg.
  ▶ [01:26:08] Em cũng cho các con ở tuổi vị thành niên
  ▶ [01:26:10] uống theo và nghiên cứu điều chỉnh theo
  ▶ [01:26:12] thể trạng từng cháu. Các con ở xa nhưng
    [01:26:15] khi tuân thủ ăn uống đầy đủ thì nỗi lo
    [01:26:18] về sức khỏe của con hầu như được giải
    [01:26:20] tỏa.
    [01:26:22] Em viết hơi dài với hy vọng chia sẻ niềm
    [01:26:24] vui tới bác sĩ Phúc, MC Khánh lành cùng
    [01:26:27] toàn thể ekip. đồng thời tiếp thêm động
    [01:26:29] lực cho các khán giả mới. Nếu em may mắn
    [01:26:32] được bác sĩ giải thích giúp cơ chế các
  ```

### o20 [M] Safety: side effects of neurological and anti-epileptic drugs

**Decisions:** D3, D9  
**Watch:** [▶ 01:27:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5271s)

- **Timestamp range:** [01:27:56]-[01:28:26]
- **Anchor** [01:27:59]: "nhưng bệnh chỉ đỡ khi dùng thuốc thần kinh và chống động kinh. Những loại thuốc gây nhiều tác dụng phụ như là hạ huyết áp, ngứa toàn thân và đau dạ dày."
- **Why it matters:** Reported drug side effects: low blood pressure, itching and stomach pain. Viewer self-report.
- **Source:** batch 06#7
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:27:44–01:28:24 · [▶ watch from 01:27:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5264s)

  ```text
    [01:27:45] đau kéo dài cả tháng với triệu chứng mệt
    [01:27:48] mỏi, chóng mặt, chân tay tự co gồng cho
    [01:27:52] dễ chịu.
    [01:27:53] Mỗi đợt như vậy tôi đều sút cân, mặt mũi
    [01:27:56] hốc hác. Dù khám nhiều giáo sư, bác sĩ
  ▶ [01:27:59] nhưng bệnh chỉ đỡ khi dùng thuốc thần
  ▶ [01:28:01] kinh và chống động kinh. Những loại
  ▶ [01:28:04] thuốc gây nhiều tác dụng phụ như là hạ
  ▶ [01:28:06] huyết áp, ngứa toàn thân và đau dạ dày.
    [01:28:11] Tôi sinh ba cháu, cháu thứ ba mới gần ba
    [01:28:14] tuổi, sinh con khi tuổi đã cao, cộng với
    [01:28:17] sức khỏe vốn yếu lại không bổ sung vi
    [01:28:19] chất
    [01:28:21] bất kỳ một vi chất nào cả. Vì mất niềm
    [01:28:23] tin vào thực phẩm chức năng và ăn uống
  ```

### o21 [M] Safety: fear of Western medicine from online healing groups

**Decisions:** D3, D9  
**Watch:** [▶ 01:28:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5309s)

- **Timestamp range:** [01:28:34]-[01:28:56]
- **Anchor** [01:28:34]: "Tôi tìm đến các nhóm chữa lành tự nhiên trên mạng và tin vào những lời hù dọa thiếu khoa học về tây y nên càng thêm sợ hãi."
- **Why it matters:** A misinformation risk the viewer herself names as unscientific.
- **Source:** batch 06#9
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:28:19–01:28:59 · [▶ watch from 01:28:19](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5299s)

  ```text
    [01:28:19] chất
    [01:28:21] bất kỳ một vi chất nào cả. Vì mất niềm
    [01:28:23] tin vào thực phẩm chức năng và ăn uống
    [01:28:26] kiêng khem quá mức. Tôi bị thiếu sữa
    [01:28:28] nuôi con. Căn bệnh đau nửa đầu xuất hiện
    [01:28:31] dày hơn khiến tôi bị căng thẳng và mệt
  ▶ [01:28:34] mỏi. Tôi tìm đến các nhóm chữa lành tự
  ▶ [01:28:37] nhiên trên mạng và tin vào những lời hù
  ▶ [01:28:40] dọa thiếu khoa học về tây y nên càng
  ▶ [01:28:43] thêm sợ hãi.
    [01:28:45] Cho đến một ngày thức dậy, toàn thân tôi
    [01:28:47] bị co cứng nhưng đầu óc tôi vẫn đủ tỉnh
    [01:28:50] táo để gọi người nhà đưa đi cấp cứu. Đến
    [01:28:53] viện, tôi được truyền canxi và chẩn đoán
    [01:28:56] làm mắc trầm cảm sau sinh.
    [01:28:58] Chuỗi ngày sau đó, tôi mang cơ thể kiệt
  ```

### o22 [M] Safety: whole-body rigidity, emergency care and IV calcium

**Decisions:** D3, D9  
**Watch:** [▶ 01:28:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5320s)

- **Timestamp range:** [01:28:45]-[01:29:05]
- **Anchor** [01:28:45]: "toàn thân tôi bị co cứng nhưng đầu óc tôi vẫn đủ tỉnh táo để gọi người nhà đưa đi cấp cứu. Đến viện, tôi được truyền canxi"
- **Why it matters:** Safety: she woke with her whole body rigid and needed emergency care, right after her account of fearing Western medicine (o21). Viewer self-report.
- **Partial coverage only:** c136 gives the diagnosis only.
- **Source:** batch 06#10
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:28:30–01:29:10 · [▶ watch from 01:28:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5310s)

  ```text
    [01:28:31] dày hơn khiến tôi bị căng thẳng và mệt
    [01:28:34] mỏi. Tôi tìm đến các nhóm chữa lành tự
    [01:28:37] nhiên trên mạng và tin vào những lời hù
    [01:28:40] dọa thiếu khoa học về tây y nên càng
    [01:28:43] thêm sợ hãi.
  ▶ [01:28:45] Cho đến một ngày thức dậy, toàn thân tôi
  ▶ [01:28:47] bị co cứng nhưng đầu óc tôi vẫn đủ tỉnh
  ▶ [01:28:50] táo để gọi người nhà đưa đi cấp cứu. Đến
  ▶ [01:28:53] viện, tôi được truyền canxi và chẩn đoán
    [01:28:56] làm mắc trầm cảm sau sinh.
    [01:28:58] Chuỗi ngày sau đó, tôi mang cơ thể kiệt
    [01:29:01] quệ đi khám tất cả các bệnh viện lớn,
    [01:29:03] nhưng kết luận chung vẫn chỉ là trầm cảm
    [01:29:05] sau sinh. Vì đang cho con bú nên tôi
    [01:29:09] không dùng thuốc bệnh và được giáo sư
  ```

### o23 [M] Nutrition from pregnancy

**Decisions:** D3  
**Watch:** [▶ 01:41:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6058s)

- **Timestamp range:** [01:41:03]-[01:42:03]
- **Anchor** [01:41:24]: "ngay từ bé ăn uống khoa học ngay từ khi nằm trong bụng mẹ mà mẹ bổ sung vi chất tốt bổ sung các cái dưỡng chất hài hòa đứa con đẻ ra sẽ thông minh sẽ xinh đẹp sẽ giỏi rang sẽ mọi cái nó sẽ tốt đẹp và"
- **Why it matters:** Extends the advice to the mother before birth, with outcome claims about the child.
- **Partial coverage only:** c213 covers 'từ nhỏ' only.
- **Source:** batch 09#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:41:09–01:41:49 · [▶ watch from 01:41:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6069s)

  ```text
    [01:41:09] từng khối vi chất và đi sâu hơn tính
    [01:41:11] từng gam từng lạng các thứ ra một chúng
    [01:41:13] ta phải như thế và chúng ta bổ sung vi
    [01:41:15] chất nó đầy đủ thế thì đã đang ở cái lứa
    [01:41:18] tuổi của các bạn học sinh là các bạn sẽ
    [01:41:20] hấp thu các cái chất rất tốt nếu chúng
    [01:41:22] ta thực hiện chế độ ăn uống khoa học
  ▶ [01:41:24] ngay từ bé ăn uống khoa học ngay từ khi
  ▶ [01:41:26] nằm trong bụng mẹ mà mẹ bổ sung vi chất
  ▶ [01:41:28] tốt bổ sung các cái dưỡng chất hài hòa
  ▶ [01:41:31] đứa con đẻ ra sẽ thông minh sẽ xinh đẹp
  ▶ [01:41:34] sẽ giỏi rang sẽ mọi cái nó sẽ tốt đẹp và
    [01:41:37] cuối cùng các bạn cũng lại duy trì một
    [01:41:38] cái cuộc sống tốt thay vì đi chạy theo
    [01:41:41] các cái bạn khác ở trong nhà trường
    [01:41:44] chúng ta hãy cùng tạo dựng lên đầu tiên
    [01:41:46] bản thân mình thật tốt đã sau đó lan tỏa
    [01:41:48] những cái kiến thức tốt đó những cái
  ```

### o24 [L] Spreading nutrition knowledge and school seminars

**Decisions:** D3  
**Watch:** [▶ 01:41:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6099s)

- **Timestamp range:** [01:41:44]-[01:42:03]
- **Anchor** [01:41:44]: "chúng ta hãy cùng tạo dựng lên đầu tiên bản thân mình thật tốt đã sau đó lan tỏa những cái kiến thức tốt đó những cái hành vi đó cho các bạn xung quanh thế"
- **Why it matters:** A community-education proposal, beyond individual diet.
- **Source:** batch 09#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:41:29–01:42:09 · [▶ watch from 01:41:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6089s)

  ```text
    [01:41:31] đứa con đẻ ra sẽ thông minh sẽ xinh đẹp
    [01:41:34] sẽ giỏi rang sẽ mọi cái nó sẽ tốt đẹp và
    [01:41:37] cuối cùng các bạn cũng lại duy trì một
    [01:41:38] cái cuộc sống tốt thay vì đi chạy theo
    [01:41:41] các cái bạn khác ở trong nhà trường
  ▶ [01:41:44] chúng ta hãy cùng tạo dựng lên đầu tiên
  ▶ [01:41:46] bản thân mình thật tốt đã sau đó lan tỏa
  ▶ [01:41:48] những cái kiến thức tốt đó những cái
  ▶ [01:41:50] hành vi đó cho các bạn xung quanh thế
    [01:41:52] rồi tiến tới là trong cả lớp xong sau đó
    [01:41:55] đến cả trường đến tất cả các cái hệ
    [01:41:57] thống giáo dục xong lan ra toàn xã hội.
    [01:41:59] Tại sao các bạn không dành những các cái
    [01:42:01] buổi seminar nói về cái chuyện ăn uống,
    [01:42:03] nói về các cái chuyện dinh dưỡng. Chúng
    [01:42:05] ta có những cái kiến thức đó thay đổi
    [01:42:07] được lối sống, thay đổi được hành vi học
  ```

### o25 [M] Arrhythmia and AV block linked to startling and sleep paralysis

**Decisions:** D3  
**Watch:** [▶ 01:50:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6644s)

- **Timestamp range:** [01:50:49]-[01:51:02]
- **Anchor** [01:50:49]: "Những các cái nhịp tim nó loạn nhịp cái gì? Block nhĩ thất thế rồi ngoại tâm thu thế rồi tạo nên cái sự giật mình, tạo nên bóng đè. Tất cả những cái đó tôi đã"
- **Why it matters:** A mechanism claim drawn from the doctor's clinical experience.
- **Partial coverage only:** c455 links radicals to sleep paralysis and heart rate, not this.
- **Source:** batch 10#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:50:34–01:51:14 · [▶ watch from 01:50:34](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6634s)

  ```text
    [01:50:35] đã từng nhìn thấy, tôi đã chưa từng chạm
    [01:50:37] vào những trái tim đang sống đập trong
    [01:50:39] lồng ngực mà chúng tôi đã mở lồng ngực
    [01:50:41] ra để chúng tôi can thiệp, chúng tôi mổ
    [01:50:43] nó sẽ khác hoàn toàn. Tôi nhìn thấy
    [01:50:45] những cái trái tim đập, những cái nhịp
    [01:50:46] đập lỗi như là của các bác bình luận đó.
  ▶ [01:50:49] Những các cái nhịp tim nó loạn nhịp cái
  ▶ [01:50:52] gì? Block nhĩ thất thế rồi ngoại tâm thu
  ▶ [01:50:54] thế rồi tạo nên cái sự giật mình, tạo
  ▶ [01:50:56] nên bóng đè. Tất cả những cái đó tôi đã
    [01:50:59] nhìn thấy những cái nhịp tim trên cái
    [01:51:00] điện tâm đồ. Tôi đã nghe cái tiếng tim
    [01:51:02] đó. Tôi đã sờ vào những cái trái tim đó
    [01:51:04] và tôi đã hiểu được đến cái bản chất vấn
    [01:51:06] đề đó là thiếu vi chất nó tạo nên cái
    [01:51:08] gì. Vậy thì khi tôi viết ra nó sẽ đảm
    [01:51:12] bảo rằng những điều tôi viết nó rất thực
    [01:51:14] tế và nó sâu sắc. Cho nên đến giờ phút
  ```

### o26 [M] Cell and molecular medicine versus treating symptoms

**Decisions:** D3  
**Watch:** [▶ 01:53:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6820s)

- **Timestamp range:** [01:53:45]-[01:54:34]
- **Anchor** [01:53:55]: "sức khỏe toàn diện, đi vào y học chính xác, đi vào y học tế bào, đi vào y học phân tử, đi vào cái nền gốc rễ chứ chúng tôi không còn đi ở cái phần ngọn đó chính là chờ đợi bệnh tật nó xảy ra rồi. Nó thành triệu chứng, nó gây tổn thương thực thể rồi chúng ta mới đi xem xét về chữa phần ngọn. thì chúng tôi đang đi có"
- **Why it matters:** States the method he advocates, against waiting for symptoms.
- **Partial coverage only:** c244 and c218 give parts of this.
- **Source:** batch 10#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:53:40–01:54:20 · [▶ watch from 01:53:40](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6820s)

  ```text
    [01:53:42] chia sẻ những cái cảm xúc, những cái suy
    [01:53:43] nghĩ của những cái người làm trong nghề
    [01:53:45] y. Thì tôi cũng rất chia sẻ với các bạn
    [01:53:48] là đôi khi như những cái số trước tôi đã
    [01:53:51] nói là tôi Khánh lành cũng như tất cả
    [01:53:53] các anh chị em đi vào trong cái lĩnh vực
  ▶ [01:53:55] sức khỏe toàn diện, đi vào y học chính
  ▶ [01:53:58] xác, đi vào y học tế bào, đi vào y học
  ▶ [01:54:00] phân tử, đi vào cái nền gốc rễ chứ chúng
  ▶ [01:54:03] tôi không còn đi ở cái phần ngọn đó
  ▶ [01:54:05] chính là chờ đợi bệnh tật nó xảy ra rồi.
  ▶ [01:54:08] Nó thành triệu chứng, nó gây tổn thương
  ▶ [01:54:10] thực thể rồi chúng ta mới đi xem xét về
  ▶ [01:54:12] chữa phần ngọn. thì chúng tôi đang đi có
    [01:54:14] con đường đó là đi vào bản chất vấn đề,
    [01:54:17] đi vào gốc tích vấn đề, nhìn nó ở đa
    [01:54:20] phương diện như lúc nãy tôi nói với bạn
  ```

### o27 [L] Number of supporters as a test of a right or wrong path

**Decisions:** D3  
**Watch:** [▶ 01:57:38](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7053s)

- **Timestamp range:** [01:57:38]-[01:58:11]
- **Anchor** [01:57:41]: "lại, nếu con đường mà chúng ta đi chỉ có một vài người đi thôi, cùng với chúng ta thôi, còn tất cả những người khác đều ngược lại chiều của chúng ta thì con đường đó là con đường sai, con đường thất bại, con đường không đúng. Tiếp nữa"
- **Why it matters:** His argument for judging the work by support and obstacles.
- **Partial coverage only:** c238 says only to go step by step.
- **Source:** batch 10#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:57:26–01:58:06 · [▶ watch from 01:57:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7046s)

  ```text
    [01:57:28] một cái con đường, một cái việc làm mà
    [01:57:30] có rất rất nhiều người ủng hộ, có hàng
    [01:57:34] trăm hàng ngàn người ủng hộ nhưng chỉ có
    [01:57:36] một vài người không ủng hộ thì con đường
    [01:57:38] đó là con đường thành công. Nhưng ngược
  ▶ [01:57:41] lại, nếu con đường mà chúng ta đi chỉ có
  ▶ [01:57:45] một vài người đi thôi, cùng với chúng ta
  ▶ [01:57:47] thôi, còn tất cả những người khác đều
  ▶ [01:57:48] ngược lại chiều của chúng ta thì con
  ▶ [01:57:50] đường đó là con đường sai, con đường
  ▶ [01:57:52] thất bại, con đường không đúng. Tiếp nữa
    [01:57:54] là nếu trên cái con đường đó mà chúng ta
    [01:57:58] đang đi mà có những các cái viên gạch,
    [01:58:01] viên đá mà cản lại chúng ta làm cho
    [01:58:03] chúng ta không tài nào vượt qua được thì
    [01:58:05] cái con đường đó không tạo nên sức mạnh,
  ```

### o28 [M] Resistance limits how far he guides supplementation

**Decisions:** D3  
**Watch:** [▶ 01:58:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7096s)

- **Timestamp range:** [01:58:21]-[01:59:04]
- **Anchor** [01:58:25]: "thế này. Nếu như có điều kiện thuận lợi thì tôi sẽ giúp đỡ được nhiều bệnh nhân hơn nữa. Tôi sẽ hướng dẫn được mọi người bổ sung vi chất các thứ ở mức cao hơn. Nhưng vì rằng là có những các cái sức cản nhất định cho nên là đôi khi chúng ta phải giảm bớt các cái nhịp đi và phải"
- **Why it matters:** He says he would guide higher levels under better conditions, a real limit on what he teaches.
- **Source:** batch 10#4
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 01:58:10–01:58:50 · [▶ watch from 01:58:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7090s)

  ```text
    [01:58:11] đường không đạt được những cái yêu cầu.
    [01:58:13] Thế thì ở đây tôi thấy rằng là đến cái
    [01:58:15] giờ phút ngày hôm nay thì đã có rất
    [01:58:17] nhiều những các cái người đi theo và còn
    [01:58:19] lại cái phần cản lại không phải là cái
    [01:58:21] phần mà quá lớn quá quan trọng. Tuy
    [01:58:23] nhiên nó cũng ảnh hưởng rất nhiều ở chỗ
  ▶ [01:58:25] thế này. Nếu như có điều kiện thuận lợi
  ▶ [01:58:28] thì tôi sẽ giúp đỡ được nhiều bệnh nhân
  ▶ [01:58:29] hơn nữa. Tôi sẽ hướng dẫn được mọi người
  ▶ [01:58:31] bổ sung vi chất các thứ ở mức cao hơn.
  ▶ [01:58:34] Nhưng vì rằng là có những các cái sức
  ▶ [01:58:36] cản nhất định cho nên là đôi khi chúng
  ▶ [01:58:38] ta phải giảm bớt các cái nhịp đi và phải
    [01:58:41] thay đổi những cái cách thức đi thì từ
    [01:58:43] đó chúng ta sẽ phải đi chậm hơn một chút
    [01:58:45] chứ chúng ta không thể đi nhanh hơn và
    [01:58:47] sẽ có những cái người mà không được
    [01:58:48] hưởng những các cái điều mà chúng tôi
  ```

### o29 [M] Bilirubin not raised despite jaundice

**Decisions:** D3  
**Watch:** [▶ 02:09:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7752s)

- **Timestamp range:** [02:09:17]-[02:09:26]
- **Anchor** [02:09:17]: "Nhưng bilirobin không tăng, các thứ không tăng nhưng đây là thiếu máu vi thể nó ở dưới da thôi. Tại sao nó"
- **Why it matters:** Separates the test result from the mechanism he proposes.
- **Partial coverage only:** c258 gives the 'thiếu máu vi thể' conclusion without the bilirubin finding.
- **Source:** batch 11#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 02:09:02–02:09:42 · [▶ watch from 02:09:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7742s)

  ```text
    [02:09:02] nó rơi vào suy sụp, nó rơi vào cái tình
    [02:09:05] trạng sụp đổ.
    [02:09:05] >> Vâng.
    [02:09:06] >> Nó rơi vào tình trạng sụp đổ. Chị nói
    [02:09:08] rất đúng rồi. Chị nói đúng rằng thứ nhất
    [02:09:10] là chị đang thiếu máu, thiếu sắt, thiếu
    [02:09:12] máu hồng cầu nhược sắc thì dẫn tới là tế
    [02:09:14] bào cầu nó mỏng manh, nó dễ vỡ và gây ra
  ▶ [02:09:17] cái vàng da. Nhưng bilirobin không tăng,
  ▶ [02:09:19] các thứ không tăng nhưng đây là thiếu
  ▶ [02:09:21] máu vi thể nó ở dưới da thôi. Tại sao nó
    [02:09:24] lại vàng da? Là bởi vì da và mắt của chị
    [02:09:26] tiếp xúc với lại ánh sáng. Tiếp xúc với
    [02:09:28] không khí. Ánh sáng có tia gì ạ? Có tia
    [02:09:31] UV đúng không ạ?
    [02:09:33] >> Thế rồi không khí có ô nhiễm, có các cái
    [02:09:35] hạt bụi mịn, hạt bụi PAM 2.5 đúng không
    [02:09:38] ạ? 2.5. Thế rồi lên tới 10 đấy.
    [02:09:41] >> Vân vân. tất cả rồi những các cái hóa
    [02:09:42] chất trị tiếp xúc cái này ra là một cái
  ```

### o30 [L] Lifestyle advice for chị Ngọc Thơ

**Decisions:** D3  
**Watch:** [▶ 02:16:04](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8159s)

- **Timestamp range:** [02:16:04]-[02:16:18]
- **Anchor** [02:16:08]: "đẩy cao được, giảm bớt tất cả các gốc tự do đi bằng cách thực hành những cái lối sống để hạn chế gốc tự do nó xuất hiện trong cơ thể mình."
- **Why it matters:** He advises lifestyle change for her, not only supplements.
- **Partial coverage only:** c543-c546 give the general advice, not this case.
- **Source:** batch 12#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 02:15:53–02:16:33 · [▶ watch from 02:15:53](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8153s)

  ```text
    [02:15:53] nó là cả một cái vòng xoắn cả một cái
    [02:15:55] chuỗi
    [02:15:56] >> và chúng ta cần phải hiểu cái bản chất
    [02:15:59] đi vào sâu vào bản chất ở mức độ tế bào
    [02:16:02] sau cái số phát sóng ngày hôm nay chị
    [02:16:04] Ngọc Thơ tiếp tục là gì? Chị làm thế nào
  ▶ [02:16:08] đẩy cao được, giảm bớt tất cả các gốc tự
  ▶ [02:16:10] do đi bằng cách thực hành những cái lối
  ▶ [02:16:12] sống để hạn chế gốc tự do nó xuất hiện
  ▶ [02:16:15] trong cơ thể mình.
    [02:16:16] >> Vâng.
    [02:16:16] >> Thì muốn như thế thì lại phải hiểu cái
    [02:16:18] phần gốc tự do nó sinh ra như thế nào.
    [02:16:20] Nó sinh ra từ nội sinh trong cơ thể
    [02:16:22] chúng ta. Nó sinh ra từ những các cái
    [02:16:25] vấn đề đấy là gì ạ? Chế độ ăn uống, chế
    [02:16:27] độ sinh hoạt, chế độ làm việc. Bây giờ
    [02:16:30] chị chỉ cần căng thẳng suy nghĩ các thứ
    [02:16:33] nó quá nhiều thôi thì cuối cùng cũng sẽ
  ```

### o31 [M] Triggers and burden of trigeminal pain

**Decisions:** D3  
**Watch:** [▶ 02:19:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8387s)

- **Timestamp range:** [02:19:52]-[02:20:10]
- **Anchor** [02:19:54]: "cần một cơn gió thổi nho nhẹ qua cái thôi là cái cơn giật mặt nó [tiếng cười] khủng khiếp. Đánh răng cái thôi là bắt đầu giật mạch khủng khiếp. Thế rồi có"
- **Why it matters:** Wind, brushing teeth or a smile can set off the pain, so people avoid contact.
- **Partial coverage only:** c286 gives the despair, not the triggers.
- **Source:** batch 12#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 02:19:39–02:20:19 · [▶ watch from 02:19:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=8379s)

  ```text
    [02:19:39] bắt đầu nó rơi vãi. Nhưng nó cũng chẳng
    [02:19:41] khỏi được. Tôi đọc các tài liệu trên thế
    [02:19:43] giới là diệt xong chỉ hai năm sau nó lại
    [02:19:45] tái phát lại và tái phát lại nó còn đau
    [02:19:47] hơn. đau hơn đến nỗi mà chẳng còn cái
    [02:19:50] giải pháp nào nữa. Và người ta chỉ nghĩ
    [02:19:52] đến cái bước đường cuối cùng. Vì sao chỉ
  ▶ [02:19:54] cần một cơn gió thổi nho nhẹ qua cái
  ▶ [02:19:57] thôi là cái cơn giật mặt nó [tiếng cười]
  ▶ [02:19:59] khủng khiếp. Đánh răng cái thôi là bắt
  ▶ [02:20:01] đầu giật mạch khủng khiếp. Thế rồi có
    [02:20:03] khi một nụ cười cái thôi là đã bắt đầu
    [02:20:05] phải trả bằng một cái giá cơn đau. Đau
    [02:20:07] nó gọi là đau như điện giật và đau khủng
    [02:20:10] khiếp người ta không chịu được. dẫn tới
    [02:20:12] là những người đau dây thần kinh số năm
    [02:20:14] luôn luôn có một khuôn mặt buồn giầu
    [02:20:17] không muốn tiếp xúc ai cả, tránh tất cả
    [02:20:19] mọi thứ và luôn đeo khẩu trang thật kỹ,
  ```

### o32 [M] Dizziness on standing, cold limbs, pale dry skin

**Decisions:** D3  
**Watch:** [▶ 03:15:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11750s)

- **Timestamp range:** [03:15:55]-[03:16:30]
- **Anchor** [03:15:59]: "cơn hoa mắt chóng mặt trao đảo mỗi khi đứng dậy. Đôi bàn tay bàn chân lúc nào cũng lạnh ngắt như ngâm trong nước đá."
- **Why it matters:** A concrete symptom cluster in the blood-disorder review.
- **Partial coverage only:** c353 lists other symptoms.
- **Source:** batch 15#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 03:15:44–03:16:24 · [▶ watch from 03:15:44](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=11744s)

  ```text
    [03:15:44] kham khổ, thiếu đạm, thiếu vi chất của
    [03:15:47] thời kỳ bao cấp.
    [03:15:49] Hậu quả trực tiếp biểu hiện ra ngoài
    [03:15:50] bằng những triệu chứng cay đắng mà bác
    [03:15:52] đang phải gánh chịu hàng ngày. Nỗi mệt
    [03:15:55] mỏi dượu dã bỏ dọc từng đốt sống. Những
  ▶ [03:15:59] cơn hoa mắt chóng mặt trao đảo mỗi khi
  ▶ [03:16:01] đứng dậy. Đôi bàn tay bàn chân lúc nào
  ▶ [03:16:04] cũng lạnh ngắt như ngâm trong nước đá.
    [03:16:07] Làn da khô nhợt nhạt, thiếu vắng hồng
    [03:16:09] cầu khỏe mạnh và đặc biệt là những nhịp
    [03:16:12] thở hụt hơi ngắn ngắt khiến căn bệnh
    [03:16:14] phổi tắc nghẽn mãn tính lại càng có cơ
    [03:16:16] hội quật ngã lồng ngực gầy gộc của bác.
    [03:16:20] Tế [âm nhạc] bào đói oxy, tủy xương đói
    [03:16:23] nguyên liệu khiến cả bộ máy cơ thể bác
  ```

### o33 [H] What can trigger a sudden COPD flare

**Decisions:** D3  
**Watch:** [▶ 03:31:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12662s)

- **Timestamp range:** [03:31:07]-[03:32:00]
- **Anchor** [03:31:07]: "Chỉ cần một trận gió mùa đông bắc tràn về qua khe cửa hay một chút vi khuẩn thừa cơ xâm nhập, lòng phế quản sẽ lập tức co thắt dữ dội, bịt kín [âm nhạc] nguồn sống ít ỏi còn lại, đầy bác vào những đợt cấp viêm phổi tắc nghẽn mạn tính [âm nhạc] kinh hoàng."
- **Why it matters:** Cold wind or bacteria can trigger bronchospasm and acute flares, which is practical for this patient.
- **Partial coverage only:** c403 says keep warm without giving this reason.
- **Source:** batch 16#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 03:30:52–03:31:32 · [▶ watch from 03:30:52](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=12652s)

  ```text
    [03:30:53] Hậu quả của phản ứng viêm mạn tính g
    [03:30:55] dẳng qua nhiều thập kỷ.
    [03:30:58] >> [âm nhạc]
    [03:30:59] >> Những đường dẫn khí trong lồng ngực của
    [03:31:01] bác này đã bị thu hẹp lại, sơ cứng và
    [03:31:04] đóng cặn, hệt như một ống dẫn nước bị
  ▶ [03:31:07] vôi hóa qua bao mùa lũ. Chỉ cần một trận
  ▶ [03:31:10] gió mùa đông bắc tràn về qua khe cửa hay
  ▶ [03:31:13] một chút vi khuẩn thừa cơ xâm nhập, lòng
  ▶ [03:31:15] phế quản sẽ lập tức co thắt dữ dội, bịt
  ▶ [03:31:18] kín [âm nhạc] nguồn sống ít ỏi còn lại,
  ▶ [03:31:20] đầy bác vào những đợt cấp viêm phổi tắc
  ▶ [03:31:23] nghẽn mạn tính [âm nhạc] kinh hoàng.
    [03:31:26] Đợt suy hô hấp cấp tính từng quật ngã
    [03:31:28] bác năm ngoái không khác gì là một tiếng
    [03:31:32] chuông cảnh báo lạnh ngắt từ tử thần
  ```

### o34 [L] Learning from patients and case records

**Decisions:** D3  
**Watch:** [▶ 03:46:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13594s)

- **Timestamp range:** [03:46:39]-[03:47:10]
- **Anchor** [03:46:48]: "đọc có hàng ngàn vạn cuốn sách nhưng nếu không có những ông thầy dạy về thực hành, không có những bệnh nhân để trở thành người thầy của sinh viên, không có những các cái bệnh án thì chúng tôi không bao giờ có thể thành thầy thuốc"
- **Why it matters:** Explains why the two program sections turn theory into practice.
- **Source:** batch 17#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 03:46:33–03:47:13 · [▶ watch from 03:46:33](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13593s)

  ```text
    [03:46:34] vực khác nhau. Cho nên là hai cái phần
    [03:46:37] này rất quan trọng.
    [03:46:39] Tôi lấy ví dụ này để quý vị hình dung
    [03:46:41] này là mỗi một khi mà chúng tôi học ở
    [03:46:43] trong trường đạo y khoa là sinh viên,
    [03:46:45] chúng tôi có lên giảng đường, chúng tôi
    [03:46:47] học suốt ngày trên giảng đường chúng tôi
  ▶ [03:46:48] đọc có hàng ngàn vạn cuốn sách nhưng nếu
  ▶ [03:46:51] không có những ông thầy dạy về thực
  ▶ [03:46:52] hành, không có những bệnh nhân để trở
  ▶ [03:46:55] thành người thầy của sinh viên, không có
  ▶ [03:46:57] những các cái bệnh án thì chúng tôi
  ▶ [03:46:58] không bao giờ có thể thành thầy thuốc
    [03:47:00] được. Vì như thế mà học ở trường y của
    [03:47:02] chúng tôi luôn luôn là các buổi sáng hầu
    [03:47:05] hết tất cả những cái thời gian dành cho
    [03:47:08] của buổi sáng đó là chúng tôi phải đi
    [03:47:10] bệnh viện để thực hành. Thế còn lại các
    [03:47:12] buổi chiều là chúng tôi về trường để học
  ```

### o35 [L] Why the health-education project runs ten years

**Decisions:** D3  
**Watch:** [▶ 03:51:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13885s)

- **Timestamp range:** [03:51:30]-[03:52:03]
- **Anchor** [03:51:36]: "sách vở thì 9 đến 10 năm sau lúc đó chúng tôi mới có thể đứng độc lập trên bệnh nhân. Vậy đây cũng là cái lý do mà tại sao tôi lại chọn cái thời gian, cái dự án mà tôi mới Khánh lành đi đó chính là 10 năm."
- **Why it matters:** Compares it to doctor training; the rationale for long-term learning.
- **Partial coverage only:** c228 covers repetition only.
- **Source:** batch 17#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 03:51:21–03:52:01 · [▶ watch from 03:51:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=13881s)

  ```text
    [03:51:24] tháng bây giờ và 18 tháng trước kia vẫn
    [03:51:26] chỉ là cái thời gian rất ngắn. Còn sau
    [03:51:28] đó chúng tôi phải học vô cùng nhiều, học
    [03:51:30] rất rất nhiều. Học của các thầy, học của
    [03:51:32] các anh đi trước, học của những thế hệ
    [03:51:34] đi trước, học trên bệnh nhân đối chiếu
  ▶ [03:51:36] sách vở thì 9 đến 10 năm sau lúc đó
  ▶ [03:51:39] chúng tôi mới có thể đứng độc lập trên
  ▶ [03:51:40] bệnh nhân. Vậy đây cũng là cái lý do mà
  ▶ [03:51:42] tại sao tôi lại chọn cái thời gian, cái
  ▶ [03:51:45] dự án mà tôi mới Khánh lành đi đó chính
  ▶ [03:51:47] là 10 năm.
    [03:51:49] 10 năm đó đủ với lại một cái chu trình
    [03:51:52] để tất cả mọi người sau khi nhiệt tình
    [03:51:54] tiếp thu kiến thức thì chúng ta có một
    [03:51:56] cái vốn liếng để có được cái sức khỏe
    [03:51:58] toàn diện cho chính bản thân mình. Thì
    [03:52:00] quý vị sẽ thấy rằng một tuần chúng ta
  ```

### o36 [M] A weakened body also leads to falls and accidents

**Decisions:** D3  
**Watch:** [▶ 03:54:08](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14043s)

- **Timestamp range:** [03:54:08]-[03:54:27]
- **Anchor** [03:54:10]: "cơ thể chúng ta suy yếu thì chúng ta mới không tập trung được, chúng ta đi mới hay bị vấp ngã, mới hay bị va chạm, mới hay bị tai nạn. Còn một khi chúng đã"
- **Why it matters:** A further branch of his free-radical argument, beyond infection.
- **Partial coverage only:** c413 and c414 cover infection and injury, not this link.
- **Source:** batch 17#4
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 03:53:55–03:54:35 · [▶ watch from 03:53:55](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14035s)

  ```text
    [03:53:57] cái cảm cúm lặt vặt ví dụ thế hoặc chúng
    [03:53:59] ta bị chấn thương thì không thể nào đổ
    [03:54:01] tại cái gốc tự do được. Nhưng cũng không
    [03:54:03] thể nào nói rằng đấy là không liên quan
    [03:54:05] bởi vì chỉ khi cơ thể chúng ta suy yếu
    [03:54:07] cái hệ miễn dịch thì chúng ta mới dễ
    [03:54:08] nhiễm virus vi khuẩn đúng không ạ. Khi
  ▶ [03:54:10] cơ thể chúng ta suy yếu thì chúng ta mới
  ▶ [03:54:12] không tập trung được, chúng ta đi mới
  ▶ [03:54:14] hay bị vấp ngã, mới hay bị va chạm, mới
  ▶ [03:54:16] hay bị tai nạn. Còn một khi chúng đã
    [03:54:19] thân khỏe, tâm an, chí sáng thì rất khó
    [03:54:21] để mà chúng ta bị như thế. Vậy thì cái
    [03:54:24] con đường, mọi cái con đường đi thì nó
    [03:54:26] đều có một cái bước trung gian trung
    [03:54:27] chuyển, đó chính là gốc tự do. Và chúng
    [03:54:30] ta thấy rằng như trường hợp của bác
    [03:54:32] Lương Trắc Nghiên thì tất cả mọi con
    [03:54:35] đường cũng lại đều hướng tới gốc tự do.
  ```

### o37 [M] Plan to raise the list to 45, then 60 micronutrients

**Decisions:** D3  
**Watch:** [▶ 04:13:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15192s)

- **Timestamp range:** [04:13:17]-[04:13:40]
- **Anchor** [04:13:17]: "Đến cái bước tiếp theo là 45 xong đến gì ạ? 60 vi chất."
- **Why it matters:** Shows a much wider intended supplement scope than the 7 groups and 18 products.
- **Partial coverage only:** c447 stops at the current list.
- **Source:** batch 18#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 04:13:02–04:13:42 · [▶ watch from 04:13:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15182s)

  ```text
    [04:13:05] đúng không ạ? Nào là bo, nào là silic.
    [04:13:09] Hôm nay chúng ta lại đến Glutathion đúng
    [04:13:11] không ạ? Tới này chúng ta lại làm một
    [04:13:13] loạt các cái thành phần khác nữa. Còn vô
    [04:13:15] cùng nhiều cái khác nữa cơ mà. Tôi đang
  ▶ [04:13:17] hướng tới là gì? Đến cái bước tiếp theo
  ▶ [04:13:19] là 45 xong đến gì ạ? 60 vi chất. Tôi cứ
    [04:13:23] nâng nâng dần lên các cái thành phần như
    [04:13:25] thế này để chúng ta bổ sung càng ngày nó
    [04:13:26] càng đi sâu hơn. Vậy ngày hôm nay một
    [04:13:29] cái rất quan trọng với bác Nghiên nữa đó
    [04:13:31] chính là bác hãy hiểu thật sâu gốc tự do
    [04:13:34] đó là cái gì và khắc phục gốc tự do đó
    [04:13:37] bằng glutathion là cái chủ đề chính của
    [04:13:40] ngày hôm nay. Đây là một bước rất quan
    [04:13:41] trọng và đã cùng với gia đình cũng như
  ```

### o38 [L] Why the gamma carbon is chosen

**Decisions:** D3  
**Watch:** [▶ 04:26:29](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15984s)

- **Timestamp range:** [04:26:29]-[04:26:46]
- **Anchor** [04:26:32]: "trong axit amin nếu chọn cái chỗ kết nối bền vững nhất, tốt nhất để không bị phá hủy, tránh những enzyme bị phá hủy thì nó phải chọn cacbon gì? Cacbon gamma là cái chỗ cuối cùng."
- **Why it matters:** The structural reason for the bond, which resists enzyme breakdown.
- **Partial coverage only:** c462 and c534 name the gamma bond only.
- **Source:** batch 19#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 04:26:17–04:26:57 · [▶ watch from 04:26:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15977s)

  ```text
    [04:26:18] đuôi của cái kìm cái quai kìm này.
    [04:26:20] >> Vâng.
    [04:26:21] >> Vậy thì khi n thực hiện kết nối phải
    [04:26:23] chọn cái chỗ chắc để kết nối chứ còn nếu
    [04:26:25] chọn cái chỗ mà nó yếu thế này để kết
    [04:26:27] nối thì sẽ không tạo thành sức mạnh
    [04:26:29] được. Cho nên chúng ta sẽ thấy rằng
  ▶ [04:26:32] trong axit amin nếu chọn cái chỗ kết nối
  ▶ [04:26:35] bền vững nhất, tốt nhất để không bị phá
  ▶ [04:26:38] hủy, tránh những enzyme bị phá hủy thì
  ▶ [04:26:40] nó phải chọn cacbon gì? Cacbon gamma là
  ▶ [04:26:43] cái chỗ cuối cùng.
    [04:26:44] >> Vâng. còn không dại gì đi chọn cacbon
    [04:26:46] alpha. Các phản ứng khoa học một là nó
    [04:26:49] chọn alpha, hai chọn beta, ba là chọn
    [04:26:51] cacbon gamma thì nó sẽ ưu tiên chọn
    [04:26:53] cacbon gamma để làm các cầu đối nếu như
    [04:26:56] cần thiết sự vững chắc.
  ```

### o39 [H] Children labeled with ADHD or autism improving on micronutrients

**Decisions:** D3  
**Watch:** [▶ 04:45:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17118s)

- **Timestamp range:** [04:45:23]-[04:45:49]
- **Anchor** [04:45:33]: "được dán nhãn là trầm cảm, được dán nhãn tăng động giảm chú ý, được gián nhãn tự kỷ. Nhưng sau khi bổ sung vi chất, tất cả mọi cái nó tốt lên, được dán nhãn học dốt tự dưng nó tốt lên."
- **Why it matters:** A strong outcome claim about developmental labels, beyond the depression case.
- **Partial coverage only:** c460 covers one depression case.
- **Source:** batch 20#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 04:45:18–04:45:58 · [▶ watch from 04:45:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17118s)

  ```text
    [04:45:18] lập tức chị thoát ra khỏi cái tình trạng
    [04:45:20] gì ạ? Trầm cảm.
    [04:45:21] >> Vâng.
    [04:45:21] >> Một cách rất ngoạn mục.
    [04:45:23] >> Chứ còn trầm cảm chúng ta sẽ bó tay. Ở
    [04:45:25] đây tôi thấy rằng vô cùng nhiều những
    [04:45:28] các cái bạn nhất là các bạn trẻ mà tôi
    [04:45:31] vẫn nói trong các số phát sóng trước
  ▶ [04:45:33] được dán nhãn là trầm cảm, được dán nhãn
  ▶ [04:45:35] tăng động giảm chú ý, được gián nhãn tự
  ▶ [04:45:37] kỷ. Nhưng sau khi bổ sung vi chất, tất
  ▶ [04:45:40] cả mọi cái nó tốt lên, được dán nhãn học
  ▶ [04:45:42] dốt tự dưng nó tốt lên. Và vô cùng nhiều
    [04:45:45] những người trầm cảm khi mà thấy cuộc
    [04:45:47] sống nó bế tắc quá rồi. Tôi không thể
    [04:45:49] tưởng tượng được. Có những người là viết
    [04:45:52] cả trên bình luận đấy. Có người đến viết
    [04:45:54] cả tôi những lá thư dài là đứng trên mấy
    [04:45:57] cây cầu lớn của Hà Nội định nhảy xuống
  ```

### o40 [L] Glutathione also on the outside of the mitochondrial membrane

**Decisions:** D3  
**Watch:** [▶ 04:52:51](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17566s)

- **Timestamp range:** [04:52:51]-[04:53:03]
- **Anchor** [04:52:51]: "Tất cả phía bên ngoài này nó lại còn tập trung glutathi nữa để phòng khi có lọt ra một chỗ tí nào nó cũng trung hòa nốt."
- **Why it matters:** A second line of defense for radicals that escape.
- **Partial coverage only:** c501 covers the inside only.
- **Source:** batch 21#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 04:52:36–04:53:16 · [▶ watch from 04:52:36](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17556s)

  ```text
    [04:52:37] ở trong cái màng này dày đặc ở bên trong
    [04:52:38] này.
    [04:52:39] >> Tất cả [tiếng cười] cái mặt trong của
    [04:52:40] màng ti thể nó dày đặc. Glutaton dày đặc
    [04:52:43] như thế để làm gì? để có bao nhiêu gốc
    [04:52:45] tự do đẩy ra sát màng tinh thể lập tức
    [04:52:47] bị gắp hết.
    [04:52:48] >> Vâng.
    [04:52:49] >> Bị trung hòa hết. Bị gắp hết để nó không
  ▶ [04:52:51] trào ra nữa. Chưa dừng lại ở đấy. Tất cả
  ▶ [04:52:54] phía bên ngoài này nó lại còn tập trung
  ▶ [04:52:56] glutathi nữa để phòng khi có lọt ra một
  ▶ [04:52:58] chỗ tí nào nó cũng trung hòa nốt.
    [04:53:00] >> Vâng.
    [04:53:01] >> Thế nếu như chúng ta thiếu glutathion
    [04:53:03] thì nguy hiểm chưa ạ?
    [04:53:04] >> Vâng. Chúng ta thiếu glutathion hoặc
    [04:53:06] thiếu những yếu tố hiệp đồng thì dù sẽ
    [04:53:09] có đủ hay thừa glutathion cũng lại vô
    [04:53:11] nghĩa thì lúc đó chúng ta sẽ sinh ra một
    [04:53:13] loạt bệnh thôi.
    [04:53:15] >> Vâng.
    [04:53:15] >> Vậy thì ở đây nó có nhiệm vụ là bảo vệ
  ```

### o41 [L] Pigment and tool names in the whitening mechanism

**Decisions:** D3  
**Watch:** [▶ 04:57:03](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17818s)

- **Timestamp range:** [04:57:03]-[04:57:44]
- **Anchor** [04:57:03]: "Sơn đen có tên là EU melanin."
- **Why it matters:** The captions give 'EU melanin', 'pho melanin' and 'Dobacakinol'; the summary says only black and white melanin.
- **Partial coverage only:** c504 and c505 describe the colors only.
- **Source:** batch 21#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 04:56:48–04:57:28 · [▶ watch from 04:56:48](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=17808s)

  ```text
    [04:56:49] này mới thấy rằng tia UV nó quá nguy
    [04:56:51] hiểm. Anh ấy sẽ đi trộn sơn màu đen. Anh
    [04:56:55] ấy trộn sơn màu đen nếu tia UV mà nhiều,
    [04:56:58] UV mà tăng nhá thì tăng lên thì sẽ để
    [04:57:01] bảo vệ ra thì bắt đầu anh ấy trộn sơn
  ▶ [04:57:03] đen. Sơn đen có tên là EU melanin.
    [04:57:07] Melanin đây là sơn đen. Vậy chúng ta đã
    [04:57:10] nhớ rằng nếu cứ có tia mà chiếu vào thì
    [04:57:14] anh thợ trộn màu tyrosin ở trong cái nhà
    [04:57:17] máy melanoxit này anh ấy sẽ lập tức là
    [04:57:20] lấy sơn đen ra. Anh ấy pha.
    [04:57:22] >> Vâng.
    [04:57:23] >> Anh ấy pha và tự dưng ra chúng ta có màu
    [04:57:25] đen.
    [04:57:26] >> Vâng.
    [04:57:26] >> Được chưa ạ? Nếu như tia UV mà ít đi
  ```

### o42 [L] Glutathione as a substance that 'eats itself' to give

**Decisions:** D3  
**Watch:** [▶ 05:01:51](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18106s)

- **Timestamp range:** [05:01:51]-[05:02:08]
- **Anchor** [05:01:54]: "glutathon được ví như là một cái chất mà tự ăn thịt mình tức là tự dứt ra những H+ và electron để luôn luôn đem cho đi"
- **Why it matters:** The doctor's closing image for how it works.
- **Partial coverage only:** c467 gives the donation only.
- **Source:** batch 21#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 05:01:39–05:02:19 · [▶ watch from 05:01:39](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18099s)

  ```text
    [05:01:41] >> Đó chính là gấp độc chất.
    [05:01:44] >> Mũi kìm thiông này gấp độc chất thông
    [05:01:46] qua cái là nó luôn luôn cái đây là sẵn
    [05:01:49] một cái bao luôn luôn chứa electron và
    [05:01:51] hyro. luôn luôn sẵn sàng cho đi thì
  ▶ [05:01:54] glutathon được ví như là một cái chất mà
  ▶ [05:01:57] tự ăn thịt mình tức là tự dứt ra những
  ▶ [05:02:00] H+ và
  ▶ [05:02:02] >> electron để luôn luôn đem cho đi đây là
    [05:02:04] cái cuộc cho hiến tự nguyện mà nó không
    [05:02:07] đòi hỏi gì.
    [05:02:08] >> Vâng.
    [05:02:09] >> Đấy thì cái vai trò của Gluta là như
    [05:02:11] vậy. Và cái cơ chế chúng ta đã hiểu rồi
    [05:02:14] thì chúng ta sẽ thấy rằng nó rất quan
    [05:02:16] trọng nếu như cái chất này có thể nói
    [05:02:18] rằng là vua của chống độc đúng không ạ?
  ```

### o43 [H] All three routes: effect is not as high as people expect

**Decisions:** D3  
**Watch:** [▶ 05:12:23](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18738s)

- **Timestamp range:** [05:12:23]-[05:12:33]
- **Anchor** [05:12:26]: "bịt mù hiệu quả nó không phải là quá cao như quý vị đang thần tượng và đang kỳ vọng vào glutathion"
- **Why it matters:** The key conclusion before moving to injection and self-synthesis.
- **Partial coverage only:** c519, c524 and c528 give each route separately.
- **Source:** batch 22#1
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 05:12:11–05:12:51 · [▶ watch from 05:12:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18731s)

  ```text
    [05:12:13] giấy lưỡi nhưng sự thực là ngấm nó cũng
    [05:12:15] không phải là được nhiều.
    [05:12:16] >> Vâng.
    [05:12:17] >> Đó cũng lại không được nhiều lắm. Tất
    [05:12:18] nhiên là ngậm dưới lưỡi cũng là một giải
    [05:12:20] pháp nhưng cũng không nhiều.
    [05:12:23] Thế thì đây là ba con đường chính nhưng
  ▶ [05:12:26] mà chúng ta thấy rằng bịt mù hiệu quả nó
  ▶ [05:12:28] không phải là quá cao như quý vị đang
  ▶ [05:12:31] thần tượng và đang kỳ vọng vào
  ▶ [05:12:32] glutathion.
    [05:12:33] >> Vâng.
    [05:12:34] >> Còn một cái con đường cuối cùng đó là
    [05:12:35] con đường tiêm. Thì con đường này quá
    [05:12:38] nguy hiểm.
    [05:12:39] Con đường tiêm này thì sẽ một là sốc và
    [05:12:42] hai là ngộ độc. Vậy thì con đường này ví
    [05:12:46] dụ như là
    [05:12:48] FDA của Mỹ là không đồng ý với con đường
  ```

### o44 [M] Vitamins and magnesium also needed by the two enzymes

**Decisions:** D3  
**Watch:** [▶ 05:15:25](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18920s)

- **Timestamp range:** [05:15:25]-[05:15:35]
- **Anchor** [05:15:25]: "Không có vitamin, không có gì ạ? Kẽm, không có ma, không có celen, không có các thứ thì hai anh này chẳng hoạt động được."
- **Why it matters:** The summary's list leaves out vitamins in general and 'ma'.
- **Partial coverage only:** c537 lists selenium, zinc, C and E only.
- **Source:** batch 22#2
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 05:15:10–05:15:50 · [▶ watch from 05:15:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=18910s)

  ```text
    [05:15:10] là anh gì ạ? Anh JS tức là anh Enzyme JS
    [05:15:15] phụ trách về cái công đoạn này. Công
    [05:15:16] đoạn này thì nó dễ dàng hơn một chút.
    [05:15:19] Thế thì enzyme để nó hoạt động tốt thì
    [05:15:22] bắt buộc chúng ta phải có gì ạ? Có đủ vi
    [05:15:24] chất.
    [05:15:25] >> Vâng.
  ▶ [05:15:25] >> Có đúng không ạ? Không có vitamin, không
  ▶ [05:15:27] có gì ạ? Kẽm, không có ma, không có
  ▶ [05:15:30] celen, không có các thứ thì hai anh này
  ▶ [05:15:32] chẳng hoạt động được. Nhất là hai anh
    [05:15:34] này rất cần celen.
    [05:15:35] >> Vâng.
    [05:15:35] >> Hai anh này rất cần kẽm. Hai anh này rất
    [05:15:38] cần vitamin C, vitamin E. không có những
    [05:15:40] cái này các anh ấy chẳng làm việc được.
    [05:15:43] Đồng ý không ạ?
    [05:15:44] >> Vâng.
    [05:15:44] >> Cho nên là chúng ta phải bổ sung vi
    [05:15:46] chất. Việc thứ hai đó chính là chế độ ăn
    [05:15:49] uống của chúng ta phải đa dạng cân bằng.
  ```

### o45 [M] Skin whitens by itself and oxidants fall

**Decisions:** D3  
**Watch:** [▶ 05:17:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19030s)

- **Timestamp range:** [05:17:15]-[05:17:33]
- **Anchor** [05:17:15]: "Thì tự da chúng ta sẽ trắng lên thôi và các chất oxy hóa sẽ giảm xuống."
- **Why it matters:** A specific effect claim for self-synthesis. The fall in oxidants is not stated anywhere.
- **Partial coverage only:** c552 covers the skin part only.
- **Source:** batch 22#3
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 05:17:00–05:17:40 · [▶ watch from 05:17:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19020s)

  ```text
    [05:17:01] enzyme này có tác dụng điều hòa để giảm
    [05:17:03] sản xuất thừa.
    [05:17:05] >> Nó không cho sản xuất thừa cho nên chúng
    [05:17:07] ta không sợ thiếu glutathion khi nào?
    [05:17:10] Khi chúng ta ăn uống cân bằng.
    [05:17:12] >> Vâng.
    [05:17:13] >> Và chúng ta bổ sung đủ vi chất.
    [05:17:14] >> Vâng.
  ▶ [05:17:15] >> Thì tự da chúng ta sẽ trắng lên thôi và
  ▶ [05:17:17] các chất oxy hóa sẽ giảm xuống. Ừ. Điều
    [05:17:20] thứ ba một là cơ thể tự đầu tiên chúng
    [05:17:24] ta bổ sung là bế tắc rồi thì cơ thể tự
    [05:17:26] tổng hợp là cái thứ hai rất quan trọng
    [05:17:28] và điều thứ ba cực kỳ quan trọng là
    [05:17:30] chúng ta phải xảm gốc tự do xuống
    [05:17:32] >> vâng
    [05:17:33] >> để không cạn kiệt glutathion.
    [05:17:35] >> Vâng
    [05:17:35] >> có đúng không ạ? Muốn giảm gốc tự do
    [05:17:37] xuống thì chúng ta giảm uống thuốc đi.
    [05:17:40] Khi nào thật sự cần uống thuốc mới uống
  ```

### o46 [H] Do not avoid beta-carotene

**Decisions:** D3  
**Watch:** [▶ 05:18:17](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19092s)

- **Timestamp range:** [05:18:17]-[05:18:27]
- **Anchor** [05:18:17]: "Đừng có tránh betacaroten như là các chị đang bình luận"
- **Why it matters:** Direct diet advice, and it reads differently from c272 on carotene causing jaundice.
- **Partial coverage only:** c272 gives the mechanism, not this advice.
- **Source:** batch 22#4
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 05:18:02–05:18:42 · [▶ watch from 05:18:02](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19082s)

  ```text
    [05:18:03] nữa. Giữ gìn đừng để chúng ta nhiễm vi
    [05:18:06] khuẩn, virus để dẫn tới là chúng ta tiêu
    [05:18:08] tốn gì ạ? Glutaton.
    [05:18:10] >> Vâng.
    [05:18:11] >> Có đúng không ạ? Tất cả những cái việc
    [05:18:13] đó chúng ta làm đừng có mất cân bằng,
    [05:18:15] đừng có ăn đường nhiều quá giống chị
    [05:18:16] Hằng.
  ▶ [05:18:17] Đừng có tránh betacaroten như là các chị
  ▶ [05:18:20] đang bình luận vân vân rất rất nhiều
    [05:18:22] những cái đó chúng ta thay đổi nó đi.
    [05:18:25] Vậy một là chúng ta phải giảm các cái
    [05:18:27] nguồn để tạo gốc tự do. Hai là chế độ ăn
    [05:18:30] uống cân bằng và bổ sung vi chất.
    [05:18:32] >> Đấy là cách tốt nhất. Còn tất nhiên quý
    [05:18:35] vị có thể bổ sung theo đường uống thì nó
    [05:18:37] không ngấm được nhiều cũng ngấm được ít.
    [05:18:39] Bởi vì rằng là nó sẽ cắt nhỏ ra những
    [05:18:41] cái này nó nó không ngấm được hết. Nhưng
    [05:18:42] mà ít nhất nó cắt ra thành những các cái
  ```

### o47 [M] Stated benefits of the endogenous route

**Decisions:** D3  
**Watch:** [▶ 05:19:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19150s)

- **Timestamp range:** [05:19:15]-[05:19:55]
- **Anchor** [05:19:15]: "chúng ta sẽ trẻ ra, chúng ta sẽ phòng tránh được bệnh tật bằng chính con đường nội sinh của chúng ta rất rẻ mà không tốn kém tiền bạc gì."
- **Why it matters:** Getting younger, preventing disease, and very cheap.
- **Partial coverage only:** c548 and c550 cover cost and sufficiency, not the first two.
- **Source:** batch 22#5
- **BEFORE:** the summary does not state this (see coverage note above, if any).
- **AFTER (if you accept it as an omission):** a summary regeneration or edit would need to add it; the audit proposes no wording.

  Transcript 05:19:00–05:19:40 · [▶ watch from 05:19:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=19140s)

  ```text
    [05:19:01] chúng ta làm cho cơ thể tăng tổng hợp
    [05:19:04] lên, bổ sung vi chất đầy đủ để nó hiệp
    [05:19:06] đồng với nhau tốt.
    [05:19:07] >> Vâng. Và chúng ta hiểu được cái này,
    [05:19:09] chúng ta ngăn chặn gốc tự do nữa đi thì
    [05:19:11] lúc đấy glutathum trong cơ thể của chúng
    [05:19:13] ta nó sẽ hoạt động một cách hiệu quả
  ▶ [05:19:15] nhất. Nó sản xuất đầy đủ nhất và chúng
  ▶ [05:19:17] ta sẽ trẻ ra, chúng ta sẽ phòng tránh
  ▶ [05:19:19] được bệnh tật bằng chính con đường nội
  ▶ [05:19:21] sinh của chúng ta rất rẻ mà không tốn
  ▶ [05:19:23] kém tiền bạc gì. Còn đến giờ phút này có
    [05:19:25] thể nói rằng sản phẩm Glutathion trên
    [05:19:28] thế giới có những sản phẩm bán rất đắt
    [05:19:30] và nó đã trở thành một cái sản phẩm khá
    [05:19:32] hot trên thị trường để mọi người lão vào
    [05:19:35] bổ sung. Tuy nhiên theo quan điểm của cá
    [05:19:37] nhân tôi thì chúng ta hoàn toàn có thể
    [05:19:40] hiểu cái cơ chế như thế này và chúng ta
  ```

## Part 4. Excluded viewer-comment candidates (batch 06)

These were excluded under the viewer-comment rule. Only 06#8 is flagged by the audit as a judgment call. The others are listed so you can confirm the exclusions.

### 06#1

**Watch:** [▶ 01:22:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4930s)

- **Pass-1 description:** Viewer (Ngọc Thơ) reports jaw muscles stiff/hard to control since 2012, slurred speech, saying B when thinking A, poor focus and forgetfulness (part of symptom picture the doctor later calls "não sương mù").
- **Anchor (pass-1 fragment):** "khu vực cơ hàm của em luôn bị khó"

  Transcript 01:22:00–01:22:40 · [▶ watch from 01:22:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4920s)

  ```text
    [01:22:00] hồng. Khi nói chuyện hay đi cầu thang,
    [01:22:03] em luôn bị hụt hơi. Người lúc nào cũng
    [01:22:06] thiếu lượng, mất tập trung, hay quên và
    [01:22:08] bị líu lưỡi. Trong đầu nghĩ a nhưng phát
    [01:22:12] ngôn lại thành b. Đặc biệt là từ năm
  ▶ [01:22:15] 2012, khu vực cơ hàm của em luôn bị khó
    [01:22:18] điều khiển hay đơ cứng khiến em nói
    [01:22:21] không tròn vành rõ chữ. có lúc mất điều
    [01:22:23] khiển phần hàm. Em trở nên mất tự tin
    [01:22:26] hoàn toàn bởi trước đây em từng là người
    [01:22:29] học giỏi, thuyết trình tốt và có ngoại
    [01:22:31] hình sáng.
    [01:22:33] Các kết quả xét nghiệm hàng năm trong
    [01:22:35] giai đoạn đó đều cho thấy các chỉ số gan
    [01:22:38] mật và bilirubin ở mức bình thường.
  ```

### 06#2

**Watch:** [▶ 01:23:24](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4999s)

- **Pass-1 description:** Viewer had read that iron-deficient red cells break down and make skin yellow, but said she did not know if this was accurate (her own hedged hypothesis, which the doctor later discusses).
- **Anchor (pass-1 fragment):** "Nhưng em không rõ độ chính xác của"

  Transcript 01:23:09–01:23:49 · [▶ watch from 01:23:09](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4989s)

  ```text
    [01:23:10] lượng để thêm dinh dưỡng thì em ăn không
    [01:23:13] nổi.
    [01:23:14] Em có xem một số tài liệu nói rằng khi
    [01:23:16] thiếu sắt hồng cầu mỏng manh dễ bị phá
    [01:23:19] hủy hàng loạt và xác hồng cầu bị phá hủy
    [01:23:21] tồn tại trên bề mặt da làm da có ánh
  ▶ [01:23:24] vàng. Nhưng em không rõ độ chính xác của
    [01:23:27] thông tin này như thế nào. Em đã đi khám
    [01:23:30] khoảng năm bệnh viện phòng khám. và bác
    [01:23:33] sĩ bệnh viện tư. Em
    [01:23:37] nhận được câu trả lời luôn là họ thừa
    [01:23:40] nhận nhìn da của em vàng thật nhưng giải
    [01:23:43] thích đó là do cơ địa, do nguồn nước. Dù
    [01:23:47] em đã chuyển chỗ ở vài lần, nguồn nước
    [01:23:49] đã thay đổi nhưng vẫn không cải thiện.
  ```

### 06#3

**Watch:** [▶ 01:23:47](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5022s)

- **Pass-1 description:** About five hospitals/clinics agreed her skin was yellow but put it down to constitution (cơ địa), water source, or beta-carotene. She moved house several times with no change (prior medical explanations rejected).
- **Anchor (pass-1 fragment):** "thích đó là do cơ địa, do nguồn nước."

  Transcript 01:23:32–01:24:12 · [▶ watch from 01:23:32](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5012s)

  ```text
    [01:23:33] sĩ bệnh viện tư. Em
    [01:23:37] nhận được câu trả lời luôn là họ thừa
    [01:23:40] nhận nhìn da của em vàng thật nhưng giải
  ▶ [01:23:43] thích đó là do cơ địa, do nguồn nước. Dù
    [01:23:47] em đã chuyển chỗ ở vài lần, nguồn nước
    [01:23:49] đã thay đổi nhưng vẫn không cải thiện.
    [01:23:52] hoặc là có thể do em ăn nhiều thực phẩm
    [01:23:55] chứa beta cararoten.
    [01:23:57] Điều này từng khiến em tự cắt bỏ gần như
    [01:24:00] 100% thực phẩm có màu vàng, màu cam và
    [01:24:02] màu đỏ. Nghĩ lại em vẫn rất tiếc cái
    [01:24:05] nguồn beta cararoten đã bỏ lỡ.
    [01:24:09] Thứ hai là quá trình điều chỉnh từ năm
    [01:24:11] 2026. Từ ngày 22 tháng 04 năm 2026, em
  ```

### 06#4

**Watch:** [▶ 01:23:57](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5032s)

- **Pass-1 description:** Because of the beta-carotene explanation she cut almost 100% of yellow/orange/red foods, which she now regrets. The doctor later ties carotene to how the liver converts it to vitamin A.
- **Anchor (pass-1 fragment):** "Điều này từng khiến em tự cắt bỏ gần như"

  Transcript 01:23:42–01:24:22 · [▶ watch from 01:23:42](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5022s)

  ```text
    [01:23:43] thích đó là do cơ địa, do nguồn nước. Dù
    [01:23:47] em đã chuyển chỗ ở vài lần, nguồn nước
    [01:23:49] đã thay đổi nhưng vẫn không cải thiện.
    [01:23:52] hoặc là có thể do em ăn nhiều thực phẩm
    [01:23:55] chứa beta cararoten.
  ▶ [01:23:57] Điều này từng khiến em tự cắt bỏ gần như
    [01:24:00] 100% thực phẩm có màu vàng, màu cam và
    [01:24:02] màu đỏ. Nghĩ lại em vẫn rất tiếc cái
    [01:24:05] nguồn beta cararoten đã bỏ lỡ.
    [01:24:09] Thứ hai là quá trình điều chỉnh từ năm
    [01:24:11] 2026. Từ ngày 22 tháng 04 năm 2026, em
    [01:24:17] đã bắt đầu dùng bộ vi chất bác sĩ phổ
    [01:24:19] biến chung kết hợp xem các số phát sóng
    [01:24:22] về sắt. Mỗi ngày em bổ sung một phiên
  ```

### 06#5

**Watch:** [▶ 01:25:45](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5140s)

- **Pass-1 description:** Viewer reports dreamless, good-quality sleep for the first time and now rarely needs a midday nap (extra self-reported outcome).
- **Anchor (pass-1 fragment):** "không cần nghỉ trưa mỗi ngày."

  Transcript 01:25:30–01:26:10 · [▶ watch from 01:25:30](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5130s)

  ```text
    [01:25:31] hôm tập thở 4 78 trước khi đi ngủ. Từ
    [01:25:35] nhỏ đến lớn, em mặc định ngủ là phải mơ,
    [01:25:38] kể cả ngủ trưa. Giờ em mới trải nghiệm
    [01:25:40] được giấc ngủ không mộng mị chất lượng
    [01:25:42] là như thế nào và hiện tại em hầu như
  ▶ [01:25:45] không cần nghỉ trưa mỗi ngày.
    [01:25:48] Tiếp theo đó là nhịn ăn gián đoạn từ
    [01:25:50] ngày 27 tháng năm 2026 đến nay giúp em
    [01:25:53] giảm 4 kg một cách khỏe mạnh, không bị
    [01:25:56] là người nhờ uống đủ bộ vì chất. Em cao
    [01:25:59] 1,6 từ khung 56 đến 57 kg, sau ăn nay
    [01:26:04] còn 52 đến 53 kg.
    [01:26:08] Em cũng cho các con ở tuổi vị thành niên
    [01:26:10] uống theo và nghiên cứu điều chỉnh theo
  ```

### 06#8  (D9 judgment call)

**Watch:** [▶ 01:28:26](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5301s)

- **Pass-1 description:** She took no supplements during pregnancy because she distrusted supplements, and she restricted her diet too much. She had too little breast milk and her migraines became more frequent (pregnancy and nutrition context).
- **Anchor (pass-1 fragment):** "Tôi bị thiếu sữa"

  Transcript 01:28:11–01:28:51 · [▶ watch from 01:28:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5291s)

  ```text
    [01:28:11] Tôi sinh ba cháu, cháu thứ ba mới gần ba
    [01:28:14] tuổi, sinh con khi tuổi đã cao, cộng với
    [01:28:17] sức khỏe vốn yếu lại không bổ sung vi
    [01:28:19] chất
    [01:28:21] bất kỳ một vi chất nào cả. Vì mất niềm
    [01:28:23] tin vào thực phẩm chức năng và ăn uống
  ▶ [01:28:26] kiêng khem quá mức. Tôi bị thiếu sữa
    [01:28:28] nuôi con. Căn bệnh đau nửa đầu xuất hiện
    [01:28:31] dày hơn khiến tôi bị căng thẳng và mệt
    [01:28:34] mỏi. Tôi tìm đến các nhóm chữa lành tự
    [01:28:37] nhiên trên mạng và tin vào những lời hù
    [01:28:40] dọa thiếu khoa học về tây y nên càng
    [01:28:43] thêm sợ hãi.
    [01:28:45] Cho đến một ngày thức dậy, toàn thân tôi
    [01:28:47] bị co cứng nhưng đầu óc tôi vẫn đủ tỉnh
    [01:28:50] táo để gọi người nhà đưa đi cấp cứu. Đến
  ```

### 06#11

**Watch:** [▶ 01:29:11](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5346s)

- **Pass-1 description:** While breastfeeding she avoided drugs, and a professor prescribed expensive brain magnetic-field therapy that did not help (treatment history).
- **Anchor (pass-1 fragment):** "chỉ định điều trị từ trường não rất tốn"

  Transcript 01:28:56–01:29:36 · [▶ watch from 01:28:56](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5336s)

  ```text
    [01:28:56] làm mắc trầm cảm sau sinh.
    [01:28:58] Chuỗi ngày sau đó, tôi mang cơ thể kiệt
    [01:29:01] quệ đi khám tất cả các bệnh viện lớn,
    [01:29:03] nhưng kết luận chung vẫn chỉ là trầm cảm
    [01:29:05] sau sinh. Vì đang cho con bú nên tôi
    [01:29:09] không dùng thuốc bệnh và được giáo sư
  ▶ [01:29:11] chỉ định điều trị từ trường não rất tốn
    [01:29:13] kém mà người vẫn mệt mỏi, không khá hơn.
    [01:29:17] Tôi rơi vào tuyệt vọng. Trong lúc mệt
    [01:29:19] mỏi, tôi ăn hoặc là uống đường mía thô
    [01:29:22] thì thấy rằng cơ thể dễ chịu hơn. Từ đó
    [01:29:26] tôi lạm dụng. Cứ mệt là tôi uống đường.
    [01:29:29] Sau 3 tháng sử dụng lượng đường quá
    [01:29:31] nhiều, cơ thể tôi gióng lên hồi chuông
    [01:29:34] thê thảm nhất. Tôi bị khó thở, nhịp tim
  ```

### 06#12

**Watch:** [▶ 01:30:22](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5417s)

- **Pass-1 description:** She quit sugar, then had acupressure and took herbal medicine, and says she recovered to about 30% before finding the channel (another intervention before supplements).
- **Anchor (pass-1 fragment):** "Sau đó, tôi bắt đầu cai đường."

  Transcript 01:30:07–01:30:47 · [▶ watch from 01:30:07](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5407s)

  ```text
    [01:30:08] vẹn, sợ buổi đêm vì mỗi lần nhắm mắt là
    [01:30:11] tim bị hẫng. Choàng tỉnh, nhịp tim đập
    [01:30:14] nhanh, bỏ nhịp, liên tục bị bóng đè và
    [01:30:18] chỉ ngủ được hai tiếng vào lúc gần sáng.
  ▶ [01:30:22] Sau đó, tôi bắt đầu cai đường. Tôi đi
    [01:30:24] bấm huyệt và uống thuốc nam thì cơ thể
    [01:30:27] đã được 30%.
    [01:30:29] May mắn nhờ duyên lành được giới thiệu
    [01:30:31] kênh bác sĩ Phúc. Tôi nghe, hiểu và mua
    [01:30:35] canxi, ma, vitamin tổng hợp, kẽm,
    [01:30:38] vitamin C về dùng. Dù thời gian đầu chưa
    [01:30:41] có kinh nghiệm chọn loại nhưng chỉ sau
    [01:30:43] một tháng sử dụng, cơ thể tôi đã hoàn
    [01:30:45] toàn khác. Tôi quay trở lại làm việc và
  ```

### 06#13

**Watch:** [▶ 01:30:35](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5430s)

- **Pass-1 description:** She bought calcium, magnesium, multivitamin, zinc and vitamin C. After one month she says she went back to work and could climb to the 4th floor (specific regimen and early outcome).
- **Anchor (pass-1 fragment):** "canxi, ma, vitamin tổng hợp, kẽm,"

  Transcript 01:30:20–01:31:00 · [▶ watch from 01:30:20](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=5420s)

  ```text
    [01:30:22] Sau đó, tôi bắt đầu cai đường. Tôi đi
    [01:30:24] bấm huyệt và uống thuốc nam thì cơ thể
    [01:30:27] đã được 30%.
    [01:30:29] May mắn nhờ duyên lành được giới thiệu
    [01:30:31] kênh bác sĩ Phúc. Tôi nghe, hiểu và mua
  ▶ [01:30:35] canxi, ma, vitamin tổng hợp, kẽm,
    [01:30:38] vitamin C về dùng. Dù thời gian đầu chưa
    [01:30:41] có kinh nghiệm chọn loại nhưng chỉ sau
    [01:30:43] một tháng sử dụng, cơ thể tôi đã hoàn
    [01:30:45] toàn khác. Tôi quay trở lại làm việc và
    [01:30:48] leo được lên tầng bốn của cơ quan. Giờ
    [01:30:51] phút đó, tôi cảm nhận mình vừa được tái
    [01:30:54] sinh từ cõi chết trở về.
    [01:30:58] Tháng năm 2026, sau 3 tháng dùng vi
  ```

