n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    k, l = map(int, input().split())
    g[k][l] = 1
    g[l][k] = 1

for c in range(n-1):
    numC = sum(g[c])
    for i in range(n):
        g[c][i] = 1/numC if g[c][i] else 0
for i in range(n-1):
    g[i] = g[i][:-1]
g.pop()

def add(mat1, mat2):
    res = [[0]*len(mat1[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            res[i][j] = mat1[i][j] + mat2[i][j]
    return res

def mult(mat1, mat2):
    res = [[0]*len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

def multV(mat, v):
    res = [0]*len(mat)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[i] += mat[i][j] * v[j]
    return res

def power(mat, p):
    for _ in range(p):
        mat = mult(mat, mat)
    return mat

res = [[0]*(n-1) for _ in range(n-1)]
res = add(res, g)
for _ in range(10):
    g = mult(g, g)
    res = add(res, g)
    for r in res:
        print(r)
    print()

print(multV(res, [1]*len(res[0])))