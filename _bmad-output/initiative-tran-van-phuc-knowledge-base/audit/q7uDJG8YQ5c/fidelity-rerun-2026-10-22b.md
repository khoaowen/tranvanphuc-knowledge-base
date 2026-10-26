# Fidelity rerun — q7uDJG8YQ5c (2026-10-22b, incomplete)

## Preconditions

- `summary.md` SHA-256: `a7fa809724e4988c07bf89ff5723dff58cef2650b78b1405eacada5384437d8d`.
- `transcript.md` SHA-256: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`.
- The pre-rerun `review.md` was copied byte-for-byte to `review-before-fidelity-rerun-2026-10-22b.json` before execution (SHA-256 `1a651c6b81ad2f50ad2ee17da8e06f23c08eb8ff6091bcc0474423ca682729dc`).

## Execution

Used a temporary `--videos-dir` containing only a symlink to this video, so `--limit 1` could not select another video:

```sh
./review-summaries --videos-dir <temporary-single-video-directory> --limit 1 --model sonnet --no-commit
```

The command retried malformed JSON responses for chunks 1, 2, and 4. It stopped when the local Claude usage limit was reached (`resets 6pm (UTC)`) and reported `reviewed 0, failed 0`.

## Result

**Incomplete — no fresh review was produced.** The command did not overwrite `review.md`; it remains SHA-256 `1a651c6b81ad2f50ad2ee17da8e06f23c08eb8ff6091bcc0474423ca682729dc` and does not bind to the current summary hash.

No commit, push, publication, queue-state, or publishability change was made. Do not retry automatically; retry only after the usage limit resets and is authorized.
