for _ in range(int(input())):
    n = int(input())
    has = list(map(int, input().split()))

    # find index of first book
    f = 0
    while f < n and has[f] != 1:
        f += 1
    
    # find index of last book
    e = n-1
    while e > -1 and has[e] != 1:
        e -= 1
    
    # answer is total span minus the number of 1's
    print(e - f + 1 - has.count(1) if e >= f else 0)