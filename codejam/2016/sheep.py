def solve(n):
    num = 0
    prevNums = []
    seen = set()
    while len(seen) < 10:
        num += n
        nextNums = list(str(num))
        if prevNums == nextNums:
            return 'INSOMNIA'
        seen = seen.union(set(nextNums))
        prevNums = nextNums.copy()
    return str(num)

with open('sheep.in') as f:
    t = int(f.readline().strip())
    out = open('sheep.out', 'w')
    for i in range(t):
        out.write('Case #%d: %s\n' % (i+1, solve(int(f.readline().strip()))))