def fOdd(n):
    for i, c in enumerate(n):
        if int(c) % 2 == 1:
            return i
    return -1

def up(n):
    i = fOdd(n)
    if i == -1:
        return n
    elif n[i] != '9':
        return n[:i] + str(int(n[i]) + 1) + ('0'*(len(n) - i - 1))
    elif i == 0:
        return '10' + ('0'*(len(n) - i - 1))
    else:
        return n[:i-1] + str(int(n[i-1]) + 1) + ('0'*(len(n) - i))

def down(n, i):
    pass

def solve(n):
    pass
    
    

for t in range(int(input())):
    n = input()
    print('Case #%d: %d' % (t+1, solve(n)))