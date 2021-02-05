from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n, k = map(int, _i().split())
time = sorted([tuple(map(int, _i().split())) for _ in range(n)])
lo, hi, best = 0, 0, 0

while hi < n:
    while hi < n and time[hi][0] - k < time[lo][1]:
        hi += 1
        best = max(best, hi - lo)
    
    lo += 1

_p(best)

stdout.flush()