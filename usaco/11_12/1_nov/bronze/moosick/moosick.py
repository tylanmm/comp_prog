with open('moosick.in') as f:
    n = int(f.readline())
    song = [int(f.readline()) for _ in range(n)]
    c = int(f.readline())
    chord = sorted([int(f.readline()) for _ in range(c)])

steps = []
for i in range(1, c):
    steps.append(chord[i] - chord[i-1])

rum_chords = []
for i in range(n-c+1):
    section = sorted(song[i:i+c])
    for j in range(1, c):
        if section[j] - section[j-1] != steps[j-1]:
            break
    else:
        rum_chords.append(str(i+1))

with open('moosick.out', 'w') as f:
    f.write(str(len(rum_chords)) + '\n')
    if len(rum_chords) > 0:
        f.write('\n'.join(rum_chords) + '\n')