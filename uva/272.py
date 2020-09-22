import sys

onLeft = True
for line in sys.stdin:
    for c in line:
        if c == '"':
            if onLeft:
                print('``', end='')
            else:
                print("''", end='')
            onLeft = not onLeft
        else:
            print(c, end='')