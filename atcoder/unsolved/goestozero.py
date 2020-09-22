N = int(input())
X = input()
n = X.count('1')

for i in range(N):
    on = n + (1 if X[i] == '1' else -1)
    x = X[:i] + ('0' if X[i] == '1' else '1') + X[i+1:]
    c = 0
    while on:
        count = 0
        while (1 << count) < on:
            count += 1
        x = x[-count:]
        on = x.count('1')
        c += 1
    print(c)