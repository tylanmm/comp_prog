import sys

with open(sys.argv[1]) as f:
    cups = list(map(int, f.read()))

def step():
    move = [cups.pop(1) for _ in range(3)]
    
    dest = cups[0]-1 + (len(cups) + len(move) if cups[0] == 1 else 0)
    while dest in move:
        dest -= 1
        if dest == 0:
            dest += len(cups) + len(move)
    
    destI = cups.index(dest)
    for n in move[::-1]:
        cups.insert(destI+1, n)
    
    cups.append(cups.pop(0))

def output(cups):
    oneI = cups.index(1)
    res = cups[oneI+1:] + cups[:oneI]
    print(''.join(map(str, res)))

for _ in range(100):
    step()

output(cups)