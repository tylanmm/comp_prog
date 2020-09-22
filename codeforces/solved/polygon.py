def solve(grid):
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            if grid[i][j] == '1' and grid[i+1][j] == '0' and grid[i][j+1] == '0':
                return 'NO'
    return 'YES'

for _ in range(int(input())):
    n = int(input())
    grid = [input() for _ in range(n)]
    print(solve(grid))        