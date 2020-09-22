def solve(u):
    letters = {}
    for _ in range(10**4):
        q, r = input().split()
        i = 0
        for c in r[::-1]:
            if c not in letters:
                letters[c] = [0] * u
            letters[c][i] += 1
            i += 1
    
    out = []
    for l in letters:
        out.append((letters[l][-1], l))
    out.sort()
    realOut = ''
    for i in range(1, 10):
        realOut = out[i][1] + realOut
    return out[0][1] + realOut

for i in range(int(input())):
    print('Case #%d: %s' % (i+1, solve(int(input()))))