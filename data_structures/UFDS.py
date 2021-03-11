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
                self.rank[x] += self.rank[x] == self.rank[y]

if __name__ == '__main__':
    ufds = UFDS(5)
    print(ufds.parent)
    print(ufds.rank)

    print(ufds.findSet(0))
    print(ufds.isSameSet(0, 1))
    ufds.union(0, 1)

    print(ufds.parent)
    print(ufds.rank)

    ufds.union(2, 1)
    ufds.union(3, 4)

    print(ufds.findSet(2))
    print(ufds.isSameSet(1, 3))
    ufds.union(1, 4)

    print(ufds.parent)
    print(ufds.rank)