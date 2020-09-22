sieve = [0]*14001
for i in range(2, 14001):
    if sieve[i]:
        continue
    for j in range(i, 14001, i):
        sieve[j] += 1

n = int(input())
nums = list(map(int, input().split()))
total = sum([sieve[n] for n in nums])
print(total)
def calc(i, total):
    if i == len(nums):
        return total
    hi = 0
    for j in range(i+1, len(nums)):
        n1, n2 = nums[i], nums[j]
        s1, s2 = sieve[n1], sieve[n2]
        if sieve[n1 + n2] >= s1 + s2:
            nums[j] += nums[i]
            hi = max(hi, calc(i+1, total - s1 - s2 + sieve[n1 + n2]))
            nums[j] -= nums[i]
    return max(hi, calc(i+1, total))

print(calc(0, total))