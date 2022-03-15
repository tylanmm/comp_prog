from math import ceil, floor
s = [int(quad) for quad in input()]
zoom = len(s)
curr = int(2**zoom)
xlo, xhi, ylo, yhi = 0, curr-1, 0, curr-1

for quad in s:
    curr //= 2
    # if in the right half
    if quad % 2:
        xlo += curr
    else:
        xhi -= curr
    
    # if in the bottom half
    if quad > 1:
        ylo += curr
    else:
        yhi -= curr

print(zoom, xlo, ylo)