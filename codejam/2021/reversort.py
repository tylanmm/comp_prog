def solve(lst):
    total = 0
    for i in range(len(lst)-1):
        j = min(range(i, len(lst)), key=lambda j: lst[j])
        total += j - i + 1
        lst[i:j+1] = lst[i:j+1][::-1]
    return total

for t in range(1, 1+int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(f'Case #{t}: {solve(l)}')