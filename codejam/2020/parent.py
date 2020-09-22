def solve(times, start, end):
    out = [''] * (times[-1][2] + 1)
    times.sort()
    cAvail = 0
    jAvail = 0
    
    for t in times:
        if t[0] >= cAvail:
            cAvail = t[1]
            out[t[2]] = 'C'
        elif t[0] >= jAvail:
            jAvail = t[1]
            out[t[2]] = 'J'
        else:
            return 'IMPOSSIBLE'
    
    return ''.join(out)

for i in range(int(input())):
    start = 24 * 60
    end = 0
    times = []
    for j in range(int(input())):
        s, e = map(int, input().split())
        start = min(start, s)
        end = max(end, e)
        times.append((s, e, j))
    
    print('Case #%d: %s' % (i+1, solve(times, start, end)))