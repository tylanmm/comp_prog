def test(s, k):
    curr = s[:k]
    for i in range(k, len(s), k):
        curr = curr[-1] + curr[:-1]
        if s[i:i+k] != curr:
            return False
    return True


s = input()
for k in range(1, len(s)+1):
    if len(s) % k == 0 and test(s, k):
        print(k)
        break
