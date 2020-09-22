n = int(input())
A = list(map(int, input().split()))
total, nums = 0, {}
for n in A:
    total += n
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 1

for _ in range(int(input())):
    b, c = map(int, input().split())
    amt = 0
    if b in nums:
        amt = nums.pop(b)
        total -= amt * b
    
    if c in nums:
        nums[c] += amt
    else:
        nums[c] = amt
    total += amt * c
    print(total)