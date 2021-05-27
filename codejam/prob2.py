def solve(freq):
    score = 0

    return score

for t in range(int(input())):
    m = int(input())
    freq = {}
    for _ in range(m):
        p, n = map(int, input().split())
        freq[p] = n
    print(f'Case #{t+1}: {solve(freq)}')