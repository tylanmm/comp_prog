def genString(s1, s2, n, a, b, c, d):
    x = [ord(s1), ord(s2)]
    out = [s1, s2]
    for i in range(2, n):
        xi = (a*x[-1] + b*x[-2] + c) % d
        x.append(xi)
        out.append(chr(97 + (xi % 26)))
    return "".join(out)

for i in range(int(input())):
    l = int(input())
    dict = input().split()
    s1, s2, n, a, b, c, d = tuple(input().split())
    n = int(n)
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    print(genString(s1, s2, n, a, b, c, d))