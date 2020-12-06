from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

g = None
matched = None
visited = None

def augmenting_path(u):
    if visited[u]:
        return 0
    visited[u] = True

    for v in g[u]:
        if matched[v] == -1 or augmenting_path(matched[v]):
            matched[u] = v
            return 1
    return 0

def solve():
    global g, matched, visited

    n, m = map(int, _i().split())
    
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(lambda x: int(x)-1, _i().split())
        g[a].append(b)
        g[b].append(a)
    
    matched = [-1] * (n)
    mcbm = 0
    for i in range(n):
        visited = [False]*n
        mcbm += augmenting_path(i)
    if n - mcbm:
        return _p('Impossible')
    
    _p('\n'.join(map(lambda x: str(x+1), matched)))

solve()

stdout.flush()