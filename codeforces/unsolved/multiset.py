def binSearch(n, nums):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == n:
            return mid
        if nums[mid] < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

from collections import deque

input()
a = deque(map(int, input().split()))
for q in map(int, input().split()):
    if q < 0:
        a.rotate(q+1)
        a.popleft()
        a.rotate(-q-1)
    else:
        i = binSearch(q, a)
        a.rotate(-i)
        a.appendleft(q)
        a.rotate(i)
print(a.popleft() if a else 0)