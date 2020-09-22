for t in range(int(input())):
    n, m, x, y = map(int, input().split())
    cost = 0
    for _ in range(n):
        row = input().split('*')
        for stretch in row:
            if x*2 <= y:
                cost += len(stretch)*x
            else:
                cost += (len(stretch)//2) * y + (x if len(stretch) % 2 else 0)

    print(cost)