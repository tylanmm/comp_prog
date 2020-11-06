pad = [[0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 5, 6, 8, 9], [3, 6, 9], [0, 4, 5, 6, 7, 8, 9], [0, 5, 6, 8, 9], [6, 9], [0, 7, 8, 9], [0, 8, 9], [9]]
poss = set()

def find(curr, d):
    if d == 0 or curr > 200:
        return
    poss.add(curr)
    for n in pad[curr%10]:
        find(curr*10 + n, d-1)

for i in range(10):
    find(i, 3)

def findNearest(k):
    closest = 1
    for num in poss:
        num = int(num)
        if abs(k - num) < abs(k - closest):
            closest = num
    return closest

for _ in range(int(input())):
    k = int(input())
    print(findNearest(k))