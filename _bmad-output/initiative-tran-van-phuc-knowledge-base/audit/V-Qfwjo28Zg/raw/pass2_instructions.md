# Blind pass-2 instructions — V-Qfwjo28Zg

You are an independent, blind auditor. You must not inspect pass-1 results, classes, explanations, omissions, or the first-pass batch outputs. Only use your assigned input claims, the current summary (via each claim's exact text), the full transcript, and the record-format contract. Do not touch video files except reading transcript; do not edit/delete/overwrite existing artifacts except writing the two named output files.

Read the FULL transcript sequentially from its first line through EOF:
`/Users/khoa/IdeaProjects/tranVanPhuc/videos/2026-10-10-so-135-glutathione-can-bang-oxy-hoa-khu-phuc-hoi-ty-the-va-bao-ve-te-bao-tu-cap-do-phan-tu/transcript.md`
Transcript has about 8,159 timestamped caption lines. Do not use keyword searches or a local section window as a substitute for the sequential full read.

Contract: `/Users/khoa/IdeaProjects/tranVanPhuc/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-summary-source-audit/audit-record-format.md`

For each assigned claim (id, section, exact summary text), independently classify it against the full transcript:
- `supported`: source supports the claim, speaker, and qualifications (hedges, conditions, quantities, populations) as written.
- `mismatch`: transcript contradicts or says something materially different.
- `attribution_qualification`: speaker is misattributed, or a qualification is added/dropped/hardened/softened.
- `unresolved`: after the complete transcript read, the evidence is genuinely ambiguous or absent. Explain why; do not infer.

Copy verbatim quote(s) from the transcript, preserving transcript spelling and punctuation. Give timestamp `hh:mm:ss`; each quote must be a contiguous span after joining consecutive caption lines with a single space, dropping timestamp prefixes and the `>>` speaker-change marker. Use concise sufficient evidence. Preserve speaker attribution and qualifiers; no medical correction or outside facts.

Write a JSON array to your designated output path, one record per input claim in the same order:
`{"id":"c001","class":"supported|mismatch|attribution_qualification|unresolved","evidence":[{"quote":"verbatim transcript quote","timestamp":"hh:mm:ss"}],"speaker":"who says it vs how summary attributes it","note":"brief reason; name exact changed hedge/speaker where applicable"}`
For unresolved claims, evidence is an empty array. Do not add first-pass fields or refer to another auditor. Also write a short plain-text output file listing any major concerns or borderline calls, or `none`.

At completion report: confirmation that all transcript lines were read sequentially, assigned claim count, counts per class, borderline calls, and output paths. No unsupported reply claims.