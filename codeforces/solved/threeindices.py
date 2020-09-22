for _ in range(int(input())):
    n, p = int(input()), list(map(int, input().split()))
    biggerL, biggerR = [-1]*n, [-1]*n
    lLo, lLoI = p[0], 0
    rLo, rLoI = p[-1], n-1
    for i in range(1, n-1):
        if p[i] > lLo:
            biggerL[i] = lLoI
        elif p[i] < lLo:
            lLo = p[i]
            lLoI = i
        
        if p[-i-1] > rLo:
            biggerR[-i-1] = rLoI
        elif p[-i-1] < rLo:
            rLo = p[-i-1]
            rLoI = n - i - 1
    
    for i in range(1, n-1):
        if biggerL[i] > -1 and biggerR[i] > -1:
            print('YES')
            print(biggerL[i]+1, i+1, biggerR[i]+1)
            break
    else:
        print('NO')