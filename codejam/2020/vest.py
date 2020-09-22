def traverse(mat):
    trace = 0
    rowRep = 0
    colRep = 0

    for i in range(len(mat)):
        trace += mat[i][i]
        if len(set(mat[i])) < len(mat):
            rowRep += 1
    
    for i in range(len(mat)):
        col = set()
        for j in range(len(mat)):
            col.add(mat[j][i])
        if len(col) < len(mat):
            colRep += 1
    
    return trace, rowRep, colRep

for i in range(int(input())):
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    k, r, c = traverse(m)
    print('Case #%d: %d %d %d' % (i+1, k, r, c))