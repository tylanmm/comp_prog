p, q = map(int, input().split())
if p == 1:
    print(1 if q % 2 else 2)
elif q == 1:
    print(1 if p % 2 else 0)
else:
    print(0)