import sys

with open(sys.argv[1]) as f:
    data = f.read()

floor = 0
for i, c in enumerate(data, 1):
    floor += 1 if c == '(' else -1
    if floor < 0:
        print(i)
        break