def solve(x, y, path):
    time = 0
    
    for c in path:
        if c == 'N':
            y += 1
        elif c == 'E':
            x += 1
        elif c == 'S':
            y -= 1
        else:
            x -= 1
        
        time += 1
        if abs(x) + abs(y) <= time:
            return str(time)
    
    return 'IMPOSSIBLE'


for i in range(int(input())):
    x, y, path = input().split()
    x, y = int(x), int(y)
    print('Case #%d: %s' % (i+1, solve(x, y, path)))