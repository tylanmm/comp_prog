for _ in range(int(input())):
    n, perm = int(input()), list(map(int, input().split()))
    i = 1
    while i < n - 1:
        if perm[i-1] < perm[i] < perm[i+1]:
            perm.pop(i)
            n -= 1
        elif perm[i-1] > perm[i] > perm[i+1]:
            perm.pop(i)
            n -= 1
        else:
            i += 1
    
    print(n)
    print(' '.join(map(str, perm)))