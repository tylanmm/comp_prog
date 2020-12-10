import sys

with open(sys.argv[1]) as f:
    lo, hi = map(int, f.readline().split('-'))

def isValid(num):
    group = [0]*6
    for i in range(1, len(num)):
        if num[i] == num[i-1]:
            if group[i-1]:
                group[i-2] = group[i-1] = group[i] = 2
            else:
                group[i-1] = group[i] = 1
        if num[i] < num[i-1]:
            return False
    return group.count(1) > 0

total = 0
for num in range(lo, hi+1):
    total += isValid(str(num))
print(total)