import sys
from collections import Counter

# count the number of occurences of each pair of letters
poly, _ = input(), input()
pairs = Counter()
for i in range(len(poly)-1):
    pairs[poly[i], poly[i+1]] += 1

# read in the rules
rules = {}
for line in sys.stdin.readlines():
    a, b = line.strip().split(' -> ')
    rules[a[0], a[1]] = b

# simulate
for step in range(40):
    curr = Counter()
    for a, b in pairs.keys():
        if (a, b) in rules:
            curr[a, rules[a, b]] += pairs[a, b]
            curr[rules[a, b], b] += pairs[a, b]
    pairs = curr

# count occurrences of each individual letter
amount = Counter()
for a, b in pairs.keys():
    amount[a] += pairs[a, b]
    amount[b] += pairs[a, b]

# everything (except for the first and last letter) was double counted
for k in amount:
    amount[k] += poly[0] == k or poly[-1] == k
    amount[k] //= 2

freq = amount.most_common()
print(freq[0][1] - freq[-1][1])