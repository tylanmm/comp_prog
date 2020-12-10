import sys

with open(sys.argv[1]) as f:
    data = [0] + [int(x) for x in f.read().split('\n')]

data.sort()
data.append(data[-1] + 3)

ways = [0]*len(data)
ways[0] = ways[1] = 1
if data[2] - data[0] <= 3:
    ways[2] = 2
else:
    ways[2] = 1

for i in range(3, len(data)):
    for j in range(1, 4):
        if data[i] - data[i-j] <= 3:
            ways[i] += ways[i-j]
print(ways[-1])