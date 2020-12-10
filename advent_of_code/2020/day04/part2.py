import sys, re

with open(sys.argv[1]) as f:
    raw = f.read().split('\n\n')

def isValid(data):
    eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if 1920 <= int(data['byr']) <= 2002:
        if 2010 <= int(data['iyr']) <= 2020:
            if 2020 <= int(data['eyr']) <= 2030:
                if (('cm' in data['hgt']) and (150 <= int(data['hgt'][:-2]) <= 193)) or (('in' in data['hgt']) and (59 <= int(data['hgt'][:-2]) <= 76)):
                    if data['hcl'][0] == '#' and int(data['hcl'][1:7], 16) > -1:
                        if data['ecl'] in eye_colors:
                            if len(data['pid']) == 9 and int(data['pid']) < 1e9:
                                return True
    return False


count = 0
for passport in raw:
    info = passport.split()
    data = {}
    for d in info:
        d = d.split(':')
        data[d[0]] = d[1]
    
    try:
        count += isValid(data)
    except Exception:
        continue

print(count)