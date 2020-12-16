with open('square.in') as f:
    x1, y1, x2, y2 = map(int, f.readline().split())
    x3, y3, x4, y4 = map(int, f.readline().split())

xs = [x1, x2, x3, x4]
ys = [y1, y2, y3, y4]
xdist = max(xs) - min(xs)
ydist = max(ys) - min(ys)

with open('square.out', 'w') as f:
    f.write(str(max(xdist, ydist)**2) + '\n')