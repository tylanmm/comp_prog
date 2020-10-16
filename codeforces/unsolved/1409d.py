def digitTotal(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

for _ in range(int(input())):
    n, s = map(int, input().split())
    N, total = n, digitTotal(n)
    
    i = 10
    while total > s:
        if int(str(n % i)[0]):
            input(str(total) + ' ' + str(n))
            total += 1 - int(str(n % i)[0])
            n -= n % i
            n += i
        i *= 10
    
    print(n - N)