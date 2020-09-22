def count(num):
    rep = '{:b}'.format(num)
    return len(rep) - rep.count('0')

def getNonZeros(num):
    num = num[::-1]
    for i in range(len(num)):
        if num[i] != '0':
            print(i, end=" ")

'''
for _ in range(int(input())):
    n = int(input())
    foundCopy = False
    i = 1
    counts = {}
    while not foundCopy:
        c = count(i * n)
        if c not in counts:
            counts[c] ='{:b}'.format(n)
        else:
            getNonZeros(counts[c])
            print()
            break
        i += 1
'''

for i in range(1, 20):
    print('%d: %d, %s' % (i, count(i*42), '{:b}'.format(i*42)))