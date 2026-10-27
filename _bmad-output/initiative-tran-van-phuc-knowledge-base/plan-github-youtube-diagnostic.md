---
title: GitHub-hosted YouTube caption diagnostic
type: chore
ticket: ''
created: '2026-10-27'
status: built
baseline_revision: '3286e98e4eb07af1733eb6d62419c3626464df9b'
route: oneshot
route_source: auto
risk: low
review: quick
review_source: pinned
lenses_ran: [quick]
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

Determine whether an Ubuntu GitHub-hosted runner can list the channel and retrieve real Vietnamese captions for its newest unseen video. Add a separate diagnostic workflow, push it on the current branch to trigger the probe, and report the observed result. Owner explicitly approved a push trigger restricted to khoaowen/Epic2-publish-videos and changes to this diagnostic YAML, because a new manual workflow cannot be bootstrapped off main. Use the existing detector and caption-fetch/parser functions and pinned dependency. Write downloaded captions only to a temporary directory. No Gemini key, cookies, corpus mutation, commits or pushes from the diagnostic job. Do not change the production workflow or cancel its queued run. Leave the pre-existing untracked kanban.html untouched. If no unseen video exists, report a no-test result without fetching a known video. A failed retrieval is diagnostic evidence, not permission to repair the production pipeline or mark story 1.11 accepted.

</frozen-after-approval>

## Implementation Notes

One-shot because this is a single small diagnostic workflow, under 100 lines. Existing functions get_channel_video_ids/get_known_video_ids and fetch_caption_json3/build_transcript_lines provide equivalent detection and caption retrieval without writing videos/. The workflow has contents: read, a branch/path-scoped push trigger plus manual dispatch, and a bounded timeout. User authorized the diagnostic and excluding kanban.html.

## Plan Change Log

## Review Triage Log

- High / HALT: manual dispatch cannot bootstrap a brand-new workflow present only on a feature branch. Verified the file is absent from main (GitHub API 404) and GitHub documentation requires default-branch registration. Need owner approval for a branch-scoped push trigger or default-branch registration. No commit, push or dispatch made at this checkpoint. Owner subsequently approved the branch/path-scoped push trigger; amended workflow and re-review before push.

- Re-review after authorized trigger amendment: no findings. YAML parsed and embedded Python compiled; trigger scope and read-only permissions asserted successfully.

## Verification

Parse YAML and compile embedded Python before commit. Independently inspect permissions, temp-directory usage, no known-video fetch, and no production-workflow edits. Push the diagnostic on khoaowen/Epic2-publish-videos, watch its triggered run, and inspect logs with context-mode. Caption success requires parsed non-empty transcript lines. No unseen video must be explicitly reported as not tested, not caption success.
