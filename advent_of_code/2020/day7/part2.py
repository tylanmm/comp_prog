import sys

with open(sys.argv[1]) as f:
    rules = f.read().split('\n')

g = {}
for r in rules:
    r = r.split(' bag')
    p = r[0]
    if p not in g:
        g[p] = set()
    
    for color in r[1:]:
        if color == 's.' or color == '.':
            break

        amt, *color = color.split()[-3:]
        color = ' '.join(color)
        if color == 'no other':
            break
        g[p].add((color, int(amt)))

def dfs(color):
    if color in req:
        return req[color]    
    
    total = 1
    for p, amt in g[color]:
        if p not in req:
            req[p] = dfs(p)
        total += req[p] * amt
    req[color] = total
    return total

req = {}
print(dfs('shiny gold'))