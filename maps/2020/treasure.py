class piece:
    w = 0
    h = 0
    map = []

    def __init__(self, w, h, map):
        self.w = w
        self.h = h
        self.map = map
    
    def rotate90(self):
        newMap = []
        for i in range(w):
            line = ''
            for j in range(h-1, -1, -1):
                line += map[i][j]
            newMap.append(line)
        self.map = newMap
    
    def rotate180(self):
        self.rotate(90)
        self.rotate(90)
    
    def rotate270(self):
        self.rotate(90)
        self.rotate(90)
        self.rotate(90)
    
    def print(self):
        for i in range(h):
            print(self.map[i])

pieces = []
n = int(input())
for _ in range(n):
    w, h = tuple(map(int, input().split()))
    map = [input() for i in range(h)]
    pieces.append(piece(w, h, map))

for p in pieces:
    p.print()