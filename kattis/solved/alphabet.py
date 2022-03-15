from string import ascii_lowercase

s = input()
alpha = ascii_lowercase
dp = [[0]*(len(s)+1) for _ in range(len(alpha)+1)]

for i in range(1, len(alpha)+1):
    for j in range(1, len(s)+1):
        if i and j:
            dp[i][j] = dp[i-1][j-1] + (alpha[i-1] == s[j-1])
        if i:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j:
            dp[i][j] = max(dp[i][j], dp[i][j-1])

print(26 - dp[-1][-1])
