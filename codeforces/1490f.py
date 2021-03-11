from sys import stdin, stdout
from collections import Counter

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

for _ in range(int(_i())):
    n = int(_i())
    freq = Counter(map(int, _i().split()))
    order = freq.most_common()
    pref = [0] * (order[0][1] + 1)
    for v, f in order:
        pref[f] += 1
    
    higher = 0
    amt = 0
    lo = n
    for c in range(len(pref)-1, 0):
        left = n - higher - pref[c]*pref[c]
        lo = min(lo, left, higher)
        
        amt += 
    _p(lo)


stdout.flush()