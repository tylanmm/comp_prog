from sys import stdin

data = stdin.readlines()
i, n = 0, len(data)

while i < n:
    a, b = map(float, data[i].split())
    n = int(data[i+1])
    intervals = []
    for j in range(n):
        ai, bi = map(float, data[i+2+j].split())
        intervals.append((ai, bi))
    
    intervals.sort(key=lambda x: -x[1])
    intervals.sort(key=lambda x: x[0])
    
    print(intervals)

    i += 2 + n