import sys

with open(sys.argv[1]) as f:
    data = [line.split(' = ') for line in f.read().split('\n')]

def get_val(orig, mask):
    num = list(bin(orig)[2:])[::-1]
    num += ['0'] * (36 - len(num))
    for i in range(36):
        if mask[i] != 'X':
            num[i] = mask[i]
    return int(''.join(num[::-1]), 2)

mask = 'X'*36
mem = {}
for comm, val in data:
    if comm[:2] == 'ma':
        mask = val[::-1]
    else:
        loc = int(comm.split('[')[1][:-1])
        mem[loc] = get_val(int(val), mask)

print(sum(mem.values()))