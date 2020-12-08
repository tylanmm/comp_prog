import sys

with open(sys.argv[1]) as f:
    rules = f.read().split('\n')

g = {}
for r in rules:
    r = r.split(' bag')
    p = r[0]
    for color in r[1:]:
        color = ' '.join(color.split()[-2:])
        if color == 'no other':
            break
        if color not in g:
            g[color] = set()
        g[color].add(p)

def dfs(color):
    visited.add(color)
    if color not in g:
        return
    for p in g[color]:
        if p not in visited:
            dfs(p)

visited = set()
dfs('shiny gold')
print(len(visited)-1)