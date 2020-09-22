from math import cos, sin, pi, tan, radians
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def scale(self, c):
        self.x *= c
        self.y *= c
    
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
    

for _ in range(int(input())):
    n = 2*int(input())
    apot = 0.5*tan(radians((90*n - 180)/n))
    if n % 4 == 0:
        print(apot*2)
    else:
        diag = 2*(0.25 + apot**2)**0.5
        v = Vector(diag, 0)
        u = Vector(diag, 0)
        v.rotate(90/n)
        u.scale(u.dot(v) / u.dot(u))
        print(u.magnitude())