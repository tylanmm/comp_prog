from sys import argv

w, h = 25, 6

with open(argv[1]) as f:
    data = f.read().strip()

res = ['2']*w*h
for i in range(0, len(data), h*w):
    layer = data[i:i+h*w]
    for i in range(w*h):
        if res[i] == '2':
            res[i] = layer[i]

i = 0
for j in range(h):
    for k in range(w):
        print(' ' if res[i] == '0' else 'X', end='')
        i += 1
    print()