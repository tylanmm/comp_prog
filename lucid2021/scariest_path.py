n = int(input())
scariness = list(map(int, input().split()))
adj = [list(map(int, input().split())) for _ in range(n)]
order = sorted(enumerate(scariness), key=lambda x: x[1], reverse=True)
seen = [False]*n

res = 0
for house, scares in order:
    seen[house] = True
    res += scares
    for i in range(n):
        if adj[house][i] and seen[i]:
            res += scariness[i]
print(res)