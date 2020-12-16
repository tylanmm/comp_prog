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

def is_valid(t):
    for val in t:
        inRange = False
        for r in rules:
            for lo, hi in rules[r]:
                if lo <= val and val <= hi:
                    inRange = True
        if not inRange:
            return False
    return True

valid_tickets = [ticket]
for t in others_raw.split('\n')[1:]:
    t = list(map(int, t.split(',')))
    if is_valid(t):
        valid_tickets.append(t)

def tickets_meet_rule(field, r, tickets):
    for t in tickets:
        works = False
        for lo, hi in rules[r]:
            if lo <= t[field] and t[field] <= hi:
                works = True
        if not works:
            return False
    return True

works = {i: [] for i in range(len(ticket))}
for i in range(len(ticket)):
    for r in rules:
        if tickets_meet_rule(i, r, valid_tickets):
            works[i].append(r)

seen = set()
assign = {}
total = 1
for field in sorted(works, key=lambda x: len(works[x])):
    new = (set(works[field]) - seen).pop()
    assign[field] = new
    if 'departure' in new:
        total *= ticket[field]
    seen.add(new)
print(total)