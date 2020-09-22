a, b, game = 0, 0, input()
for i in range(0, len(game), 2):
    if game[i] == 'A':
        a += int(game[i+1])
    else:
        b += int(game[i+1])

print('A' if a > b else 'B')