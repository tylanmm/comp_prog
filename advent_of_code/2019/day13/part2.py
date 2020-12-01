import sys
import os

def updateScreen(objs, score):
    screen = [[' ']*42 for _ in range(20)]
    for c, r in objs:
        if objs[(c, r)] == 1:
            screen[r][c] = '#'
        elif objs[(c, r)] == 2:
            screen[r][c] = '▯'
        elif objs[(c, r)] == 3:
            screen[r][c] = '_'
        elif objs[(c, r)] == 4:
            screen[r][c] = 'o'
    
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 'Score: %d' % score
    print(f'{score:^42}')
    print('\n'.join([''.join(r) for r in screen]))
    

def run(comm):
    i = 0
    base = 0
    comm = comm + [0]*(1000000 - len(comm))
    score = 0
    pos = []
    objs = {}
    joystick = 0
    ball = 0
    paddle = 0
    update = False
    numBlocks = 0
    while comm[i] != 99:
        code = comm[i] % 100
        mode = comm[i] // 100
        
        if code == 1:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]] if mode % 10 == 0 else comm[comm[i+2] + base]
            mode //= 10
            comm[comm[i+3] + (base if mode else 0)] = val1 + val2
            i += 4
        
        elif code == 2:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]] if mode % 10 == 0 else comm[comm[i+2] + base]
            mode //= 10
            comm[comm[i+3] + (base if mode else 0)] = val1 * val2
            i += 4
        
        elif code == 3:
            comm[comm[i+1] + (base if mode else 0)] = -1 if ball < paddle else 1 if ball > paddle else 0
            i += 2
        
        elif code == 4:
            val = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            pos.append(val)
            if len(pos) == 3:
                if pos[0] == -1 and pos[1] == 0:
                    score = val
                else:
                    objs[(pos[0], pos[1])] = pos[2]
                    if pos[2] == 2:
                        numBlocks += 1
                        update = numBlocks > 206
                    if pos[2] == 3:
                        paddle = pos[0]
                    elif pos[2] == 4:
                        ball = pos[0]
                pos = []
                if update: updateScreen(objs, score)
            i += 2
        
        elif code == 5:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]] if mode % 10 == 0 else comm[comm[i+2] + base]
            if val1 != 0:
                i = val2
            else:
                i += 3
        
        elif code == 6:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]] if mode % 10 == 0 else comm[comm[i+2] + base]
            if val1 == 0:
                i = val2
            else:
                i += 3
        
        elif code == 7:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]] if mode % 10 == 0 else comm[comm[i+2] + base]
            mode //= 10
            comm[comm[i+3] + (base if mode else 0)] = 1 if val1 < val2 else 0
            i += 4
        
        elif code == 8:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]] if mode % 10 == 0 else comm[comm[i+2] + base]
            mode //= 10
            comm[comm[i+3] + (base if mode else 0)] = 1 if val1 == val2 else 0
            i += 4
        
        elif code == 9:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]] if mode % 10 == 0 else comm[comm[i+1] + base]
            base += val1
            i += 2
    
    return score


with open(sys.argv[1]) as f:
    comm = list(map(int, f.readline().split(',')))

score = run(comm)
print(score)