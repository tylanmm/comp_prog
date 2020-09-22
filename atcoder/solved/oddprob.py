N = int(input())
squares = list(map(int, input().split()))
count = 0
for i in range(N):
    if (i+1) % 2 and squares[i] % 2:
        count += 1
print(count)