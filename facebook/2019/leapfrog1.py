f = open('leapfrogin.txt')
o = open('leapfrogout.txt', 'w')
for t in range(int(f.readline())):
    l = f.readline().strip()
    numB = l.count('B') 
    if len(l)//2 <= numB <= len(l)-2:
        o.write(f'Case #{t+1}: Y\n')
    elif 2 <= numB <= len(l)-2:
        o.write(f'Case #{t+1}: Y\n')
    else:
        o.write(f'Case #{t+1}: N\n')
f.close()
o.close()