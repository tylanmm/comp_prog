"""
ID: tylan071
LANG: PYTHON3
TASK: beads
"""

with open('beads.in') as f:
    n = int(f.readline().strip())
    beads = f.readline().strip()

def count(start):
    curr = beads[start]
    i = start + 1
    i %= len(beads)
    num = 1
    switched = False

    while num < len(beads):
        if curr == 'w' and beads[i] != 'w':
            curr = beads[i]
        
        if beads[i] == curr or beads[i] == 'w':
            pass
        elif not switched:
            curr = beads[i]
            switched = True
        else:
            break
        
        num += 1
        i += 1
        i %= len(beads)
    
    return num

best = 0
for i in range(len(beads)):
    best = max(best, count(i))

with open('beads.out', 'w') as f:
    f.write(str(best) + '\n')