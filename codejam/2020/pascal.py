triangle = []
def step(n):
    global triangle
    for i in range(len(triangle), n):
        level = []
        for j in range(n):
            level.append((i + 1, j + 1))
        if i % 2 == 1:
            level.reverse()
        triangle.append(level)

def biggestRow(num):
    total = 0
    i = 0
    while total + 2**i <= num:
        total += 2**i
        i += 1
    return i, total

def reduce(lst):
    out = []
    for i in range(len(lst)):
        out.extend(lst[i])
    return out

def solve(n):
    rows, sum = biggestRow(n)
    step(biggestRow(rows))
    spots = reduce(triangle[:rows])
    for i in range(1, n - sum + 1):
        if 

for i in range(int(input())):
    print(biggestRow(int(input())))