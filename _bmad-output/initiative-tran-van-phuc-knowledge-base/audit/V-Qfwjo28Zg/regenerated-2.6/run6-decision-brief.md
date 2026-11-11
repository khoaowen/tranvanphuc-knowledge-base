# Ticket 2.6, run 6 decision brief

**Proposals only. No edits applied, no gate run, `summary.md` untouched.** V-Qfwjo28Zg stays blocked. The definition of done is unchanged.

Run 6 reviewed summary `5bdca9fc…` (same file as run 5; Codex gpt-6.1-sol). Verdict fail, 582 claims (571 pass, 11 fail), 2 concerns, 4 omissions, `coverage_complete` false. Review: `gate-run6/work/V-Qfwjo28Zg/review.md`. Run-6 claim IDs are used below. Transcript = `gate-run6/work/V-Qfwjo28Zg/transcript.md`.

## Same text, different verdicts

Run 5 failed c101, c208, c433, c540 and raised the c047 and catalase concerns. Run 6 reads the same text and passes them, with no concern on c047 or catalase. I did not re-check them. They are not open for this run, and I propose no edits. Run 6 also fails new claims (c221, c232, c527, c468, c491, c567) that run 5 passed.

## A. Already decided, no new information (accept)

| Run-6 claim | Why it is not new |
|---|---|
| c113 (xương cổ đùi split) and its concern | Accepted by owner earlier. Same finding as runs 4 and 5. |
| c488 (GSSG note) | Editorial note, accepted in run 4. The gate cannot verify a note about its own transcript. |
| c491 (NADPH note) | Same kind as c488: the note states the transcript has "NA/DPH" and "NADH". |
| c528 (no dose or condition stated) | Absence-of-detail caveat, accepted in run 3. |
| c567 (summarizer note about transcript wording) | Same kind as c528, a note with no transcript text to check. Not in the decisions recorded so far, so **needs your accept**. |

## B. Unresolved findings

### B1. c312, vitamin D "5.600 UI" (material concern, still open)

Transcript at [02:49:13](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10153s): "Có người chỉ có 5 600 UI đã đủ rồi nhưng có người lên tới 6 7000 UI cơ … Nhưng đại đa số mọi người là con số trên dưới 2000 UI."

- **Audio check: not done.** I could not do it. `yt-dlp` was refused by YouTube ("Sign in to confirm you're not a bot"). No local audio exists. No speech-recognition tool is installed. I did not use browser cookies without your approval.
- **What the transcript alone suggests (not proof).** "Chỉ có … đã đủ" means "only … is enough", a low figure against the 2,000 average. The two figures are written in parallel, "5 600" and "6 7000". In Vietnamese speech that pattern is usually "năm sáu trăm" (500–600) and "sáu bảy nghìn" (6,000–7,000). 5,600 would sit above the 2,000 average, which does not fit "chỉ … đã đủ". The reading 500–600 / 6,000–7,000 fits the sentence better.
- **Conflict with your earlier decision.** `human-decisions.md` (c201) records "5.600 UI đúng; 6.000 đến 7.000 UI đúng". I do not know whether that came from listening or from reading the transcript.
- **Decision needed.** Please listen at [02:49:10](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10150s) (about 10 seconds), or tell me you already did.
  - If 500–600: change the summary to "khoảng 500 đến 600 UI".
  - If 5,600: keep the text.
  - If unclear: use "(phiên âm ghi '5 600', chưa xác định được con số)".
- This is the only finding that can put a wrong number into the public summary.

### B2. "chồng" vs "bố chồng" (c221, c232, c527)

The summary already discloses your correction. The gate fails each claim because each chunk it reads has only "chồng".

New transcript evidence:
- At [01:11:18](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=4278s) a comment from a nurse named Ngân is read out. At 01:11:55 the comment says "em đã bổ sung vi chất cho **bố chồng** bị tiểu đường … 5.5 đến 6.8".
- At [02:10:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=7854s) the doctor says "chị Ngân nói rằng chồng chị là bị tiểu đường", about the same chị Ngân and the same topic.

So "bố chồng" is supported inside the same transcript, and the doctor's "chồng" is a slip.

- **Proposal: keep as is and accept** all three. The gate cannot see across chunks.
- **Optional:** add "(xem mục 01:11:21)" to the disclosures. This changes wording only and needs your approval. It would not stop the gate failing these claims.

### B3. c381, Japan ("như bản")

The transcript reads "như bản" and the owner confirmed Nhật Bản. The summary says so and the evidence for the figure is unchanged. Run 6 flags only the confirmation. Run 5's side suggestion was to change "Ông so sánh" to "Phần nhận xét so sánh". Run 6 did not raise that. **Proposal: keep and accept.** The attribution change is optional.

### B4. c468, hometown (Hải Dương vs Hưng Yên)

- Transcript at [04:15:00](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15900s): "quê bác ở Hải Dương".
- Transcript at [02:54:15](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=10455s) (c315, passed): "Hưng Yên".
- The summary shows both and discloses the conflict. The gate fails c468 because the earlier detail is not in its chunk.

**Proposal: keep and accept.** The speakers disagree and the summary says so.

## C. Omissions (4)

| Omission | Seen before | Proposal |
|---|---|---|
| [01:50:49](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=6649s), block nhĩ thất and ngoại tâm thu linked to giật mình and bóng đè | Run 4 and run 6. Also matches 2.5 `review.md` (not verified). | **Add (draft):** "Bác sĩ liên hệ rối loạn nhịp tim như block nhĩ thất và ngoại tâm thu với cảm giác giật mình, bóng đè." |
| [04:12:21](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=14741s), bẫy khí in COPD | Run 6; 2.5 files also mention this timestamp (not verified). | **Accept**, or add on your decision. It is a side remark ("một câu chuyện rất phức tạp"). |
| [01:01:54](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=3714s), the "cảm tử" step itself creates more free radicals | New in run 6. Not in runs 3–5. | **Accept** (first appearance). Summary line 135 already describes the three steps. |
| [04:25:28](https://www.youtube.com/watch?v=V-Qfwjo28Zg&t=15928s), naming cacbon alpha and beta | New in run 6, but the same topic as O13 (accepted). | **Accept** under O13. |

Not repeated in run 6 (nothing proposed): the run-5 items O9 (symptoms in bác Nghiên's case), outer-mitochondrial glutathione, and the other run-5 omissions.

## D. The definition of done, stated without changing it

Done means only accepted failures remain **and** `coverage_complete` is true. Every run so far has had `coverage_complete` false, and run 6 has 4 omissions. Accepting omissions does not change that flag. So acceptance alone may not reach "done", whatever you decide in B and C. Options for you: add the omissions you choose (e.g. 01:50:49), or keep ticket 2.6 open. I propose no change to the definition. Any change needs your explicit approval and a ticket amendment.

## Decisions I need from you

1. **B1:** audio result for 02:49:13 (500–600 or 5,600), or tell me to leave it unresolved.
2. **A and B2–B4:** approve "accept" for c567, c221/c232/c527, c381 and c468 (the others are already accepted). Say whether you want the optional "(xem mục 01:11:21)" disclosure or the optional "Phần nhận xét so sánh" wording.
3. **C:** add the 01:50:49 block-nhĩ-thất sentence, or accept it.
4. No paid run is requested or implied.
