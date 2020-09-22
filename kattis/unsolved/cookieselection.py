class SortedList:
    def __init__(self):
        self.nums = []
        self.size = 0
    
    def add(self, num):
        i = self.find(num)
        self.nums.insert(i, num)
        self.size += 1

    def find(self, num):
        lo = 0
        hi = self.size - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if self.nums[mid] == num:
                return mid
            elif self.nums[mid] > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def getMedian(self):
        med = self.nums.pop(self.size//2) if self.size % 2 else self.nums.pop(self.size//2)
        self.size -= 1
        return med

from sys import stdin, stdout

hold = SortedList()
for op in stdin.readlines():
    if op.strip() == '#':
        print(hold.getMedian())
    else:
        hold.add(int(op))