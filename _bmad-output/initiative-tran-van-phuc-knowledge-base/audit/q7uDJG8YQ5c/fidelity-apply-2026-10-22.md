# Fidelity apply report: c068 and c163, q7uDJG8YQ5c (2026-10-22)

> 2 corrections applied, video still blocked (`publishable` = false)

The owner (BDK) approved the exact text of p1 and p2 in `proposed-corrections-fidelity.md` on 2026-10-22 and authorised applying them. Each `current` text occurred exactly once in `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/summary.md` and was replaced with the approved text, verbatim. No other line changed.

## Source hashes (sha256)

| file | before | after |
|---|---|---|
| summary.md | `e8cef3b0e5aa9caa7a84fab6dca4b08e0d5c20de2dcf0a9988db2cfd1a9ac620` | `04ba0755a8500d5e024f8de87027dda8ef3b67384e0eec0abec5d768e0d94ff8` |
| transcript.md | `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b` | unchanged |

## Claim extraction (`fidelity.extract_claims`)

194 claims before and after. The ids are identical, and the sections are unchanged. Text alignment with difflib shows exactly two replaced claims and 192 unchanged claims:

| id | section | old text | new text |
|---|---|---|---|
| c068 | [01:42:36] Khái niệm màng tế bào là bộ não của tế bào | …bác sĩ nói nguyên phân tạo ra hai tế bào, còn giảm phân tạo ra bốn. | …bác sĩ nói qua quá trình gián phân thì một tế bào tạo nên hai tế bào bằng cách phân chia nhân, còn qua quá trình giảm phân thì một tế bào tạo thành 'bốn bào tử'. |
| c163 | [03:01:21] Công thức tính tỷ lệ EPA và DHA để lựa chọn dầu cá | Alzheimer 'cải thiện được rất nhiều' (Parkinson được nhắc trong cùng đoạn, người nói không rõ); ông nói từ 0,6 trở lên thì giá thành đắt. | Ông nhắc đến Alzheimer ('nhớ nhớ quên quên') và Parkinson ('run rẩy tay chân'), nói là 'cải thiện được rất nhiều, học hành nó tốt'; ông nói từ 0,6 trở lên thì giá thành đắt. |

The 194-claim baseline and its id scheme are therefore unchanged. `supplement-records.json` is kept as the historical record and has not been edited. The records below supersede its c068 and c163 entries.

## Superseding records

- **c068: supported (caption + asr + human).** Evidence: "Nếu qua quá trình dán phân thì một tế bào sẽ tạo nên hai tế bào bằng cách là phân chia nhân." (01:45:28-01:45:33) and "Thế còn qua quá trình giảm phân thì một tế bào sẽ tạo thành bốn bào tử" (01:45:35-01:45:37). "gián phân" is not a caption substring: the caption has the homophone "dán". The spelling rests on blind ASR and on BDK's listen (A1, A-xref).
- **c163: supported (caption + human speaker identity).** Evidence: "Alzimer run rẩy tay chân Parkison." (03:02:47), "nhớ nhớ quên quên" (03:02:51), "cải thiện được rất nhiều, học hành nó tốt" (03:02:51-03:02:53) and "từ 0,6 trở lên nhưng mà giá thành đắt" (03:02:55). Speaker: Dr. Trần Văn Phúc, per BDK (B1-B4, 100% confidence, non-blind). The condition-to-phrase pairing follows BDK's B2; the caption order differs.

Every single-quoted fragment in both new texts resolves as a verbatim transcript substring via `fidelity.resolve_quote`.

## Impact on other checks

- Omissions: no item in `omissions.md`, `omissions-recheck.md` or `proposed-omissions.md` cites c068 or c163. The 11 covered / 11 still omitted tally is unaffected. Its input-hash header now refers to the previous summary.
- `review.md` is not refreshed. It is hash-bound to the previous summary, so `queue_state.current_review` is false and the video state is `summarized`. A refresh would be a model run and needs separate approval.
- Still pending, not touched: c019, c055, c192, and the omission proposals.
- Uncommitted and unpushed at the time of writing. Publication not unblocked.
