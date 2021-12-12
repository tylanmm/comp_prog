grid = [list(map(int, input())) for _ in range(10)]

ans = 0
dirs = [(i, j) for j in range(-1, 2) for i in range(-1, 2)]
dirs.remove((0, 0))

def flash(i, j, flashes):
    flashes.add((i, j))
    for di, dj in dirs:
        if 0 <= i+di < 10 and 0 <= j+dj < 10:
            grid[i+di][j+dj] += 1
            if grid[i+di][j+dj] == 10:
                flash(i+di, j+dj, flashes)

for step in range(100):
    flashes = set()
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1
            if grid[i][j] == 10:
                flash(i, j, flashes)
    
    ans += len(flashes)
    for i, j in flashes:
        grid[i][j] = 0

print(ans)