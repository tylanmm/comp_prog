for _ in range(int(input())):
    n = int(input())
    numC = list(map(int, input().split()))
    numO = list(map(int, input().split()))
    minC, minO = min(numC), min(numO)

    total = 0
    for i in range(n):
        total += max(numC[i] - minC, numO[i] - minO)
    
    print(total)