n = int(input())
deck = list(map(int, input().split()))
end = n-1
for i in range(n-1, 0, -1):
    if deck[i] < deck[i-1]:
        end = i
        break
else:
    print('1 1')
    quit()

for i in range(n-1, end, -1):
    if deck[i] == deck[end]:
        end = i
        break

start = 0
for i in range(end):
    if deck[i] > deck[end]:
        start = i
        break

deck[start:end+1] = deck[start:end+1][::-1]
for i in range(1, n):
    if deck[i] < deck[i-1]:
        print('impossible')
        break
else:
    print(start+1, end+1)
