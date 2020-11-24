with open("breedflip.in") as f:
    n = int(f.readline().strip())
    a = f.readline().strip()
    b = f.readline().strip()

count = 0
prev = -2
for i in range(len(b)):
    if b[i] != a[i]:
        if i != prev + 1:
            count += 1
        prev = i        

with open("breedflip.out", "w") as f:
    f.write(str(count) + "\n")