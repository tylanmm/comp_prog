with open('moobuzz.in') as f:
    n = int(f.readline())

nums = [14, 1, 2, 4, 7, 8, 11, 13]

# every 15, we will have said 8 numbers
# find number of times we have completely counted 15
# offset that amount by the remainder
with open('moobuzz.out', 'w') as f:
    f.write(str(15 * ((n - 1) // 8) + nums[n % 8]) + '\n')