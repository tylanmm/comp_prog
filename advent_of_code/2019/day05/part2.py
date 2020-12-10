import sys

def run(comm):
    i = 0
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
            comm[comm[i+1]] = int(input())
            i += 2
        
        elif code == 4:
            val = comm[i+1] if mode % 10 == 1 else comm[comm[i+1]]
            print(val)
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

run(comm)