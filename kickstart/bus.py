for i in range(int(input())):
    n, d = map(int, input().split())
    buses = list(map(int, input().split()))
    for j in range(n-1, -1, -1):
        d -= d % buses[j]
    print('Case #%d: %d' % (i+1, d))