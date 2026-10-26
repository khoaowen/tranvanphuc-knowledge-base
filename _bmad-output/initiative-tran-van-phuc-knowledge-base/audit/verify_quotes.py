#!/usr/bin/env python3
"""Read-only verifier: each quote must be a verbatim substring of the transcript
(caption line breaks/timestamp prefixes joined by single spaces; the caption speaker-change marker ">>" is ignored on both sides), and the cited
timestamp must be that of a caption line within the quote's span (+/- tolerance).
usage: verify_quotes.py <video_id> <transcript.md> <records.json> [tol_seconds]"""
import json,re,sys
vid,tp,rp=sys.argv[1:4]; tol=int(sys.argv[4]) if len(sys.argv)>4 else 5
def sec(ts):
    p=[int(x) for x in ts.split(':')]; 
    while len(p)<3:p.insert(0,0)
    return p[0]*3600+p[1]*60+p[2]
text="";spans=[]  # (start_char,end_char,ts)
for ln in open(tp,encoding='utf-8').read().split('\n'):
    m=re.match(r'\[(\d+:\d+:\d+)\]\s?(.*)$',ln)
    if not m: continue
    s=len(text); text+=re.sub(r"(^|\s)>>\s?",r"\1",m.group(2))+" "; spans.append((s,len(text),sec(m.group(1))))
recs=json.load(open(rp)); bad=0;n=0
for r in recs:
    for e in r.get('evidence',[]):
        n+=1;q=re.sub(r'\s+',' ',re.sub(r'(^|\s)>>\s?',r'\1',e['quote'])).strip();i=text.find(q)
        if i<0: bad+=1;print('NOT VERBATIM',r['id'],q[:70]);continue
        ts=sec(e['timestamp']);j=i+len(q)
        ts_list=[t for s,en,t in spans if s<j and en>i]
        # any occurrence
        ok=False;k=i
        while k>=0 and not ok:
            kk=k+len(q);tl=[t for s,en,t in spans if s<kk and en>k]
            if tl and min(tl)-tol<=ts<=max(tl)+tol: ok=True
            k=text.find(q,k+1)
        if not ok: bad+=1;print('TIMESTAMP MISMATCH',r['id'],e['timestamp'],q[:50])
print(vid,'quotes',n,'failures',bad); sys.exit(1 if bad else 0)
