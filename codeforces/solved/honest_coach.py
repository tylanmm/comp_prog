for _ in range(int(input())):
    n = int(input())
    ath = sorted(list(map(int, input().split())))
    best = ath[-1] - ath[0]
    for i in range(1, n):
        best = min(best, ath[i] - ath[i-1])
    print(best)