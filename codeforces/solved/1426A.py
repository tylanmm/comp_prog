from math import ceil
for _ in range(int(input())):
    n, x = map(int, input().split())
    print(1 if n <= 2 else ceil((n - 2) / x) + 1)