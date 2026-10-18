# Final claim mapping and audit of changed claims — q7uDJG8YQ5c (supplementary, supersedes claims-after-apply.md and split-claims-audit.*)

> corrections applied, uncommitted, video still blocked

Audit-time claims: 149. Current claims in summary.md: 160. Old records are not overwritten. Alignment is by exact claim text (difflib); ids are `fidelity.extract_claims` ids of the current summary.

- Unchanged claims: 111, each keeps its old audit record.
- Changed or new claims: 49, each has a record in `final-claims-audit.json` taken from the hash-bound opus review of the current summary (quotes verified as transcript substrings: 0 failures).
- Every current claim maps to a record (old or new); every old record is either mapped 1:1 (unchanged) or superseded by the listed new claims. No claim is dropped silently: a superseded old record with no new claim is shown as '-'.

## Changed blocks (old audit ids -> current ids)

| old audit ids | current ids | kind |
|---|---|---|
| c001..c001 | c001, c002 | replace |
| c012..c013 | c013, c014 | replace |
| c015..c015 | c016 | replace |
| c019..c020 | c020, c021, c022, c023 | replace |
| c029..c029 | c032 | replace |
| c036..c036 | c039 | replace |
| c045..c045 | c048 | replace |
| c056..c056 | c059 | replace |
| c060..c061 | c063, c064 | replace |
| c063..c071 | c066, c067, c068, c069, c070, c071, c072, c073, c074, c075, c076, c077 | replace |
| c076..c076 | c082 | replace |
| c085..c085 | c091 | replace |
| c087..c087 | c093 | replace |
| c106..c106 | c112 | replace |
| c108..c108 | c114 | replace |
| c110..c110 | c116 | replace |
| c113..c113 | c119 | replace |
| c119..c119 | c125 | replace |
| c123..c123 | c129 | replace |
| c126..c129 | c132, c133, c134, c135, c136 | replace |
| c135..c137 | c142, c143, c144, c145, c146, c147, c148 | replace |
| c146..c146 | c157 | replace |

## Status of changed claims in the opus review

| id | status | note |
|---|---|---|
| c001 | pass |  |
| c002 | fail | evidence found at 00:14:04-00:14:19, outside the section's timestamp window |
| c013 | pass |  |
| c014 | fail | evidence found at 00:46:29-00:46:35, outside the section's timestamp window |
| c016 | fail | evidence found at 00:46:05-00:46:07, outside the section's timestamp window |
| c020 | pass |  |
| c021 | pass |  |
| c022 | pass |  |
| c023 | pass |  |
| c032 | pass |  |
| c039 | pass |  |
| c048 | pass |  |
| c059 | pass |  |
| c063 | pass |  |
| c064 | pass |  |
| c066 | pass |  |
| c067 | pass |  |
| c068 | pass |  |
| c069 | pass |  |
| c070 | pass |  |
| c071 | pass |  |
| c072 | pass |  |
| c073 | pass |  |
| c074 | pass |  |
| c075 | pass |  |
| c076 | pass |  |
| c077 | pass |  |
| c082 | pass |  |
| c091 | pass |  |
| c093 | pass |  |
| c112 | pass |  |
| c114 | pass |  |
| c116 | fail | evidence found at 03:10:30, outside the section's timestamp window; evidence found at 03:10:30, outside the section's timestamp window |
| c119 | pass |  |
| c125 | pass |  |
| c129 | pass |  |
| c132 | pass |  |
| c133 | pass |  |
| c134 | pass |  |
| c135 | pass |  |
| c136 | pass |  |
| c142 | pass |  |
| c143 | pass |  |
| c144 | pass |  |
| c145 | pass |  |
| c146 | pass |  |
| c147 | pass |  |
| c148 | pass |  |
| c157 | pass |  |

fail = only 'evidence outside the section timestamp window' (tool rule), see apply-report.md.
