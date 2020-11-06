n = int(input())
res = n-1
for i in range(1, n-1):
    res *= i
print(res // (n//2))