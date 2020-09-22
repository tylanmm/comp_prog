"""
ID: tylan071
LANG: PYTHON3
TASK: skidesign
"""

with open('skidesign.in') as f:
    n = int(f.readline())
    hills = []
    for _ in range(n):
        hills.append(int(f.readline()))
    hills.sort()

lo = 1000000
for i in range(hills[0], hills[-1] - 16):
    cost = 0
    for h in hills:
        if h < i:
            cost += (i - h) ** 2
        elif h > i + 17:
            cost += (h - i - 17) ** 2
    lo = min(lo, cost)

with open('skidesign.out', 'w') as f:
    f.write(f'{lo}\n')