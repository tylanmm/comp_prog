# Used for counting number of elements that fall within a certain range
class FenwickTree:

    def __init__(self, n, nums=None):
        self.ft = [0]*(n+1)
        if nums:
            for n in nums:
                self.adjust(n, 1)
    
    # Updates cumulative counts at the "on" bits of a
    def rfq(self, a):
        total = 0
        while a:
            total += self.ft[a]
            a -= a & -a
        return total

    # Returns the count of elements between a and b (inclusive)
    def RFQ(self, a, b):
        return self.rfq(b) - (self.rfq(a) if a else 0)

    # Changes the number of occurrences of k by v
    def adjust(self, k, v):
        while k < len(self.ft):
            self.ft[k] += v
            k += k & -k

if __name__ == '__main__':
    lst = [5,2,9,8,4,5,7,6,6,7,6]
    ft = FenwickTree(11, lst)
    print(ft.RFQ(2, 5))
    ft.adjust(5, -1)
    print(ft.RFQ(2, 5))
    print(ft.ft)