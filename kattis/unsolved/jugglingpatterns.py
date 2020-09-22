from sys import stdin, stdout
from heapq import *

for line in stdin.readlines():
    line = list(map(int, line.strip()))
    total = sum(line)
    if abs(total/len(line) - round(total/len(line))) > 1e-6:
        stdout.write(f'{"".join(map(str, line))}: invalid # of balls\n')
        continue
    numBalls = total // len(line)

    b, h = 1, 0
    hands = [[], []]

stdout.flush()