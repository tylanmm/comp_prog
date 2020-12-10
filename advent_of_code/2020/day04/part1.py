import sys

with open(sys.argv[1]) as f:
    raw = f.read().split('\n\n')

count = 0
for passport in raw:
    data = passport.split()
    have = set()
    for d in data:
        have.add(d.split(':')[0])
    count += len(have) == 8 or (len(have) == 7 and 'cid' not in have)
print(count)