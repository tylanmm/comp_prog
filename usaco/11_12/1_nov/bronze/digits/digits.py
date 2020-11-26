with open('digits.in') as f:
    b2 = f.readline().strip()
    b3 = f.readline().strip()

def solve(b2, b3):
    for i in range(len(b2)):
        num1 = int(b2[:i] + ('1' if b2[i] == '0' else '0') + b2[i+1:], 2)
        for j in range(len(b3)):
            num2 = int(b3[:j] + str((int(b3[j]) + 1) % 3) + b3[j+1:], 3)
            num3 = int(b3[:j] + str((int(b3[j]) + 2) % 3) + b3[j+1:], 3)
            if num1 == num2 or num1 == num3:
                return num1

with open('digits.out', 'w') as f:
    f.write(str(solve(b2, b3)) + '\n')