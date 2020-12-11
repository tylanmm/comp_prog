import sys

with open(sys.argv[1]) as f:
    data = [list(row) for row in f.read().split('\n')]

def state(grid):
    r, c = len(grid), len(grid[0])
    newGrid = [[grid[i][j] for j in range(c)] for i in range(r)]
    changeHappen = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                continue

            adj = 0
            adj += i and j and grid[i-1][j-1] == '#'
            adj += i and grid[i-1][j] == '#'
            adj += i and j + 1 < c and grid[i-1][j+1] == '#'
            adj += j and grid[i][j-1] == '#'
            adj += j + 1 < c and grid[i][j+1] == '#'
            adj += i + 1 < r and j and grid[i+1][j-1] == '#'
            adj += i + 1 < r and grid[i+1][j] == '#'
            adj += i + 1 < r and j + 1 < c and grid[i+1][j+1] == '#'
            
            if grid[i][j] == 'L' and adj == 0:
                changeHappen = True
                newGrid[i][j] = '#'
            elif grid[i][j] == '#' and adj >= 4:
                changeHappen = True
                newGrid[i][j] = 'L'
    return newGrid, changeHappen

changeHappen = True
while changeHappen:
    data, changeHappen = state(data)

total = 0
for row in data:
    total += row.count('#')
print(total)