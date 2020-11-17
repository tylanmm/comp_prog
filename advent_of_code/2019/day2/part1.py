import sys

with open(sys.argv[1]) as f:
    comm = list(map(int, f.readline().split(',')))

comm[1] = 12
comm[2] = 2

i = 0
while comm[i] != 99:
    if comm[i] == 1:
        comm[comm[i+3]] = comm[comm[i+1]] + comm[comm[i+2]]
    else:
        comm[comm[i+3]] = comm[comm[i+1]] * comm[comm[i+2]]
    i += 4

print(comm[0])