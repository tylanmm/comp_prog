import heapq
q = []
infLevel = {}

def binSearch(name):
    lo, hi = 0, len(q) - 1
    level = -infLevel[name]
    while lo < hi:
        mid = (lo + hi) // 2
        if q[mid][0] == level:
            if q[mid][2] == name:
                return mid
            hi = mid
        elif q[mid][0] > level:
            hi = mid - 1
        else:
            lo = mid + 1
    
    # Now linear search until you find the cat's index
    while q[lo][2] != name:
        lo += 1
    return lo

numCats = 0
for _ in range(int(input())):
    line = input()
    if line[0] == '0':
        numCats += 1
        com, name, level = line.split()
        level = int(level)
        infLevel[name] = level
        heapq.heappush(q, (-level, numCats, name))
    elif line[0] == '1':
        com, name, level = line.split()
        level = int(level)
        l, num, name = q.pop(binSearch(name))
        infLevel[name] += level
        heapq.heappush(q, (-infLevel[name], num, name))
    elif line[0] == '2':
        com, name = line.split()
        q.pop(binSearch(name))
        infLevel.pop(name)
    else:
        print('The clinic is empty' if not q else q[0][2])