for _ in range(int(input())):
    n, m = map(int, input().split())
    strs = [input() for _ in range(n)]
    used = [False]*n
    res = ''
    for j in range(m):
        diff = set()
        for i in range(n):
            diff.add(strs[i][j])
        #if len(diff) > 
