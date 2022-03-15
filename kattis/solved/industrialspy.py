from itertools import permutations

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

c = int(input())
for _ in range(c):
    digits = input()
    primes = set()
    for r in range(1, len(digits)+1):
        for perm in permutations(digits, r):
            num = int(''.join(perm))
            if is_prime(num):
                primes.add(num)
    print(len(primes))