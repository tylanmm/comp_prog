class Node:

    def __init__(self, a, b):
        self.lo = a
        self.hi = b
        self.left = None
        self.right = None
    
    def add(self, lo, hi):
        total = 0
        left, right = True, True
        if lo < self.lo:
            if self.left:
                t, l, r = self.left.add(lo, self.lo if hi > self.lo else hi)
                total += t
                left &= l
            else:
                self.left = Node(lo, self.lo if hi > self.lo else hi)
                total += self.left.hi - self.left.lo
        elif lo <= self.hi:
            left = False
        
        if hi > self.hi:
            if self.right:
                t, l, r = self.right.add(self.hi if lo < self.hi else lo, hi)
                total += t
                right &= r
            else:
                self.right = Node(self.hi if lo < self.hi else lo, hi)
                total += self.right.hi - self.right.lo
        elif hi >= self.lo:
            right = False
        
        return total, left, right

def genRest(a, b, c, d, n, sizes):
    for i in range(n-len(sizes)):
        sizes.append(((a*sizes[-2] + b*sizes[-1] + c) % d) + 1)

def solve(lengths, widths, heights):
    p = 2*(widths[0] + heights[0])
    res = p
    tree = Node(lengths[0], lengths[0] + widths[0])

    for i in range(1, len(lengths)):
        amt, left, right = tree.add(lengths[i], lengths[i] + widths[i])
        if left and right:
            p += 2*(widths[i] + heights[i])
        elif left or right:
            p += 2*amt + heights[i]
        else:
            p += 2*amt
        res *= p
        res %= 1_000_000_007
    
    return res

answers = []
with open('perimetric_2_in.txt') as f:
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
        answers.append((t+1, solve(lengths, widths, heights)))

with open('perimetric_2_out.txt', 'w') as f:
    for t, p in answers:
        f.write(f'Case #{t}: {p}\n')