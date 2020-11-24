from sys import setrecursionlimit

# read in data, store graph, store friends as queries
with open('milkvisits.in') as f:
    n, m = map(int, f.readline().split())
    type = f.readline()
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = map(lambda x: int(x)-1, f.readline().split())
        g[x].append(y)
        g[y].append(x)

    queries = []
    for _ in range(m):
        a, b, c = f.readline().split()
        a = int(a) - 1
        b = int(b) - 1
        queries.append((a, b, c))

# regular dfs, but use component number to mark something as visited
setrecursionlimit(200000)
comp = [0] * n
def dfs(farm, c):
    comp[farm] = c
    for neighbor in g[farm]:
        if type[neighbor] == type[farm] and comp[neighbor] == 0:
            dfs(neighbor, c)

# find components, using milk type to break them up
comp_num = 1
for i in range(n):
    if comp[i] == 0:
        dfs(i, comp_num)
        comp_num += 1

# answer queries
res = []
for a, b, c in queries:
    if comp[a] != comp[b] or type[a] == c:
        res.append('1')
    else:
        res.append('0')

with open('milkvisits.out', 'w') as f:
    f.write(''.join(res) + '\n')