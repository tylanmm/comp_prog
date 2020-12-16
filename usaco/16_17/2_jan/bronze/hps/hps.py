with open(__file__[:-2] + 'in', 'r') as f:
    n = int(f.readline())
    games = [tuple(map(int, f.readline().split())) for _ in range(n)]

rules = [[0, 2, 3, 1], [0, 3, 1, 2]]
hi = 0
for rule in rules:
    total = 0
    for x, y in games:
        total += rule.index(x) == y
    hi = max(hi, total)

with open(__file__[:-2] + 'out', 'w') as f:
    f.write(str(hi) + '\n')