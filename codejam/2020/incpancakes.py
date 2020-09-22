from math import sqrt
def solve(l, r):
    '''
    i = 1
    n = 0
    while i <= l or i <= r:
        n += 1
        if l >= r:
            l -= i
        else:
            r -= i
        i += 1
    return n, l, r
    '''
    n = int(((-1 + sqrt(1 + 8 * abs(l - r)))/2) + 0.5)
    amt = n * (n + 1) // 2
    if l >= r:
        l -= amt
    else:
        r -= amt
    
    

for i in range(int(input())):
    l, r = map(int, input().split())
    n, l, r = solve(l, r)
    print('Case #%d: %d %d %d' % (i+1, n, l, r))