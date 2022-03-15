from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

grid = [_i() for _ in range(8)]
row, col, di1, di2 = set(), set(), set(), set()

def solve():
    count = 0
    for i in range(8):
        for j in range(8):
            if grid[i][j] != '*': continue
            count += 1
            if (i in row) or (j in col) or (i+j in di1) or (i-j in di2):
                _p('invalid')
                return
            row.add(i)
            col.add(j)
            di1.add(i+j)
            di2.add(i-j)
    _p('valid' if count == 8 else 'invalid')

solve()

stdout.flush()