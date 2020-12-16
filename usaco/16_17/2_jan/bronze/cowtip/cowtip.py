with open(__file__[:-2] + 'in', 'r') as f:
    n = int(f.readline())
    grid = [list(map(int, f.readline().strip())) for _ in range(n)]

def flip(r, c, grid):
    for i in range(r+1):
        for j in range(c+1):
            grid[i][j] ^= 1

amt = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if grid[i][j]:
            flip(i, j, grid)
            amt += 1

with open(__file__[:-2] + 'out', 'w') as f:
    f.write(str(amt) + '\n')