from sys import setrecursionlimit, stdin
setrecursionlimit(1000005)

R, C = map(int, stdin.readline().split())
grid = [list(stdin.readline()) for _ in range(R)]

comps = [[0]*C for _ in range(R)]
dir = [-1, 0, 1, 0, -1]


def dfs(r, c):
    s = [(r, c)]
    while s:
        r, c = s.pop()
        if r < 0 or r >= R or c < 0 or c >= C or comps[r][c] or grid[r][c] != curr:
            continue
        comps[r][c] = comp
        for i in range(4):
            s.append((r+dir[i], c+dir[i+1]))


comp = 0
for i in range(R):
    for j in range(C):
        if not comps[i][j]:
            curr = grid[i][j]
            comp += 1
            dfs(i, j)

for _ in range(int(input())):
    r1, c1, r2, c2 = map(lambda x: int(x)-1, stdin.readline().split())
    if grid[r1][c1] == grid[r2][c2] and comps[r1][c1] == comps[r2][c2]:
        print('binary' if grid[r1][c1] == '0' else 'decimal')
    else:
        print('neither')

# dfs, floodfill
