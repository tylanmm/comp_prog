from sys import stdin

def flood(grid, R, C, i, j):
    if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] != '-':
        return
    
    grid[i][j] = '#'
    flood(grid, R, C, i+1, j)
    flood(grid, R, C, i-1, j)
    flood(grid, R, C, i, j+1)
    flood(grid, R, C, i, j-1)

lines = stdin.readlines()
l, numLines, t = 0, len(lines), 1

while l < numLines:
    m, n = map(int, lines[l].split())
    grid = [list(lines[j].strip()) for j in range(l+1, l+1+m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '-':
                count += 1
                flood(grid, m, n, i, j)
    print('Case %d: %d' % (t, count))
    l += 1 + m
    t += 1