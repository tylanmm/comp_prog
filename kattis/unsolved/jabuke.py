def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
    if val < 0:
        return 1    # clockwise
    elif val > 0:
        return -1   # counterclockwise
    else:
        return 0    # colinear

def intersects(p, q, r, s):
    o1 = orientation(p, q, r)
    o2 = orientation(p, q, s)
    o3 = orientation(r, s, p)
    o4 = orientation(r, s, q)
    
    if o3 == 0 and (min(r[0], s[0]) <= p[0] <= max(r[0], s[0])) and (min(r[1], s[1]) <= p[1] <= max(r[1], s[1])):
        return -1
    if o1 != o2 and o3 != o4:
        return 1
    return 0

v = [tuple(map(int, input().split())) for _ in range(3)]
v.append(v[0])

area = 0
for i in range(3):
    area += v[i][0]*v[i+1][1] - v[i][1]*v[i+1][0]
print(f'{area / 2:.1f}')

trees = [tuple(map(int, input().split())) for _ in range(int(input()))]
inArea = 0
for t in trees:
    cross = 0
    end = [t[0] + 20983, t[1] + 20981]
    for i in range(3):
        inter = intersects(t, end, v[i], v[i+1])
        if inter == -1:
            inArea += 1
            break
        cross += inter
    else:
        inArea += 1 if cross % 2 else 0

print(inArea)