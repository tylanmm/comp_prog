"""
ID: tylan071
LANG: PYTHON3
TASK: hamming
"""

with open('hamming.in') as f:
    n, b, d = map(int, f.readline().split())

isValid = [False] * (2**(b+1))
for i in range(2**(b+1)):
    count, num = 0, i
    while num:
        count += 1
        num -= num & -num
    isValid[i] = count >= d

codes = [0]
num = 1
while len(codes) < n:
    for c in codes:
        if not isValid[c ^ num]:
            break
    else:
        codes.append(num)
    num += 1

with open('hamming.out', 'w') as f:
    for i in range(0, len(codes), 10):
        f.write(' '.join(map(str, codes[i:min(i+10, len(codes))])) + '\n')