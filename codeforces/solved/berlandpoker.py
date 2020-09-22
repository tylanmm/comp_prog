for _ in range(int(input())):
    n, m, k = map(int, input().split())
    cards = n//k
    if m <= cards:
        print(m)
    else:
        print(cards - ((1 if ((m-cards)%(k-1)) else 0) + (m - cards) // (k - 1)))