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
    if o4 == 0 and (min(r[0], s[0]) <= q[0] <= max(r[0], s[0])) and (min(r[1], s[1]) <= q[1] <= max(r[1], s[1])):
        return -1
    if o1 != o2 and o3 != o4:
        return 1
    return 0

def contains(p, v):
    cross = 0
    end = [101, 103]
    for i in range(n):
        inter = intersects(p, end, v[i], v[i+1])
        if inter == -1:
            return True
        cross += inter
    else:
        return True if cross % 2 else False

def getCellStates(points, loX, hiX, loY, hiY):
    notCrossed = [[True for _ in range(hiX - loX + 1)] for _ in range(hiY - loY + 1)]
    # check horizontal segments
    for i in range(len(notCrossed)):
        for j in range(len(notCrossed[i])):
            for k in range(len(points)-1):
                print((j+loX, hiY-i), (j+loX+1, hiY-i))
                inter = intersects((j+loX, hiY-i), (j+loX+1, hiY-i), points[k], points[k+1])
                if inter == 1:
                    notCrossed[i][j] == False
    
    print()
    # check vertical segments
    for i in range(len(notCrossed)):
        for j in range(len(notCrossed[i])):
            if notCrossed[i][j]:
                for k in range(len(points)-1):
                    inter = intersects((j+loX, hiY-i), (j+loX, hiY-i-1), points[k], points[k+1])
                    if inter == 1:
                        notCrossed[i][j] == False
    return notCrossed

n = int(input())
while n:
    points = [tuple(map(int, input().split())) for _ in range(n)]
    points.append(points[0])
    loX, hiX = min(points, key=lambda p:p[0])[0], max(points, key=lambda p:p[0])[0]
    loY, hiY = min(points, key=lambda p:p[1])[1], max(points, key=lambda p:p[1])[1]
    cells = getCellStates(points, loX, hiX, loY, hiY)
    print(cells)
    total = 0
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if cells[i][j]:
                if contains((i-loX, j-loY), points):
                    print(i, j)
                    total += 1
    print(total)

    n = int(input())