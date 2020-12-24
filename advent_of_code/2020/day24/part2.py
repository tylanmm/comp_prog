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

dirs = [(-1, 1), (0, 1), (-1, 0), (1, 0), (0, -1), (1, -1)]

def step(tiles):
    # set up new dict with all the tiles that need checking
    new_tiles = {}
    for x, y in tiles:
        new_tiles[(x, y)] = tiles[(x, y)]
        for dx, dy in dirs:
            if (x+dx, y+dy) not in new_tiles:
                new_tiles[(x+dx, y+dy)] = 0
        
    for x, y in new_tiles:
        # get count for each individual tile
        count = 0
        for dx, dy in dirs:
            if (x+dx, y+dy) in tiles and tiles[(x+dx, y+dy)] == 1:
                count += 1
        
        # decide whether this tile gets flipped
        if new_tiles[(x, y)] == 0 and count == 2:
            new_tiles[(x, y)] = 1
        if new_tiles[(x, y)] == 1 and (count == 0 or count > 2):
            new_tiles[(x, y)] = 0
    
    return new_tiles
    
for _ in range(100):
    tiles = step(tiles)
print(list(tiles.values()).count(1))