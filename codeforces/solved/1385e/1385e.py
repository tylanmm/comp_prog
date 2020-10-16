# just dfs + placing node in order after processing all neighbors
def topo(node):
    visited[node] = True
    for neighbor in g[node]:
        if not visited[neighbor]:
            topo(neighbor)
    order.append(node)

for _ in range(int(input())):
    # read in data
    n, m = map(int, input().split())
    edges = []
    g = [[] for i in range(n)]

    for i in range(m):
        t, x, y = map(int, input().split())
        edges.append((x-1, y-1))
        # only place edge in graph if it's directed
        if t:
            g[x-1].append(y-1)
    
    # do topological sort
    visited = [False]*n
    order = []
    for i in range(n):
        if not visited[i]:
            topo(i)
    order.reverse()
    
    # store position of nodes for easy access
    pos = [0]*n
    for i in range(n):
        pos[order[i]] = i
    
    # check for a cycle
    hasCycle = False
    for i in range(n):
        for node in g[i]:
            if pos[i] > pos[node]:
                hasCycle = True
    
    if hasCycle:
        print('NO')
    else:
        print('YES')
        for a, b in edges:
            if pos[a] < pos[b]:
                print(a+1, b+1)
            else:
                print(b+1, a+1)