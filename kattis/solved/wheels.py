def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def gcf(a, b):
    return gcf(b, a % b) if b else a

def reduce(a, b):
    GCF = max(gcf(max(abs(a), b), min(abs(a), b)), 1)
    return a // GCF, b // GCF

EPS = 1e-6

for _ in range(int(input())):
    n = int(input())
    cog = [tuple(map(int, input().split())) for _ in range(n)]
    seen = [False]*n
    speed = [(0, 0)]*n
    speed[0] = (1, 1)
    
    stack = [0]
    while stack:
        top = stack.pop()
        if seen[top]: continue
        seen[top] = True
        for i in range(n):
            if i == top or seen[i]: continue
            if abs(dist(cog[top][0], cog[top][1], cog[i][0], cog[i][1]) - cog[top][2] - cog[i][2]) > EPS: continue
            speed[i] = (-speed[top][0] * cog[top][2], speed[top][1] * cog[i][2])
            stack.append(i)

    for s in speed:
        a, b = reduce(*s)
        if a == 0:
            print('not moving')
        elif b == 1:
            print('{} {}'.format(abs(a), 'clockwise' if a > 0 else 'counterclockwise'))
        else:
            print('{}/{} {}'.format(abs(a), b, 'clockwise' if a > 0 else 'counterclockwise'))