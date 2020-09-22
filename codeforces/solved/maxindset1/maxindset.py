import heapq

def run(file):
    with open(f'{file}.in') as f:
        n, m = map(int, f.readline().split())
        used, g = [0] * (n+1), {i:set() for i in range(1, n+1)}
        for _ in range(m):
            v1, v2 = map(int, f.readline().split())
            g[v1].add(v2)
            g[v2].add(v1)

    q = []
    for v in g:
        heapq.heappush(q, (len(g[v]), v))

    count = 0
    while q:
        c, v = heapq.heappop(q)
        for v2 in g[v]:
            if used[v2]:
                break
        else:
            count += 1
            used[v] = 1

    with open(f'{file}.out', 'w') as f:
        f.write(f'{count}\n')
        f.write(' '.join(map(str, used[1:])))

for f in ['b1', 'b2', 'b3', 'b4']:
    run(f)