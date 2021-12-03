import sys
nums = sys.stdin.read().split()
oxy, co2 = set(nums), set(nums)
bit = 0
while len(oxy) > 1:
    subsets = [set(), set()]
    for num in oxy:
        subsets[int(num[bit])].add(num)
    oxy = subsets[len(subsets[0]) <= len(subsets[1])]
    bit += 1

bit = 0
while len(co2) > 1:
    subsets = [set(), set()]
    for num in co2:
        subsets[int(num[bit])].add(num)
    co2 = subsets[len(subsets[0]) > len(subsets[1])]
    bit += 1

print(int(oxy.pop(), 2) * int(co2.pop(), 2))