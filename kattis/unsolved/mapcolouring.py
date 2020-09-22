lo = float('inf')
def color(country, comp):
    global lo
    
    poss = {1, 2, 3, 4}
    for n in g[country]:
        poss.discard(colors[n])
    
    if not poss:
        return

    numColored = 0
    for n in comp:
        numColored += colors[n] != 0
    if numColored + 1 == len(comp):
        lo = min(lo, max(max(colors), min(poss)))
        return
    
    for c in poss:
        colors[country] = c
        for n in g[country]:
            if colors[n] == 0:
                color(n, comp)
        colors[country] = 0

def dfs(country, comp):
    colors[country] = 1
    comp.append(country)
    for n in g[country]:
        if not colors[n]:
            dfs(n, comp)

def findComponents():
    comps = []
    for i in range(len(colors)):
        if colors[i] == 0:
            comp = []
            dfs(i, comp)
            comps.append(comp)
    return comps

for _ in range(int(input())):
    c, b = map(int, input().split())
    g = {i:set() for i in range(c)}
    for border in range(b):
        i, j = map(int, input().split())
        g[i].add(j)
        g[j].add(i)
    
    lo = float('inf')
    colors = [0]*c
    comps = findComponents()
    colors = [0]*c
    for comp in comps:
        color(comp[0], comp)
    print(lo if lo < 5 else 'many')