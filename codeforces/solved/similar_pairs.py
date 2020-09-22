def solve(nums):
    parity = [[], []]
    for n in nums:
        parity[n%2].append(n)
    if len(parity[0]) % 2 == 0:
        return 'YES'
    
    for n in parity[0]:
        if n+1 in parity[1] or n-1 in parity[1]:
            return 'YES'
    return 'NO'

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))