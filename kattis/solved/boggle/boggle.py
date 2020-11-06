from sys import stdin, stdout

# determine if word is in the boggle grid
def find(word, grid):
    visited = [[False]*4 for _ in range(4)]
    works = False
    for i in range(4):
        for j in range(4):
            if grid[i][j] == word[0]:
                works |= recur(word, grid, visited, i, j)
            if works:
                return True
    return False

# dfs in grid for word
def recur(word, grid, visited, r, c):
    if len(word) == 0:
        return True
    
    if r < 0 or r > 3 or c < 0 or c > 3 or visited[r][c] or word[0] != grid[r][c]:
        return False
    
    visited[r][c] = True
    works = False
    works = works or recur(word[1:], grid, visited, r+1, c)     # down
    works = works or recur(word[1:], grid, visited, r-1, c)     # up
    works = works or recur(word[1:], grid, visited, r, c+1)     # right
    works = works or recur(word[1:], grid, visited, r, c-1)     # left
    works = works or recur(word[1:], grid, visited, r-1, c-1)   # up left
    works = works or recur(word[1:], grid, visited, r-1, c+1)   # up right
    works = works or recur(word[1:], grid, visited, r+1, c-1)   # down left
    works = works or recur(word[1:], grid, visited, r+1, c+1)   # down right
    visited[r][c] = False

    return works

# calculate the three values for each boggle grid
def solve(board):
    score = 0
    best = ''
    found = 0

    for n in words:
        for w in words[n]:
            if find(w, board):
                score += points[n]
                found += 1
                if n > len(best):
                    best = w
                elif n == len(best):
                    best = min(best, w)

    stdout.write('%d %s %d\n' % (score, best, found))

# read in words, organize in dictionary
w = int(stdin.readline())
words = {i:set() for i in range(1, 9)}
for _ in range(w):
    word = stdin.readline().strip()
    words[len(word)].add(word)

# read grid, count found words
points = [0, 0, 0, 1, 1, 2, 3, 5, 11]
stdin.readline()
b = int(stdin.readline())
for i in range(b):
    grid = [stdin.readline().strip() for _ in range(4)]
    solve(grid)
    if i + 1 < b:
        stdin.readline()
stdout.flush()