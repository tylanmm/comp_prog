"""
ID: tylan071
LANG: PYTHON3
TASK: milk2
"""

start = 1000000
end = 0
times = []

with open('milk2.in') as f:
    n = int(f.readline().strip())
    for _ in range(n):
        s, e = tuple(map(int, f.readline().split()))
        times.append((s, e))
        start = min(start, s)
        end = max(end, e)

milking = [False] * end
for t in times:
    for i in range(t[0], t[1]):
        milking[i] = True

longSome = 0
longNone = 0
currType = milking[0]
curr = 0
for m in milking[start:end]:
    if m == currType:
        curr += 1
    else:
        curr = 1
        currType = m

    if currType:
        longSome = max(longSome, curr)
    else:
        longNone = max(longNone, curr)

with open('milk2.out', 'w') as f:
    f.write('%d %d\n' % (longSome, longNone))