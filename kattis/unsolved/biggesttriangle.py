class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.m = ((p2[1] - p1[1]) / (p2[0] - p1[0])) if p2[0] - p1[0] else float('inf')
        self.b = (p1[1] - self.m*p1[0]) if self.m != float('inf') else -float('inf')
    
    def eval(self, x):
        if self.m != float('inf'):
            return self.m * x + self.b
        else:
            return 
    
    def findIntersection(self, other):
        x = (other.b - self.b) / (self.m - other.m)
        return (x, self.eval(x))

def getDist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def getPerimeter(line1, line2, line3):
    p1 = line1.findIntersection(line2)
    p2 = line1.findIntersection(line3)
    p3 = line2.findIntersection(line3)
    return getDist(p1, p2) + getDist(p2, p3) + getDist(p1, p3)

n = int(input())
lines = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(Line((x1, y1), (x2, y2)))

hi = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            hi = max(getPerimeter(lines[i], lines[j], lines[k]), hi)

print(hi if hi else 'no triangle')