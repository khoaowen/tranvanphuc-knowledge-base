---
title: Recover locally prepared weekly artifacts without refetching
created: '2026-10-29'
type: bugfix
ticket: ''
status: built
baseline_revision: '8b6cb8cdef31047671946aa31fa9dcc55a026123'
route: full
route_source: auto
risk: medium
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** The owner's successful local prepare produced one fetched video and 135 metadata-only pending folders, but report.json and before.sha were stored in macOS temporary storage and disappeared. The launcher correctly refuses to start fresh against those untracked files. The owner wants a single command, not repeated manual repair steps.

**Approach:** Add explicit ./weekly-sync --recover to validate and adopt only complete, entirely untracked prepared artifacts. Reconstruct a clearly labelled recovery report in durable outside-repository storage, then resume summarize/finalize through the existing launcher. Show the recovered selected ID/count and require owner confirmation before adoption; retain the existing confirmation before commit/push. No report means historical log/status evidence is unavailable, not magically successful.

## Boundaries & Constraints

**Always:** Recovery is explicit and mutually exclusive with --resume. With --recover, ignore a stale WEEKLY_RUN pointing to the missing temporary report. Refuse staged or modified tracked work, unrelated untracked files, symlinks, malformed metadata, duplicate IDs (including IDs already in tracked corpus), partial fetches, multiple fetched videos, and existing summary/review/stale artifacts. Require exactly one fully fetched new video and every other new folder to contain metadata.json only. Validate IDs, core fields, date, positive duration, canonical metadata path and YouTube identity; bind provenance video ID/source/track to metadata. Verify compressed-caption checksum, nonempty parsed captions, exact transcript rendering and transcript checksum using existing read-only helpers. Save recovery timestamp, actual current full HEAD/branch, inventory digests, selected/pending IDs and explicit lost-evidence caveats. Use current recovery HEAD as a labelled replacement baseline, not a claim to have recovered the original before.sha. Stop at any failure; never continue into summarize/finalize after a failed inspection or declined confirmation.

**Never:** Fetch metadata/captions, re-detect channel order, call Gemini, write videos/, stage/commit/push, alter Git history/config, or mutate existing evidence during recovery itself. No synthetic success of the original run; original logs and channel order remain unavailable. No main/master or detached execution, no GitHub runner, no production YAML changes, no story acceptance or ticket edits. Leave existing untracked kanban.html on this agent's checkout untouched and excluded from implementation commits.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|---|---|---|---|
| Valid prepared inventory | One new complete fetch, rest metadata-only | Display inventory; after approval save durable recovered state and skip prepare | Existing launcher handles later phases |
| Missing original report | --recover plus stale WEEKLY_RUN | Ignore stale path; inspect actual artifacts | Caveat lost original evidence explicitly |
| Broken integrity | Caption/transcript checksum mismatch, malformed/empty captions, identity mismatch | No recovered report, no corpus mutation or later phase | Clear failure and nonzero exit |
| Unsafe inventory | Tracked/staged changes, unrelated files, duplicates, extra artifacts or ambiguous fetches | Refuse adoption | Clear failure and nonzero exit |
| Owner declines | Valid inspection but no adoption confirmation | No recovered report or later phase | Stop cleanly |
| Later terminal restart | Valid recovered durable report | Existing --resume works, with no prepare or repeated summary | Do not require temporary path |

</frozen-after-approval>

## Code Map

- `weekly-sync` — stdlib launcher: resolve args after bootstrap; currently reads resume before dirty gate. Add recover integration without weakening ordinary resume/fresh guards; keep key restricted to summarize.
- `scripts/weekly_sync.py` — reuse `new_state`, state version/fields and `save_state` format as applicable; do not change phase behavior.
- `scripts/fetch_transcript.py` — reuse `load_raw_captions`, `check_transcript`, `build_transcript_lines`, `render_transcript`, `metadata_json_for`/slug semantics; these validation APIs do not download. Do not call fetch/rerender/write APIs.
- `scripts/recover_weekly.py` (new) — read-only inventory/validation and recovery-report persistence separated so declining confirmation writes no evidence. Use NUL-delimited Git paths and canonical containment checks.
- `tests/test_local_weekly_launcher.py`, `tests/test_recover_weekly.py` (new) — hermetic integration/unit fixtures; no live network, secrets or push.
- `docs/weekly-sync.md` — document one-command recovery, durable evidence location and original-evidence limitations.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/recover_weekly.py` — inspect untracked prepared inventory and validate artifacts; save labelled durable state only after approval.
- [ ] `weekly-sync` — add --recover and adoption prompt, reuse the validated state for existing resume path and finalize confirmation.
- [ ] `tests/test_recover_weekly.py`, `tests/test_local_weekly_launcher.py` — prove accepted and rejected states plus no network/corpus writes, no prepare on recovery and correct key scoping.
- [ ] `docs/weekly-sync.md` — explain recovery and distinguish replacement baseline/verified artifacts from missing original run evidence.

**Acceptance Criteria:**
- Given the owner's valid prepared inventory and no report, when --recover is confirmed, then a durable labelled report records the one selected ID and 135 pending items (count derived, not hardcoded) and no prepare is invoked.
- Given any rejected inventory or declined adoption, when recovery runs, then no report or corpus mutation occurs and summarize/finalize do not run.
- Given a recovered report, when the launcher continues, then only the selected video is summarized and final commit/push still requires owner confirmation.
- Given a later explicit resume of recovered evidence, when the launcher runs, then no known-video fetch or already-successful summary generation is repeated.

## Implementation Notes

Owner approved the plan and chose to stop before implementation on 2026-10-29. No recovery code, commit or push has been made.

Owner approved explicit recovery after observing 136 untracked metadata files and only the selected video's transcript, raw captions and provenance; no tracked changes. The original report pasted in conversation had selected s2cOsPTA_Ek and no notices/failures/fatal. Code must independently validate artifacts, not assume that historical result proves current file integrity. This is >100 changed code lines including tests, so full route.

## Plan Change Log

## Review Triage Log

| # | Lens | Finding | Verdict | Route | Evidence |
|---|---|---|---|---|---|
| 1 | quick | Ignored `.DS_Store` tolerated in pending folders | medium | patch | Orchestrator-added tolerance broke `fetch_transcript.py:354` metadata-only invariant for later `--complete-pending`; reverted to strict refusal (plan-conformant), owner command deletes Finder files first. |
| 2 | quick | NaN/Infinity duration passes positive check | low | patch | `json.loads` accepts NaN; `nan <= 0` is False; added `math.isfinite` plus tests. |
| 3 | quick | `unseen` fabricated from folder order | medium | patch | `weekly_sync.py:195` defines it as channel detection order, which is lost; now `[]` and asserted in test. |
| 4 | quick | Docs say pending order by published date; code sorts by dir name | low | patch | Docs corrected to "directory name (published date, then slug), newest first". |

## Verification

Run `python3 -m unittest discover -s tests`, `python3 scripts/validate_summaries.py`, launcher --help and `git diff --check`. Unit tests use real temporary Git repositories and real caption/provenance fixtures where possible; launcher tests mock network/process boundaries. Assert byte-identical videos/ before/after read-only inspection and after failures. Independent review before commit. No live local fetch/Gemini/data push from this server.
