for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    o = e = 0
    for i in range(n):
        if i % 2 and a[i] % 2 == 0:
            o += 1
        elif i % 2 == 0 and a[i] % 2:
            e += 1
    
    if o - e:
        print(-1)
    else:
        print(o)