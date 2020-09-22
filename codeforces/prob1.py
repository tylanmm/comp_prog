for _ in range(int(input())):
    a, b = map(int, input().split())
    print((abs(a - b)//10) + (1 if (abs(a - b) % 10) > 0 else 0))