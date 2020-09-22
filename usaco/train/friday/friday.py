"""
ID: tylan071
LANG: PYTHON3
TASK: friday
"""

with open('friday.in') as f:
    n = int(f.readline().strip())

year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = 2
thirteens = [0] * 7

for i in range(n):
    # Change number of days in February
    yearCount = i + 1900
    if yearCount % 4 == 0 and yearCount % 100 != 0:
        year[1] = 29
    elif yearCount % 400 == 0:
        year[1] = 29
    else:
        year[1] = 28
    
    for month in year:
        for day in range(month):
            if day == 12:
                thirteens[dow] += 1
            dow += 1
            dow %= 7

with open('friday.out', 'w') as f:
    for i in range(6):
        f.write(str(thirteens[i]) + ' ')
    f.write(str(thirteens[6]) + '\n')