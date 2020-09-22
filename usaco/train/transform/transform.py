"""
ID: tylan071
LANG: PYTHON3
TASK: transform
"""

def rotate90(grid):
    out = []
    for j in range(len(grid[0])):
        row = ''
        for i in range(len(grid)-1, -1, -1):
            row += grid[i][j]
        out.append(row)
    return out

def rotate180(grid):
    return rotate90(rotate90(grid))

def rotate270(grid):
    return rotate180(rotate90(grid))

def reflect(grid):
    return [grid[i][::-1] for i in range(len(grid))]

with open('transform.in') as f:
    n = int(f.readline().strip())
    begin = [f.readline().strip() for _ in range(n)]
    after = [f.readline().strip() for _ in range(n)]

answer = '7'
if rotate90(begin) == after:
    answer = '1'
elif rotate180(begin) == after:
    answer = '2'
elif rotate270(begin) == after:
    answer = '3'
elif reflect(begin) == after:
    answer = '4'
elif rotate90(reflect(begin)) == after:
    answer = '5'
elif rotate180(reflect(begin)) == after:
    answer = '5'
elif rotate270(reflect(begin)) == after:
    answer = '5'
elif begin == after:
    answer = '6'

with open('transform.out', 'w') as f:
    f.write(answer + '\n')