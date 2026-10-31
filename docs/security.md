# Pipeline secret-leak prevention

The weekly pipeline publishes to a public repository, so it refuses to commit, push
or upload anything the pinned scanner flags — or anything it cannot examine.

## What it is (and is not)

- **Scanner:** [Gitleaks](https://github.com/gitleaks/gitleaks) **8.30.1**, free CLI,
  built-in default rules only. "Deterministic" means fixed rules: no LLM, no calls to
  validate credentials. It finds *recognizable* credential formats and high-entropy
  assignments. **A clean scan does not prove the absence of all secrets, medical
  safety or prompt-injection safety.**
- **Implementation:** `scripts/scan_secrets.py` (stdlib only), shared by the Mac command,
  the GitHub workflows and the tests.
- **Rules are never weakened:** inline `gitleaks:allow`, `.gitleaksignore`, baselines,
  `.gitleaks.toml` and `GITLEAKS_*` environment overrides are all disabled. A
  `.gitleaks.toml`/`.gitleaksignore` committed to the repo is scanned as inert text and
  noted in the result. There are no path exclusions: tests, generated content, raw
  captions and gzip'd captions (decompressed, bounded) are scanned.

**One reviewed exception:** three historical blobs of `tests/test_weekly_sync.py` (pinned by
exact git blob id in `SYNTHETIC_PLACEHOLDER_BLOBS`) contained a synthetic, non-working
placeholder key. In history mode only, that one line is dropped from those blobs; the rest of
each blob is still scanned and any other finding still blocks. It is not a baseline, path
exclusion or rule change, and it matches no new content.

## Bootstrap and supported platforms

macOS arm64/x64 and Linux x64/arm64. The release archive is downloaded over HTTPS into
`~/.cache/tranvanphuc-weekly/scanner/` (override: `TRANVANPHUC_SCANNER_CACHE`) and checked
against SHA-256 values embedded in the script (taken from upstream
`gitleaks_8.30.1_checksums.txt` and cross-checked with the GitHub release asset digests),
then the extracted binary's own SHA-256 and `version` output are verified — on every use.
Unsupported platform, download failure, checksum/version mismatch, timeout or scanner
error all **block** with a sanitized message. To bump the version, update the pins from the
upstream checksums file and re-run the tests.

```
python3 scripts/scan_secrets.py bootstrap      # install/verify the scanner
python3 scripts/scan_secrets.py index          # exact prospective index (write-tree)
python3 scripts/scan_secrets.py repository     # reachable history + final tracked snapshot of HEAD
python3 scripts/scan_secrets.py commit <rev>
python3 scripts/scan_secrets.py artifacts [--allow-missing] FILE...
```
Exit codes: `0` clean, `3` findings, `4` could not certify. Add `--json` for the sanitized
outcome. Output contains only rule ids, a repo-relative path (withheld if it looks like it
carries a secret) and a line number — never matched values, snippets or raw reports.
Files over 20 MB, NUL-bearing non-image content (e.g. UTF-16), corrupt gzip, symlink
oddities, shallow clones and index changes during a scan are errors, not "clean". Known
image files are listed in the result as not text-scanned.

## Where it gates publication

| Point | Check | On failure |
| --- | --- | --- |
| `./weekly-sync` preflight | bootstrap, then `repository` scan (before any prompt) | stops, no key prompt |
| `finalize`, after generation and staging | scan of the exact index tree id; index re-verified unchanged; that tree is committed (`commit-tree`) | no commit, exit 2 |
| `finalize`, immediately before push (after the rebase and the `before_push` seam) | reachable history **and** final tree of the exact commit id | no push, exit 2 |
| push | pushes the scanned commit id, never a moving `HEAD`, never forced | — |
| `summarize-seed.yml` | scan of `summary.md` + `measurement.log` | no artifact upload |
| `secret-scan.yml` (hosted) | `repository` scan on PR / push / manual | red check |

Sanitized outcomes are stored in the run report under `report.secret_scan`. Findings and
the offending files are kept locally; nothing deletes them, rotates keys or rewrites history.

The automated commit is created from the scanned tree with `git commit-tree`, so local
`pre-commit`/`commit-msg` hooks do not run for it (none are configured in this repository).
Scan content is written to opaque file names, so the scanner's built-in path allowlist
(lockfiles, `.svg`, `.pdf`, ...) and `.gitattributes` `export-ignore` cannot exempt files;
history mode scans every reachable blob. Images are scanned for printable strings only.

Manual `git commit`/`git push` outside the pipeline are **not** gated. GitHub-native secret
scanning and push protection are complementary; verify their state in the repository
settings before relying on them (they were enabled with no rulesets when this was written).

## When a scan blocks

1. Read the sanitized rule/path/line; open the file locally (do not paste the value anywhere).
2. If it is a real credential: **revoke/rotate it at the provider first.** If it was ever
   public (a pushed commit, a workflow artifact), deleting the file is not enough.
3. Remove it from the working tree and any unpushed commits (history rewriting is a
   deliberate owner decision, never done by the pipeline). A secret in an outgoing
   intermediate commit blocks the push even when absent at `HEAD`.
4. If it is a synthetic test value, build it at runtime in the test instead of writing the
   literal. Do not add allow-lists or baselines.
5. Re-run `./weekly-sync --resume <evidence dir>` (or the scan command above).

Scanner unavailable? Fix connectivity/platform and rerun; the pipeline will not publish
without a verified scan. Reachable history is scanned in full, so a historical finding
already on the remote keeps blocking pushes until the owner decides how to handle it
(rotate, then rewrite history, or knowingly change the gate's scope in a reviewed change).

## Required check (owner setup, not automated)

Enabling a required status check is a repository setting. In *Settings → Rules* (or branch
protection), require the **Secret scan / scan** check on the default branch and require
review of changes to `scripts/scan_secrets.py`, `.github/workflows/secret-scan.yml` and the
other workflows (CODEOWNERS or a ruleset path rule). A PR executes its own copy of the gate,
so changes to the gate cannot prove themselves; they need human review. Fork PRs run on a
hosted runner with a read-only token and no secrets.

## Incident response

Revoke/rotate first, then assess exposure (public commits, forks, cached artifacts), then
remove the value from the repository and, if the owner decides, from history. Record the
rotation; the gate stays on.
