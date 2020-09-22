line = input()
while line != '0 0':
    n, t = line.split()
    n, t = int(n), float(t)

    pR = (1 + t + t*t) / 2

    exp, prize, p = 0, 1, 1
    for i in range(n):
        if prize * 2 * 
        exp += p * prize
        prize *= 2
        p *= pR
    print(exp + p * prize)

    line = input()