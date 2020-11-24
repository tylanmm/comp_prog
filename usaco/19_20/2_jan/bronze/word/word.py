with open('word.in') as f:
    n, k = map(int, f.readline().split())
    words = f.readline().split()

out = ''
pos = 0
for w in words:
    if pos + len(w) <= k:
        if pos > 0:
            out += ' '
        out += w
        pos += len(w)
    else:
        out += '\n' + w
        pos = len(w)

with open('word.out', 'w+') as f:
    f.write(out + '\n')