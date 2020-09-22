n, b = map(int, input().split())
row = [1, 2]
def gen_primes(n):
    sieve = [True] * (n+1)
    for i in range(2, n//2):
        if not sieve[i]:
            continue
        for j in range(2*i, n+1, i):
            sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]

primes = gen_primes(1000)
row = [1, 2]
while len(row) < n:
    pass