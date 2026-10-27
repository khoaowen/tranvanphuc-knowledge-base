# Final mechanical verification — current-23db671f

Result: **PASS for the designated completed evidence and approval-candidate versions.** Mechanical integrity does not establish medical truth, human acceptance, or publication clearance.

## Input binding

- Summary SHA-256: `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64`.
- Transcript SHA-256: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`.
- Extractor SHA-256: `cc570d0b53168ebce3027af755d5c2a91045faa2c4e8bd2a93f78dea2538da0d`.
- All four video-file hashes in `input-manifest.json`, including review and metadata, matched before and after final checks.
- Executing the existing extractor in memory against the current summary exactly regenerated all 210 saved records, including question and section-bound metadata. No extractor file was changed or bytecode written.

## Coverage and record integrity

- Seven designated completed first-pass artifacts: exactly c001–c210 once, in order. c091–c120 uses `pass1-c091-c120-completed.md`, not the preserved original draft.
- Five independent recheck artifacts: 70 unique records, exactly the queued non-supported and flagged-supported IDs. Every first-pass non-supported claim has an independent recheck.
- All 21 first/second-pass class disagreements remain preserved. Their union with the 15 second-pass non-supported IDs is exactly the 29 advisory adjudication targets.
- Consolidated JSON: 210 unique ordered records; exact claim and section strings; allowed classes; all seven canonical fields exactly equal the designated source record. First-pass, second-pass and advisory class metadata were checked against those artifacts. Every disposition remains `pending-human-acceptance`.
- Consolidated advisory counts: 191 supported, 15 attribution_qualification, 4 unresolved, 0 mismatch. These are recommendations, not accepted dispositions.

## Timestamped verbatim evidence checks

Each nonempty quote was checked as a literal substring of an actual transcript line bearing its cited timestamp; repeated timestamps were handled. No whitespace normalization or fuzzy match was used.

| Artifact group | Matching quote occurrences | Failures |
|---|---:|---:|
| Designated completed first passes | 2,024 | 0 |
| Independent second passes | 774 | 0 |
| Advisory adjudication | 286 | 0 |
| Consolidated claim records | 1,894 | 0 |
| Original correction proposals | 188 | 0 |
| Independent correction-wording review | 194 | 0 |
| Independent replacement-wording review | 51 | 0 |
| Omission candidate | 12 | 0 |

These counts include evidence repeated across artifacts; they are not counts of distinct transcript passages. The original c091–c120 draft is deliberately excluded from the passing completed set: it contains three known invalid timestamp anchors, remains preserved, and is not a canonical evidence source.

## Omission and correction versions

- o001: unique omission ID, ordered timestamp range, all anchors inside its range, status `pending-human-approval`. Full-transcript coverage-map quotations: 108/108 exact substrings of the current summary.
- Twenty original proposal IDs p001–p020 occur exactly once, with exact current claim text for the 19 claim corrections. Their claim-ID set equals the 19 non-supported consolidated advisory records; o001 is the separate optional insertion.
- Independent review targets exactly match all 20 original proposal texts and claim IDs. Eighteen originals received model approve; p004 and p020 received model reject.
- Replacement review contains exactly p004 and p020. Each `candidate_text` exactly equals the prior review's `replacement_text`; both received independent model approve. All records still say `pending-human-approval`.
- For human consideration, use the 18 approved original texts plus the two approved replacement texts, **not the rejected originals**. See `final-handoff.md` for the version map. No proposal was applied.

## Publication and repository boundaries

Read-only calls to existing `queue_state.publishable` returned **false** for both q7uDJG8YQ5c and V-Qfwjo28Zg. This is not an audit of V-Qfwjo28Zg and does not refresh either review.

`git diff HEAD -- videos/` was empty. `git status --short` showed only the pre-existing initiative `deferred-work.md` modification and the untracked `current-23db671f/` audit folder. No commit, push, publication, migration, delete, source correction, review/progress update or tool modification was performed.

## Method and limitations

Parent verification processed files in memory through context-mode tools. An initial queue-state check stopped because the in-memory module lacked `__file__`; the check was corrected by supplying the real module path, and both read-only publication checks and final hash/repository checks passed. Earlier claim/proposal/omission checks had already passed before that setup error.

Context-mode creates runtime temporary scripts, and the subagent harness keeps infrastructure outside this audit folder. Earlier scratch-file violations and the historical failed anchors are disclosed in `continuation.md` and `consolidated-audit.md`. Perfect compliance with the original no-outside-files requirement is **not** claimed. No cleanup or deletion was authorized. Parent used context-mode repeatedly, not only once; older references to a single use are historical checkpoints, not a total-use assertion.

Full source-reading attestations belong to the named reader artifacts. Semantic close calls, source ASR/speaker uncertainty, the bounded canonical-name policy caveat, and all human decisions remain open as described in the consolidated audit. Mechanical PASS must not be read as human acceptance of any class or correction.
