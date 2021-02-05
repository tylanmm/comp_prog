def sod(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

nums = [1]
for _ in range(100):
    nums.append(nums[-1] + sod(nums[-1]))
print(nums)

prefs = [nums[0]]
for n in nums[1:]:
    prefs.append(prefs[-1] + n)
for i in range(len(prefs)):
    print(i+1, ':', prefs[i])