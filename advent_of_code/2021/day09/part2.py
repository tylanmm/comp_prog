import sys

with open(sys.argv[1]) as f:
    grid = [list(map(int, line)) for line in f.read().split('\n')]

dirs = [0, -1, 0, 1, 0]
def is_low(i, j):
    for k in range(4):
        if 0 <= i+dirs[k] < len(grid) and 0 <= j+dirs[k+1] < len(grid[i]) and grid[i][j] >= grid[i+dirs[k]][j+dirs[k+1]]:
            return False
    return True

low = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_low(i, j):
            low.append((i, j))

def dfs(i, j):
    if grid[i][j] == 9: 
        return 0
    total = 1
    grid[i][j] = 9
    for k in range(4):
        di, dj = dirs[k], dirs[k+1]
        if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[i]):
            total += dfs(i+di, j+dj)
    return total

basins = []
for i, j in low:
    basins.append(dfs(i, j))
basins.sort()
print(basins[-1] * basins[-2] * basins[-3])

