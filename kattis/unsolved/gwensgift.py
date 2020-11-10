def isValid(n, k):
    for i in range(len(n)):
        for j in range(i+1, len(n)+1):
            if sum(n[i:j]) % k == 0:
                return False
    return True

def allDigitsValid(n, k):
    for d in n:
        if not (0 < d < k):
            return False
    return True

def showAll(k):
    lo = int('1'*(k-1))
    hi = int(str(k-1)*(k-1))

    total = 0
    for i in range(lo, hi+1):
        n = list(map(int, str(i)))
        if allDigitsValid(n, k) and isValid(n, k):
            total += 1
            print(f'{total}\t{i:>8}\t{sum(n):>3}\t{sum(n)%k:>4}')
            # print('%d\t%d\t%d\t%d' % (total, i, sum(n), sum(n) % k))
    print('Total: %d' % total)

for i in range(2, 7):
    print('Valid numbers for n = %d' % i)
    showAll(i)
    print()