import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

sqft = 0
for present in data:
    l, w, h = map(int, present.split('x'))
    sqft += 2*l*w + 2*w*h + 2*h*l
    sqft += min(l*w, w*h, h*l)
print(sqft)