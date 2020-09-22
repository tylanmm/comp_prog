"""
ID: tylan071
LANG: PYTHON3
TASK: dualpal
"""

def convert(n, base):
    out = ''
    while n >= base:
        out = str(n % base) + out
        n //= base
    return str(n) + out


with open('dualpal.in') as f:
    n, s = tuple(map(int, f.read().split()))

f = open('dualpal.out', 'w+')
count = 0
curr = s + 1
while count < n:
    palCount = 0
    for i in range(2, 11):
        converted = convert(curr, i)
        if converted == converted[::-1]:
            palCount += 1
        if palCount == 2:
            f.write(f'{curr}\n')
            count += 1
            break
    curr += 1

f.close()