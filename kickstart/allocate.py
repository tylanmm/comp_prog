for i in range(int(input())):
    n, b = map(int, input().split())
    costs = sorted(list(map(int, input().split())), reverse=True)
    while len(costs) > 0 and b > 0 and costs[-1] <= b:
        b -= costs.pop()
    print('Case #%d: %d' % (i+1, n-len(costs)))