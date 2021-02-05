import math

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_angle(p1, v, p2):
    return math.acos((dist(p1, v) + dist(p2, v) - dist(p1, p2)) / (2 * (dist(p1, v)**0.5) * (dist(p2, v)**0.5)))

cities = [tuple(map(int, input().split())) for _ in range(3)]
angles = [get_angle(cities[(i-1)%3], cities[i], cities[(i+1)%3]) for i in range(3)]
for i in range(3):
    if angles[i] >= 2*math.pi/3:
        print('%f %f' % (cities[i][0], cities[i][1]))
        break
else:
    tris = []
    for i in range(3):
        tris.append(1/math.sin(angles[i] + math.pi/3))
    denom = sum(tris)
    x = sum([tris[i] * cities[i][0] for i in range(3)])
    y = sum([tris[i] * cities[i][1] for i in range(3)])
    print(x, y)