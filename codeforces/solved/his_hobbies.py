for _ in range(int(input())):
    n = int(input())
    S = set(map(int, input().split()))
    if n % 2:
        print(-1)
        continue
    for k in range(1, max(S)<<1):
        for s in S:
            if s ^ k not in S:
                break
        else:
            print(k)
            break
    else:
        print(-1)