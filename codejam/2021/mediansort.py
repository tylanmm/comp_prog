def connect(mid, l, r, lstL, lstR):
    lstL[r] = mid
    lstR[l] = mid
    lstL[mid] = l
    lstR[mid] = r

def construct(lst, s):
    res = []
    while s:
        res.append(s)
        s = lst[s]
    return ' '.join(map(str, res))

def runcase(n, q):
    left  = list(range(-1, n))
    right = list(range(1, n+2))
    left[0] = right[0] = right[-1] = 0

    for i in range(2, n):
        print(i-1, i, i+1)
        mid = int(input())
        if mid == i:
            if right[i-1] == i+1:
                connect(mid, i-1, i+1, left, right)
            else:
                connect(mid, i+1, i-1, left, right)
        elif mid == i-1:
            if right[i] == i+1:
                connect(mid, i, i+1, left, right)
            else:
                connect(mid, i+1, i, left, right)
        else:
            if right[i-1] == i:
                connect(mid, i-1, i, left, right)
            else:
                connect(mid, i, i-1, left, right)
    
    print(left)
    print(right)
    for i in range(1, n+1):
        if left[i] == 0:
            return construct(right, i)

t, n, q = map(int, input().split())
for _ in range(t):
    print(f'{runcase(n, q//t)}')
    if input() == '-1': break