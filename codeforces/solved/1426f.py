mod = int(1e9 + 7)

n, s = int(input()), input()
seen = {'a': 0, 'ab': 0, 'abc': 0, '': 1}
for c in s:
    if c == 'a':
        seen['a'] = (seen['a'] + seen['']) % mod
    elif c == 'b':
        seen['ab'] = (seen['ab'] + seen['a']) % mod
    elif c == 'c':
        seen['abc'] = (seen['abc'] + seen['ab']) % mod
    else:
        seen['abc'] = (seen['ab'] + 3*seen['abc']) % mod
        seen['ab'] = (seen['a'] + 3*seen['ab']) % mod
        seen['a'] = (seen[''] + 3*seen['a']) % mod
        seen[''] = (seen[''] * 3) % mod

print(seen['abc'])