from math import ceil

for t in range(int(input())):
    n, k = map(int, input().split())
    count, time = 0, 0
    intervals = sorted([tuple(map(int, input().split())) for _ in range(n)])
    for s, e in intervals:
        time = max(time, s)
        x = ceil((e - time)/k)
        count += x
        time += x * k
    print('Case #%d: %d' % (t+1, count))