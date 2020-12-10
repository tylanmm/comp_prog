import sys

with open(sys.argv[1]) as f:
    grid = f.read().split()

def solve(r, d):
    i = j = count = 0
    while i < len(grid):
        count += grid[i][j] == '#'
        j = (j + r) % len(grid[i])
        i += d
    return count

res = 1
res *= solve(1, 1)
res *= solve(3, 1)
res *= solve(5, 1)
res *= solve(7, 1)
res *= solve(1, 2)
print(res)