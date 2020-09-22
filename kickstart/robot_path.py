def solve(path):
    i = 0
    n = len(path)
    delX = 0
    delY = 0
    while i < n:
        if path[i] == 'N':
            delY -= 1
        elif path[i] == 'S':
            delY += 1
        elif path[i] == 'E':
            delX += 1
        elif path[i] == 'W':
            delX -= 1
        elif path[i] == ')':
            return delX, delY, i
        else:
            subPath = solve(path[i+2:])
            delX += int(path[i]) * subPath[0]
            delY += int(path[i]) * subPath[1]
            i += subPath[2] + 2
        i += 1
    return delX, delY, i

size = 10**9
for i in range(int(input())):
    x, y, _ = solve(input())
    print('Case #%d: %d %d' % (i+1, (x+size) % size + 1, (y+size) % size + 1))