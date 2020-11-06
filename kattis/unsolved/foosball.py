from collections import deque

n = int(input())
wo, bo, wd, bd, *q = input().split()
q = deque(q)
hi = 0
best = []
wins = {}

for g in input():
    if g == 'W':
        wo, wd = wd, wo
        q.append(bd)
        bd, bo = bo, q.popleft()
        if wd + ' ' + wo not in wins and wo + ' ' + wd not in wins:
            wins[0]