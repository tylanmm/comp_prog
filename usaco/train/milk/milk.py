"""
ID: tylan071
LANG: PYTHON3
TASK: milk
"""
import heapq
with open('milk.in') as f:
    n, m = map(int, f.readline().split())
    q = []
    for _ in range(m):
        heapq.heappush(q, tuple(map(int, f.readline().split())))

cost = 0
while n > 0:
    p, a = heapq.heappop(q)
    if n - a >= 0:
        cost += a * p
        n -= a
    else:
        cost += p * n
        n = 0

with open('milk.out', 'w') as f:
    f.write(f'{cost}\n')