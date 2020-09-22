"""
ID: tylan071
LANG: PYTHON3
TASK: sort3
"""

with open('sort3.in') as f:
    n = int(f.readline())
    nums = [int(f.readline()) for _ in range(n)]

inOrder = sorted(nums)

moves = [[0]*4 for _ in range(4)]
for i in range(n):
    moves[nums[i]][inOrder[i]] += 1

count = 0
coords = [(1, 2), (1, 3), (2, 3)]
for i, j in coords:
    amt = min(moves[i][j], moves[j][i])
    count += amt
    moves[i][j] -= amt
    moves[j][i] -= amt
count += 2 * max(moves[1][2], moves[1][3])

with open('sort3.out', 'w') as f:
    f.write(f'{count}\n')