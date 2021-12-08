import sys

with open(sys.argv[1]) as f:
    data = f.read().split('\n')

size = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def find(target, filter, filteredSize, patterns):
    for digit in patterns:
        if len(digit) != size[target]: continue
        segments = set(digit)
        if len(segments & filter) == filteredSize:
            return digit

def update(num, pattern, conversion, sets, rem):
    key = ''.join(sorted(pattern))
    conversion[key] = num
    sets[num] = set(pattern)
    rem.remove(pat)

# (target, set to filter by, size of filtered set)
order = [(8, 8, 7), (1, 8, 2), (4, 8, 4), (7, 8, 3), (9, 4, 4), (3, 1, 2), (0, 1, 2), (6, 0, 5), (2, 6, 4), (5, 6, 5)]
total = 0

for line in data:
    # parse line
    patterns, display = line.split(' | ')
    patterns = set(patterns.split(' '))
    display = display.split(' ')

    # set up trackers for current display
    toDigit = {'abcdefg': 8}
    toSet = {8: set('abcdefg')}

    # use set logical ordering to determine mappings
    for target, filter, filteredSize in order:
        pat = find(target, toSet[filter], filteredSize, patterns)
        update(target, pat, toDigit, toSet, patterns)
    
    # convert display
    dis = []
    for digit in display:
        dis.append(toDigit[''.join(sorted(digit))])
    num = int(''.join(map(str, dis)))
    total += num

print(total)