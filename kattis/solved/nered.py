n, m = map(int, input().split())
grid = [[0]*n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1

for i in range(n):
    for j in range(1, n):
        grid[i][j] += grid[i][j-1]
for j in range(n):
    for i in range(1, n):
        grid[i][j] += grid[i-1][j]

def query(i1, j1, i2, j2):
    ans = grid[i2][j2]
    ans += grid[i1-1][j1-1] if i1 and j1 else 0
    ans -= grid[i1-1][j2] if i1 else 0
    ans -= grid[i2][j1-1] if j1 else 0
    return ans

answer = m
for r in range(1, n+1):
    if m % r or m // r > n: continue
    c = m // r
    for i in range(n-r+1):
        for j in range(n-c+1):
            answer = min(answer, m - query(i, j, i+r-1, j+c-1))
print(answer)