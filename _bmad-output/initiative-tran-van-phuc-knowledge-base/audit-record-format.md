# Audit record format

Outputs live in the spec's sibling `audit/<video_id>/` (never under `videos/`).

## Claim record (one per claim from current `fidelity.extract_claims`)

| field | content |
|---|---|
| id | `c001…` from current extraction (not from old review.md) |
| section | summary section heading containing the claim |
| claim | exact summary text, unmodified |
| evidence | verbatim transcript quote(s), with `[hh:mm:ss]` caption timestamp; empty if none |
| speaker | who says it in the transcript (doctor, guest, quoted source) vs how the summary attributes it |
| class | `supported` · `mismatch` · `attribution_qualification` · `unresolved` |
| note | one line: why; for attribution_qualification name the dropped/hardened hedge or speaker |

## Classes

- **supported**: quote backs claim, speaker and qualifiers (hedges, conditions, "có thể", dosage/population limits) intact.
- **mismatch**: transcript contradicts or says something materially different (number, direction, entity).
- **attribution_qualification**: content present but speaker misattributed, or a qualification dropped, hardened or added.
- **unresolved**: no evidence found by retrieval, or ambiguous. Stays unresolved until the full transcript has been read for it; only then may it become mismatch (absent from transcript) or another class.

## Omissions

Per video: topic, transcript timestamp range, verbatim anchor quote, why important (one line). Small talk excluded.

## Proposed corrections (separate file `proposed-corrections.md`)

Per item: claim id, current text, proposed text, supporting quote+timestamp, status `pending-human-approval`. Nothing applied in this phase.

## Per-video summary

Counts per class, omission count, and a stated publication status: `blocked`.
