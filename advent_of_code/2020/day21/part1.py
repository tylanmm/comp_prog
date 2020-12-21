import sys
from collections import Counter

with open(sys.argv[1]) as f:
    foods = f.read().split('\n')

allergens = {}
allings = Counter()
for i in range(len(foods)):
    ing, ale = foods[i].split(' (contains ')
    ing = set(ing.split())
    ale = ale[:-1].split(', ')
    for a in ale:
        if a not in allergens:
            allergens[a] = ing
        else:
            allergens[a] &= ing
    allings.update(ing)

for a in allergens:
    for w in allergens[a]:
        allings.pop(w) if w in allings else None
print(sum(allings.values()))