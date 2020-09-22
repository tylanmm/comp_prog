"""
ID: tylan071
LANG: PYTHON3
TASK: ride
"""

with open("ride.in") as f:
    comet = f.readline().strip()
    group = f.readline().strip()

def convert(name):
    num = 1
    for c in name:
        num *= ord(c) - ord('A') + 1
    return num % 47

with open("ride.out", "w+") as f:
    cometNum = convert(comet)
    groupNum = convert(group)
    f.write("GO" if cometNum == groupNum else "STAY")
    f.write("\n")