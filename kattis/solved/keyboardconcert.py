n, m = map(int, input().split())
instr = [set() for _ in range(m+1)]
for i in range(n):
    k, *l = map(int, input().split())
    for note in l:
        instr[note].add(i)
notes = list(map(int, input().split()))

# dp[i][j] = min switches to end up on note i and instrument j
dp = [[float('inf')]*n for _ in range(m)]

# initialize dp array
for i in instr[notes[0]]:
    dp[0][i] = 0

note_min = [float('inf')]*m
note_min[0] = 0
for i in range(1, m):
    for j in range(n):
        if j in instr[notes[i]]:
            dp[i][j] = min(dp[i][j], dp[i-1][j], note_min[i-1] + 1)
            note_min[i] = min(note_min[i], dp[i][j])

print(min(dp[-1]))
# for row in dp:
#     print('\t'.join(map(str, row)))