class Node:
    def __init__(self, ra, pa, rb, pb, score, turn, visited, s):
        self.ra = ra
        self.pa = pa
        self.rb = rb
        self.pb = pb
        self.s = s
        self.turn = turn
        self.children = []
        self.visited = visited
        self.score = score
    
    def getChildren(self, r, p):
        if p % 2 == 0: # if triangle points down
            return [(r-1, p-1), (r, p-1), (r, p+1)]
        else:
            children = []
            if p < r*2-1:
                children.append((r, p+1))
            if r < self.s:
                children.append((r+1, p+1))
            if p > 1:
                children.append((r, p-1))
            return children

    def getBestChild(self):
        if self.turn % 2: # bethe's turn
            poss = self.getChildren(self.rb, self.pb)
            noC = True
            if poss:
                for r, p in poss:
                    if str(r)+str(p) not in self.visited:
                        n = Node(self.ra, self.ra, r, p, self.score-1, self.turn+1, self.visited + str(r) + str(p) + " ", self.s)
                        noC = False
                        self.children.append(n)
                        n.getBestChild()
            if self.turn < self.s**2 and noC:
                n = Node(self.ra, self.pa, self.rb, self.pb, self.score, self.turn+1, self.visited, s)
                self.children.append(n)
                n.getBestChild()
        else:
            poss = self.getChildren(self.ra, self.pa)
            noC = True
            if poss:
                for r, p in poss:
                    if str(r)+str(p) not in self.visited:
                        n = Node(r, p, self.rb, self.pb, self.score+1, self.turn+1, self.visited + str(r) + str(p) + " ", self.s)
                        noC = False
                        self.children.append(n)
                        n.getBestChild()
            if self.turn < self.s**2 and noC:
                n = Node(self.ra, self.pa, self.rb, self.pb, self.score, self.turn+1, self.visited, self.s)
                self.children.append(n)
                n.getBestChild()
        
        if self.children:
            if self.turn % 2:
                score = float('inf')
                for child in self.children:
                    score = min(score, child.score)
            else:
                score = -float('inf')
                for child in self.children:
                    score = max(score, child.score)
            self.score = score

def solve(s, ra, pa, rb, pb, c):
    visited = '%d%d %d%d ' % (ra, pa, rb, pb)
    for _ in range(c):
        visited += ''.join(input().split()) + ' '
    n = Node(ra, pa, rb, pb, 0, 0, visited, s)
    n.getBestChild()
    return n.score    

for t in range(int(input())):
    s, ra, pa, rb, pb, c = map(int, input().split())
    print('Case #%d: %d' % (t+1, solve(s, ra, pa, rb, pb, c)))