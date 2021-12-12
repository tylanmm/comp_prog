import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

# build graph
g = {}
for line in data:
    a, b = line.split('-')
    if a not in g: g[a] = set()
    if b not in g: g[b] = set()
    g[a].add(b)
    g[b].add(a)

seen = set()

def dfs(cave):
    if cave == 'end': return 1
    
    # only mark as visited if it's a small cave
    if cave[0] >= 'a':
        seen.add(cave)
    
    # recur at each neighbor
    total = 0
    for adj in g[cave]:
        if adj not in seen:
            total += dfs(adj)
    
    # unmark this cave so it can be used later
    seen.discard(cave)
    
    return total
        
print(dfs('start'))