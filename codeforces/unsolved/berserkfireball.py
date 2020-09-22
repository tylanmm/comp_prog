def solve():
    n, m = map(int, input().split())
    x, k, y = map(int, input().split())
    powers = list(map(int, input().split()))
    goal = list(map(int, input().split()))

    if n == m:
        print(-1 if powers != goal else 0)
        return
    
    ai, bi, prev, cost, hi = 0, 0, 0, 0, powers[0]
    while ai < n and bi < m:
        if powers[ai] == goal[bi]:
            num = ai - prev
            if num == 0:
                pass
            elif k <= num:
                
                cost += min(y*num, x*(num//k) + y*(num%k))
            elif powers[ai] > hi:
                cost += y*num
            else:
                print(-1)
                return
            bi += 1
            hi = 0
            prev = ai + 1
        else:
            hi = max(hi, powers[ai])
        ai += 1
    
    if ai != n:
        hi = max(powers[ai:])
        num = n - ai
        if k <= num:
            cost += min(y*num, x*(num//k) + y*(num%k))
        elif powers[ai-1] > hi:
            cost += y*num
        else:
            print(-1)
            return

    print(cost if bi == m else -1)

solve()