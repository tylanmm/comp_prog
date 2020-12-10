import sys

count = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        rule, password = line.split(': ')
        lo, hi = map(lambda x: int(x)-1, rule.split(' ')[0].split('-'))
        c = rule[-1]
        count += (password[lo] == c) ^ (password[hi] == c)
print(count)