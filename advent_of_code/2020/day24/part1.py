import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

# make nw (-1, 1), ne (0, 1), w (-1, 0), e (1, 0), sw (0, -1), and se (1, -1)
tiles = {}
for instr in data:
    x, y = 0, 0
    i, n = 0, len(instr)
    while i < n:
        if instr[i] == 'e':
            x += 1
            i += 1
        elif instr[i] == 'w':
            x -= 1
            i += 1
        elif instr[i] == 'n':
            y += 1
            if instr[i+1] == 'w':
                x -= 1
            i += 2
        elif instr[i] == 's':
            y -= 1
            if instr[i+1] == 'e':
                x += 1
            i += 2
        
    if (x, y) in tiles:
        tiles[(x, y)] ^= 1
    else:
        tiles[(x, y)] = 1

print(list(tiles.values()).count(1))