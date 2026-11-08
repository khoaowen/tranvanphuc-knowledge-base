#!/usr/bin/env python3
"""Rebuild regenerated/summary.md into regenerated-2.5/summary.md (ticket 2.5). Read-only on inputs."""
import json,re,hashlib,sys
R='regenerated/'; O='regenerated-2.5/'
rv=json.load(open(R+'review.md')); C={c['id']:c for c in rv['claims']}
L=open(R+'summary.md').read().split('\n')
URL='https://www.youtube.com/watch?v=V-Qfwjo28Zg'
def sec(t): h,m,s=map(int,t.split(':')); return h*3600+m*60+s
# parse
first=next(i for i,l in enumerate(L) if l.startswith('## ['))
pre=L[:first]; H=[]
for i in range(first,len(L)):
    l=L[i]
    if l.startswith('## ['):
        m=re.match(r'## \[(\d\d:\d\d:\d\d)\] (.*?) — (\S+)$',l); H.append(dict(t=m[1],title=m[2],raw=[l],blocks=None,mod=False))
    else: H[-1]['raw'].append(l)
for h in H:
    body=h['raw'][1:]; bl=[];cur=None
    for l in body:
        if l.startswith('**Q:'): cur=dict(q=l,t=[]);bl.append(cur)
        elif cur is not None and l.strip(): cur['t'].append(l)
    h['blocks']=bl; h['stub']=(not bl and any('Đã gộp' in l for l in body))
byt={h['t']:h for h in H}
# claim -> (heading time, block, index span)
loc={}
for c in rv['claims']:
    ht=c['section'][1:9]; h=byt[ht]
    for b in h['blocks']:
        if len(b['t'])==1 and c['claim'] in b['t'][0]: loc[c['id']]=(ht,b); break
def rng(a,b): return ['c%03d'%i for i in range(a,b+1)]
S=[('00:31:19','Superoxit: gốc tự do cơ bản nhất (tiếp)',['c041','c060','c061']),
 ('00:33:42',None,['c042']),
 ('02:26:23',None,rng(150,164)),('02:34:11',None,rng(165,167)),
 ('02:35:19',None,rng(168,171)+['c173','c174']+rng(175,179)+['c181','c182']),('02:04:21',None,['c172']),
 ('04:11:00','Danh sách vi chất theo bác sĩ: magie, kẽm, canxi, vitamin D3',['c180']+rng(415,417)),
 ('02:42:02','Bóng đè do thiếu oxy hay do tư thế nằm, và cách giảm bóng đè',rng(183,187)),
 ('02:44:45','Vitamin D 50.000 IU: nồng độ mục tiêu và cách duy trì',rng(193,211)),
 ('04:53:37',None,rng(274,277)),('02:43:43',None,rng(302,305)),
 ('03:09:46','Hình thể gầy và chỉ số BMI của bác Lương Trắc Nghiên',rng(317,320)),
 ('03:13:53','Ý nghĩa MPV giảm, MCV và MCH tăng nhẹ ở bác Lương Trắc Nghiên',rng(325,328)),
 ('03:17:03','AST tăng, ALT bình thường ở bác Lương Trắc Nghiên',['c334','c335']),
 ('03:18:45','Axit uric và cholesterol tăng ở người gầy, ăn đạm bạc',rng(339,341)),
 ('04:03:09',None,['c342','c343']),
 ('03:21:06','Chỉ số TSAT, feritin và biểu hiện thiếu sắt',rng(356,361)),
 ('03:28:54','Chụp CT lồng ngực của bác Lương Trắc Nghiên: xẹp thùy phổi và đường dẫn khí',rng(363,367)),
 ('03:31:26',None,rng(368,370)),
 ('04:09:52','Bác Nghiên tập thở an toàn khi sức yếu',rng(408,410)),
 ('04:44:28','Chị Hằng: thuốc trầm cảm và kết quả sau khi bổ sung vi chất',rng(466,468)),
 ('04:29:03','Cấu tạo, hoạt động và tái tạo của glutathion (tiếp)',['c470','c471','c472','c476']+rng(478,484))]
# apply edits to texts first (owner decisions)
EDIT={'c271':'Bố chồng chị Ngân bổ sung vi chất và đường huyết giảm xuống (bác sĩ nói “chồng chị Ngân”; theo chủ sở hữu, ý là bố chồng chị Ngân).',
 'c286':'Người dẫn đọc bình luận của một điều dưỡng về bố chồng bị tiểu đường, đường huyết kiểm soát 5.5–6.8 (xem mục 01:11:21, lúc 01:11:52). Bác sĩ nói “chồng chị Ngân” sau khi uống thì đường huyết giảm trở lại bình thường (theo chủ sở hữu, bác sĩ nói lỡ, ý là bố chồng chị Ngân), còn chị Ngọc Thơ giải quyết được vàng da vàng mắt (lúc 02:14:12).'}
moves=[]
def claims_of(h):
    out=[]
    for b in h['blocks']:
        if len(b['t'])!=1: b['sp']=None; continue
        t=b['t'][0]; pos=0; sp=[]
        for c in rv['claims']:
            if c['section'][1:9]==h['t'] and loc.get(c['id'],(0,0))[1] is b:
                i=t.find(c['claim'],pos)
                if i<0: i=t.find(c['claim'])
                sp.append((i,c['id'],c['claim'])); pos=i+len(c['claim'])
        sp.sort(); b['sp']=sp
        assert ' '.join(x[2] for x in sp)==t,(h['t'],b['q'][:40])
for h in H:
    if h['blocks']: claims_of(h)
for h in H:
    if h['blocks']:
        for b in h['blocks']:
            if b['sp'] is None: continue
            b['sp']=[(i,cid,EDIT.get(cid,tx)) for i,cid,tx in b['sp']]
            for old,new in (('chồng chị Ngân ra sao','bố chồng chị Ngân ra sao'),):
                if old in b['q'] and h['t']=='02:10:50': b['q']=b['q'].replace(old,new); h['mod']=True
            if any(cid in EDIT for _,cid,_ in b['sp']): h['mod']=True
def nb(q): return dict(q=q,sp=[])
for dt,title,ids in S:
    if dt not in byt:
        h=dict(t=dt,title=title,raw=None,blocks=[],mod=True,new=True); byt[dt]=h; H.append(h)
    d=byt[dt]; d['mod']=True
    if d.get('stub'): d['blocks']=[]
    for cid in ids:
        ht,b=loc[cid]; src=byt[ht]
        item=[x for x in b['sp'] if x[1]==cid][0]
        b['sp']=[x for x in b['sp'] if x[1]!=cid]; src['mod']=True
        tgt=next((x for x in d['blocks'] if x['q']==b['q'] and x['sp'] is not None),None)
        if tgt is None: tgt=nb(b['q']); d['blocks'].append(tgt)
        tgt['sp'].append(item); tgt['sp'].sort(key=lambda x:x[1])
        moves.append(dict(claim=cid,text=item[2],from_heading=ht,to_heading=dt,question=b['q'][4:-2]))
for h in H:
    if h['blocks'] is not None: h['blocks']=[b for b in h['blocks'] if b['sp'] is None or b['sp']]
H.sort(key=lambda h:sec(h['t']))   # stable: chronological
out=list(pre)
for h in H:
    if not h['mod']: out+=h['raw']; continue
    out.append(f"## [{h['t']}] {h['title']} — {URL}&t={sec(h['t'])}s"); out.append('')
    for b in h['blocks']:
        out.append(b['q'])
        out+= b['t'] if b['sp'] is None else [' '.join(x[2] for x in b['sp'])]
        out.append('')
text='\n'.join(out)
open(O+'summary.md','w').write(text)
json.dump(moves,open(O+'moves.json','w'),ensure_ascii=False,indent=1)
print(len(moves),'moved claims; sha',hashlib.sha256(text.encode()).hexdigest())
