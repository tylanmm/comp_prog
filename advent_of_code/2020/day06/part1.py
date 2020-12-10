import sys

with open(sys.argv[1]) as f:
    groups = f.read().split('\n\n')

count = 0
for g in groups:
    g = g.split('\n')
    seen = set()
    for p in g:
        seen.update(set(p))
    count += len(seen)
print(count)