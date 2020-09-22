def factorial(n):
    res = n
    for i in range(2, n):
        res *= i
    return res

for i in range(1700, 2001):
    fact = str(factorial(i))
    j = len(fact) - 1
    while fact[j] == '0':
        j -= 1
    print(f'{i}, {len(fact)}, {len(fact)-j-1}')