import math

with open("race.in") as f:
    raw = f.readlines()
    k, n = tuple(map(int, raw[0].split()))
    xs = list(map(int, raw[1:]))

def findTime(x):
    remDist = k
    speed = 1
    time = 0
    while True:
        remDist -= speed
        time += 1
        if remDist <= 0:
            return time
        if speed >= x:
            remDist -= speed
            time += 1
            if remDist <= 0:
                return time
        speed += 1

with open("race.out", "w+") as f:
    for x in xs:
        f.write(str(findTime(x)) + '\n')