from math import atan, ceil, cos, pi, sin

class balloon:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
    
    def __repr__(self):
        return '[({}, {}, {}), r={}]'.format(self.x, self.y, self.z, self.r)
    
    def __str__(self):
        return self.__repr__()

def calc_next_balloon(x, y, bi):
    for i in range(bi+1, len(balloons)):
        if balloons[i].r**2 - (x - balloons[i].x)**2 - (y - balloons[i].y)**2 > 0.0000001:
            return i, balloons[i]
    
def calc_dropoff(x, y, b):
    dx, dy = x - b.x, y - b.y
    theta = atan(dy / dx) if abs(dx) > 0.00001 else pi/2 if dy > 0 else -pi/2
    if dx < 0 and dy < 0: theta -= pi
    elif dx < 0: theta += pi
    new_x = b.r * cos(theta) + b.x
    new_y = b.r * sin(theta) + b.y
    return new_x, new_y

n = int(input())
balloons = [balloon(*map(int, input().split())) for _ in range(n)]
balloons.append(balloon(0, 0, 0, 200))
balloons.sort(key=lambda b: b.z, reverse=True)

x, y, z = 0, 0, 1500
bi, currBalloon = calc_next_balloon(x, y, -1)
while currBalloon.z > 0:
    x, y = calc_dropoff(x, y, currBalloon)
    z = currBalloon.z
    bi, currBalloon = calc_next_balloon(x, y, bi)
    x, y = round(x, 6), round(y, 6)

print(ceil(x), ceil(y))