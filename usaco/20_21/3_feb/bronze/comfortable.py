'''
Because of how large the grid can be and how many cows we will
be reading in, we have to keep track of our answer as we go;
we can't do a manual count every single time. This is okay,
since adding a single cow will only ever affect the four cells
around it.

To handle this, for each cell in the 1001 x 1001 grid, store
whether there is a cow there, as well as how many neighbors it
has. Every time a cow is added to the field, increase the
neighbor counter for each of those four cells by 1. If a cell's
counter reaches 3, then increase the total amount of comfortable
cows by 1. If the count reaches 4, then decrease the count by 1.
'''

n = int(input())
grid = [[False]*1001 for i in range(1001)]
neighbors = [[0]*1001 for i in range(1001)]
count = 0

# Handles updating the number of neighbors that a cell has
def updateNeighbor(x, y):
    # If (x, y) is out of the grid, exit
    if x < 0 or x > 1000 or y < 0 or y > 1000:
        return 0
    
    # Increase the neighbor count, see if it became comfortable
    # or if it went from comfortable to uncomfortable
    # Return a number that says how much counter should change by
    neighbors[x][y] += 1
    if grid[x][y]: 
        if neighbors[x][y] == 4:
            return -1
        elif neighbors[x][y] == 3:
            return 1
    return 0

# I tracked the directions that I needed to track like this
# for simplicity; you could easily have a few separate calls
# to updateNeighbor that accomplish the same thing
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    x, y = map(int, input().split())
    grid[x][y] = True
    if neighbors[x][y] == 3:
        count += 1
    for dx, dy in dirs:
        count += updateNeighbor(x + dx, y + dy)
    print(count)