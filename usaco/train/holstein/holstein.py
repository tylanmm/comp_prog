"""
ID: tylan071
LANG: PYTHON3
TASK: holstein
"""

with open('holstein.in') as f:
    v = int(f.readline())
    vit = list(map(int, f.readline().split()))
    g = int(f.readline())
    feed = [list(map(int, f.readline().split())) for _ in range(g)]

lo = g + 1
loScoops = 0
for k in range(1, 2**g):
    amts = [0]*v
    numScoops = 0
    scoops = k
    for i in range(g):
        useScoop = scoops % 2
        scoops //= 2
        if not useScoop:
            continue
        
        numScoops += 1
        for j in range(v):
            amts[j] += feed[i][j]
    
    for i in range(v):
        if amts[i] < vit[i]:
            break
    else:
        if numScoops < lo:
            lo = numScoops
            loScoops = k

ans = [str(lo)]
i = 1
while loScoops:
    if loScoops % 2:
        ans.append(str(i))
    i += 1
    loScoops //= 2

with open('holstein.out', 'w') as f:
    f.write(' '.join(ans) + '\n')