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

def dfs(cave, double):
    if cave == 'end': return 1
    
    # if we've been to this small cave before
    if cave in seen:
        # can only be here if:
        #   1) haven't doubled already
        #   2) it's not the start
        if double or cave == 'start':
            return 0
        double = cave
    
    # only mark as visited if it's a small cave
    elif cave[0] >= 'a':
        seen.add(cave)
        
    # recur at each neighbor
    total = 0
    for adj in g[cave]:
        total += dfs(adj, double)
    
    # unmark this cave so it can be used later
    if cave != double: seen.discard(cave)
    
    return total

print(dfs('start', ''))