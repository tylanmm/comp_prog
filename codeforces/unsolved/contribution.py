n, m = map(int, input().split())
g = {i+1:set() for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

t = list(map(int, input().split()))
sameT = {}
for i in range(n):
    if t[i] in sameT:
        sameT[t[i]].add(i+1)
    else:
        sameT[t[i]] = set([i+1])
    t[i] = (t[i], i+1)
t.sort()

res = [1]*n
for top, blog in t:
    if res[blog-1] == top:
        for b in g[blog]:
            res[b-1] = top + 1
    else:
        print(-1)
        break
else:
    print(' '.join(map(lambda x: str(x[1]), t)))