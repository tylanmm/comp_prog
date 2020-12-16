import sys
from math import ceil

with open(sys.argv[1]) as f:
    t = int(f.readline())
    data = f.read().split(',')

lo = float('inf')
best = float('inf')
for n in data:
    if n == 'x':
        continue

    n = int(n)
    time = n * ceil(t / n)
    if time < best:
        best = time
        lo = n

print(lo * (best - t))