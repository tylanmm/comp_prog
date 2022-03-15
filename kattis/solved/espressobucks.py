n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.': continue
        for di, dj in dirs:
            if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == 'E':
                break
        else:
            grid[i][j] = 'E'
for row in grid:
    print(''.join(row))