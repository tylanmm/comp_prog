def rotate90(grid):
    new_grid = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_grid[-j-1][i] = grid[i][j]
    return new_grid


def slide_0s(row):
    for i in range(4):
        if row[i]:
            while i and not row[i-1]:
                row[i], row[i-1] = row[i-1], row[i]
                i -= 1


def print_grid(grid):
    for row in grid:
        print(*row)


grid = [list(map(int, input().split())) for _ in range(4)]
d = int(input())
for _ in range(d):
    grid = rotate90(grid)

for row in grid:
    slide_0s(row)
    for i in range(1, 4):
        if row[i-1] == row[i]:
            row[i-1] += row[i]
            row[i] = 0
    slide_0s(row)

for _ in range(4 - d):
    grid = rotate90(grid)

print_grid(grid)

# simulation, arrays
