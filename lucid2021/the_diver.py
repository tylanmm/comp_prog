import heapq

m, n = int(input()), int(input())
grid = [list(map(int, input().split())) for _ in range(m)]
q = [(0, i, j) for i in range(m) for j in range(n) if not grid[i][j]]
MAX = 2147483647
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    dist, i, j = heapq.heappop(q)
    grid[i][j] = min(grid[i][j], dist)
    for di, dj in dirs:
        if di+i < 0 or di+i >= m or dj+j < 0 or dj+j >= n or grid[di+i][dj+j] == -1 or grid[di+i][dj+j] < MAX:
            continue
        heapq.heappush(q, (dist+1, di+i, dj+j))

for row in grid:
    print(*row)