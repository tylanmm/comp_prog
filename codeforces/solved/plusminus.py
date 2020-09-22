for _ in range(int(input())):
    lo = curr = res = 0
    s = input()
    for i in range(len(s)):
        curr += 1 if s[i] == '+' else -1
        if curr < lo:
            res += i + 1
            lo = curr
    print(res + len(s))