import sys

class Cup:

    def __init__(self, label):
        self.val = label
        self.next = None
    
    def __str__(self):
        return f'Cup(Label: {self.val}, Next: {self.next.val if self.next else None})'
    
    def __repr__(self):
        return self.__str__()


with open(sys.argv[1]) as f:
    first = list(map(int, f.read()))

cups = [Cup(i) for i in range(1000001)]

# set up initial connections
for i in range(len(first)-1):
    cups[first[i]].next = cups[first[i+1]]
cups[first[-1]].next = cups[len(first)+1]

# connect the rest of the cups
for i in range(len(first)+1, 1000000):
    cups[i].next = cups[i+1]
cups[-1].next = cups[first[0]]

def step(curr):
    # grab the three to be moved
    move = [curr.next, curr.next.next, curr.next.next.next]
    vals = {cup.val for cup in move}
    curr.next = curr.next.next.next.next

    # find the destination cup
    dest = curr.val - 1 + (1000000 if curr.val == 1 else 0)
    while dest in vals:
        dest -= 1
        if dest == 0:
            dest = 1000000

    # insert those three cups
    move[-1].next = cups[dest].next
    cups[dest].next = move[0]

curr = cups[first[0]]
for _ in range(10000000):
    step(curr)
    curr = curr.next

print(cups[1].next.val * cups[1].next.next.val)