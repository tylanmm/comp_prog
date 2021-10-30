from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(400000)

def _i():
    return stdin.readline()

def _p(x):
    stdout.write(str(x) + '\n')

def dfs(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v)

n, m = map(int, _i().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, _i().split())
    g[a].append(b)
    g[b].append(a)

visited = [False]*n
dfs(0)

conn = True
for i in range(n):
    if not visited[i]:
        _p(i+1)
        conn = False

if conn:
    _p('Connected')

stdout.flush()
