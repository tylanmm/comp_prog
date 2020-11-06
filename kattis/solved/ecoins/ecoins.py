from collections import deque
from sys import stdin, stdout

def bfs(coins, S):
    seen = [[False]*(S+1) for _ in range(S+1)]
    q = deque([(0, 0, 0)])
    while q:
        v1, v2, amt = q.popleft()
        d = (v1**2 + v2**2)**0.5
        if d > S or seen[v1][v2]:
            continue
        seen[v1][v2] = True
        if abs(d - S) < 0.000001:
            return str(amt)
        
        for x1, x2 in coins:
            q.append((v1+x1, v2+x2, amt+1))
    return 'not possible'

n = int(stdin.readline())
for i in range(n):
    m, S = map(int, stdin.readline().split())
    coins = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
    stdout.write(bfs(coins, S) + '\n')
    if i != n-1:
        stdin.readline()

stdout.flush()