def solve(n, c, m, henchmen):
    pass

for _ in range(int(input())):
    n, c, m = map(int, input().split())
    henchmen = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, c, m, henchmen))