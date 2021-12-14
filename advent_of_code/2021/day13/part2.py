import sys

curr = set()
line = input()
while line:
    x, y = map(int, line.split(','))
    curr.add((x, y))
    line = input()

for inst in sys.stdin.read().split('\n'):
    *_, line = inst.split(' ')
    ori, coord = line.split('=')
    coord = int(coord)

    prev, curr = curr, set()
    for x, y in prev:
        if ori == 'x':
            if x > coord:
                x -= 2 * (x - coord)
        elif ori == 'y':
            if y > coord:
                y -= 2 * (y - coord)
        curr.add((x, y))

X = max([dot[0] for dot in curr])
Y = max([dot[1] for dot in curr])
out = [['.']*(X+1) for _ in range(Y+1)]
for x, y in curr:
    out[y][x] = '#'

for row in out:
    print(*row)