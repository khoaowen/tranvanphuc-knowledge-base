---
title: 'Generate structured summary'
type: 'feature'
ticket: '3'
created: '2026-10-10'
status: 'superseded'
baseline_revision: ''
route: 'full'
route_source: 'pinned'
risk: 'high'
review: 'thorough'
review_source: 'pinned'
lenses_ran: [adversarial, edge-case-hunter, structure, prose]
review_loop_iteration: 1
context:
  - '/Users/khoa/IdeaProjects/tranVanPhuc/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/spec-tran-van-phuc-kb.md'
  - '/Users/khoa/IdeaProjects/tranVanPhuc/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/repo-structure.md'
  - '/Users/khoa/IdeaProjects/tranVanPhuc/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/disclaimer.md'
  - '/Users/khoa/IdeaProjects/tranVanPhuc/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-tran-van-phuc-kb/pipeline-architecture.md'
---

> **SUPERSEDED 2026-10-11.** Paid Anthropic auditor, WIF and dollar caps (including this plan's frozen block) are renegotiated by the human under the $0 constraint. Kept for history only. Do not implement. Replaced by stories re-sliced from the amended spec.

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Vietnamese health transcripts need navigable summaries, but a plausible paraphrase can reverse a qualification, invent advice, or misattribute a host's words to the doctor. Incorrect summaries can propagate into a public medical-content knowledge base.

**Approach:** Build a fail-closed, evidence-bearing generator/auditor pipeline for CAP-3:

`immutable transcript -> timestamped segment parser -> deterministic input validation -> generator -> independent auditor -> deterministic evidence validator -> validated structured data -> Markdown renderer -> atomic summary.md write`

Use Gemini structured JSON generation (`GEMINI_MODEL`, default `gemini-3.6-flash`, official `google-genai` SDK). Use an independently invoked Claude auditor through the Anthropic API alongside Gemini; the exact auditor API model/version remains pending approval. Both evaluate fidelity solely against the raw Vietnamese transcript, not external knowledge. Model agreement does not prove medical correctness.

## Boundaries & Constraints

**Always:** Keep `transcript.md` byte-for-byte unchanged and metadata read-only. Retain Vietnamese evidence and summary content without a translation step. Distinguish a faithful transcription summary, what an explicitly identified speaker stated, and medically correct advice: this system produces only the first two and makes no claim about the third. Every key point, notable claim, and substantive overview statement must have precise timestamp ranges, verbatim Vietnamese quotes, immutable source references, explicit speaker attribution, and preserved uncertainty/qualifications. Use the canonical English disclaimer verbatim. Validate before rendering/publishing; never write partial or unaudited summaries. Keep the plan draft until human approval; this revision authorizes changes to the frozen block, not implementation.

**Never:** No search, grounding APIs, external fact-checking, correction, medical validation, personalized advice, translation, credential reuse from coding CLIs, or automatic medical “repair.” Do not assign all statements to Dr. Trần Văn Phúc by channel identity. Treat transcript instructions as untrusted quoted data, never system instructions. Models cannot write Markdown, files, or vocabulary. They cannot execute tools. Do not modify companion specifications or implement anything during this planning revision.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|---|---|---|---|
| Valid seed | `q7uDJG8YQ5c`, approved vocabulary and auditor configuration, valid credentials | Evidence-bearing Vietnamese `summary.md`, canonical disclaimer, tags, key points, claims | Exit 0 only after every gate passes |
| Long transcript / boundary claim | Timestamped segments exceed prompt budget | Overlapping segment chunks; evidence records survive synthesis; final raw-source audit | Fail video if context cannot fit safely within budgets |
| Invalid input | Empty/malformed/non-monotonic timestamps, unusable duration, decoding error | No model call or summary write | Non-retryable input code |
| Uncertain source | Inaudible text, ambiguous speaker/qualification, unresolved cross-passage reference | No guessed words or attribution; reject unsafe record | Fail video if required coverage is lost |
| Negative audit / evidence mismatch | Any non-supported verdict, fabricated quote, irrelevant timestamp, changed clinical scope | Exclude invalid records; never render them | Fail closed if required content cannot be validated |
| Unknown tag / absent vocabulary | Generated tag is not approved, no curated ledger | Do not silently seed or grow canonical tags | Require approval; fail if no valid tags remain |
| Provider fault | Timeout, transient 429/5xx versus authentication/quota failure | Bounded retries only for transient errors | Sanitized codes; no partial output |
| Mixed batch | At least one valid video and at least one failed video | Keep atomic successes, identify failures without content | Non-zero exit; Actions run remains failed |
| Existing summary / concurrent input change | Regeneration fails or source hash changes | Existing summary preserved, not treated as current success | No consolidation of stale/failed target |
| No inputs | No requested/discovered videos | Summarizer makes no model calls or writes; workflow still evaluates eligible corpus | Summarizer exits 0; consolidation/Actions fail without eligible corpus and preserve prior artifacts |

</frozen-after-approval>

## Human Decision Register

- **Approved by the user — auditor provider direction:** Use Claude through the Anthropic API as the preferred independent auditor alongside Gemini. This approves the provider direction only, not a specific Claude model/version, retention/training policy, pricing or budgets. No coding-CLI credentials or subscription-login reuse is allowed. The assistant recommends the Sonnet family as the initial candidate; that recommendation is not a measured Vietnamese-fidelity result or a user-approved model selection.
- **Approved by the user — exact auditor model candidate:** `claude-sonnet-5-5` via the Anthropic API is the approved exact auditor model identifier. This approval is not live-use readiness. Live use remains blocked until an offline qualification check against the synthetic adversarial fixtures shows the auditor rejects each required negative fixture and accepts its positive counterpart. Documentation facts (ID, Active status, 1M context, pricing, structured-output support; fetched 2026-10-11) are not evidence of Vietnamese fidelity, and model agreement is not medical correctness. Any other model, alias or automatic fallback requires new approval. Retention/training policy, secret-variable name, pricing configuration and spending/token ceilings remain separate unapproved decisions.
- **Approved by the user — auditor data-handling terms:** The default Anthropic commercial API terms, as published and reviewed on 2026-10-11 (Anthropic Privacy Center "Is my data used for model training?" and the API and data retention documentation), are accepted for `claude-sonnet-5-5` via the synchronous Messages API only. Published defaults at review: inputs and outputs are not used for training by default, and conversation content is not retained by default. `claude-sonnet-5-5` is not a listed Covered Model. The Batch API (29-day retention) is not approved, and ZDR is not required. These are provider defaults, not verified account terms: before live use the user must confirm out-of-band that the dedicated account or workspace is under Commercial Terms, with no conflicting retention override. Safety and abuse-monitoring retention was not verified. Gemini generator terms are not covered by this approval.
- **Approved by the user — auditor authentication method:** CI uses Anthropic Workload Identity Federation with the GitHub Actions OIDC issuer for `claude-sonnet-5-5`, instead of a static key stored in GitHub Secrets. Design requirements, from Anthropic documentation reviewed 2026-10-11: the federation rule must be pinned to this repository, the protected `main` ref and the repository owner, so pull-request and fork runs cannot obtain tokens; the workflow requests `id-token: write` only on the job that calls the auditor; preflight fails if `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` is set, because those override federation; token-exchange or refresh failure is a non-retryable authentication failure, not retried within the three-attempt policy; the identity token must stay fresh for the 30-minute per-video deadline. A separate dedicated static key is permitted only for the local offline qualification check and never for CI. Coding-CLI credentials remain forbidden. The local qualification check's static key is read only from the environment variable `TVP_AUDITOR_ANTHROPIC_API_KEY`, passed explicitly to the SDK, never from `ANTHROPIC_API_KEY`, never used in CI, and never logged. Federation identifiers, rule scope, OAuth scope and token lifetime are not yet approved. The user reports having admin rights to create the issuer, service account and rule; this is not independently verified. `GEMINI_API_KEY` remains the generator credential.
- **Approved by the user — auditor pricing configuration:** For `claude-sonnet-5-5`, standard synchronous Messages API pricing of $2 per million input tokens and $10 per million output tokens, per Anthropic documentation fetched 2026-10-11, with the source URL and verification date stored in the versioned configuration. No Batch API and no prompt caching are approved. Prices are updated only by human re-verification at a configuration-version change, never automatically from a live page. Account-specific discounts, taxes and future price changes are unverified. Gemini generator pricing is not researched or approved and remains a blocker for per-video totals. Spending, token and request ceilings, including any safety margin, remain unapproved (Decision 3).
- **Approved by the user — vocabulary process:** The user owns initial approval. Hand-curated topic targets are candidates only; the initial evidence-backed ledger requires separate approval. New tag proposals remain separate from the canonical ledger, with no automatic additions or generation-derived approval. No ledger is created by this planning revision.
- **Approved by the user — output/resource policies:** Retain the 40% full-rendered-output threshold including evidence, provenance and disclaimer, with no short-input exception; conservative extractive/protected-span checks; explicit unidentified-speaker labeling rather than guessed attribution; 120-second request timeout; 30-minute per-video deadline; three total attempts per request; and one video processed concurrently. Finite token/request/spending ceilings are required before live use, but their values remain unapproved.
- These approvals settle individual policies only. They do not approve the plan, select an exact API model, authorize implementation or change draft status. Completed review lenses and triage are recorded below; review is not implementation, testing or final plan approval.

## Open Questions — Human Approval Required

1. Approve the offline qualification check for `claude-sonnet-5-5`. Approve the non-secret federation identifiers and rule scope. Account-level confirmation of Commercial Terms remains a pre-live-use human check. Claude/Anthropic is approved as the preferred provider direction, alongside the Gemini generator; the Sonnet family is a recommendation pending model approval. No same-model exception is approved; block rather than silently fall back. Credentials must be dedicated API environment/GitHub Secrets configuration, never coding-CLI credential reuse.
2. Approve actual initial vocabulary entries and ledger version/provenance before generation; ownership and proposal approval process are approved above, but tag contents are not.
3. Choose finite per-video/per-run monetary caps and token/request ceilings after selecting providers. Confirm that the hard defaults and worst-case call reservations fit those ceilings; absent approved pricing/caps, live use fails closed. Gemini generator pricing must also be researched and approved before per-video totals can be computed.
4. Decide whether to approve the proposed durable validation receipt artifact, its name/layout and fail-closed publication/eligibility contract. This is a new output-contract proposal, not an approved policy or a companion edit; rendered provenance alone cannot establish untampered output eligibility.
5. After completed review findings and the plan diff are presented, explicitly approve the final plan before any status change or implementation. Until then the plan remains draft and implementation readiness is blocked.

## Implementation Notes

No scripts, tests, workflows, vocabulary, transcripts or metadata are implemented or changed by this revision.

## Tasks & Acceptance

**Execution (future work, dependency ordered):**
- [ ] `topics/vocabulary.md` -- after separate evidence-backed human approval of actual entries, record stable tag IDs, labels, evidence/source references, approval provenance and version. Candidate preparation is not approval; do not derive approval from the first generated summary.
- [ ] `scripts/summary_schema.json` -- define strict generator, auditor, and validated-document schemas with unknown fields rejected; include evidence/qualification requirements and coverage mapping below.
- [ ] `scripts/summary_fidelity.py` -- implement segment parser, snapshot hashing, normalization with source-offset mapping, input/evidence/protected-span validators, length/secret/disclaimer checks, deterministic renderer and same-directory atomic publication.
- [ ] `scripts/summary_providers.py`, `requirements.txt` -- implement independently configured JSON generator/auditor adapters, disabled tools/grounding, safe errors, token budgets, retries, timeouts and cost accounting; pin SDK dependencies after provider approval.
- [ ] `scripts/summarize.py` -- orchestrate CLI discovery, overlapping segment chunking, evidence-only synthesis, final audit, coverage checks, resource limits, restricted temporary storage, locks and safe machine-readable batch status.
- [ ] `tests/test_summary_fidelity.py`, `tests/test_summarize.py`, `tests/fixtures/summary_fidelity/` -- implement offline fake-provider tests for the matrix and every adversarial fixture below, including positive controls. Assert failure before atomic replace, unchanged input hashes, no secret/content logs and bounded calls.
- [ ] `.github/workflows/weekly-sync.yml`, `tests/test_summary_workflow.py` -- later wire GitHub Secrets, serialization, timeout, partial-success handling and eligible-input consolidation contract; test failure notification and explicit success-only paths without implementing the consolidator here.

**Acceptance Criteria:**
1. Given valid timestamped input, when parsed, then stable hash-bound segment IDs, ordered bounded ranges and source offsets are produced without changing transcript or metadata; malformed input fails before any API request.
2. Given valid generator JSON, when independently audited, then every atomic record receives exactly one allowed verdict and source-backed rationale; absent/duplicate verdicts, invalid schemas or auditor unavailability prevent publication. The final synthesis is audited against raw transcript segments, not merely generator prose.
3. Given an accepted record, when the deterministic gate runs, then all required evidence, speaker and qualification fields pass source matching, locality and protected-span checks; every substantive rendered statement maps to a supported record. Unsupported, materially altered, ambiguous, contradicted and missing-evidence records never appear in `summary.md`.
4. Given any adversarial fixture below, when the offline end-to-end pipeline runs, then its unsafe record is rejected, and a required-content failure prevents any summary from being created or replaced. A mocked auditor incorrectly returning `supported` must not bypass deterministic quote, time, protected-span or coverage checks.
5. Given a long-input positive fixture, when chunking and synthesis run, then a boundary qualification is retained with original IDs/quotes/ranges, overlap duplicates collapse without merging unrelated statements, and final raw-source auditing succeeds within the configured budget.
6. Given supported structured data, when rendered, then output includes overview, key points, notable claims, approved tags, per-record evidence/speaker/qualification and the exact canonical disclaimer; the full output's whitespace-token count is at most 40% of the normalized source-body whitespace-token count. Short-source inputs that cannot meet this threshold fail rather than waive the gate.
7. Given missing credentials, retry exhaustion, non-retryable failures, secret-like content, hash changes or lock contention, when processing runs, then publication is blocked, input files and previous summary remain unchanged, temporary files are cleaned, and logs contain only bounded allowed codes/counts/IDs.
8. Given a mixed-success batch, when Actions runs, then valid summaries may be committed by an explicit success-only step, failed targets are excluded, safe consolidation runs under the contract below, and the final workflow conclusion is failure. No-input and all-success summarizer runs exit 0; any video failure exits non-zero. Workflow success additionally requires successful consolidation; no eligible corpus fails consolidation even when the summarizer queue is empty.
9. Given an unapproved tag proposal or concurrent vocabulary revision, when processing runs, then no automatic ledger update occurs; only snapshot-approved tags may be published, and incompatible ledger drift requires revalidation.
10. Given omitted qualifiers, invented unqualified text, reused introduction attribution or an incomplete source coverage ledger, when a mocked auditor returns `supported`, then source-clause extraction, context/turn binding and exhaustive ledger checks still prevent publication.
11. Given dropped/deduplicated records or hostile source markup, when final validation/rendering runs, then references resolve only to surviving unique records and every dynamic field renders as inert text.
12. Given a prior summary failure, input-writer interference, or orphaned temporary output, when the next workflow runs, then retry discovery includes the failed existing video, publication requires exclusive input access, and startup recovery excludes/removes owned orphaned temporary files. Edited summary bytes cannot become eligible merely by retaining old provenance; the proposed durable receipt contract requires human approval before downstream publication.

## Code Map

- `scripts/fetch_transcript.py` -- current source emits `[hh:mm:ss] text` lines with start times only; reuse layout, not its raw-exception logging or mixed-batch exit-0 convention. Do not modify fetcher in this story.
- `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/{transcript.md,metadata.json}` -- seed; duration is 12765 seconds; introductory lines identify host Khánh Lành as well as the doctor. Read-only integration input, not an automatic correctness oracle.
- `scripts/summarize.py` -- planned CLI and pipeline; not yet implemented.
- `scripts/summary_schema.json`, `scripts/summary_fidelity.py`, `scripts/summary_providers.py` -- planned strict schema, pure validation/rendering helpers, and provider adapters.
- `requirements.txt` -- currently only `yt-dlp`; later add pinned generation/schema and approved auditor dependencies.
- `topics/vocabulary.md` -- planned human-curated approved tag ledger, consistent with hand-curated topic targets in `repo-structure.md`.
- `.github/workflows/weekly-sync.yml` -- currently detection only; retain this single Actions entry point and extend it later. `scripts/consolidate.py` is a downstream contract, not an implementation deliverable here.
- Canonical companions in frontmatter -- read-only contract; `disclaimer.md` is the exact disclaimer source.

## Design Notes

### Immutable input and timestamp contract

Read one UTF-8 byte snapshot; hash transcript and metadata with SHA-256 at entry and recheck before replacement. Derive segment ID as `transcript_sha256:line_number`; retain original text/byte offsets. Validate nonempty text, `hh:mm:ss` syntax, minute/second bounds, nondecreasing starts and `0 <= start < duration`. Equal starts form one temporal group while retaining distinct line IDs. Derived ends use the next distinct start, or validated metadata duration for the final group. These are caption-location intervals, not invented word-level timing. Claim ranges must equal the envelope of cited contiguous segments and remain within duration. Invalid or unavailable duration fails closed; never infer an end from generated prose.

Quote normalization is limited to Unicode NFC, CRLF-to-LF and collapsing Unicode whitespace to one space with edge trimming. Preserve case, accents, punctuation, numbers, units, negation and modality. Match contiguous normalized substrings within the cited segment IDs using a reversible offset map; no fuzzy matching, translations or ellipsis-as-verbatim. Multiple excerpts remain separate evidence entries. Quote offsets must resolve inside cited intervals: no arbitrary “nearby” tolerance and no quote elsewhere in the video satisfying a citation. The rendered quote uses original source characters. A valid timestamp without relevant evidence cannot pass.

### Structured intermediate data

Strict versioned JSON, not model Markdown:
- Envelope: `schema_version`, `video_id`, `transcript_sha256`, `vocabulary_version`, `overview[]`, `key_points[]`, `notable_claims[]`, `tags[]`, `coverage[]`.
- Every substantive record: `record_id`, atomic Vietnamese `statement`, `speaker {label, status, attribution_evidence[]}`, `evidence[]`, `qualifications`, `protected_spans[]`. Each evidence entry carries `segment_ids[]`, `start_s`, `end_s`, `quote_vi`, and source character offsets validated against the immutable snapshot.
- `qualifications` explicitly covers negation, uncertainty/modality, quantities/units, dosage, duration, population, conditions and exceptions. Values are source-linked exact spans or explicit `not_stated`, never inferred defaults. `protected_spans` maps those source spans to verbatim retained spans in the statement; attribution must not change patient/population or recommendation scope.
- `speaker.status`: `source_identified` or `unidentified`; explicit unknown attribution is allowed only when faithfully stated as unidentified, not guessed as the doctor. Unsupported identity claims fail. Auditors check attribution evidence separately.
- `tags[]`: approved ID plus supporting record IDs. `coverage[]`: required salient source passage IDs and their accepted record IDs; auditor evaluates missing important limitations/context directly from raw transcript, including chunk boundaries. Metadata/title are navigation context only, never medical evidence.
- Auditor report: source hash and provider/model identity; for each applicable record, exactly one `record_id` and `outcome`, a source-linked rationale, and identified missing-required-content entries. It cannot return replacement claims. Validated envelope adds verified report references, source/vocabulary hashes and generator/auditor model IDs; these provenance fields render in Markdown for later eligibility checks.

### Independent auditor and deterministic gate

Fresh auditor context receives candidate records plus raw Vietnamese source segments and neighboring context, not generator reasoning or claimed authority. The approved provider direction is Anthropic/Claude independent of Gemini. Exact auditor model/version and provider policy/configuration remain blocking; no same-model exception or automatic model fallback is approved. No external search, grounding or medical validation for either model. A final auditor pass examines synthesis and source coverage; over-budget sources require segment-based audit passes with overlap and a complete coverage ledger, not silent truncation.

Outcomes: **supported** (faithfully entailed with preserved speaker/scope); **unsupported** (not supported by source); **materially altered** (meaning/qualification changed); **ambiguous** (cannot safely resolve text/speaker/scope); **contradicted** (opposes source); **missing evidence** (no usable source reference/quote). JSON uses `supported`, `unsupported`, `materially_altered`, `ambiguous`, `contradicted`, `missing_evidence`. Only supported records may survive. Removing a rejected optional record requires rerunning coverage and final-output validation; no automatic rewritten claim or replacement advice. If key points/claims, essential limitations, evidence-backed tags, or required coverage cannot be safely retained, fail the video instead of publishing an empty or misleading subset.

Deterministic checks must validate schemas/required fields and one-to-one audit coverage, source hashes, timestamp bounds/locality, exact quotes/offsets, evidence for every claim, protected-span preservation (including negation and all clinical qualifiers), controlled tags, literal disclaimer, length, secrets and read-only inputs. Preserve the full contextual source clause whenever a qualifier cannot be isolated safely. Missing protection fields, lost spans, conflicting quantities, disjoint evidence used as a causal assertion or unverifiable scope fail closed.

Admissible substantive `statement` spans must map to exact, contiguous, complete source clauses, with only fixed renderer-owned attribution wrappers added. Generated bridging, causal connectors and free paraphrase are not admissible. Keep separate clauses as separate records rather than composing a new assertion. The validator examines the full cited clause and its necessary neighboring context, not only model-nominated spans: retain the whole clause including qualifiers; reject `not_stated` if relevant qualification text is present. If clause completeness, unresolved antecedents, or qualification scope cannot be conservatively established, reject the record. Models cannot define the gate's protection inventory; this extractive rule operationalizes the approved conservative checks without claiming exhaustive Vietnamese semantic detection.

Initialize a source-review ledger deterministically from every parsed temporal group, including overlap groups. Every group must receive a source-bound audit disposition (represented, context-only, non-substantive, or unresolved) and source-linked rationale; unresolved entries fail. The auditor marks mandatory limitations/context and maps them to retained records. Verify that the ledger covers the complete parsed source set, never just generator-selected salient passages. This guarantees review traversal, not objective salience or medical completeness.

Attribution must be turn-local: identity evidence must explicitly bind the cited passage to the identified speaker without an unresolved intervening turn. An introduction or channel identity cannot identify later unlabeled speech. When this binding cannot be established, use the fixed `unidentified` speaker label, or reject if ambiguity changes scope. No guessed speaker boundaries.

After any removal, synthesis or deduplication, validate globally unique record IDs and resolve all tags, coverage mappings, evidence IDs and audit references exclusively to surviving supported records; drop invalid dependent references and rerun required-content checks and final source audit. Unresolvable or required-content gaps fail.

Deterministic string checks cannot prove general semantic entailment or discover every Vietnamese qualification. They enforce a conservative extractive/protected-span contract in addition to independent semantic auditing, not instead of it. Ambiguous semantic preservation fails; neither model agreement nor this gate certifies medical correctness.

### Safe chunking

Chunk whole timestamped segments with at least two complete temporal groups of overlap on each boundary; extend overlap to include a whole qualifying clause/speaker turn. Determine complete clause/turn context from explicit source text and references, not timestamp groups alone or a model's unverified boundary suggestion. Extend through unresolved antecedents/qualifiers; if a complete context boundary cannot be conservatively established within the token budget, fail rather than sever context. Chunk outputs use the same evidence schema and absolute IDs/ranges; synthesize only evidence-bearing records with referenced raw context, never prose-only summaries. Deduplicate by source references without joining unrelated passages. Re-audit all synthesized records against raw source, not previous approvals alone.

### Rendering and publication

Renderer is deterministic and renders every dynamic field as inert text, including source quotes, statements, speaker labels, tags and provenance. Escape Markdown/HTML delimiters and disallow active links/images from these fields; source-injection quotes are data, not executable links/instructions. Evidence matching uses original source characters before display escaping; escaping must preserve their decoded textual content, not silently rewrite evidence. All factual overview text is record-based. The canonical block copied from the companion is:

> **Health disclaimer.** This content is a transcription and summary of Dr. Trần Văn Phúc's public videos (channel "Bác sĩ Trần Văn Phúc Official"). It is provided for informational and educational purposes only, does not constitute personalized medical advice, and is not a substitute for consultation, diagnosis, or treatment by a healthcare professional. If you have a health concern, consult a doctor.

Count normalized whitespace-delimited tokens of the source text after removing timestamp prefixes; denominator includes all source bodies. Numerator includes the entire rendered Markdown, including disclaimer, evidence and provenance. Require `summary_tokens <= floor(0.40 * source_tokens)`; reject zero-length source or too-short inputs. Validate the rendered bytes in memory, then write/fsync a restrictive same-directory temporary file and atomically replace `summary.md` under a per-video lock after rechecking hashes and vocabulary version. Preserve old output on any failure. The orchestrator must ensure exclusive access by all input/vocabulary writers throughout final recheck and publication, not rely on a summarizer-only lock. This story does not change the fetcher: serialize fetch-before-summary and reject publication if exclusive input ownership cannot be established. Recheck bindings again at the commit/consolidation boundary; outside edits invalidate eligibility.

Catchable interruption triggers cleanup; SIGKILL/power loss cannot guarantee it. At next locked startup, recover only owned, recognizable summary temporary files without following symlinks or touching inputs/old final outputs. Restrictive permissions apply from creation; commit staging uses an explicit final-artifact allowlist, never broad directory staging.

**Proposed additional output contract — human approval required:** persist a durable validation receipt binding exact rendered-summary SHA-256, transcript/metadata/vocabulary hashes, schema/validator version, approved provider/configuration identity and audit-report references. Keep content/secrets out of the receipt. A separate receipt beside `summary.md` needs an approved name/layout and fail-closed crash/partial-publication protocol: an absent/mismatched receipt makes the summary ineligible. This adds a planned artifact beyond the companion layout; do not implement or assume approval. Until resolved, rendered provenance alone is insufficient for downstream eligibility and CAP-3-to-consolidation publication is blocked.

### Vocabulary and operational safety

Automatically select approved existing tags only. New proposals carry evidence, rationale and source IDs for human approval or a separately controlled reviewed update; proposals never silently change the canonical ledger. Missing ledger is an approval dependency, not a model-seeding opportunity. Vocabulary updates use version/hash compare-and-swap and a repository-wide lock (Actions concurrency group); incompatible changes force revalidation. The summarizer itself does not write vocabulary or metadata topics.

Keys only through environment/GitHub Secrets (`GEMINI_API_KEY` and provider-specific approved auditor key); no literal-key CLI examples, shell tracing, debug SDK HTTP dumps or raw exception bodies. Log only validated video IDs, counts, stage and allowlisted error codes with messages capped at 200 characters. Never log transcript text, prompts, model responses, evidence quotes or credentials, including CI annotations, failed test assertions and artifacts. Secret-check input before sending to providers and candidate JSON/rendered bytes before writing, using known credential values plus key/token-pattern detection; suspicious strings fail without echoing them. Secret scanning is a defense, not a guarantee of detecting every unknown credential format.

Approved request/resource policies: 120-second request timeout, 30-minute per-video deadline, maximum three attempts with jittered exponential backoff honoring bounded `Retry-After`, concurrency one video, with a required hard preflight input/output-token and request-count budget including chunking, synthesis, all audit passes and retries; numeric ceilings remain pending approval. Retry requests that fail because of timeouts, transient transport errors, transient 429 errors or 5xx errors. Do not retry failures involving invalid input/schema, authentication/permission, exhausted quota/billing, audit/evidence failure or source drift. Approved provider pricing and finite per-video/per-run monetary caps must be configured; absent pricing/caps fail closed, never assume unlimited/free LLM usage. Stop before a call exceeding its reserved worst-case budget. Always clean restricted temporary files on success, failure and interruption; no sensitive CI artifacts or caches. Provider data-retention/training policy requires approval. Before live use, require a versioned human-approved configuration binding exact auditor model/version, dedicated secret-variable name, retention/training terms, pricing and finite ceilings; fail preflight if any required approval is absent. No availability, pricing or retention/training terms have been researched or verified during this review.

### Actions and consolidation contract

Retain the single scheduled/manual workflow; disable tracing and inject credentials at the model-call step only. Set job timeout and serialize publication/vocabulary operations with a repository concurrency group. A protected per-run manifest contains only IDs, statuses and hashes, never content or keys. Any failed requested video returns non-zero (including partial success), matching the companion's failed-workflow notification requirement. Explicit conditional follow-up steps may commit successful validated summaries and run consolidation despite a summary-step failure; a final status step must preserve the failure conclusion, not hide it with `continue-on-error`.

Consolidation regenerates on each pipeline run from only current hash-bound validated summaries and already eligible corpus entries, never partial, stale or audit-failed targets. Preserve fetch-produced raw transcript/metadata files without editing them. Legacy summaries without verifiable provenance require revalidation before inclusion. When no current successes exist, regenerate from remaining eligible corpus; if none exists, fail consolidation without overwriting prior artifacts. Honor <=20 files and the existing size limit contract; consolidation failures also fail Actions. This story defines/wires the eligibility interface, not CAP-5 packing implementation. Failed videos must remain explicitly retryable on later runs even when transcripts already exist; presence of raw inputs alone is not summary success. Build the summary queue as the deduplicated union of newly detected videos and existing transcript directories without a currently eligible summary (including stale, legacy, previously failed and receipt-mismatched outputs). Do not depend solely on detector repository-presence discovery. Validate IDs/paths and exclude out-of-repository/symlink targets. Offline workflow tests must show a fetched-but-failed video being requeued on the next scheduled run.

### Adversarial automated fixtures

All fixtures use synthetic Vietnamese source and offline scripted providers, never live medical validation. Each has a legitimate supported positive counterpart. Required negatives:
- Reversed negation (`không nên` -> `nên`).
- Uncertainty strengthened (`có thể` / “may” -> `sẽ` / “will”).
- Dosage or duration altered (quantity/unit and days/weeks separately).
- Population changed (adults -> children, or removal of subgroup restriction).
- Conditions/exceptions removed (`nếu`, `trừ khi`, contraindication/context clauses).
- Unrelated passages merged into a recommendation or causal assertion.
- Fabricated quote, including quote valid elsewhere but absent in cited segments.
- Syntactically valid, in-bounds but irrelevant timestamps.
- Medically plausible claim absent from raw source; models' background knowledge cannot justify it.
- Prompt-injection transcript text demanding instruction override, credential disclosure or fabricated advice.
- Ambiguous/inaudible source with missing quantity, uncertain negation or unknown speaker; no guessed repair.

Also test omitted source qualifications falsely marked `not_stated`, fabricated qualifier-free assertions, incomplete temporal-group review ledgers, introduction evidence misused for later turns, dangling references after deletion/deduplication, hostile source HTML/images/links/blockquote and delimiter breaks, summary-byte tampering with unchanged provenance, source changes during final-check/replace and commit windows, locked startup recovery after simulated abrupt termination, empty queue with empty/eligible corpus, failed-existing-video retry discovery, duplicate timestamps, boundary exceptions, normalization with accents/punctuation retained, missing auditor verdict, injected `supported` for deterministic mismatches, partial/all-failure exits, short-source ratio failure, secret detection, concurrent vocabulary/source changes, timeout/quota budgets, interrupted cleanup and preservation of previous output.

## Verification

**Future commands only; no implementation or live API verification is run during this plan revision:**
- `python -m py_compile scripts/summarize.py scripts/summary_fidelity.py scripts/summary_providers.py` -- syntax succeeds once implemented.
- `python -m unittest discover -s tests -p 'test_summary*.py'` -- offline schema/gate, adversarial and workflow contract tests pass without external network or unsafe output.
- `python -m unittest discover -s tests -p 'test_summarize*.py'` -- offline orchestration/partial-success/resource tests pass, including filesystem/hash/log assertions.
- `env -u GEMINI_API_KEY python scripts/summarize.py videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua` -- non-zero credential code, no write; run in an isolated copy with approved configuration.
- `python scripts/summarize.py videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua` -- optional approved live smoke test in an isolated copy, keys supplied out-of-band through environment, approved auditor/vocabulary/pricing/caps required. Success only if every gate passes; rejection is valid evidence of fail-closed behavior, not permission to relax checks.

**Human checks:** Inspect the before/after plan diff and confirm companions/implementation inputs unchanged. Before implementation approval, inspect selected fixture source/claim pairs, attribution policy, approved tags/provider configuration and evidence-bearing output layout. This is fidelity review, not clinical review or validation of the doctor's claims.

## Plan Change Log

- User-authorized draft revision: raised risk to high, replaced single-model/prose-oriented generation and implicit vocabulary seeding with independent transcript-fidelity auditing, strict evidence schema, fail-closed publication, operational controls and adversarial acceptance tests. KEEP: Vietnamese immutable source, English canonical disclaimer, no medical validation, single Actions pipeline and Markdown repository contract.

## Review Triage Log

- Independent read-only review completed against the pre-edit draft: adversarial (13 findings), edge-case-hunter (2 findings), structure (4 change suggestions and 2 preservation notes), and prose (7 wording clarifications). All four selected applicable lenses completed; these findings describe the pre-edit draft, not an independent re-review of the revised plan. Verification-gap did not apply: this is a behavioral document, not code. No implementation, offline tests or live API calls ran. High risk means distortion/propagation risk, not medical validation.
- A1–A2: existing model/configuration and actual vocabulary approvals remain blockers, not review postponements. Clarified separate vocabulary-entry approval; neither Sonnet recommendation nor provider direction approves an exact model/configuration.
- A3–A8: accepted clarifications of approved conservative checks: source-clause extraction, source-side qualification/context completeness, exhaustive temporal-group review ledger, turn-local attribution, complete-context chunk boundaries, surviving-record referential integrity. Ledger traversal does not prove salience or semantic/medical correctness.
- A9: accepted the output-tampering gap; durable receipt is a proposed new output artifact requiring human approval, not silently adopted. Downstream eligibility remains blocked pending that contract.
- A10 / E1: overlapping findings retained; require orchestration-level exclusion of input writers through publication and binding checks at commit/consolidation, without changing the fetcher.
- A11–A13: accepted concrete existing-video retry queue, separate summarizer/workflow empty-input outcomes, and inert rendering/hostile-markup fixtures for every dynamic field.
- E2: accepted locked recovery of owned orphan temporary files and explicit commit allowlist; corrected the impossible guarantee of cleanup after SIGKILL/power loss.
- Structure: accepted all four suggestions (move approval sections/notes forward, logs last, tasks before code map, split chunking from rendering/publication). Preserved matrix/criteria/fixtures and local safety/disclaimer reinforcement. Parent ran word_metrics.py: original 3,628 words; approval sections 358, notes/logs 97, Code Map 150, chunking/rendering 243. Moves remove 0 words (0%); splitting/renaming headings adds a net 1 word. Reviewer estimates were superseded by these measured counts; added safety detail is not an editorial reduction.
- Prose: accepted all 7 communication fixes: explicit ratio quantities, report-level versus per-record audit fields, retry/error nouns, model-tool grammar, no-create/no-replace outcome, replacement wording and medical-correctness limitation. Directive voice and deliberate safety reinforcement preserved.
- Planning verification: all four companions match the complete initial read snapshots byte-for-byte. Git status/path checks show no new implementation/input changes; the pre-existing modified fetch-transcript plan was not edited. The initial repository-wide hash snapshot was lost to context-mode sandbox cleanup, so a full before/after hash assertion for all files is not claimed. The original plan was recovered from its initial read for the review-session diff.
- These are plan-review findings and parent drafting decisions only. Draft status and explicit final human approval gate remain unchanged.

