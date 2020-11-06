def dfs(v, color, comp, graph, cols):
    colors[v] = color
    comps[v] = comp
    cols[color] += 1
    for neighbor, rule in graph[v]:
        if colors[neighbor] == -1:
            dfs(neighbor, color ^ rule, comp, graph, cols)

def solve(n, row1, row2):
    # find positions of numbers 1 - n
    pos = [[] for _ in range(n)]
    for i in range(n):
        pos[row1[i]].append(i)
        pos[row2[i]].append(i)
    
    # build graph, one node for each column
    g = [[] for _ in range(n)]
    for i in range(n):
        # if i does not appear exactly twice, impossible
        if len(pos[i]) != 2:
            print(-1)
            return
        
        # if same number in the same column, skip
        c1, c2 = pos[i]
        if c1 == c2: continue

        # find row that each instance of the number is in
        r1 = 0 if row1[c1] == i else 1
        r2 = 1 if row2[c2] == i else 0

        # connect nodes
        g[c1].append((c2, r1 == r2))
        g[c2].append((c1, r1 == r2))
    
    # color the graph
    compCount = 0
    colorCounts = []
    ans = 0
    for i in range(n):
        if colors[i] == -1:
            colorCount = [0, 0]
            dfs(i, 0, compCount, g, colorCount)
            compCount += 1
            colorCounts.append(colorCount)
            ans += min(colorCount)
    
    # make sure everything is valid
    for i in range(n):
        for v, diff in g[i]:
            if colors[i] ^ colors[v] != diff:
                print(-1)
                return
    
    print(ans)
    for i in range(n):
        change = colorCounts[comps[i]][0] < colorCounts[comps[i]][1]
        if colors[i] ^ change:
            print(i+1, end=' ')
    print()   

for _ in range(int(input())):
    # get input
    n = int(input())
    a1 = list(map(lambda x: int(x)-1, input().split()))
    a2 = list(map(lambda x: int(x)-1, input().split()))
    colors = [-1]*n
    comps = [-1]*n
    solve(n, a1, a2)