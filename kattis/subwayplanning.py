from math import atan, pi, sin

def getTheta(point):
    theta = atan(point[1] / point[0]) if point[0] else pi/2 if point[1] > 0 else 3*pi/2
    theta += pi if point[0] < 0 else 0
    theta += 2*pi if point[0] > 0 and point[1] < 0 else 0
    return theta

def dist(point):
    return (point[0]**2 + point[1]**2)**0.5

def distToLine(point, angle):
    return dist(point) * sin(abs(angle - point[2]))

for dataset in range(int(input())):
    n, d = map(int, input().split())
    loc = []
    for _ in range(n):
        x, y = map(int, input().split())
        loc.append((x, y, getTheta((x, y))))
    loc.sort(key=lambda p: p[2])
    print(loc)
    print([distToLine(p, 0) for p in loc])