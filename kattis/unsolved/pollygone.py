n, P = input().split()
n, P = int(n), float(P)
boxes = []
for _ in range(n):
    e, p = input().split()
    e, p = int(e), float(p)
    boxes.append((e, p))

dp = [[[0,0] for i in range(n+1)] for j in range(n+1)]
minEnergy = float('inf')
for numC in range(1, n+1):
    for numU in range(1, n+1):
        if dp[numC-1][numU-1][1] + boxes[numC-1][1] >= dp[numC-1][numU][1]:
            dp[numC][numU][0] = dp[numC-1][numU-1][0] + boxes[numC-1][0]
            dp[numC][numU][1] = dp[numC-1][numU-1][1] + boxes[numC-1][1]
        else:
            dp[numC][numU][0] = dp[numC-1][numU][0] + boxes[numC-1][0]
            dp[numC][numU][1] = dp[numC-1][numU][1] + boxes[numC-1][1]
        
        if dp[numC][numU][1] >= P:
            minEnergy = min(minEnergy, dp[numC][numU][0])

print(minEnergy)