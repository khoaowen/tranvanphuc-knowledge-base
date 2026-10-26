# Verification report — q7uDJG8YQ5c supplement build

**Current result (2026-10-20): assembly and quote checks pass; publication remains blocked.** The dated recheck below supersedes the earlier missing-supplement and undetermined-omission findings. Classification adjudication and remaining omission gaps are incomplete. The original preconditions and findings below are preserved as historical evidence, not current assertions of missing files.

## Checks completed

- `fidelity.extract_claims(summary.md)` returns 194 claims, c001–c194.
- The read-only `final_records.json` contains 149 records: 125 supported and 24 attribution_qualification. All 24 non-supported records have a pass-2 class recorded.
- `verify_quotes.py q7uDJG8YQ5c <transcript.md> final_records.json` reports 355 quotes and 0 failures.
- `omissions.md` has 22 numbered omissions. `audit-summary.md`'s prior 47 count is erroneous, as the existing `report.md` and `omissions.md` both specify 22.
- `queue_state.publishable(video_dir)` returns `False`.
- `git diff --stat 47c72ce -- videos/` is empty, and `git status --short -- videos/` is empty (before/after this build).

## Blocking gap

The existing `final-claims-mapping.md` and `final-claims-audit.json` cover the earlier 160-claim state (111 unchanged and 49 changed/new). They do not map the current 194 claims, which the plan says comprise 89 unchanged and 105 changed/new. The 49 review-tool records lack the required section, speaker, and class fields. Consequently, they cannot be promoted as format-compliant supplement records, and a complete id remap / 194-record quote-verification result cannot be asserted from these artifacts.

No supplement records or second-pass results were fabricated. The requested independent `gpt-6.1-sol` pass was not run because a validated set of non-supported supplement claims and corresponding full-format records is not yet available. No `opus` invocation was made. The 22 omissions have not been individually rechecked against the current summary, so their statuses remain undetermined by this build.

## Files and protected state

The verification report and append-only audit-summary notes changed; new supplement records, pass-2 results and omission recheck were added. `final_records.json`, pass1/raw artifacts, source video files, summary/transcript/review files, `omissions.md`, and all pending-human-approval omission items remain untouched. Publication remains blocked.

## 2026-10-20 current-files recheck — gpt-6.1-sol (this invocation)

### Checks actually run

1. Reran existing `fidelity.extract_claims` against the current summary: **194 claims, c001–c194**.
2. Parsed existing `supplement-records.json`: **89 id_remap entries + 105 new records**. Built a temporary assembly by copying each referenced original record from read-only `final_records.json`, replacing its ID with `current_id`, and adding the 105 new records. No audit input was changed.
3. Checked that assembly against current extraction: **194 unique IDs**, complete c001–c194 coverage, no unknown/missing IDs, exact `claim` and `section` matches, required `id`, `section`, `claim`, `evidence`, `speaker`, `class`, `note` fields present and nonempty evidence on all records. **0 errors**. This establishes structural/text completeness, not new semantic adjudication of all claims.
4. Ran existing `audit/verify_quotes.py q7uDJG8YQ5c <current transcript.md> <temporary assembled-current-records.json>` with its default five-second tolerance: **exit 0, 335 quotes, 0 failures**. The input contained all 194 current assembled records; the script checks their `evidence` arrays. This is a new current-assembly result, distinct from the historical 149-record/355-quote result above.
5. Parsed existing `supplement-pass2.json`: **8 entries**, exactly matching the eight non-supported supplement-record IDs. Converted their `pass2_evidence` to temporary `id`/`evidence` verifier input and ran the same existing script: **exit 0, 31 quotes, 0 failures**. Temporary verification inputs were removed. This verifies existing evidence, not a new blind pass or its model provenance.
6. Rechecked all **22 numbered omissions** against current summary and source transcript passages: **11 covered / 11 still omitted**. Partial or unclear full-item coverage remains omitted. See [omissions-recheck.md](omissions-recheck.md) for current claim IDs, summary section timestamps, source ranges and specific residual gaps.
7. Reran `queue_state.publishable(video_dir)`: **False**. Checked `git status --short -- videos/` and `git diff --stat 47c72ce -- videos/`: **both empty**. Source video files, summary and transcript remain unchanged.

### Retained classifications and pass-2 disagreement

The 105 supplement records retain **97 supported, 2 attribution_qualification, 6 unresolved**. The 89 remapped records are supported; assembled current classes are **186 supported, 2 attribution_qualification, 6 unresolved**. No retained class was overwritten from a pass-2 opinion.

| Current ID | Retained class | Existing pass-2 class | Remaining question |
| --- | --- | --- | --- |
| c019 | attribution_qualification | supported | Simplified scalar V equation versus hypothetical sum of multivariable functions. |
| c055 | attribution_qualification | supported | Spoken 600/2000 comparison versus attribution/qualification of a US recommendation. Numerical omission 2 is covered, without adjudicating this class. |
| c068 | unresolved | mismatch | Caption's cell-division terminology versus the summary's normalization. |
| c080 | unresolved | unresolved | Article's exact optimum/range remains unclear in captions. |
| c087 | unresolved | unresolved | “dầu ôu” does not unambiguously establish olive oil. |
| c107 | unresolved | unresolved | “CL” and “Alla”/“Ala” chemical identities remain uncertain. |
| c163 | unresolved | attribution_qualification | Attribution of Alzheimer's improvement after a speaker-change marker. |
| c192 | unresolved | attribution_qualification | Speaker attribution of the general-checkup expansion/diabetes example. |

Thus **5 class disagreements** remain (c019, c055, c068, c163, c192); the other **3 entries agree on unresolved**. Agreement on unresolved does not resolve a claim, and the two supported pass-2 opinions do not clear retained non-supported classes. Human adjudication remains outstanding. These are current supplement entries; the earlier audit's historical disagreements are separate.

### Remaining risks and preserved scope

- Still-omitted items: **3, 4, 6, 7, 8, 10, 11, 12, 20, 21, 22**. Several are substantially covered in part. Counts assess each original item's full scope, including substantive details in its explanation, rather than just its title. The recheck specifies those distinctions.
- Quote verification establishes verbatim caption substrings and timestamp tolerance. It does not establish medical truth, resolve ASR or speaker ambiguity, or check summary section windows. No fresh full fidelity/section-window review was run; prior publication preconditions remain in force.
- Existing pass-2 files were inspected and their evidence verified. A separate `codex exec -m gpt-6.1-sol` invocation ran an independent blind pass 2 on all eight non-supported supplement records; its eight results are in `supplement-pass2.json` and were quote-verified. No supported-claim sample pass or opus invocation was run.
- The historical 160-claim mapping remains stale. Current completeness is established by the separate 89-remap/105-record assembly, not by promoting the older 49 incomplete review-tool records. The previous report's missing-supplement conclusion is superseded; the older artifacts themselves are unchanged.
- This invocation writes only `omissions-recheck.md`, appends a dated note to `audit-summary.md`, and updates this verification report. Pre-existing workspace edits are preserved. `omissions.md`, supplement files, original audit/raw files and source videos/summary/transcript are untouched. The pending human-approval omission file was neither inspected nor changed. Publication remains blocked.

## 2026-10-20 — transcript-fidelity evidence addendum (no adjudication)

See [fresh-context continuation](../../continuation-transcript-fidelity.md) and [correction proposals](proposed-corrections-fidelity.md). Current summary/transcript SHA-256 values still match omissions-recheck.md; a full audit rerun is not required merely to resume.

- c068: additional blind audio-ASR evidence is available ("gián phân", "bốn bào tử"); human confirmation and exact correction approval pending. Written-transcript mismatch remains.
- c163: the `>>` marker is an ASR cue, not proof of a speaker change. The YouTube transcript panel omits it. Acoustic/visual evidence suggests continuous speech, but does not independently establish speaker identity. Prior marker-only rationale must be revisited; no supported classification recorded.
- c192 and omission 20: attribution remains unresolved, not cleared by findings on c163. Omission 4 identity likewise remains unresolved.
- Other classification/omission proposals remain pending and have not been rerun in this addendum. Distinguish substantive coverage from unresolved fidelity/identity, rather than treating every fidelity concern as a missing topic.

No historical records, class decisions, source content or publication flags were replaced.
