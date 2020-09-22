import heapq

def solve(n):
    heavy1 = []
    heavy2 = []
    equalw = []
    for _ in range(n):
        c, j = map(int, input().split())
        heavy1.append((c*2, j))
        heavy2.append((j*2, c))
        equalw.append((c+j, c, j))
    
    heapq.heapify(heavy1)
    heapq.heapify(heavy2)
    heapq.heapify(equalw)

    prev = 0
    diff = False
    allDiffW = True
    equalDiff = False
    for i in range(n):
        l = heapq.heappop(heavy1)
        m = heapq.heappop(heavy2)
        n = heapq.heappop(equalw)

        if not (l[0]//2 == m[1] and m[0]//2 == l[1]):
            diff = True
        
        if n[0] == prev:
            allDiffW = False
        
        if not (n[1] == m[1] and n[2] == l[1]):
            equalDiff = True
        prev = n[0]
    
    return 1 + diff + (allDiffW and equalDiff)

for i in range(int(input())):
    print('Case #%d: %d' % (i+1, solve(int(input()))))