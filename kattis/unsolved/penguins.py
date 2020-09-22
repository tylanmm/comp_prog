from math import sqrt

def areClose(f1, f2):
    return sqrt((f2[0] - f1[0])**2 + (f2[1] - f1[1])**2) <= d



def maxFlow(end):
    


n, d = map(float, input().split())
n = int(n)
srcs = set()
numPenguins = 0
floes = []
for i in range(n):
    f = tuple(map(int, input().split()))
    floes.append(f)
    if f[2] > 0:
        srcs.add(i)
        numPenguins += f[2]

g = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if areClose(floes[i], floes[j]):
            g[i].append(j)
            g[j].append(i)




