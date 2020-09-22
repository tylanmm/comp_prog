import sys

def complement(data):
    newData = [''] * len(data)
    for i in range(len(data)):
        if data[i] != '':
            newData[i] = int(not data[i])
        else:
            newData[i] = ''
    return newData

def reverse(data):
    return data[::-1]

def both(data):
    return complement(reverse(data))

"""
On the guess where things change, ask about the first bit
Use that first bit to narrow down the possible changes to
two of them. Look for the first bit between those two 
options that's different. If there is such a bit, ask
about that one and then modify the data that you know. If
no such bit exists, then apply any of the two operations
and continue asking for new bits.

Takes in the data that you already know, and the value of
the first bit after the change.

Finds the first bit that differentiates the remaining two
possibilities.
"""
def findBit(data, first):
    comp = complement(data)
    reve = reverse(data)
    core = both(data)

    # Determine which 2 of the 4 possibilities it's narrowed down to
    use1 = []
    use2 = []
    if data[0] == first:
        use1 = data.copy()
    elif comp[0] == first:
        use1 = comp
    
    if reve[0] == first:
        use2 = reve
    elif core[0] == first:
        use2 = core
    # Find and return the location of the first mismatched bit
    for i in range(len(use1)):
        if use1[i] != use2[i]:
            return i + 1
    
    # If we get this far, they're the same, so 
    # return -1 to apply complement
    # return -2 to do nothing (these are the only two possibilities)
    if use1 == comp:
        return -1
    else:
        return -2

# Figure out which operation to apply to the data based off of the new information and what the data was before
def detOp(data, bit1, bit2, bit2I):
    if data[0] == bit1 and data[bit2I] == bit2:
        return data
    comp = complement(data)
    reve = reverse(data)
    core = both(data)
    if comp[0] == bit1 and comp[bit2I] == bit2:
        return comp
    if reve[0] == bit1 and reve[bit2I] == bit2:
        return reve
    if core[0] == bit1 and core[bit2I] == bit2:
        return core

t, b = map(int, input().split())
for i in range(t):
    data = [''] * b
    for j in range(1, 6):
        print(j)
        sys.stdout.flush()
        data[j-1] = int(input())
        print(b - j + 1)
        sys.stdout.flush()
        data[-j] = int(input())
    
    emp = 6
    for j in range(14):
        # This part takes care of the first two guesses
        print(1)
        sys.stdout.flush()
        first = int(input())
        res = findBit(data, first)
        if res > -1:
            print(res)
            sys.stdout.flush()
            second = int(input())
            data = detOp(data, first, second, res - 1)
        elif res == -1:
            data = complement(data)
            print(emp - 1)
            sys.stdout.flush()
            data[emp-1] = int(input())
        else:
            print(emp - 1)
            sys.stdout.flush()
            data[emp-1] = int(input())

        # If after those first two guesses we know enough, then guess
        if '' not in data:
            print(''.join(map(str, data)))
            sys.stdout.flush()
            if input() == 'N':
                quit()
            else:
                break
        
        # Otherwise, keep asking for information
        for k in range(4):
            print(emp)
            sys.stdout.flush()
            data[emp-1] = int(input())
            print(b - emp + 1)
            sys.stdout.flush()
            data[-emp - 1] = int(input())
            emp += 1
            if '' not in data and k != 3:
                print(''.join(map(str, data)))
                sys.stdout.flush()
                if input() == 'N':
                    quit()
                else:
                    break
quit()