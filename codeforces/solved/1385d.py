def solve(n, s, c):
    if n == 1:
        return 1 if s[0] != c else 0
    half1 = (n//2 - s[:n//2].count(c)) + solve(n//2, s[n//2:], c+1)
    half2 = (n//2 - s[n//2:].count(c)) + solve(n//2, s[:n//2], c+1)
    return min(half1, half2)

# read input, change chars to ints
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    for i in range(n):
        s[i] = ord(s[i])
    print(solve(n, s, 97))