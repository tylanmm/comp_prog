n, w = map(int, input().split())
# dp[i][j] = max revenue for j seats sold by week i
dp = [[0]*(n+1) for _ in range(w+2)]
for i in range(w+1):
    k, *nums = list(map(int, input().split()))
    for p in range(k):
        price, seats = nums[p], nums[p+k]
        for j in range(n):
            if dp[i][j] or (i == 0 and j == 0):
                dp[i+1][j+seats] = max(dp[i+1][j+seats], dp[i][j] + price*)
max([dp[i][n] for i in range(w)])
