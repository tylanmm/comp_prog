from sys import stdin, stdout


# standard input/output functions
def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)


# prefix sum across all possible values of i
mod = int(1e9) + 7
vals = [6]
for i in range(1, 100000):
    vals.append(((i+1)*(i+2)*(i+3) + vals[-1]) % mod)

# i is 1 indexed
# size is the number of elements counting from i (inclusive)
# i is negative if we want the value to be negative
def get_range_sum(i, size):
    return rsq(abs(i)-1, abs(i)-2+size) * (1 if i > 0 else -1)

def rsq(x, y):
    return vals[y] - (vals[x-1] if x != 0 else 0)


class LazySegment:

    def __init__(self, n):
        self.n = n
        self.tree = [0]*(2*n)
        self.lazy = [0]*(2*n)
    
    def update(self, x, y, isAdd=True):
        self._update(1, 1, self.n, x, y, isAdd)

    def _update(self, ri, rs, re, us, ue, isAdd):
        # out of range
        if re < us or ue < rs:
            return
        # propagate as necessary
        self._lazy(ri, rs, re, us, isAdd)

        
        # completely in the target range
        if us <= rs and re <= ue:
            
            # update the value of the current node
            # reuse the _lazy function to handle proper propagation
            self._lazy(ri, rs, re, us, isAdd)

            return
        
        # overlaps target range
        mid = (rs + re) // 2
        self._update(  ri*2,    rs, mid, us, ue, isAdd)
        self._update(ri*2+1, mid+1,  re, us, ue, isAdd)

        self.tree[ri] = (self.tree[ri*2] + self.tree[ri*2 + 1]) % mod
  
    def _lazy(self, ri, rs, re, us, isAdd=True):
        # we have a pending update
        if self.lazy[ri] != 0:
            
            # grab the corresponding range sum
            # multiply that by the size of this interval
            # update the current node's value
            self.tree[ri] += get_range_sum(self.lazy[ri], re - rs + 1)
            
            # if this isn't a leaf node,
            # then send the update to the children
            if rs != re:

                # children may have their own pending updates
                # since I don't have a way to stack updates (yet),
                # we have to recur to make sure we don't overwrite
                mid = (rs + re)//2
                self._lazy(    ri*2,      rs, mid, us, isAdd)
                self._lazy(ri*2 + 1, mid + 1,  re, us, isAdd)
            
            self.lazy[ri] = 0
        else:
            
            # now that the update has happened, 
            # replace the pending update        
            self.lazy[ri] = (rs - us + 1) * (1 if isAdd else -1)

    def query(self, x, y):
        return self._query(1, 1, self.n, x, y)
    
    def _query(self, ri, rs, re, us, ue):
        self._lazy(ri, rs, re, us)
        
        # not in range
        if ue < rs or re < us:
            return 0
        
        # completely in range
        if us <= rs and re <= ue:
            return self.tree[ri]
        
        # overlaps range; get segments
        mid = (rs + re)//2
        left  = self._query(  ri*2,    rs, mid, us, ue)
        right = self._query(ri*2+1, mid+1,  re, us, ue)
        return (left + right) % mod

n, m = map(int, _i().split())
arr = LazySegment(n)
for _ in range(m):
    t, x, y = map(int, _i().split())
    if t == 0:
        _p(arr.query(x, y))
    elif t == 1:
        arr.update(x, y)
    elif t == 2:
        arr.update(x, y, False)
    print(arr.tree)

stdout.flush()