# Walkthrough: CI validator and publish gate (ticket 10)

Target: commits b79e5ef, 47c72ce plus uncommitted hardening in the working tree.
Current block: none (review done)

- [x] 1. Intent (accepted, unchanged)
- [x] 2. Broad strokes (accepted)
- [x] 3. Slice: publish-state derivation and exit codes (accepted)
- [x] 4. Slice: summary contract checks (accepted)
- [x] 5. Slice: stale marker (accepted)
- [x] 6. Slice: tests (accepted)
- [x] 7. Periphery (accepted)

## 1. Intent

Source: ticket [story-ci-validator-and-publish-gate-plan.md](../tickets/epic-video-knowledge-pipeline/tickets/story-ci-validator-and-publish-gate-plan.md), verbatim.

**Problem:** Nothing yet decides whether a `summary.md` may be published or consolidated. `summary-contract.md` names `scripts/validate_summaries.py` as the gate, but it does not exist, and `queue_state` only knows pending/transcribed/summarized.

**Approach:** Add a stdlib, read-only `scripts/validate_summaries.py` that checks each summary against the contract, rejects stale ones, and derives `published` from files: valid + current + not stale + a hash-bound `pass` review (via `queue_state.publishable`). Exit non-zero on any invalid video so CI can gate the commit.

## 2. Broad strokes

Read-only gate: per video, run contract checks, then ask `queue_state` whether a hash-bound passing review exists.

1. [`validate_video`](../../../scripts/validate_summaries.py) - orchestrates state, checks, review lookup, transcript-unchanged guard.
2. [`check_summary`](../../../scripts/validate_summaries.py) - returns the list of contract violations.
3. [`is_stale` / `mark_stale`](../../../scripts/validate_summaries.py) - hash-based stale marker.
4. [`main`](../../../scripts/validate_summaries.py) - CLI, one line per video, exit codes 0/1/2.
5. [`tests/test_validate_summaries.py`](../../../tests/test_validate_summaries.py) - one fixture per I/O row.
