#!/usr/bin/env python3
"""Ticket 2.5 gate run 2: write claim-map.md and gate-report.md for review.md bound to summary 970a54c9.
Run from audit/V-Qfwjo28Zg/. Reads only; writes only into regenerated-2.5/gate-970a54c9/."""
import json, hashlib, collections
D = 'regenerated-2.5/gate-970a54c9/'
SUM = '970a54c9e30fceb11fb27b3011a905f035b8adec38082272672a32a71c80974d'
n = json.load(open(D + 'review.md'))
p = json.load(open('regenerated-2.5/review.md'))   # historical, bound to 606f8441
o = json.load(open('regenerated/review.md'))       # 2.4, bound to 90c7e4aa
assert n['summary_sha256'] == SUM
assert hashlib.sha256(open('regenerated-2.5/summary.md', 'rb').read()).hexdigest() == SUM
assert p['summary_sha256'].startswith('606f8441')

# historical 2.5 claim map: 2.5(run1) id -> (2.4 id, relation)
hist = {}
for l in open('regenerated-2.5/claim-map.md'):
    if l.startswith('| c'):
        f = [x.strip() for x in l.strip().strip('|').split('|')]
        hist[f[0]] = (f[1], f[2])
O = {c['id']: c for c in o['claims']}

def match(src, dst):
    """map each claim of dst to the claim of src with identical text (same occurrence order)."""
    idx = collections.defaultdict(list)
    for c in src['claims']:
        idx[c['claim']].append(c)
    used = collections.Counter(); out = {}
    for c in dst['claims']:
        k = c['claim']; i = used[k]; used[k] += 1
        out[c['id']] = idx[k][i] if i < len(idx[k]) else None
    return out

M = match(p, n)
rows = []
for c in n['claims']:
    pc = M[c['id']]
    oid, rel = hist.get(pc['id'], ('-', 'unmapped')) if pc else ('-', 'no run-1 match')
    if pc and pc['section'][:10] != c['section'][:10]:
        rel = f'moved after run 1 ({pc["section"][1:9]} -> {c["section"][1:9]}); 2.4 relation: {rel}'
    ostat = O[oid]['status'] if oid in O else '-'
    rows.append(dict(id=c['id'], pid=pc['id'] if pc else '-', oid=oid, rel=rel, o=ostat,
                     p=pc['status'] if pc else '-', n=c['status'], c=c))

cm = ['# Claim map: 2.5 gate run 2 review -> 2.5 gate run 1 review -> 2.4 review (by claim text)', '',
      f'Run-2 review binds summary SHA-256 `{SUM}`. Run-1 ids and statuses come from `../review.md` '
      f'(bound to `{p["summary_sha256"]}`); 2.4 ids and relations come from the historical `../claim-map.md`. '
      'Matching is by exact claim text, in occurrence order.', '',
      '| run-2 id | run-1 id | 2.4 id | relation | 2.4 status | run-1 status | run-2 status |', '|---|---|---|---|---|---|---|']
cm += [f"| {r['id']} | {r['pid']} | {r['oid']} | {r['rel']} | {r['o']} | {r['p']} | {r['n']} |" for r in rows]
open(D + 'claim-map.md', 'w').write('\n'.join(cm) + '\n')

st = collections.Counter(c['status'] for c in n['claims'])
tr = collections.Counter((r['p'], r['n']) for r in rows)
sev = collections.Counter(x['severity'] for x in n['concerns'])
fails = [r for r in rows if r['n'] == 'fail']
def esc(s): return str(s).replace('|', '\\|').replace('\n', ' / ')
def origin(r):
    a = 'still fails (failed in run 1)' if r['p'] == 'fail' else 'new in run 2 (passed in run 1)'
    b = {'fail': 'failed in 2.4', 'pass': 'passed in 2.4'}.get(r['o'], 'no 2.4 match')
    return f'{a}; {b}; {r["rel"]}'
g = ['# Gate report ticket 2.5, run 2 (summary 970a54c9)', '',
     f'Review `review.md` binds summary SHA-256 `{SUM}` (= `../summary.md`, the current 2.5 summary with c277 moved alongside the case at 04:53:37). '
     'This is the one owner-authorized paid run on this hash: codex gpt-6.1-sol, `./review-summaries --provider codex --model gpt-6.1-sol --limit 1 --no-commit` '
     'on an isolated copy. It hit the usage limit after chunks 1–10, and the owner chose to resume the same run after the quota reset. '
     'The resume reused the hash-bound progress cache for chunks 1–10 and reviewed only chunk 11 plus the coverage audit. No second gate run was made.', '',
     f'**Verdict: {n["verdict"]}.** {len(n["claims"])} claims: {st["pass"]} pass, {st["fail"]} fail, {st.get("flag",0)} flag; '
     f'{len(n["concerns"])} concerns ({sev["material"]} material, {sev["minor"]} minor); {len(n["omissions"])} omissions; '
     f'coverage_complete {str(n["coverage_complete"]).lower()}; {n["chunks"]} chunks. Failures are reported, not fixed (ticket 2.6). V-Qfwjo28Zg stays blocked.', '',
     f'Run 1 (`../gate-report.md`, `../review.md`, summary 606f8441) reported 566 claims, 511 pass, 55 fail, 25 concerns, 15 omissions. '
     'Those files are historical and were not changed. Between the two runs only c277 moved; every other claim text and section is identical. '
     'The differences below are therefore model variance between runs, not fixes.', '',
     '## Status change vs run 1 (same claim text)', '']
g += [f'- run 1 {a} -> run 2 {b}: {k}' for (a, b), k in sorted(tr.items())]
g += ['', '## c277 contextual-placement exception', '',
      'c277 ("Bác sĩ không nêu rõ liều hay điều kiện cụ thể.") is run-2 claim ' +
      ', '.join(f"{r['id']} ({r['n']}, evidence {r['c']['timestamp']}, section {r['c']['section'][1:9]})" for r in rows if r['pid'] == 'c218') +
      '. The owner placed it beside the case at 04:53:37 on purpose; its evidence stays at 02:11:08–02:11:09. '
      'The general timestamp checks were not relaxed. `verify.py` still reports it as "moved claim outside window". '
      'The gate passed the claim. The gate checks that the quote matches the transcript at its timestamp; it does not check the heading window. '
      'Since commit `8975775` (2026-10-18, "accept verified cross-section evidence in aggregation and publish gate"), the reviewer and `queue_state` deliberately accept verbatim evidence outside the section window. '
      'So neither the gate nor the publication check enforces placement, and `verify.py` is the only window check. '
      '`docs/review-summaries.md` still describes the older window rule; that documentation drift is recorded as deferred, not blocking. '
      'This is a documented exception, not a pass of the window check.', '',
      '## Failing claims', '', '| run-2 id | run-1 id | 2.4 id | origin | claim | issues |', '|---|---|---|---|---|---|']
for r in fails:
    iss = '; '.join(f"[{x.get('timestamp')}] {x.get('finding')} (quote: {x.get('quote')})" for x in r['c']['issues']) or '(no issue text)'
    g.append(f"| {r['id']} | {r['pid']} | {r['oid']} | {esc(origin(r))} | {esc(r['c']['claim'])} | {esc(iss)} |")
g += ['', '## Claims that failed in run 1 and pass in run 2', '', '| run-2 id | run-1 id | claim |', '|---|---|---|']
g += [f"| {r['id']} | {r['pid']} | {esc(r['c']['claim'])} |" for r in rows if r['p'] == 'fail' and r['n'] == 'pass']
g += ['', '## Concerns', '', '| severity | chunk | timestamp | finding |', '|---|---|---|---|']
g += [f"| {x['severity']} | {x.get('chunk')} | {x.get('timestamp')} | {esc(x['finding'])} |" for x in n['concerns']]
g += ['', '## Omissions', '', '| timestamp | topic |', '|---|---|']
g += [f"| {x.get('timestamp')} | {esc(x['topic'])} |" for x in n['omissions']]
open(D + 'gate-report.md', 'w').write('\n'.join(g) + '\n')
print(st, tr, len(fails))
