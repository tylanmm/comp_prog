with open(__file__[:-2] + 'in', 'r') as f:
    n = int(f.readline())
    cows = sorted([tuple(map(int, f.readline().split())) for _ in range(n)])

# find minimum distance between a sick and non-sick cow
r = float('inf')
for i in range(n):
    if cows[i][1] == 0:
        if i > 0 and cows[i-1][1]:
            r = min(r, cows[i][0] - cows[i-1][0])
        if i + 1 < n and cows[i+1][1]:
            r = min(r, cows[i+1][0] - cows[i][0])
r -= 1

# find the number of groups that could have infected each other
prev, groups = -float('inf'), 0
for loc, is_sick in cows:
    if is_sick:
        if loc - prev > r:
            groups += 1
        prev = loc

with open(__file__[:-2] + 'out', 'w') as f:
    f.write(str(groups) + '\n')