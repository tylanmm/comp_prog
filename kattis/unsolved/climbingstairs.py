from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n, r, k = map(int, _i().split())

# dist between ground and office and registry will cover all the steps
if n - k <= abs(k - r):
    _p(k + abs(k - r) + r)
# you'll need to go up and down on your way to the registry
else:
    _p(k + abs(k - r) + (n - k + abs(k - r)) + r)

stdout.flush()