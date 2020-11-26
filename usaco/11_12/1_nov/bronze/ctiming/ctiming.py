with open('ctiming.in') as f:
    d, h, m = map(int, f.readline().split())

total = 0
total += (d - 11) * 60 * 24
total += (h - 11) * 60
total += (m - 11)

with open('ctiming.out', 'w') as f:
    f.write(str(-1 if total < 0 else total) + '\n')