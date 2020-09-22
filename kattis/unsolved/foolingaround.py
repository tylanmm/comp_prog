isPrime = [True] * 101
isPrime[0] = isPrime[1] = False
for i in range(2, 101//2):
    if isPrime[i]:
        for j in range(i*2, 101, i):
            isPrime[j] = False
primes = [i for i in range(2, 101) if isPrime[i]]
print(primes)
'''
for _ in range(int(input())):
    pass
'''