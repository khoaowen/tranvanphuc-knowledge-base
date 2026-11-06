# Walkthrough: ticket 2.4 (V-Qfwjo28Zg summary rebuilt, review of the run)

Target: uncommitted output of ticket 2.4 on branch `khoaowen/lane-b-audit` (HEAD `b043891`): [regenerated/](../audit/V-Qfwjo28Zg/regenerated/), [regenerated-timefix/](../audit/V-Qfwjo28Zg/regenerated-timefix/), new audit side files, and edits to three tracked audit files.
Current block: none (all blocks accepted; wrap-up pending).

- [x] 1. Intent (accepted, unchanged)
- [x] 2. Broad strokes (accepted, unchanged)
- [x] 3. Slice: the 15 approved replacements (accepted, unchanged)
- [x] 4. Slice: owner decisions beyond the 15 (accepted, unchanged)
- [x] 5. Slice: validators and review gate (criterion 3 fails) (accepted, unchanged)
- [x] 6. Slice: claim mapping and the 46 undecided items (accepted, unchanged)
- [x] 7. Slice: edits to tracked audit files (accepted, unchanged)
- [x] 8. Periphery (accepted, unchanged)

## 1. Intent

Source: ticket 2.4, [story file](../tickets/epic-summary-source-audit/tickets/story-a-current-v-qfwjo28zg-summary-is-built-from-the-historical-text-an.md) (summarised, not verbatim: the Description is below).

> `videos/` has no `summary.md` for V-Qfwjo28Zg: the old one was removed in `4e31e57` to re-queue the video. This story builds one current summary by applying the 15 replacements the owner approved to the historical summary text, in a temporary folder outside `videos/`, then validates it and leaves a report. ... Applying the result to `videos/` is a separate ticket with its own approval and start.

## 2. Broad strokes

Historical summary text plus approved edits go into a scratch folder; a report scores the result against the 9 criteria. Nothing touches `videos/`.

1. [provenance.json](../audit/V-Qfwjo28Zg/regenerated/provenance.json): six input hashes, all matching the ticket.
2. [summary.md](../audit/V-Qfwjo28Zg/regenerated/summary.md): the product, 565 claims, 8 tags outside the vocabulary.
3. [report.md](../audit/V-Qfwjo28Zg/regenerated/report.md): criteria table, 15-replacement table, owner decisions, undecided items.
4. [human-decisions.md](../audit/V-Qfwjo28Zg/human-decisions.md): source of every change beyond the 15.
5. [regenerated-timefix/report.md](../audit/V-Qfwjo28Zg/regenerated-timefix/report.md): byte-identical copy plus a heading-time drift report; changes nothing.

## 3. Slice: the 15 approved replacements

Mechanism: each of the 15 claims in the historical text (c318, c156, c275, c544, c552, c286, c158, c242, c260, c402, c213, c538, c278, c279, c013) was replaced by the owner-approved sentence from the draft. The report lists each one with its new line, section and reason, and says 15 applied, 0 not applied.

- [report table](../audit/V-Qfwjo28Zg/regenerated/report.md): all 15 rows (lines 21-41).
- c013: [summary.md line 33](../audit/V-Qfwjo28Zg/regenerated/summary.md). The report admits the sentence reads a little repetitive.
- c156/c158: [summary.md line 210](../audit/V-Qfwjo28Zg/regenerated/summary.md). The wake-to-sleep direction is merged into one item.
- c278/c279: [summary.md line 372](../audit/V-Qfwjo28Zg/regenerated/summary.md). The "u não" remark is attributed to the doctor, not to chị Nhung.
- Reference to compare against: [revised-summary-draft.md](../audit/V-Qfwjo28Zg/revised-summary-draft.md).
## 4. Slice: owner decisions beyond the 15

Mechanism: [human-decisions.md](../audit/V-Qfwjo28Zg/human-decisions.md) records 17 further decisions. The run applied all of them, which is wider than the ticket's minimum list. The report records this as "all recorded decisions applied", chosen by the owner. [report.md section 3](../audit/V-Qfwjo28Zg/regenerated/report.md) lists what was done.

- Removed: c456 (the general disclaimer at c553 stays).
- Rewritten: c509 at [summary.md line 670](../audit/V-Qfwjo28Zg/regenerated/summary.md); c401, c070, c250, c488.
- Labelled: c541 as summariser's note at [line 707](../audit/V-Qfwjo28Zg/regenerated/summary.md).
- Owner confirmations not in the transcript, labelled as such: Nhật Bản at [line 489](../audit/V-Qfwjo28Zg/regenerated/summary.md), the 2.000 UI figures at [line 251](../audit/V-Qfwjo28Zg/regenerated/summary.md), GSSG and NADPH near [line 626](../audit/V-Qfwjo28Zg/regenerated/summary.md).
- Added: audience stories o19-o22 under "Khán giả tự kể" at [line 189](../audit/V-Qfwjo28Zg/regenerated/summary.md) and [line 194](../audit/V-Qfwjo28Zg/regenerated/summary.md); the doctor retelling a letter at [line 615](../audit/V-Qfwjo28Zg/regenerated/summary.md); the early-stage vitamin D reason (three sentences).
## 5. Slice: validators and review gate

Mechanism: criterion 3 runs `validate_summaries.py` and the LLM review gate on the scratch folder. The run reported both failing. Neither was patched, per the ticket.

- Validator, as reported: 8 tags outside the vocabulary ([report.md section 7](../audit/V-Qfwjo28Zg/regenerated/report.md)). Re-run today, after `b043891` added the owner-approved vocabulary ([topics/vocabulary.md](../topics/vocabulary.md)): only `thiếu máu thiếu sắt` remains outside it, because the vocabulary has `thiếu máu` and `thiếu sắt` as two tags. Header at [summary.md line 6](../audit/V-Qfwjo28Zg/regenerated/summary.md).
- Review gate: verdict fail, 565 claims, 48 fail, 26 concern, 14 omission, coverage incomplete; it names the summary's SHA. Output in [review.md](../audit/V-Qfwjo28Zg/regenerated/review.md).
- Of the 6 failing claims that this run changed or added, 5 are labels or owner confirmations with no transcript evidence. c286 (from c278) joins two quotes from two moments; the reviewer failed it. See [review.md c286](../audit/V-Qfwjo28Zg/regenerated/review.md).
- The other 42 failing claims are mostly inherited from the historical text. Review output is not deterministic between runs.
## 6. Slice: claim mapping and the 46 undecided items

Mechanism: criterion 8 maps the new claims onto the audit's claim records. Criterion 7 sorts the 63 non-supported items into followed, not followed and undecided. Both are in [report.md](../audit/V-Qfwjo28Zg/regenerated/report.md).

- Claim mapping ([section 5](../audit/V-Qfwjo28Zg/regenerated/report.md)): 554 historical claims become 565. 26 replaced or rewritten, 9 added, c456 removed; c070 splits into 3 and c544 into 2. Claim ids shift after additions, and the audit records are untouched. Added claims have no audit record, so a fresh audit would be needed. The report rates criterion 8 "partial": it gives counts and a diff list, not a claim-to-record table.
- Followed 17, not followed 0, undecided 46 ([section 4](../audit/V-Qfwjo28Zg/regenerated/report.md)). The undecided 46 keep their old sentences. The ticket said 48; the report explains why it counts 46.
## 7. Slice: edits to tracked audit files

Mechanism: three tracked files changed (uncommitted). They record owner decisions and new omissions. The status of each proposal stays `pending-human-approval`.

- [proposed-corrections.md](../audit/V-Qfwjo28Zg/proposed-corrections.md): 35 lines. For c070, c111, c201, c377 and others the `proposed` text now follows the owner's decision, and `why` gains a "Quyết định người duyệt" sentence. The JSON twin is not changed, so the .md and .json now disagree on those items.
- [omissions.md](../audit/V-Qfwjo28Zg/omissions.md): o29 removed; o48-o50 added (thức→ngủ, vitamin D early-stage reason, the letter). Header now says 49 kept, 20 excluded.
- [omission-anchors.json](../audit/V-Qfwjo28Zg/omission-anchors.json): 864 changed lines, but only about 36 are real changes once whitespace is ignored; the rest is re-indentation.
- Untracked companions: [additional-corrections.md](../audit/V-Qfwjo28Zg/additional-corrections.md), [additional-corrections.json](../audit/V-Qfwjo28Zg/additional-corrections.json), [human-decisions.md](../audit/V-Qfwjo28Zg/human-decisions.md).
## 8. Periphery

- [Plan file for ticket 2.4](../tickets/epic-summary-source-audit/tickets/story-a-current-v-qfwjo28zg-summary-is-built-from-the-historical-text-an-plan.md): the run's working plan, untracked.
- [owner-decision-brief.md](../audit/V-Qfwjo28Zg/regenerated/owner-decision-brief.md): brief for the owner's triage.
- [metadata.json](../audit/V-Qfwjo28Zg/regenerated/metadata.json) and [transcript.md](../audit/V-Qfwjo28Zg/regenerated/transcript.md): copies the validators need.
- [revised-summary-draft.md](../audit/V-Qfwjo28Zg/revised-summary-draft.md): the reference draft, untracked.
- [regenerated-timefix/](../audit/V-Qfwjo28Zg/regenerated-timefix/): copy plus drift report.
- Other untracked folders belong to other reviews: `walkthrough-revised-summary-draft/` and `review-pr9/`. They are not 2.4 output.
