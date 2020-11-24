with open('photo.in') as f:
    n = int(f.readline())
    bis = list(map(int, f.readline().split()))

for i in range(1,bis[0]):
    found = True
    ai = i
    aip1 = bis[0] - i
    if aip1 < 1:
        continue
    ais = [ai, aip1]
    used = set([ai, aip1])
    for bi in bis[1:]:
        ai = aip1
        aip1 = bi - ai
        if aip1 < 1:
            found = False
            break
        ais.append(aip1)
        if aip1 not in used:
            used.add(aip1)
        else: 
            found = False
            break
    if found:
        break

with open('photo.out', 'w+') as f:
    f.write(' '.join(map(str, ais)) + '\n')