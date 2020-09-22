"""
ID: tylan071
LANG: PYTHON3
TASK: sprime
"""

with open('sprime.in') as f:
    n = int(f.read())

def isPrime(num):
    for i in range(2, int(num**0.5 + 0.5) + 1):
        if num % i == 0:
            return False
    return True

ribs = [2, 3, 5, 7]
for _ in range(n-1):
    res = []
    for rib in ribs:
        for i in range(1, 10, 2):
            num = rib * 10 + i
            if isPrime(num):
                res.append(num)
    ribs = res

with open('sprime.out', 'w') as f:
    for r in ribs:
        f.write(f'{r}\n')