from sys import setrecursionlimit

with open('pageant.in') as f:
    n, m = map(int, f.readline().split())
    grid = [f.readline().strip() for _ in range(n)]

setrecursionlimit(200000)
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
group = [None, set(), set()]
def dfs(r, c, comp):
    if r < 0 or r >= n or c < 0 or c >= m or comps[r][c] != 0 or grid[r][c] != 'X':
        return
    comps[r][c] = comp
    group[comp].add((r, c))
    for dr, dc in dir:
        dfs(r + dr, c + dc, comp)

comp_num = 1
comps = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.' and comps[i][j] == 0:
            dfs(i, j, comp_num)
            comp_num += 1

lo = m + n
for r1, c1 in group[1]:
    for r2, c2 in group[2]:
        lo = min(lo, abs(r1 - r2) + abs(c1 - c2) - 1)

with open('pageant.out', 'w') as f:
    f.write(str(lo) + '\n')