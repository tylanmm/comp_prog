from math import sin, cos, pi, atan

n = int(input())
x, y, d = 0, 0, 0
for _ in range(n):
    di, deg, pace = input().split()
    d = (d + int(deg) * (-1 if di == 'Right' else 1)) % 360
    pace = int(pace)
    x += pace * cos(d * pi / 180)
    y += pace * sin(d * pi / 180)

paces = round((x*x + y*y)**0.5)
degrees = atan(y / x) * 180 / pi if abs(x) > 0.000001 else 90
# print(degrees)
if x < 0 and y > 0: degrees += 180
if y < 0: degrees = (180 - degrees) % 180
degrees = round(degrees)
print('Left' if y >= 0 else 'Right', degrees, paces)