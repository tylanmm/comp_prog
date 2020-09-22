"""
ID: tylan071
LANG: PYTHON3
TASK: namenum
"""

def convert(name):
    out = ''
    for c in name:
        n = ord(c)
        if n < ord('Q'):
            out += str((n - ord('A'))//3 + 2)
        else:
            out += str((n - ord('A') - 1)//3 + 2)
    return out

nums = {}
with open('dict.txt') as f:
    names = f.read().split()
    for n in names:
        num = convert(n)
        if num not in nums:
            nums[num] = [n]
        else:
            nums[num].append(n)

with open('namenum.in') as f:
    num = f.read().strip()

with open('namenum.out', 'w') as f:
    if num not in nums:
        f.write('NONE\n')
    else:
        for name in nums[num]:
            f.write(name + '\n')