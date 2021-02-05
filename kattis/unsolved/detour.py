from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

class MinHeap:

    def __init__(self, nums=None):
        """Takes an optional parameter nums and initializes the min heap.
        h: the 1-indexed heap
        loc: dictionary that stores the current index of each of the unique entries
        size: current number of elements
        """
        self.h = [None]
        self.loc = {}
        self.size = 0
        if nums:
            for n in nums:
                self.add(n)
    
    def getSize(self):
        return self.size

    def add(self, num):
        """Inserts num into h using min heap algorithm.
        Place num at the end
        While num is less than its parent (at index i//2),
        Swap num with its parent

        Note: if num is already in the heap, it is not inserted.
        """
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
        """Removes min element from the heap using min heap algorithm.
        Replace min element with the number at the end of the list
        While that element is bigger than either of its children,
        Swap that element with the smaller of the two children

        Note: takes optional arg ind to remove the element currently at position ind
        """

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
        """Removes the specified number if in the heap, otherwise returns None"""

        return self.pop(self.loc[num]) if num in self.loc else None
    
    def __str__(self):
        return str(self.h[1:])

# read the input
n, m = map(int, _i().split())
g = [{} for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, _i().split())
    g[a][b] = d
    g[b][a] = d

def dijkstra(graph, src):
    used = [False]*len(graph)
    parent = [None]*len(graph)
    dist = [float('inf') for _ in range(len(graph))]
    dist[src] = 0
    q = MinHeap()
    q.add((0, src))

    while q.getSize() > 0:
        d, src = q.pop()
        used[src] = True
        for neighbor in graph[src]:
            if not used[neighbor] and dist[neighbor] > d + graph[src][neighbor]:
                q.remove((dist[neighbor], neighbor))
                dist[neighbor] = d + graph[src][neighbor]
                q.add((dist[neighbor], neighbor))
                parent[neighbor] = src
    
    return parent

parent = dijkstra(g, 0)

def getPath(curr, parent, path):
    if curr == 0:
        path.append('0')
    else:
        getPath(parent[curr], parent, path)
        path.append(str(curr))

# remove edges that are in the shortest path
curr = 1
while curr:
    g[curr].pop(parent[curr])
    g[parent[curr]].pop(curr)
    curr = parent[curr]

parent = dijkstra(g, 0)
if parent[1] != None:
    path = []
    getPath(1, parent, path)
    _p(str(len(path)) + ' ' + ' '.join(path))
else:
    _p('impossible')

stdout.flush()