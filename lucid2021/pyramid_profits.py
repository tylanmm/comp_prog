n = int(input())
boss = {}
emps = {}
earn = {}
for _ in range(n):
    emp, b, amt = input().split()
    boss[emp] = (b, int(amt))
    earn[emp] = 0
    earn[b] = 0

def dfs(emp, amt, pct):
    if emp in boss:
        amt = dfs(boss[emp][0], amt, boss[emp][1])
    emp_amt = amt * (100 - pct) / 100
    earn[emp] += emp_amt
    return amt - emp_amt

m = int(input())
for _ in range(m):
    emp, amt = input().split()
    amt = int(amt)
    dfs(emp, amt, 0)

ans = list(map(tuple, earn.items()))
for p, amt in sorted(ans):
    print(p, round(amt))