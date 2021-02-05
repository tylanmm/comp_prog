import sys

with open(sys.argv[1]) as f:
    dirs = f.read()

x, y = 0, 0
seen = {(0, 0)}
for d in dirs:
    if d == '^':
        y += 1
    elif d == 'v':
        y -= 1
    elif d == '>':
        x += 1
    else:
        x -= 1
    seen.add((x, y))
print(len(seen))