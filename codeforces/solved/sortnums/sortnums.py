with open('sortnums.in') as f:
    n = int(f.readline())
    nums = sorted(list(map(int, f.readline().split())))

with open('sortnums.out', 'w') as f:
    f.write(' '.join(map(str, nums)))