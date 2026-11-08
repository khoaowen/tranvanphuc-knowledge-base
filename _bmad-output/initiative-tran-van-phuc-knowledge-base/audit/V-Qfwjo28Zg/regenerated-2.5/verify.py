import json,re,hashlib
R='regenerated/';O='regenerated-2.5/'
old=open(R+'summary.md').read();new=open(O+'summary.md').read()
rv=json.load(open(R+'review.md'));mv=json.load(open(O+'moves.json'))
def sec(t): h,m,s=map(int,t.split(':')); return h*3600+m*60+s
def f(x): return "%02d:%02d:%02d"%(x//3600,x%3600//60,x%60)
res=[]
ol=old.split('\n');nl=new.split('\n')
fo=next(i for i,l in enumerate(ol) if l.startswith('## ['));fn=next(i for i,l in enumerate(nl) if l.startswith('## ['))
res.append(('header identical',ol[:fo]==nl[:fn]))
hs=[re.match(r'## \[(\d\d:\d\d:\d\d)\] (.*?) — (\S+)$',l) for l in nl if l.startswith('## [')]
ts=[sec(m[1]) for m in hs]
res.append(('headings count old/new',(sum(l.startswith('## [') for l in ol),len(hs))))
res.append(('headings strictly increasing',all(a<b for a,b in zip(ts,ts[1:]))))
res.append(('?t= matches heading time',all(m[3].endswith('&t=%ds'%sec(m[1])) for m in hs)))
EDIT={'c271','c286'}
miss=[c['id'] for c in rv['claims'] if c['id'] not in EDIT and new.count(c['claim'])!=old.count(c['claim'])]
res.append(('claims whose text count changed (excl c271,c286)',miss))
res.append(('claims absent from new',[c['id'] for c in rv['claims'] if c['id'] not in EDIT and c['claim'] not in new]))
# transcript quote check for moved claims
T=open(R+'transcript.md').read().split('\n')
words=[]
for l in T:
    m=re.match(r'\[(\d\d:\d\d:\d\d)\] (.*)',l)
    if m:
        for w in re.sub(r'[^\w]+',' ',m[2].lower()).split(): words.append((sec(m[1]),w))
ws=[w for _,w in words]
def loc(q,rt):
    qw=re.sub(r'[^\w]+',' ',q.lower()).split()[:8]
    if len(qw)<4: return None
    h=[words[i][0] for i in range(len(ws)-len(qw)) if ws[i:i+len(qw)]==qw]
    return min(h,key=lambda x:abs(x-rt)) if h else None
C={c['id']:c for c in rv['claims']}
rows=[];bad=[];na=[]
for m in mv:
    c=C[m['claim']];ev=c.get('evidence') or []
    H=sec(m['to_heading'])
    if not ev or not ev[0].get('quote'): na.append((m['claim'],'no quote'));continue
    rt=sec(ev[0]['timestamp'].split('-')[0]);t=loc(ev[0]['quote'],rt)
    if t is None: na.append((m['claim'],'quote not verbatim in transcript, reviewer time '+f(rt)));continue
    ok=H-120<=t<=H+420
    rows.append((m['claim'],f(t),m['to_heading'],ok))
    if not ok: bad.append((m['claim'],f(t),m['to_heading']))
res.append(('moved claims located verbatim and inside new heading window',(len(rows)-len(bad),len(rows))))
res.append(('moved claims outside window',bad));res.append(('moved claims not locatable (flag)',na))
# remaining far claims in the 16 headings
T16=['00:19:12','00:48:55','01:31:32','01:33:05','02:10:50','02:22:01','02:53:59','02:55:58','02:56:30','02:57:13','02:57:43','02:59:04','03:36:48','03:38:50','04:19:29','04:21:40']
mvd={m['claim'] for m in mv}; rem=[]
for c in rv['claims']:
    if c['section'][1:9] in T16 and c['id'] not in mvd:
        ev=c.get('evidence') or []
        if not ev: continue
        rt=sec(ev[0]['timestamp'].split('-')[0]);t=loc(ev[0]['quote'],rt) or rt;H=sec(c['section'][1:9])
        if not(H-120<=t<=H+420): rem.append((c['id'],c['section'][1:9],f(t)))
res.append(('far claims still under original heading',rem))
res.append(('sha256 new',hashlib.sha256(new.encode()).hexdigest()))
for k,v in res: print(k,'=>',v)
