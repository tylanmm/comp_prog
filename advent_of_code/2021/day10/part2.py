import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

scores = []
points = {')': 1, ']': 2, '}': 3, '>': 4}
match = {'[':']', '(':')', '<':'>', '{':'}'}
for line in data:
    s = []
    incomplete = True
    for c in line:
        if c in match:
            s.append(c)
        elif not s or match[s[-1]] != c:
            incomplete = False
            break
        else:
            s.pop()
    
    if incomplete:
        total = 0
        while s:
            total = total * 5 + points[match[s.pop()]]
        scores.append(total)

print(sorted(scores)[len(scores)//2])