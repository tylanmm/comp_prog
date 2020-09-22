n, m, sx, sy = map(int, input().split())
visited = [[False]*(m+1) for _ in range(n+1)]

visited[sx][sy], visited[1][sy] = True, True
print(sx, sy)
print(1, sy)

x = 1
while x <= n:
    y = 1
    if not visited[x][y]: 
        visited[x][y] = True
        print(x, y)
    
    y += 1
    lastY = y
    while y <= m:
        if not visited[x][y]:
            lastY = y if not (y == sy and x+1 == sx) else lastY
            visited[x][y] = True
            print(x, y)
        y += 1
    
    x += 1
    if x <= n:
        visited[x][lastY] = True
        print(x, lastY)