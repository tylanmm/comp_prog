import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

ribbon = 0
for present in data:
    l, w, h = map(int, present.split('x'))
    ribbon += min(2*(l + w), 2*(w + h), 2*(l + h)) + l*w*h
print(ribbon)