---
title: 'Repo organization and consolidation'
type: 'feature'
ticket: '4'
created: '2026-10-29'
status: done
baseline_revision: 'c8aad7566bea8f9c1d208122c8c36246daed974d'
route: 'full'
route_source: 'auto'
risk: 'medium'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['self-inspection']
review_loop_iteration: 0
context:
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/repo-structure.md'
  - '{project-root}/_bmad-output/initiative-tran-van-phuc-knowledge-base/disclaimer.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Validated summaries are only reachable by path. There is no README index, no `topics/` pages, no `topics/vocabulary.md` (tags are free-form), and no `knowledge-gpt/` for the manual GPT upload.

**Approach:** Two stdlib generators read only videos the validator reports `published`: `generate_index.py` (README index block, `topics/<tag>.md`) and `consolidate.py` (`knowledge-gpt/*.md`). Seed `topics/vocabulary.md` from the published summary's tags with human approval, re-validate all summaries, and wire both generators into `weekly_sync.py finalize` after the validation gate.

**Decision (user, 2026-10-29):** vocabulary is seeded from published summaries only (today q7uDJG8YQ5c). Summaries failing tag validation afterwards are re-queued, not tag-rewritten.

## Boundaries & Constraints

**Always:** Output is deterministic and idempotent. Include only `published` videos (reuse `validate_summaries.validate_video`). Disclaimer banner (canonical text from `summarize.DISCLAIMER_BANNER`) on the README index and every consolidated file. Each `summary.md` is copied whole, never excerpted. `knowledge-gpt/` has at most 20 files, each at most `MAX_FILE_BYTES` (2,000,000, a constant); if packing cannot fit, exit non-zero and write nothing. Generated files carry a "generated, do not edit" marker; only marked files are ever removed.

**Never:** Write `videos/*` (transcript, summary, review). Hand-edit `knowledge-gpt/`. Commit or approve the vocabulary without the human's yes. Include transcripts, unvalidated or stale summaries. New third-party dependency. GPT setup docs (entry 5), refactors (entry 6).

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Published | q7uDJG8YQ5c published | README row (date, title, links to summary and transcript); `topics/<slug>.md` per tag; in `knowledge-gpt/` | — |
| Unpublished | summarized, pending, flag/fail review, stale | absent from README, topics, knowledge-gpt | — |
| No vocabulary | `topics/vocabulary.md` missing | topic pages built from tags found | — |
| Overflow | content needs more than 20 files or a file over cap | exit 1, nothing written | message names counts |
| Zero published | none published | README block says none yet; `knowledge-gpt/` holds only the overview | — |
| Rerun | unchanged inputs | no file changes | — |
| Tag outside vocabulary | summary fails validation | not published; listed for re-queue | human approves removing its `summary.md` |

</frozen-after-approval>

## Code Map

- `scripts/validate_summaries.py` -- `validate_video` gives `published`; `load_vocabulary` format (one tag per line, `#` comments, `norm` NFC lowercase). Reuse; do not change.
- `scripts/queue_state.py` -- `list_videos` (newest first). Reuse.
- `scripts/summarize.py` -- `DISCLAIMER_BANNER`; summary header fields (`- **Topics:**`, `- **Video ID:**`). Import, do not change.
- `scripts/weekly_sync.py` -- `phase_finalize` (after `validate_all` and `run_tests`), `build_allowlist`, `Deps` seams, report dict. Add a generation step and allowlist entries (`README.md`, `topics/`, `knowledge-gpt/`); keep `protected_changes`.
- `tests/test_weekly_sync.py`, `tests/test_validate_summaries.py` -- tempdir-fixture and fake-Deps patterns to copy.
- `README.md` -- hand-written; only the block between `<!-- index:start -->` and `<!-- index:end -->` is generated; also replace its stale "Status" text.
- `.github/workflows/weekly-sync.yml` -- finalize already runs the script; edit only comments if needed.
- `docs/weekly-sync.md` -- document the new step.
- Do not touch `videos/`, `review-*`, `summarize.py`.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/generate_index.py` -- published-only README block and `topics/<slug>.md` (slug = unaccented tag, `đ`→`d`) with links to summary and transcript
- [ ] `scripts/consolidate.py` -- `knowledge-gpt/00-overview.md` plus date-ordered packed volumes of whole summaries; caps; stale generated files removed
- [ ] `tests/test_generate_index.py`, `tests/test_consolidate.py` -- one case per matrix row, rerun idempotence, cap overflow, hand-written files untouched
- [ ] `scripts/weekly_sync.py` + `tests/test_weekly_sync.py` -- run both after validation and tests; add outputs to the allowlist; failure blocks generated files, not the video commit
- [ ] `topics/vocabulary.md` -- draft from published summaries' tags; show the human; write only after approval
- [ ] Re-validate every summary against the vocabulary; list failures; with approval `git rm` their `summary.md` (and `review.md`, `summary.stale`) so `review-batch` regenerates them
- [ ] `README.md`, `docs/weekly-sync.md` -- markers, index block, and doc updates

**Acceptance Criteria:**
- Given q7uDJG8YQ5c published and the other two unpublished, when both generators run, then README and a topic page link it in two clicks or fewer and neither other video appears anywhere generated.
- Given `knowledge-gpt/` generated, then it has at most 20 files, each under `MAX_FILE_BYTES`, and each carries the disclaimer.
- Given the approved vocabulary, when the validator runs over all summaries, then q7uDJG8YQ5c stays `published` and the failures are listed.
- Given a weekly run, when validation passes, then generated files are in the same allowlist-gated commit, and a validation failure commits none.

## Implementation Notes

## Plan Change Log

## Review Triage Log

No subagent was authorized; self-inspection of the diff found no open findings. Known, accepted: the two other summaries (so-137, so-135) fail the approved vocabulary and are listed for re-queue; per the user's choice they were not deleted.

## Design Notes

Packing is greedy by date, oldest first, so adding a new week only appends to the last volume or creates one. Generators take `--root`, `--videos-dir`, `--vocabulary` so tests need no git.

## Verification

**Commands:**
- `python3 -m unittest discover -s tests` -- expected: all pass
- `python3 scripts/generate_index.py && python3 scripts/consolidate.py && git status --short` -- expected: second run changes nothing
- `python3 scripts/validate_summaries.py --videos-dir videos` -- expected: q7uDJG8YQ5c `published`

**Manual checks:**
- Open `README.md`, follow a topic link, then the summary link: two clicks.
- Review the drafted vocabulary list before approving.
