# Used for making range minimum queries
class SegmentTree:

    def __init__(self, vals):
        self.vals = vals                    # Stores the original values
        self.tree = [0] * (len(vals) * 4)   # Provide plenty of space
        # self.tree stores the index of the smallest element that corresponds
        # to a given segment. 1-indexed (so index 0 stores a dummy value)
        self.build(1, 0, len(self.vals)-1)

    def build(self, i, L, R):
        if L == R:                  # If the range only has a single element
            self.tree[i] = L        # or R, either way
        else:                       # Then recursively build the subtrees
            self.build(self.left(i) , L           , (L+R)//2)
            self.build(self.right(i), (L+R)//2 + 1, R)
            i1 = self.tree[self.left(i) ]
            i2 = self.tree[self.right(i)]
            self.tree[i] = i1 if self.vals[i1] <= self.vals[i2] else i2
    
    def RMQ(self, l, r):
        return self.rmq(1, 0, len(self.vals)-1, l, r)

    # Returns the index in self.vals where the minimum of the given range is stored
    # l, r defines the range that we are querying
    # L, R define the range that corresponds to the node we are currently inside
    # i is the index of the node that we are inside
    def rmq(self, i, L, R, l, r):
        if r < L or l > R:          # If node i's range is fully outside the target
            return -1
        if l <= L and R <= r:       # If node i’s range is contained in the queried range 
            return self.tree[i]
        
        # Look for the min element in the left and right segments
        i1 = self.rmq(self.left(i) , L           , (L+R)//2, l, r)
        i2 = self.rmq(self.right(i), (L+R)//2 + 1, R       , l, r)
        
        # At least one of those two indices will be valid
        # Return the valid one if the other is invalid
        if i1 == -1:
            return i2
        if i2 == -1:
            return i1
        
        # Finally, if i1 and i2 are valid, return the index that contains the smaller value
        return i1 if self.vals[i1] <= self.vals[i2] else i2

    def update(self, valI, n):
        self.up(1, 0, len(self.vals)-1, valI, n)

    # Handles dynamic changes where self.vals[i] is set equal to n
    def up(self, i, L, R, valI, n):
        if valI < L or valI > R:        # If the index to update is outside the range
            return
        if valI == L and valI == R:     # If we've hit the node of the index to update
            self.vals[valI] = n
            return
        
        # Update the subtrees as necessary (only 1 will really by updated)
        self.up(self.left(i) , L           , (L+R)//2, valI, n)
        self.up(self.right(i), (L+R)//2 + 1, R       , valI, n)
        # Update the current node using the smaller of the two values
        i1 = self.tree[self.left(i) ]
        i2 = self.tree[self.right(i)]
        self.tree[i] = i1 if self.vals[i1] <= self.vals[i2] else i2

    # The children of a node are indexed like in a binary heap, where
    # 2*i is the left child and 2*i + 1 is the right
    def left(self, i):
        return i << 1
    
    def right(self, i):
        return (i << 1) + 1

if __name__ == '__main__':
    lst = [18, 17, 21, 11, 13, 16, 10]
    st = SegmentTree(lst)
    print(st.vals)
    print(st.RMQ(0, 4))

    st.update(3, 99)
    print(st.vals)
    print(st.RMQ(0, 4))