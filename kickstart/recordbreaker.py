def solve(n, nums):
    hi, count = -1, 0
    for i in range(n-1):
        if nums[i] > hi and nums[i] > nums[i+1]:
            count += 1
        hi = max(hi, nums[i])
    if nums[-1] > hi:
        count += 1
    return count

for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    print('Case #%d: %d' % (t+1, solve(n, nums)))