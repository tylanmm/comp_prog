def solve(upper):
    letters = {}
    numbers = {i:set() for i in range(10)}
    out = [''] * 10
    for i in range(10**4):
        q, r = input().split()
        for c in r:
            if c not in letters:
                letters[c] = set()
        letters[r[0]].add(0)
        numbers[0].add(r[0])

        if q != '-1' and len(q) == len(r):
            for i in range(int(q[0]) + 1, 10):
                letters[r[0]].add(i)
                numbers[i].add(r[0])

        if len(letters[r[0]]) == 9:
            num = set(range(10)).difference(letters[r[0]]).pop()
            if out[num] == '':
                out[num] = r[0]
                for i in numbers:
                    if i != num:
                        numbers[i].add(r[0])
                for l in letters:
                    if l != r[0]:
                        letters[l].add(num)

    out[0] = set(letters.keys()).difference(numbers[0]).pop()
    return ''.join(out)


for i in range(int(input())):
    upper = 10**int(input()) - 1
    print('Case #%d: %s' % (i+1, solve(upper)))