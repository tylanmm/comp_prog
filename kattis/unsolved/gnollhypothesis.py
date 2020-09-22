def choose(n, k):
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res

print(choose(500, 250))