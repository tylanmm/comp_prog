from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n = int(_i())
have = {'pink': 1}
for _ in range(n):
    o, w, r = _i().split()
    r = float(r)
    
    if w in have:
        if o in have:
            have[o] = max(have[o], have[w]*r)
        else:
            have[o] = have[w]*r

if 'blue' in have:
    _p(min(10, have['blue']))
else:
    _p(0)

stdout.flush()