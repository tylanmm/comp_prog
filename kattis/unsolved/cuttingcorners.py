from math import acos, pi

def calcAngle(o, a, b):
    ax = a[0] - o[0]
    ay = a[1] - o[1]
    bx = b[0] - o[0]
    by = b[1] - o[1]

    dot = ax * bx + ay * by
    aSize = (ax*ax + ay*ay)**0.5
    bSize = (bx*bx + by*by)**0.5
    return acos(dot / (aSize * bSize))

line = input().split()
while line[0] != '0':
    n = int(line[0])
    shape = [(int(line[i]), int(line[i+1])) for i in range(1, n*2, 2)]
    
    while len(shape) > 3:
        minAngle = 2*pi
        minAngleI = -1
        for i in range(len(shape)):
            a = calcAngle(shape[i], shape[i-1], shape[(i+1) % len(shape)])
            if a < minAngle:
                newA = calcAngle(shape[i-1], shape[i-2], shape[(i+1) % len(shape)])
                newB = calcAngle(shape[(i+1) % len(shape)], shape[i-1], shape[(i+2) % len(shape)])
                if a <= newA and a <= newB:
                    minAngle = a
                    minAngleI = i
        if minAngleI != -1:
            shape.pop(minAngleI)
        else:
            break
    
    res = [str(len(shape))] + [str(p[0]) + ' ' + str(p[1]) for p in shape]
    print(' '.join(res))

    line = input().split()