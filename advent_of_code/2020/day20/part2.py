import sys
from time import time

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
    
    def get_roughness(self, tile):
        grid = self.__str__()
        total_pound = grid.count('#')
        grid = grid.split('\n')
        
        found_pounds = set()

        # for every possible orientation of the tile
        for m in range(2):
            for o in range(4):
                found_pounds.update(self.check_tile(tile, grid))
                tile.rotate90()
            tile.flipv()
        
        return total_pound - len(found_pounds)

    def check_tile(self, tile, grid):
        # for every possible top left corner to start the tile at
        # use the input orientation of the tile
        all_found_pounds = set()
        for i in range(len(grid) - len(tile.grid) + 1):
            for j in range(len(grid[i]) - len(tile.grid[0]) + 1):
                found_pounds = self.tile_matches(tile, grid, i, j)
                all_found_pounds.update(found_pounds)
        return all_found_pounds

    def tile_matches(self, tile, grid, i, j):
        # use i, j as top left corner; k, l are offsets
        found_pounds = set()
        for k in range(tile.r):
            for l in range(tile.c):
                if tile.grid[k][l] == '#':
                    if grid[i+k][j+l] == '.':
                        return set()
                    found_pounds.add((i+k, j+l)) 
        return found_pounds

    def __str__(self):
        try:
            res = []
            # for each row in the photo
            for i in range(self.r):
                # for each line in that row's tiles
                for line in range(1, self.photo[0][0].r-1):
                    res_line = []
                    # for each tile in that row
                    for j in range(self.c):
                        tile_line = ''.join(self.photo[i][j].grid[line])
                        res_line.append(tile_line[1:-1])
                    res.append(''.join(res_line))
            return '\n'.join(res)
        except Exception:
            return 'Could not construct photo'
                            
s = time()
with open(sys.argv[1]) as f:
    raw = f.read().split('\n\n')

tiles = []
for t in raw:
    raw_id, *tile = t.split('\n')
    id = int(raw_id.split(' ')[1][:-1])
    tiles.append(Tile(id, tile))

photo = TilePhoto(tiles)
photo.fit_tiles()

with open('monster.txt') as f:
    SEA_MONSTER = Tile(0, f.read().split('\n'))

print(photo.get_roughness(SEA_MONSTER))
e = time()
print(f'Time elapsed: {e-s} seconds')