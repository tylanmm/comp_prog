import sys

with open(sys.argv[1]) as f:
    nums = [int(n) for n in f.read().split('\n')]

def isValid(num, pre):
    for i in pre:
        for j in pre:
            if i != j and i + j == num:
                return True
    return False

preamble = 5
badI = 0
for i in range(preamble, len(nums)):
    if not isValid(nums[i], nums[i-preamble:i]):
        badI = i
        break

sums = [0]*badI
sums[0] = nums[0]
for i in range(1, badI):
    sums[i] += sums[i-1] + nums[i]

def solve():
    for i in range(badI-1):
        for j in range(i+1, badI):
            if sums[j] - (sums[i-1] if i else 0) == nums[badI]:
                return i, j

i, j = solve()
print(max(nums[i:j+1]) + min(nums[i:j+1]))