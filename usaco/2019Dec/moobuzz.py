with open('moobuzz.in') as f:
    n = int(f.read().strip())

nums = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8]

with open('moobuzz.out', 'w') as f:
    f.write(str((n // 15) * 8 + nums[n % 15]) + '\n')