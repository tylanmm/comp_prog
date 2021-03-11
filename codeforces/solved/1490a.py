from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

for _ in range(int(_i())):
    n = int(_i())
    a = list(map(int, _i().split()))
    ans = 0
    for i in range(n-1):
        while a[i] / a[i+1] > 2:
            ans += 1
            a[i] = (a[i] >> 1) + (a[i] & 1)
        while a[i+1] / a[i] > 2:
            ans += 1
            a[i] <<= 1
    _p(ans)

stdout.flush()