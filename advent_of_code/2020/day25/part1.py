import sys
from math import log

with open(sys.argv[1]) as f:
    card, door = map(int, f.read().split('\n'))

def get_vals(subject):
    mod = 20201227
    vals = [1]
    for i in range(5000):
        vals.append((vals[-1]*subject) % mod)
    vals.pop(0)
    return vals

# (7 ^ loopsize) % 20201227 = key

card_vals = get_vals(card)
door_vals = get_vals(door)
for v in card_vals:
    if v in door_vals:
        print(v)
        break