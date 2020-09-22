def solve(k, nums):
    pitches = [0] * k
    lo = hi = breaks = 0
    for i in range(1, k):
        if nums[i] > nums[i-1]:
            pitches[i] = pitches[i-1] + 1
        elif nums[i] < nums[i-1]:
            pitches[i] = pitches[i-1] - 1
        else:
            pitches[i] = pitches[i-1]
        
        lo = min(lo, pitches[i])
        hi = max(hi, pitches[i])
        if hi - lo >= 4:
            breaks += 1
            lo = hi = pitches[i] = 0
    return breaks


for t in range(int(input())):
    k = int(input())
    pitches = list(map(int, input().split()))
    print('Case #%d: %d' % (t+1, solve(k, pitches)))