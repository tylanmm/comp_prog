import sys

with open(sys.argv[1]) as f:
    nums = list(map(int, f.readlines()))

def solve(nums):
    seen = {}
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j: continue
            val = nums[i] + nums[j]
            if val not in seen:
                seen[val] = set()
            seen[val].add((i, j))

    for k in range(len(nums)):
        if 2020 - nums[k] in seen:
            for i, j in seen[2020-nums[k]]:
                if i != k and j != k:
                    return nums[i] * nums[j] * nums[k]

print(solve(nums))