from fractions import Fraction
from math import floor


def con_to_rat(con, i):
    if i == len(con) - 1:
        return Fraction(con[i], 1)
    return Fraction(con[i], 1) + Fraction(1, con_to_rat(con, i+1))


def rat_to_con(rat):
    con = []
    while rat:
        whole = floor(rat)
        con.append(whole)
        rat -= whole
        if rat:
            rat = 1 / rat
    return con


n1, n2 = map(int, input().split())
r1 = con_to_rat(list(map(int, input().split())), 0)
r2 = con_to_rat(list(map(int, input().split())), 0)

print(*rat_to_con(r1 + r2))
print(*rat_to_con(r1 - r2))
print(*rat_to_con(r1 * r2))
print(*rat_to_con(r1 / r2))
