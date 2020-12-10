import sys

with open(sys.argv[1]) as f:
    data = [0] + [int(x) for x in f.read().split('\n')]

data.sort()
data.append(data[-1] + 3)

amts = [0]*4
for i in range(1, len(data)):
    amts[data[i] - data[i-1]] += 1
print(amts[1] * (amts[3]))