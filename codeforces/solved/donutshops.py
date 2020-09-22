for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x1, x2 = -1, -1
    if a < c:
        x1 = 1
    if a*b > c:
        x2 = b
    print(x1, x2)