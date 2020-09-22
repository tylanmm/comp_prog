from math import ceil
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a -= b
    if a <= 0:
        print(b)
    elif c <= d:
        print(-1)
    else:
        times = ceil(a / (c-d))
        print(b + c*times)