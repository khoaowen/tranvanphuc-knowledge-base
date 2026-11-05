---
id: 14
type: story
title: "The owner approves the tags used by the V-Qfwjo28Zg summary and each approved tag is added to the controlled vocabulary"
parent: epic-video-knowledge-pipeline
after: []
refined: true
hitl: true
risk: medium
---

# The owner approves the tags used by the V-Qfwjo28Zg summary and each approved tag is added to the controlled vocabulary

## Description

topics/vocabulary.md grows by human approval only. The V-Qfwjo28Zg summary uses 8 tags outside it (gốc tự do, glutathion, chống oxy hóa, vi chất, bóng đè, vitamin D, thiếu máu thiếu sắt, lối sống lành mạnh). The owner approves, renames or rejects each tag; approved tags are added.

## Requirements

1. **Every tag gets a decision**
   **Given** the 8 tags the V-Qfwjo28Zg summary uses outside `topics/vocabulary.md`
   **When** the owner reviews them
   **Then** each tag has one recorded decision: approve, rename or split into stated tags, or reject, with a one-line reason
   **And** the record sits in Notes of this file, so a later ticket can read it.

2. **Approved tags join the vocabulary**
   **Given** the decisions
   **When** the vocabulary is updated
   **Then** `topics/vocabulary.md` gains exactly the approved tags, and the renamed or split tags under their new names, one per line
   **And** a rejected tag is not added.

3. **The validator accepts approved tags**
   **Given** a summary header whose topic tags are all in the updated vocabulary
   **When** `validate_summaries.py` checks the tags
   **Then** it reports no "tags outside vocabulary" reason.

4. **The validator still rejects an unapproved tag**
   **Given** a header with one tag that is neither in the vocabulary nor approved here
   **When** `validate_summaries.py` checks the tags
   **Then** it reports that tag as "tags outside vocabulary".

5. **No near-duplicate by accident**
   **Given** the existing tag `vitamin d3` and the proposed `vitamin D`
   **When** the owner decides on `vitamin D`
   **Then** the decision names whether it is a new tag or replaced by `vitamin d3`, and the same is stated for any other tag that overlaps an existing one.

## Boundaries

- Must not change: the 8 existing tags, any topic page, `scripts/validate_summaries.py`, its tests, `videos/`, and the audit files.
- Must not change: the V-Qfwjo28Zg summary. Applying a rename to it belongs to tickets 2.5 and 2.6, which build the temporary summary.

## References

- parent — _bmad-output/initiative-tran-van-phuc-knowledge-base/tickets/epic-video-knowledge-pipeline/epic-video-knowledge-pipeline.md
- ../../../audit/V-Qfwjo28Zg/regenerated/owner-decision-brief.md
- ../../../summary-contract.md

## Notes

- Risk medium: tags apply to every later video, so a wrong tag spreads, but one line in a text file reverts it.
- Decision recorded from the owner's instruction: approve the seven tags below as new vocabulary entries, and split `thiếu máu thiếu sắt` into two new entries, `thiếu máu` and `thiếu sắt`. Add 9 tags total. Keep `vitamin D` as a separate tag; do not replace it with existing `vitamin d3`. Tickets 2.5 and 2.6 will apply the split tags in the summary header.

| Original summary tag | Owner's decision | Vocabulary entries to add |
|---|---|---|
| gốc tự do | Approve as a new tag | gốc tự do |
| glutathion | Approve as a new tag | glutathion |
| chống oxy hóa | Approve as a new tag | chống oxy hóa |
| vi chất | Approve as a new tag | vi chất |
| bóng đè | Approve as a new tag | bóng đè |
| vitamin D | Approve as a new tag, distinct from existing `vitamin d3` | vitamin D |
| thiếu máu thiếu sắt | Split into two new tags | thiếu máu; thiếu sắt |
| lối sống lành mạnh | Approve as a new tag | lối sống lành mạnh |

- Tag comparison ignores case and Unicode composition, so `vitamin D` and `vitamin d` are the same tag.
