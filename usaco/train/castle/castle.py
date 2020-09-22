"""
ID: tylan071
LANG: PYTHON3
TASK: castle
"""

with open('castle.in') as f:
    M, N = map(int, f.readline().split())
    castle = [list(map(int, f.readline().split())) for _ in range(N)]

def floodfill(r, c):
    if r < 0 or r >= N or c < 0 or c >= M or (castle[r][c] >= 16):
        return 0
    
    res = 1
    castle[r][c] += 16

    # west
    if not (castle[r][c] & 1):
        res += floodfill(r, c-1)
    
    # north
    if not (castle[r][c] & 2):
        res += floodfill(r-1, c)
    
    # east
    if not (castle[r][c] & 4):
        res += floodfill(r, c+1)
    
    # south
    if not (castle[r][c] & 8):
        res += floodfill(r+1, c)
    
    return res

def reset():
    for r in range(N):
        for c in range(M):
            if castle[r][c] >= 16:
                castle[r][c] -= 16

numRooms, maxRoom = 0, 0
for r in range(N):
    for c in range(M):
        if castle[r][c] < 16:
            numRooms += 1
            maxRoom = max(maxRoom, floodfill(r, c))
reset()

maxModRoom, R, C, dir = 0, 0, 0, 'N'
for c in range(M):
    for r in range(N-1, -1, -1):
        if r and (castle[r][c] & 2):
            castle[r][c] -= 2
            roomSize = floodfill(r, c)
            castle[r][c] += 2
            reset(r, c)
            if roomSize > maxModRoom:
                maxModRoom = roomSize
                R = r
                C = c
                dir = 'N'
        
        if c < M-1 and (castle[r][c] & 4):
            castle[r][c] -= 4
            roomSize = floodfill(r, c)
            castle[r][c] += 4
            reset(r, c)
            if roomSize > maxModRoom:
                maxModRoom = roomSize
                R = r
                C = c
                dir = 'E'

with open('castle.out', 'w') as f:
    f.write(f'{numRooms}\n{maxRoom}\n{maxModRoom}\n{R+1} {C+1} {dir}\n')