from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n = int(_i())
xh, yh, xw, yw = map(int, _i().split())
if xh > xw:
    xh, yh, xw, yw = xw, yw, xh, yh

minx = min(xh, xw)
maxx = max(xh, xw)
miny = min(yh, yw)
maxy = max(yh, yw)

# only want the errands that are in the range defined by home and work
errands = []
for _ in range(n):
    x, y = map(int, _i().split())
    if minx <= x <= maxx and miny <= y <= miny:
        errands.append((x, y))

if yh > yw:
    errands.sort(key=lambda x: x[1], reverse=True)
errands.sort(key=lambda x: x[0])



stdout.flush()