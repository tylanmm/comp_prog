import sys

with open(sys.argv[1]) as f:
    seats = f.read().split()

hi = 0
for s in seats:
    row, seat = s[:7], s[7:]
    row = int(''.join(['0' if c == 'F' else '1' for c in row]), 2)
    seat = int(''.join(['0' if c == 'L' else '1' for c in seat]), 2)
    hi = max(hi, row * 8 + seat)
print(hi)