from math import ceil

for t in range(int(input())):
    n, x = map(int, input().split())
    q = list(map(int, input().split()))
    res = [(ceil(q[i]/x), i+1) for i in range(n)]
    res.sort()

    print('Case #%d:' % (t+1), end='')
    for amt, i in res:
        print(' %d' % i, end='')
    print()