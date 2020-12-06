from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

g = None
matched = None
visited = None

def augmenting_path(pair, i):
    if pair in visited:
        return 0
    visited.add(pair)

    for res, op in g[i]:
        if matched[res] == -1 or augmenting_path(matched[res][0], matched[res][1]):
            matched[res] = (pair, i)
            matched[pair] = (res, op)
            return 1
    return 0

def solve():
    global g, matched, visited

    n = int(_i())
    pairs = [tuple(map(int, _i().split())) for _ in range(n)]
    g = [[] for _ in range(n)]
    matched = {pairs[i]:-1 for i in range(n)}
    for i, p in enumerate(pairs):
        g[i].append((p[0] + p[1], '+'))
        matched[p[0] + p[1]] = -1
        g[i].append((p[0] - p[1], '-'))
        matched[p[0] - p[1]] = -1
        g[i].append((p[0] * p[1], '*'))
        matched[p[0] * p[1]] = -1

    mcbm = 0
    for i in range(n):
        visited = set()
        mcbm += augmenting_path(pairs[i], i)

    if mcbm != n:
        return _p('impossible')
    for x, y in pairs:
        _p('%d %s %d = %d' % (x, matched[(x, y)][1], y, matched[(x, y)][0]))

solve()

stdout.flush()