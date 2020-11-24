from itertools import permutations

with open('lineup.in') as f:
    n = int(f.readline())
    rules = []
    for _ in range(n):
        x, *fill, y = f.readline().split()
        rules.append((x, y))

ans = None
cows = sorted(['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue'])
for perm in permutations(cows):
    for x, y in rules:
        if abs(perm.index(x) - perm.index(y)) != 1:
            break
    else:
        ans = perm
        break

with open('lineup.out', 'w') as f:
    f.write('\n'.join(ans) + '\n')