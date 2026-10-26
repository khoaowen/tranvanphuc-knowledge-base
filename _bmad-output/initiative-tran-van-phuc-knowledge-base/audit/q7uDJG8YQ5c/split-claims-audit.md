# Split-claims audit (supplementary) — q7uDJG8YQ5c

> corrections applied, uncommitted, video still blocked

Covers the 18 claims that exist because 7 audit records (c001, c019, c064, c065, c128, c135, c137) split when the approved corrections were applied. Existing audit files are not overwritten. Ids are from `fidelity.extract_claims` on the edited summary (160 claims). Machine-readable copy: `split-claims-audit.json`.

- Method: each claim read against the transcript window around the cited timestamps; speaker and hedges compared. Every quote is a verbatim substring of transcript.md (case, punctuation and caption line breaks normalised); timestamps recomputed from the transcript. 18/18 found.
- Result: supported 18, attribution_qualification 0, mismatch 0, unresolved 0.
- Scope limit: the 17 corrections that stay one sentence (c013, c015, c029, c036, c045, c063, c068, c069, c085, c087, c106, c108, c113, c119, c123, c127, c136) keep their old audit records, which describe the pre-edit text. Their new text is covered only by the supporting-quote check in apply-report.md, not by a fresh claim audit. Re-auditing them is optional and is the human's call.
- Fragment note: c067 and c134 end in `;` because the extractor splits sentences on semicolons.
- c087's fragment was fixed to be verbatim (see apply-report.md).

| new id | replaces audit id | class |
|---|---|---|
| c001 | c001 | supported |
| c002 | c001 | supported |
| c020 | c019 | supported |
| c021 | c019 | supported |
| c022 | c019 | supported |
| c067 | c064 | supported |
| c068 | c064 | supported |
| c069 | c064 | supported |
| c070 | c065 | supported |
| c071 | c065 | supported |
| c134 | c128 | supported |
| c135 | c128 | supported |
| c142 | c135 | supported |
| c143 | c135 | supported |
| c144 | c135 | supported |
| c145 | c135 | supported |
| c147 | c137 | supported |
| c148 | c137 | supported |

## c001 (from audit c001) — supported
- claim: Theo quan điểm bác sĩ Phúc (do Khánh Lành nêu), 15 giây đầu tiên hay những video ngắn chỉ đáp ứng nhu cầu giải trí đơn thuần nhằm lấp đầy những khoảng thời gian trống trải của con người.
- speaker: Host Khánh Lành relays Dr. Phúc's view; summary attributes it to Dr. Phúc via Khánh Lành
- evidence [00:01:13]: "Bác sĩ Phúc nghĩ rằng là 15 giây đầu tiên hay là những video ngắn chỉ đáp ứng nhu cầu giải trí đơn thuần nhằm lấp đầy những khoảng thời gian chống trải của con người"
- note: Attribution and scope match; 'trống trải' normalises the caption's ASR 'chống trải'.

## c002 (from audit c001) — supported
- claim: Các clip 10 đến 15 phút, nhiều lắm khoảng 20 phút là cách tư duy truyền thông ban đầu của Khánh Lành và ekip; bác sĩ Phúc cho rằng làm như thế sẽ không bao giờ cung cấp được kiến thức cho người dân.
- speaker: Dr. Phúc describing Khánh Lành and the ekip's initial thinking, then his own view
- evidence [00:13:56]: "Khánh Lành đang tư duy theo cái cách của truyền thông cùng với cả đội ngũ ekip"
- evidence [00:14:04]: "Đó là làm những các cái clip chỉ ngắn thôi trong vòng cỡ độ 10 đến 15 phút thôi. Cái nào nhiều lắm thì kéo dài khoảng độ 20 phút"
- evidence [00:14:16]: "sẽ không bao giờ cung cấp được kiến thức cho người dân"
- note: Initial ('thời điểm đầu') plan and Dr. Phúc's objection are both kept.

## c020 (from audit c019) — supported
- claim: Quan niệm xưa (trong lời nói về hàm tuổi tác): 60 năm cuộc đời, 70 'xưa nay hiếm', cha ông mơ ước 100 tuổi; bác sĩ Phúc nói biên độ tuổi 'loanh quanh' khoảng 100 tuổi.
- speaker: Dr. Phúc (host/doctor turns mixed around the 60-year line; summary attributes neutrally)
- evidence [00:35:53]: "60 năm cuộc đời hay là nhân sinh thất thật của Lai Hi tức là người thọ 70 xưa nay hiếm nhưng mà cha ông chúng ta thì vẫn mơ ước rằng 100 tuổi"
- evidence [00:36:24]: "loanh quanh nó cũng chỉ là con số quãng độ 100 tuổi"
- note: Hedges and attribution kept.

## c021 (from audit c019) — supported
- claim: Ông 'vẫn hy vọng' kéo dài tuổi thọ lên 130, 140, 150 và 175 tuổi; xu hướng khoa học, một số nhà khoa học và một số quốc gia đang tính đến chuyện vượt qua 100 tuổi, và ông 'tin rằng' trong thế kỷ 21 'hoàn toàn làm được' việc giúp con người sống đến 150 tuổi.
- speaker: Dr. Phúc, first person
- evidence [00:36:28]: "tôi vẫn hy vọng rằng chúng ta có thể kéo dài tuổi thọ lên tới 130, 140, 150 và 175 tuổi"
- evidence [00:36:50]: "một số những nhà khoa học, một số những quốc gia đang tính đến chuyện nâng cao tuổi thọ và người ta nghĩ đến chuyện là phải vượt qua con số 100 tuổi"
- evidence [00:36:58]: "Và tôi tin rằng là trong một cái tương lai của thế kỷ 21 này là chúng ta hoàn toàn làm được, sẽ giúp được cho con người sống đến 150 tuổi"
- note: Hope and belief framing preserved.

## c022 (from audit c019) — supported
- claim: Riêng mục tiêu của ông, Khánh Lành và ekip là muốn khán giả coi tuổi 70-80 mới là bước vào cuộc đời, đang là tuổi sung sức.
- speaker: Dr. Phúc, first person
- evidence [00:47:48]: "Mục tiêu tôi với Khánh Lành với toàn bộ ekip làm ở đây muốn tất cả quý vị phải coi tuổi 70 80 mới là bước vào cuộc đời thôi. Và đây đang là cái tuổi sung sức"
- note: Matches.

## c067 (from audit c064) — supported
- claim: Theo bài báo được đọc, Omega-6 có trong các loại dầu thực vật như hoa hướng dương, dầu ngô;
- speaker: Dr. Phúc reading a quoted newspaper article
- evidence [01:54:57]: "Axit béo Omega 6 được tìm thấy trong các loại dầu thực vật như hoa hướng dương, dầu ngô"
- note: Attributed to the article. Fragment ends in ';' because the extractor splits on the semicolon.

## c068 (from audit c064) — supported
- claim: Omega-3 có trong cá béo, giúp giảm viêm, điều hòa huyết áp, rất quan trọng cho não và tim, và 'gắn liền với giảm nguy cơ' nhiều bệnh gồm tiểu đường, hội chứng ruột kích thích, đột quỵ, viêm khớp, hen suyễn và một số bệnh ung thư.
- speaker: Quoted newspaper article
- evidence [01:55:10]: "Omega 3 được tìm thấy trong cá béo, giúp giảm viêm, điều hòa huyết áp và rất quan trọng cho não và tim"
- evidence [01:55:16]: "Chúng cũng gắn liền với giảm nguy cơ nhiều bệnh bao gồm bệnh tiểu đường, hộ chứng ruột kích thích, đột quỵ, viêm khớp, hen suyễn và một số bệnh ung thư"
- note: 'gắn liền với giảm nguy cơ' hedge preserved.

## c069 (from audit c064) — supported
- claim: Bài báo nói Omega-3 là chất chống viêm, còn Omega-6 'có xu hướng gây viêm'.
- speaker: Quoted newspaper article
- evidence [01:55:42]: "trong khi Omega 3 là chất chống viêm, Omega6 có xu hướng gây viêm"
- note: Matches.

## c070 (from audit c065) — supported
- claim: Theo bài báo được đọc, những năm gần đây các nhà khoa học phát hiện hầu hết mọi người đang hấp thụ lượng lớn Omega-6 so với thời trước, trong khi tiêu thụ thực phẩm động vật giàu Omega-3 ở mức thấp nhất từ trước đến nay; sự mất cân đối này liên quan đến béo phì, tiểu đường, bệnh tim, ung thư, trầm cảm, đau, bệnh viêm như hen suyễn và các bệnh tự miễn.
- speaker: Quoted newspaper article
- evidence [01:54:29]: "Những năm gần đây, các nhà khoa học phát hiện ra rằng hầu hết mọi người đều đang hấp thụ một lượng lớn các chất béo Omega6 so với thời trước"
- evidence [01:54:38]: "lượng tiêu thụ thực phẩm từ động vật giàu hàm lượng omega 3 lại đang ở thời kỳ thấp nhất từ trước đến nay"
- evidence [01:54:47]: "Sự mất cân đối trong chế độ ăn uống này liên quan đến béo phì"
- note: 'liên quan' hedge kept; list matches (béo phì, tiểu đường, bệnh tim, ung thư, trầm cảm, đau, hen suyễn, tự miễn).

## c071 (from audit c065) — supported
- claim: Bài báo dẫn nghiên cứu của tạp chí 'Hell' cho thấy người Mỹ hiện nay ăn thực phẩm chứa Omega-6 nhiều hơn Omega-3 gấp sáu lần.
- speaker: Quoted newspaper article citing a journal (caption 'Hell')
- evidence [01:55:30]: "Các nghiên cứu của tạp chí Hell cho thấy người Mỹ hiện nay ăn thực phẩm chứa Omega6 nhiều hơn Omega 3 gấp sáu lần"
- note: Journal name is the caption's, kept in quotes.

## c134 (from audit c128) — supported
- claim: Từ 0,6 trở lên, bác sĩ Phúc nói chúng ta sẽ bỏ được nhiều sản phẩm thuốc như thuốc tiểu đường, thuốc mỡ máu, thuốc tim mạch ('Tôi thấy rất nhiều người bỏ được'), thuốc huyết áp; khớp đang đau 'bắt đầu hết đau'; phản ứng viêm dị ứng 'bắt đầu là hết'; viêm xoang, viêm mũi 'hết'; trí nhớ 'bắt đầu cải thiện';
- speaker: Dr. Phúc, first person (clinical experience)
- evidence [03:02:22]: "nếu quý vị nào mà uống từ 0,6 trở lên thì chúng ta sẽ bỏ được nhiều những các cái sản phẩm thuốc"
- evidence [03:02:32]: "Tôi thấy rất nhiều người bỏ được"
- evidence [03:02:38]: "khớp đang đau bắt đầu hết đau"
- evidence [03:02:42]: "Viêm xoang, viêm mũi các thứ nọ kia hết"
- evidence [03:02:44]: "trí nhớ bắt đầu cải thiện"
- note: Anecdotal framing kept ('Tôi thấy rất nhiều người bỏ được'); no medical claim beyond what he says.

## c135 (from audit c128) — supported
- claim: Alzheimer 'cải thiện được rất nhiều' (Parkinson được nhắc trong cùng đoạn, người nói không rõ); ông nói từ 0,6 trở lên thì giá thành đắt.
- speaker: Dr. Phúc; 'Alzimer run rẩy tay chân Parkison' follows a speaker change
- evidence [03:02:51]: "Alzimer nhớ nhớ quên quên là cải thiện được rất nhiều"
- evidence [03:02:55]: "từ 0,6 trở lên nhưng mà giá thành đắt rồi"
- note: Parkinson mention kept with its uncertain speaker.

## c142 (from audit c135) — supported
- claim: Theo bác sĩ Phúc (nói 'tôi đang lấy ví dụ'), những ai đang bị gan nhiễm mỡ, mỡ máu, tiểu đường, đau khớp, tăng huyết áp, ngứa ngáy, dị ứng... thì 'chúng ta mua EPA tăng lên', đặc biệt là người bị mỡ máu và gan nhiễm mỡ thì ưu tiên 'EPA tăng hơn so với DHA' để quét mỡ máu và quét gan nhiễm mỡ đi (caption ghi 'phải mua APA cao hơn DHA').
- speaker: Dr. Phúc, with host interjections
- evidence [03:15:13]: "thì chúng ta mua EPA tăng lên"
- evidence [03:15:37]: "EPA tăng hơn so với DHA để nó quét cái mỡ máu đi"
- evidence [03:15:41]: "Và quét cái gan nhiễm mỡ đi"
- evidence [03:14:05]: "chúng ta phải mua APA cao hơn DHA"
- note: Hedged as an example; 'APA' is the caption's error for EPA and is flagged as such.

## c143 (from audit c135) — supported
- claim: Trẻ con có gan nhiễm mỡ, mỡ máu tăng 'vẫn dùng EPA tăng lên'.
- speaker: Dr. Phúc
- evidence [03:16:03]: "trẻ con nhưng vẫn dùng EPA tăng lên"
- note: Matches.

## c144 (from audit c135) — supported
- claim: Riêng với các cháu, ông nêu thừa cân béo phì, thức đêm, chơi game online, xem video ngắn nhiều là các yếu tố khiến 'rất dễ bị rối loạn nhịp tim, rất dễ bị gan nhiễm mỡ và dễ bị mỡ máu'.
- speaker: Dr. Phúc
- evidence [03:16:48]: "Béo phì là một, tăng thừa cân, béo phì là một. Thứ hai là các cháu thức đêm nhiều, các cháu chơi game online nhiều, các cháu xem phim ngắn, video ngắn nhiều"
- evidence [03:16:58]: "Chỉ cần một trong những yếu tố này thôi là các cháu rất dễ bị rối loạn nhịp tim, rất dễ bị gan nhiễm mỡ và dễ bị mỡ máu"
- note: 'Chỉ cần một trong' (any one factor) is not stated in the claim but is not contradicted.

## c145 (from audit c135) — supported
- claim: Ông dặn đừng để mất cân bằng: quá nhiều DHA mà ít EPA hoặc ngược lại quá nhiều EPA mà ít DHA thì không nên.
- speaker: Dr. Phúc (03:18:30)
- evidence [03:18:30]: "quá nhiều DHA mà lại ít EPA hoặc ngược lại quá nhiều EPA mà lại ít DHA thì chúng ta cũng không nên"
- note: Matches; placed after the children passage in the summary, said later at 03:18:30.

## c147 (from audit c137) — supported
- claim: Còn những ai khỏe mạnh, xét nghiệm tốt đẹp, cơ thể không bị bệnh gì thì bác sĩ Phúc nói 'chúng ta mua cái DHA tăng lên một chút' để ưu tiên cho não và mắt, 'sẽ rất thông minh, sẽ mắt sẽ rất tinh'; các cháu không bị gan nhiễm mỡ, không bị mỡ máu uống DHA thì 'sẽ thông minh lên, mắt sáng hơn'.
- speaker: Dr. Phúc
- evidence [03:16:08]: "Còn những ai khỏe mạnh, xét nghiệm tốt đẹp như tranh vẽ, cơ thể chúng ta không bị bệnh các thứ gì thì chúng ta mua cái DHA tăng lên một chút"
- evidence [03:16:21]: "thì chúng ta sẽ rất thông minh, sẽ mắt sẽ rất tinh"
- evidence [03:16:28]: "các cháu uống DHA này vào thì các cháu sẽ thông minh lên"
- note: Hedged and first-person; matches.

## c148 (from audit c137) — supported
- claim: Ông dặn đừng để mất cân bằng: quá nhiều DHA mà ít EPA hoặc ngược lại thì không nên.
- speaker: Dr. Phúc (03:18:30)
- evidence [03:18:30]: "Còn đừng có để mất cân bằng. Tức là quá nhiều DHA mà lại ít EPA hoặc ngược lại quá nhiều EPA mà lại ít DHA thì chúng ta cũng không nên"
- note: The summary shortens 'hoặc ngược lại'; meaning unchanged.
