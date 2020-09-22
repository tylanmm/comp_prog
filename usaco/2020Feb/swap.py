with open("swap.in") as f:
    n, k = tuple(map(int, f.readline().split()))
    a1, a2 = tuple(map(lambda x : int(x) - 1, f.readline().split()))
    b1, b2 = tuple(map(lambda x : int(x) - 1, f.readline().split()))

def doSwaps(cows):
    cows = cows[:a1] + cows[a1:a2+1][::-1] + cows[a2+1:]
    cows = cows[:b1] + cows[b1:b2+1][::-1] + cows[b2+1:]
    return cows

# Find out how many steps are necessary before the cows reset
counter = 0
original = list(range(1, n+1))
cows = list(range(1, n+1))
while counter < k:
    counter += 1
    cows = doSwaps(cows)
    if cows == original:
        break

for i in range(k % counter):
    cows = doSwaps(cows)

with open("swap.out", "w") as f:
    for c in cows:
        f.write(str(c) + "\n")