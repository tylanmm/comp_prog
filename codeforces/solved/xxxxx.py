for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    hi = 1 if a[0] % x else -1
    seenR = {a[0] % x: 0}
    for i in range(1, n):
        if a[i] % x:
            hi = max(hi, 1)
        
        a[i] += a[i-1]
        r = a[i] % x
        if r not in seenR:
            seenR[r] = i
        
        if r:
            hi = i + 1
            continue
        for k in seenR:
            if k != r:
                break
        else:
            continue
        
        hi = max(hi, i - seenR[k])
    
    print(hi)