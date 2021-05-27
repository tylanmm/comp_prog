with open('badmilk.in') as f:
    N, M, D, S = map(int, f.readline().split())
    drink = [tuple(map(int, f.readline().split())) for _ in range(D)]
    sick  = [tuple(map(int, f.readline().split())) for _ in range(S)]

person = [[] for _ in range(N+1)]
for p, m, t in drink:
    person[p].append((t, m))

poss = set(range(1, M+1))
for p, t in sick:
    poss &= {m for ti, m in person[p] if ti < t}

res = 0
for p in person:
    for t, m in p:
        if m in poss:
            res += 1
            break

with open('badmilk.out', 'w') as f:
    f.write(f'{res}\n')