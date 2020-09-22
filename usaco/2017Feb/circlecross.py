with open('circlecross.in') as f:
    cows = f.read().strip()

count = 0
s = []
seen = set()
for c in cows:
    if c not in seen:
        s.append(c)
        seen.add(c)
    else:
        while s and s[-1] != c:
            s.pop()
            count += 1
        if s and s[-1] == c:
            s.pop()
        else:
            s.append(c)
            count += 1
print(count + len(s))