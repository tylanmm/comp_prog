import sys

with open(sys.argv[1]) as f:
    grid = f.read().split()

i = j = count = 0
while i < len(grid):
    count += grid[i][j] == '#'
    j = (j + 3) % len(grid[i])
    i += 1

print(count)