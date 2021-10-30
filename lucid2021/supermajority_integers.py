from collections import Counter
n = int(input())
freq = Counter([input() for _ in range(n)])
print(freq.most_common(1)[0][1]*3 > 2*n)