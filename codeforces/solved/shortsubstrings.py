for _ in range(int(input())):
    b = input()
    a = [b[0]]
    for i in range(1, len(b)-1, 2):
        a.append(b[i])
    a.append(b[-1])
    print(''.join(a))