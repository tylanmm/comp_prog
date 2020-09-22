def genRest(a, b, c, d, n, sizes):
    for i in range(n-len(sizes)):
        sizes.append(((a*sizes[-2] + b*sizes[-1] + c) % d) + 1)

def solve(lengths, widths, heights):
    pass

answers = []
with open('perimetric_1_in.txt') as f:
    for t in range(int(f.readline())):
        n, k = map(int, f.readline().split())
        lengths = list(map(int, f.readline().split()))
        al, bl, cl, dl = map(int, f.readline().split())
        widths = list(map(int, f.readline().split()))
        aw, bw, cw, dw = map(int, f.readline().split())
        heights = list(map(int, f.readline().split()))
        ah, bh, ch, dh = map(int, f.readline().split())
        
        genRest(al, bl, cl, dl, n, lengths)
        genRest(aw, bw, cw, dw, n, widths)
        genRest(ah, bh, ch, dh, n, heights)
        answers.append((t+1, solve(lengths, heights, w)))

with open('perimetric_1_out.txt', 'w') as f:
    for t, p in answers:
        f.write(f'Case #{t}: {p}\n')