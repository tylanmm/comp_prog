import sys

count = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        rule, password = line.split(': ')
        lo, hi = map(int, rule.split(' ')[0].split('-'))
        c = rule[-1]
        amt = password.count(c)
        count += lo <= amt and amt <= hi
print(count)