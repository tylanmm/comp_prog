with open('haybales.in') as f:
    n = int(f.readline())
    bales = [int(f.readline()) for _ in range(n)]

average = sum(bales) // n
total = 0
for b in bales:
    if b < average:
        total += average - b

with open('haybales.out', 'w') as f:
    f.write(str(total) + '\n')