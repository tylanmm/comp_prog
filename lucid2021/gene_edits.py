from collections import deque

s = input()
n = int(input())
edits = []
for _ in range(n):
    i, edit = input().split()
    edits.append((int(i), edit))

dq = deque(s)
res = []
for i, edit in edits:
    while len(res) < i and dq:
        res.append(dq.popleft())
    if str.isnumeric(edit):
        amt = min(int(edit), len(dq))
        while amt:
            dq.popleft()
            amt -= 1
    else:
        for c in edit[::-1]:
            dq.appendleft(c)

print(''.join(res) + ''.join(dq))