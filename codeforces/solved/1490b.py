from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

for t in range(int(_i())):
    n = int(_i())
    a = list(map(int, _i().split()))
    rem = [0, 0, 0]
    for num in a:
        rem[num % 3] += 1
    ans = 0
    for i in range(6):
        diff = rem[i%3] - n//3
        if diff > 0:
            rem[(i+1)%3] += diff
            rem[i%3] = n//3
            ans += diff
    _p(ans)

stdout.flush()