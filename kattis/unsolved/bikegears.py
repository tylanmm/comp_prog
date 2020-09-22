F, B = tuple(map(int, input().split()))
front = list(map(int, input().split()))
back = list(map(int, input().split()))

pairs = []
for f in front:
    for b in back:
        pairs.append((f/b, f, b))

pairs.sort(key=lambda x:x[1])
pairs.sort(key=lambda x:x[0])
for r, f, b in pairs:
    print(f'({f},{b})')