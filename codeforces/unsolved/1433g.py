import heapq

n, m, k = map(int, input().split())
g = [set() for _ in range(n)]
weights = [[0]*n for _ in range(n)]
for _ in range(m):
    x, y, w = map(int, input().split())
    g[x-1].add((y-1, w))
    g[y-1].add((x-1, w))
    weights[x-1][y-1] = w
    weights[y-1][x-1] = w

def run(a, b):
    q = [(0, a, [a])]
    seen = [False]*n
    while q:
        cost, district, path = heapq.heappop(q)
        if seen[district]:
            continue
        seen[district] = True
        if district == b:
            return path, cost
        for d, w in g[district]:
            if not seen[d]:
                heapq.heappush(q, (cost+w, d, path+[d]))

times = {}
cost = 0
for _ in range(k):
    a, b = map(int, input().split())
    path, c = run(a-1, b-1)
    cost += c
    for i in range(len(path)-1):
        s, e = path[i], path[i+1]
        if (s, e) not in times:
            times[(s, e)] = 0
        times[(s, e)] += weights[s][e]

print(cost - max(times.values()))