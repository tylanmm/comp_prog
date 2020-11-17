def calcFuel(w):
    t = w//3 - 2
    if t > 0:
        return t + calcFuel(t)
    return 0

total = 0

with open('day1.in') as f:
    for line in f.readlines():
        total += calcFuel(int(line))

print(total)