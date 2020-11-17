import sys

with open(sys.argv[1]) as f:
    g = {}
    while True:
        try:
            a, b = f.readline().strip().split(')')
            if a in g:
                g[a].append(b)
            else:
                g[a] = [b]
            
            if b not in g:
                g[b] = []
        except ValueError:
            break

depth = 0
def dfs(obj, d):
    global depth
    depth += d
    for n in g[obj]:
        dfs(n, d+1)

dfs('COM', 0)
print(depth)