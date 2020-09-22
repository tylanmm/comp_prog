for _ in range(int(input())):
    s = input()
    c = [0, 0]
    for n in s:
        c[int(n)] += 1
    print('DA' if min(c)%2 else 'NET')