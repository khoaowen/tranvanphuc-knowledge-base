# Raw captions (`videos/<dir>/raw/`)

`transcript.md` is a rendering of YouTube's Vietnamese automatic (ASR) captions. When
`scripts/fetch_transcript.py` fetches a video, it also keeps the caption file it downloaded,
so the transcript can always be rebuilt and checked. The raw file also keeps data the
transcript drops: per-word timings (`tOffsetMs`) and the `>>` speaker-change markers in context.

    videos/<published_at>-<slug>/
      metadata.json
      transcript.md                  # rendered from raw/, never hand-edited
      raw/
        captions.<track>.json3.gz    # track = vi-orig (preferred) or vi
        provenance.json

- **`captions.<track>.json3.gz`** is the source of truth. It holds exactly the json3 bytes yt-dlp
  downloaded, gzip-compressed with `mtime=0` and no embedded filename. No timestamp or
  filename goes into the stored bytes. It is written once and never edited. A re-fetch into a dir that
  already has `raw/` is refused. Read it with `zcat` or Python's `gzip.open`.
- **`provenance.json`** records `video_id`, `source_url`, `track`, `caption_kind` (`asr`, from
  `--write-auto-sub`), `retrieved_at` (UTC), `raw_file`, `sha256` (of the stored `.gz`),
  `yt_dlp_version`, `tool`, and `transcript_sha256` (of `transcript.md`).

**Why gzip:** a 3.5 h video's json3 is about 4.3 MB of pretty-printed JSON. Gzipped it is about
310 KB. Git compresses blobs anyway, so history size is about the same either way. The gain is in
the working tree and CI checkout. Raw files never change, so losing readable diffs costs nothing.

## Re-render and check (no network)

    python3 scripts/fetch_transcript.py --rerender videos/<dir> [...]  # rewrite transcript.md from raw/
    python3 scripts/fetch_transcript.py --check videos/<dir> [...]     # exit 1 on any difference

`--check` fails when any of these hold:
- `transcript.md` is not byte-identical to a re-render of the raw file.
- The raw file's sha256 no longer matches `provenance.json`.
- `transcript_sha256` is stale.
- The dir has no `raw/` layer.

`--rerender` refuses to run from a raw file whose sha256 does not match.

**Not yet backfilled:** videos fetched before this layer existed have no `raw/` yet, and
`--check` reports them as failures. Backfilling them is a follow-up. It means re-downloading,
then confirming that `--check` passes against the committed `transcript.md`.
