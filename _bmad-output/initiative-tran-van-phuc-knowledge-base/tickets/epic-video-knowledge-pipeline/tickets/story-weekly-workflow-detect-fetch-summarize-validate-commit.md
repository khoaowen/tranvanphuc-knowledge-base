---
id: 11
type: story
title: "Weekly workflow: detect, fetch, summarize, validate, commit"
parent: epic-video-knowledge-pipeline
covers: [R1, R2, R3]
after: [1, 2, 8, 10, 13]
refined: true
hitl: true
risk: medium
---

# Weekly workflow: detect, fetch, summarize, validate, commit

## Description

Complete the weekly automation for R1–3 using the shipped detector, provenance-preserving fetcher, Gemini summarizer, and validator. Commit useful, valid results without confusing a committed summary with a published one; leave backlog fetching and fidelity review local. The owner inspects one real-channel manual run and its commit/logs before accepting the story.

## Requirements

1. **One weekly entry point** (R1–3)
   **Given** the existing scheduled and manually dispatched weekly workflow,
   **When** either trigger runs,
   **Then** it performs detection, selection/queuing, selected-video fetch and summarization, branch-wide validation, tests, selective commit, and safe push in that order where applicable.
   **And** the Sunday 03:00 UTC schedule and manual dispatch remain available; overlapping weekly runs on the same branch are serialized without cancelling a run mid-write. No second production workflow is created.

2. **Select before queuing** (R1, R2)
   **Given** the channel's newest-first upload list and the video IDs in existing metadata,
   **When** unseen IDs are detected,
   **Then** exactly the first distinct unseen ID is selected before any new metadata directories are created. Known IDs are compared by metadata video ID, not slug; repeated IDs do not create duplicate work.
   **And** the remaining unseen IDs get core metadata only and derive `pending`; CI makes no caption-fetch or Gemini calls for them. Metadata-only requests needed to queue them are allowed. Existing directories/artifacts are not overwritten, duplicated, or re-fetched. An ambiguous ID/destination or unusable metadata stops that item's writes with a visible diagnostic, not a guessed destination.

3. **No new video and captions not ready** (R1–3)
   **Given** either no unseen ID or a selected upload without available Vietnamese captions,
   **When** the run processes that selection,
   **Then** no unseen ID means no fetch or Gemini calls, but tests and branch-wide validation still run; an empty diff means no commit or push.
   **And** unavailable captions leave the selected ID metadata-only `pending`, with a visible retry/local-processing notice and no partial transcript/raw/summary. CI does not fall back to an older ID or retry the backlog. After this pending metadata is committed, later CI runs regard the ID as known; entry 9 fetches it locally when captions are ready. Other fetch/detection errors are reported as failures, never as a successful empty detection; only independently safe queue/fetch artifacts may survive a per-video error.

4. **Fetch preserves provenance and source bytes** (R2)
   **Given** a selected unseen video with available captions,
   **When** its fetch succeeds,
   **Then** its core metadata, transcript, exact compressed raw caption bytes, and provenance are committed together as a complete fetch result under the shipped raw-caption contract. An incomplete fetch result is not staged.
   **And** every pre-existing transcript and raw/provenance artifact remains byte-identical. Validation and summarization never re-render, correct, or edit them. This is not legacy backfill.

5. **Read per-video validity, not aggregate success** (R3)
   **Given** any summaries on the branch, including local entry-9 pushes,
   **When** validation runs,
   **Then** all are checked and their structured per-video results determine the allowlist: `invalid`, `review_missing`, `published`, `state`, and diagnostic reasons. Use the shipped validator's per-video API; do not infer validity/publication from the CLI exit alone or parse its human-readable text.
   **And** newly generated invalid summary bytes are never committed. Valid summaries can be committed with `published = false`; missing, flagged, failed, malformed, or hash-mismatched reviews do not promote them. Only a valid, non-stale summary with a current hash-bound passing review has `published = true`. No publication flag is persisted as a substitute for the file-derived gate; the published set is the handoff for entry 4.

6. **Validator exit policy and selective commit** (R2, R3)
   **Given** aggregate validation results,
   **When** the validator returns,
   **Then** exit 0 allows staging safe artifacts, even if zero videos are published; it is not a publication approval. Exit 1 records a failed run with per-video reasons but still permits an independently valid result, complete fetch result, pending metadata, or stale marker to be committed after tests pass. Existing invalid summaries already on the branch remain untouched and excluded, not deleted or re-committed as new output.
   **And** exit 2 (transcript changed) aborts the whole write path: no workflow commit or push, including otherwise safe results or markers. Unexpected validator errors, missing/undecodable results, and unexplained transcript changes fail closed the same way. Exit-1 or generation/fetch failures remain visible in the final job status even when safe progress was pushed; they cannot be swallowed by a later successful command.
   **And** staging is an explicit allowlist of this run's complete, safe changes, never a blanket add of the working tree. Temporary drafts, logs, secrets, invalid candidates, and unrelated files are excluded.

7. **Failed regeneration preserves and disqualifies the prior summary** (R3)
   **Given** a summary exists before an attempted regeneration,
   **When** generation fails (including exhausted retries/quota, timeout, malformed output, or Reduce guard rejection), or its replacement fails validation,
   **Then** the prior summary is retained/restored byte-for-byte and `validate_summaries.py --mark-stale <video_id>` is called against those retained bytes, before deriving final eligibility and staging safe artifacts. A failure after replacement must not mark the rejected replacement's hash instead.
   **And** the resulting marker is committed if the other write gates permit it; the old review remains untouched but cannot publish that stale summary. Repeated attempts cannot clear staleness by merely re-running validation/review or rewriting identical summary bytes. Only changed summary bytes can escape that marker, and they still need validation and a current passing review to publish. Failure to restore or mark the unique prior summary stops commit/push.
   **And** with no prior summary, failed generation leaves only the complete fetch result (`transcribed`); there is no stale-marker call and no invalid summary committed. CI's normal newest-unseen selection does not add regeneration of known videos; the failure-handling path is tested explicitly for future/reused orchestration.

8. **Unittest gates every automated commit** (R1–3)
   **Given** any run, including one with no new video or only safe partial progress,
   **When** it reaches the write gate,
   **Then** `python -m unittest discover -s tests -v` must pass before any commit/push. A failing test blocks all workflow commits, including metadata and stale markers. Tests run without Gemini credentials, subscription login, or live LLM calls.
   **And** transcript byte-preservation is still checked independently of the deferred corpus-wide provenance check. The workflow does not run the all-video `fetch_transcript.py --check` gate in this story, skip legacy failures to claim success, or fetch old videos to make it pass.

9. **Transient Gemini failures are bounded** (R3)
   **Given** a map or Reduce request receives HTTP 5xx, a timeout, or a connection error,
   **When** retrying,
   **Then** retry that request only, keeping completed map results in the current process, with the shipped exponential backoff and jitter and at most five retries per call per transient-error budget. Preserve the existing separate 429 budget, Retry-After handling, and immediate daily-quota stop with reset hint; do not retry the entire video/job automatically.
   **And** exhausted retries take criterion 7's safe failure path. Tests prove eventual recovery and exhaustion for both map and Reduce without live requests or sleeping. This preserves existing retry behavior; durable map checkpoints across separate runs are not required.

10. **Bound the complete Reduce prompt** (R3)
    **Given** all map outputs and optional vocabulary,
    **When** building the complete Reduce request including instructions and wrappers,
    **Then** a configurable positive character ceiling is checked before the Reduce API call; use 60,000 characters by default, the same conservative input-size scale as the shipped map chunks. At or below the ceiling the call is allowed; above it, no Reduce request is made and generation fails with counts and a safe diagnostic, taking criterion 7's path.
    **And** invalid/nonpositive configuration fails before model calls. Tests cover exact boundary, one character over, vocabulary/wrapper overhead, and preservation/staleness of a prior summary. No truncation, silent omission of map outputs, or automatic hierarchical Reduce is allowed. The ceiling is an operational guard, not a claim that characters equal tokens or that every model accepts it; API context-limit rejection remains a safe generation failure.

11. **Rebase without losing local pushes** (R1–3)
    **Given** safe changes and passing tests,
    **When** committing and pushing to the checked-out target branch,
    **Then** fetch and rebase the workflow commit onto that branch's latest remote head immediately before a normal non-force push. A non-conflicting entry-9/12 local push is retained. After successful rebase, rerun tests and all-summary validation against the exact combined tree and recompute per-video eligibility; do not reuse pre-rebase hashes/publication decisions.
    **And** if merged changes invalidate this run's candidate artifacts or a hard gate fails, do not push. An unrelated pre-existing invalid summary follows criterion 6's exit-1 policy. A rebase conflict is aborted, fails the job, identifies the branch/conflicted paths, and requests human reconciliation/rerun; no ours/theirs choice, force push, overwrite, or regeneration to resolve it. A further non-fast-forward rejection also fails visibly with no force or unbounded retry; rerun from the latest branch. No remote change is made by a failed push.

12. **Secrets and authentication** (R3)
    **Given** the free-tier Gemini key and configured model,
    **When** CI invokes summarization or handles any success/error/retry,
    **Then** only that step receives `GEMINI_API_KEY` through its secret environment and `GEMINI_MODEL` through configuration. The key never appears in logs, command arguments, job outputs, artifacts, committed files, or exception text. No environment dumps or shell tracing expose it. Test errors containing a sentinel key, including retries and API error bodies, prove redaction.
    **And** CI never runs `claude -p`, a subscription login, or the local fidelity reviewer. Repository writes use the workflow token with only the permissions needed to push; no paid API or subscription credentials are introduced. Missing Gemini configuration fails the selected-video generation path safely; it does not prevent no-new-video tests/validation.

13. **Observable acceptance evidence** (R1–3)
    **Given** the completed workflow integration,
    **When** verifying it,
    **Then** deterministic offline fixtures cover newest-first/duplicate/known-ID selection, no-new-video, captions unavailable, backlog exclusion, all validator exits, valid-unreviewed versus published, invalid candidate isolation, failed regeneration, unittest failure, retries, Reduce bounds, secret redaction, and both non-conflicting and conflicting/rejected push races. Temporary Git repositories prove safe staging and preservation of local pushes; nothing writes to the real remote during tests.
    **And** the owner manually dispatches the weekly workflow against the real channel and inspects its selected ID, pending backlog, validation/eligibility report, final status, and committed file list/logs for leaks and unintended changes. If no unseen video exists, accept the live no-op plus offline new-video evidence rather than re-fetching a known video to manufacture a live success. Record the run URL, commit SHA or no-diff result, and owner's acceptance in the build evidence.

## Boundaries

- Must not change: the shipped summary contract, file-derived queue states, hash-bound local review gate, existing transcript/raw bytes, and entry 9's local backlog-fetch ownership.
- Must not change: the manual seed-measurement workflow or its behavior. No seed-specific production branch is added.
- Out of scope: local Claude review automation in CI, legacy raw-caption backfill and corpus-wide raw `--check` wiring, README/topic/GPT consolidation (entry 4), GPT upload, automatic rebase conflict resolution, hierarchical Reduce, durable map caches, and a new provider output-token cap. Local workflow regression fixtures belong here; entry 7 still owns the full epic end-to-end suite.

## References

- parent — _bmad-output/initiative-tran-van-phuc-knowledge-base/tickets/epic-video-knowledge-pipeline/epic-video-knowledge-pipeline.md, Requirements and Notes
- contract — _bmad-output/initiative-tran-van-phuc-knowledge-base/summary-contract.md, Required structure and CI validation
- deferrals — _bmad-output/initiative-tran-van-phuc-knowledge-base/deferred-work.md, Gemini retries/Reduce and CI checks
- measurement — docs/summarizer-limits.md, Limits and Behavior notes
- provenance — docs/raw-captions.md, Re-render and check and Not yet backfilled

## Notes

- Owner acceptance (2026-10-29) — accepted the local weekly flow in place of criterion 13's live GitHub `workflow_dispatch` requirement. The owner recovered the already-prepared inventory locally with `./weekly-sync --recover`: selected `s2cOsPTA_Ek`, 135 pending; recovery integrity checks, test preflight and summary validation passed; Gemini summarized only the selected video; owner confirmed the final commit/push prompt and reported "pushed." The pushed branch head observed after that report is `4b29fbf7722e98489d77a658ac9916488696c707`. Recovery caveats were shown and accepted: original prepare evidence and channel order were unavailable. This is acceptance of the agreed local-flow alternative, not evidence of a live GitHub Actions dispatch.
- Decision (2026-10-24) — settled now: refine 1.11 and commit its planning artifacts only; do not start the build. Keep identity, prerequisites, hitl and medium risk (incorrect gating could expose unreviewed health summaries); the person-step is the owner's live-run inspection. Entries 1, 2, 8, 9, 10, 12 and 13 are done; 1.11 is unassigned and not started. Entries 4–7 remain downstream.
- Decision (2026-10-24) — settled now, exit codes and state: use structured `validate_video` results from the validator, not CLI text or exit 0 as a published flag. Exit 0 permits safe commits even with no published videos; exit 1 permits selective safe progress but ends red; exit 2/unexpected validator failure blocks all commits/pushes. Unreviewed valid summaries are committed as summarized/unpublished; only the file-derived validated current pass publishes (criteria 5–6).
- Decision (2026-10-24) — settled now, failed regeneration: preserve/restore the pre-attempt summary and call `--mark-stale` after any failed generation or invalid replacement, binding the marker to the retained hash. No prior summary means no marker. Unchanged bytes remain ineligible even with a previous pass (criterion 7).
- Decision (2026-10-24) — settled now, CI tests: unittest gates every automated commit in 11, independently of raw-caption backfill. The deferred-work entries bundling the two checks are separated by this decision (criterion 8).
- Decision (2026-10-24) — settled now, raw check stays deferred: do not wire the corpus-wide `fetch_transcript.py --check` in 11; the two legacy videos lack raw captions and would fail it. First deliver an approved legacy backfill, then wire that gate as follow-up. No backfill is authorized here; transcript immutability and fresh-fetch provenance remain required.
- Decision (2026-10-24) — settled now, backlog selection: select the newest distinct unseen ID before queuing any IDs; fetch captions and Gemini-summarize that one only. Queue all other unseen IDs as metadata-only pending, not transcribed. No-new-video still runs gates. Captions-not-ready leaves the selected ID pending, without fallback; subsequent completion is local entry 9 because committed metadata makes it known (criteria 2–3). This removes the pulled entry's contradictory phrase that backlog is queued as transcribed and settles the epic's detect/fetch queuing unknown for this story.
- Decision (2026-10-24) — settled now, push races: serialize weekly writers, rebase before non-force push, and repeat gates on the combined tree. Abort conflicting rebase and fail with human reconciliation/rerun instructions; a later rejected push also fails without force or automatic conflict resolution (criterion 11).
- Decision (2026-10-24) — settled now, existing workflows: extend `.github/workflows/weekly-sync.yml`; leave `.github/workflows/summarize-seed.yml` unchanged as the manual measurement tool. Its old comment about absorption does not authorize deleting or editing it.
- Decision (2026-10-24) — settled now, secrets: step-scoped environment key, safe diagnostics/redaction on every path, no subscription login or local Claude execution in CI (criterion 12).
- Decision (2026-10-24) — settled now, Gemini 5xx/timeouts are in 11 as regression acceptance, not a second retry implementation. The deferred note is superseded by shipped `TransientError` handling and the seed measurement's recovered 503s; preserve/test bounded request-level retries and exhaustion (criterion 9).
- Decision (2026-10-24) — settled now, Reduce guard is in 11: enforce the complete-prompt character bound with a 60,000-character configurable default and fail closed without truncation. Hierarchical Reduce and `maxOutputTokens` remain deferred; they are not needed to establish this safe input guard (criterion 10).
- Decision (2026-10-24) — left to the story: orchestration/helper layout, safe temporary candidate storage, report transport into workflow steps, and fixture layout are implementation choices constrained by these criteria. No spike is required for the listed decisions; do not reinterpret those choices as permission to change selection, gates, or scope.
- Decision (2026-10-24) — settled now, R3 contract: 11 consumes the shipped summary-contract and validator/review semantics unchanged; it does not re-author the summary schema. See the epic Notes' 2026-10-24 R3 resolution immediately after its historical Source conflict; the richer retrieval/fidelity requirements are retained.
- Decision (2026-10-24) — settled now, refinement validation: the independent Ticket check found the criteria executable and the prerequisite/order checks clear; its one documentation fix was to put the existing R3 resolution in the owning epic and reference it here. Applied without changing scope. No build has started.
