from sys import stdin, stdout

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

a = []
res = []

def depth(lo, hi, d):
    if lo > hi:
        return
    if lo == hi:
        res[lo] = d
        return
    
    hii = lo
    for i in range(lo+1, hi+1):
        if a[i] > a[hii]:
            hii = i
    res[hii] = d
    depth(lo, hii-1, d+1)
    depth(hii+1, hi, d+1)

for t in range(int(_i())):
    n = int(_i())
    a = list(map(int, _i().split()))
    res = [0]*n
    depth(0, n-1, 0)
    _p(' '.join(map(str, res)))

stdout.flush()