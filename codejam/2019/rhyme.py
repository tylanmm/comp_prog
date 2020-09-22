class TrieNode:
    def __init__(self):
        self.neighbors = [None] * 26
        self.count = 0
        self.end = False
    
    def add(self, word):
        self.count += 1
        if len(word) > 0:
            self.addNeighbor(word[0])
            self.neighbors[ord(word[0]) - ord('A')].add(word[1:])
        else:
            self.end = True
    
    def addNeighbor(self, letter):
        i = ord(letter) - ord('A')
        if self.neighbors[i] == None:
            self.neighbors[i] = TrieNode()
    
    def startCount(self):
        total = 0
        for n in self.neighbors:
            if n != None:
                total += n.countPairs(0)
        return total

    def countPairs(self, avail):
        for i in range(25, -1, -1):
            if self.neighbors[i] == None:
                self.neighbors.pop(i)
        self.neighbors = sorted(self.neighbors, key=lambda x: x.count)
        pairs = 0
        parentUsed = False
        pairFound = False
        for n in self.neighbors:
            if n != None:
                if n.end == n.count:
                    if not parentUsed:
                        parentUsed = True
                    elif not pairFound:
                        pairFound = True
                        pairs += 1
                elif not n.end and n.count == 1 and self.end:
                    if not parentUsed and not pairFound:
                        parentUsed = True
                        pairFound = True
                elif not n.end and n.count == 1 and avail > 0:
                    pairs += 1
                    avail -= 1
                else:
                    pairs += n.countPairs(parentUsed)
        
        return pairs

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        self.root.add(word[::-1])
    
    def countPairs(self):
        return self.root.startCount()

for i in range(int(input())):
    n = int(input())
    t = Trie()
    for _ in range(n):
        t.add(input())
    print('Case #%d: %d' % (i+1, t.countPairs()*2))