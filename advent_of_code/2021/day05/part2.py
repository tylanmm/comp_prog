import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

grid = [[0]*1000 for _ in range(1000)]
for line in data:
    p1, p2 = line.split(' -> ')
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    if x1 == x2 or y1 == y2: # hor or ver
        for x in range(x1, x2+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                grid[x][y] += 1
    else:
        x, y = x1, y1
        for _ in range(x2 - x1 + 1):
            grid[x][y] += 1
            x += 1
            y += 1 if y2 > y1 else -1

ans = sum([sum([grid[i][j] > 1 for j in range(len(grid[i]))]) for i in range(len(grid))])
print(ans)