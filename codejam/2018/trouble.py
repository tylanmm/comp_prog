def troubleSort(v):
    done = False
    while not done:
        done = True
        for i in range(len(v) - 2):
            if v[i] > v[i+2]:
                done = False
                temp = v[i+2]
                v[i+2] = v[i]
                v[i] = temp
    return v

def isSorted(v):
    for i in range(len(v) - 1):
        if v[i] > v[i+1]:
            return i
    return -1

t = int(input())
for i in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    v = troubleSort(v)
    problem = isSorted(v)
    if problem == -1:
        print("Case #%d: OK" % (i+1))
    else:
        print("Case #%d: %d" % (i+1, problem))