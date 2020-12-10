import sys

def process(comms):
    comm = comms.copy()
    i = 0
    while True:
        if comm[i] == 99:
            i += 1
            return comm[0]
        elif comm[i] == 1:
            comm[comm[i+3]] = comm[comm[i+1]] + comm[comm[i+2]]
            i += 4
        elif comm[i] == 2:
            comm[comm[i+3]] = comm[comm[i+1]] * comm[comm[i+2]]
            i += 4

def solve(comm):
    for noun in range(100):
        for verb in range(100):
            comm[1] = noun
            comm[2] = verb
            if process(comm) == 19690720:
                return 100*noun + verb

with open(sys.argv[1]) as f:
    comm = list(map(int, f.readline().split(',')))

print(solve(comm))