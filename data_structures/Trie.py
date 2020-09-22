class Trie:

    def __init__(self, words=None):
        self.next = [None]*26
        self.word = False
        if words:
            self.build(words)

    def build(self, words):
        for w in words:
            self.add(w)

    def add(self, word):
        if not word:
            self.word = True
            return
        n = ord(word[0]) - 97
        if not self.next[n]:
            self.next[n] = Trie()
        self.next[n].add(word[1:])

    def contains(self, word, isPrefix=False):
        if not word:
            return self.word or isPrefix
        n = ord(word[0]) - 97
        return False if not self.next[n] else self.next[n].contains(word[1:], isPrefix)

if __name__ == '__main__':
    words = ['hi', 'hell', 'hello', 'hello']
    tr = Trie(words)
    print(tr.contains('hello'))
    print(tr.contains('hel'))
    print(tr.contains('hel', True))