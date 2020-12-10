import sys

with open(sys.argv[1]) as f:
    g = {}
    while True:
        try:
            a, b = f.readline().strip().split(')')
            if a in g:
                g[a].append(b)
            else:
                g[a] = [b]
            
            if b in g:
                g[b].append(a)
            else:
                g[b] = [a]

        except ValueError:
            break

visited = set()
def dfs(obj, goal, d):
    visited.add(obj)
    if obj == goal:
        return d
    for n in g[obj]:
        if n not in visited:
            dist = dfs(n, goal, d+1)
            if dist: return dist

print(max(1, dfs('YOU', 'SAN', 0)-2))