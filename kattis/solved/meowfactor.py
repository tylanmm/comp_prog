n = int(input())
m = 1
ans = 1
while m**9 <= n:
    if n % int(m**9) == 0:
        ans = m
    m += 1
print(ans)