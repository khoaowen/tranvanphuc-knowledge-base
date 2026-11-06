---
title: '2.4 Build V-Qfwjo28Zg summary from historical text plus 15 approved replacements'
type: 'chore'
ticket: '4'
created: '2026-11-02'
status: 'done'
baseline_revision: 'f7980cf8e7c4643b004a313ada90faa35bd2dd63'
route: 'oneshot'
route_source: 'auto'
risk: 'high'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** videos/ has no current summary for V-Qfwjo28Zg; owner approved 15 replacements plus other decisions on the historical text, nothing built yet.

**Approach:** Apply the 15 replacements and every decision recorded in human-decisions.md to the hashed historical summary, write only under audit/V-Qfwjo28Zg/regenerated/, validate, report. Owner decisions in this run: the other undecided items keep their old sentence and are reported "chưa quyết"; owner-confirmed evidence is labelled "xác nhận của người duyệt; phiên âm không chứa"; all recorded decisions are applied (c401, c070, c250, c488, vitamin D reason, crisis letter included); ticket 2.2 stays in review; no commit, stage, publish, status change. Paid external review model is not called without asking the owner.

</frozen-after-approval>

## Implementation Notes

Oneshot: data transformation by a throwaway script outside the repo; output only in regenerated/. Risk high (medical summary). Dirty tree is the owner-declared audit state and is left untouched.

Files written: audit/V-Qfwjo28Zg/regenerated/{summary.md,transcript.md,metadata.json,review.md,report.md,provenance.json} and this plan. Owner decisions during the run: apply all recorded decisions; run the pipeline review gate with codex gpt-6.1-sol (--no-commit). Result: validator fails on 8 header tags outside topics/vocabulary.md; review verdict fail (47/565 claims). Not committed, not done. The bmad quick review lens (subagent) was not run: subagents were not authorized.

## Review Triage Log

Quick lens (1 subagent không ngữ cảnh), diff `/tmp/review-diff-2.4.diff` (review.md, transcript.md loại khỏi diff). Không sửa gì ngoài plan này; các mục cần sửa chỉ báo cho owner (route = báo owner, không patch).

| # | Vị trí | Phát hiện | Verdict | Bằng chứng / hướng xử lý |
|---|---|---|---|---|
| 1 | summary.md mục [04:21:40], ghi chú NADPH | Nhãn "phiên âm không chứa" nhưng đồng thời dẫn "NA DPH" | low | transcript dòng 6789-6790 `NA` / `DPH.` bị ngắt dòng; nhãn do plan quy định nhưng câu hơi tự mâu thuẫn. Đề xuất: đổi thành "phiên âm ngắt dòng NA/DPH". |
| 2 | summary.md mục [01:33:05], c201 | Nhãn "xác nhận của người duyệt; phiên âm chỉ ghi '5 600'…" lệch chuỗi plan | low | Report §3 giải thích (phiên âm có chuỗi gần đúng); số liệu khớp human-decisions. Đề xuất: owner chấp nhận hoặc đổi về chuỗi chuẩn. |
| 3 | summary.md mục [03:36:48], "người duyệt xác nhận là thì thở ra" | Nhãn vượt phạm vi quyết định | false | human-decisions.md dòng 17: quyết định chính là "kéo dài thì thở ra, không phải nín thở"; nhãn khớp. |
| 4 | summary.md mục [03:36:48], "nhịn được 15 giây, 10 giây" cạnh "không phải nín thở" | Chỉ dẫn thở gây hiểu lầm nội tại | medium | Câu phiên âm dòng ~6210-6218 giữ "nhịn được"; c402 giữ theo nguồn theo quyết định, nhưng người đọc có thể hiểu mâu thuẫn trong nội dung liên quan an toàn. Đề xuất: owner quyết ghi chú làm rõ. |
| 5 | summary.md mục [01:33:05], vitamin D | Chữ "khoảng nồng độ" không có trong phiên âm | low | transcript 4229-4232 chỉ có "trong khoảng này"; "nồng độ" là diễn giải theo ngữ cảnh. Đề xuất: đổi thành "một khoảng" hoặc owner chấp nhận. |
| 6 | summary.md [01:33:05] t=5585s và [04:19:29] t=15569s | Nội dung vitamin D / thư khủng hoảng nằm dưới heading lệch giờ | low | Thực tế ~02:46 (t≈9956s) và ~04:46 (t≈17149s) theo human-decisions; lỗi heading kế thừa bản lịch sử, report §8 đã nêu. Đề xuất: ticket riêng sửa heading. |
| 7 | summary.md [01:31:32], c156/c158 vs o48 | Mất "tim đập nhanh" ở chiều thức→ngủ | low | transcript 3846-3848 có ý đó; c158 bỏ đúng theo bản đã duyệt, human-decisions chỉ yêu cầu gộp theo đề xuất. Đề xuất: owner quyết có thêm hay không. |
| 8 | report.md §1 dòng 8 (tiêu chí 8) | Chấm "Đạt" khi thiếu bảng ánh xạ claim→record | low | Report §5 có số liệu 554→565, tách/thêm/xóa; intent cho phép áp dụng mọi quyết định. Đề xuất: bổ sung bảng ánh xạ hoặc đổi nhãn. |
| 9 | report.md §1 dòng 2 (tiêu chí 2) | Chấm "Đạt" dù áp dụng rộng hơn chữ ticket | low | Intent đóng băng: "all recorded decisions are applied". Đề xuất: ghi "đạt theo intent". |
| 10 | report.md §3 dòng 61 | "ba mục cuối" liệt kê bốn nhóm; c013 lặp câu mở | low | Xác nhận ở dòng 61; cosmetic. Sửa trực tiếp khi owner cho phép. |
| 11 | diff: omission-anchors.json, omissions.md, proposed-corrections.md (tracked, sửa) | Run 2.4 sửa audit lịch sử | false | mtime 2026-11-01 08:24, trước run (summary.md 2026-11-02 07:51); dirty do owner khai báo, report §6 xác nhận git diff không đổi. |
| 12 | thư mục regenerated-timefix/ | Thư mục untracked ngoài phạm vi, không được nêu | false | Tạo 2026-11-02 14:41, sau report 2.4 (09:57); có report riêng (phương án A, giữ nguyên summary). Không do change này; chỉ lưu ý cho owner. |
| 13 | tiêu chí 3 (validator exit 1, 8 tag ngoài vocabulary) / review gate fail 47/565 | Tiêu chí chưa đạt | high | Đã tự ghi nhận ở Implementation Notes và report; chưa done. Cần owner quyết (thêm tag vocabulary hoặc đổi tag). |

Đã đối chiếu và khớp (không có phát hiện): đếm 15 thay thế (15/15), 46 "chưa quyết" (17+46=63), 554→565; c156/c278/c279 đúng ràng buộc; c377, c471 đúng nhãn.
