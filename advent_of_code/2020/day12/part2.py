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
dxw, dyw = 10, 1
for c in comm:
    dir, amt = c[0], int(c[1:])
    if dir == 'N':
        dyw += amt
    elif dir == 'S':
        dyw -= amt
    elif dir == 'W':
        dxw -= amt
    elif dir == 'E':
        dxw += amt
    elif dir == 'L':
        for i in range(amt // 90):
            dxw, dyw = -dyw, dxw
    elif dir == 'R':
        for i in range(amt // 90):
            dxw, dyw = dyw, -dxw
    else:
        x += dxw * amt
        y += dyw * amt
print(abs(x) + abs(y))