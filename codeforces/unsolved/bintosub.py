from collections import deque
for _ in range(int(input())):
    n, s = int(input()), input()
    ans = [0]*n
    ans[0] = 1
    d = deque()
    d.append((s[0], 1))
    for i in range(1, n):
        if s[i] == '0':
            if d[-1][0] == '1':
                ans[i] = d[-1][1]
                d.appendleft(('0', d.pop()[1]))
            else:
                ans[i] = len(d) + 1
                d.appendleft(('0', len(d) + 1))
        else:
            if d[0][0] == '0':
                ans[i] = d[-1][1]
                d.append(('1', d.popleft()[1]))
            else:
                ans[i] = len(d) + 1
                d.append(('1', len(d) + 1))
    print(len(d))
    print(' '.join(map(str, ans)))