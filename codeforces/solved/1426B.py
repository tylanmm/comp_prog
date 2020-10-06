for _ in range(int(input())):
    n, m = map(int, input().split())
    diag = False
    for _ in range(n):
        a, b = input().split()
        c, d = input().split()
        diag |= b == c
    print('YES' if diag and (m % 2 == 0) else 'NO')