class MinHeap:

    def __init__(self, nums=None):
        """Takes an optional parameter nums and initializes the min heap.
        h: the 1-indexed heap
        loc: dictionary that stores the current index of each of the unique entries
        size: current number of elements
        """
        self.h = [None]
        self.loc = {}
        self.size = 0
        for n in nums:
            self.add(n)
    
    def add(self, num):
        """Inserts num into h using min heap algorithm.
        Place num at the end
        While num is less than its parent (at index i//2),
        Swap num with its parent

        Note: if num is already in the heap, it is not inserted.
        """
        if num in self.loc: return

        self.h.append(num)
        i = self.size + 1
        self.loc[num] = i
        while i//2 and self.h[i//2] > num:
            self.loc[num], self.loc[self.h[i//2]] = i//2, i
            self.h[i], self.h[i//2] = self.h[i//2], self.h[i]
            i //= 2
        self.size += 1
    
    def pop(self, ind=1):
        """Removes min element from the heap using min heap algorithm.
        Replace min element with the number at the end of the list
        While that element is bigger than either of its children,
        Swap that element with the smaller of the two children

        Note: takes optional arg ind to remove the element currently at position ind
        """

        if self.size == 0: return
        
        rem = self.h[ind]
        self.loc.pop(rem)

        self.h[ind], i = self.h[-1], ind
        self.loc[self.h[ind]] = ind
        self.h.pop()
        self.size -= 1

        while (i*2 <= self.size and self.h[i] > self.h[i*2]) or (i*2 + 1 <= self.size and self.h[i] > self.h[i*2 + 1]):
            if i*2 + 1 > self.size or self.h[i*2] < self.h[i*2 + 1]:
                self.loc[self.h[i]], self.loc[self.h[i*2]] = i*2, i
                self.h[i], self.h[i*2] = self.h[i*2], self.h[i]
                i = i*2
            else:
                self.loc[self.h[i]], self.loc[self.h[i*2 + 1]] = i*2 + 1, i
                self.h[i], self.h[i*2 + 1] = self.h[i*2 + 1], self.h[i]
                i = i*2 + 1

        return rem

    def remove(self, num):
        """Removes the specified number if in the heap, otherwise returns None"""

        return self.pop(self.loc[num]) if num in self.loc else None
    
    def __str__(self):
        return str(self.h[1:])

if __name__ == '__main__':
    heap = MinHeap([3, 5, 4, 7, 1, 10])
    print(heap)
    heap.pop()
    heap.remove(4)
    print(heap)
    heap.pop()
    print(heap)