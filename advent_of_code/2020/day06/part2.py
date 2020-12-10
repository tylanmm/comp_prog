import sys
from collections import Counter

with open(sys.argv[1]) as f:
    groups = f.read().split('\n\n')

count = 0
for g in groups:
    g = g.split('\n')
    seen = Counter()
    for p in g:
        seen.update(Counter(p))
    count += list(seen.values()).count(len(g))
print(count)