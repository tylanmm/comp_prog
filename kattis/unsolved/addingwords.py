from sys import stdin, stdout

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

mem = {}
opp = {}

def evaluate(calc):
    val = 0
    op = ''
    for i, var in enumerate(calc):
        if var not in '+-=':
            if var not in opp:
                return 'unknown'
            elif op == '+':
                val += opp[var]
            elif op == '-':
                val -= opp[var]
            else: # op == ''
                val = opp[var]
        elif var != '=':
            op = var
    
    return mem[val] if val in mem else 'unknown'

for line in stdin:
    line = line.split()
    if line[0] == 'def':
        var, val = line[1], int(line[2])
        if var in opp:
            mem[opp[var]] = ''
        mem[val] = var
        opp[var] = val
    elif line[0] == 'calc':
        print(' '.join(line[1:]) + f' {evaluate(line[1:])}')
    else: # line[0] == 'clear'
        mem = {}
        opp = {}

stdout.flush()