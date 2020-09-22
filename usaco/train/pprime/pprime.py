"""
ID: tylan071
LANG: PYTHON3
TASK: pprime
"""

with open('pprime.in') as f:
    A, B = map(int, f.readline().split())

def isPrime(num):
    for i in range(2, int(num**0.5 + 0.5) + 1):
        if num % i == 0:
            return False
    return True

palindromes = []
for a in range(1, 10, 2):
    palindromes.append(a)
    palindromes.append(a*10 + a)
    for b in range(10):
        palindromes.append(a*100 + b*10 + a)
        palindromes.append(a*1000 + b*100 + b*10 + a)
        for c in range(10):
            palindromes.append(a*10000 + b*1000 + c*100 + b*10 + a)
            palindromes.append(a*100000 + b*10000 + c*1000 + c*100 + b*10 + a)
            for d in range(10):
                palindromes.append(a*1000000 + b*100000 + c*10000 + d*1000 + c*100 + b*10 + a)
                palindromes.append(a*10000000 + b*1000000 + c*100000 + d*1000 + d*10000 + c*100 + b*10 + a)
palindromes.sort()

f = open('pprime.out', 'w')
for n in palindromes:
    if n < A:
        continue
    elif n <= B and isPrime(n):
        f.write(str(n) + '\n')
    elif n > B:
        break
f.close()