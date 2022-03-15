cups = []
for _ in range(int(input())):
    a, b = input().split()
    if a.isalpha():
        cups.append((int(b)*2, a))
    else:
        cups.append((int(a), b))
print('\n'.join([c for r, c in sorted(cups)]))
