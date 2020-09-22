F, B = tuple(map(int, input().split()))
front = list(map(int, input().split()))
front.reverse()
back = list(map(int, input().split()))
back.reverse()

pairs = []
for f in front:
    for b in back:
        pairs.append((f/b, f, b))

pairs.sort()
for p in pairs:
    print('(%d,%d)' % (p[1], p[2]))