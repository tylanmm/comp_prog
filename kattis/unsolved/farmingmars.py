from collections import Counter
from math import floor

n, m = map(int, input().split())
ph = [input() for _ in range(n)]
prefix = [Counter()]
freq = Counter()
for p in ph:
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1
    prefix.append(Counter(freq))

for _ in range(m):
    l, r = map(int, input().split())
    prefix[r].subtract(prefix[l-1])
    if prefix[r].most_common(1)[0][1] >= floor((r - l + 1)/2)+1:
        print('usable')
    else:
        print('unusable')
    prefix[r].update(prefix[l-1])