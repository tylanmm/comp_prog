from sys import stdin, stdout

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

cubes = set()
for i in range(1, 10001):
    cubes.add(i*i*i)

for _ in range(int(_i())):
    x = int(_i())
    for c in cubes:
        if x - c in cubes:
            _p('YES')
            break
    else:
        _p('NO')

stdout.flush()