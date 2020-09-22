class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.neighbors = []
    
    def addNeighbors(self, grid):
        for i in range(len(grid)):
            if i == self.x:
                continue
            for j in range(len(grid[0])):
                if j == self.y:
                    continue
                if i - j == self.x - self.y:
                    continue
                if i + j == self.x + self.y:
                    continue
                self.neighbors.append(grid[i][j])
    
    def hasCycle(self, maxLen, path = '', numVisited = 0):
        numVisited += 1
        path += self.__repr__()
        if numVisited == maxLen:
            return True, path
       
        self.visited = True
        foundPath = False
        for n in self.neighbors:
            if not n.visited:
                n.visited = True
                foundPath, path2 = n.hasCycle(maxLen, path, numVisited)
                if foundPath:
                    return foundPath, path2
                n.visited = False
        self.visited = False
        return foundPath, path

    def __repr__(self):
        return '%d %d\n' % (self.x, self.y)

for k in range(int(input())):
    xMax, yMax = map(int, input().split())
    grid = [[Cell(x, y) for y in range(yMax)] for x in range(xMax)]
    for i in range(xMax):
        for j in range(yMax):
            grid[i][j].addNeighbors(grid)
    
    foundPath = False
    path = ''
    for row in grid:
        for col in row:
            foundPath, path = col.hasCycle(xMax * yMax)
            if foundPath:
                break
        if foundPath:
            break
    
    if foundPath:
        print('Case #%d: POSSIBLE' % (k+1))
        print(path)
    else:
        print('Case #%d: IMPOSSIBLE' % (k+1))
