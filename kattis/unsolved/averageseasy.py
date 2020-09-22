t = int(input())
input()

for _ in range(t):
    ncs, nec = map(int, input().split())
    students = []
    line = input()
    while line:
        students.extend(list(map(int, line.split())))
        line = input()

    cs = students[:ncs]
    ec = students[ncs:]
    csIQ, ecIQ = sum(cs)/ncs, sum(ec)/nec
    
    count = 0
    for stu in cs:
        if stu < csIQ and stu > ecIQ:
            count += 1
    print(count)