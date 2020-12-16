import sys

with open(sys.argv[1]) as f:
    data = [line.split(' = ') for line in f.read().split('\n')]

def update(pos, val, mask, i=0):
    if i == 36:
        loc = int(''.join(pos[::-1]), 2)
        mem[loc] = val
        return

    if mask[i] == '0':
        update(pos, val, mask, i+1)
    elif mask[i] == '1':
        pos[i] = '1'
        update(pos, val, mask, i+1)
    else:
        pos[i] = '0'
        update(pos, val, mask, i+1)
        pos[i] = '1'
        update(pos, val, mask, i+1)

mask = 'X'*36
mem = {}
for comm, val in data:
    if comm[:2] == 'ma':
        mask = val[::-1]
    else:
        loc = list(bin(int(comm.split('[')[1][:-1]))[2:])[::-1]
        loc += ['0'] * (36 - len(loc))
        update(loc, int(val), mask)

print(sum(mem.values()))