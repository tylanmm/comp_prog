"""
ID: tylan071
LANG: PYTHON3
TASK: combo
"""

def getWorkingNums(combo, n):
    for i in range(3):
        works = set()
        for j in range(combo[i] - 2, combo[i] + 3):
            while j < 1:
                j += n
            while j > n:
                j -= n
            works.add(j)
        combo[i] = works

with open('combo.in') as f:
    n = int(f.readline())
    fj = list(map(int, f.readline().split()))
    mc = list(map(int, f.readline().split()))

getWorkingNums(fj, n)
getWorkingNums(mc, n)
total = 2 * len(fj[0]) ** 3
same = 1
for i in range(3):
    same *= len(fj[i] & mc[i])
total -= same

with open('combo.out', 'w') as f:
    f.write(f'{total}\n')