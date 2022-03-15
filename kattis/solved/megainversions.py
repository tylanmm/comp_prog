# Used for counting number of elements that fall within a certain range
class FenwickTree:

    def __init__(self, n, nums=None):
        self.n = n
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
        if a > self.n:
            return 0
        return self.rfq(min(b, self.n)) - (self.rfq(a-1) if a else 0)

    # Changes the number of occurrences of k by v
    def adjust(self, k, v):
        while k < len(self.ft):
            self.ft[k] += v
            k += k & -k

n, a = int(input()), list(map(int, input().split()))
ft = FenwickTree(n)
total = FenwickTree(n, a)
res = 0 
for i in range(n):
    num = a[i]
    # get the amount of larger numbers that we have already seen
    hi = ft.RFQ(num+1, n)
    # amount of lower numbers that we have yet to see
    lo = total.RFQ(1, num-1) - ft.RFQ(1, num-1)
    res += hi * lo
    ft.adjust(num, 1)
print(res)