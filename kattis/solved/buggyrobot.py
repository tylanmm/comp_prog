# read dims
h, w = map(int, input().split())

# variables for tracking stuff; offset to make edges easier
curr = [[float('inf')]*(w+2) for _ in range(h+2)]
end = None

obs = [[False]*(w+2) for _ in range(h+2)]
obs[0] = [True]*(w+2)
obs[-1] = [True]*(w+2)
for i in range(1, h+1):
    obs[i][0] = True
    obs[i][-1] = True

# read in grid
for i in range(h):
    row = input()
    for j in range(w):
        # store needed info
        if row[j] == 'S':
            curr[i+1][j+1] = 0
        elif row[j] == '#':
            obs[i+1][j+1] = True
        elif row[j] == 'G':
            end = (i+1, j+1)

s = input()


def update(k, i, j, di, dj, inserted):
    if obs[i+di][j+dj]:     # hit wall, stuck in current cell
        curr[i][j] = min(curr[i][j], k+inserted)
    else:
        curr[i+di][j+dj] = min(curr[i+di][j+dj], k+inserted)


# change in row and col that results from a given command
di = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dj = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

t = 0
ans = float('inf')
while t <= len(s) + ans:
    prev, curr = curr, [[float('inf')]*(w+2) for _ in range(h+2)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if prev[i][j] == float('inf'):
                continue

            # update next cell with current command
            if t - prev[i][j] < len(s):
                c = s[t - prev[i][j]]
                update(prev[i][j], i, j, di[c], dj[c], False)

            # update all surrounding cells with inserted commands
            for c in di:
                update(prev[i][j], i, j, di[c], dj[c], True)

    ans = min(ans, curr[end[0]][end[1]])

    # for row in curr:
    #     print('\t'.join(map(str, row)))
    # print()

    t += 1

print(ans)
