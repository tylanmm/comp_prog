from sys import stdin

for line in stdin:
    n, *line = list(map(int, line.split()))
    seen = [False]*n
    for i in range(1, n):
        diff = abs(line[i] - line[i-1])
        if diff == 0 or diff > n-1 or seen[diff]:
            print('Not jolly')
            break
        seen[diff] = True
    else:
        print('Jolly')