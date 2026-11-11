# Walkthrough: ticket 1.14, owner-approved topic tags

Target: commit [b043891](../../../topics/vocabulary.md) "feat: add owner-approved topic vocabulary" (9 lines added to `topics/vocabulary.md`, plus its plan file). Status: ticket 1.14 is `built`, marked done after this walkthrough.

Review complete: all blocks accepted by the owner; ticket 1.14 marked done.

- [x] **1. Intent** (accepted, unchanged)
- [x] **2. Broad strokes** (accepted, unchanged)
- [x] **3. The nine vocabulary lines** (accepted, unchanged)
- [x] **4. Does the validator behave as the ticket requires?** (accepted, unchanged)
- [x] **5. Periphery** (accepted, unchanged)

## 1. Intent

From the ticket, [story 1.14](../tickets/epic-video-knowledge-pipeline/tickets/story-the-owner-approves-the-tags-used-by-the-v-qfwjo28zg-summary.md):

> `topics/vocabulary.md` grows by human approval only. The V-Qfwjo28Zg summary uses 8 tags outside it (gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu thiếu sắt, lối sống lành mạnh). The owner approves, renames or rejects each tag; approved tags are added.

The owner's decision, recorded in the ticket's Notes: approve seven as they are, split `thiếu máu thiếu sắt` into `thiếu máu` and `thiếu sắt`, keep `vitamin D` separate from `vitamin d3`. That makes 9 new entries.

## 2. Broad strokes

The change is nine appended lines in a plain text file that the validator reads.

- [topics/vocabulary.md](../../../topics/vocabulary.md): the controlled tag list; the nine new lines are 10 to 18.
- [scripts/validate_summaries.py](../../../scripts/validate_summaries.py): reads that file and rejects summary tags that are not in it. Not changed.
- [Ticket 1.14](../tickets/epic-video-knowledge-pipeline/tickets/story-the-owner-approves-the-tags-used-by-the-v-qfwjo28zg-summary.md): holds the decisions table the nine lines come from.
- [Plan file](../tickets/epic-video-knowledge-pipeline/tickets/story-the-owner-approves-the-tags-used-by-the-v-qfwjo28zg-summary-plan.md): the build record.

## 3. The nine vocabulary lines

Mechanism: the validator compares tags after Unicode normalization and case folding, so a line only has to match in that sense. The nine lines are exactly the ticket's table, one per line, and the merged tag `thiếu máu thiếu sắt` was not added.

- [topics/vocabulary.md](../../../topics/vocabulary.md) lines 10 to 18.
- `vitamin D` sits next to the existing `vitamin d3` as its own entry, as the owner decided.

## 4. Does the validator behave as the ticket requires?

Mechanism: the ticket asks that approved tags pass and an unapproved tag is still reported as "tags outside vocabulary". Nothing in the validator was edited, so this depends only on the vocabulary content.

- Entry points: `norm` and `load_vocabulary` in [scripts/validate_summaries.py](../../../scripts/validate_summaries.py).
- The plan file reports 41 validator tests passing.

## 5. Periphery

- The plan file is the only other file in the commit.
- Not touched, as the ticket requires: the 8 old tags, `scripts/`, `tests/`, `videos/`, audit files, the summary.
- Tickets 2.5 and 2.6 were to apply the split tags in the summary header; that is outside this commit.
