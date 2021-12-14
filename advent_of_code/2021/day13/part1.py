import sys

curr = set()
line = input()
while line:
    x, y = map(int, line.split(','))
    curr.add((x, y))
    line = input()

instructions = []
for inst in sys.stdin.read().split('\n'):
    *_, line = inst.split(' ')
    ori, coord = line.split('=')
    coord = int(coord)
    instructions.append((ori, coord))

prev, curr = curr, set()
for x, y in prev:
    if instructions[0][0] == 'x':
        if x > instructions[0][1]:
            x -= 2 * (x - instructions[0][1])
    elif instructions[0][0] == 'y':
        if y > instructions[0][1]:
            y -= 2 * (y - instructions[0][1])
    curr.add((x, y))
print(len(curr))