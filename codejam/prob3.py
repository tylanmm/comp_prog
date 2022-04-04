def solve(sides):
    sides.sort()
    ans = 0
    for s in sides:
        if s > ans:
            ans += 1
    return ans


for t in range(int(input())):
    n = int(input())
    sides = list(map(int, input().split()))
    print('Case #{}: {}'.format(t+1, solve(sides)))
