# Walkthrough: uncommitted work on ticket 2.3 (q7uDJG8YQ5c corrections)

Target: the uncommitted working tree on top of `5f4536d`.
Current block: none (all blocks accepted).

- [x] **1. Intent**
- [x] **2. Broad strokes**
- [x] **3. Gate change: cross-section evidence is allowed**
- [x] **4. Tests**
- [x] **5. Applied corrections to the omega-3 summary**
- [x] **6. Periphery**

## 1. Intent

Source: the target plan, [story-apply-approved-corrections-q7uDJG8YQ5c-plan.md](../tickets/epic-summary-source-audit/tickets/story-apply-approved-corrections-q7uDJG8YQ5c-plan.md), Intent section (condensed).

Ticket 2.3 applies the 24 human-approved corrections to the q7uDJG8YQ5c (omega-3) summary. The video stays blocked from publication. While applying them, a follow-up came up: the fidelity review rejected a claim whose verbatim transcript quote was real but sat outside the claim's own summary section. This step lets such a claim pass, as long as the quote is authentic and every other check holds. It adds regression tests and stops for your review. Nothing is staged, committed or published.

## 2. Broad strokes

1. [review_summaries.py `aggregate_claim`](../../../scripts/review_summaries.py) — turns per-chunk evidence into a claim verdict; the section-window rule is removed here.
2. [queue_state.py `current_review`](../../../scripts/queue_state.py) — the publish gate; the same rule is removed here.
3. [test_review_summaries.py](../../../tests/test_review_summaries.py) — the old "wrong timestamp" expectations are flipped, and new negative cases are added.
4. [summary.md](../../../videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/summary.md) — the 24 corrections as applied text.
5. [review.md](../../../videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/review.md) — the stored review, rewritten against the new summary.

## 3. Gate change: cross-section evidence is allowed

Mechanism: the section-window rule existed in two places, aggregation and the publish gate. Both drop it. Quote authenticity, timestamp matching, the semantic flags and coverage stay.

- [aggregate_claim](../../../scripts/review_summaries.py): `located` and `misplaced` are removed. Pass now needs at least one clean verbatim evidence anywhere. Clean means supported, attributed and qualifications preserved, with no contradiction.
- [current_review](../../../scripts/queue_state.py): the `in_section_window` predicate is removed, along with the `zip(claims, expected)` that fed it.

## 4. Tests

Mechanism: old expectations are flipped, and negative cases show the relaxed rule does not let defects through.

- [test_verbatim_evidence_before_or_after_section_passes](../../../tests/test_review_summaries.py): quotes found before and after their section now pass, and the review is publishable.
- [test_cross_section_evidence_does_not_excuse_content_failures](../../../tests/test_review_summaries.py): each of supported=False, attributed=False, qualifications_preserved=False and contradicts=True still fails the claim, and nothing is publishable.
- [test_strict_pass_accepts_cross_section_quote_but_rejects_invalid_evidence](../../../tests/test_review_summaries.py): the gate accepts a cross-section quote, and rejects a wrong timestamp, a fabricated quote and an invalid timestamp.

## 5. Applied corrections to the omega-3 summary

Mechanism: the summary was edited in three waves, all uncommitted and all documented in [apply-report.md](../spec-summary-source-audit/audit/q7uDJG8YQ5c/apply-report.md).

1. The 24 approved corrections (13 reviewer-approved, 11 revised in r2). All applied, 61 quotes checked, 0 failures.
2. Follow-ups f1-f4, human-approved on 2026-10-15, drafted in [proposed-corrections-followup.md](../spec-summary-source-audit/audit/q7uDJG8YQ5c/proposed-corrections-followup.md).
3. An "opus review loop" of further edits (c157, c013, c082, ...), made at "follow opus review to fix everything". These are outside both approved lists.

Edits are in [summary.md](../../../videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/summary.md). The review is [review.md](../../../videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/review.md).

## 6. Periphery

- [approval-record.md](../spec-summary-source-audit/audit/q7uDJG8YQ5c/approval-record.md): notes that corrections are applied, uncommitted, video still blocked.
- [proposed-corrections.md](../spec-summary-source-audit/audit/q7uDJG8YQ5c/proposed-corrections.md): c087 quote fragment fixed, c119 block restored.
- [audit-summary.md](../spec-summary-source-audit/audit/q7uDJG8YQ5c/audit-summary.md), [report.md](../spec-summary-source-audit/audit/q7uDJG8YQ5c/report.md): status lines updated.
- [spec-summary-source-audit.md](../spec-summary-source-audit/spec-summary-source-audit.md), [epic-summary-source-audit.md](../tickets/epic-summary-source-audit/epic-summary-source-audit.md), [story-apply-approved-corrections-q7uDJG8YQ5c.md](../tickets/epic-summary-source-audit/tickets/story-apply-approved-corrections-q7uDJG8YQ5c.md): small status notes.
- New artifacts in `spec-summary-source-audit/audit/q7uDJG8YQ5c/`: apply-report.md, claims-after-apply.md, final-claims-audit.json, final-claims-mapping.md, proposed-corrections-followup.md, proposed-omissions.md, split-claims-audit.json, split-claims-audit.md, tool-fix-report.md.
- New plan: [story-apply-approved-corrections-q7uDJG8YQ5c-plan.md](../tickets/epic-summary-source-audit/tickets/story-apply-approved-corrections-q7uDJG8YQ5c-plan.md).
