for _ in range(int(input())):
    A, B, x, y, N = map(int, input().split())
    
    # Give priority to A
    a, b, n = A, B, N
    if a - x < n:
        n -= a - x
        a = x
    else:
        a -= n
        n = 0
    
    if n:
        if b - y < n:
            b = y
        else:
            b -= n
    ans = a * b
    
    # Do again, give priority to B
    a, b, n = A, B, N
    if b - y < n:
        n -= b - y
        b = y
    else:
        b -= n
        n = 0
    
    if n:
        if a - x < n:
            a = x
        else:
            a -= n

    print(min(ans, a * b))