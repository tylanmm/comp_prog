import sys
from math import ceil

with open(sys.argv[1]) as f:
    t = int(f.readline())
    data = f.read().split(',')

for i in range(len(data)):
    if data[i] == 'x':
        continue


