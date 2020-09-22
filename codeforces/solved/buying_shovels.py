from math import sqrt

def gf(n, k):
    hi = 1
    for i in range(1, min(k, int(sqrt(n)))+1):
        if n % i == 0:
            if n // i <= k:
                hi = max(hi, n//i)
            else:
                hi = max(hi, i)
    return hi

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(n // gf(n, k))