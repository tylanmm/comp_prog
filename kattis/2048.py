from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

grid = [list(map(int, _i().split())) for _ in range(4)]
move = int(_i())

# rotate an n*n matrix 90 deg counterclockwise
def rotate90(grid):
    n = len(grid)
    for i in range(n//2):
        for j in range(i, n-i-1):
            grid[i][j], grid[j][-i-1], grid[-i-1][-j-1], grid[-j-1][i] = \
            grid[j][-i-1], grid[-i-1][-j-1], grid[-j-1][i], grid[i][j]

def slide_left(grid):
    for row in grid:
        # move all the 0's to the right
        j = 0
        for i in range(1, len(row)):
            if j < len(row) and row[i]:
                row[j], row[i] = row[i], row[j]
                while j < len(row) and row[j]: j += 1
        
        # NOW actually try to combine the numbers
        for i in range(len(row)-1):
            j = i+1
            if row[i] == row[i+1]:
                row[i] *= 2
                row.pop(i+1)
                row.append(0)

for i in range(move): rotate90(grid)
slide_left(grid)
for i in range((4 - move) % 4): rotate90(grid)

for r in grid: print(*r)

stdout.flush()