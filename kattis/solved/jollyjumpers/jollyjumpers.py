from sys import stdin

for line in stdin.readlines():
    line = line.split()
    n, nums = int(line[0]), list(map(int, line[1:]))
    gaps = [False]*n
    for i in range(n-1):
        gap = abs(nums[i] - nums[i+1])
        if gap >= n or gaps[gap]:
            print('Not jolly')
            break
        gaps[gap] = True
    else:
        print('Jolly')