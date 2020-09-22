from sys import stdin

class BIT:
    def __init__(self, n):
        self.arr = [0]*(n+1)
        self.cap = n

    def update(self, key, val):
        while key <= self.cap:
            self.arr[key] += val
            key += key & -key
    
    def query(self, key):
        res = 0
        while key:
            res += self.arr[key]
            key ^= key & -key
        return res

n = int(stdin.readline())
bit = BIT(n)

for i in range(n):
    num = int(stdin.readline())
    # How many swaps?
    # The amount of numbers that have to pass from right to left
    # The amount of numbers that have to pass from left to right
    # The amount of numbers it will have to pass to get to its spot

    
    bit.update(num, 1)