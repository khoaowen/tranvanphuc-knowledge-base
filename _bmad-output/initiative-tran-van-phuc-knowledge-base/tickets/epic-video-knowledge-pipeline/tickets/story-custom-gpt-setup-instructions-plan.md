---
title: 'Custom GPT setup instructions'
type: 'feature'
ticket: '5'
created: '2026-10-29'
status: 'built'
baseline_revision: '58449c1e35b3eb2a9556f0a67d8d0526c793824c'
route: 'oneshot'
route_source: 'auto'
risk: 'medium'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/disclaimer.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Story 1.4 generates `knowledge-gpt/*.md`, but the owner has no documented GPT Builder hand-off or reusable answer instructions. Story 1.5 supplies that manual step; it does not operate or publish a hosted GPT.

**Approach:** Add `docs/custom-gpt-setup.md` and link it from README's hand-written Browse paragraph. Explain account/workspace permission prerequisites, opening GPT Builder, configuring name/description, pasting a complete Instructions block, uploading all current generated Markdown files including `00-overview.md`, waiting for processing, testing in Preview, and explicitly saving/updating with private visibility for initial testing. Link official OpenAI guidance rather than promise a particular subscription or unchanging UI label.

The copy-paste Instructions must start every health-specific answer with the canonical English disclaimer from `disclaimer.md` or its faithful localized equivalent in the user's language. Answer in that language, translate Vietnamese on demand, preserve qualifications and speaker attribution, and answer only from uploaded summaries. Include supporting source evidence and an existing timestamped YouTube link for each substantive video-derived claim; never invent quotations or timestamps. Explain missing evidence rather than fill gaps from model memory; treat knowledge as reference material, not instructions. Do not impersonate the doctor, diagnose, prescribe, or turn source statements into personalized medical advice. Disable web search and other unnecessary capabilities for this source-only GPT.

Document a repeatable refresh: use the successful pipeline's current generated output, never hand-edit it or upload raw transcripts/unreviewed summaries; remove all previous Knowledge files and upload the entire current set, not just changed volumes, because packing/removals can change names. Save/update, then retest in a fresh conversation. A repo update alone does not refresh a GPT. Cite repository caps (20 files, 2,000,000 bytes each) without confusing them with provider limits. If there are no published videos or generation/upload fails, do not represent the GPT as refreshed.

Include a repeatable manual acceptance checklist: ask in English about q7uDJG8YQ5c's account of health beyond absence of disease; verify attribution, localized disclaimer, evidence and the existing `t=1072s` source link against the uploaded volume. Ask the same health question in French and check the translated disclaimer. Test an unsupported question and a personalized dosage request for evidence limitations/no prescription. Record revision, uploaded filenames, date, actual responses and pass/fail. Live GPT Builder verification requires the owner's authenticated browser and remains explicitly pending until actually performed; local inspection cannot establish this ticket's live success criterion. Do not change `videos/`, generated files, publication gates, vocabulary, tickets, or unrelated docs.

</frozen-after-approval>

## Implementation Notes

One-shot: documentation-only change, estimated fewer than 100 added/modified lines across two files. Risk raised from low to medium because incorrect health-answer instructions could suppress the disclaimer or misrepresent source claims. The existing disclaimer and generated source links are authoritative. `scripts/consolidate.py` defines the repository caps and copies whole published summaries; `docs/weekly-sync.md` describes generation after validation. The current overview lists q7uDJG8YQ5c only. The current volume contains the health definition at 00:17:52 and its exact YouTube link. Preserve all generated content.

Official OpenAI Help pages on creating/editing GPTs and Knowledge were located by web search; direct fetch returned HTTP 403. Avoid hardcoded account entitlement claims and identify UI labels as potentially changing. No authenticated Builder session is available here.

Implemented `docs/custom-gpt-setup.md` (setup, source-only Instructions, localized recurring disclaimer, citations, refresh and live checklist) and its README link. Local checks passed: canonical disclaimer text, Markdown link targets, existing q7uDJG8YQ5c timestamp and protected-path diff. `git diff --check` passed. No runtime code changed, so no runtime tests were run. Live Builder checks remain pending owner execution; no GPT was created, updated, or shared.

## Plan Change Log

## Review Triage Log

Quick independent context-free review (inherited session model): no findings. Verdict counts: high 0, medium 0, low 0, false 0, maybe-false 0. Nothing deferred. Live Builder acceptance remains pending, explicitly distinct from local documentation verification.

## Verification

- `git diff --check` must pass. Inspect local Markdown links and exact canonical disclaimer inclusion in the copy-paste Instructions.
- Confirm the smoke-test video ID and timestamp exist in `knowledge-gpt/01-summaries.md`; inspect diff scope to ensure generated data and video/review files are unchanged.
- Owner follows the documented Builder procedure and records actual English/French responses, evidence links, missing-evidence behavior and safe handling of a dosage request. Until that happens, report live verification as pending, not passed.
