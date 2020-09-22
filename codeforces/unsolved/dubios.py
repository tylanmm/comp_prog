from math import ceil
for _ in range(int(input())):
    l, r, m = map(int, input().split())
    n = max(1, ceil((m + l - r)/r))
    