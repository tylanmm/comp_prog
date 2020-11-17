import sys

with open(sys.argv[1]) as f:
    wire1 = f.readline().split(',')
    wire2 = f.readline().split(',')

def getPath(wire):
    spots = set()
    time = {}
    t = 0
    x, y = 0, 0

    for step in wire:
        dx, dy = 0, 0
        if   step[0] == 'R':
            dx = 1
        elif step[0] == 'L':
            dx = -1
        elif step[0] == 'U':
            dy = 1
        elif step[0] == 'D':
            dy = -1
        
        for _ in range(int(step[1:])):
            x += dx
            y += dy
            t += 1
            spots.add((x, y))
            if (x, y) not in time:
                time[(x, y)] = t
    
    return spots, time

path1, time1 = getPath(wire1)
path2, time2 = getPath(wire2)
closest = min(path1.intersection(path2), key=lambda z: time1[z] + time2[z])
print(time1[closest] + time2[closest])