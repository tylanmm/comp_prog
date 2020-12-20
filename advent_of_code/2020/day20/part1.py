import sys

sys.setrecursionlimit(200000)

class Tile:

    def __init__(self, id, rows):
        self.id = id
        self.r = len(rows)
        self.c = len(rows[0]) if rows else 0
        self.grid = [list(r) for r in rows]
    
    def rotate90(self):
        res = [['']*self.r for _ in range(self.c)]
        for c in range(self.c):
            for r in range(self.r):
                res[c][-r - 1] = self.grid[r][c]
        self.r, self.c = self.c, self.r
        self.grid = res
    
    def fliph(self):
        for r in self.grid:
            r.reverse()
    
    def flipv(self):
        for i in range(self.r//2):
            self.grid[i], self.grid[-i-1] = self.grid[-i-1], self.grid[i]

    def getid(self):
        return self.id

    def toprow(self):
        return self.grid[0] if self.grid else None
    
    def bottomrow(self):
        return self.grid[-1] if self.grid else None
    
    def leftcol(self):
        return [self.grid[i][0] for i in range(self.c)] if self.grid else None

    def rightcol(self):
        return [self.grid[i][-1] for i in range(self.c)] if self.grid else None

    def __str__(self):
        return f'Tile {self.id}\n' + '\n'.join([' '.join(r) for r in self.grid])
    
    def __repr__(self):
        return self.__str__()


class TilePhoto:

    def __init__(self, tiles, rows=None, cols=None):
        self.tiles = tiles
        self.pos = [None]*len(tiles)
        if rows != None and cols != None:
            self.r = rows
            self.c = cols
        else:
            self.r = int(len(tiles)**0.5)
            self.c = int(len(tiles)**0.5)
        self.photo = [[None]*self.c for _ in range(self.r)]
    
    def fit_tiles(self, i=0, j=0):
        if j == self.c:
            j = 0
            i += 1
        if i == self.r:
            return True
        
        for t in range(len(self.tiles)):
            if self.pos[t] != None: 
                continue
            
            for m in range(2):
                for o in range(4):
                    if self.tile_fits(self.tiles[t], i, j):
                        self.pos[t] = (i, j)
                        self.photo[i][j] = self.tiles[t]
                        works = self.fit_tiles(i, j+1)
                        if works:
                            return True
                    self.tiles[t].rotate90()
                self.tiles[t].flipv()
            self.pos[t] = None
        
        self.photo[i][j] = None
        
        return False
    
    def tile_fits(self, tile, r, c):
        works = True
        if r:
            works &= self.photo[r-1][c].bottomrow() == tile.toprow()
        if c:
            works &= self.photo[r][c-1].rightcol() == tile.leftcol()
        return works
    
    def mult_corners(self):
        try:
            val  = self.photo[0][0].getid() * self.photo[0][-1].getid()
            val *= self.photo[-1][0].getid() * self.photo[-1][-1].getid()
            return val
        except Exception:
            print('Invalid photo; could not multiply IDs')
            return 0

    def __str__(self):
        try:
            res = []
            # for each row in the photo
            for i in range(self.r):
                # for each line in that row's tiles
                for line in range(self.photo[0][0].r):
                    res_line = []
                    # skip the top line if we're not in the top row
                    if i != 0 and line == 0:
                        continue
                    # for each tile in that row
                    for j in range(self.c):
                        tile_line = ''.join(self.photo[i][j].grid[line])
                        # ignore the first character if we're not in the first column
                        if j != 0:
                            res_line.append(tile_line[1:])
                        else:
                            res_line.append(tile_line)
                    res.append(''.join(res_line))
            return '\n'.join(res)
        except Exception:
            return 'Could not construct photo'
                            
                        
with open(sys.argv[1]) as f:
    raw = f.read().split('\n\n')

tiles = []
for t in raw:
    raw_id, *tile = t.split('\n')
    id = int(raw_id.split(' ')[1][:-1])
    tiles.append(Tile(id, tile))

photo = TilePhoto(tiles)
photo.fit_tiles()
print(photo.mult_corners())