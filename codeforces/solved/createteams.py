for _ in range(int(input())):
    n, x = map(int, input().split())
    skill = sorted(list(map(int, input().split())))
    teams, i, size = 0, n-1, 0
    while i > -1:
        size += 1
        if skill[i] * size >= x:
            teams += 1
            size = 0
        i -= 1
    print(teams)