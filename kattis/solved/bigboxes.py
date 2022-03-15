def test(x, k, weights):
    curr = 0
    for w in weights:
        if w > x:
            return False
        if curr + w <= x:
            curr += w
        else:
            curr = w
            k -= 1
    return k > 0

n, k = map(int, input().split())
weights = list(map(int, input().split()))
lo, hi = 1, sum(weights)
while lo < hi:
    x = (lo + hi) // 2
    if test(x, k, weights):
        hi = x
    else:
        lo = x + 1
print(lo)