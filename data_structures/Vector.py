from math import cos, sin, pi
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def toVec(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.dot(other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __str__(self):
        return f'[{self.x}; {self.y}]'
    
    def __bool__(self):
        return True

    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def scale(self, c):
        self.x *= c
        self.y *= c

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def magnitude(self):
        return self.dot(self)**0.5
    
    # rotate vector by theta degrees CCW w.r.t. origin (0, 0)
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
