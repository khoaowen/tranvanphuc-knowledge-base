# Pass-1 reader instructions (V-Qfwjo28Zg) — identical for every batch

You are a read-only auditor. Do NOT edit any file except the two output files named in your task. Never touch `videos/` except reading `transcript.md`. No medical correction, no inference beyond the transcript. Preserve speaker identity and qualifications as spoken.

Transcript (READ ALL OF IT, in chunks with offset/limit until the last line; ~8158 lines):
`/Users/khoa/IdeaProjects/tranVanPhuc/videos/2026-10-10-so-135-glutathione-can-bang-oxy-hoa-khu-phuc-hoi-ty-the-va-bao-ve-te-bao-tu-cap-do-phan-tu/transcript.md`
Format: caption lines `[hh:mm:ss] text`; a quote may span several consecutive caption lines (join with single space; drop `[ts]` prefixes; ignore the `>>` speaker-change marker).
Record format spec: `/Users/khoa/IdeaProjects/tranVanPhuc/_bmad-output/initiative-tran-van-phuc-knowledge-base/spec-summary-source-audit/audit-record-format.md`

For every claim in your input batch (JSON list of {id, section, text}) decide against the FULL transcript (not just the section window; the summary section time is only a hint):
- class `supported`: quote backs the claim, speaker and qualifiers (hedges, conditions, "có thể", dosage/population limits) intact.
- `mismatch`: transcript contradicts or says something materially different (number, direction, entity).
- `attribution_qualification`: content present but speaker misattributed, or a qualification dropped/hardened/added (name which in `note`).
- `unresolved`: no evidence found or ambiguous after reading the whole transcript; leave `evidence` empty.
Be strict and independent: do not assume the summary is right. Copy quotes character-for-character from the transcript (Vietnamese diacritics and the transcript's own typos included); quotes are checked by a script as verbatim substrings. Keep each quote reasonably short (one to three caption lines worth) but sufficient; use 1-3 quotes per claim, each with the `[hh:mm:ss]` of a caption line it covers (format `hh:mm:ss`).

Output 1: write JSON array (valid JSON, UTF-8) to the out path in your task, one object per input claim, same order, all ids present:
{"id":"c001","class":"supported|mismatch|attribution_qualification|unresolved","evidence":[{"quote":"...","timestamp":"hh:mm:ss"}],"speaker":"who says it in the transcript vs how the summary attributes it","note":"one line why; for attribution_qualification name the dropped/hardened hedge or speaker"}
Do not include the claim text.

Output 2: write plain text to the om path in your task: important transcript topics NOT covered by the summary that you noticed while reading the whole transcript, restricted to the timestamp range given in your task (small talk, greetings, viewer-comment reading excluded). Each item numbered: `N. [hh:mm:ss] topic description (one line why important). Anchor: "verbatim quote"`. If none, write `none found`.

When done reply with: counts per class, number of omissions, and any claim you could not complete. Keep reply short.
