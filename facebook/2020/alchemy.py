fin = open('alchemyin.txt')
fout = open('alchemyout.txt', 'w')

for t in range(int(fin.readline())):
    n = int(fin.readline())
    colors = fin.readline().strip()
    numA = colors.count('A')
    if n/3 <= numA <= 2*n/3:
        fout.write(f'Case #{t+1}: Y\n')
    else:
        fout.write(f'Case #{t+1}: N\n')

fin.close()
fout.close()