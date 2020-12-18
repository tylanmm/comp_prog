import sys
from collections import deque

with open(sys.argv[1]) as f:
    eqs = f.read().split('\n')

def evaluate(eq):
    res = []
    op = ''
    while eq:
        c = eq.popleft()
        if c == ' ':
            continue
        
        if c == '+' or c == '*':
            op = c
        elif c == ')':
            break
        else:
            if c == '(':
                num = evaluate(eq)
            else:
                num = int(c)

            if op == '+':
                res[-1] += num
            else:
                res.append(num)
    
    while len(res) > 1:
        top = res.pop()
        res[-1] *= top
    return res[0]

total = 0
for eq in eqs:
    eq = deque(list(eq))
    total += evaluate(eq)
print(total)