n, a = int(input()), list(map(int, input().split()))
b = [str(a[-1] + 1)] * n
for i in range(n-1, -1, -1):
    if a[i]-1 > i:
        print(-1)
        break
    
    
else:
    print(' '.join(b))