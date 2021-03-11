from sys import stdin, stdout, setrecursionlimit
import heapq

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

h, w = map(int, _i().split())
grid = [list(map(int, _i().split())) for _ in range(h)]
i, j = map(lambda x: int(x) - 1, _i().split())

dirs = [(-1, -1), (-1, 0), (-1, 1),
         (0, -1),  (0, 0), (0, 1),
         (1, -1),  (1, 0), (1, 1)]

pq = [(grid[i][j], -float('inf'), i, j)]
total = 0
while pq:
    alt, prev, i, j = heapq.heappop(pq)
    if grid[i][j] >= 0:
        continue
    prev = max(prev, alt)
    grid[i][j] = 0
    total += abs(prev)

    for di, dj in dirs:
        if (i + di >= 0) and (i + di < h) and (j + dj >= 0) and (j + dj < w) and (grid[i+di][j+dj] < 0):
            heapq.heappush(pq, (grid[i+di][j+dj], prev, i+di, j+dj))
    
_p(total)

stdout.flush()