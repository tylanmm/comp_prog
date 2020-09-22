points = [tuple(map(int, input().split())) for _ in range(int(input()))]
points.append(points[0])

def calcArea(points):
    total = 0
    for i in range(len(points)):
        total += points[i][0]*points[i+1][1] - points[i][1]*points[i+1][0]
    return total

area = calcArea(points)
amt = 2*area
removed = set()
i = 0
while i < len(points):
    if len(points) >= 3:
        if 0 < i < len(points)-2:
            a = calcArea(points[i-1:i+1])
        elif i == 0:
            a = calcArea([points[-1]] + points[:2])
        else:
            a = calcArea(points[-2:] + [points[0]])
        if amt - 2*a + points[i][2] > amt:
            amt += points[i][2] - 2*a
            removed.add(points.pop(i))
            i -= 1
    i += 1