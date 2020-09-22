def solve(k):
    print(press('', 1, k))

nextNum = [[], [2, 4], [3, 5], [6], [5, 7], [6, 8], [9], [8], [9, 0], []]
def press(num, digit, k):
    if len(num) == len(str(k)):
        return int(num)
    
    best = press(num + str(digit), digit, k)
    for d in nextNum[digit]:
        n = press(num, d, k)
        if abs(k - n) < abs(k - best):
            best = n
    return best

for _ in range(int(input())):
    solve(int(input()))