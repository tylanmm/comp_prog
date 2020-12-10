import sys
from itertools import permutations

output = 0
def run(comm, phase):
    global output
    i = 0
    got_phase = False
    while comm[i] != 99:
        code = comm[i] % 100
        mode = comm[i] // 100
        
        if code == 1:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]]
            comm[comm[i+3]] = val1 + val2
            i += 4
        
        elif code == 2:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]]
            comm[comm[i+3]] = val1 * val2
            i += 4
        
        elif code == 3:
            comm[comm[i+1]] = output if got_phase else phase
            got_phase = True
            i += 2
        
        elif code == 4:
            val = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            output = val
            i += 2
        
        elif code == 5:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]]
            if val1 != 0:
                i = val2
            else:
                i += 3
        
        elif code == 6:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]]
            if val1 == 0:
                i = val2
            else:
                i += 3
        
        elif code == 7:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]]
            comm[comm[i+3]] = 1 if val1 < val2 else 0
            i += 4
        
        elif code == 8:
            val1 = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            mode //= 10
            val2 = comm[i+2] if mode % 10 == 1 else comm[comm[i+2]]
            comm[comm[i+3]] = 1 if val1 == val2 else 0
            i += 4

with open(sys.argv[1]) as f:
    comm = list(map(int, f.readline().split(',')))

best = -float('inf')
for p in permutations(range(5), 5):
    output = 0
    for phase in p:
        run(comm.copy(), phase)
    best = max(best, output)
print(best)