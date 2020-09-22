def solve(n, slices, d):
    freq = {}
    for s in slices:
        if s not in freq:
            freq[s] = 1
        else:
            freq[s] += 1
        if freq[s] == d:
            return 0
    
    if d == 2:
        return 1
    
    for s in freq:
        if s*2 in freq:
            return 1
        if freq[s] == 2 and s != max(freq):
            return 1
    
    return 2

for i in range(int(input())):
    n, d = map(int, input().split())
    slices = list(map(int, input().split()))
    print('Case #%d: %d' % (i+1, solve(n, slices, d)))