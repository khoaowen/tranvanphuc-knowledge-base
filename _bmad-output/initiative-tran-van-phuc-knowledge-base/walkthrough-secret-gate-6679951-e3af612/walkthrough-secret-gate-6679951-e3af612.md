# Human review: fail-closed pipeline secret gate

Target: commits `66799519e46ab8114deca90444fd634997370746..e3af612f825144e6995755ca20333f5f1c00ab14`

Status: review closed. All walkthrough blocks accepted; one finding deferred. No implementation files have been changed during this review.

- [x] **1 — Intent — accepted**

  **Problem:** The public pipeline has no secret-content gate; seed artifacts upload even after failures. Plugin hardening is deferred by owner choice.

  **Approach:** Use pinned, SHA-256-verified Gitleaks 8.30.1 to gate commits, pushes and seed uploads; add a hosted PR/push check. Deterministic means fixed rules, no LLM or credential-validity calls—not detection of every possible secret.

  Source: approved [plan](../plan-pipeline-secret-leak-prevention.md), Intent section.

- [x] **2 — Broad strokes — accepted**

  The change adds one shared scanner and connects it to each route that can persist or expose generated content. The local launcher performs a fail-closed preflight before its existing interactive flow; the weekly orchestrator scans the staged index before commit, then the final history/tree before pushing a bound commit ID. Hosted workflows run the shared scanner for PR/push review, scheduled publication, and seed-artifact upload.

  1. [Scanner entry points](../../../scripts/scan_secrets.py#L490) — implements index, commit/history, and artifact scan modes over a verified pinned Gitleaks binary.
  2. [Finalization and push binding](../../../scripts/weekly_sync.py#L479) — scans final Git state and pushes the explicitly scanned commit; [finalize](../../../scripts/weekly_sync.py#L545) adds the pre-commit index gate.
  3. [Local `./weekly-sync` command](../../../weekly-sync#L110) — retains the one-command interactive route while adding bootstrap/history preflight checks.
  4. [Hosted PR/push scan](../../../.github/workflows/secret-scan.yml#L12) — read-only full-history check using the same scanner.
  5. [Publication and artifact workflows](../../../.github/workflows/weekly-sync.yml#L47) and [seed upload gate](../../../.github/workflows/summarize-seed.yml#L36) — bootstrap before scheduled execution and scan both seed outputs before upload.

- [x] **3 — Local fail-closed scanning and immutable bindings — accepted**

  The index gate snapshots the prospective index to an immutable tree ID, scans that tree, then rejects an index that changed during the scan. The commit path checks that same scanned tree immediately before constructing the commit with `commit-tree`; the push path runs its hook first, resolves an immutable commit ID, scans its complete reachable history plus final tree, and pushes that hash explicitly rather than a moving `HEAD`.

  The scanner treats operational failures as blocked outcomes and scans file bytes through opaque names so Gitleaks path allowlists, repo ignore/baseline files, inline skips, and environment overrides do not certify content. Its sole historical exception is bound to three exact blob IDs and a synthetic-marker line, with remaining bytes scanned.

  - [Exact index snapshot and stability check](../../../scripts/scan_secrets.py#L490)
  - [Reachable-history and immutable-tree scan](../../../scripts/scan_secrets.py#L450)
  - [Allowlist staging, scan/target equality, and atomic ref update](../../../scripts/weekly_sync.py#L426)
  - [Post-hook final-commit scan and explicit-hash push](../../../scripts/weekly_sync.py#L479)
  - [Scanner seam and sanitized-failure conversion](../../../scripts/weekly_sync.py#L76) and [run wrapper](../../../scripts/weekly_sync.py#L409)

- [x] **4 — Publication and artifact-upload gates — accepted**

  The manual seed workflow runs the same scanner against both files named in its artifact upload: the generated summary and measurement log. The scan always runs—even if generation fails—but upload requires that scan step to succeed; a missing, non-regular, unreadable, binary, scanner-error, or finding result makes the scan fail and prevents the upload.

  The gate uses the artifact mode without `--allow-missing`, so both intended files must exist. The upload action is full-SHA pinned and its paths mirror the scan arguments.

  - [Artifact-mode fail-closed checks](../../../scripts/scan_secrets.py#L524)
  - [Seed scan and conditional upload](../../../.github/workflows/summarize-seed.yml#L32)
  - [Scheduled workflow scanner bootstrap](../../../.github/workflows/weekly-sync.yml#L47)

- [x] **5 — Hosted workflow hardening — accepted**

  The new hosted scan is a GitHub-hosted, read-only PR/push/manual check with no secrets, full history, and no persisted checkout credential. It bootstraps and invokes the same shared scanner used locally. The publishing workflow retains its required `contents: write` scope and limits the Gemini key to its summarize step; all actions touched in these workflows use complete commit-SHA pins.

  Review also covers whether every touched workflow declares only the permissions it needs, rather than inheriting repository defaults.

  - [Read-only hosted scan configuration](../../../.github/workflows/secret-scan.yml#L12)
  - [Publishing workflow permissions and secret scope](../../../.github/workflows/weekly-sync.yml#L16)
  - [Seed workflow configuration](../../../.github/workflows/summarize-seed.yml#L7)
  - [Workflow security tests](../../../tests/test_secret_scan_workflows.py)

- [x] **6 — Tests, documentation, and workflow preservation — accepted**

  Scanner outcomes retain only rule, safe path, and line; subprocess stdout/stderr and raw reports are captured rather than surfaced, while Gitleaks is invoked with redaction. Tests construct synthetic tokens at runtime and cover withheld values, scanner errors/timeouts, missing artifacts, index races, history findings, and Git binding behavior. The local-launcher test preserves the existing phase/key-scoping interaction while asserting scanner preflight occurs first and stops the flow before prompts or pipeline phases on failure.

  Security and local-run documentation describe supported platforms, fail-closed recovery, the narrow historical exception, incident response, and the unchanged single-command route.

  - [Result redaction and safe diagnostics](../../../scripts/scan_secrets.py#L83) and [scanner invocation](../../../scripts/scan_secrets.py#L360)
  - [Redaction and failure tests](../../../tests/test_scan_secrets.py#L280)
  - [`./weekly-sync` preflight preservation test](../../../tests/test_local_weekly_launcher.py)
  - [Security guide](../../../docs/security.md) and [local workflow guide](../../../docs/weekly-sync.md)

- [x] **7 — Periphery — accepted**

  - [Approved plan](../plan-pipeline-secret-leak-prevention.md) — records the reviewed historical-blob exception and verification boundaries.
  - [Deferred work](../deferred-work.md#L43) — leaves plugin hardening explicitly outside this security-gate change.
  - [Workflow security tests](../../../tests/test_secret_scan_workflows.py) — registers structural checks for permissions, SHA pins, secret scope, and upload ordering.
