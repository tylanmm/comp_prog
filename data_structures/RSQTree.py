# Used for making range sum queries
class RSQTree:

    def __init__(self, vals):
        self.vals = vals                    # Stores the original values
        self.tree = [0] * (len(vals) * 4)   # Provide plenty of space
        # self.tree stores the sum of the elements that correspond
        # to a given segment. 1-indexed (so index 0 stores a dummy value)
        self.build(1, 0, len(self.vals)-1)

    def build(self, i, L, R):
        if L == R:                          # If the range only has a single element
            self.tree[i] = self.vals[L]     # or R, either way
        else:                               # Then recursively build the subtrees
            self.build(self.left(i) , L           , (L+R)//2)
            self.build(self.right(i), (L+R)//2 + 1, R)
            self.tree[i] = self.tree[self.left(i)] + self.tree[self.right(i)]
    
    def RSQ(self, l, r):
        return self.rsq(1, 0, len(self.vals)-1, l, r)

    # Returns the the total of the elements in the query range
    # l, r defines the range that we are querying
    # L, R define the range that corresponds to the node we are currently inside
    # i is the index of the node that we are currently inside
    def rsq(self, i, L, R, l, r):
        if r < L or l > R:          # If the current node's range is fully outside the target
            return 0
        if l <= L and R <= r:       # If the current node's range is entirely contained in the queried range 
            return self.tree[i]
        
        return self.rsq(self.left(i), L, (L+R)//2, l, r) + self.rsq(self.right(i), (L+R)//2+1, R, l, r)

    def update(self, valI, n):
        self.up(1, 0, len(self.vals)-1, valI, n)

    # Handles dynamic changes where self.vals[i] is set equal to n
    def up(self, i, L, R, valI, n):
        if valI < L or valI > R:        # If the index to update is outside the range
            return
        if valI == L and valI == R:     # If we've hit the node corresponding to the index to update
            self.vals[valI] = n
            self.tree[i] = n
            return
        
        # Update the subtrees as necessary (only 1 will really be updated)
        self.up(self.left(i) , L           , (L+R)//2, valI, n)
        self.up(self.right(i), (L+R)//2 + 1, R       , valI, n)
        self.tree[i] = self.tree[self.left(i)] + self.tree[self.right(i)]

    # The children of a node are indexed like in a binary heap, where
    # 2*i is the left child and 2*i + 1 is the right
    def left(self, i):
        return i << 1
    
    def right(self, i):
        return (i << 1) + 1

if __name__ == '__main__':
    lst = [1, 4, 5, 2, 6, 7, 10]
    st = RSQTree(lst)
    print(st.vals)
    print(st.RSQ(1, 4))

    st.update(3, 0)
    print(st.vals)
    print(st.RSQ(1, 4))