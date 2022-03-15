n = int(input())
p = sorted(list(map(int, input().split())))
total = 0
for reg in p[:len(p)//2+1]:
    total += reg // 2
print(total + sum(p[len(p)//2+1:]))
