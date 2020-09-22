def gcd(a, b):
    r = a % b
    return gcd(b, r) if r else b

t, sizes = int(input()), list(map(int, input().split()))
for n in sizes:
    print(((n*4 * (n+1))//gcd(n*4, n+1))//(n+1) + 1)