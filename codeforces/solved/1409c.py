for _ in range(int(input())):
    n, x, y = map(int, input().split())

    d = y - x
    for i in range(1, y - x):
        if (y - x) % i == 0 and (y - x) // i + 1 <= n:
            d = i
            break
    
    a1 = x
    while a1 - d > 0 and a1 - d + (d*(n-1)) >= y:
        a1 -= d
    
    terms = [str(a1+(d*i)) for i in range(n)]
    print(' '.join(terms))