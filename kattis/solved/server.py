n, T = map(int, input().split())
ans = 0
for t in map(int, input().split()):
    if T - t >= 0:
        ans += 1
    T -= t
    if T <= 0:
        break
print(ans)
