import sys
from collections import Counter

poly, _ = input(), input()
rules = {}
for line in sys.stdin.readlines():
    a, b = line.strip().split(' -> ')
    rules[a[0], a[1]] = b

for step in range(10):
    curr = []
    for i in range(len(poly)-1):
        curr.append(poly[i])
        if (poly[i], poly[i+1]) in rules:
            curr.append(rules[poly[i], poly[i+1]])
    curr.append(poly[-1])
    poly = curr

freq = Counter(poly).most_common()
print(freq[0][1] - freq[-1][1])