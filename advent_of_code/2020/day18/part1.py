import sys
from collections import deque

with open(sys.argv[1]) as f:
    eqs = f.read().split('\n')

def evaluate(eq):
    res = 0
    op = ''
    while eq:
        c = eq.popleft()
        if c == ' ':
            continue
        if c == '+' or c == '*':
            op = c
        elif c == ')':
            return res
        else:
            if c == '(':
                num = evaluate(eq)
            else:
                num = int(c)

            if op:
                res = (res * num) if op == '*' else (res + num)
            else:
                res = num
    return res

total = 0
for eq in eqs:
    eq = deque(list(eq))
    total += evaluate(eq)
print(total)