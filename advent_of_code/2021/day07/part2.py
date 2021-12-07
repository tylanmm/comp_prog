nums = list(map(int, input().split(',')))
crabs = [0]*(max(nums)+1)
for c in nums:
    crabs[c] += 1

best = float('inf')
for x in range(len(crabs)):
    cost = 0
    for i in range(len(crabs)):
        d = abs(x - i)
        cost += crabs[i] * d * (d + 1) // 2
    best = min(best, cost)
print(best)