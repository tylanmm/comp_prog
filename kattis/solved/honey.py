dp = [[[0]*29 for _ in range(29)] for _ in range(15)]
dp[0][14][14] = 1

dirs = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
for t in range(14):
    for i in range(29):
        for j in range(29):
            for di, dj in dirs:
                if 0 <= i+di < 29 and 0 <= j+dj < 29:
                    dp[t+1][i+di][j+dj] += dp[t][i][j]

for _ in range(int(input())):
    n = int(input())
    print(dp[n][14][14])

# 3D dp
