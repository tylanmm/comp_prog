from math import gcd

class GCDSegTree:

    def __init__(self, nums):
        # find size of complete binary tree
        n = len(nums)
        self.n = n
        lsb = n & -n
        while lsb != n:
            n += lsb
            lsb = n & -n
        
        # pad the tree
        tree = [0]*(2*n)
        for i in range(self.n):
            tree[n+i] = nums[i]
        
        # propogate the values
        for i in range(n-1, 0, -1):
            tree[i] = gcd(tree[2*i], tree[2*i+1])
        self.t = tree
    
    def _q(self, node, nL, nR, qL, qR):
        # if this node's range is completely in range, return its value
        if qL <= nL and nR <= qR:
            return self.t[node]
        # if this node's range is completely disjoin, return "null"
        if nR < qL or qR < nL:
            return 0
        
        # go down into left and right children
        mid = (nL + nR) // 2
        left = self._q(node*2, nL, mid, qL, qR)
        right = self._q(node*2+1, mid+1, nR, qL, qR)
        return left if not right else right if not left else gcd(left, right)
    
    def query(self, left, right):
        return self._q(1, 0, self.n-1, left, right)
    
    def update(self, i, val):
        # update, and then propogate the change upwards
        self.t[self.n+i] = val
        curr = (self.n+i)//2
        while curr:
            self.t[curr] = gcd(self.t[2*curr], self.t[2*curr+1])
            curr //= 2
        
        
if __name__ == '__main__':
    seg = GCDSegTree([8, 0, 18, 3, 12, 6, 2, 7])
    print(seg.query(2, 5))
    seg.update(3, 6)
    print(seg.query(2, 5))