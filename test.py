with open('test.txt', 'w') as f:
    f.write('1\n1000 1000\n')
    for i in range(999):
        f.write(f'1 {i+1} {i+2}\n')
    f.write(f'1 1000 1\n')