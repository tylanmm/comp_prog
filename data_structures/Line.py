class Line:
    def __init__(self, a=1, b=1, c=0):      # for storing line in form ax + by = c (for non-vertical lines, b = 1)
        self.a = a
        self.b = b
        self.c = c
    
    def pointsToLine(self, p1, p2):
        if abs(p1.x - p2.x) < 0.000001:     # if line is vertical
            self.a = 1
            self.b = 0
            self.c = -p1.x
        else:
            self.a = -((p1.y - p2.y) / (p1.x - p2.x))
            self.b = 1
            self.c = -(self.a * p1.x) - p1.y
    
    def areParallel(self, other):
        return abs(self.a - other.a) < 0.000001 and abs(self.b - other.b) < 0.000001
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c
    
    def intersect(self, other):
        if not self.areParallel(other):
            return False
        x = (other.b * self.c - self.b * other.c) / (other.a * self.b - self.a * other.b)
        y = -(self.a * x + self.c) if abs(self.b > 0.000001) else -(other.a * x + other.c)
        return Point(x, y)






from math import cos, sin, pi
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __bool__(self):
        return True

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    # rotate point by theta degrees CCW w.r.t. origin (0, 0)
    def rotate(self, theta):
        theta %= 360
        if theta % 90:      # not a multiple of 90 (avoid using expensive cosine function when possible)
            theta = (theta / 180) * pi      # cos and sin require radians (not degrees)
            self.x, self.y = self.x*cos(theta) - self.y*sin(theta), self.x*sin(theta) + self.y*cos(theta)
        elif theta == 90:
            self.x, self.y = -self.y,  self.x
        elif theta == 180:
            self.x, self.y = -self.x, -self.y
        elif theta == 270:
            self.x, self.y =  self.y, -self.x
    
    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5