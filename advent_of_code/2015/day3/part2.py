import sys

with open(sys.argv[1]) as f:
    dirs = f.read()

x1, y1 = 0, 0
x2, y2 = 0, 0
seen = {(0, 0)}
for i, d in enumerate(dirs):
    if i % 2 == 0:
        if d == '^':
            y1 += 1
        elif d == 'v':
            y1 -= 1
        elif d == '>':
            x1 += 1
        else:
            x1 -= 1
        seen.add((x1, y1))
    else:
        if d == '^':
            y2 += 1
        elif d == 'v':
            y2 -= 1
        elif d == '>':
            x2 += 1
        else:
            x2 -= 1
        seen.add((x2, y2))
print(len(seen))