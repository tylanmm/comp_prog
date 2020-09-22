def solve(cakes):
    n = list(map(int, cakes[::-1].replace('-', '0').replace('+', '1')))
    i = 0
    count = 0
    while i < len(cakes):
        if n[i] == 0:
            for j in range(i, len(n)):
                n[j] = int(not n[j])
            count += 1
        i += 1
    return count

with open('pancakes.in') as f:
    t = int(f.readline().strip())
    out = open('pancakes.out', 'w')
    for i in range(t):
        out.write('Case #%d: %d\n' % (i+1, solve(f.readline().strip())))
    out.close()