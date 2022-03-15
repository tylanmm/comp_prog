class UFDS:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def findSet(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.findSet(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        x, y = self.findSet(i), self.findSet(j)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                self.rank[x] += self.rank[x] == self.rank[y]
            return True
        return False


# read input
n, m, p = map(int, input().split())
unsafe = {a: float('inf') for a in map(int, input().split())}
edges = sorted([tuple(map(int, input().split()))
               for _ in range(m)], key=lambda x: x[2])

if n == p:
    print(sum([e[2] for e in edges]) if m == n*(n-1)//2 else 'impossible')
    quit()

ufds = UFDS(n+1)
comps = n - p
cost = 0
unsafe_edges = 0
for a, b, w in edges:
    # properly handle unsafe edges
    if (a in unsafe) or (b in unsafe):
        if (a in unsafe) and (b in unsafe):
            pass
        elif a in unsafe:
            unsafe[a] = min(unsafe[a], w)
        else:
            unsafe[b] = min(unsafe[b], w)
        continue

    if ufds.union(a, b):
        cost += w
        comps -= 1

cost += sum(unsafe.values())

print(cost if cost < float('inf') and comps == 1 else 'impossible')
