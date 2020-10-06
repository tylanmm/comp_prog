from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'Val: {self.val}'

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, val):
        self.size += 1
        if self.root is None:
            self.root = Node(val)
            return 
        
        curr = self.root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    return
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    return
            else:
                self.size -= 1
                return
    
    def find(self, val):
        curr = self.root
        while curr:
            if curr.val == val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False
    
    def __str__(self):
        return str(self.root)

if __name__ == '__main__':
    tree = BST()
    for _ in range(100000):
        tree.insert(randint(1, 100000))
    
    count = 0
    for _ in range(100000):
        count += tree.find(randint(1, 100000))
    print(count)