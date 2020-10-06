for _ in range(int(input())):
    n = int(input())
    x = int(n**0.5)
    y = n - x*x
    if y == 0:
        print(2*x - 2)
    elif y <= x:
        print(2*x - 1)
    else:
        print(2*x)