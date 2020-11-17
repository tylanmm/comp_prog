from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

class MinHeap:

    def __init__(self, nums=None):
        self.h = [None]
        self.loc = {}
        self.size = 0
        if nums:
            for n in nums:
                self.add(n)
    
    def add(self, num):
        if num in self.loc: return

        self.h.append(num)
        i = self.size + 1
        self.loc[num] = i
        while i//2 and self.h[i//2] > num:
            self.loc[num], self.loc[self.h[i//2]] = i//2, i
            self.h[i], self.h[i//2] = self.h[i//2], self.h[i]
            i //= 2
        self.size += 1
    
    def pop(self, ind=1):
        if self.size == 0: return
        
        rem = self.h[ind]
        self.loc.pop(rem)

        self.h[ind], i = self.h[-1], ind
        self.loc[self.h[ind]] = ind
        self.h.pop()
        self.size -= 1

        while (i*2 <= self.size and self.h[i] > self.h[i*2]) or (i*2 + 1 <= self.size and self.h[i] > self.h[i*2 + 1]):
            if i*2 + 1 > self.size or self.h[i*2] < self.h[i*2 + 1]:
                self.loc[self.h[i]], self.loc[self.h[i*2]] = i*2, i
                self.h[i], self.h[i*2] = self.h[i*2], self.h[i]
                i = i*2
            else:
                self.loc[self.h[i]], self.loc[self.h[i*2 + 1]] = i*2 + 1, i
                self.h[i], self.h[i*2 + 1] = self.h[i*2 + 1], self.h[i]
                i = i*2 + 1

        return rem

    def remove(self, num):
        return self.pop(self.loc[num]) if num in self.loc else None
    
    def __str__(self):
        return str(self.h[1:])

# read input, set up initial graph
n, m = map(int, _i().split())
g = [[] for _ in range(n+2)]
for _ in range(m):
    u, v, w = map(int, _i().split())
    g[u+1].append((v+1, w))
s, t = map(lambda x: int(x)+1, _i().split())
g[0].append((s, 0))
g[t].append((n+1, 0))

# set up priority queue
q = MinHeap()
q.loc = {(float('inf'), i) : i for i in range(1, n+2)}
q.loc[(0, 0)] = 0
q.h.append((0, 0))
for i in range(1, n+2):
    q.h.append((float('inf'), i))
q.size = n+2

# run dijkstra's, find parents of every node in shortest paths from 0 to n+1
parent = [set() for _ in range(n+2)]
dist = [0] + [float('inf')]*(n+1)
while q.size:
    d, station = q.pop()
    for conn, time in g[station]:
        if d + time < dist[conn]:
            parent[conn] = {station}
            dist[conn] = d + time
            q.remove((conn, dist[conn]))
            q.add((d + time, conn))
        elif d + time == dist[conn]:
            parent[conn].add(station)

# build new graph from dijkstra's parent graph; pretend it's undirected
newG = [set() for _ in range(n+2)]
stack = [n+1]
while stack:
    curr = stack.pop()
    for p in parent[curr]:
        newG[p].add(curr)
        newG[curr].add(p)
        stack.append(p)

# find articulation points
num = [-1]*(n+2)
low = [-1]*(n+2)
parent = [-1]*(n+2)
visited = [0]
isArtPoint = [False]*(n+2)
def findArtPoints(u):
    low[u] = num[u] = visited[0]
    visited[0] += 1
    for v in newG[u]:
        if num[v] == -1:
            parent[v] = u
            findArtPoints(v)
            if num[u] <= low[v]:
                isArtPoint[u] = True
            low[u] = min(low[u], low[v])
        elif v != parent[u]:
            low[u] = min(low[u], num[v])

# write output
findArtPoints(0)
isArtPoint[0] = isArtPoint[-1] = False
for i in range(1, n+1):
    if isArtPoint[i]:
        _p(i-1, ' ')

stdout.flush()