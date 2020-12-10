import sys

with open(sys.argv[1]) as f:
    instr = [comm.split() for comm in f.read().split('\n')]

def solve(instr):
    acc, i = 0, 0
    seen = [False] * len(instr)
    while i < len(instr) and not seen[i]:
        seen[i] = True
        op, arg = instr[i]
        arg = int(arg)
        if op == 'acc':
            acc += arg
        elif op == 'jmp':
            i += arg - 1
        i += 1
    
    return acc if i == len(instr) else -1

ans = -1
for i in range(len(instr)):
    if instr[i][0] != 'acc':
        instr[i][0] = 'jmp' if instr[i][0] == 'nop' else 'nop'
        ans = solve(instr)
        instr[i][0] = 'jmp' if instr[i][0] == 'nop' else 'nop'
    if ans != -1:
        break
print(ans)