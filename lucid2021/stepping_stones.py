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

m, n = map(int, input().split())
days = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m*n)]
days.reverse()
grid = [[0]*n for _ in range(m)]

ufds = UFDS(m*n+2)
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
last_day = m*n-1
for i, j in days:
    grid[i][j] = 1
    for di, dj in dirs:
        if j+dj < 0:
            ufds.union(0, i*n + j + 1)
        elif j+dj == n:
            ufds.union(m*n+1, i*n + j + 1)
        elif 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj]:
            ufds.union((i+di)*n + j+dj + 1, i*n + j + 1)
    
    if ufds.isSameSet(0, m*n+1):
        print(last_day)
        quit()
    last_day -= 1