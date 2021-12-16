import sys

data = [format(int(c, 16), '04b') for c in sys.stdin.read()]
transmission = ''.join(data)

def read_literal(i, trans):
    res = 0
    stop = False
    while not stop:
        stop = not int(trans[i])
        i += 1
        for _ in range(4):
            res *= 2
            res += int(trans[i])
            i += 1
    return i, res

def evaluate(T, val, res):
    if T == 0: return res + val
    if T == 1: return res * val
    if T == 2: return min(res, val)
    if T == 3: return max(res, val)
    if T == 5: return 1 if res > val else 0
    if T == 6: return 1 if res < val else 0
    if T == 7: return 1 if res == val else 0

def read_packet(i, trans):
    V = int(trans[i:i+3], 2)
    T = int(trans[i+3:i+6], 2)
    res = 0
    i += 6
    if T == 4:
        i, res = read_literal(i, trans)
    else:
        len_type_ID = int(trans[i])
        i += 1
        first_packet = True
        if len_type_ID == 0:
            stop = i + 15 + int(trans[i:i+15], 2)
            i += 15
            while i < stop:
                i, dv, val = read_packet(i, trans)
                V += dv
                if first_packet:
                    first_packet = False
                    res = val
                else:
                    res = evaluate(T, val, res)
        else:
            num_subpackets = int(trans[i:i+11], 2)
            i += 11
            for _ in range(num_subpackets):
                i, dv, val = read_packet(i, trans)
                V += dv
                if first_packet:
                    first_packet = False
                    res = val
                else:
                    res = evaluate(T, val, res)
    return i, V, res

i, version_total, res = read_packet(0, transmission)
print("result={}".format(res))