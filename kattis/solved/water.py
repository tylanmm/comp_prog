from collections import deque

n, p, k = map(int, input().split())
g = [{} for _ in range(n+1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    g[a][b] = c
    g[b][a] = c


def bfs():
    dist = [-1]*(n+1)
    parent = list(range(n+1))
    bottleneck = [float('inf')]*(n+1)
    dist[1] = 0

    q = deque([1])
    while q:
        u = q.popleft()
        if u == 2:
            break
        for v in g[u]:
            if g[u][v] > 0 and dist[v] == -1:
                parent[v] = u
                dist[v] = dist[u] + 1
                bottleneck[v] = min(bottleneck[u], g[u][v])
                q.append(v)

    return dist, parent, bottleneck


def reduce(parent, f):
    curr = 2
    while curr != 1:
        g[parent[curr]][curr] -= f
        g[curr][parent[curr]] += f
        curr = parent[curr]


def flow():
    dist, parent, bottleneck = bfs()
    gain = 0
    while dist[2] != -1:
        f = bottleneck[2]
        reduce(parent, f)
        gain += f
        dist, parent, bottleneck = bfs()
    return gain


f = flow()
print(f)
for _ in range(k):
    a, b, c = map(int, input().split())
    if a in g[b]:
        g[a][b] += c
        g[b][a] += c
    else:
        g[a][b] = c
        g[b][a] = c
    f += flow()
    print(f)

# network flow, max flow, min cut
