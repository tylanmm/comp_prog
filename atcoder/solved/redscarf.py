n = int(input())
cats = list(map(int, input().split()))
key = cats[0]
for c in cats[1:]:
    key ^= c

res = []
for c in cats:
    res.append(str(c ^ key))
print(' '.join(res))