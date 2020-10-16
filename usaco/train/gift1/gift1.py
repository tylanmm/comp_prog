"""
ID: tylan071
LANG: PYTHON3
TASK: gift1
"""

with open('gift1.in') as f:
    n = int(f.readline().strip())
    balances = {f.readline().strip(): 0 for _ in range(n)}

    for i in range(n):
        name = f.readline().strip()
        bal, give = map(int, f.readline().split())
        if give == 0:
            continue

        for j in range(give):
            balances[f.readline().strip()] += bal // give
        balances[name] = (bal % give) - bal

with open('gift1.out', 'w') as f:
    for name in balances:
        f.write('%s %d\n' % (name, balances[name]))