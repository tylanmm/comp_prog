n, m = map(int, input().split())
colors = 'ROYGBIV'
g = {i:set() for i in range(1, n+1)}
for _ in range(m):
    l1, l2, d, c = input().split()
    l1, l2, d = map(int, [l1, l2, d])
    c = colors.index(c)
    g[l1].add((l2, d, c))
    g[l2].add((l1, d, c))
print(g)