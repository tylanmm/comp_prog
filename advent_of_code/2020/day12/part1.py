import sys

def read_lines(file, data_type=int, split_char=' '):
    data = file.read().split('\n')
    for i in range(len(data)):
        data[i] = data[i].split(split_char)
        if len(data[i]) == 1:
            data[i] = data_type(data[i][0])
            continue
        for j in range(len(data[i])):
            data[i][j] = data_type(data[i][j])
    return data

with open(sys.argv[1]) as f:
    comm = read_lines(f, str)

x, y = 0, 0
dx, dy = 1, 0
for c in comm:
    dir, amt = c[0], int(c[1:])
    if dir == 'N':
        y += amt
    elif dir == 'S':
        y -= amt
    elif dir == 'W':
        x -= amt
    elif dir == 'E':
        x += amt
    elif dir == 'L':
        for i in range(amt // 90):
            dx, dy = -dy, dx
    elif dir == 'R':
        for i in range(amt // 90):
            dx, dy = dy, -dx
    else:
        x += dx * amt
        y += dy * amt
print(abs(x) + abs(y))