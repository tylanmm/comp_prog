dp = [0]*15
dp[2] = 6
for i in range(3, 15):
    dp[i] = dp[i-1]*(i-2)*2
print(dp)