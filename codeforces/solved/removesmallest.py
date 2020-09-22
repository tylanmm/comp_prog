for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(set(map(int, input().split()))))
    print('YES' if nums == list(range(nums[0], nums[-1] + 1)) else 'NO')