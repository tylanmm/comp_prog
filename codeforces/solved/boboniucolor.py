for _ in range(int(input())):
    r, g, b, w = map(int, input().split())
    n = r + g + b + w
    parity = [0, 0]
    parity[r % 2] += 1
    parity[g % 2] += 1
    parity[b % 2] += 1
    parity[w % 2] += 1
    if r == 0 or g == 0 or b == 0:
        if n % 2 == 0:
            print('Yes' if parity[0] == 4 else 'No')
        else:
            print('Yes' if parity[0] == 3 else 'No')
    else:
        if n % 2 == 0:
            print('Yes' if parity[0] == 0 or parity[0] == 4 else 'No')
        else:
            print('Yes' if parity[0] == 3 or parity[0] == 1 else 'No')