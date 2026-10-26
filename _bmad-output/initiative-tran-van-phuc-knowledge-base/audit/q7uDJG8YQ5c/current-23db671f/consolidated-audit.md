# Consolidated advisory audit — q7uDJG8YQ5c (current summary 23db671f)

**Status: ADVISORY ASSEMBLY ONLY.** This file and `consolidated-claims.json` merge existing hash-bound artifacts. Every claim's `disposition_status` is `pending-human-acceptance`. **No human has accepted any disposition.** This is not a refreshed review verdict, not a pass/flag/fail result and not a publication decision. **Publication status: blocked.** Nothing has been applied to `videos/`.

## 1. Navigation

| artifact | role |
|---|---|
| `consolidated-claims.json` | 210 merged records. Canonical seven fields (id, section, claim, evidence, speaker, class, note) come from the advisory record when there is one, otherwise from the designated first-pass record. Each record also has `source_artifact`, `first_pass_class`, `second_pass_class`, `advisory_class`, `disposition_status` and `source_references` |
| `proposed-corrections.md` | DRAFT wording: 19 required claim corrections plus 1 optional omission (o001), all `pending-human-approval`. An independent literal-wording review follows |
| `adjudication-recommendations.md` | Opus advisory adjudication of 29 targets; its rationale is the reference for every advisory class |
| `pass1-*.md` (7 designated), `pass1-c091-c120.md` (historical draft) | First-pass records |
| `pass2-*-findings.md` (5) | Independent rechecks, 70 records |
| `omissions.md` | Full-transcript omission pass (o001) |
| `continuation.md`, `input-manifest.json`, `claims.json` | Process history, bindings and extraction (210 claims) |

Artifact codes used below: P1-A `pass1-c001-c030.md`, P1-B `pass1-c031-c060.md`, P1-C `pass1-c061-c090.md`, P1-D `pass1-c091-c120-completed.md`, P1-E `pass1-c121-c150.md`, P1-F `pass1-c151-c180.md`, P1-G `pass1-c181-c210.md`, DRAFT `pass1-c091-c120.md` (original draft, preserved; contains three historical invalid anchors at c105, c106 and c112, which the completed file repairs), P2-A `pass2-c001-c030-findings.md`, P2-B `pass2-c031-c090-findings.md`, P2-C `pass2-c091-c120-findings.md`, P2-D `pass2-c121-c180-findings.md`, P2-E `pass2-c181-c210-findings.md`, ADJ `adjudication-recommendations.md`. Every JSON record also lists `claims.json` in `source_references`.

## 2. Bindings (re-verified before assembly)

| file | SHA-256 | result |
|---|---|---|
| summary.md | `23db671f7ffecac43155de9c2e27610328ebbd14a019ebf446d7ee52a4df4f64` | match |
| transcript.md | `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b` | match |
| review.md (hashed only, not used as evidence) | `5f588b23bda088c0e74837dffea6a452510af878299cc4950f25e594f7840a41` | match |
| metadata.json | `c3f19953b8499eb724aa0b8d3126a83b94249c8df83b52951c0d8b429de76dcd` | match |
| scripts/fidelity.py (extractor) | `cc570d0b53168ebce3027af755d5c2a91045faa2c4e8bd2a93f78dea2538da0d` | match |

## 3. Counts (provisional; none accepted)

| class | first pass (210) | second pass (70 rechecked) | advisory targets (29) | merged advisory aggregate (210) |
|---|---|---|---|---|
| supported | 187 | 55 | 10 | **191** |
| attribution_qualification | 14 | 9 | 15 | **15** |
| unresolved | 9 | 6 | 4 | **4** |
| mismatch | 0 | 0 | 0 | **0** |

- Merge rule: the advisory class where an advisory record exists (29 claims), otherwise the first-pass class (181 claims). All 181 non-target claims are first-pass `supported`. 41 of them were also rechecked `supported` in the second pass (flagged-supported rechecks).
- Draft c091–c120 (historical) differs from the completed first pass on c092, c096, c110 and c116 (draft `supported`, completed `unresolved`).
- First/second-pass class disagreements: **21** (c003, c004, c010, c016, c024, c030, c034, c037, c047, c051, c052, c064, c065, c068, c072, c076, c110, c115, c116, c120, c167). All three views are preserved in their own artifacts. The advisory explanation for each is in ADJ §5–§6, by reference.
- Advisory targets: **29**, the 21 disagreements plus the 8 claims both passes marked non-supported (c012, c092, c096, c112, c122, c165, c175, c208). See ADJ for rationale. Close calls where a human could reasonably take the other side: c037, c065, c068, c096, c120, c167.
- Non-supported advisory claims (19): c010, c012, c016, c024, c030, c047, c051, c052, c064, c065, c068, c076, c092, c112, c115, c122, c165, c175, c208. Draft wording for each is in `proposed-corrections.md` (p001–p019).

## 4. Open items requiring human choice

1. **Unresolved literal or audio choices (4):** c092 (oil token "ôu"), c112 (la/Alla/Ala inflammation direction), c115 (alcohol-analogy speaker), c175 (Alzheimer-clause speaker). The text cannot settle any of them. The options are an audio check or explicit literal wording that names no speaker (p013, p014, p015, p018).
2. **Canonical-name policy caveat (bounded adjudication):** ADJ applied a strict policy to its 29 targets. Phonetic normalization of a spoken token was accepted (Mozart←Moa, Lipton←Lip Tông, lupus←lú bút). Unspoken given names or English expansions were not (Kurt, Wolfgang Amadeus, Bruce, Re-esterified Triglyceride → c010, c016, c064 and c165 are AQ). **Analogous non-target claims were not re-adjudicated and remain first-pass `supported`.** Examples are c017 ("Ludwig van Beethoven") and c018 ("Immanuel Kant"). The same applies to the 01:35:27 section heading and question ("Bruce Lipton"), which sit outside the 210 claim records, and to the glossary expansions. **This audit claims no global consistency.** If the human adopts a canonical-expansion policy, c010, c016, c064 and c165 become `supported` together. If the human keeps the strict policy, the analogous non-target claims need a separate, explicit decision.
3. **Omission o001 (optional):** reciprocal knowledge-sharing and anti-secrecy principle extended to fellow doctors (00:21:03–00:22:50). It is confirmed present in the source and absent from the summary. Priority is optional and low. The draft insertion is p020, which uses the corrected wording "tìm đến **để tìm hiểu**" in place of "tìm đến trao đổi". Status: pending-human-approval.
4. **Outside the 210 claims (separate decisions, not automatic corrections):** section heading and question strings, glossary rows, the DHA editorial note, and the optional precision edits on advisory-`supported` claims (c003, c004, c034, c037, c072, c096, c110, c120, c167). See `proposed-corrections.md` §3.

## 5. 210-claim index

Columns: first-pass class, draft class (c091–c120 only), second-pass class, advisory class, **merged class**, artifact supplying the canonical fields, all opinion artifacts, and flags (`1≠2` = first/second-pass class disagreement; `draft≠1` = draft vs completed first pass). S = supported, AQ = attribution_qualification, U = unresolved, — = no record. Section is given by its timestamp heading. Every row's status is pending-human-acceptance.

| id | section | P1 | draft | P2 | ADJ | merged | canonical from | references | flags |
|---|---|---|---|---|---|---|---|---|---|
| c001 | 00:00:15 | S | — | — | — | **S** | P1-A | P1-A |  |
| c002 | 00:00:15 | S | — | — | — | **S** | P1-A | P1-A |  |
| c003 | 00:00:15 | S | — | AQ | S | **S** | ADJ | P1-A, P2-A, ADJ | 1≠2 |
| c004 | 00:00:15 | S | — | AQ | S | **S** | ADJ | P1-A, P2-A, ADJ | 1≠2 |
| c005 | 00:08:55 | S | — | — | — | **S** | P1-A | P1-A |  |
| c006 | 00:08:55 | S | — | — | — | **S** | P1-A | P1-A |  |
| c007 | 00:08:55 | S | — | — | — | **S** | P1-A | P1-A |  |
| c008 | 00:08:55 | S | — | — | — | **S** | P1-A | P1-A |  |
| c009 | 00:23:00 | S | — | — | — | **S** | P1-A | P1-A |  |
| c010 | 00:23:00 | S | — | AQ | AQ | **AQ** | ADJ | P1-A, P2-A, ADJ | 1≠2 |
| c011 | 00:23:00 | S | — | — | — | **S** | P1-A | P1-A |  |
| c012 | 00:23:00 | AQ | — | AQ | AQ | **AQ** | ADJ | P1-A, P2-A, ADJ |  |
| c013 | 00:31:36 | S | — | — | — | **S** | P1-A | P1-A |  |
| c014 | 00:31:36 | S | — | — | — | **S** | P1-A | P1-A |  |
| c015 | 00:31:36 | S | — | — | — | **S** | P1-A | P1-A |  |
| c016 | 00:31:36 | S | — | AQ | AQ | **AQ** | ADJ | P1-A, P2-A, ADJ | 1≠2 |
| c017 | 00:31:36 | S | — | — | — | **S** | P1-A | P1-A | name-policy caveat |
| c018 | 00:31:36 | S | — | — | — | **S** | P1-A | P1-A | name-policy caveat |
| c019 | 00:34:05 | S | — | — | — | **S** | P1-A | P1-A |  |
| c020 | 00:34:05 | S | — | — | — | **S** | P1-A | P1-A |  |
| c021 | 00:34:05 | S | — | — | — | **S** | P1-A | P1-A |  |
| c022 | 00:34:05 | S | — | — | — | **S** | P1-A | P1-A |  |
| c023 | 00:34:05 | S | — | — | — | **S** | P1-A | P1-A |  |
| c024 | 00:34:05 | S | — | AQ | AQ | **AQ** | ADJ | P1-A, P2-A, ADJ | 1≠2 |
| c025 | 00:34:05 | S | — | — | — | **S** | P1-A | P1-A |  |
| c026 | 00:34:05 | S | — | — | — | **S** | P1-A | P1-A |  |
| c027 | 00:49:35 | S | — | — | — | **S** | P1-A | P1-A |  |
| c028 | 00:49:35 | S | — | — | — | **S** | P1-A | P1-A |  |
| c029 | 00:49:35 | S | — | — | — | **S** | P1-A | P1-A |  |
| c030 | 00:49:35 | S | — | AQ | AQ | **AQ** | ADJ | P1-A, P2-A, ADJ | 1≠2 |
| c031 | 00:58:42 | S | — | — | — | **S** | P1-B | P1-B |  |
| c032 | 00:58:42 | S | — | — | — | **S** | P1-B | P1-B |  |
| c033 | 00:58:42 | S | — | — | — | **S** | P1-B | P1-B |  |
| c034 | 00:58:42 | AQ | — | S | S | **S** | ADJ | P1-B, P2-B, ADJ | 1≠2 |
| c035 | 00:58:42 | S | — | — | — | **S** | P1-B | P1-B |  |
| c036 | 01:03:00 | S | — | — | — | **S** | P1-B | P1-B |  |
| c037 | 01:03:00 | AQ | — | S | S | **S** | ADJ | P1-B, P2-B, ADJ | 1≠2 |
| c038 | 01:03:00 | S | — | — | — | **S** | P1-B | P1-B |  |
| c039 | 01:07:33 | S | — | — | — | **S** | P1-B | P1-B |  |
| c040 | 01:07:33 | S | — | — | — | **S** | P1-B | P1-B |  |
| c041 | 01:07:33 | S | — | — | — | **S** | P1-B | P1-B |  |
| c042 | 01:07:33 | S | — | — | — | **S** | P1-B | P1-B |  |
| c043 | 01:07:33 | S | — | — | — | **S** | P1-B | P1-B |  |
| c044 | 01:12:00 | S | — | — | — | **S** | P1-B | P1-B |  |
| c045 | 01:12:00 | S | — | — | — | **S** | P1-B | P1-B |  |
| c046 | 01:12:00 | S | — | — | — | **S** | P1-B | P1-B |  |
| c047 | 01:12:00 | AQ | — | S | AQ | **AQ** | ADJ | P1-B, P2-B, ADJ | 1≠2 |
| c048 | 01:20:24 | S | — | — | — | **S** | P1-B | P1-B |  |
| c049 | 01:20:24 | S | — | — | — | **S** | P1-B | P1-B |  |
| c050 | 01:20:24 | S | — | — | — | **S** | P1-B | P1-B |  |
| c051 | 01:20:24 | AQ | — | S | AQ | **AQ** | ADJ | P1-B, P2-B, ADJ | 1≠2 |
| c052 | 01:20:24 | AQ | — | S | AQ | **AQ** | ADJ | P1-B, P2-B, ADJ | 1≠2 |
| c053 | 01:20:24 | S | — | — | — | **S** | P1-B | P1-B |  |
| c054 | 01:20:24 | S | — | — | — | **S** | P1-B | P1-B |  |
| c055 | 01:20:24 | S | — | — | — | **S** | P1-B | P1-B |  |
| c056 | 01:25:23 | S | — | — | — | **S** | P1-B | P1-B |  |
| c057 | 01:25:23 | S | — | — | — | **S** | P1-B | P1-B |  |
| c058 | 01:25:23 | S | — | — | — | **S** | P1-B | P1-B |  |
| c059 | 01:25:23 | S | — | S | — | **S** | P1-B | P1-B, P2-B |  |
| c060 | 01:25:23 | S | — | — | — | **S** | P1-B | P1-B |  |
| c061 | 01:25:23 | S | — | — | — | **S** | P1-C | P1-C |  |
| c062 | 01:25:23 | S | — | — | — | **S** | P1-C | P1-C |  |
| c063 | 01:25:23 | S | — | — | — | **S** | P1-C | P1-C |  |
| c064 | 01:35:27 | AQ | — | U | AQ | **AQ** | ADJ | P1-C, P2-B, ADJ | 1≠2 |
| c065 | 01:35:27 | AQ | — | S | AQ | **AQ** | ADJ | P1-C, P2-B, ADJ | 1≠2 |
| c066 | 01:35:27 | S | — | — | — | **S** | P1-C | P1-C | heading caveat |
| c067 | 01:35:27 | S | — | — | — | **S** | P1-C | P1-C | heading caveat |
| c068 | 01:42:36 | AQ | — | S | AQ | **AQ** | ADJ | P1-C, P2-B, ADJ | 1≠2 |
| c069 | 01:42:36 | S | — | — | — | **S** | P1-C | P1-C |  |
| c070 | 01:42:36 | S | — | — | — | **S** | P1-C | P1-C |  |
| c071 | 01:42:36 | S | — | — | — | **S** | P1-C | P1-C |  |
| c072 | 01:42:36 | AQ | — | S | S | **S** | ADJ | P1-C, P2-B, ADJ | 1≠2 |
| c073 | 01:47:01 | S | — | — | — | **S** | P1-C | P1-C |  |
| c074 | 01:47:01 | S | — | — | — | **S** | P1-C | P1-C |  |
| c075 | 01:47:01 | S | — | — | — | **S** | P1-C | P1-C |  |
| c076 | 01:47:01 | AQ | — | S | AQ | **AQ** | ADJ | P1-C, P2-B, ADJ | 1≠2 |
| c077 | 01:47:01 | S | — | — | — | **S** | P1-C | P1-C |  |
| c078 | 01:47:01 | S | — | S | — | **S** | P1-C | P1-C, P2-B |  |
| c079 | 01:47:01 | S | — | — | — | **S** | P1-C | P1-C |  |
| c080 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c081 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c082 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c083 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c084 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c085 | 01:53:28 | S | — | S | — | **S** | P1-C | P1-C, P2-B |  |
| c086 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c087 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c088 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c089 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c090 | 01:53:28 | S | — | — | — | **S** | P1-C | P1-C |  |
| c091 | 01:53:28 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c092 | 01:53:28 | U | S | U | U | **U** | ADJ | P1-D, DRAFT, P2-C, ADJ | draft≠1 |
| c093 | 01:53:28 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c094 | 01:53:28 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c095 | 01:53:28 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c096 | 02:00:15 | U | S | U | S | **S** | ADJ | P1-D, DRAFT, P2-C, ADJ | draft≠1 |
| c097 | 02:00:15 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c098 | 02:00:15 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c099 | 02:00:15 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c100 | 02:00:15 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c101 | 02:00:15 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c102 | 02:00:15 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c103 | 02:08:28 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c104 | 02:08:28 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c105 | 02:08:28 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C | draft anchor invalid (repaired in P1-D) |
| c106 | 02:08:28 | S | S | — | — | **S** | P1-D | P1-D, DRAFT | draft anchor invalid (repaired in P1-D) |
| c107 | 02:08:28 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c108 | 02:08:28 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c109 | 02:08:28 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c110 | 02:08:28 | U | S | S | S | **S** | ADJ | P1-D, DRAFT, P2-C, ADJ | 1≠2 draft≠1 |
| c111 | 02:08:28 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c112 | 02:08:28 | U | U | U | U | **U** | ADJ | P1-D, DRAFT, P2-C, ADJ | draft anchor invalid (repaired in P1-D) |
| c113 | 02:08:28 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c114 | 02:08:28 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c115 | 02:08:28 | U | U | S | U | **U** | ADJ | P1-D, DRAFT, P2-C, ADJ | 1≠2 |
| c116 | 02:23:30 | U | S | S | S | **S** | ADJ | P1-D, DRAFT, P2-C, ADJ | 1≠2 draft≠1 |
| c117 | 02:23:30 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c118 | 02:23:30 | S | S | S | — | **S** | P1-D | P1-D, DRAFT, P2-C |  |
| c119 | 02:23:30 | S | S | — | — | **S** | P1-D | P1-D, DRAFT |  |
| c120 | 02:23:30 | U | U | S | S | **S** | ADJ | P1-D, DRAFT, P2-C, ADJ | 1≠2 |
| c121 | 02:23:30 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c122 | 02:23:30 | AQ | — | AQ | AQ | **AQ** | ADJ | P1-E, P2-D, ADJ |  |
| c123 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c124 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c125 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c126 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c127 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c128 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c129 | 02:23:30 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c130 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c131 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c132 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c133 | 02:23:30 | S | — | — | — | **S** | P1-E | P1-E |  |
| c134 | 02:23:30 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c135 | 02:23:30 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c136 | 02:23:30 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c137 | 02:37:13 | S | — | — | — | **S** | P1-E | P1-E |  |
| c138 | 02:37:13 | S | — | — | — | **S** | P1-E | P1-E |  |
| c139 | 02:37:13 | S | — | — | — | **S** | P1-E | P1-E |  |
| c140 | 02:37:13 | S | — | — | — | **S** | P1-E | P1-E |  |
| c141 | 02:39:11 | S | — | — | — | **S** | P1-E | P1-E |  |
| c142 | 02:39:11 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c143 | 02:39:11 | S | — | — | — | **S** | P1-E | P1-E |  |
| c144 | 02:39:11 | S | — | — | — | **S** | P1-E | P1-E |  |
| c145 | 02:39:11 | S | — | — | — | **S** | P1-E | P1-E |  |
| c146 | 02:39:11 | S | — | — | — | **S** | P1-E | P1-E |  |
| c147 | 02:39:11 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c148 | 02:39:11 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c149 | 02:41:46 | S | — | S | — | **S** | P1-E | P1-E, P2-D |  |
| c150 | 02:41:46 | S | — | — | — | **S** | P1-E | P1-E |  |
| c151 | 02:41:46 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c152 | 02:41:46 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c153 | 02:41:46 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c154 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c155 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c156 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c157 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c158 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c159 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c160 | 02:46:03 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c161 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c162 | 02:46:03 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c163 | 02:46:03 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c164 | 02:46:03 | S | — | — | — | **S** | P1-F | P1-F |  |
| c165 | 02:46:03 | U | — | U | AQ | **AQ** | ADJ | P1-F, P2-D, ADJ |  |
| c166 | 02:46:03 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c167 | 02:46:03 | AQ | — | S | S | **S** | ADJ | P1-F, P2-D, ADJ | 1≠2 |
| c168 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c169 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c170 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c171 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c172 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c173 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c174 | 03:01:21 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c175 | 03:01:21 | U | — | U | U | **U** | ADJ | P1-F, P2-D, ADJ |  |
| c176 | 03:01:21 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c177 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c178 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c179 | 03:01:21 | S | — | — | — | **S** | P1-F | P1-F |  |
| c180 | 03:01:21 | S | — | S | — | **S** | P1-F | P1-F, P2-D |  |
| c181 | 03:09:08 | S | — | S | — | **S** | P1-G | P1-G, P2-E |  |
| c182 | 03:09:08 | S | — | S | — | **S** | P1-G | P1-G, P2-E |  |
| c183 | 03:09:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c184 | 03:09:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c185 | 03:09:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c186 | 03:13:11 | S | — | S | — | **S** | P1-G | P1-G, P2-E |  |
| c187 | 03:13:11 | S | — | — | — | **S** | P1-G | P1-G |  |
| c188 | 03:13:11 | S | — | — | — | **S** | P1-G | P1-G |  |
| c189 | 03:13:11 | S | — | — | — | **S** | P1-G | P1-G |  |
| c190 | 03:13:11 | S | — | — | — | **S** | P1-G | P1-G |  |
| c191 | 03:13:11 | S | — | — | — | **S** | P1-G | P1-G |  |
| c192 | 03:13:11 | S | — | — | — | **S** | P1-G | P1-G |  |
| c193 | 03:13:11 | S | — | S | — | **S** | P1-G | P1-G, P2-E |  |
| c194 | 03:13:11 | S | — | — | — | **S** | P1-G | P1-G |  |
| c195 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c196 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c197 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c198 | 03:19:08 | S | — | S | — | **S** | P1-G | P1-G, P2-E |  |
| c199 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c200 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c201 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c202 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c203 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c204 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c205 | 03:19:08 | S | — | — | — | **S** | P1-G | P1-G |  |
| c206 | 03:19:08 | S | — | S | — | **S** | P1-G | P1-G, P2-E |  |
| c207 | 03:19:08 | S | — | S | — | **S** | P1-G | P1-G, P2-E |  |
| c208 | 03:19:08 | AQ | — | AQ | AQ | **AQ** | ADJ | P1-G, P2-E, ADJ |  |
| c209 | 03:28:17 | S | — | — | — | **S** | P1-G | P1-G |  |
| c210 | 03:28:17 | S | — | — | — | **S** | P1-G | P1-G |  |

## 6. Process caveats (from `continuation.md`; not resolved by this assembly)

- **Historical scratch and runtime locations outside the audit folder:** earlier child reports disclosed scratch verification files under `/tmp/p2/` and `/tmp/q7aud/`. Runtime-managed infrastructure exists under `/tmp/pi-subagents-uid-1001/async-subagent-runs/…`. Context-mode runs created sandbox scripts (`/tmp/.ctx-mode-…/script.py`), and the parent used `ctx_execute_file` once. Perfect no-outside-files compliance is **not** claimed. None of these were deleted, by design.
- **Earlier failed anchors:** the original draft `pass1-c091-c120.md` had invalid timestamp anchors (c105 and c112 cited 02:14:01 instead of 02:14:02; c106 cited 02:15:31 instead of 02:15:29). The draft is preserved unchanged. `pass1-c091-c120-completed.md` repairs these anchors and is the designated first-pass source.
- **Rate, usage and runtime failures:** Anthropic HTTP 429 `rate_limit_error` stopped workflow `d1446330…` (request `req_011CgP464ynEhdH1KpvKZ3CF`) and child `a9a616e7…` (request `req_011CgP5hv39ESQKvUDMCDC7z`). A Codex usage limit failed child `0cf13843…`, and its native resume returned "Async run not found". The first launch was rejected locally because of an unsupported `options.tools` key. No retry loops were run. Same-protocol continuations were made only under explicit operator direction.
- **Model changes:** the first passes c001–c090 and pass2 c001–c030 ran on `anthropic/claude-opus-5-5`. After the second 429, the operator switched remaining readers to `openai-codex/gpt-6.1-sol`, which covered c091–c210 first passes, pass2 c031–c210 and omissions. The operator then directed a return to `anthropic/claude-opus-5-5` for the adjudication, for this assembly and for the planned independent wording review.
- **Label exposure:** some later rechecks report independence of rationale but not label-blindness, because the required continuation exposed prior labels.
- **This assembly's own process:** under a narrow supervisor-approved exception, `consolidated-claims.json` was serialized directly to its new final path by an in-memory `PYTHONDONTWRITEBYTECODE=1 python3` heredoc, as a byte-exact mechanical merge with no script, scratch or intermediate file. The two Markdown files were written with the Write tool. No other file was created or modified.

## 7. Human acceptance checkpoint (mandatory reminders)

- Nothing here is accepted. The human must explicitly accept or override each advisory class (`pending-human-acceptance`) and, separately, approve or reject each draft correction (`pending-human-approval`) after the independent literal-wording review.
- Publication remains **blocked**. Applying corrections, editing `summary.md`, refreshing `review.md` or `.review-progress.json`, and any commit, push or delete are all out of scope for this phase.
- **At human acceptance of this hash-bound audit, before the next work item:** remind the human about `bmad migrate method` and offer a **read-only BMad migration inventory and approval plan**. The plan should first list evidence relocations and reference rewrites, including this folder, the historical draft, the preserved scratch disclosures and `deferred-work.md`. **There must be no automatic migration, standard commits, removals, deletions or global-skill removal.** Each needs a separate explicit approval that reconciles it with the standing no-commit and no-delete directions.
