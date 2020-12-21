import sys

with open(sys.argv[1]) as f:
    foods = f.read().split('\n')

allergens = {}
for i in range(len(foods)):
    ing, ale = foods[i].split(' (contains ')
    ing = set(ing.split())
    ale = ale[:-1].split(', ')
    for a in ale:
        if a not in allergens:
            allergens[a] = ing
        else:
            allergens[a] = allergens[a].intersection(ing)

print(allergens)
canon = []
while len(canon) != len(allergens):
    for ale in allergens:
        if len(allergens[ale]) == 1:
            ing = allergens[ale].pop()
            canon.append((ale, ing))
            for a in allergens:
                if ing in allergens[a]:
                    allergens[a].remove(ing)

canon.sort()
print(','.join([w for a, w in canon]))