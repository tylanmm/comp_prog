for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if nums[i] == i+1:
            count += 1
    print(0 if count == 0 else 1 if count == 1 else 2)