class UFDS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.size = [1]*n

    def findSet(self, i):
        p = self.parent[i]
        while i != p:
            self.parent[i] = self.parent[p]
            i = p
            p = self.parent[i]
        return i

    def groupSize(self, i):
        return self.size[self.findSet(i)]

    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)
    
    def union(self, i, j):
        x, y = self.findSet(i), self.findSet(j)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                self.rank[x] += 1 if self.rank[x] == self.rank[y] else 0

n, q = map(int, input().split())
groups = UFDS(n+1)
for _ in range(q):
    line = input().split()
    if line[0] == 't':
        groups.union(int(line[1]), int(line[2]))
    else:
        print(groups.groupSize(int(line[1])))