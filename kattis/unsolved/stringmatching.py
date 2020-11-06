from sys import stdin, stdout

p = [1007]
m = int(1e9 + 7)

def hash(s):
    while len(p) < len(s):
        p.append(p[-1] * 1007)
    
    arr = [ord(s[0])]
    for i in range(1, len(s)):
        arr.append(ord(s[i])*p[i] + arr[-1])
    return arr

def getHash(h, i, j):
    if i == 0:
        return h[j]
    else:
        return (h[j] - h[i-1])

lines = stdin.readlines()
for i in range(0, len(lines), 2):
    pos = []
    h1 = hash(lines[i])
    h2 = hash(lines[i+1])
    
    if len(h1) > len(h2):
        print()
        continue

    for i in range(len(h2) - len(h1) + 1):
        pass
