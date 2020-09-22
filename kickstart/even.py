def findOdd(n):
    i = len(str(n)) - 1
    while i > -1 and (((n % 10**(i + 1)) // 10**i) % 2 != 1):
        i -= 1
    return i

def roundUp(n):
    i = findOdd(n)
    if i != -1:
        return ((n // 10**i) + 1) * 10**i
    return n

def roundDown(n):
    i = findOdd(n)
    if i != -1:
        return ((n // 10**i) * 10**i) - 1
    return n

def solve(n):
    if findOdd(n) == -1:
        return 0
    
    upDiff = 0
    oldUp = n
    while True:
        newUp = roundUp(oldUp)
        upDiff += newUp - oldUp
        if newUp == oldUp:
            break
        oldUp = newUp

    downDiff = 0
    oldDown = n
    while True:
        newDown = roundDown(oldDown)
        downDiff += oldDown - newDown
        if newDown == oldDown:
            break
        oldDown = newDown
    
    return min(upDiff, downDiff)

t = int(input())
for i in range(t):
    n = int(input())
    print("Case #%d: %d" % (i+1, solve(n)))