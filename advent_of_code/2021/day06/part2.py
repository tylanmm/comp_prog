from collections import Counter

curr = Counter(map(int, input().split(',')))
for _ in range(256):
    prev, curr = curr, Counter()
    for day in range(1, 9):
        curr[day-1] = prev[day]
    curr[8] = prev[0]
    curr[6] += prev[0]
print(sum(curr.values()))