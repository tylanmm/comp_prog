n, k = map(int, input().split())
ids = list(map(int, input().split()))
row = 1
while k - row > 0:
    k -= row
    row += 1
print(ids[k-1])