import sys

with open(sys.argv[1]) as f:
    state = [[[list(line) for line in f.read().split('\n')]]]

ACTIVE = '#'
INACTIVE = '.'

def count_neighbors(x, y, z, w, space):
    # (x, y, z) is a coordinate in the new_state
    # we have to be careful when looking at its neighbors
    # since many of them (especially when on the edge)
    # will be outside of the current space

    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue
                    if x + i < 0 or x + i >= len(space[0][0][0]):
                        continue
                    if y + j < 0 or y + j >= len(space[0][0]):
                        continue
                    if z + k < 0 or z + k >= len(space[0]):
                        continue
                    if w + l < 0 or w + l >= len(space):
                        continue
                    total += space[w+l][z+k][y+j][x+i] == ACTIVE
    return total

def next_state(space):
    oldw = len(space)
    oldz = len(space[0])
    oldy = len(space[0][0])
    oldx = len(space[0][0][0])
    # deep copy of space
    # however, needs to have extra room (can grow at most 1 in each direction)
    new_state = [[[['']*(oldx+2) for k in range(oldy+2)] for j in range(oldz+2)] for i in range(oldw+2)]

    # for each hypercube
    for w in range(oldw+2):
        for z in range(oldz+2):
            for y in range(oldy+2):
                for x in range(oldx+2):
                    num_neighbors = count_neighbors(x-1, y-1, z-1, w-1, space)
                    
                    # if it's within space and is active
                    if 0 <= x - 1 < oldx and 0 <= y - 1 < oldy and 0 <= z - 1 < oldz and 0 <= w - 1 < oldw and space[w-1][z-1][y-1][x-1] == ACTIVE:
                        if 2 <= num_neighbors <= 3:
                            new_state[w][z][y][x] = ACTIVE
                        else:
                            new_state[w][z][y][x] = INACTIVE
                    
                    # otherwise it's inactive
                    else:
                        if num_neighbors == 3:
                            new_state[w][z][y][x] = ACTIVE
                        else:
                            new_state[w][z][y][x] = INACTIVE
    
    return new_state

num_cycles = 6
for _ in range(num_cycles):
    state = next_state(state)

total = 0
for dim in state:
    for layer in dim:
        for y in layer:
            total += y.count(ACTIVE)
print(total)