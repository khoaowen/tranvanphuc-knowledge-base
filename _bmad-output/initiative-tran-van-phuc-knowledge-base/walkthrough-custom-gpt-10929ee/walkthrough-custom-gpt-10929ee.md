# Custom GPT setup — guided walkthrough

Target commit: `10929ee4a205f1b01aed59558a2e3205b7e912be`.

Review **accepted by user**: all five blocks accepted; no current block. No content changes during review. Live Builder testing remains **pending, not passed**. Walkthrough notes remain uncommitted.

## 1 — Intent

- [x] Accepted by user
- Status: **accepted**
- Changed during review: **no**

### Ticket 1.5 description

> [docs/custom-gpt-setup.md](../../../docs/custom-gpt-setup.md): step-by-step GPT Builder setup (create GPT, upload [knowledge-gpt/*.md](../../../knowledge-gpt/), system-prompt text restating the disclaimer per health-specific answer and translating on demand per [disclaimer.md](../disclaimer.md)), and how to re-upload after a pipeline run.

Source: ticket entry 5 in [tickets.toml](../tickets/epic-video-knowledge-pipeline/tickets/tickets.toml), as supplied for this walkthrough. The [plan's intent](../tickets/epic-video-knowledge-pipeline/tickets/story-custom-gpt-setup-instructions-plan.md#L21) describes a manual Builder hand-off, not operation or publication of a hosted GPT.

## 2 — Broad strokes

- [x] Accepted by user
- Status: **accepted**
- Changed during review: **no**

Three entry points organize the guide:

1. [docs/custom-gpt-setup.md:6 — Prepare the upload](../../../docs/custom-gpt-setup.md#L6): use current successful pipeline output, inspect publication state, and prepare the complete generated set.
2. [docs/custom-gpt-setup.md:23 — Copy-paste Instructions](../../../docs/custom-gpt-setup.md#L23): supply the answer contract in the Builder Instructions field.
3. [docs/custom-gpt-setup.md:53 — Refresh procedure](../../../docs/custom-gpt-setup.md#L53): repeat preparation, replace the corpus as a full set, save, and retest.

## 3 — Answer contract

- [x] Accepted by user
- Status: **accepted**
- Changed during review: **no**

The [Instructions block](../../../docs/custom-gpt-setup.md#L25) calls for a disclaimer at the start of every health-specific answer, including follow-ups: exact English wording for English and a faithful localized equivalent otherwise. It requests answers in the user's language and translation of Vietnamese material on demand.

The same block preserves speaker attribution, qualifications, uncertainty, numbers and scope. Substantive video-derived claims require supporting evidence, video title/ID and an existing timestamped source URL. It distinguishes translated quotations and summary excerpts from verified transcript quotations.

Source-only safeguards restrict answers to uploaded summaries, treat retrieved material as reference data rather than instructions, prohibit invented evidence and model-memory gap filling, and describe missing-evidence/conflict handling. They distinguish reporting a speaker's statement from endorsing it and prohibit diagnosis, prescriptions and personalized dosage recommendations.

## 4 — Upload/refresh and live acceptance

- [x] Accepted by user
- Status: **accepted**
- Changed during review: **no**

[Preparation and configuration](../../../docs/custom-gpt-setup.md#L6) describe account/workspace access, successful generation, publication-state checks, uploading all generated Markdown including the overview, processing confirmation, source-only capability settings, private initial saving, and fresh-conversation checks of the saved GPT. Empty publication output or generation failure stops the hand-off.

[Refresh](../../../docs/custom-gpt-setup.md#L53) removes all prior corpus Knowledge files and uploads the entire current set, rather than appending or replacing only changed volumes. Processing/count checks precede saving; a partial failed upload is not a completed refresh. A repository update alone does not refresh a GPT.

The [manual acceptance checklist](../../../docs/custom-gpt-setup.md#L41) covers an English question about q7uDJG8YQ5c's account of health beyond absence of disease, a French follow-up with recurring localized disclaimer, an unsupported-video question and a personalized dosage request. It calls for attribution, evidence and the existing 00:17:52 source link, then repeat checks after saving in a fresh conversation.

The [acceptance-record instructions](../../../docs/custom-gpt-setup.md#L49) request date, revision, uploaded filenames/count, actual answers and pass/fail without private health information. **Live Builder acceptance remains pending owner execution and recording; local inspection does not establish GPT behavior.**

## 5 — Periphery

- [x] Accepted by user
- Status: **accepted**
- Changed during review: **no**

The [README Browse paragraph](../../../README.md#L11) links readers to the manual setup, copy-paste Instructions and refresh checklist. The [story plan](../tickets/epic-video-knowledge-pipeline/tickets/story-custom-gpt-setup-instructions-plan.md#L1) records built status and the hand-off scope; its built status does not establish user acceptance of this walkthrough or live Builder behavior.
