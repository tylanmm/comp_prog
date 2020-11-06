for _ in range(int(input())):
    n = int(input())
    gang = list(map(int, input().split()))
    edges = []
    g = gang[0]
    other = -1
    same = []
    for i in range(1, n):
        if g != gang[i]:
            edges.append((1, i+1))
            other = i+1
        else:
            same.append(i+1)
    
    if other == -1:
        print('NO')
        continue
    
    print('YES')

    for i in same:
        print(other, i)
    
    for x, y in edges:
        print(x, y)