N = int(input())
T = [int(input()) for _ in range(N)]

left = [1]*N
right = [1]*N
for i in range(1, N):
    left[i] = left[i-1] * T[i-1]
    right[-i-1] = right[-i] * T[-i]

res = 0
for l in range(N-1):
    pass
