"""
ID: tylan071
LANG: PYTHON3
TASK: numtri
"""

with open('numtri.in') as f:
    r = int(f.readline())
    rows = []
    for _ in range(r):
        rows.append(list(map(int, f.readline().split())))

for i in range(r-2, -1, -1):
    for j in range(i+1):
        rows[i][j] += max(rows[i+1][j], rows[i+1][j+1])

with open('numtri.out', 'w') as f:
    f.write(str(rows[0][0]) + '\n')