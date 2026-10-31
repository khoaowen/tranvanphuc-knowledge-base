---
id: 1
type: story
title: "The seed workflow declares read-only GITHUB_TOKEN permissions"
parent: none
covers: []
after: []
assignee: ""
refined: true
hitl: false
risk: low
---

# The seed workflow declares read-only GITHUB_TOKEN permissions

## Description

`.github/workflows/summarize-seed.yml` sets no top-level `permissions`, so its GITHUB_TOKEN gets whatever the repository or organization default is. The workflow only checks out the repo and uploads an artifact, so it needs `contents: read` and nothing more. This closes the one finding the secret-gate walkthrough left open.

## Requirements

1. **The workflow declares least-privilege permissions**
   **Given** `summarize-seed.yml`
   **When** its top-level `permissions` are read
   **Then** they are exactly `contents: read`
   **And** no job in the file sets its own `permissions`, and no `write` scope appears anywhere in the file

2. **Structural tests assert the permissions**
   **Given** `tests/test_secret_scan_workflows.py`
   **When** the suite runs
   **Then** a test on `summarize-seed.yml` fails if the top-level `permissions` block is missing, is not exactly `contents: read`, or any `write` scope is present
   **And** that test fails when run against the current file, before the fix

3. **Everything else in the workflow is unchanged**
   **Given** the edited workflow
   **When** the existing workflow tests run
   **Then** all pass unmodified, proving: the only trigger is `workflow_dispatch`; `GEMINI_API_KEY` appears once, in the summarize step only; the scan runs after summarize and before upload; upload requires the scan step to succeed; artifact name and paths (`seed-summary`, `$SEED_DIR/summary.md`, `measurement.log`) are as before; every `uses:` is pinned to the same full 40-character SHA

4. **Verification touches nothing live**
   **Given** the build is verified
   **When** it is checked
   **Then** only local static tests ran: no workflow run was triggered, nothing was pushed or uploaded, and no GitHub setting changed

Verify: run `python -m unittest tests.test_secret_scan_workflows` locally; review the diff, which touches only `summarize-seed.yml` and that test file.

## Boundaries

- Must not change: the manual-only trigger, the Gemini key scope, the scan-before-upload gate, artifact paths, and the full-SHA action pins.
- Out of scope: `weekly-sync.yml` and `secret-scan.yml` (they already declare permissions), repository or organization default token settings, plugin hardening.

## References

- walkthrough — `_bmad-output/initiative-tran-van-phuc-knowledge-base/walkthrough-secret-gate-6679951-e3af612/walkthrough-secret-gate-6679951-e3af612.md`, block 5 and the log's closing entry (deferred finding: add explicit least-privilege `permissions` to `summarize-seed.yml`)
- walkthrough log — `_bmad-output/initiative-tran-van-phuc-knowledge-base/walkthrough-secret-gate-6679951-e3af612/walkthrough-secret-gate-6679951-e3af612-log.md`
- plan — `_bmad-output/initiative-tran-van-phuc-knowledge-base/plan-pipeline-secret-leak-prevention.md`
- tests — `tests/test_secret_scan_workflows.py`

## Notes

- Source: finding from the closed secret-gate walkthrough (commits 6679951..e3af612): `summarize-seed.yml` has no explicit top-level permissions, so its token scope inherits repository/organization defaults.
- Decision: 2026-10-30 owner approved the ticket, including `contents: read` as sufficient (only checkout and upload-artifact are used; no live run allowed to prove it).
- Decision: 2026-10-30 risk is low (manual-only workflow, one secret, one-block change).
