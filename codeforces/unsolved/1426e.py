n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# max(wins) = sum(a) - min(loss) - min(tie)
maxWins = 0
for i in range(3):
    maxWins += min(a[i], b[(i+1)%3])

# loop through b in descending order, prioritize A's losses and then ties
for amt, i in sorted([(b[i], i) for i in range(3)], reverse=True):
    loss = min(a[(i+1)%3], b[i])
    a[(i+1)%3] -= loss
    b[i] -= loss  

    ties = min(a[i], b[i])
    a[i] -= ties
    b[i] -= ties

print(sum(a), maxWins)