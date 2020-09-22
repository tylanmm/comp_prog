for _ in range(int(input())):
    n, S = map(int, input().split())
    parent = list(range(n+1))
    weight = [0] * (n+1)
    