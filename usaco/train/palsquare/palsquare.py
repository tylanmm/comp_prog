"""
ID: tylan071
LANG: PYTHON3
TASK: palsquare
"""

digits = '0123456789ABCDEFGHIJ'
def toBase(num, base):
    res = ''
    while num >= base:
        res = digits[num % base] + res
        num //= base
    return digits[num] + res

with open('palsquare.in') as f:
    b = int(f.read())
    
with open('palsquare.out', 'w+') as f:    
    for i in range(1, 301):
        inB = toBase(i*i, b)
        if inB == inB[::-1]:
            f.write(f'{toBase(i, b)} {inB}\n')