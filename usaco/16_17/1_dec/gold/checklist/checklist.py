from sys import stdin

H, G = map(int, stdin.readline().split())
hol = [tuple(map(int, stdin.readline().split())) for _ in range(H)]
gue = [tuple(map(int, stdin.readline().split())) for _ in range(G)]

def energy(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

dp = [[[float('inf')]*2 for _ in range(G+1)] for _ in range(H+1)]
dp[1][0][0] = 0
for h in range(1, H+1):
    for g in range(1, G+1):
        fromG = dp[h][g-1][1] + energy(gue[g-2], hol[h-1])
        if h > 1:
            fromH = dp[h-1][g][0] + energy(gue[h-2], hol[h-1])
        dp[h][g][0] = min(fromG, fromH)