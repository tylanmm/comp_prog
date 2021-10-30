col = int(input())
order = list(map(int, input().split()))
s = input()
grid, i, n = [], 0, len(s)
while i < n:
    if i % col == 0:
        grid.append(['']*col)
    grid[-1][i % col] = (s[i])
    i += 1

for c in order:
    print(''.join([grid[i][c-1] for i in range(len(grid))]), end='')
print()