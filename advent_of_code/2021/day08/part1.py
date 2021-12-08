import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

ans = 0
for line in data:
    patterns, display = line.split(' | ')
    patterns = patterns.split(' ')
    display = display.split(' ')
    for digit in display:
        if len(digit) in [2, 3, 4, 7]:
            ans += 1
print(ans)