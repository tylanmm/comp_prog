def solve(n, x):
    count = 0
    for i in range(1, n):

        # no change necessary
        if x[i] > x[i-1]: 
            continue
        
        # we HAVE to multiply by 10
        if len(str(x[i])) == len(str(x[i-1])):
            x[i] *= 10
            count += 1
            continue
        
        diff = len(str(x[i-1])) - len(str(x[i]))
        # we can make current number into the previous, + 1 to lowest digit
        if (int(str(x[i-1])[:-diff]) <= x[i]) and any([d != '9' for d in str(x[i-1])[-diff:]]):
            x[i] = x[i]*(10**diff) + (x[i-1] % (10**diff)) + 1
            count += diff

        # just add a bunch of zeros
        else:
            x[i] *= 10**(diff+1)
            count += diff + 1
    
    return count

for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    print(f'Case #{t+1}: {solve(n, x)}')