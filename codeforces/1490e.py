from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

for t in range(int(_i())):
    n = int(_i())
    a = map(int, _i().split())
    a = sorted([(num, i+1) for i, num in enumerate(a)], reverse=True)

    total = sum([a[i][0] for i in range(n)])
    prev = a[0][0]
    pending = 0
    totals = [0]*n
    for i in range(n):
        if a[i][0] != prev:
            total -= pending
            pending = 0
        pending += a[i][0]
        totals[i] = total


    

stdout.flush()