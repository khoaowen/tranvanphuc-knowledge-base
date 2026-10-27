# Per-second median F0 (autocorrelation), objective voice-separation aid. Not speaker identification.
import sys, wave, numpy as np
f, base, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
w = wave.open(f); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float)/32768
n = int(sr*0.04); hop = n//2; lo, hi = int(sr/400), int(sr/70); fs = []
for i in range(0, len(x)-n, hop):
    s = x[i:i+n]-x[i:i+n].mean()
    if np.sqrt((s**2).mean()) < 0.02: fs.append(None); continue
    ac = np.correlate(s, s, 'full')[n-1:]; k = lo+np.argmax(ac[lo:hi])
    fs.append(sr/k if ac[k] > 0.4*ac[0] else None)
L = []
for t0 in range(int(len(x)/sr)):
    seg = [v for j, v in enumerate(fs) if v and t0 <= j*hop/sr < t0+1]
    T = base+t0; lab = f"{int(T//3600):02d}:{int(T%3600//60):02d}:{int(T%60):02d}"
    L.append(f"{lab}\tvoiced={len(seg):3d}\tmedianF0={'%.0f' % np.median(seg) if len(seg) >= 3 else '-'}")
open(out, 'w').write('\n'.join(L)+'\n'); print('\n'.join(L))
