with open(__file__[:-2] + 'in', 'r') as f:
    n, t = map(int, f.readline().split())
    state = f.readline().strip()
    log = [tuple(map(int, f.readline().split())) for _ in range(t)]



with open(__file__[:-2] + 'out', 'w') as f:
    pass