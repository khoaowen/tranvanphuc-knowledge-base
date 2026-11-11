# Audit summary: V-Qfwjo28Zg

- **Publication status: `blocked`**
- **Bound summary:** `git show 4e31e57^:<video dir>/summary.md`, SHA-256 `fbae11bf16fa47c8055fe7b309f45dfeb696db23a0009c593504c1351a98203c`. `summary.md` and `review.md` were deleted from `videos/` in `4e31e57`, so `summary.md` is absent at HEAD.
- **Validity:** any regenerated summary invalidates these claim ids, which come from extracting this exact text.
- **Claims audited:** 554
- **Classes (effective):** supported 490, attribution_qualification 46, mismatch 15, unresolved 3. Historical `final_records.json` is unchanged and still shows supported 491, mismatch 14; the one difference is c158, reclassified supported → mismatch in `effective-overrides.json` after review (the quote "tim đập nhanh" belongs to the opposite wake→sleep scenario; see `additional-corrections.md`). c158 was independently rechecked against the transcript.
- **Omissions:** 49 kept, 20 candidates excluded (`omissions.md`). 46 kept and 19 excluded candidates consolidate 23 range-restricted pass-1 reads; o29 was moved from kept to excluded after review as already covered, and o48-o50 were added from a later sequential read of the whole transcript. 49 + 20 = 69 = the 66 original candidates + 3 added.
- **Proposed corrections:** 63, all `pending-human-approval`, none applied (`proposed-corrections.md`). The effective non-supported set is 64: these 63 plus c158, whose correction is in `additional-corrections.*` (15 supplemental items, also pending, none applied).
- **Pass-2 coverage:** 94 claims (64 effective non-supported + 30 sampled supported). The other 460 supported claims had pass 1 only. c158's second pass is recorded in `effective-overrides.json`.
- **Reviewer decisions:** recorded per item in `decisions.json` (from `human-decisions.md`). They do not change any status: every correction stays `pending-human-approval`. The class counts, 63 and 15 above predate the decisions; items decided `keep-original` (e.g. c111, c471) still appear in them.
- **Overlap:** c013, c156 and c275 are in both correction files. The `additional-corrections.*` entry supersedes (`supersedes` field).
- **Omissions reconciliation:** 66 consolidated candidates + 3 added (o48-o50) = 69 = 49 kept + 20 excluded; o29 moved from kept to excluded.
- **Checks:** `check_audit.py` verifies the extraction, classes, effective overrides, evidence, quotes (including `additional-corrections.json` and `effective-overrides.json`), correction sets, omission counts against this summary, `videos/` diff and publication gate.

## Reconciled pass-1/pass-2 disagreements: 24, human to confirm

| Claim | Pass 1 | Pass 2 | Final |
|---|---|---|---|
| c003 | attribution_qualification | supported | supported |
| c013 | attribution_qualification | supported | attribution_qualification |
| c034 | attribution_qualification | supported | attribution_qualification |
| c054 | mismatch | supported | mismatch |
| c103 | attribution_qualification | supported | attribution_qualification |
| c111 | mismatch | unresolved | unresolved |
| c121 | attribution_qualification | supported | attribution_qualification |
| c125 | attribution_qualification | supported | attribution_qualification |
| c135 | attribution_qualification | supported | attribution_qualification |
| c166 | attribution_qualification | supported | attribution_qualification |
| c177 | attribution_qualification | supported | attribution_qualification |
| c182 | attribution_qualification | supported | attribution_qualification |
| c193 | attribution_qualification | supported | attribution_qualification |
| c235 | attribution_qualification | supported | attribution_qualification |
| c254 | attribution_qualification | supported | attribution_qualification |
| c282 | supported | attribution_qualification | attribution_qualification |
| c294 | attribution_qualification | supported | attribution_qualification |
| c352 | mismatch | supported | mismatch |
| c377 | attribution_qualification | supported | attribution_qualification |
| c456 | attribution_qualification | unresolved | unresolved |
| c471 | mismatch | supported | mismatch |
| c478 | mismatch | supported | mismatch |
| c500 | attribution_qualification | supported | attribution_qualification |
| c509 | attribution_qualification | unresolved | attribution_qualification |
