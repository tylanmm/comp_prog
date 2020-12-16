with open('cowsignal.in') as f:
    m, n, k = map(int, f.readline().split())
    design = [f.readline().strip() for _ in range(m)]

res = []
for line in design:
    new_line = []
    for c in line:
        new_line.append(c*k)
    res.extend([''.join(new_line)]*k)

with open('cowsignal.out', 'w') as f:
    f.write('\n'.join(res) + '\n')