def factorial(n):
    if n <= 1:
        return 1
    end = n
    for i in range(2, n):
        end *= i
    return end

def choose(n, r):
    if r <= 0 or n <= 1:
        return 1
    return factorial(n) // (factorial(r) * factorial(n-r))

for j in range(int(input())):
    w, h, l, u, r, d = map(int, input().split())
    
    fall = 0
    if u >= 2:
        for i in range(l, r):
            fall += choose(i+u-3, u-2) * ((0.5) ** (i + u - 2))
        if r != w:
            fall += choose(r+u-3, u-2) * ((0.5) ** (r + u - 2))
        else:
            for i in range(0, u):
                fall += choose(i+r-1, i) * ((0.5) ** (r + i - 1))

    if l >= 2:
        for i in range(u, d):
            fall += choose(i+l-3, l-2) * ((0.5) ** (i + l - 2))
        if d != h:
            fall += choose(d+l-3, l-2) * ((0.5) ** (d + l - 2))
        else:
            for i in range(0, l):
                fall += choose(i+d-1, i) * ((0.5) ** (d + i - 1))
    
    if fall > 1:
        fall = 1.0
    print('Case #%d: %f' % (j+1, 1 - fall))