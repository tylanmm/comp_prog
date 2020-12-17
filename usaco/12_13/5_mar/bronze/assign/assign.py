# This is essentially a line-for-line translation of the Java solution
# It will only pass the first four test cases
# (the Java solution passes all of them)

with open('assign.in') as f:
    n, k = map(int, f.readline().split())
    rules = []
    for _ in range(k):
        rel, x, y = f.readline().split()
        rel = 1 if rel == 'S' else 0
        x, y = int(x) - 1, int(y) - 1
        rules.append((rel, x, y))

def is_valid(assignments):
    for rel, x, y in rules:
        if rel == 1:
            if assignments[x] != assignments[y]:
                return False
        else:
            if assignments[x] == assignments[y]:
                return False
    return True

def count_valid_assignments(assignments, pos):
    if pos == n:
        return is_valid(assignments)
    total = 0
    for i in range(3):
        assignments[pos] = i
        total += count_valid_assignments(assignments, pos+1)
    return total

with open('assign.out', 'w') as f:
    f.write(str(count_valid_assignments([0]*n, 0)) + '\n')