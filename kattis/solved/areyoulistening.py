from math import floor

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

cx, cy, n = map(int, input().split())
p = [tuple(map(int, input().split())) for _ in range(n)]
res = float('inf')
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            di = dist(cx, cy, p[i][0], p[i][1]) - p[i][2]
            dj = dist(cx, cy, p[j][0], p[j][1]) - p[j][2]
            dk = dist(cx, cy, p[k][0], p[k][1]) - p[k][2]
            res = min(res, max(di, dj, dk))
print(max(floor(res), 0))