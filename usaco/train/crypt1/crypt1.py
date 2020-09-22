"""
ID: tylan071
LANG: PYTHON3
TASK: crypt1
"""

with open('crypt1.in') as f:
    n = int(f.readline())
    digits = list(map(int, f.readline().split()))

nums = [False] * 10000
for d1 in digits:
    for d2 in digits:
        nums[d2*10 + d1] = True
        for d3 in digits:
            nums[d3*100 + d2*10 + d1] = True
            for d4 in digits:
                nums[d4*1000 + d3*100 + d2*10 + d1] = True

count = 0
for i in range(111, 1000):
    for j in range(11, 100):
        if nums[i] and nums[j]:
            pp1, pp2 = i * (j%10), i * (j//10)
            if pp1 < 1000 and nums[pp1] and pp2 < 1000 and nums[pp2] and i*j < 10000 and nums[i*j]:
                count += 1

with open('crypt1.out', 'w') as f:
    f.write(f'{count}\n')