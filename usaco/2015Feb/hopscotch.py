# Read in the data
with open("hopscotch.in") as f:
    raw = f.read().split()
    R, C = tuple(map(int, raw[:2]))
    hopscotch = raw[2:]

# Create an empty grid that will contain the number of ways to get to a given cell
# Initialize every cell to 0
grid = []
for i in range(R):
    row = []
    for j in range(C):
        row.append(0)
    grid.append(row)

# Set the top right cell to 1 (since we start there)
grid[0][0] = 1

# Loop through every row and column that can be a starting place (not on the edge, value isn't 0)
for r in range(R - 1):
    for c in range(C - 1):
        if grid[r][c] == 0:
            continue
        color = hopscotch[r][c]
        val = grid[r][c]
        # For every cell below and to the right,
        for i in range(r + 1, R):
            for j in range(c + 1, C):
                # If it's a different color, increase that cell's count by the amount in the cell we are "hopping" from
                if hopscotch[i][j] != color:
                    grid[i][j] += val

# Answer is the value in the bottom right cell
with open("hopscotch.out", "w") as f:
    f.write(str(grid[-1][-1]))