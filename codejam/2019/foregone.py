t = int(input())

def solve(N):
    A = ""
    B = ""
    for d in str(N):
        a = int(d) - 1
        b = 1
        if a < 0:
            A += "0"
            B += "0"
        else:
            while a == 4 or b == 4:
                a -= 1
                b += 1
            A += str(a)
            B += str(b)

    return (A, B)

for i in range(t):
    pair = solve(int(input()))
    print("Case #%d: %s %s" % (i + 1, pair[0], pair[1]))