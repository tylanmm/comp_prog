def hash(f):
    val = 0
    for c in f:
        val ^= ord(c)
    return val

n = int(input())
while n:
    files = [input() for _ in range(n)]
    hashes = [hash(f) for f in files]

    unique = [True]*n
    collisions = 0
    for i in range(n-1):
        if not unique[i]: continue
        for j in range(i+1, n):
            if i != j and unique[j]:
                if hashes[i] == hashes[j]:
                    collisions += 1
                    if files[i] == files[j]:
                        unique[j] = False
    
    print(sum(unique), collisions)
    n = int(input())