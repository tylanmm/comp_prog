from sys import stdin, stdout

primes = []
sieve = [0]*1500
for i in range(2, 1500):
    if sieve[i]:
        continue
    sieve[i] += 1
    primes.append(i)
    for j in range(i*2, 1500, i):
        sieve[j] += 1

def numNonPrimeFactors(n):
    count, total = 0, 1
    prime, pI = 2, 0
    while prime*prime <= n:
        if n % prime == 0:
            count += 1
            n //= prime
        else:
            total *= count + 1
            count = 0
            pI += 1
            prime = primes[pI]
    
    if n == prime:
        total *= count + 2
    elif n != 1:
        total *= 2
        total *= count + 1
        
    return total - sieve[n]

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    stdout.write(str(numNonPrimeFactors(n)) + '\n')