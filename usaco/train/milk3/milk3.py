"""
ID: tylan071
LANG: PYTHON3
TASK: milk3
"""

with open('milk3.in') as f:
    a, b, c = map(int, f.readline().split())

cLevels = set()
used = set()
def dfs(amts):
    if amts in used:
        return
    used.add(amts)
    if amts[0] == 0:
        cLevels.add(amts[2])
    
    for child in genChildren(amts):
        if child not in used:
            dfs(child)

def genChildren(amts):
    children = []
    # pour type 1: into bucket a...
    if amts[0] < a:
        # ...from bucket b
        if amts[1] > 0:
            if amts[0] + amts[1] <= a:
                children.append((amts[0] + amts[1], 0, amts[2]))
            else:
                children.append((a, amts[1] - (a - amts[0]), amts[2]))
        # ...from bucket c
        if amts[2] > 0:
            if amts[0] + amts[2] <= a:
                children.append((amts[0] + amts[2], amts[1], 0))
            else:
                children.append((a, amts[1], amts[2] - (a - amts[0])))
    
    # pour type 2: into bucket b...
    if amts[1] < b:
        # ...from bucket a
        if amts[0] > 0:
            if amts[1] + amts[0] <= b:
                children.append((0, amts[1] + amts[0], amts[2]))
            else:
                children.append((amts[0] - (b - amts[1]), b, amts[2]))
        # ...from bucket c
        if amts[2] > 0:
            if amts[1] + amts[2] <= b:
                children.append((amts[0], amts[1] + amts[2], 0))
            else:
                children.append((amts[0], b, amts[2] - (b - amts[1])))
    
    # pour type 3: into bucket c...
    if amts[2] < c:
        # ...from bucket a
        if amts[0] > 0:
            if amts[2] + amts[0] <= c:
                children.append((0, amts[1], amts[2] + amts[0]))
            else:
                children.append((amts[0] - (c - amts[0]), amts[1], c))
        # ...from bucket b
        if amts[1] > 0:
            if amts[2] + amts[1] <= c:
                children.append((amts[0], 0, amts[2] + amts[1]))
            else:
                children.append((amts[0], amts[1] - (c - amts[2]), c))
    
    return children
    
dfs((0, 0, c))

with open('milk3.out', 'w') as f:
    f.write(' '.join(map(str, sorted(list(cLevels)))) + '\n')