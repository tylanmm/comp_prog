import sys

with open(sys.argv[1]) as f:
    nums = [int(n) for n in f.read().split('\n')]

def isValid(num, pre):
    for i in pre:
        for j in pre:
            if i != j and i + j == num:
                return True
    return False

for i in range(25, len(nums)):
    if not isValid(nums[i], nums[i-25:i]):
        print(nums[i])
        break