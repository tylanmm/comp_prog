class Dance:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.grid = [list(map(int, input().split())) for _ in range(r)]
    
    def round(self):
        score = 0
        toElim = []
        change = False
        for i in range(self.r):
            for j in range(self.c):
                score += self.grid[i][j]
                if self.grid[i][j] != 0:
                    ave = self.calcAve(i, j)
                    if ave > self.grid[i][j]:
                        toElim.append((i, j))
                        change = True
        for t in toElim:
            self.grid[t[0]][t[1]] = 0
        return change, score
    
    def calcAve(self, i, j):
        total = 0
        count = 0

        r = i - 1
        if r >= 0:
            while r > 0 and self.grid[r][j] == 0:
                r -= 1
            if r != i and self.grid[r][j] != 0:
                total += self.grid[r][j]
                count += 1

        r = i + 1
        if r <= (self.r - 1):
            while r + 1 < self.r and self.grid[r][j] == 0:
                r += 1
            if r != i and self.grid[r][j] != 0:
                total += self.grid[r][j]
                count += 1
        
        r = i
        c = j - 1
        if c >= 0:
            while c > 0 and self.grid[i][c] == 0:
                c -= 1
            if c != j and self.grid[i][c] != 0:
                total += self.grid[i][c]
                count += 1
    
        c = j + 1
        if c <= (self.c - 1):
            while c + 1 < self.c and self.grid[i][c] == 0:
                c += 1
            if c != j and self.grid[i][c] != 0:
                total += self.grid[i][c]
                count += 1

        if count > 0:
            return total / count
        else:
            return self.grid[i][j]

    def __str__(self):
        return str(self.grid)

for i in range(int(input())):
    r, c = map(int, input().split())
    dance = Dance(r, c)
    totalScore = 0
    cont = True
    while cont:
        cont, roundScore = dance.round()
        totalScore += roundScore
    print('Case #%d: %d' % (i+1, totalScore))