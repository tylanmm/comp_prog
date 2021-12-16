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

def read_packet(i, trans):
    V = int(trans[i:i+3], 2)
    T = int(trans[i+3:i+6], 2)
    print("i={} V={} T={}".format(i, V, T))
    i += 6
    if T == 4:
        i, num = read_literal(i, trans)
        # print("num={}".format(num))
    else:
        len_type_ID = int(trans[i])
        i += 1
        if len_type_ID == 0:
            stop = i + 15 + int(trans[i:i+15], 2)
            i += 15
            while i < stop:
                i, dv = read_packet(i, trans)
                V += dv
        else:
            num_subpackets = int(trans[i:i+11], 2)
            i += 11
            for _ in range(num_subpackets):
                i, dv = read_packet(i, trans)
                V += dv
    return i, V

print("transmission={}".format(transmission))
i, version_total = read_packet(0, transmission)
print("version number total={}".format(version_total))