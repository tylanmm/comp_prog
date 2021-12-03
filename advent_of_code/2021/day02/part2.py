import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

h, v, aim = 0, 0, 0
for line in data:
    dir, x = line.split()
    x = int(x)
    if dir == 'forward':
        h += x
        v += aim * x
    else:
        aim += x if dir == 'down' else -x
print(h*v)