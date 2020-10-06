n = int(input())
costs = sorted(list(map(int, input().split())))
m = int(input())
orders = list(map(int, input().split()))

dp = [0] * (max(orders) + 1)
dp[0] = []
for total in range(1, len(dp)):
    for i in range(n):
        c = costs[i]
        if c > total: break
        if dp[total-c] == 2:
            dp[total] = 2
            break
        elif dp[total] and (dp[total-c] == 2 or dp[total-c] == []):
            dp[total] = 2
            break
        elif dp[total-c] == []:
            dp[total] = [i+1]
        elif dp[total-c] != 0 and dp[total-c][-1] <= c:
            dp[total] = dp[total-c] + [i+1]

for o in orders:
    if dp[o] == 0:
        print('Impossible')
    elif dp[o] == 2:
        print('Ambiguous')
    else:
        print(*dp[o])