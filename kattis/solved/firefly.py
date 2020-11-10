n, h = map(int, input().split())
num = [0]*(h+1)
num[0] = n//2
num[-1] = -n//2
for _ in range(n//2):
    lo = int(input())
    num[lo] -= 1

    hi = int(input())
    num[h-hi] += 1

lo = num[0]
amt = 1
for i in range(1, h):
    num[i] += num[i-1]
    if num[i] < lo:
        lo = num[i]
        amt = 1
    elif num[i] == lo:
        amt += 1

print(lo, amt)

'''
 | | |
 | |
 | ||
 |  |
 || |
  | |
| | |
'''