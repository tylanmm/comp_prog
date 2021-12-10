import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

score = 0
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
match = {'[':']', '(':')', '<':'>', '{':'}'}
for line in data:
    s = []
    for c in line:
        if c in match:
            s.append(c)
        elif not s or match[s[-1]] != c:
            score += points[c]
            break
        else:
            s.pop()
print(score)