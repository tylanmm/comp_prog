from sys import stdin, stdout
from collections import deque

# read input, set up tree
n = int(stdin.readline())
g = [set() for _ in range(n)]
for _ in range(n-1):
    # make farms 0-indexed to make storage/retrieval simpler
    a, b = map(lambda x: int(x)-1, stdin.readline().split())
    g[a].add(b)
    g[b].add(a)

# add dummy value to the first farm to balance out the -1 later on
g[0].add(0)

# run bfs
days = 0
amt = [0]*n
amt[0] = 1
q = deque([0])
while q:
    curr_farm = q.popleft()

    # double the infected amt there until num_infected > num_children
    # (strictly greater since 1 needs to stay behind)
    # subtract 1 from the number of neighbors so that the parent is ignored
    while amt[curr_farm] <= len(g[curr_farm]) - 1:
        amt[curr_farm] *= 2
        days += 1
    
    # send 1 infected to each of the uninfected neighbors
    # add to the queue to repeat the process there
    for neighbor in g[curr_farm]:
        if amt[neighbor] == 0:
            q.append(neighbor)
            amt[neighbor] += 1
            amt[curr_farm] -= 1
            days += 1

stdout.write(str(days) + '\n')