for i in range(int(input())):
    n, b = map(int, input().split())
    costs = list(map(int, input().split()))
    costs.sort(reverse=True)
    total = 0
    while len(costs) > 0 and b > 0:
        top = costs.pop()
        if top <= b:
            total += 1
            b -= top
        else:
            break
    print('Case #%d: %d' % (i+1, total))