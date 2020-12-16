import sys
from time import time

s = time()

with open(sys.argv[1]) as f:
    start = [int(n) for n in f.read().split(',')]

last = {start[i]: [i, i] for i in range(len(start))}
last_num = start[-1]
for i in range(len(start), 30000000):
    last_num = last[last_num][1] - last[last_num][0]
    if last_num in last:
        last[last_num][0], last[last_num][1] = last[last_num][1], i
    else:
        last[last_num] = [i, i]

print(last_num)

e = time()
print(f'Time elapsed: {e-s:.3f} s')