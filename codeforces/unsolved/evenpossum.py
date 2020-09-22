for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n <= 2:
        print(max(a))
        continue
    
    for i in range(2, n):
        a[i] += a[i-2]
    