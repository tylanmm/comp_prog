def solve(printers):
    lim = [min([p[i] for p in printers]) for i in range(4)]
    if sum(lim) < 1e6:
        return 'IMPOSSIBLE'
    ans = [0]*4
    rem = int(1e6)
    for i in range(4):
        amt = min(rem, lim[i])
        rem -= amt
        ans[i] = amt
    return ' '.join(map(str, ans))


for t in range(int(input())):
    printers = [tuple(map(int, input().split())) for _ in range(3)]
    print('Case #{}: {}'.format(t+1, solve(printers)))
