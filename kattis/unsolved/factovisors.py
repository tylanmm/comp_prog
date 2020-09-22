from sys import stdin

primes = []
sieve = [False]*47000
sieve[0] = sieve[1] = True
for i in range(2, 47000):
    if sieve[i]:
        continue
    primes.append(i)
    for j in range(i*i, 47000, i):
        sieve[j] = True

def getFactors(n):
    factors = {}
    prime, pI = 2, 0
    while prime*prime <= n:
        if n % prime == 0:
            if prime not in factors:
                factors[prime] = 0
            factors[prime] += 1
            n //= prime
        else:
            pI += 1
            prime = primes[pI]
    if n != 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors

def getFactorialFactors(n):
    factors = {}
    for i in range(2, n+1):
        fact = getFactors(i)
        for f in fact:
            if f in factors:
                factors[f] += fact[f]
            else:
                factors[f] = fact[f]
    return factors

for line in stdin.readlines():
    n, m = map(int, line.split())
    mFact = getFactors(m)
    if max(mFact) > n:
        print(f'{m} does not divide {n}!')
        continue
    
    nFact = getFactorialFactors(n)
    for f in mFact:
        if f not in nFact or nFact[f] < mFact[f]:
            print(f'{m} does not divide {n}!')
            break
    else:
        print(f'{m} divides {n}!')