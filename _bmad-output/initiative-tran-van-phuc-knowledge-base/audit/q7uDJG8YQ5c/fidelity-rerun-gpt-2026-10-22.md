# Fidelity rerun — q7uDJG8YQ5c (GPT, 2026-10-22)

## Preconditions

- `summary.md` SHA-256: `a7fa809724e4988c07bf89ff5723dff58cef2650b78b1405eacada5384437d8d`.
- `transcript.md` SHA-256: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`.
- The previous incomplete-Claude cache was preserved as `review-progress-before-codex-rerun-2026-10-22.json` and cleared so that no Claude-produced chunk result was reused.

## Execution

The reviewer now supports Codex and defaults to `gpt-6.1-sol`. It invokes:

```sh
codex exec --ephemeral --sandbox read-only --model gpt-6.1-sol \
  --output-last-message <temporary-file> -
```

The rerun used a temporary `--videos-dir` containing only a symlink to this video:

```sh
./review-summaries --provider codex --model gpt-6.1-sol \
  --videos-dir <temporary-single-video-directory> --limit 1 --no-commit
```

All seven chunks and the coverage audit completed. The command reported `reviewed 1, failed 0`. The progress cache was removed after successful completion.

## Result

- `review.md` SHA-256: `ba9ed5640bcac6f1cfadcb6c64d3b03c4c83b92fcbb7a3cb0532b0719d591b9f`.
- Bound summary SHA-256: `a7fa809724e4988c07bf89ff5723dff58cef2650b78b1405eacada5384437d8d`.
- Verdict: **fail**.
- Claims: **185 pass, 15 flag, 4 fail** (204 total).
- Chunks: 7.
- Coverage complete: false; omissions: 7; concerns: 1.

No commit, push, publication, queue-state, or publishability change was made.

## Verification

`python3 -m unittest -v tests.test_review_batch.CliStub.test_codex_client_reads_final_message tests.test_review_summaries` passed: 45 tests.
