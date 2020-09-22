from sys import stdin
n = int(input())
g = {i:set() for i in range(1, n+1)}
for line in stdin.readlines():
    a, b = map(int, line.split('-'))
    g[a].add(b)
    g[b].add(a)

color = [0]*(n+1)
for j in range(1, 5):
    color[1] = j
    for i in range(2, n+1):
        poss = {1, 2, 3, 4}
        for n in g[i]:
            poss.discard(color[n])
        if poss:
            color[i] = min(poss)
        else:
            break
    else:
        break

for e in g:
    print(e, color[e])