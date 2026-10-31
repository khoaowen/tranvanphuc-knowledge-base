---
title: 'Seed workflow declares read-only GITHUB_TOKEN permissions'
type: 'bugfix'
ticket: 'story-seed-workflow-explicit-read-only-permissions'
created: '2026-10-31'
status: done
baseline_revision: 'a82f4c31e625a27060c703b46e3d703e03b0a6ce'
route: 'oneshot'
route_source: 'auto'
risk: 'low'
review: 'quick'
review_source: 'pinned'
lenses_ran: [quick-inline]
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** `.github/workflows/summarize-seed.yml` has no top-level `permissions`, so its GITHUB_TOKEN inherits repo/org defaults (walkthrough secret-gate finding).

**Approach:** Add top-level `permissions: contents: read` and a structural test asserting exactly that. Keep trigger, Gemini key scope, scan-before-upload gate, artifact paths and full-SHA pins unchanged. Verify with local static tests only: no live runs, pushes, uploads or GitHub-setting changes.

</frozen-after-approval>

## Implementation Notes

Oneshot: one workflow block plus one test; ticket criteria are the spec.

Changed: `.github/workflows/summarize-seed.yml` (top-level `permissions: contents: read`), `tests/test_secret_scan_workflows.py` (`test_permissions_are_explicit_and_read_only`). The new test fails on the old workflow and passes on the new one; all other workflow tests pass unmodified.

## Review Triage Log

Quick lens run inline by the builder (no subagent launched; delegation was not authorized). Diff inspected against the ticket criteria: no findings. Trigger, key scope, scan/upload gate, artifact paths and SHA pins are untouched by the diff.
