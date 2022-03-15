r, c = map(int, input().split())
g = [list(input()) for _ in range(r)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j):
    if i < 0 or i >= r or j < 0 or j >= c or g[i][j] == 'W':
        return
    g[i][j] = 'W'
    for di, dj in dirs:
        dfs(i+di, j+dj)


islands = 0
for i in range(r):
    for j in range(c):
        if g[i][j] == 'L':
            dfs(i, j)
            islands += 1
print(islands)
