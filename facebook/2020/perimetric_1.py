def genRest(a, b, c, d, n, sizes):
    for i in range(n-len(sizes)):
        sizes.append(((a*sizes[-2] + b*sizes[-1] + c) % d) + 1)

def solve(lengths, heights, w):
    p = [2*(heights[0] + w)]
    res = p[0]
    for i in range(1, len(lengths)):
        if lengths[i] > lengths[i-1] + w:       # current room does not overlap previous
            p.append(p[-1] + 2*(heights[i] + w))
        elif heights[i] <= heights[i-1]:        # current room is shorter than previous
            p.append(p[-1] + 2*(lengths[i] - lengths[i-1]))
        else:                                   # current room is taller than previous
            hiJ = i-1
            for j in range(i-1, -1, -1):
                if lengths[j] + w < lengths[i]:
                    break
                if heights[j] > heights[hiJ]:
                    hiJ = j
            
            if heights[i] <= heights[hiJ]:
                p.append(p[hiJ] + 2*(lengths[i] - lengths[hiJ]))
            else:
                p.append(p[hiJ] + 2*(heights[i] - heights[hiJ] + lengths[i] - lengths[hiJ]))
        
        res *= p[-1]
        res %= 1_000_000_007
    
    return res

answers = []
with open('perimetric_1_in.txt') as f:
    for t in range(int(f.readline())):
        n, k, w = map(int, f.readline().split())
        lengths = list(map(int, f.readline().split()))
        al, bl, cl, dl = map(int, f.readline().split())
        heights = list(map(int, f.readline().split()))
        ah, bh, ch, dh = map(int, f.readline().split())
        
        genRest(al, bl, cl, dl, n, lengths)
        genRest(ah, bh, ch, dh, n, heights)
        answers.append((t+1, solve(lengths, heights, w)))

with open('perimetric_1_out.txt', 'w') as f:
    for t, p in answers:
        f.write(f'Case #{t}: {p}\n')