from fractions import Fraction

n = int(input())
coef = list(map(int, input().split()))
x = Fraction(coef[-1], 1)
for c in coef[::-1][1:]:
    x = Fraction(c, 1) + Fraction(1, x)
print(x)