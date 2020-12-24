# read the input
n = int(input())
cows = {'N': [], 'E': [], 'S': [], 'W': []}
grass = [0]*n
for i in range(n):
    dir, x, y = input().split()
    cows[dir].append((int(x), int(y), i))

for x1, y1, i in cows['N']:
    y = float('inf')
    for x2, y2, j in cows['N']:
        if x1 == x2 and y2 > y1:
            y = min(y, y2)
    for x2, y2, j in cows['E']:
        if x2 <= x1 and y2 >= y1 and (x1 - x2) < (y2 - y1):
            y = min(y, y2)
    for x2, y2, j in cows['W']:
        if x2 >= x1 and y2 >= y1 and (x2 - x1) < (y2 - y1):
            y = min(y, y2)
    for x2, y2, j in cows['S']:
        if x1 == x2 and y2 > y1:
            y = min(y, (y1 + y2)//2 + 1)
    grass[i] = y - y1

# repeat that for each direction?