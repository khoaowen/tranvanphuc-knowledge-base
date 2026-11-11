---
title: 'Add owner-approved topic tags'
type: 'feature'
ticket: '14'
created: '2026-11-06'
status: 'done'
baseline_revision: 'c798d607045bdd62ccffa5bc7177c44a128999e4'
route: 'oneshot'
route_source: 'auto'
risk: 'medium'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---
<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">
## Intent
**Problem:** Eight summary tags need owner decisions before entering the controlled vocabulary. The owner has already recorded those decisions in ticket 1.14.
**Approach:** Preserve those decisions and add exactly nine approved entries to `topics/vocabulary.md`, one per line: `gốc tự do`, `glutathion`, `chống oxy hóa`, `vi chất`, `bóng đè`, `vitamin D`, `thiếu máu`, `thiếu sắt`, and `lối sống lành mạnh`. The last two replace the proposed `thiếu máu thiếu sắt`; `vitamin D` is distinct from existing `vitamin d3`. Do not modify the ticket, existing vocabulary entries, topic pages, validator or tests, videos, summaries, or audit files.
</frozen-after-approval>
## Implementation Notes
Oneshot: nine-line vocabulary addition; existing ticket records owner decisions. Preserved existing dirty work. Added nine lines to topics/vocabulary.md. Validator tests: 41 passed via unittest; temporary fixture verified all approved tags accepted and unknown tag rejected. Python/pytest unavailable; standard-library unittest succeeded.
## Plan Change Log
## Review Triage Log
Quick review: no findings; high 0, medium 0, low 0, false 0, maybe-false 0.
## Verification
- Check the vocabulary diff contains exactly the nine approved new entries and preserves existing lines.
- Run the existing validator tests and verify using the validator that approved entries pass and an unknown tag yields `tags outside vocabulary`; avoid changing repository fixtures.
