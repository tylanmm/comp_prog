for _ in range(int(input())):
    n = int(input())
    size = list(map(int, input().split()))
    hi = max(size)
    if size.count(hi) == n:
        print(-1)
        continue
    
    for i in range(n):
        if size[i] == hi:
            if i == 0:
                if size[1] != hi:
                    print(1)
                    break
            elif i == n-1:
                if size[n-2] != hi:
                    print(n)
                    break
            else:
                if size[i-1] != hi or size[i+1] != hi:
                    print(i+1)
                    break