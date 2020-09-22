"""
ID: tylan071
LANG: PYTHON3
TASK: ariprog
"""

with open('ariprog.in') as f:
    n, m = int(f.readline()), int(f.readline())

cap = 2 * m**2
bisquares = [False] * (cap + 1)
for i in range(m+1):
    for j in range(m+1):
        bisquares[i*i + j*j] = True

progs = []
for a in range(cap - n + 1):
    for b in range(1, (cap-a)//(n - 1) + 1):
        for i in range(n):
            if not bisquares[a + b*i]:
                break
        else:
            progs.append((a, b))

progs.sort(key=lambda x:x[1])
with open('ariprog.out', 'w') as f:
    if progs:
        for a, b in progs:
            f.write(f'{a} {b}\n')
    else:
        f.write('NONE\n')