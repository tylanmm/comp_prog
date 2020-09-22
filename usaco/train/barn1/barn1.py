"""
ID: tylan071
LANG: PYTHON3
TASK: barn1
"""

with open('barn1.in') as f:
    m, s, c = map(int, f.readline().split())
    cows = sorted([int(f.readline()) for _ in range(c)])

dist = cows[-1] - cows[0] + 1
gaps = []
for i in range(1, c):
    gaps.append(cows[i] - cows[i-1] - 1)
gaps.sort()

for _ in range(min(c-1, m-1)):
    dist -= gaps.pop()

with open('barn1.out', 'w') as f:
    f.write(f'{dist}\n')