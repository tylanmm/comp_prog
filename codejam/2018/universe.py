def solve(d, p):
    if p.count('S') > d:
        return "IMPOSSIBLE"
    
    if p.count('C') == 0 or p.count('S') == 0:
        return str(0)

    damage = [0] * (p.count('C') + 1)
    numC = 0
    for instruction in p:
        if instruction == 'C':
            numC += 1
        else:
            damage[numC] += 1
    
    totalDamage = sum([2**i * damage[i] for i in range(len(damage))])
    swaps = 0
    while totalDamage > d:
        if damage[numC] == 0:
            damage.pop()
            numC -= 1
        else:
            damage[numC - 1] += 1
            damage[numC] -= 1
            swaps += 1
            totalDamage -= 2**(numC - 1)

    return str(swaps)

t = int(input())
for i in range(t):
    d, p = input().split()
    d = int(d)
    print("Case #%d: %s" % (i+1, solve(d, p)))