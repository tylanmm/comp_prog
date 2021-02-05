from sys import argv
from math import gcd
from collections import deque

with open(argv[1]) as f:
    grid = f.read().split()
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                pos.append((i, j))

slopes = {}
loc = (34, 30)
for x, y in pos:
    if (x, y) != loc:
        dx, dy = x - loc[0], y - loc[1]
        if dx == 0 or dy == 0:
            gcf = max(abs(dx), abs(dy))
        else:
            gcf = gcd(dx, dy)
        dx //= gcf
        dy //= gcf
        if (dx, dy) not in slopes:
            slopes[(dx, dy)] = []
        slopes[(dx, dy)].append((x, y))

def dist(point):
    return ((point[0] - 34)**2 + (point[1] - 30)**2)**0.5
for p in slopes:
    slopes[p].sort(key=dist)
    slopes[p] = deque(slopes[p])

ordered = sorted(slopes, key=lambda x: x[1]/x[0] if x[0] else float('inf') if x[1] > 0 else -float('inf'))
left, right = [p for p in ordered if p[0] >= 0], [p for p in ordered if p[0] < 0]
ordered = left[::-1] + right[::-1]

count = 0
last = None
while count < 200:
    for p in ordered:
        if slopes[p]:
            poss = slopes[p].popleft()
            count += 1
        if count == 200:
            last = poss
            break
print(last[0]*100 + last[1])