import sys
from collections import deque

with open(sys.argv[1]) as f:
    p1, p2 = f.read().split('\n\n')

p1 = deque(map(int, p1.split('\n')[1:]))
p2 = deque(map(int, p2.split('\n')[1:]))

while p1 and p2:
    if p1[0] > p2[0]:
        p1.append(p1.popleft())
        p1.append(p2.popleft())
    else:
        p2.append(p2.popleft())
        p2.append(p1.popleft())

score = 0
while p1:
    score += len(p1) * p1.popleft()
while p2:
    score += len(p2) * p2.popleft()
print(score)