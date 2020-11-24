with open('gymnastics.in') as f:
    k, n = map(int, f.readline().split())
    pos = []
    for _ in range(k):
        session = list(map(int, f.readline().split()))
        rank = [0]*n
        for i in range(n):
            rank[session[i]-1] = i
        pos.append(rank)

def is_valid_pair(i, j):
    if i == j:
        return False
    
    for rank in pos:
        if rank[i] < rank[j]:
            return False
    return True

pairs = 0
for i in range(n):
    for j in range(n):
        pairs += is_valid_pair(i, j)

with open('gymnastics.out', 'w') as f:
    f.write(str(pairs) + '\n')