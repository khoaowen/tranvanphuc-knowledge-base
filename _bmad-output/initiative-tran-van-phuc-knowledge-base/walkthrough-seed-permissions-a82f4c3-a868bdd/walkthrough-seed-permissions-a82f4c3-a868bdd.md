# Human review: seed workflow read-only permissions

Target: commit `a868bdd1bf9cc8345a7eb7bb2872e2801923aca4` (parent `a82f4c31e625a27060c703b46e3d703e03b0a6ce`)

Status: all blocks accepted; awaiting wrap-up.

- [x] **1 — Intent — accepted**

  **Problem:** [`summarize-seed.yml`](../../../.github/workflows/summarize-seed.yml) had no top-level `permissions`, so its GITHUB_TOKEN inherited repository/org defaults. The secret-gate walkthrough left this as its one open finding.

  **Approach:** Declare `contents: read` and add a structural test for it. Trigger, Gemini key scope, scan-before-upload gate, artifact paths and full-SHA pins stay as they are. Verification is local and static only.

  Source: ticket [story-seed-workflow-explicit-read-only-permissions](../../backlog/story-seed-workflow-explicit-read-only-permissions.md), Description and Requirements.

- [x] **2 — Broad strokes — accepted**

  A three-line workflow change and one new test.

  1. [Workflow permissions block](../../../.github/workflows/summarize-seed.yml#L10) — top-level `contents: read`.
  2. [Permissions test](../../../tests/test_secret_scan_workflows.py#L84) — asserts the block, a single occurrence, and no `write` scope.

- [x] **3 — Unchanged behavior — accepted**

  The existing tests in [test_secret_scan_workflows.py](../../../tests/test_secret_scan_workflows.py) still cover the manual trigger, single Gemini key use, scan-before-upload order, artifact paths and SHA pins; they pass unmodified.

- [x] **4 — Periphery — accepted**

  - [Build plan](../../backlog/story-seed-workflow-explicit-read-only-permissions-plan.md) — status `built`, with the triage log.
  - [Ticket](../../backlog/story-seed-workflow-explicit-read-only-permissions.md) — source of the criteria.
