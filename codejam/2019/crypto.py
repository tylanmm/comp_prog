from string import ascii_uppercase as abc

t = int(input())

def gcf(n1, n2):
    while n1 > 1 and n2 > 1:
        n = n1 - n2
        if n == 0:
            return n2
        n1 = max(n, n2)
        n2 = min(n, n2)
    return 1

def solve(nums):
    primes = []
    factor = gcf(max(nums[0], nums[1]), min(nums[0], nums[1]))
    primes.append(int(nums[0] / factor))
    for i in range(0, len(nums)):
        primes.append(int(nums[i] / primes[i]))
    forAbc = sorted(list(set(primes.copy())))
    key = {forAbc[i]: abc[i] for i in range(26)}
    out = ""
    for p in primes:
        out += key[p]
    return out

for i in range(t):
    n, l = tuple(map(int, input().split()))
    line = list(map(int, input().split()))
    print("Case #%d: %s" % (i + 1, solve(line)))