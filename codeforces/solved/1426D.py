n = int(input())
arr = map(int, input().split())

seen, total, count = {0}, 0, 0
for n in arr:
    total += n
    if total in seen:   # if I have been at this "height" before,
        count += 1      # then I have found a section that sums to 0
        total = n
        seen = {0}      # reset the set of "heights" that I have seen
    seen.add(total)
print(count)