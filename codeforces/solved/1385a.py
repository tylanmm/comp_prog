for _ in range(int(input())):
    xyz = list(map(int, input().split()))
    m = max(xyz)
    if xyz.count(m) > 1:
        print('YES')
        print(m, min(xyz), 1)
    else:
        print('NO')