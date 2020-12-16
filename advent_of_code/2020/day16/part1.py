import sys

with open(sys.argv[1]) as f:
    rules_raw, ticket_raw, others_raw = f.read().split('\n\n')

rules = {}
rules_raw = rules_raw.split('\n')
for i in range(len(rules_raw)):
    r = rules_raw[i].split(': ')
    rules[r[0]] = []
    for rang in r[1].split(' or '):
        rules[r[0]].append(tuple(map(int, rang.split('-'))))

ticket = list(map(int, ticket_raw.split('\n')[1].split(',')))

total_error = 0
for t in others_raw.split('\n')[1:]:
    t = list(map(int, t.split(',')))
    error = 0
    for val in t:
        inRange = False
        for r in rules:
            for lo, hi in rules[r]:
                if lo <= val and val <= hi:
                    inRange = True
        if not inRange:
            error += val
    total_error += error
print(total_error)