---
title: 'Fetch transcript and metadata'
type: 'feature'
ticket: '2'
created: '2026-03-21'
status: 'built'
baseline_revision: '5c83890a51204d5eaa04e3202ac18f16e91a9eeb'
route: 'full'
route_source: 'auto'
risk: 'low'
review: 'quick'
review_source: 'pinned'
lenses_ran: ['quick']
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Entry 1's new-video-id list has nothing to act on yet — no way to pull a video's Vietnamese transcript and metadata into `videos/<slug>/`.

**Approach:** Add `scripts/fetch_transcript.py`. For each video ID (arg or piped on stdin, one per line), use `yt-dlp` (same tool as entry 1, no API key; verified locally: seed video has both `vi-orig` and `vi` auto-caption tracks) to fetch metadata and the Vietnamese caption track in `json3` format, then write `videos/<date>-<slug>/metadata.json` and `transcript.md`.

## Boundaries & Constraints

**Always:** Use `yt-dlp` for both metadata and captions. Prefer `vi-orig`, fall back to `vi`. Slug = slugified full title (diacritics stripped, lowercased, non-alphanumeric runs collapsed to one hyphen), prefixed with upload date as `YYYY-MM-DD` — do not extract a "Số N" number separately; real titles show it's inconsistent (`Số 132: ...` prefix, `...- Số 127` suffix, absent on seed video `q7uDJG8YQ5c`), and slugifying the whole title preserves it wherever present without branching. `metadata.json` = exactly `{video_id, title, url, published_at, duration, topics}`, `topics` always `[]` (CAP-3 fills it later). Parse `json3` (not `vtt`, which rolls duplicate text across cues); build `transcript.md` from its `events`, skipping bare-newline-only entries, one `[hh:mm:ss] text` line per remaining event. A per-video failure (no Vietnamese captions, yt-dlp error) must not abort the run — warn to stderr, skip, continue. Exit non-zero only if every requested video failed.

**Never:** Do not call `summarize.py`/write `summary.md` (entry 3). Do not touch `topics/*.md`/`README.md` (entry 4). Do not add a YouTube Data API key or a third-party transcript package. Do not write partial/empty files for a video whose fetch failed.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Seed video, has captions | `q7uDJG8YQ5c` as arg | `videos/2025-12-06-<slug>/metadata.json` + `transcript.md` created | No error |
| IDs piped via stdin | `echo q7uDJG8YQ5c \| python scripts/fetch_transcript.py` | Same result as arg form | No error |
| No Vietnamese captions | Real ID, no `vi`/`vi-orig` track | Video skipped, run continues | Warning to stderr, no crash |
| yt-dlp fetch fails | Subprocess non-zero (network/bad ID) | Video skipped, run continues | Warning to stderr, no crash |
| No video IDs given | Empty args and empty stdin | No-op, nothing written | Exits 0, no error |
| All requested videos fail | e.g. one bad ID only | No files written | Exits non-zero, stderr summary |

</frozen-after-approval>

## Code Map

- `scripts/fetch_transcript.py` -- new file; only new file. Stdlib only (`json`, `sys`, `argparse`, `subprocess`, `unicodedata`, `pathlib`, `tempfile`) plus `yt-dlp` via `subprocess`.
- `scripts/detect_new_videos.py` -- reuse its error-handling style (stderr warning + continue, `subprocess.run(..., timeout=..., capture_output=True, text=True)`), not its code.
- `repo-structure.md` (spec) -- defines `videos/<slug>/metadata.json` fields and `transcript.md`.
- Verified locally: `yt-dlp --skip-download --write-auto-sub --sub-langs "vi-orig,vi" --sub-format json3 <url>` downloads both tracks for `q7uDJG8YQ5c`. `json3`'s `events` hold `{tStartMs, dDurationMs, segs:[{utf8:...}]}`; pure line-break entries carry `segs:[{utf8:"\n"}]` with no `dDurationMs` — filter those, keep the rest (no rolling-duplicate text, unlike `vtt`).
- Verified locally: prefer `yt-dlp --skip-download -j <url>` (JSON) over `--print "a|b|c"` to avoid delimiter collisions with titles; parse `title`, `upload_date` (`YYYYMMDD`), `duration`, `webpage_url`, `id`.

## Tasks & Acceptance

**Execution:**
- [ ] `scripts/fetch_transcript.py` -- implement `slugify(title)` (NFD-normalize, strip combining marks, map `đ`/`Đ` explicitly, lowercase, collapse non-alphanumerics to single hyphens, trim ends), `fetch_metadata(video_id)` (`yt-dlp --skip-download -j <url>`, parse JSON, raise on failure/bad JSON), `fetch_caption_json3(video_id, tmp_dir)` (`yt-dlp --skip-download --write-auto-sub --sub-langs "vi-orig,vi" --sub-format json3 -o <tmp_dir>/%(id)s <url>`, pick `vi-orig` file else `vi`, raise if neither), `build_transcript_lines(json3_path)` (parse `events`, skip bare-newline entries, format `[hh:mm:ss] text`), `write_video_files(videos_dir, metadata, lines)` (create `videos/<published_at>-<slug>/`, write `metadata.json` with `topics: []` + `transcript.md`), and `main()` reading IDs from `sys.argv[1:]` or stdin, catching per-video exceptions as warnings, exiting non-zero only if all requested IDs failed.
- [ ] Ad-hoc `python3 -c` checks (no test framework set up yet) covering `slugify` and the newline-filtering in `build_transcript_lines` -- see Verification.

**Acceptance Criteria:**
- Given no `videos/` dir, when `python scripts/fetch_transcript.py q7uDJG8YQ5c` runs, then `videos/<date>-<slug>/metadata.json` and `transcript.md` exist, `video_id` is `q7uDJG8YQ5c`, `transcript.md` has timestamped lines.
- Given an ID piped via stdin instead of an arg, when run, then the same files are produced.
- Given one bad ID mixed with one good one, when run, then the good one's files are written, stderr warns about the bad one, exit is 0.
- Given only bad IDs, when run, then nothing is written and exit is non-zero.

## Implementation Notes

## Plan Change Log

## Review Triage Log

## Design Notes

`json3` over `vtt`: `vtt` auto-captions roll each phrase across overlapping cues (needs de-dup); `json3`'s `events` already segment cleanly, aside from trivial newline-only markers.

## Verification

**Commands:**
- `python scripts/fetch_transcript.py q7uDJG8YQ5c` -- expected: exit 0; `videos/2025-12-06-<slug>/metadata.json` + `transcript.md` exist; metadata has `"video_id": "q7uDJG8YQ5c"` and `"topics": []`; transcript has multiple `[hh:mm:ss]` lines.
- `echo q7uDJG8YQ5c | python scripts/fetch_transcript.py` -- expected: same result as arg form.
- `python scripts/fetch_transcript.py not-a-real-id q7uDJG8YQ5c` -- expected: exit 0; stderr warns on `not-a-real-id`; seed video's files still written.
- `python scripts/fetch_transcript.py not-a-real-id` -- expected: exit non-zero; nothing written.
- `python3 -c "from scripts.fetch_transcript import slugify; print(slugify('Số 132: \"Vắc xin ung thư\" viết lại'))"` -- expected: clean ascii-hyphen slug, no diacritics, no leading/trailing hyphens.

**Manual checks (if no CLI):**
- Open `videos/2025-12-06-<slug>/transcript.md`, confirm coherent non-duplicated Vietnamese text with ascending timestamps.
