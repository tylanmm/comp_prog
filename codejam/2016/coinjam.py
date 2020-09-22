import math

coins = {}

def isPrime(n, coin):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            coins[coin].append(str(i))
            return False
    return True

def check(n):
    converts = [int(n, i) for i in range(2, 11)]
    print(converts)
    coins[n] = []
    for num in converts:
        if isPrime(num, n):
            coins.pop(n)
            print('%d is prime' % (num))
            return        

with open('coinjam.in') as f:
    f.readline()
    out = open('coinjam.out', 'w')
    n, j = tuple(map(int, f.readline().strip().split()))
    num = '1' + '0'*(n-2) + '1'
    while len(coins) < j:
        check(num)
        print(len(coins))
        num = bin(int(num, 2) + 1)[2:]
    
    out.write('Case #1:\n')
    for coin in coins:
        out.write('%s %s\n' % (coin, ' '.join(coins[coin])))
    
    out.close()