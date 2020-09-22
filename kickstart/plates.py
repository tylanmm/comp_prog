for i in range(int(input())):
    n, k, p = map(int, input().split())
    stacks = [list(map(int, input().split())) for _ in range(n)]
    take = [0] * n

    total, used, i, j = 0, 0, 0, 0
    while used < p:
        if j < k:
            total += stacks[i][j]
            used += 1
            j += 1
            take[i] += 1
        else:
            j = 0
            i += 1
    
    for j in range(i, n):
        totals = [total]
        for l in range(take[l], k):
            for m in range(0, j):
                totals.append(totals[-1] - )
    