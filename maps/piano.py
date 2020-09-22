n, m = tuple(map(int, input().split()))
taken = [False] * m
times = {i: [] for i in range(1, n+1)}

for i in range(n):
    stu = list(map(int, input().split()))
    
    for j in range(1, stu[0] + 1):
        times[stu[j]].append(i)

print(taken)
print(times)