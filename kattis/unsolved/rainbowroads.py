n = int(input())
g = {i:set() for i in range(1, n+1)}
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].add((b, c))
    g[b].add((a, c))

goodNodes = []
visited = [False]*(n+1)
def traverse(node, color):
    isGood = visited[node] = True
    roads = set()
    for n, c in g[node]:
        if visited[n]:
            continue
        isGood &= isGood and traverse(n, c)
        roads.add(c)
    
    if isGood and roads:
        goodNodes.append(node)
    return isGood and color not in roads

traverse(1, 0)
goodNodes.sort()
print(len(goodNodes))
print('\n'.join(map(str, goodNodes)))