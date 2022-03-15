for _ in range(int(input())):
    r, b, m = map(lambda x: int(x.replace('.', '')), input().split())
    payments = 0
    while b > 0 and payments <= 1200:
        b += (b*r + 5000)//10000 - m
        payments += 1
    print(payments if payments <= 1200 else 'impossible')
