from collections import deque

n, r = map(int, input().split())
BOUND = 2**(n+1)
exposed = set()
for i in map(int, input().split()):
    while i:
        exposed.add(i)
        i //= 2

q = deque([1])
K = []
while q:
    curr = q.popleft()
    if curr not in exposed:
        K.append(curr)
    elif curr*2 < BOUND:
        q.append(2*curr)
        q.append(2*curr+1)
print(*K)