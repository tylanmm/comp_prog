for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    dist = k
    count = 0
    for i in range(n):
        if s[i] == '1':
            if dist < k:
                count -= 1
            dist = 0
        elif dist >= k:
            count += 1
            dist = 0
        else:
            dist += 1
    
    print(count)