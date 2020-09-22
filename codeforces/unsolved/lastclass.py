def firstPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i
    return n

for _ in range(int(input())):
    n = int(input())
    fac = firstPrime(n)
    print(n//fac, n - n//fac)