n, m = map(int, input().split())
k, r = map(int, input().split())
straight = [int(input()) for _ in range(n)]
curve = [tuple(map(int, input().split())) for _ in range(n-1)]

dp = [[0]*(m) for i in range(n)]
for lane in range(m):
    if lane*k <= straight[0]:
        dp[0][lane] = straight[0] + lane*r + curve[0][0] + curve[0][1]*(lane+1)

for seg in range(1, n-1):
    for lane in range(m):
        minDist, minLane = float('inf'), 0
        for prevLane in range(m):
            if dp[seg-1][prevLane] and abs(lane - prevLane)*k <= straight[seg]:
                if dp[seg-1][prevLane] < minDist:
                    minDist = dp[seg-1][prevLane]
                    minLane = prevLane
        dp[seg][lane] = minDist + straight[seg] + abs(minLane - lane)*r + curve[seg][0] + curve[seg][1]*(lane+1)

print(dp[-2][0] + straight[-1])