# Fresh-context continuation: transcript fidelity and blocked Omega-3 audit

## Start here

Repository: `/Users/khoa/orca/workspaces/tranVanPhuc/Epic2-publish-videos`.
Initiative: `initiative-tran-van-phuc-knowledge-base`. BMad `core.active_initiative` is currently unset; explicitly use this initiative's existing artifacts, not a new loose initiative.

Read this file, then the linked research report, correction proposals and implementation plan. Do not restart the full audit, re-download evidence, or apply corrections automatically. User asked for durable BMAD tracking; no merge, publication or correction application was authorized by that request.

## Workstreams and status

1. **Research:** `research-transcript-fidelity-q7udjg8yq5c/research-transcript-fidelity-q7udjg8yq5c.md`. Raw captions, actual browser player responses/screenshots, Show transcript panel, audio, blind local Whisper output and timing comparison are in its `evidence/` directory. Machine pilot complete, human listening pending. Report has not received independent semantic review.
2. **Human listening:** `research-transcript-fidelity-q7udjg8yq5c/listener-bundle.zip` (about 4.4 MB, local/ignored), 8 MP3s + bilingual questions + answer template. Not sent to anyone, no human verification received. `listener-bundle/README-vi.md` omits suggested turn times in B1, while the original packet still contains them. Preserve this distinction. Packet has prompted alternatives; for an unbiased response have the listener first transcribe freely, then answer those questions.
3. **Correction proposals:** `spec-summary-source-audit/audit/q7uDJG8YQ5c/proposed-corrections-fidelity.md` (p1=c068, p2=c163, supplement IDs). Drafts only, pending human listen and explicit approval of exact final text. No video artifacts changed.
4. **Implementation:** branch `feat/raw-caption-provenance`, worktree `/Users/khoa/orca/workspaces/tranVanPhuc/Epic2-raw-captions`, commit `9124c18e65595c9834ebc559c55deec7ae105182`, baseline `47c72ce`. Canonical plan in THAT worktree: `epic-video-knowledge-pipeline/story-raw-caption-provenance-plan.md` under this initiative. Status in-review, independent review missing; 137 unittest tests pass (15 new), also rerun by parent. No merge/push. Existing videos unchanged. New gzip raw + provenance, --rerender and --check. Do NOT copy the branch's entire deferred-work.md over the main file; integrate individual changes after review.
5. **Follow-ups, not implemented:** existing-video raw backfill; CI wiring; precise claim-level links; handling ASR speaker-change flags; preserving spoken terms in summaries; optional ASR triage. Do not mistake research recommendations for approved spec changes.

## Is the earlier five-disagreement / eleven-omission report still relevant?

**Partially. No wholesale rerun is needed against the current files.** Their current hashes match the input hashes in `omissions-recheck.md`:
- summary.md: `e8cef3b0e5aa9caa7a84fab6dca4b08e0d5c20de2dcf0a9988db2cfd1a9ac620`
- transcript.md: `bbc4c9a51a2d844e4c5f818adb82031a872e09843e2ff20d62d60891d3cbd24b`

The actual current source is `videos/2025-12-06-nhung-meo-chon-thuc-pham-bo-sung-omega-3-hieu-qua/summary.md`; no audit-local summary exists. Keep claim IDs scoped to the supplement: c068 has different meanings in historical final_records.json vs supplement-records.json.

| Earlier item | Current treatment |
|---|---|
| c019 illustrative equation | Earlier proposed disposition remains relevant, NOT approved or newly rechecked. |
| c055 600 vs 2000 | Same: proposed attribution_qualification remains pending; do not turn transcript fidelity into guideline truth. |
| c068 division term/product | Text mismatch remains relevant. Audio is now available; blind Whisper hears `gián phân` twice (target and cross-reference), and `bốn bào tử`. This is machine evidence, not human confirmation. Earlier statement that no audio evidence exists is superseded. p1 proposes preserving spoken terms, not textbook substitution. |
| c163 Alzheimer/price | Earlier reasoning from `>>` as an actual turn is superseded. Player overlay carries ASR marker; YouTube's transcript panel omits it and groups text at 03:02:44. Pitch and blind ASR are compatible with continuous speech; screenshots are visual context, NOT proof of exact spoken identity. Keep identity pending human listening. Do not call this approved supported or definitively a false turn from pitch alone. p2 is pending. |
| c192 testing attribution | Still pending, not investigated against audio in this pilot. Since `>>` can be wrong, any attribution conclusion relying on it alone needs targeted audio verification, not automatic clearance. |
| Omission items 3,6,7,8,10,11,12,21,22 | Earlier coverage proposals still apply to unchanged summary; not approved, no new substantive check performed in this handoff. |
| Omission 4 practical diet | Distinguish covered-in-substance from unresolved `dầu ôu` identity. No new audio verification for that word. |
| Omission 20 testing/check-up | Covered-in-substance proposal separate from c192 attribution, which is still unresolved. |

The historical omissions recheck labels 11 items 'still omitted', including identity/attribution-only issues. The user's later proposed table separates substantive omissions from fidelity questions: preserve both as dated views, do not silently replace the historical tally. Scientific truth remains outside this investigation.

## Next actions in a fresh context

1. Run an independent review of `47c72ce..9124c18` in the implementation worktree using bmad-code-review/bmad-build review continuation. This is the required unfinished quality gate; the implementation is NOT complete/merged just because tests pass. Obtain authorization before launching new reviewer agents if not already supplied in the fresh request.
2. Get the human listening answers. No paid services, fabricated verification or auto-approval.
3. Refresh only c068/c163 evidence/disposition proposals; add targeted c192 speaker verification if requested. Keep other findings and omission scope decisions pending explicit approval.
4. Once exact correction text is approved/applied, regenerate current claim extraction/mapping, source hashes and impacted audit/omission checks. Until then retain the 194-claim baseline and blocked publication.
5. Merge/backfill/CI only when authorized. No change to review decisions or publication flags here.

## Cautions / prior overclaims

Prior chat and some research prose overstated: 'all machine evidence shows one person', 'the question rests on a false premise', 'the hedge is unnecessary'. Pitch cannot establish identity or rule out a second similar voice; still images cannot verify an utterance. Treat those as provisional hypotheses, not resolved audit findings.
Prior ASR word-timing comparisons are estimates, not calibrated human alignment; the claimed ±0.3 s accuracy was not established. Word-alignment agreement does not by itself prove audiovisual synchronization. See `evidence/timing-alignment.md` for exploratory values only.
Independent Whisper hallucinated all of regression R3 and dropped backchannels in R2: never replace captions with it unattended.

## Local environment / recovery

- Existing Homebrew yt-dlp restored at 2026.03.17 after a failed upgrade; isolated `uvx --from 'yt-dlp[default]@latest' yt-dlp` used 2026.08.19 to download audio without cookies.
- whisper.cpp model already local: `~/whisper.cpp/models/ggml-large-v3-turbo.bin`. Use CPU `-ng`; AMD Metal run produced gibberish and aborted.
- Chrome debugging on port 9222 was launched with a copied user profile; may still be open. Don't log cookies/tokens. Browser evidence can include signed URLs; don't publish those unredacted.
- Full audio/MP3/zip are gitignored local evidence; preserve them separately if moving machines. Research/docs in the main checkout are uncommitted. Don't stash/reset or overwrite unrelated audit changes.
