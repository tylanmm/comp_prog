import sys

with open(sys.argv[1]) as f:
    lo, hi = map(int, f.readline().split('-'))

def isValid(num):
    hasDouble = False
    for i in range(1, len(num)):
        hasDouble |= num[i] == num[i-1]
        if num[i] < num[i-1]:
            return False
    return hasDouble

total = 0
for num in range(lo, hi+1):
    total += isValid(str(num))
print(total)