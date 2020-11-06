for _ in range(int(input())):
    x = input()
    total = 10 * (int(x[0]) - 1)
    n = len(x)
    total += n * (n+1) // 2
    print(total)