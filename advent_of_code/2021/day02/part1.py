import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

h, v = 0, 0
for line in data:
    dir, x = line.split()
    x = int(x)
    if dir == 'forward':
        h += x
    else:
        v += x if dir == 'down' else -x
print(h*v)