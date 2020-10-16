for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    pos, zer, neg = [], [], []
    posSum, negSum = 0, 0
    for num in a:
        if num < 0:
            neg.append(num)
            negSum += num
        elif num > 0:
            pos.append(num)
            posSum += num
        else:
            zer.append(num)
    
    ans = []
    if posSum > -negSum:
        ans = pos + neg + zer
    elif posSum < -negSum:
        ans = neg + pos + zer
    else:
        ans = []
    
    if ans:
        print('YES')
        print(*ans)
    else:
        print('NO')
    