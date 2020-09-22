for _ in range(int(input())):
    seen = {'1':-1, '2':-1, '3':-1}
    s = input()
    best = len(s) + 1
    vals = seen.values()
    for i in range(len(s)):
        seen[s[i]] = i
        if -1 not in vals:
            best = min(best, max(vals) - min(vals) + 1)
    if best == len(s) + 1:
        print(0)
    else:
        print(best)