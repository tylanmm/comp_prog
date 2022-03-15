n = int(input())
gas = sorted(list(map(int, input().split())))
lo = 1
for i in range(n, 0, -1):
    if i >= gas[i-1]:
        lo = min(lo, gas[i-1] / i)
    else:
        print('impossible')
        quit()
print(lo)