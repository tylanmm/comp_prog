for _ in range(int(input())):
    n = int(input())
    weights = list(map(int, input().split()))
    freq, used = {}, [False]*(n+1)
    for w in weights:
        if used[w]: freq[w] += 1
        else:       freq[w]  = 1
        used[w] = True
    
    possSums = set()
    for i in range(n-1):
        for j in range(i+1, n):
            possSums.add(weights[i] + weights[j])

    bestK = 0
    for s in possSums:
        k = 0
        for w in freq:
            if s-w > n:
                break
            if 0 < s-w and used[s-w]:
                k += min(freq[w], freq[s-w])
        bestK = max(bestK, k//2)
    
    print(bestK)