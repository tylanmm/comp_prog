import sys
import heapq

grid = [list(map(int, line)) for line in sys.stdin.read().split('\n')]
R, C = len(grid), len(grid[0])

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

print(dijkstras(grid, (0, 0), (R-1, C-1)))