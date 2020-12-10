import sys

with open(sys.argv[1]) as f:
    nums = list(map(int, f.readlines()))

seen = set()
for n in nums:
    if 2020 - n in seen:
        print(n * (2020 - n))
        break
    seen.add(n)