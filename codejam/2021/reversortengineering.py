def getFlips(n, c):
    res = []
    while c:
        if n-1 <= c:
            res.append(n)
            c -= n-1
        n -= 1
    return res[::-1]

def solve(n, c):
    if c < n-1 or c > n*(n+1)//2 - 1:
        return 'IMPOSSIBLE'

    lst = list(range(1, n+1))
    for amt in getFlips(n, c - n + 1):
        lst[-amt:] = lst[-amt:][::-1]
    return ' '.join(map(str, lst))

for t in range(1, 1+int(input())):
    n, c = map(int, input().split())
    print(f'Case #{t}: {solve(n, c)}')