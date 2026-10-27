---
title: 'Preserve raw captions with provenance and a zero-diff re-render check'
type: 'feature'
ticket: '13'
created: '2026-10-20'
status: done
baseline_revision: '47c72cecc30ff5e836e868b690352ec17cd613c6'
route: 'full'
route_source: 'auto'
risk: 'low'
review: 'quick'
review_source: 'pinned'
lenses_ran: [quick]
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** `fetch_transcript.py` downloads YouTube's Vietnamese ASR json3 into a temp dir, renders `transcript.md`, then throws the json3 away. Per-word timings (`tOffsetMs`) and speaker-change markers are lost, and nothing records where or when a transcript came from.

**Approach:** On fetch, store the downloaded json3 unchanged under `videos/<dir>/raw/`, plus a `raw/provenance.json`. Add a CLI path that re-renders `transcript.md` from the raw file, and a check mode that exits non-zero when the re-render differs from the committed `transcript.md`.

## Boundaries & Constraints

**Always:** The raw file is the source of truth: written once, never edited. It is stored gzip-compressed and deterministic: `raw/captions.<track>.json3.gz`, where track is `vi-orig` or `vi`, written with `gzip.compress(data, compresslevel=9, mtime=0)`. Decompressing it gives back exactly the bytes yt-dlp downloaded. The renderer reads `.gz` transparently. `provenance.json` holds `video_id`, `source_url`, `track`, `caption_kind` (`asr`, because the source is `--write-auto-sub`), `retrieved_at` (UTC ISO-8601, `YYYY-MM-DDTHH:MM:SSZ`), `raw_file`, `sha256` (of the stored `.gz` bytes), `yt_dlp_version` (`yt-dlp --version`), `tool` (`scripts/fetch_transcript.py`), and `transcript_sha256` (of the `transcript.md` bytes). The `transcript.md` format stays byte-identical to today's renderer: same `[hh:mm:ss] text` lines, `>>` kept as is, timestamps unchanged. Tests make no network calls; `subprocess.run` is mocked.

**Never:** Do not re-fetch, re-render or modify any existing `videos/*` file (transcript, summary, metadata, review). Backfilling raw captions for existing videos is a follow-up. Do not change `metadata.json`'s schema. Do not touch the claim-level timestamp links or the handling of `>>` as metadata; those are later stories. Do not add dependencies; use the stdlib only.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| New fetch, vi-orig present | `fetch_transcript.py <id>` | `metadata.json`, `transcript.md`, `raw/captions.vi-orig.json3.gz`, `raw/provenance.json` with `track: vi-orig` | No error |
| Only vi track produced | yt-dlp writes only `<id>.vi.json3` | `raw/captions.vi.json3.gz`, `track: vi` | No error |
| Raw captions already stored | `raw/provenance.json` exists for the target dir | Nothing in that dir is written; video skipped | Warning to stderr naming `--rerender` |
| `yt-dlp --version` fails | non-zero exit | Video skipped, nothing written | Per-video warning, as today |
| Re-render | `--rerender <video_dir>` | `transcript.md` rewritten from raw; provenance unchanged | Missing raw or provenance: error, exit 1 |
| Check, clean | `--check <video_dir>` | Exit 0 | — |
| Check, tampered transcript | `transcript.md` edited | Exit 1, names the dir | stderr message |
| Check, tampered raw | raw `.gz` sha256 differs from provenance | Exit 1 | stderr message |
| Check, no raw layer | dir without `raw/provenance.json` | Exit 1 | stderr "no raw captions" |

</frozen-after-approval>

## Code Map

- `scripts/fetch_transcript.py` -- the only code change. `fetch_caption_json3` already returns the vi-orig/vi path, and its filename gives the track. `build_transcript_lines` must keep its output exactly; it gains transparent `.gz` reading. `write_video_files` writes `"\n".join(lines) + "\n"`. Pull that into a `render_transcript(lines)` helper shared by fetch, rerender and check, so all three produce the same bytes. `fetch_one_video` calls yt-dlp's version check and builds everything inside the tempdir. `main` gets `--rerender DIR...` and `--check DIR...` (mutually exclusive with the video ids).
- `scripts/review_batch.py:109` -- `commit_video` runs `git add -- <video_dir>`, so `raw/` is committed along with everything else. No change needed.
- `scripts/queue_state.py`, `scripts/detect_new_videos.py` -- glob `*/metadata.json` only, so `raw/` does not affect them. No change.
- `tests/test_summarize.py` -- conventions: `unittest`, `sys.path.insert(REPO_ROOT/"scripts")`, `mock.patch.object(module.x, ...)`, `tempfile.TemporaryDirectory`.
- Evidence (read-only, other worktree): `_bmad-output/.../research-transcript-fidelity-q7udjg8yq5c/evidence/raw-captions/q7uDJG8YQ5c.vi-orig.json3` and `.vi.json3`. Both are 4.3 MB. With today's `build_transcript_lines`, both re-render byte-identically to the committed seed `transcript.md`. gzip -9 -n gives about 311 KB.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/fetch_transcript.py` -- add `yt_dlp_version()`, `track_from_caption_path()`, `render_transcript()`, `write_raw_captions()` (gzip + provenance), `rerender_transcript(video_dir)`, `check_transcript(video_dir)` (returns a list of problems), and the `--rerender`/`--check` CLI. Update the docstring. -- implements the raw layer.
- [ ] `tests/test_fetch_transcript.py` -- new file. Uses a fixture json3 with a newline-only event, a `>>` line and an hour+ timestamp, and a mocked `subprocess.run` that writes the fixture to the `-o` template. Covers: raw + provenance written with every field and correct hashes; the gz decompresses to the fixture bytes; the exact expected `transcript.md`; rerender restores the transcript and `--check` passes; tampered transcript or raw fails `--check`; the vi fallback records `track: vi`; an existing raw layer is refused; no raw layer fails `--check`.
- [ ] `docs/raw-captions.md` -- new file: layout, provenance fields, the gzip choice, rerender/check usage, backfill follow-up. -- AC6.
- [ ] `README.md` -- one line pointing to the doc.

**Acceptance Criteria:**
- Given the full existing suite, when `python3 -m unittest discover -s tests` runs, then all tests pass, including the new ones.
- Given the branch, when `git diff 47c72ce -- videos/` runs, then the output is empty.

## Implementation Notes

- Implemented directly by the worker session, with no coding subagent available. Changed `scripts/fetch_transcript.py`. New files: `tests/test_fetch_transcript.py` (15 tests) and `docs/raw-captions.md`. Added one line to `README.md`.
- Byte-identity evidence:
  - On the fixture, the baseline `build_transcript_lines` (from `47c72ce`), the new renderer and `EXPECTED_TRANSCRIPT` give identical output.
  - The seed's stored json3 files (`vi-orig` and `vi`, read-only from the Epic2-publish-videos evidence folder) were stored through `write_raw_captions` into a temp dir. `check_transcript` then passed against a copy of the committed seed `transcript.md`. Stored size: 310,815 bytes.
- `check_transcript` also flags a stale `transcript_sha256` in provenance. `rerender_transcript` refuses a raw file whose sha256 mismatches.
- The two existing videos have no `raw/`, so `--check videos/*/` reports them as failures, as designed. Backfill is deferred.

## Plan Change Log

- 2026-10-24: Repaired the missing ticket link using existing entry 13 from commit `554fb5d` (not an ancestor of this branch). Restored that entry and its recorded prerequisite on entry 11 in the migrated `tickets/tickets.toml`. No new ID was allocated. Preserved this plan's `in-review` status; the historical commit's `done` transition was not copied. No implementation or video content changed.

## Review Triage Log

- Pass 1 (self-review in place of the Quick lens; this session could not spawn a context-free reviewer subagent, so `lenses_ran` is empty and the independent review gate is still open): high 0, medium 0, low 2, false 0, maybe-false 0.
  - low / patch: the docs and comment said the gzip bytes "depend only on the content". That is not exactly true: the zlib version and OS header byte also matter. Reworded the docs, the comment and the Design Notes. Provenance hashes the stored file, so verification is unaffected.
  - low / patch: `--check`'s stale `transcript_sha256` branch and `--rerender` on a dir with no raw layer were untested. Added `test_check_detects_stale_transcript_sha256` and the rerender assertions in `test_check_fails_without_raw_layer`.

## Design Notes

**gzip over plain json3.** A 3.5 h video's json3 is about 4.3 MB of pretty-printed JSON. With deterministic gzip -9 it is about 311 KB, roughly 14x smaller. Git zlib-compresses blobs anyway, so clone and pack size are about the same either way. The real difference is the working tree and CI checkout: roughly 135+ backlog videos would cost hundreds of MB as plain files, versus tens of MB gzipped. The usual cost of gzip, losing readable diffs, does not apply because raw files never change. `zcat`/`gzip.open` read them transparently. `mtime=0` and no embedded filename keep timestamps out of the stored bytes. The recorded `sha256` is of the stored file, so verification never depends on recompressing.

**Refusing to overwrite raw.** A re-run of `fetch_transcript.py` for a dir whose raw layer exists would otherwise overwrite the source of truth with a different download. The task says the raw file is never edited, so the script refuses and points to `--rerender`. Existing videos have no `raw/`, so their behavior does not change.

## Verification

**Commands:**
- `python3 -m unittest discover -s tests` -- expected: OK.
- `git diff 47c72ce --stat -- videos/` -- expected: empty.
- `git status --porcelain videos/` -- expected: empty.

## Code Review

### 2026-10-20
**Review summary:** 0 decision-needed, 3 patch, 1 defer, 4 rejected.

- [x] [Review][Patch] Refuse fetching into any existing video directory [scripts/fetch_transcript.py:286] — fixed: the target directory is rejected before fetching captions; regression test preserves a pre-raw directory unchanged.
- [x] [Review][Patch] Make fetch output atomic [scripts/fetch_transcript.py:299] — fixed: all output is assembled in a sibling staging directory and renamed only after raw/provenance writing succeeds.
- [x] [Review][Patch] Report unreadable raw captions as check failures [scripts/fetch_transcript.py:348] — fixed: malformed gzip/json3 is reported per directory and does not stop subsequent checks.
- [x] [Review][Defer] Wire raw-caption tests/check into CI [ .github/workflows/weekly-sync.yml:1 ] — deferred: CI wiring is an explicitly deferred follow-up and cannot enable `--check` before existing videos are backfilled.

**Rejected**
- Blind Hunter: gzip byte variation across platforms — low: provenance verifies the stored bytes and raw files are immutable; cross-platform reproducible compressed bytes are not needed for ordinary use.
- Blind Hunter: arbitrary `raw_file` basename accepted — low: fetch writes the required filename and the current validation prevents traversal; only coordinated manual provenance changes could bypass the layout convention.
- Blind Hunter: provenance is not cross-checked with metadata video ID/track — low: the check verifies raw/transcript consistency, not authenticity against manually replaced complete directories; no ordinary path creates that state.
- Intent Alignment: gzip differs from a literal uncompressed reading — false: the frozen plan explicitly requires deterministic gzip with decompression recovering the exact downloaded bytes.

### 2026-10-20 (re-review)
**Review summary:** 0 decision-needed, 1 patch, 1 defer, 2 rejected.

- [x] [Review][Patch] Contain all malformed raw-caption failures [scripts/fetch_transcript.py:354] — fixed: `EOFError`, `zlib.error`, and schema-triggered `ValueError` are returned as per-directory check failures; truncation and malformed-schema regressions are covered.
- [x] [Review][Defer] Add a legacy-video raw-caption backfill path [scripts/fetch_transcript.py:287] — deferred: existing-video backfill is an explicit follow-up; it requires an approved source/retrieval and verification process, not an automatic re-fetch.

**Rejected**
- Blind Hunter + Edge Case Hunter: concurrent destination creation can race the pre-rename existence check — low: it requires an independent concurrent writer for the same derived directory; a portable no-replace directory commit would add disproportionate complexity, while ordinary fetches remain protected.
- Intent Alignment: this hardening diff does not newly test unchanged happy-path raw-caption behavior — false: those behaviors are outside this re-review's changed surface and were already covered by the prior full review/tests.

### 2026-10-20 (final re-review)
**Review summary:** 0 decision-needed, 4 patch, 0 defer, 3 rejected.

- [x] [Review][Patch] Remove duplicate CI/backfill tracking [ _bmad-output/initiative-tran-van-phuc-knowledge-base/deferred-work.md:28 ] — fixed: retained the canonical CI/backfill entries and removed the duplicate review entry.
- [x] [Review][Patch] Align fetch failure docstring with staged behavior [scripts/fetch_transcript.py:282] — fixed: documents no partial video directory and refusal of any existing target directory.
- [x] [Review][Patch] Distinguish unreadable transcript errors [scripts/fetch_transcript.py:348] — fixed: transcript I/O now reports its own path, separate from raw-caption decoding/integrity errors.
- [x] [Review][Patch] Reject negative caption timestamps [scripts/fetch_transcript.py:195] — fixed: non-integer, boolean, and negative `tStartMs` raise a reported validation error; negative-timestamp regression coverage added.

**Rejected**
- Edge Case Hunter: deeply nested JSON must add `RecursionError` handling — false: `RecursionError` is a `RuntimeError`, already caught by `check_transcript`.
- Blind Hunter + Edge Case Hunter: concurrent destination creation can race the pre-rename existence check — low: it requires an independent concurrent writer for the same derived directory; a portable no-replace directory commit would add disproportionate complexity.
- Intent Alignment: the final hardening diff does not newly test unchanged happy paths — false: unchanged feature paths remain out of scope for this focused re-review and retain existing coverage.

### 2026-10-20 (follow-up re-review)
**Review summary:** 1 decision-needed, 3 patch, 0 defer, 2 rejected.

- [ ] [Review][Decision] Resolve pending-directory fetch policy — `review_batch` fetches a queued `PENDING` directory that already contains metadata; the new universal existing-directory refusal makes that documented flow fail. Choose whether an explicitly validated pending directory may be completed with raw/transcript artifacts, or whether pending discovery must create no directory until fetch succeeds.
- [ ] [Review][Patch] Contain recursion-limit raw-caption failures [scripts/fetch_transcript.py:363] — `RecursionError` during json decoding is not caught by the render path and can still abort `--check`.
- [ ] [Review][Patch] Reject raw JSON without a json3 event list [scripts/fetch_transcript.py:184] — a hash-valid `{}` can render as a newline and pass `--check` rather than being reported as malformed caption data.
- [ ] [Review][Patch] Document malformed raw-caption check failures [docs/raw-captions.md:32] — `--check` now reports unreadable gzip, JSON, and schema errors but the documented failure list omits them.

**Rejected**
- Blind Hunter: `transcript_path.is_file()` can abort on an OSError — false: `Path.is_file()` suppresses `OSError` and returns false, which is reported as a missing transcript.
- Blind Hunter + Edge Case Hunter: concurrent destination creation can race the pre-rename existence check — low: it requires an independent concurrent writer for the same derived directory; a portable no-replace directory commit would add disproportionate complexity.

### 2026-10-21 (approved pending-completion exception and final review)
**Review summary:** 0 decision-needed, 4 patch, 0 defer, 2 rejected.

- [x] [Review][Decision] Pending-directory fetch policy — user explicitly confirmed Option 1. Added a controlled pending-completion mode used by `review_batch.py`; ordinary fetch still refuses existing directories. Pending artifacts are staged then installed with atomic no-replace file links and raw-directory creation; collisions and interrupted attempts fail closed. The frozen intent was not edited; this approved exception is recorded here.
- [x] [Review][Patch] Contain recursion-limit raw-caption failures — `RecursionError` is converted to a per-directory `--check` failure during raw loading or transcript rendering; regression test added.
- [x] [Review][Patch] Reject raw JSON without a json3 `events` list — renderer now validates the required list and event objects; hash-valid malformed JSON regression test added.
- [x] [Review][Patch] Document malformed raw-caption check failures — docs now list gzip/JSON/schema failures and explain per-directory continuation.
- [x] [Review][Patch] Existing-directory refusal should name `--rerender` — final independent Quick review identified the omission; refusal now directs users to `--rerender` when raw captions exist, covered by regression assertion.
- Pending-completion collision regression verifies a concurrently created transcript is preserved and causes failure rather than overwrite.
- Final independent Quick review of the post-fix diff: no findings. Full suite: 147 tests passed; `git diff 47c72ce -- videos/` remains empty.

**Rejected**
- User-approved pending completion was not treated as permission to rewrite existing metadata or to backfill published videos; the implementation checks metadata identity and metadata-only directory state and adds only staged transcript/raw artifacts.
- Additional review iterations were not requested; stop after applying and verifying the one final reviewer patch.
