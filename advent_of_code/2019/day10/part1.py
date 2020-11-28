from sys import argv
from math import gcd

with open(argv[1]) as f:
    grid = f.read().split()
    pos = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                pos.append((i, j))

hi = 0
loc = None
for x1, y1 in pos:
    count = 0

    for x2, y2 in pos:
        if x1 == x2 and y1 == y2: continue

        dx, dy = x2 - x1, y2 - y1
        if dx == 0 or dy == 0:
            gcf = max(abs(dx), abs(dy))
        else:
            gcf = gcd(max(abs(dx), abs(dy)), min(abs(dx), abs(dy)))
        dx //= gcf
        dy //= gcf
        x, y = x1+dx, y1+dy
        
        can_see = True
        while (x, y) != (x2, y2):
            if grid[x][y] == '#':
                can_see = False
                break
            x += dx
            y += dy
        if can_see:
            count += 1
    
    if count > hi:
        hi = count
        loc = (x1, y1)

print(hi, loc)