def solve(w):
    left = []
    right = []
    curr = 1
    while w:
        digit = w % 3
        w //= 3
        if digit == 1:
            right.append(curr)
        elif digit == 2:
            left.append(curr)
            w += 1        
        curr *= 3
    
    print('left pan:', *left[::-1])
    print('right pan:', *right[::-1])
    print()

for _ in range(int(input())):
    solve(int(input()))

# 243 81 27 9 3 1
# 21 = 210
# 250 = 100021