import sys

with open(sys.argv[1]) as f:
    pos = []
    vel = [[0]*3 for _ in range(4)]
    for _ in range(4):
        line = f.readline().split('=')
        x = int(line[1].split(',')[0])
        y = int(line[2].split(',')[0])
        z = int(line[3].split('>')[0])
        pos.append([x, y, z])

pairs = [(i, j) for i in range(4) for j in range(4) if i < j]

for t in range(277200):
    # apply gravity (change velocity)
    for i, j in pairs:
        for k in range(3):
            if pos[i][k] < pos[j][k]:
                vel[i][k] += 1
                vel[j][k] -= 1
            elif pos[i][k] > pos[j][k]:
                vel[i][k] -= 1
                vel[j][k] += 1

    # apply velocity
    for i in range(4):
        for j in range(3):
            pos[i][j] += vel[i][j]
    
    if vel[0] == [0, 0, 0]:
        print(t, *pos)
        print(*vel)
        print()