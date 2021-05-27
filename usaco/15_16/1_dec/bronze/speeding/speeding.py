with open('speeding.in') as f:
    n, m = map(int, f.readline().split())
    road = [tuple(map(int, f.readline().split())) for _ in range(n)]
    bess = [tuple(map(int, f.readline().split())) for _ in range(m)]

limit = []
for length, lim in road:
    for _ in range(length):
        limit.append(lim)

speed = []
for length, lim in bess:
    for _ in range(length):
        speed.append(lim)

hi = 0
for i in range(100):
    hi = max(hi, max(0, speed[i] - limit[i]))

with open('speeding.out', 'w') as f:
    f.write(f'{hi}\n')