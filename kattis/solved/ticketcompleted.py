from sys import setrecursionlimit

setrecursionlimit(100005)

n, m = map(int, input().split())
g = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)


def dfs(u, comp_num):
    comp[u] = comp_num
    for v in g[u]:
        if not comp[v]:
            dfs(v, comp_num)


comp = [0]*(n+1)
comp_num = 0
for u in range(1, n+1):
    if not comp[u]:
        comp_num += 1
        dfs(u, comp_num)

comp_size = [0]*(comp_num+1)
for c in comp:
    comp_size[c] += 1

total = 0
for s in comp_size:
    total += s * (s-1) // 2

print(total / (n * (n-1) // 2))
