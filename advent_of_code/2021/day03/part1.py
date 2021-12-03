import sys
nums = sys.stdin.read().split()
gam = eps = 0
for i in range(len(nums[0])):
    bit = 0
    for j in range(len(nums)):
        bit += 1 if nums[j][i] == '1' else -1
    gam = gam*2 + (bit > 0)
    eps = eps*2 + (bit < 0)
print(gam * eps)