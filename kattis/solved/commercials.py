n, p = map(int, input().split())
students = [int(num)-p for num in input().split()]
hi, length, curr, currLength = 0, 0, -float('inf'), 0

for s in students:
    if s > curr+s:
        curr = 0
        currLength = 0
    curr += s
    currLength += 1
    
    if curr > hi:
        hi = curr
        length = currLength

print(hi)