# Apply report — q7uDJG8YQ5c

> corrections applied, uncommitted, video still blocked

Target: `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/summary.md`. Source: `proposed-corrections.md` revision 2.

- Applied: 24. Not applied: 0. Total: 24.
- Tag counts: reviewer-approved 13, revised (r2) 11.
- Matching: each `current` text occurs exactly once in summary.md and its audit-time id points at that same text in claims.json (24/24). Reversing all 24 replacements reproduces HEAD summary.md byte for byte, so no other line changed.
- c119: its block in proposed-corrections.md was corrupted (already in HEAD); restored from r1 with the human's confirmation. Tagged reviewer-approved (r1 text).
- Quote check: 61 supporting quotes, 0 failures (normalised case, punctuation, caption line breaks; searched at the cited timestamp, -3s to +75s). Single-quoted fragments in proposed texts: 37 checked, 1 not a verbatim substring (see flag).
- **c087 fixed at the human's request:** the fragment was 'có những nghiên cứu và tài liệu' (not verbatim). It is now 'có những nghiên cứu và những tài liệu' (verbatim, 02:28:43), changed in summary.md and in proposed-corrections.md. All 37 single-quoted fragments are now verbatim substrings.
- **Claim mapping:** 149 -> 160 claims; 7 items split (c001, c019, c064, c065, c128, c135, c137). Not one-to-one by itself; the human chose a new audit for the split claims. Result in `split-claims-audit.md`: 18 new records, all supported. Full mapping in `claims-after-apply.md`.
- Publication: `queue_state.publishable` = false. Not staged, not committed.
- review.md REFRESHED at the human's request (2026-10-15), by running `review_summaries.review_video` on this video only (sonnet, no commit). Old sha256 b30610e1…, new d219afe0…, hash-bound to the edited summary.md. `.review-progress.json` was its temporary cache and was deleted on completion. Verdict **fail**, coverage_complete false: 160 claims, 150 pass, 3 flag, 7 fail. Five fails (c002, c014-c017) and c121 are 'evidence outside the section's timestamp window' (the review tool's window rule, not content errors; c015-c017 are untouched by this run). c063 fail ('Omega-3 chiếm tới 30%' vs 'omega in general') is a real finding on a sentence these corrections did not touch. Flags: c032, c059, c140. The refresh does not change the blocked state; `queue_state.publishable` = false.

| audit id | result | tag | claims after | quotes ok | reason |
|---|---|---|---|---|---|
| c001 | applied | revised (r2) | c001, c002 | 3/3 | text and id matched once; split into 2 claims |
| c013 | applied | reviewer-approved | c014 | 2/2 | text and id matched once |
| c015 | applied | reviewer-approved | c016 | 2/2 | text and id matched once |
| c019 | applied | revised (r2) | c020, c021, c022 | 3/3 | text and id matched once; split into 3 claims |
| c029 | applied | reviewer-approved | c032 | 3/3 | text and id matched once |
| c036 | applied | reviewer-approved | c039 | 2/2 | text and id matched once |
| c045 | applied | revised (r2) | c048 | 2/2 | text and id matched once |
| c063 | applied | revised (r2) | c066 | 3/3 | text and id matched once |
| c064 | applied | revised (r2) | c067, c068, c069 | 3/3 | text and id matched once; split into 3 claims |
| c065 | applied | revised (r2) | c070, c071 | 3/3 | text and id matched once; split into 2 claims |
| c068 | applied | reviewer-approved | c074 | 1/1 | text and id matched once |
| c069 | applied | reviewer-approved | c075 | 1/1 | text and id matched once |
| c085 | applied | reviewer-approved | c091 | 3/3 | text and id matched once |
| c087 | applied | reviewer-approved | c093 | 3/3 | text and id matched once ; fragment flag |
| c106 | applied | revised (r2) | c112 | 4/4 | text and id matched once |
| c108 | applied | reviewer-approved | c114 | 2/2 | text and id matched once |
| c113 | applied | reviewer-approved | c119 | 1/1 | text and id matched once |
| c119 | applied | reviewer-approved | c125 | 3/3 | text and id matched once |
| c123 | applied | revised (r2) | c129 | 3/3 | text and id matched once |
| c127 | applied | reviewer-approved | c133 | 3/3 | text and id matched once |
| c128 | applied | revised (r2) | c134, c135 | 3/3 | text and id matched once; split into 2 claims |
| c135 | applied | revised (r2) | c142, c143, c144, c145 | 3/3 | text and id matched once; split into 4 claims |
| c136 | applied | reviewer-approved | c146 | 2/2 | text and id matched once |
| c137 | applied | revised (r2) | c147, c148 | 3/3 | text and id matched once; split into 2 claims |

## Follow-up after the apply (human-directed, outside the 24)
- c063-old (summary line 92, 'Trong cấu trúc màng tế bào nói chung, Omega-3 chiếm tới 30%.') corrected at the human's request, after the sonnet review failed it: now 'Theo bác sĩ Phúc, các axit béo omega nói chung chiếm tới 30% cấu trúc màng tế bào (ở một đoạn khác ông cũng nói Omega-3 chiếm 30%).' Basis: 02:22:06 says 'omega' in general; 01:48:21 says 'Omega 3 ... chiếm tới 30%'. This is NOT one of the 24 approved texts; it needs the human's review.
- review.md re-run with opus (replaces the sonnet review), bound to the current summary.md: 160 claims, 153 pass, 7 fail, 0 flag, verdict fail, coverage_complete false. All 7 fails (c002, c014-c017, c121, c156) are 'evidence outside the section timestamp window' (tool rule). c063 now passes.
- An opus run on the summary before the c063 fix also raised, on untouched sentences: c064 (DHA benefit lacks the condition 'DHA phải nhiều'), c072/c076/c077 (article-sourced Omega-6/Omega-3 ratio claims stated without attribution), and a material concern that c069/c070 omit the article's statement that no study shows Omega-6 causes disease. Those did not recur in the final run, so they are unresolved and not fixed.
- publishable = false.

## Follow-up f1-f4 applied (human approved 2026-10-15; outside the 24)
- Applied exactly as drafted in `proposed-corrections-followup.md` (status now `approved`): f1 (old c064, DHA condition), f2 (old c072+c073 merged into one claim), f3 (old c076, 'Theo tài liệu được đọc'), f4 (old c077 split into two claims: article caveat + oxidation point, closing clause kept). Each `current` text matched exactly once; all 7 supporting quotes were verbatim substrings.
- Claim count stays 160 (f2 -1, f4 +1). Current ids: f1=c064, f2=c072, f3=c075, f4=c076+c077; ids after c072 shift by -1 up to c076, so earlier mapping tables in claims-after-apply.md are valid only up to c071. New records for c072, c075, c076, c077 are NOT yet in split-claims-audit.*; the opus review below covers them.
- Opus review re-run on this summary (hash-bound): 160 claims, 152 pass, 8 fail, 0 flag, verdict fail, coverage_complete false. c064, c072, c075, c076, c077 all pass. Fails: c002, c014-c017, c121, c156 (timestamp-window rule, as before) and NEW c157 (the summary says the test measures the red-cell membrane; the doctor says 'trong hồng cầu'; text untouched by any correction, not fixed). Minor concerns: 'hệ mặt trời' vs 'hệ vũ trụ' (c013); C22:5n-3 notation for DHA is not in the transcript.
- publishable = false. Nothing staged or committed.

## Opus review loop (human: 'follow opus review to fix everything') — all outside the 24 and f1-f4, need the human's diff review
Edits to summary.md, each checked against transcript.md:
- c157 test: 'trong màng tế bào hồng cầu' -> 'trong tế bào hồng cầu'; added 'theo bác sĩ Phúc, xét nghiệm này hiện chưa được làm ở Việt Nam vì chưa có nhu cầu' (03:24:38-03:24:53).
- c013 piano: 'hệ mặt trời' -> 'hệ vũ trụ ... ; sau đó bác sĩ Phúc nói "hệ mặt trời"' (00:32:19, 00:32:46).
- c082 DHA: removed notation '(C22:5n-3)' (not in transcript), now '(theo lời bác sĩ Phúc)'.
- c132 (<0,3): hedged ('đang có xu hướng nhiều tạp chất...', plus 'gần với tự nhiên hơn, dễ hấp thu hơn', 03:01:21-03:01:48).
- Cousin story under L: now framed as told to show width (W) matters more than length (00:38:20-00:40:40).
- c142: removed the hedge 'tôi đang lấy ví dụ' (it belongs to the earlier example, 03:14:20).
- c059: 'theo ông Lipton, màng tế bào dường như đóng vai trò ... chứ không phải nhân tế bào' (01:44:38).
Final opus review (hash-bound, 160 claims): 154 pass, 6 fail, verdict fail, coverage_complete false. The 6 fails are the timestamp-window rule only (c002, c014-c017, c121, c156-class). One minor concern left: c116 'never buy hand-carried goods' is stricter than the doctor, who says the risk is poor storage in transit; not fixed. Each opus run raised some new minor concern on untouched text, so the loop does not converge to zero; I stopped when no content fail remained.
Claim count still 160 (verify), but ids/mapping in claims-after-apply.md and split-claims-audit.* are stale after f2/f4; not yet regenerated.
publishable = false.

## Final round (human: yes to c116, regenerate mapping, review diff)
- c116 (criterion 5): rewritten as 'Theo bài được đọc: ... không nên mua hàng xách tay hoặc hàng trôi nổi...; riêng hàng xách tay, bác sĩ Phúc nói vẫn có thể là sản phẩm tốt, vấn đề là vận chuyển và bảo quản' (03:10:27-03:10:46, 02:41:00).
- c136 (new opus fail): 'Thực tế ghi nhận người dùng loại 0,7...' was a generalised anecdote; now 'Bác sĩ Phúc kể tuần trước có mấy bác mang kết quả xét nghiệm đến... (các bác phản ánh là tốn tiền quá)' (03:03:27-03:03:50).
- Final opus review (hash-bound, 160 claims): 153 pass, 7 fail, verdict fail, coverage_complete false. All 7 fails (c002, c014-c017, c116, c121) are the timestamp-window rule; c116 now cites the 03:10 storage passage while its section is 02:39, which trips that rule.
- Mapping regenerated: `final-claims-mapping.md` + `final-claims-audit.json` (49 changed/new claims, quotes verified, 0 failures). They supersede claims-after-apply.md and split-claims-audit.*; those older files are kept, not edited.
- Hard limits re-checked: transcript.md unchanged, publishable = false, nothing staged or committed. review.md was rewritten (human-approved refresh); .review-progress.json absent.

## Accepted
- Human accepted the summary.md diff on 2026-10-18. Still uncommitted, video still blocked.

## Independent review by gpt-6.1-sol (via `codex exec -m gpt-6.1-sol -s read-only`, 2026-10-18)
- Spot-checked 14 changed claims against transcript.md (c013, c023, c059, c063, c064, c072, c076, c077, c082, c116, c132, c136, c142, c157): no unfaithful change found. Not a full-fidelity proof.
- Decision on the 7 timestamp-window fails: **A, leave blocked** and handle in a later ticket (tool cross-section evidence handling, assess recorded omissions such as the Omega-6 caveat and the <0,3 monitoring advice, regenerate the hash-bound review). Do not reword faithful claims just to satisfy the window rule. No override recommended yet.
- No files were modified by the reviewer. publishable = false; nothing staged or committed.
