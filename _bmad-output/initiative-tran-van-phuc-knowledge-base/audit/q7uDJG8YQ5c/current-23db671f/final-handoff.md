# Human handoff — q7uDJG8YQ5c current-summary audit

**Current status: full audit accepted; all 19 correction wordings and the optional paragraph approved, NOT applied. Publication remains blocked.** See [human-approvals.md](human-approvals.md) for the explicit approval, hash-bound snapshots and exact wording-version selections (replacement texts for p004 and p020). **Application is now explicitly authorized for these exact 20 wordings, but has not yet been performed.** See the latest authorization at the top of the approval ledger; no further application-approval question is needed unless a genuinely new ambiguity arises.

The sections below preserve the original pre-approval handoff. Their pending-status and no-application-authorization statements are historical and superseded by the human approval ledger. Apply only within its latest explicit scope; publication remains unauthorized.

## Read these files

1. [Consolidated audit](consolidated-audit.md): scope, binding, 210-claim index, preserved opinions, close calls and process caveats.
2. [Consolidated records](consolidated-claims.json): exact 210 current claims, timestamped verbatim evidence, and separate first/second/advisory classifications.
3. [Correction proposals](proposed-corrections.md), using the authoritative wording-version map below, together with [independent review](correction-wording-review.md) and [replacement review](correction-replacements-review.md).
4. [Omission pass](omissions.md): full-transcript coverage map and optional o001.
5. [Final mechanical verification](verification.md): coverage, exact extraction, quote checks, unchanged hashes and read-only publication checks.

## Results and acceptance boundary

- First pass: 210/210 claims; independent rechecks: 70/70 queued claims, covering every non-supported finding and flagged supported claim.
- Twenty-one first/second-pass class disagreements are preserved; [Opus advisory adjudication](adjudication-recommendations.md) weighs their union with residual non-supported findings, 29 targets total.
- Merged advisory recommendations: **191 supported, 15 attribution_qualification, 4 unresolved, 0 mismatch**. Every consolidated record remains `pending-human-acceptance`.
- Unresolved: c092 (oil-name ASR), c112 (LA/ALA direction conflict), c115 and c175 (speaker uncertainty). Proposed literal/non-attributed text does not resolve the underlying source uncertainty; stronger evidence would require audio verification.
- One fully omitted knowledge-sharing subtopic, o001, is retained as **optional / low priority**, not a health/product-selection omission.
- Close calls and the bounded added-name/English-expansion policy caveat remain explicit. No global consistency claim is made about analogous non-target names or glossary expansions. Human acceptance may select or override advisory recommendations without rewriting historical opinions.

## Exact correction versions eligible for human consideration

All items below are **pending-human-approval**. A model approve means only an independent source-fidelity check; it is not permission to apply or publish.

| Proposal | Claim/topic | Text to consider | Independent wording result |
|---|---|---|---|
| p001 | c010 | `proposed-corrections.md` → `proposed_text` | approve |
| p002 | c012 | `proposed-corrections.md` → `proposed_text` | approve |
| p003 | c016 | `proposed-corrections.md` → `proposed_text` | approve |
| p004 | c024 | **`correction-replacements-review.md` → `candidate_text`** | approve replacement |
| p005 | c030 | `proposed-corrections.md` → `proposed_text` | approve |
| p006 | c047 | `proposed-corrections.md` → `proposed_text` | approve |
| p007 | c051 | `proposed-corrections.md` → `proposed_text` | approve |
| p008 | c052 | `proposed-corrections.md` → `proposed_text` | approve |
| p009 | c064 | `proposed-corrections.md` → `proposed_text` | approve |
| p010 | c065 | `proposed-corrections.md` → `proposed_text` | approve |
| p011 | c068 | `proposed-corrections.md` → `proposed_text` | approve |
| p012 | c076 | `proposed-corrections.md` → `proposed_text` | approve |
| p013 | c092 | `proposed-corrections.md` → `proposed_text` | approve literal/uncertainty handling |
| p014 | c112 | `proposed-corrections.md` → `proposed_text` | approve literal/uncertainty handling |
| p015 | c115 | `proposed-corrections.md` → `proposed_text` | approve non-attributed wording |
| p016 | c122 | `proposed-corrections.md` → `proposed_text` | approve |
| p017 | c165 | `proposed-corrections.md` → `proposed_text` | approve |
| p018 | c175 | `proposed-corrections.md` → `proposed_text` | approve non-attributed wording |
| p019 | c208 | `proposed-corrections.md` → `proposed_text` | approve |
| p020 | o001, optional | **`correction-replacements-review.md` → `candidate_text`** | approve replacement |

**Do not select the original p004 or p020 wording from `proposed-corrections.md`.** Those originals were rejected and remain as historical evidence. p004's approved alternative places the quoted words at the hospital visit, not at a narrated farewell meal, and preserves prognosis rather than claiming actual survival/death. p020's approved alternative preserves the doctor's self-improvement statement as personal, not a universal rule about all sharers. The replacement texts exactly match the prior review's suggested alternatives and have now received their own independent literal check.

There are **19 claim-correction candidates and one optional insertion**, with 18 approved original texts and two approved replacement texts. No supported-claim precision edits, heading changes, glossary changes, audio checks, or canonical-expansion policy decisions are silently included in an application authorization. Those remain separate human decisions.

## Preservation and publication

Completed c001–c090 and every subsequent completed batch were preserved, not restarted. Original first/second/draft/advisory opinions remain in separate files; the invalid draft anchors are disclosed and excluded from the canonical completed evidence set. Input hashes are unchanged, fresh extraction exactly matches all 210 saved records, and `videos/` has no diff against HEAD. Existing publication gates for both specified videos return false. The pre-existing `deferred-work.md` edit was not modified.

No summary/transcript/review/progress/tool/publication edits, corrections, commits, pushes, deletes or migrations were applied. The original no-outside-files constraint was not perfectly met by historical scratch and runtime/context-mode infrastructure; see `verification.md` and continuation for explicit process caveats. No cleanup was performed.

## Mandatory reminder at human audit acceptance

After the human accepts this hash-bound audit, and before the next work item, **offer a read-only BMad migration inventory and approval plan** for the deferred `bmad migrate method` work. Enumerate every evidence relocation and reference rewrite first. **Never migrate automatically.** Any commits, removals/deletions, reference rewrites or retired global-skill removal need separate explicit approval reconciled with the standing no-commit/no-delete directions. Preserve historical evidence and `deferred-work.md`.
