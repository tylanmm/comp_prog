for _ in range(int(input())):
    s = input()
    opp = {'R':'P', 'S':'R', 'P':'S'}
    counts = {'R':0, 'S':0, 'P':0}
    hi, bestC = 0, 'R'
    for c in s:
        counts[c] += 1
        if counts[c] > hi:
            hi = counts[c]
            bestC = c
    print(opp[bestC]*len(s))