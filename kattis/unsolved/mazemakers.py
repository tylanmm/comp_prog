def dfs(r, c, graph, visited, dir, h, w):
    if r < 0 or r >= h or c < 0 or c >= w:
        return 0, False
    
    if visited[r][c]:
        return 0, True
    
    total, repeat = 1, False
    visited[r][c] = True
    if dir != 1 and graph[r][c] & 1 == 0:
        amt, rep = dfs(r, c-1, graph, visited, 4, h, w)
        total += amt
        repeat |= rep
    if dir != 2 and graph[r][c] & 2 == 0:
        amt, rep = dfs(r+1, c, graph, visited, 8, h, w)
        total += amt
        repeat |= rep
    if dir != 4 and graph[r][c] & 4 == 0:
        amt, rep = dfs(r, c+1, graph, visited, 1, h, w)
        total += amt
        repeat |= rep
    if dir != 8 and graph[r][c] & 8 == 0:
        amt, rep = dfs(r-1, c, graph, visited, 2, h, w)
        total += amt
        repeat |= rep
    
    return total, repeat

def solve(h, w):
    # read in maze
    maze = []
    for r in range(h):
        row = []
        for c in input():
            row.append(int(c, 16))
        maze.append(row)
    
    # find openings
    openings = set()
    for i in range(w):
        if maze[0][i] & 8 == 0:
            openings.add((0, i))
        if maze[-1][i] & 2 == 0:
            openings.add((h-1, i))
    
    for i in range(h):
        if maze[i][0] & 1 == 0:
            openings.add((i, 0))
        if maze[i][-1] & 4 == 0:
            openings.add((i, w-1))
    
    # check that there are two openings
    if len(openings) != 2:
        return 'NO SOLUTION'

    # run dfs/floodfill
    visited = [[False]*w for _ in range(h)]
    r1, c1 = openings.pop()
    amt, repeat = dfs(r1, c1, maze, visited, -1, h, w)
    r2, c2 = openings.pop()
    
    # determine statement
    if not visited[r2][c2]:
        return 'NO SOLUTION'
    elif amt != h*w:
        return 'UNREACHABLE CELL'
    elif repeat:
        return 'MULTIPLE PATHS'
    else:
        return 'MAZE OK'

h, w = map(int, input().split())
while h and w:
    print(solve(h, w))