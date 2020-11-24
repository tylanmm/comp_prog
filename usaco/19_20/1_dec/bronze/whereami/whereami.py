with open('whereami.in') as f:
    n = int(f.readline())
    road = f.readline()

ans = n
for i in range(1, n+1):
    seen = set()
    for j in range(n-i+1):
        section = road[j:j+i]
        if section in seen:
            break
        else:
            seen.add(section)
    else:
        ans = i
        break

with open('whereami.out', 'w') as f:
    f.write(str(ans) + '\n')