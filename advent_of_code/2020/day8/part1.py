import sys

with open(sys.argv[1]) as f:
    instr = [comm.split(' ') for comm in f.read().split('\n')]

acc, i = 0, 0
seen = [False] * len(instr)
while not seen[i]:
    seen[i] = True
    op, arg = instr[i]
    arg = int(arg)
    if op == 'acc':
        acc += arg
    elif op == 'jmp':
        i += arg - 1
    i += 1

print(acc)