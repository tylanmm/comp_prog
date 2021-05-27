def hash(f):
    val = 0
    for c in f:
        val ^= ord(c)
    return val

n = int(input())
while n:
    files = [input() for _ in range(n)]
    hashes = [hash(f) for f in files]

    unique = set()
    inSet = [True]*n
    collisions = 0
    for i in range(n):
        if files[i] in unique:
            inSet[i] = False
            collisions += 1
            continue
        unique.add(files[i])
        for j in range(i):
            if hashes[i] == hashes[j] and inSet[j]:
                collisions += 1
                if files[j] == files[i]:
                    inSet[i] = False
    
    print(len(unique), collisions)
    n = int(input())