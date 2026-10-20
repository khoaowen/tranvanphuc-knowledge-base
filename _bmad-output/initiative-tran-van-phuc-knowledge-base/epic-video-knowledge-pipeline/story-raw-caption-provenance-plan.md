---
title: 'Preserve raw captions with provenance and a zero-diff re-render check'
type: 'feature'
ticket: ''
created: '2026-10-20'
status: 'in-review'
baseline_revision: '47c72cecc30ff5e836e868b690352ec17cd613c6'
route: 'full'
route_source: 'auto'
risk: 'low'
review: 'quick'
review_source: 'pinned'
lenses_ran: []
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
