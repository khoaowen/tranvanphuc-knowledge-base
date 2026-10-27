# Fidelity rerun — q7uDJG8YQ5c (2026-10-22)

## Preconditions

- `summary.md` SHA-256: `3a90c9dbf75027562600f2ffb4bd7185b92dbfca57484f18888fe13a92210c39` (matched required value).
- `transcript.md` SHA-256: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b` (matched required value).
- The pre-rerun, uncommitted `review.md` was copied byte-for-byte to `review-before-fidelity-rerun-2026-10-22.json` before execution (SHA-256 `58ee9b33328c42eceb84281607e6da86724925ed5f09a6ce22a84a7fa6455d2c`).

## Execution

Used a temporary `--videos-dir` containing only a symlink to this video, so `--limit 1` could not select another video:

```sh
./review-summaries --videos-dir <temporary-single-video-directory> --limit 1 --model sonnet --no-commit
```

Local Claude was authorized for this run. `--no-commit` was used; no commit, push, publication, or queue-state/publishability change was made. The command reported `reviewed 1, failed 0`.

## Result

The rerun overwrote the working-tree `review.md`; its resulting SHA-256 is `1a651c6b81ad2f50ad2ee17da8e06f23c08eb8ff6091bcc0474423ca682729dc` and it binds to the required new summary hash.

- Verdict: **flag**
- Claims: **202 pass, 2 flag, 0 fail** (204 total)
- Chunks: 7
- Coverage complete: true; confirmed omissions: 0
- Concerns: 4 minor, 0 material

The two flagged claims are c033 (the home-to-work traffic/roadworks illustration is not in the cited slice) and c061 (the cited slice introduces Lipton but not the stated 1985/Caribbean/lesson-preparation details). Neither is one of the nine approved omission insertions.

## Approved omission insertions

All claim units created by the nine approved insertions passed: c075 and c076 (om30's semicolon-separated paragraph), c112 (om13), c116 (om31), c124 (om12), c129 (om15), c156 (om18), c165 (om19), c199 (om29), and c201 (om32). Thus none of the nine inserted sentences has a failed or flagged claim.

## Continuity checks

The unchanged prior claim text referred to as c068 remains c068 and passes. The unchanged text formerly identified as c163 was renumbered to c171 after the insertions and passes.

For comparison only, the known open-item texts formerly identified as c012, c124, c019, c055, and c192 map in this rerun to c012, c130, c019, c055, and c202 respectively; the model returned pass for each. They are not reported as new regressions by this rerun.
