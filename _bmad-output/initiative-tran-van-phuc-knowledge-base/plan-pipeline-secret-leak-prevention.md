---
title: 'Fail-closed pipeline secret-leak prevention'
type: 'feature'
ticket: ''
created: '2026-10-30'
status: 'built'
baseline_revision: '66799519e46ab8114deca90444fd634997370746'
route: 'full'
route_source: 'auto'
risk: 'high'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** The public pipeline has no secret-content gate; seed artifacts upload even after failures. Plugin hardening is deferred by owner choice.

**Approach:** Use pinned, SHA-256-verified Gitleaks 8.30.1 to gate commits, pushes and seed uploads; add a hosted PR/push check. Deterministic means fixed rules, no LLM or credential-validity calls—not detection of every possible secret.

## Boundaries & Constraints

**Always:** Preserve the single `./weekly-sync` Mac command and existing confirmations, validation, tests, protected artifacts, rebase handling and no-force policy. Bootstrap the pinned scanner into an external cache on supported macOS/Linux architectures, verifying artifact integrity; unsupported platforms, download/hash/version/scan errors block publication. CI and local paths use the same implementation. Scan the exact prospective index after generation and staging, and reachable HEAD history plus the final tracked snapshot immediately before every push, including new remote branches and rebases. Removed intermediate-commit secrets must block. Bind scans to immutable tree/commit IDs; verify the index stayed unchanged before commit and push the scanned commit ID, not a moving HEAD.

Scan seed summary and measurement log before artifact upload. Disable inline skip directives, repository ignore/baseline overrides and environment config overrides; use the pinned default rules without broad exclusions, including tests and generated content. No size/binary/encoding/path error may silently certify unexamined intended text as clean. Keep scanner subprocess output captured/redacted and never publish matched values, snippets or raw scan reports; store only sanitized outcomes. Scanner findings or inability to scan must prevent the affected commit/push/upload, with nonzero status. Retain local evidence, never auto-delete a finding, rotate keys or rewrite history. **Owner-approved exception (2026-10-30):** the three identified historical blobs containing the malformed, synthetic test sentinel may be excluded by exact blob ID and marker line only; this must be documented and tested, must scan all other bytes of those blobs, and must not match new content. No other baseline or finding-hiding mechanism is allowed.

**Never:** Modify videos/reviews, publication eligibility or plugin behavior; claim a clean scan proves absence of all secrets, medical safety or prompt-injection safety. No repository setting changes, paid scanner/action dependency, production workflow dispatch, pushes or public uploads during verification. Manual Git operations remain outside the pipeline gate; document native push protection and required-check administration separately. Existing public exposure requires revocation/rotation, not merely deleting a file.

## I/O & Edge-Case Matrix

| State | Required result |
| --- | --- |
| Clean candidate | Existing pipeline behavior preserved |
| Recognizable synthetic token in metadata/raw/summary/generated/index content | Block before automated commit; no push |
| Secret in an outgoing intermediate commit but absent at HEAD | Block push |
| Secret introduced by rebase or before-push hook | Rescan final state; block push |
| Scanner missing, corrupt, wrong version, timeout or error | Fail closed, sanitized diagnostic |
| Seed summary/log contains token, or scan step fails | No artifact upload |
| GitHub PR from fork | Hosted read-only scan, no secrets, no self-hosted runner |

</frozen-after-approval>

## Code Map

- `scripts/weekly_sync.py`: `Deps` seams; `phase_finalize` generates before `commit_allowlist`; insert index gate there. `sync_and_push` must gate after `before_push` on every path, not only after rebase. Reuse exit-2 blocked/report semantics; check Git inspection return codes.
- `weekly-sync`: cached venv and preflight runner; retain hidden key handling and one-command workflow.
- `.github/workflows/weekly-sync.yml`: full checkout, secret only in summarize, finalize runs after earlier failures; scanner failure must remain blocking there.
- `.github/workflows/summarize-seed.yml`: unconditional artifact upload is a separate exposure path; require successful output scan.
- `tests/test_weekly_sync.py`: temporary bare remote, fake Deps and before-sync/push hooks cover races without external services.
- No existing scanner/config. GitHub API inspection: public repo, secret scanning and push protection enabled, no rulesets. These settings do not guarantee required PR checks.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/scan_secrets.py` — implement verified pinned bootstrap, index/tree/history/artifact scan modes, fixed rules and sanitized fail-closed results. Verify release checksums from upstream before embedding; support macOS arm64/x64 and Linux x64/arm64.
- [ ] `scripts/weekly_sync.py`, `weekly-sync` — integrate preflight/index/final-push gates using injectable scanner seams; fail safely without overriding existing protections.
- [ ] `.github/workflows/secret-scan.yml` — PR/push/manual hosted check with full history, contents-read permission, no secrets and pinned dependencies; no workflow-run or pull-request-target escalation. Treat changes to the gate itself as security-sensitive, not self-proving.
- [ ] `.github/workflows/weekly-sync.yml`, `.github/workflows/summarize-seed.yml` — install/use the shared gate and condition artifact uploads on successful scans; pin actions touched here to verified full commit SHAs.
- [ ] `tests/test_scan_secrets.py`, `tests/test_weekly_sync.py`, `tests/test_secret_scan_workflows.py` — test every matrix case, bootstrap integrity, override/inline-ignore resistance and redaction. Construct fake tokens at runtime, never introduce live credentials.
- [ ] `docs/security.md`, `docs/weekly-sync.md` — document coverage, local command, supported platforms, failure recovery, no-scan/no-upload behavior, required-check setup and incident response.

**Acceptance Criteria:**
- Given a clean fixture, when finalize runs, then it commits/pushes as before and records successful scanning.
- Given a synthetic supported token in any candidate surface, when finalize runs, then no commit or push occurs and reports/logs contain no token.
- Given a bad rebased snapshot or secret-bearing reachable commit, when final push is attempted, then remote HEAD remains unchanged.
- Given unavailable/corrupt scanning or unsafe seed output, when publication is attempted, then it fails nonzero without upload/push or raw scanner diagnostics.
- Given fork PR configuration, when inspected/tested, then checks run hosted with read-only permission and no secret references.

## Implementation Notes

- Scanner pinned to Gitleaks 8.30.1 (tarball + binary SHA-256, 4 platforms). Content is scanned via opaque file names (dir mode) incl. all reachable history blobs, to avoid the scanner's built-in path allowlist and git attributes (found in independent review).
- Baseline finding: pre-existing history blobs of `tests/test_weekly_sync.py` contain a literal `AIza…`-shaped sentinel (synthetic). Working tree now builds it at runtime; history still blocks `repository`/push scans until the owner decides (no baseline added).

## Plan Change Log

- 2026-10-30 — Owner renegotiated the no-exception constraint: permit only the exact historical synthetic-sentinel blob/line exception after determining it is not a real Gemini key. It must be content-bound, documented and tested; no general baseline, path rule or new-content bypass is allowed.

## Review Triage Log

- false — `scripts/scan_secrets.py:70-76,483-485`: The narrow historical sentinel exception would have contradicted the original frozen constraint, but the owner explicitly renegotiated that constraint by choosing the documented-exception option. The frozen intent and change log now require exact blob/marker binding, coverage of remaining bytes, and no new-content match; tests prove those bounds.
- medium / patch — `.github/workflows/summarize-seed.yml:35`: `--allow-missing` allowed a missing measurement log while uploading a present summary, so one intended artifact was not scanned. Removed the flag; missing either output now fails the scan and prevents upload.

## Design Notes

Use the free CLI. PR checks cannot undo first exposure; native push protection is complementary. Malicious pipeline changes or policy bypass remain authorization threats.

## Verification

- `python3 -m unittest discover -s tests` — all tests pass, no network/model calls in unit tests.
- `python3 scripts/scan_secrets.py repository` — scan local tracked snapshot and reachable history using the real verified scanner; output sanitized, no remote writes. If findings exist, stop for triage without exposing values or weakening rules.
- `git diff --check` and scoped diff inspection — no videos/reviews/generated corpus changes.
- Independently review all publication paths and failure branches. Live Actions execution and enabling a required check need separate owner authorization.
