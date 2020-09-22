"""
ID: tylan071
LANG: PYTHON3
TASK: frac1
"""

def gcd(a, b):
    return gcd(b, a%b) if a%b else b

fracs = {(0, 1), (1, 1)}
with open('frac1.in') as f:
    n = int(f.readline())

for numer in range(1, n+1):
    for denom in range(numer+1, n+1):
        GCD = gcd(denom, numer)
        fracs.add((numer//GCD, denom//GCD))

fracs = sorted(list(fracs), key=lambda x: x[0]/x[1])

with open('frac1.out', 'w') as f:
    for numer, denom in fracs:
        f.write(f'{numer}/{denom}\n')