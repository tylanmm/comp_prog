import sys
import heapq

# prep grid
g = [list(map(int, line)) for line in sys.stdin.read().split('\n')]
R, C = len(g), len(g[0])
for i in range(R):
    g[i] *= 5
for _ in range(4):
    for i in range(R):
        g.append(g[i].copy())

# adjust values
for k in range(5):
    for i in range(k*R, k*R + R):
        for j in range(C*5):
            if i >= R:
                g[i][j] = g[i-R][j] + 1
            elif j >= C:
                g[i][j] = g[i][j-C] + 1
            if g[i][j] == 10:
                g[i][j] = 1

R *= 5; C *= 5

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dijkstras(grid, src, dst):
    q = [(0, src[0], src[1])]
    seen = [[False]*C for i in range(R)]
    while q:
        d, r, c = heapq.heappop(q)
        if seen[r][c]: continue
        if r == dst[0] and c == dst[1]: return d
        seen[r][c] = True
        for dr, dc in dirs:
            if 0 <= r+dr < R and 0 <= c+dc < C and not seen[r+dr][c+dc]:
                heapq.heappush(q, (d+grid[r+dr][c+dc], r+dr, c+dc))

print(dijkstras(g, (0, 0), (R-1, C-1)))