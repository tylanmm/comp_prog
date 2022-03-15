n, m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
t = [0] * m
prev = [(0, i) for i in range(n)]
for j in range(m):
    curr = []
    for time, i in prev:
        curr.append((max(time, t[j]) + p[i][j], i))
        t[j] = curr[-1][0]
    prev = curr
    prev.sort()

ans = [0] * n
for time, i in prev:
    ans[i] = time
print(*ans)