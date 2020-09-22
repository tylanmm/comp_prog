"""
ID: tylan071
LANG: PYTHON3
TASK: wormhole
"""

with open('wormhole.in') as f:
    n = int(f.readline())
    holes = []
    for _ in range(n):
        holes.append(tuple(map(int, f.readline().split())))

# sort holes so that if two consecutive holes have the same y,
# the second hole is to the right of the first
holes.sort()
holes.sort(key=lambda x:x[1])
right = [-1] * n
for i in range(1, n):
    if holes[i][1] == holes[i-1][1]:
        right[i-1] = i

# list to keep track of which holes are paired up at any point in our recursive calls
# -1 indicates an unpaired wormhole
partner = [-1] * n

# determine if given pairing contains a cycle somewhere
def hasCycle():
    # start at each wormhole
    for i in range(n):
        pos = i
        # take n steps through the pairing
        for _ in range(n):
            pos = right[partner[pos]]
            if pos == -1:
                break
        
        if pos != -1:
            return True
    return False

def solve():
    # find first unmatched hole
    for i in range(n):
        if partner[i] == -1:
            break
    else:
        # if there's nothing left to match up, check for a cycle
        return 1 if hasCycle() else 0

    # once you have your unmatched hole, match if up with something
    total = 0
    for j in range(i+1, n):
        if partner[j] == -1:
            partner[i] = j
            partner[j] = i
            total += solve()
            # after you've tested everything with that pairing, reset
            partner[i] = partner[j] = -1
    
    return total

with open('wormhole.out', 'w') as f:
    f.write(f'{solve()}\n')