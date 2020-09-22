for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    
    if (b//a ^ -b//a)//-2 == b//a:
        res = 0
        b //= a
        for i in range(3, 0, -1):
            while b >> i > 0:
                b >>= i
                res += 1
        print(res)
    else:
        print(-1)