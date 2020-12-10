total = 0

with open('day1.in') as f:
    for line in f.readlines():
        total += max(0, int(line)//3 - 2)

print(total)