n, c = map(int, input().split())
w = list(map(int, input().split()))
w.append(float('inf'))

arr = [0]*(n+2)

s, e = 0, -1
total = 0
while s < n:
    if e >= n or total + w[e+1] > c:
        total -= w[s]
        s += 1
    else:
        e += 1
        total += w[e]
    arr[s] += 1
    arr[e+1] -= 1


for i in range(1, n):
    arr[i] += arr[i-1]

print('\n'.join(map(str, arr[:-2])))
