import sys

with open(sys.argv[1]) as f:
    grid = [list(map(int, line)) for line in f.read().split('\n')]

dirs = [0, -1, 0, 1, 0]
def is_low(i, j):
    for k in range(4):
        if 0 <= i+dirs[k] < len(grid) and 0 <= j+dirs[k+1] < len(grid[i]) and grid[i][j] >= grid[i+dirs[k]][j+dirs[k+1]]:
            return False
    return True

risk_level = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_low(i, j):
            risk_level += grid[i][j] + 1
print(risk_level)

