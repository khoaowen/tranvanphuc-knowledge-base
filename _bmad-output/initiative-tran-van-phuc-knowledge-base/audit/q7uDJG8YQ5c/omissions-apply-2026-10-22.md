# Omission apply — q7uDJG8YQ5c (2026-10-22)

## Approval
Human (user) approved nine drafts from `omissions-consolidated-2026-10-22.md`, applied verbatim: om12, om13, om15, om18, om19, om29, om30, om31, om32. **om04 skipped by instruction** (stays pending-human-approval). All other items remain pending/not applied. Approval of om13, om31 and om32 overrides the report's "recommend not adding"; recording a statement is not medical validation or endorsement (incl. alcohol).

## Pre-checks
- HEAD `d28dc443792a62e8b85283ea5e67ce52f5f27081`.
- Baseline summary.md SHA-256 `04ba0755…94ff8` — matched report. transcript.md `bbc4c9a5…d24b` — matched, unchanged.
- Each draft's evidence quotes re-resolved against transcript.md with `fidelity.resolve_quote`: all found (e.g. om12 02:30:47–02:30:53; om13 02:20:12–02:20:17; om15 02:34:07–02:34:11; om18 02:51:02–02:51:05; om19 03:06:05–03:06:07; om29 03:25:33; om30 00:42:11–00:42:13; om31 02:29:52/02:29:55/02:29:55/(02:30:00 list); om32 03:26:53, 03:27:32–03:27:36). Matching text is not speaker identity or truth.

## Applied (after the whole anchor claim; no anchor text edited)
| Draft | After claim | Form |
| --- | --- | --- |
| om30 | c074 | new paragraph |
| om31 | c112 | new paragraph |
| om13 | c109 | new paragraph |
| om12 | c119 | new bullet |
| om15 | c123 | new bullet |
| om18 | c149 | inline sentence after claim (claim not line-final) |
| om19 | c157 | new paragraph |
| om29 | c190 | new paragraph |
| om32 | c191 | new paragraph |

## Results
- New summary.md SHA-256 `3a90c9dbf75027562600f2ffb4bd7185b92dbfca57484f18888fe13a92210c39`; diff = 9 insertions, 1 line modified (om18 inline); no deletions of text.
- All 194 previous claims remain verbatim (incl. c068, c163 correction text); claims now 204. **Claim IDs after the first insertion (c074) are renumbered**, so earlier audit ids refer to the pre-apply summary (hash above); match by claim text.
- om31 keeps 'Anzimer'/'bakis' verbatim as caption strings; no disease identity asserted.
- `validate_summaries.py` (local, read-only): video reports "summarized (no passing review bound to this summary)" — the summary hash changed, so the stored review no longer binds. Expected; re-review is a separate step.
- Not touched: historical audit files, review.md (pre-existing working-tree change kept), transcript.md, metadata.json, queue_state, publishable. No paid services, commit, push or publication. Video stays blocked.
