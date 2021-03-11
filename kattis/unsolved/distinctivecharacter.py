from sys import stdin, stdout

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n, k = map(int, _i().split())
vals = [_i() for _ in range(n)]
res = []
for i in range(k):
    tot = 0
    for v in vals:
        if v[i] == '1':
            tot += 1
    res.append('0' if 2*tot > n else '1')

_p(''.join(res))

stdout.flush()