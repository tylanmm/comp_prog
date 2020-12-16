from collections import Counter
import string

with open('blocks.in') as f:
    n = int(f.readline())
    words = [f.readline().split() for _ in range(n)]

total = Counter({c: 0 for c in string.ascii_lowercase})
for w1, w2 in words:
    total.update(Counter(w1) | Counter(w2))

with open('blocks.out', 'w') as f:
    for c in string.ascii_lowercase:
        f.write(str(total[c]) + '\n')