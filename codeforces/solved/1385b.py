for _ in range(int(input())):
    n = int(input())
    res = []
    seen = [False]*(n+1)
    for num in map(int, input().split()):
        if not seen[num]:
            res.append(num)
            seen[num] = True
    print(*res)