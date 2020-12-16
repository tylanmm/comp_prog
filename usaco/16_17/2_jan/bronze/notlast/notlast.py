with open(__file__[:-2] + 'in', 'r') as f:
    n = int(f.readline())
    log = [f.readline().split() for _ in range(n)]

names = 'Bessie, Elsie, Daisy, Gertie, Annabelle, Maggie, Henrietta'.split(', ')
totals = {name: 0 for name in names}
for name, amt in log:
    amt = int(amt)
    totals[name] += amt

winner = 'Tie'
ordered = sorted(totals, key=lambda x: totals[x])
for i in range(1, len(ordered)):
    if totals[ordered[i]] > totals[ordered[i-1]]:
        winner = ordered[i]
        break

if winner != 'Tie' and list(totals.values()).count(totals[winner]) > 1:
    winner = 'Tie'

with open(__file__[:-2] + 'out', 'w') as f:
    f.write(winner + '\n')