fin = open('travelin.txt')
fout = open('travelout.txt', 'w')

for t in range(int(fin.readline())):
    # setup matrix
    n = int(fin.readline())
    mat = [['Y']*n for _ in range(n)]

    inbound = fin.readline().strip()
    for i in range(n):
        if inbound[i] == 'Y':
            continue
        # everything up to i can't get into i (and therefore can't get past)
        for j in range(i):
            for k in range(i, n):
                mat[j][k] = 'N'
        # everything after i can't get into i (and therefore can't get past)
        for j in range(i+1, n):
            for k in range(i+1):
                mat[j][k] = 'N'
    
    outbound = fin.readline().strip()
    for i in range(n):
        if outbound[i] == 'Y':
            continue
        # everything up through i can't get past i
        for j in range(i+1):
            for k in range(i+1, n):
                mat[j][k] = 'N'
        # everything after i can't get past i
        for j in range(i, n):
            for k in range(i):
                mat[j][k] = 'N'
    
    for i in range(n): mat[i][i] = 'Y'

    fout.write(f'Case #{t+1}:\n')
    fout.write('\n'.join([''.join(line) for line in mat]) + '\n')

fin.close()
fout.close()