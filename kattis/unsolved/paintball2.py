class Shooter:

    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist
        self.xmin = max(0, x-dist)
        self.xmax = min(1000, x+dist)
        self.ymin = max(0, y-dist)
        self.ymax = min(1000, y+dist)

    def calcDist(self, other):
        deltax = self.x - other.x
        deltay = self.y - other.y
        return (deltax*deltax + deltay*deltay)**0.5
    
    def overlaps(self, other):
        return self.calcDist(other) < (self.dist + other.dist)
    
    def updateBounds(self, other):
        self.xmin = min(self.xmin, other.xmin)
        self.xmax = max(self.xmax, other.xmax)
        self.ymin = min(self.ymin, other.ymin)
        self.ymax = max(self.ymax, other.ymax)
    
    def blocks(self):
        return self.ymin == 0 and self.ymax == 1000

class UFDS:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def findSet(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.findSet(self.parent[i])
        return self.parent[i]

    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)
    
    def union(self, i, j):
        x, y = self.findSet(i), self.findSet(j)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                self.rank[x] += 1 if self.rank[x] == self.rank[y] else 0

n = int(input())
shooters = []
for _ in range(n):
    x, y, r = map(int, input().split())
    shooters.append(Shooter(x, y, r))

sets = UFDS(n)
for i in range(n):
    si = shooters[i]
    for j in range(i+1, n):
        sj = shooters[j]
        if si.overlaps(sj):
            sets.union(i, j)
            si.updateBounds(sj)
            sj.updateBounds(si)

canDo = True
bestEntry = 0
bestExit = 0
for i in range(n):
    if sets.parent[i] == i:
        si = shooters[i]
        canDo &= not si.blocks()
        bestEntry = max(bestEntry, si.ymax if (xmin != 0 ))