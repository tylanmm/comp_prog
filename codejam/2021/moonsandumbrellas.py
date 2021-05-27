def solve(x, y, s):
    dp = [[float('inf')]*2 for _ in range(len(s))]
    if s[0] == '?':   dp[0] = [0, 0]
    elif s[0] == 'C': dp[0][0] = 0
    else:             dp[0][1] = 0

    for i in range(1, len(s)):
        if s[i] == 'C' or s[i] == '?':
            dp[i][0] = min(dp[i-1][0], dp[i-1][1] + y)
        if s[i] == 'J' or s[i] == '?':
            dp[i][1] = min(dp[i-1][0] + x, dp[i-1][1])
    
    return min(dp[-1])

for t in range(1, int(input())+1):
    x, y, s = input().split()
    x, y = int(x), int(y)
    print(f'Case #{t}: {solve(x, y, s)}')